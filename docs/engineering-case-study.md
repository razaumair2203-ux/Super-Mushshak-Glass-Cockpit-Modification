# Systems Engineering Case Study

## Engineering problem

Modernising a legacy trainer with a glass cockpit is an **aircraft retrofit programme**, not a display-swap exercise.

The design problem spans coupled domains: flight-state sensing/presentation; engine/airframe sensing/indication; navigation and communication integration; retained avionics; aircraft electrical supply/protection/transients; cockpit HMI/audio/alerting; physical installation and the modification harness; software/settings/databases; maintainability; installed-aircraft verification; flight test; and customer evaluation.

This coupling is the reason a functionally capable COTS avionics suite can still create aircraft-level integration risk.

## Lead Systems Engineer responsibility represented

The programme lead identifies his role on the retrofit as **Lead Systems Engineer**.

The public-safe responsibility statement covers:

- system boundary, architecture alternatives and cross-domain integration;
- glass-cockpit integration with revised sensing, aircraft electrical power/protection, retained avionics and the complete modification harness;
- prototype ground/flight test, discrepancy investigation and re-verification;
- hardware/configuration restoration after equipment change;
- OEM technical coordination;
- customer-evaluation support.

The role statement is controlled as **E-25**. It is intentionally separated from technical proof: individual engineering claims still require their own evidence.

## Context and functional architecture

![System context](../assets/system-context.svg)

![Functional decomposition](../assets/functional-decomposition.svg)

The model begins with aircraft/stakeholder context and equipment-independent functions. Equipment is introduced only at configuration level. This prevents a vendor reference architecture from being mistaken for the aircraft design.

## Baseline characterisation

A non-public period first-modification report contains detailed analysis of the legacy cockpit, avionics, electrical and mechanical installation. The source document is not republished.

Only high-level facts needed for the public engineering model are retained:

- the baseline used conventional flight/engine instruments and separate avionics functions;
- replacement required analysis of instrument/sensor interfaces;
- electrical capacity/protection were integration constraints;
- panel/equipment installation and cabling were part of the modification problem;
- multiple architectural approaches were considered.

Exact baseline equipment lists, antenna locations, load tables and detailed installation data remain outside the repository.

A separate retrospective programme-lead scope statement identifies **sensor-suite replacement and the complete modification wiring-harness change** as part of the executed retrofit scope. That statement is explicitly identified as E-24 rather than being presented as a period drawing.

## Architecture alternatives and configuration identity

### Dynon SkyView

This branch has the strongest surviving installed-aircraft evidence: cockpit/in-flight photographs, troubleshooting correspondence, interface/configuration exchanges, flight-test feedback and customer-evaluation evidence.

### Garmin G900X/G950 family

This is a separate prototype/evaluation path. OEM documentation supports the family’s modular integrated-flight-deck architecture, but the exact public aircraft-installed baseline is only partially reconstructed.

### Garmin G3X comparison

The G3X appears in period comparison material. It is retained as a **candidate/trade-study artefact**, not relabelled as the G900X/G950 aircraft configuration.

**Architecture similarity does not erase configuration identity.**

## Interface engineering

The surviving archive supports aircraft-level interface work involving electrical power/protection, flight-state sensing, engine/airframe sensing, NAV/COM, retained navigation, transponder, audio/alerting, software/settings/data and maintenance/OEM support.

The public interface register deliberately omits exact pins and wiring.

See [Interface control](interface-control.md).

## Integration-risk control

The retrospective risk register exposes the most important evidence-backed integration risks without inventing probability/severity values:

- aircraft power/transient behaviour;
- configuration restoration after LRU change;
- radio/engine-indication cross-domain interaction;
- high-dynamic attitude-reference behaviour;
- retained-avionics interoperability;
- supportability / aircraft-on-ground exposure.

See [Integration risk register](integration-risk-register.md).

## Electrical integration and discrepancy investigation

