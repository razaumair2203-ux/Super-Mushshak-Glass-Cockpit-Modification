# Systems-Engineering Method

This case study is organised around the aircraft-level engineering lifecycle rather than around isolated equipment features.

![Systems-engineering lifecycle](../assets/systems-engineering-lifecycle.svg)

## 1. Need and constraints

The retrofit problem was to modernise a legacy trainer while preserving aircraft suitability for training, acceptance, maintainability and fleet support. The engineering boundary therefore extended beyond cockpit displays to sensing, retained avionics, aircraft electrical integration, complete harness changes, configuration data, test evidence and lifecycle support.

## 2. Requirement normalisation

The surviving archive is transformed into public, testable requirement statements only where the evidence supports them. Requirements currently cover:

- primary flight information;
- engine/airframe information;
- NAV/COM integration;
- electrical integration;
- configuration restoration;
- retained-system interfaces;
- installed-aircraft verification and discrepancy closure;
- maintainability and OEM support;
- qualification/certification fit;
- failure response and redundancy;
- HMI/training suitability;
- configuration identity and evidence control.

The machine-readable source is [model/requirements.csv](../model/requirements.csv).

## 3. Architecture and alternatives

Architecture is modelled as a set of aircraft-level functions and logical interfaces. The important configuration rule is that the **Dynon SkyView** path and the **Garmin G900X/G950-family** path remain separate. A Garmin G3X comparison deck is retained as trade-study evidence only.

The public architecture intentionally omits exact wiring, pins, harness routing, connector detail and precise installation locations.

## 4. Integration

Integration is treated as a multi-domain activity:

- sensing and flight-state data;
- engine/airframe indication;
- NAV/COM and retained avionics;
- aircraft electrical power and protection;
- audio/alerting;
- software, settings and databases;
- physical installation and harness change;
- maintainability and LRU replacement.

This is why the programme is represented as an **aircraft retrofit**, not a display replacement.

## 5. Verification and discrepancy closure

Verification follows a closed-loop rule:

**identified configuration → installed check / flight event → observation → analysis → disposition → configuration update → re-verification**

Evidence is not generalized across configuration states. A result observed in one hardware/software/database baseline is not claimed for another unless the record supports that link.

See [Verification and flight test](verification-and-flight-test.md) and [model/verification.csv](../model/verification.csv).

## 6. Validation / customer evaluation

Customer and field evaluation is treated as system validation context rather than as a substitute for technical verification. The Qatar evaluation record demonstrates repeated operational flying while separate certification/acceptance questions remained open.

## 7. Configuration and evidence control

Every public engineering claim is classified against one of four evidence classes:

1. **direct project evidence** — period photographs, correspondence, test/status records;
2. **OEM/reference evidence** — vendor manuals and architecture documentation;
3. **derived engineering artefact** — retrospective requirement, interface, architecture or traceability view;
4. **public programme evidence** — public contract/operator reporting used for downstream programme context.

Unknown values remain unknown. Generic OEM architecture is not promoted into aircraft-specific installation evidence.

## 8. Digital-thread continuation

The current follow-on work converts the historical archive into stable model objects with IDs and links across requirements, interfaces, configurations, verification records, decisions and evidence. That structure is the foundation for progressively higher-fidelity digital-twin work where releasable data exists.

See [Digital twin follow-on](digital-twin.md).
