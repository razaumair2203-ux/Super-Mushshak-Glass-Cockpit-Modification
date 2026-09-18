# Retrospective Systems Model

This directory is the machine-readable core of the public systems-engineering reconstruction.

The model is intentionally **tool-agnostic**. Stable IDs and explicit links matter more than a particular MBSE application.

## Object sets

| File | Namespace | Purpose |
|---|---|---|
| stakeholders.csv | STK-### | actors / needs around the system of interest |
| functions.csv | FUN-### | equipment-independent aircraft-retrofit functions |
| requirements.csv | REQ-### | retrospectively normalised requirements / constraints |
| interfaces.csv | IF-### | evidence-backed public logical interfaces |
| configurations.csv | CFG-### / CMP-### | distinct historical configuration states / comparison artefacts |
| verification.csv | VER-### | installed-aircraft test, evaluation or architecture-review events |
| issues.csv | ISS-### | discrepancies and their evidence-bounded status |
| decisions.csv | DEC-### | recovered engineering decisions / rationale |
| evidence.csv | E-## | source/evidence register |
| claims.csv | CLM-### | controlled public technical claims |
| traceability.csv | REQ-### keyed | compact requirements-to-functions/interfaces/config/V&V view |
| links.csv | mixed | typed graph edges between model objects |

## Core modelling rules

1. No object is added solely because it would be normal for an aircraft of this type.
2. Generic OEM architecture is not treated as proof of the exact aircraft installation.
3. G3X comparison material is not merged into the G900X/G950 prototype/evaluation identity.
4. Verification evidence is tied to the configuration state in which it was observed.
5. Discrepancy discussion is not automatically treated as discrepancy closure.
6. Unknown values stay unknown.
7. Public objects omit controlled implementation detail.
8. Every derived object identifies an evidence basis.
9. Retired evidence IDs are not silently reused.

## Evidence states

The model uses **Observed**, **Documented**, **Derived**, **Partially reconstructed** and **Not reconstructed** as controlled status language.

## Configuration rule

A configuration is more than hardware. Where evidenced, the state includes LRU/display identity, interface equipment, software/settings, navigation/terrain databases, sensor/monitoring configuration, physical installation/harness state and as-tested evidence.

A result from one state does not automatically verify another.

## Relationship to formal MBSE

The CSV objects correspond conceptually to requirements, functions, blocks/interfaces, configurations, verification cases, issues, decisions and evidence that could be implemented in SysML/Capella/Cameo or a requirements tool.

This repository does **not** claim that these model artefacts existed in the original programme. They are a retrospective transformation of surviving evidence.

The quality criterion is **identity + evidence + traceability + configuration specificity**, not model density.
