#!/usr/bin/env python3
"""Export the public systems model as graph-ready JSON.

This does not create new engineering facts. It serializes the controlled CSV
objects and typed links into a portable digital-thread representation.
"""

from __future__ import annotations

import argparse
import csv
import json
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


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(ROOT / "generated" / "digital-thread.json"),
        help="Output JSON path",
    )
    args = parser.parse_args()

    nodes: list[dict[str, object]] = []
    known_ids: set[str] = set()

    for name in OBJECT_FILES:
        rows = read_rows(MODEL / name)
        for row in rows:
            first_key = next(iter(row))
            obj_id = row[first_key].strip()
            known_ids.add(obj_id)
            nodes.append(
                {
                    "id": obj_id,
                    "object_type": name.removesuffix(".csv"),
                    "source_file": f"model/{name}",
                    "attributes": {k: v for k, v in row.items() if k != first_key},
                }
            )

    edges: list[dict[str, str]] = []
    for row in read_rows(MODEL / "links.csv"):
        source = row["source_id"].strip()
        target = row["target_id"].strip()
        if source not in known_ids or target not in known_ids:
            raise SystemExit(
                f"Unresolved typed link: {source} --{row['relation']}--> {target}"
            )
        edges.append(
            {
                "source": source,
                "relation": row["relation"].strip(),
                "target": target,
                "evidence_ids": row.get("evidence_ids", "").strip(),
                "notes": row.get("notes", "").strip(),
            }
        )

    payload = {
        "schema": "super-mushshak-public-digital-thread/v1",
        "provenance": (
            "Retrospective public-safe export. Nodes and edges are serialized "
            "from the controlled CSV model; no new aircraft detail is inferred."
        ),
        "counts": {"nodes": len(nodes), "edges": len(edges)},
        "nodes": nodes,
        "edges": edges,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(nodes)} nodes and {len(edges)} edges to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
