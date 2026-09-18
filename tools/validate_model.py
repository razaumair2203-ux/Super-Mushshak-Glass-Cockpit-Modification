#!/usr/bin/env python3
"""Repository quality gate for the public Super Mushshak systems model.

Checks:
1. required machine-readable model files exist;
2. object-definition IDs are unique;
3. singular/plural ID references resolve to known objects;
4. typed-link source/target IDs resolve;
5. local Markdown links and image paths resolve;
6. no fragile external hot-linked images are embedded.

Uses Python standard library only.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model"

OBJECT_FILES = [
    "stakeholders.csv",
    "functions.csv",
    "requirements.csv",
    "interfaces.csv",
    "configurations.csv",
    "verification.csv",
    "issues.csv",
    "risks.csv",
    "decisions.csv",
    "evidence.csv",
    "claims.csv",
]

RELATION_FILES = [
    "traceability.csv",
    "links.csv",
]

MODEL_FILES = OBJECT_FILES + RELATION_FILES

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\((https?://[^)]+)\)", re.IGNORECASE)
HTML_SRC_RE = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.IGNORECASE)
EXTERNAL_HTML_IMG_RE = re.compile(
    r"<img\s+[^>]*src=[\"']https?://", re.IGNORECASE
)


def split_ids(value: str) -> list[str]:
    return [x.strip() for x in value.split(";") if x.strip()]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return rows, reader.fieldnames or []


def check_model(errors: list[str]) -> dict[str, str]:
    all_ids: dict[str, str] = {}
    tables: dict[str, tuple[list[dict[str, str]], list[str]]] = {}

    for name in MODEL_FILES:
        path = MODEL / name
        if not path.exists():
            fail(errors, f"Missing model file: {path.relative_to(ROOT)}")
            continue

        rows, fields = load_csv(path)
        tables[name] = (rows, fields)
        if not fields:
            fail(errors, f"No CSV header: {path.relative_to(ROOT)}")

    # Only object tables define identities. Traceability/links reuse identities.
    for name in OBJECT_FILES:
        if name not in tables:
            continue
        rows, fields = tables[name]
        if not fields:
            continue
        path = MODEL / name
        id_field = fields[0]

        for lineno, row in enumerate(rows, start=2):
            obj_id = (row.get(id_field) or "").strip()
            if not obj_id:
                fail(errors, f"{path.relative_to(ROOT)}:{lineno}: blank {id_field}")
                continue
            if obj_id in all_ids:
                fail(
                    errors,
                    f"Duplicate object ID {obj_id}: {all_ids[obj_id]} and "
                    f"{path.relative_to(ROOT)}:{lineno}",
                )
            else:
                all_ids[obj_id] = f"{path.relative_to(ROOT)}:{lineno}"

    # Validate reference fields in all tables. In object tables the first
    # column defines the object and is therefore not itself a reference.
    for name, (rows, fields) in tables.items():
        if not fields:
            continue
        path = MODEL / name
        defining_field = fields[0] if name in OBJECT_FILES else None

        for lineno, row in enumerate(rows, start=2):
            for field in fields:
                if field == defining_field:
                    continue

                if field.endswith("_ids"):
                    refs = split_ids(row.get(field, ""))
                elif field.endswith("_id"):
                    value = (row.get(field) or "").strip()
                    refs = [value] if value else []
                else:
                    refs = []

                for ref in refs:
                    if ref not in all_ids:
                        fail(
                            errors,
                            f"{path.relative_to(ROOT)}:{lineno}: "
                            f"{field} references unknown ID {ref}",
                        )

    return all_ids


def clean_link(raw: str) -> str:
    value = raw.strip()
    # Markdown may append a quoted title after whitespace.
    if value.startswith("<") and ">" in value:
        value = value[1:value.index(">")]
    elif " " in value:
        value = value.split(" ", 1)[0]
    return value.split("#", 1)[0].split("?", 1)[0]


def is_external(value: str) -> bool:
    lower = value.lower()
    return lower.startswith(("http://", "https://", "mailto:", "data:"))


def check_markdown(errors: list[str]) -> None:
    md_files = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]

    for path in md_files:
        if not path.exists():
            fail(errors, f"Missing Markdown file: {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")

        if EXTERNAL_HTML_IMG_RE.search(text) or MARKDOWN_IMAGE_RE.search(text):
            fail(
                errors,
                f"{path.relative_to(ROOT)}: contains an external hot-linked image; "
                "link to the source or use a licence-cleared local asset instead",
            )

        candidates = [m.group(1) for m in MARKDOWN_LINK_RE.finditer(text)]
        candidates += [m.group(1) for m in HTML_SRC_RE.finditer(text)]

        for raw in candidates:
            link = clean_link(raw)
            if not link or is_external(link) or link.startswith("#"):
                continue

            target = (path.parent / link).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}: local link escapes repository: {raw}",
                )
                continue

            if not target.exists():
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}: broken local link/image: {raw}",
                )


def main() -> int:
    errors: list[str] = []
    all_ids = check_model(errors)
    check_markdown(errors)

    if errors:
        print("QUALITY GATE: FAIL")
        for item in errors:
            print(f" - {item}")
        return 1

    prefixes: dict[str, int] = {}
    for obj_id in all_ids:
        prefix = obj_id.split("-", 1)[0]
        prefixes[prefix] = prefixes.get(prefix, 0) + 1

    print("QUALITY GATE: PASS")
    print(f"Resolved model objects: {len(all_ids)}")
    print("Object counts:")
    for prefix in sorted(prefixes):
        print(f" - {prefix}: {prefixes[prefix]}")
    print("ID references: resolved")
    print("Local Markdown links/images: resolved")
    print("External hot-linked images: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
