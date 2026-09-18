# Super Mushshak Glass-Cockpit Retrofit

**Lead systems engineering · avionics integration · prototype V&V · aircraft-level test · customer evaluation · digital-thread reconstruction**

![Original Dynon SkyView prototype cockpit](assets/dynon-cockpit-prototype-sanitized.jpg)

*Original project photograph of the Dynon SkyView prototype cockpit; cropped/redacted only where needed for public release.*

This repository reconstructs my work as **lead systems engineer / avionics integration engineer** on the Super Mushshak glass-cockpit retrofit. The modification was an aircraft-level integration problem, not a display replacement: it included the aircraft sensor suite, glass displays, navigation/communication equipment, electrical integration, the complete aircraft wiring-harness change associated with the modification, software/settings/databases, maintainability, OEM coordination, ground and flight test, and customer evaluation.

The reconstruction is deliberately evidence-led. Historical project material, original photographs, OEM documentation and public programme records are separated from retrospective MBSE derivations so that a reviewer can see **what was observed, what was engineered, what was verified, and what is inferred**.

## System-level scope

- replacement/integration of flight-state and engine/airframe sensing;
- PFD/MFD/EMS functions, cockpit HMI and associated controls;
- Garmin 430-family navigation/communication integration on the Dynon track;
- ARINC-429 and other avionics-interface work;
- aircraft electrical integration, protection and transient troubleshooting;
- complete aircraft harness / installation changes associated with the modification;
- avionics databases, software/settings and configuration restoration;
- maintainability, spares, LRU replacement and OEM support considerations;
- installed-aircraft functional checks, flight-test feedback, discrepancy resolution and re-test;
- customer-facing technical evaluation and prototype support.

## System architecture

![Public-safe logical architecture](assets/mbse-system-architecture.svg)

This is a **retrospective public-safe logical architecture** derived from project evidence. It intentionally omits pinouts, exact harness routing, controlled drawings and precise equipment locations.

## Prototype identities — kept deliberately separate

### Dynon SkyView prototype

The strongest surviving evidence is on the Dynon track: original cockpit and in-flight photographs, direct OEM engineering exchanges, installed-aircraft troubleshooting, ARINC/GNS integration, database/configuration activity, and repeated flight-test feedback.

### Garmin G900X / G950-family prototype and evaluation track

A separate Garmin G900X/G950-family track was developed/evaluated. Surviving material includes G900X/G950 architecture documentation, a Qatar-focused G950 technical presentation, and later G900X configuration-mode correspondence. Garmin's own installation material describes the family as a modular LRU-based integrated avionics architecture; the generic OEM architecture is used here only as reference evidence, not silently relabelled as the exact aircraft wiring.

### Garmin G3X comparative material

A 2012 comparison presentation evaluates **Dynon SkyView against Garmin G3X**. That deck is retained as evidence of trade-study practice only. It is **not relabelled as the G900X/G950 prototype**, because doing so would merge distinct configurations.

![Configuration evolution](assets/configuration-evolution.svg)

This configuration-state view is central to the retrospective model: evidence from one prototype, hardware/software/database state or vendor candidate is not silently applied to another.

## From evidence to verified aircraft

![Evidence-to-verification digital thread](assets/mbse-verification-thread.svg)

The historical engineering loop is reconstructed as:

**evidence → requirement/constraint → interface → configuration → verification → decision/disposition → configuration update → re-test**

The model ties verification to the configuration in which it occurred rather than treating one test result as evidence for every later hardware/software/database state.

### Verification cross-reference

![Requirements to verification cross-reference](assets/traceability-matrix.svg)

The matrix is generated from the current public traceability model. Blank cells are deliberate: the repository does not invent verification evidence simply to make the matrix look complete.

## Original flight / test evidence

<table>
<tr>
<td width="50%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon PFD in flight"><br><sub>Original in-flight project photograph: installed-aircraft PFD / synthetic-vision operation.</sub></td>
<td width="50%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Dynon prototype cockpit"><br><sub>Original installed Dynon prototype cockpit photograph.</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/qaef-ground-evaluation-sanitized.jpg" alt="Qatar ground evaluation"><br><sub>Original Qatar customer-evaluation period photograph. Used as programme/test context, not as proof of a different configuration.</sub></td>
<td width="50%"><b>Additional period flight-test imagery</b><br><sub>The project archive also contains cockpit-in-flight, aerial test-flight and test-engineer photographs. These are treated as operational/test context unless the visible configuration itself provides technical evidence.</sub></td>
</tr>
</table>

