# Super Mushshak Glass-Cockpit Retrofit

**Lead Systems Engineer case study · aircraft-level avionics integration · prototype development · configuration control · ground/flight verification · customer evaluation · digital-thread reconstruction**

<table>
<tr>
<td width="50%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Installed Dynon SkyView prototype cockpit"></td>
<td width="50%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon SkyView display in flight"></td>
</tr>
<tr>
<td><sub><b>Authentic project evidence:</b> installed Dynon SkyView prototype cockpit. Public-release processing only; no synthetic reconstruction.</sub></td>
<td><sub><b>Authentic project evidence:</b> installed-aircraft display in flight. Used only for what is visible and traceable.</sub></td>
</tr>
</table>

I was the **Lead Systems Engineer** for this Super Mushshak glass-cockpit retrofit. The engineering problem was not “replace analogue gauges with screens”; it was to integrate a new cockpit architecture into an existing training aircraft while controlling sensing, aircraft power, retained avionics, NAV/COM, the complete modification harness, software/data state, HMI, verification, maintainability and customer-evaluation risk.

The archive contains two distinct prototype/evaluation paths: **Dynon SkyView** and the **Garmin G900X/G950 family**. A separate **Garmin G3X comparison deck** survives as trade-study evidence only and is deliberately not relabelled as the G900X/G950 aircraft configuration.

## 30-second engineering view

| Dimension | Evidence-backed summary |
|---|---|
| **Role** | **Lead Systems Engineer** — aircraft-level architecture/integration, test/troubleshooting, OEM coordination and customer-evaluation support |
| **System of interest** | complete aircraft glass-cockpit retrofit: revised sensing, displays/HMI, retained avionics, power/protection, physical installation, complete modification harness and configuration data |
| **Core engineering problem** | integrate commercial avionics into an aerobatic military training-aircraft environment without losing aircraft-level compatibility, testability or supportability |
| **Prototype tracks** | Dynon SkyView installed prototype; separate Garmin G900X/G950-family path; G3X retained only as comparative evidence |
| **V&V model** | installed checks → flight observations → discrepancy isolation → engineering/OEM disposition → configuration restoration/change → re-test / re-flight |
| **Configuration discipline** | every test result belongs to the identified as-tested hardware/software/data state; unknown details stay unknown |
| **Customer validation** | surviving 2012 records document repeated customer-evaluation flying, including night operation; validation is not promoted into certification evidence |
| **Later programme scale** | public reporting records **80 aircraft** across Qatar, Nigeria, Türkiye and Azerbaijan in the 2016–2017 export sequence; this is programme context, not a sole-causation claim |

## Why this is a systems-engineering retrofit

![System context](assets/system-context.svg)

The system boundary is the **aircraft**, not an avionics display. The public reconstruction therefore models the retrofit against the legacy airframe, electrical system, revised sensor suite, retained systems, pilot/instructor, maintenance/OEM support, test activity and acceptance environment.

![Functional decomposition](assets/functional-decomposition.svg)

The aircraft-level functions are decomposed into four technical domains and three lifecycle functions:

- **Acquire aircraft state** — flight-state and engine/airframe sensing.
- **Present and interact** — primary flight information, engine/airframe information and pilot/instructor HMI.
- **Integrate avionics services** — NAV/COM, retained avionics, audio and alerting.
- **Integrate aircraft platform** — electrical power/protection, physical installation and complete modification harness.
- **Control configuration** — hardware, software, settings, databases and as-tested identity.
- **Verify installed aircraft** — ground/flight verification, discrepancy disposition and re-test.
- **Sustain and support** — LRU replacement/repair, spares, configuration restoration and OEM support.

Exact pins, connector data, controlled harness routes and precise internal installation detail are intentionally excluded from the public model.

## Lifecycle and architecture

![Retrospective V-model](assets/systems-engineering-lifecycle.svg)

This retrospective V-model expresses the engineering flow rather than pretending an original MBSE model existed in 2010–2012. The left side defines the problem and interfaces; the right side closes evidence against the corresponding configuration and requirement.

![Logical system architecture](assets/mbse-system-architecture.svg)

The logical architecture is deliberately vendor-neutral at aircraft level. Vendor reference architecture is used only to understand the design space. It is **not** presented as the exact Super Mushshak wiring baseline.

## Prototype identity and configuration control

![Configuration identity](assets/configuration-evolution.svg)

| ID | Configuration identity | Evidence boundary |
|---|---|---|
| **CFG-000** | legacy aircraft baseline | public-safe system boundary only |
| **CFG-D1** | Dynon initial installed prototype | early installed-aircraft operation and discrepancy evidence |
| **CFG-D2** | Dynon post-replacement / reconfiguration state | restored data/settings, interface work and return-to-flight evidence |
| **CFG-D3** | Dynon performance / customer-evaluation state | later flight-test and customer-evaluation observations |
| **CFG-G1** | Garmin G900X/G950-family path | separate prototype/evaluation family; exact public installed LRU baseline remains partial |
| **CMP-G3X** | Garmin G3X comparison artefact | trade-study evidence only; no installed-aircraft verification is assigned |

This separation is intentional: **configuration identity is part of the evidence model, not diagram decoration**.

## Verification and discrepancy closure

![Evidence-to-verification digital thread](assets/mbse-verification-thread.svg)

The main assurance rule is:

> **A verification claim belongs only to the configuration in which it was observed.**

The surviving archive supports a real installed-aircraft loop: observation → isolate interface/configuration → engineering and OEM analysis → hardware/configuration action → restore required settings/data → re-verify.

