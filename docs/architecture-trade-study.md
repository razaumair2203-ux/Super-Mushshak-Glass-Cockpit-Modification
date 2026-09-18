# Architecture Trade Study

The glass-cockpit work evolved through multiple candidate configurations. Surviving 2010–12 records include formal comparisons of **Dynon SkyView**, **Garmin G950/G900-family solutions**, and at some stages **Garmin G3X** material.

This page does not recreate a proprietary vendor block diagram. Instead, it records the **aircraft-level decision dimensions that are evidenced in the archive**.

## Principal public tracks

### Dynon SkyView prototype track

Evidence includes:

- original photographs of the first modified cockpit;
- direct OEM technical correspondence;
- integration and troubleshooting questions;
- database/configuration work;
- flight-test feedback and first-sortie correspondence;
- later configuration/equipment follow-up.

### Garmin G900 / G950-family track

Evidence includes:

- period G950/G900-family technical and quotation material;
- package/component-definition work;
- architecture comparison;
- reliability, maintainability and redundancy questions;
- customer-facing evaluation/presentation support.

### Naming note

Different surviving records use G950/G900-family terminology and also reference G3X during comparative/prototype work. The project was evolving. This repository therefore uses **Garmin G900/G950-family track** as a conservative public label and does not claim an exact sub-variant unless a specific surviving record supports it.

## Trade-space dimensions

| Dimension | Systems-engineering question |
|---|---|
| Functional coverage | Which flight, engine, navigation, communication and warning functions are provided? |
| Legacy compatibility | What existing aircraft equipment can remain, and what requires replacement or interface adaptation? |
| Sensor integration | What sensing/transducers and conditioning are required? |
| Electrical integration | Can the aircraft power system support the configuration with adequate margin and protection? |
| Physical installation | What equipment, panel, cabling and installation burden is introduced? |
| Data/interface architecture | Which digital/analog interfaces are required and where are integration risks concentrated? |
| HMI / training role | Is information presented clearly for a basic-training cockpit and instructor/student use? |
| Alerts and backup | How are warnings, abnormal indications and fallback information handled? |
| Reliability / redundancy | How tolerant is the architecture of individual equipment or display failures? |
| Qualification | What environmental/airworthiness evidence exists and what additional verification is required? |
| Maintainability | How is troubleshooting, replacement, spares support and post-installation test handled? |
| OEM support | What engineering support is available during integration and lifecycle operation? |
| Upgradeability | Can third-party equipment or future configuration changes be incorporated without redesigning the whole cockpit? |
| Cost / schedule | What is the total aircraft-level integration burden, not merely equipment purchase price? |

## What the trade study demonstrates

The significant engineering result is the **method**, not an invented vendor “winner”.

The programme compared alternative architectures against aircraft constraints, training needs, integration risk, supportability and lifecycle considerations. A signed 2010 systems-engineering study and a later comparative presentation authored by the programme systems engineer provide direct evidence of this work.

Exact internal load budgets, LRU locations, proprietary diagrams, pinouts, harness routes and controlled documents are intentionally excluded from the public repository.