**Photographic release rule:** crop/resize/quality correction is allowed; redaction is limited to genuinely sensitive detail. For photographs of me, **rank insignia is redacted where required; public-event participants are not blanked merely because they are in uniform.** No synthetic replacement aircraft, cockpit, people or scenery is used.

## Programme-level downstream impact

![Programme impact timeline](assets/programme-impact.svg)

The early retrofit work should not be presented as if one prototype or one engineer alone caused later sales. It is still legitimate to show the scale of the product programme that followed the modernisation work:

| Publicly documented contract / service evidence | Aircraft | Evidence |
|---|---:|---|
| Nigeria contract, 2016 | 10 | APP reported a 10-aircraft contract; the first four delivered aircraft were explicitly described as **glass-cockpit** equipped |
| Qatar contract, 2016 | 8 | APP / Ministry of Defence Production reported eight Super Mushshak aircraft |
| Türkiye contract, 2017 | 52 | APP reported the signed 52-aircraft Turkish Air Force contract |
| Azerbaijan contract, 2017 | 10 | APP reported a 10-aircraft sale plus training and technical support |
| **New-customer contracts above** | **80** | 2016–2017 public contract record |

The same Azerbaijan report states that Super Mushshak was already in service with **Saudi Arabia, Oman, Iran and South Africa**, while Türkiye, Nigeria and Qatar had recently contracted the aircraft. Adding Azerbaijan gives a documented 2017 foreign customer/service footprint across **at least eight countries**. This is a historical programme-footprint statement, **not a claim that all eight have the same current fleet status today**.

Two of those four export deals also have public value estimates: Nigeria's 10 aircraft were estimated in its 2016 defence budget at **US$10.2 million**, while Anadolu Agency reported the 52-aircraft Türkiye deal at **around US$2 million per aircraft** (about **US$104 million implied**). That is **more than US$114 million in publicly estimable aircraft value for those two deals alone**; Qatar and Azerbaijan values are not asserted here because reliable public contract values were not found.

### Public operator evidence

<img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/PAC%20MFI-17%20Super%20Mushshak%20Turkish%20Air%20Force.jpg" alt="Turkish Air Force Super Mushshak" width="760">

*Turkish Air Force Super Mushshak, photographed by CeeGee at Teknofest 2023; Wikimedia Commons, CC BY-SA 4.0. This public operator image is programme-context evidence, separate from my original project photographs.*

The individual contribution claimed in this repository remains bounded to the **documented early systems engineering, avionics integration, prototype development, aircraft test/trials and customer-evaluation work**. The later contracts demonstrate downstream product/programme scale, not sole-causation.

## Retrospective MBSE evidence

The machine-readable model turns the surviving archive into linked engineering objects:

- [MBSE retrospective](docs/mbse-retrospective.md)
- [Structured model](model/README.md)
- [Requirements](model/requirements.csv)
- [Interfaces](model/interfaces.csv)
- [Verification records](model/verification.csv)
- [Configuration states](model/configurations.csv)
- [Decision records](model/decisions.csv)
- [Traceability](model/traceability.csv)

The model is intentionally public-safe: no pinouts, harness routes, controlled drawings, precise equipment locations, security markings, private customer correspondence, or confidential vendor data are published.

## Technical case-study map

- [Systems engineering case study](docs/engineering-case-study.md)
- [Architecture and trade study](docs/architecture-trade-study.md)
- [Verification and flight test](docs/verification-and-flight-test.md)
- [Qatar evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Evidence register](docs/evidence-register.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources and release boundary](docs/references.md)

## From retrofit to digital engineering

The current **Super Mushshak Digital Twin** is a separate follow-on effort. The retrofit archive provides real configuration history, interfaces, decisions, discrepancies and verification evidence that can seed a modern digital thread. The twin will increase in fidelity only where releasable evidence supports it.

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

> **Portfolio intent:** show the complete systems-engineering arc — trade study → architecture → aircraft integration → verification → customer evaluation → configuration traceability → digital-twin follow-on — without manufacturing evidence that did not exist.
