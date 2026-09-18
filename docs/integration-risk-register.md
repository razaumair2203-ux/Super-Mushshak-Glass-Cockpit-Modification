# Integration Risk Register

This is a **retrospective, evidence-bounded risk view** of the retrofit. It is not represented as an original programme FHA, FMEA or formal safety assessment.

The purpose is to show how real aircraft-integration risks emerged across disciplines and how they were controlled through interface definition, configuration control, troubleshooting and re-verification.

| Risk | Evidence-backed engineering concern | Control / response | Public status |
|---|---|---|---|
| **RSK-001 — electrical power / transients** | Installed avionics experienced a power/internal-voltage-related discrepancy after earlier sorties | aircraft-power checks, OEM troubleshooting, hardware/configuration action, re-test/re-flight | return to flight evidenced; detailed root cause not public |
| **RSK-002 — configuration restoration** | replacement hardware required deliberate restoration of settings/databases | restore configuration data before functional re-test | reverified; exact versions withheld |
| **RSK-003 — cross-domain interaction** | radio PTT activity coincided with short-duration engine-indication fluctuation | capture condition, isolate interface path, OEM investigation, require verification before closure | final corrective-action closure not reconstructed |
| **RSK-004 — high-dynamic attitude behaviour** | ADAHRS compare/attitude-recovery behaviour appeared during high-rate manoeuvre/spin-recovery testing | capture observation, obtain OEM functional explanation, assess in training/test context | characterised; final acceptance closure not reconstructed |
| **RSK-005 — retained-avionics interoperability** | NAV/transponder/audio functions created configuration-specific interface burden | define interfaces, coordinate with OEM, perform bench/installed checks | integration activity evidenced; detailed implementation withheld |
| **RSK-006 — supportability/AOG exposure** | LRU failure or replacement could create downtime and configuration-restoration burden | spares, OEM repair/support loop, controlled restoration | qualitative supportability response evidenced |

Machine-readable source: [model/risks.csv](../model/risks.csv).

## Why this matters

The risk pattern demonstrates that the programme was not a display substitution. The dominant integration risks crossed **electrical, sensing, digital avionics, HMI, configuration-data and lifecycle-support boundaries**.

That is the systems-engineering problem: a functionally capable COTS suite can still fail at aircraft level if power quality, interfaces, as-tested configuration, human interaction and supportability are not controlled together.

## Boundary

- No probability or severity numbers are invented.
- No formal hazard classification is claimed where the surviving archive does not support one.
- No pin-level, harness-route or controlled implementation detail is published.
- An observed discrepancy is not called closed unless the public-safe evidence supports closure.
