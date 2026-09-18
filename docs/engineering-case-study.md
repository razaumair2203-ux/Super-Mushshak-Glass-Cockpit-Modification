# Systems Engineering Case Study

## Engineering problem

Modernising a legacy trainer with a glass cockpit is an **aircraft retrofit programme**, not a display-swap exercise.

The design problem spans several coupled domains:

- flight-state sensing and presentation;
- engine/airframe sensing and indication;
- navigation and communication integration;
- retained avionics;
- aircraft electrical supply, protection and transient behaviour;
- cockpit HMI, audio and alerting;
- physical installation and complete modification-harness change;
- software, settings and databases;
- maintainability, spares and OEM support;
- installed-aircraft verification, flight test and customer evaluation.

This coupling is the reason a functionally capable COTS avionics suite can still create aircraft-level integration risk.

## Engineering responsibility represented

The reconstruction represents **lead systems-engineering and hands-on avionics integration/test responsibility** across architecture, interface definition, installation, troubleshooting, configuration restoration, OEM coordination, flight-test feedback and customer evaluation.

The role statement is kept separate from the evidence model: technical claims still require project, OEM, public-source or derived evidence.

## Context and functional architecture

![System context](../assets/system-context.svg)

![Functional decomposition](../assets/functional-decomposition.svg)

The model begins with the aircraft and stakeholders, then decomposes the retrofit into functions. Equipment is introduced only at configuration level. This prevents a vendor reference architecture from being mistaken for the aircraft design.

## Baseline characterisation

A period first-modification completion report contains detailed analysis of the legacy cockpit, avionics, electrical and mechanical installation. The report is not published because it contains security markings and implementation detail.

Only high-level facts needed for the public engineering model are retained:

- the baseline used conventional flight/engine instruments and separate avionics functions;
- replacement required analysis of instrument/sensor interfaces;
- electrical capacity and protection were integration constraints;
- panel/equipment installation and cabling were part of the modification problem;
- multiple architectural approaches were considered.

Exact baseline equipment lists, antenna locations, load tables, detailed installation data and controlled markings remain outside this repository.

## Architecture alternatives and configuration identity

### Dynon SkyView

This branch has the strongest surviving installed-aircraft evidence: cockpit and in-flight photographs, troubleshooting correspondence, interface/configuration exchanges, flight-test feedback and customer-evaluation evidence.

### Garmin G900X/G950 family

This is a separate prototype/evaluation path. OEM documentation supports the family’s modular integrated-flight-deck architecture, but the exact public aircraft-installed baseline is only partially reconstructed.

### Garmin G3X comparison

The G3X appears in period comparison material. It is retained as a **candidate/trade-study artefact**, not relabelled as the G900X/G950 aircraft configuration.

The rule is simple: **architecture similarity does not erase configuration identity**.

## Interface engineering

The surviving archive supports aircraft-level interface work involving aircraft electrical power/protection, flight-state sensing, engine/airframe sensing, NAV/COM integration, retained navigation, transponder, audio/alerting, software/settings/data and maintenance/OEM support.

The public interface register deliberately omits exact pins and wiring.

See [Interface control](interface-control.md).

## Electrical integration and discrepancy investigation

The early Dynon configuration flew before a later engine-start event produced a display internal-voltage/power-related discrepancy. The surviving troubleshooting chain shows a real aircraft integration process: symptom capture, aircraft-power checks, OEM support, hardware replacement, restoration of configuration data and return to flight.

The public case study does not publish connector/pin information from those exchanges.

## Configuration restoration

Replacement displays did not mean “swap and go”. Settings and databases had to be restored deliberately. The evidence also distinguishes data that had to be loaded per display from settings recoverable from backup.

That makes hardware, software/settings and databases all part of the **as-tested configuration**, not administrative metadata.

## Retained-system and cross-domain behaviour

The record includes NAV interface work, transponder/audio questions and later cross-domain observations in which a radio-transmit action coincided with engine-indication fluctuation.

The final closure of that later interference issue is **not publicly reconstructed** and is not claimed.

## Flight-test and customer-evaluation loop

The project progressed from installed prototype operation to continued flight feedback, performance testing and customer evaluation.

A later high-rate-manoeuvre/spin-related ADAHRS observation received an OEM functional explanation. The repository records the observation and explanation but does not invent a final acceptance disposition.

The Qatar evaluation record supports repeated sorties, including night operation. That is validation context; it is not presented as certification approval.

## Maintainability and support

The team explicitly considered how failed LRUs would be repaired, whether spares should support aircraft-on-ground recovery and how configuration would be restored after replacement.

This expands the architecture trade space from acquisition capability to **availability, repair concept, logistics and configuration sustainment**.

## Qualification and certification fit

The archive includes questions concerning environmental qualification, TSO status and customer/type-acceptance suitability. Functional flight performance and acceptance/certification suitability are therefore represented as separate engineering concerns.

The repository does not claim certification status beyond what the source record supports.

## Evidence-to-model chain

The retrospective digital thread is:

**evidence → claim → requirement → function → interface → configuration → verification / issue → decision**

Each object has a stable ID under [model](../model/README.md).

## What is deliberately not claimed

This case study does not claim that:

- the public diagrams are original programme drawings;
- formal SysML/MBSE tooling was used during the original programme;
- the G3X comparison candidate was the G900X/G950 prototype;
- generic Garmin interconnect diagrams reproduce the Super Mushshak wiring;
- every historical discrepancy has a surviving closure record;
- customer evaluation proves certification;
- later export contracts were caused by one early prototype or one engineer;
- private correspondence or controlled source documents are public-release material.

The engineering record is valuable because the **boundaries and unknowns are explicit**.