The model does not force every historical issue to “closed”. It distinguishes **observed**, **reverified**, **characterised/explained**, and **final closure not reconstructed**.

![Representative traceability slice](assets/traceability-matrix.svg)

The recruiter-facing matrix above is intentionally readable. The complete relationship set remains machine-readable in [model/traceability.csv](model/traceability.csv), linking requirements, functions, interfaces, configurations, verification records, issues, risks, decisions and evidence.

## Authentic project imagery and independent public media

The engineering narrative uses **original project photographs** as the primary visual evidence. No aircraft, cockpit, equipment, person or test scene is synthetically generated.

<table>
<tr>
<td width="50%"><img src="assets/qaef-ground-evaluation-sanitized.jpg" alt="Customer evaluation period project photograph"></td>
<td width="50%"><a href="https://commons.wikimedia.org/wiki/File:PAC_Super_Mushshak_cockpit.jpg"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/PAC%20Super%20Mushshak%20cockpit.jpg" alt="Public Super Mushshak cockpit photograph, Dubai Airshow 2017"></a></td>
</tr>
<tr>
<td><sub><b>Project archive:</b> customer-evaluation-period photograph. Used as field context only.</sub></td>
<td><sub><b>Independent public context:</b> Super Mushshak cockpit, Dubai Airshow 2017, Mztourist, CC BY-SA 4.0. This is not represented as an original project photograph.</sub></td>
</tr>
</table>

Independent sources strengthen the public context without being substituted for project evidence:

| Public source | What it supports |
|---|---|
| [Times Aerospace — *Nigeria opts for Super Mushshaks*](https://www.timesaerospace.aero/features/defence/nigeria-opts-for-super-mushshaks) | public appearance of the two-display glass cockpit at Dubai Airshow 2011; Dynon and Garmin alternatives |
| [Asian Military Review — *Super Mushshaks, Super Popular!*](https://www.asianmilitaryreview.com/2019/01/super-mushshaks-super-popular/) | 80-aircraft 2016–2017 export sequence; Qatar/Türkiye Garmin 950, Nigeria Dynon, Azerbaijan selection not identified |
| [The Peninsula Qatar — 2018 aviation feature](https://thepeninsulaqatar.com/pdf/20180322_1521670567-11085.pdf) | No. 30 Sqn, Al Zaeem Air Academy reported equipped with eight Garmin glass-cockpit Super Mushshaks in 2017 |
| [Defence Journal — *Super Mushshak*](https://www.defencejournal.com/2018/09/10/super-mushshak/) | overseas Garmin 950 / Dynon SkyView preference and PAF Dynon adoption context |
| [Wikimedia Commons cockpit photograph](https://commons.wikimedia.org/wiki/File:PAC_Super_Mushshak_cockpit.jpg) | reusable, independently sourced 2017 cockpit visual under CC BY-SA 4.0 |

Copyrighted news/operator photographs remain source-linked rather than copied into the project archive. Licensed imagery is clearly attributed and kept evidentially separate from original project photographs.

See [Independent public glass-cockpit and operator evidence](docs/public-operator-evidence.md).

## Later programme context

Specialist and public reporting documents the following 2016–2017 new-customer sequence:

| Customer | Quantity | Public configuration evidence used here |
|---|---:|---|
| Qatar | 8 | Garmin 950 |
| Nigeria | 10 | Dynon |
| Türkiye | 52 | Garmin 950 |
| Azerbaijan | 10 | configuration not identified in the cited specialist source |
| **Total** | **80** | programme-level context |

This demonstrates the later scale and continuity of the glass-cockpit product path. It **does not** establish that an early prototype was reproduced unchanged or that one engineer alone caused the later sales.

![Programme context](assets/programme-context.svg)

## Digital thread → future digital twin

![Digital-thread / twin roadmap](assets/digital-twin-roadmap.svg)

The follow-on digital-engineering work starts from the historical evidence rather than inventing missing aircraft data. The implemented backbone under `/model` contains stable IDs and traceability for:

**evidence → claims → requirements → functions → interfaces → configurations → verification → issues/risks → decisions**

Executable electrical, failure-state, maintenance/health, data-replay and verification-scenario models are future increments and will only be promoted when releasable source data supports the required fidelity.

## Evidence and public-release boundary

This repository intentionally does **not** publish security markings, private correspondence, personal data, detailed wiring routes, connector/pin data, controlled drawings, exact internal equipment locations or proprietary implementation detail.

Image processing is limited to **crop, resize, exposure/contrast correction, sharpening and targeted redaction** of unnecessary identifiers/location details. There is **no synthetic cockpit or aircraft reconstruction**.

## Technical record

For deeper review:

- [Systems-engineering case study](docs/engineering-case-study.md)
- [System context and functions](docs/system-context-and-functions.md)
- [Systems-engineering method](docs/systems-engineering-method.md)
- [Architecture and trade study](docs/architecture-trade-study.md)
- [Interface control](docs/interface-control.md)
- [Configuration management](docs/configuration-management.md)
- [Verification and flight test](docs/verification-and-flight-test.md)
- [Traceability and V&V](docs/traceability-and-vv.md)
- [Integration risk register](docs/integration-risk-register.md)
- [Customer evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Independent public evidence](docs/public-operator-evidence.md)
- [Evidence register](docs/evidence-register.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources and public-release boundary](docs/references.md)
- [Machine-readable model](model/README.md)

**Executable quality gate:** `python tools/validate_model.py` validates model-ID uniqueness, reference integrity, typed links, local Markdown/image paths and external image references. Engineering correctness, evidence provenance, configuration identity and public-release suitability remain human review gates.
