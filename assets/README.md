# Visual Asset Provenance

The visual layer is split into two evidence classes:

1. **authentic project imagery** — original photographs from the retrofit/test archive, processed only for public release; and
2. **independent public media** — external photographs or reporting used only as contextual corroboration, with licence/source controls.

No synthetic aircraft, cockpit, equipment, person or test imagery is permitted.

| File | Source | Public processing | Evidentiary use |
|---|---|---|---|
| dynon-cockpit-prototype-sanitized.jpg | original Dynon prototype cockpit photograph | crop/resize/quality adjustment + targeted redaction where required | installed cockpit/configuration context visible in image |
| dynon-pfd-inflight-sanitized.jpg | original in-flight project photograph | resize/quality adjustment only | installed-aircraft display operation visible in image |
| qaef-ground-evaluation-sanitized.jpg | original customer-evaluation-period project photograph | conservative public-release processing | customer/field-evaluation context |
| system-context.svg | retrospective systems model | responsive native vector | system boundary / actor context |
| functional-decomposition.svg | retrospective systems model | responsive native vector | aircraft-level functional hierarchy |
| systems-engineering-lifecycle.svg | retrospective V-model | responsive native vector | definition ↔ verification lifecycle |
| mbse-system-architecture.svg | retrospective logical model | responsive native vector | public-safe logical domains / interfaces |
| mbse-verification-thread.svg | retrospective assurance model | responsive native vector | evidence-to-verification and discrepancy closure |
| configuration-evolution.svg | retrospective configuration model | responsive native vector | prototype/configuration separation |
| traceability-matrix.svg | retrospective recruiter-facing traceability view | responsive native vector | readable representative closure slice |
| programme-context.svg | retrospective programme-context view | responsive native vector | later public programme context without causal attribution |
| digital-twin-roadmap.svg | retrospective digital-engineering view | responsive native vector | implemented digital thread vs future executable twin |

## Authentic-image processing rule

Permitted processing is limited to:

- crop and resize;
- exposure / contrast / white-balance correction;
- sharpening and noise reduction;
- narrowly targeted redaction of security markings, private personal information, unnecessary organisational identifiers/logos, or precise location identifiers that add no engineering value.

Processing must **not** add, replace, reconstruct or generatively alter aircraft structure, cockpit equipment, people, scenery, displays or backgrounds.

## Independent public media rule

External media is treated separately from the project archive.

- Copyrighted news/operator photographs remain **source-linked**, not copied into this repository.
- A reusable photograph may be embedded when the licence explicitly permits it and attribution is preserved.
- The README currently uses the Wikimedia Commons photograph **“PAC Super Mushshak cockpit.jpg”** (Mztourist, Dubai Airshow 2017) under **CC BY-SA 4.0** as independent contextual imagery.
- The external photograph is never labelled as project evidence and is not used to infer hidden wiring, prototype identity or test results.
- Public reporting may corroborate programme dates, quantities or configuration labels only to the extent the source actually states them.

## Diagram quality rule

The systems-engineering SVGs are **derived retrospective views**, not original period drawings. They are generated as responsive vectors with explicit `viewBox` geometry so GitHub rendering does not crop boxes or text.

Diagram connectors are deliberately orthogonal/minimal. Dense relationship data stays in the machine-readable CSV model rather than being forced into unreadable “spaghetti” diagrams.

The source of truth for IDs and relationships is under `/model`; diagrams are presentation views of that model.

**No synthetic aircraft/cockpit/test imagery is used anywhere in the visual evidence chain.**