The early Dynon configuration flew before a later engine-start event produced a display internal-voltage/power-related discrepancy. The surviving troubleshooting chain shows a real aircraft integration process: symptom capture, aircraft-power checks, OEM support, hardware replacement, restoration of configuration data and return to flight.

Connector/pin troubleshooting detail remains outside the public repository.

## Configuration restoration

Replacement displays did not mean “swap and go”. Settings and databases had to be restored deliberately. The evidence distinguishes data that had to be loaded per display from settings recoverable from backup.

Hardware, software/settings and databases therefore form part of the **as-tested configuration**.

## Cross-domain behaviour

The record includes NAV interface work, retained-avionics questions and later cross-domain observations in which a radio-transmit action coincided with engine-indication fluctuation.

The final closure of that later interference issue is **not publicly reconstructed** and is not claimed.

## Flight-test and customer-evaluation loop

The project progressed from installed prototype operation to continued flight feedback, performance testing and customer evaluation.

A later high-rate-manoeuvre/spin-related ADAHRS observation received an OEM functional explanation. The repository records the observation and explanation but does not invent a final acceptance disposition.

The customer-evaluation record supports repeated sorties, including night operation. That is validation context; it is not presented as certification approval.

## Maintainability and support

The team explicitly considered failed-LRU repair, spare units for aircraft-on-ground recovery and configuration restoration after replacement.

This expands the trade space from acquisition capability to **availability, repair concept, logistics and configuration sustainment**.

## Qualification and acceptance fit

The archive includes questions concerning environmental qualification, TSO status and customer/type-acceptance suitability. Functional flight performance and acceptance/certification suitability are represented as separate engineering concerns.

The repository does not claim certification status beyond what the source record supports.

## Requirements-to-evidence closure

The public model currently contains:

- **6 stakeholders**
- **14 retrospectively normalised requirements**
- **12 aircraft-level functions**
- **11 logical interfaces**
- **6 configuration/comparison states**
- **8 verification records**
- **4 discrepancy records**
- **6 evidence-bounded integration risks**
- **8 recovered decision records**
- **25 evidence records**
- **12 controlled public claims**

The model is intentionally compact. Depth comes from traceability and configuration specificity, not from inflating object counts.

The evidence-to-model chain is:

**evidence → claim → requirement → function → interface → configuration → verification / issue / risk → decision**

## International programme outcome

Public reporting documents a four-customer 2016–2017 export sequence totalling **80 aircraft**: Nigeria 10, Qatar 8, Türkiye 52 and Azerbaijan 10.

Independent configuration reporting identifies **Dynon** on Nigeria and **Garmin 950** on Qatar and Türkiye.

Public commercial reporting places the Nigeria order at an estimated **US$10.2M** and the Türkiye agreement at approximately **US$50M**. Those two values alone exceed **US$60M**; no value is invented for Qatar or Azerbaijan.

This demonstrates that the retrofit sat on a commercially significant international product path. It does not prove sole causation by one engineer or one early prototype.

## Systems-engineering conclusion

The strongest engineering result is not “a glass display was installed.” It is that the aircraft modification was managed as a coupled system:

**need and constraints → architecture alternatives → aircraft-level interfaces → physical/electrical integration → configuration control → installed verification → discrepancy closure/re-test → customer validation → supportability and later product continuity**

That lifecycle is the core of this case study.

## What is deliberately not claimed

This case study does not claim that:

- public diagrams are original programme drawings;
- formal SysML/MBSE tooling was used during the original programme;
- the G3X comparison candidate was the G900X/G950 prototype;
- generic Garmin interconnect diagrams reproduce the Super Mushshak wiring;
- every historical discrepancy has a surviving closure record;
- customer evaluation proves certification;
- later export contracts were caused by one early prototype or one engineer;
- private correspondence or non-public source documents are public-release material.

The technical value comes from **controlled identity, traceability, evidence-backed risk handling and explicit unknowns**.
