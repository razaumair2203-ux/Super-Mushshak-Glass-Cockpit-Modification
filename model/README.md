# Retrospective Systems Model

This directory is the machine-readable core of the retrospective MBSE reconstruction.

The model is intentionally **tool-agnostic**. It can be migrated later into a formal requirements/MBSE environment, but the important property is already present: stable IDs and traceability.

## Files

- requirements.csv — retrospectively normalised requirements / constraints;
- interfaces.csv — logical interfaces supported by the evidence;
- configurations.csv — distinct historical configuration states;
- verification.csv — installed-aircraft verification / discrepancy events;
- decisions.csv — recovered engineering decision records;
- traceability.csv — links requirements to interfaces, configurations, verification and evidence.

## Modelling rules

1. No object is added solely because it would be normal for an aircraft of this type.
2. Generic OEM architecture is not treated as proof of the exact aircraft installation.
3. G3X comparison material is not merged into the G900X/G950 prototype identity.
4. Test evidence is tied to the configuration state in which it was observed.
5. Unknown values stay unknown.
6. Public objects omit controlled implementation details.
7. Every derived object must identify its evidence basis.

## Relationship to SysML / MBSE

The CSV objects correspond conceptually to requirement, block/interface, configuration, verification and decision elements that could be implemented in SysML/Capella/Cameo or linked to a requirements tool.

This repository does not pretend that these CSV files are original programme artefacts. They are a **retrospective engineering model generated from the surviving project evidence**.
