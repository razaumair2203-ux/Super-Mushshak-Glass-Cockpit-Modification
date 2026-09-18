# Super Mushshak Glass-Cockpit Retrofit

**Lead Systems Engineer case study · aircraft-level systems integration · prototype development · ground/flight verification · customer evaluation · configuration control · digital-thread reconstruction**

<table>
<tr>
<td width="50%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Installed Dynon SkyView prototype cockpit"></td>
<td width="50%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon SkyView display in flight"></td>
</tr>
<tr>
<td><sub>Installed Dynon SkyView prototype cockpit — authentic project photograph.</sub></td>
<td><sub>Installed-aircraft flight evidence — authentic in-flight project photograph.</sub></td>
</tr>
</table>

I led the systems engineering for this **Super Mushshak glass-cockpit retrofit programme**, carrying the aircraft-level integration problem from architecture and interface definition through prototype troubleshooting, installed-aircraft verification, OEM coordination and customer evaluation. The engineering boundary was the aircraft, not the display: the modification affected the sensor suite, complete modification wiring harness, aircraft electrical integration, NAV/COM and retained-avionics interfaces, software/settings/databases, cockpit HMI, physical installation, maintainability, installed-aircraft verification, flight evaluation and customer trials.

The archive contains distinct **Dynon SkyView** and **Garmin G900X/G950-family** prototype/evaluation paths. A separate **Garmin G3X** comparison deck is retained only as trade-study evidence and is not mislabelled as the G900X/G950 aircraft configuration.

## Executive engineering and programme summary

| Item | Public-safe summary |
|---|---|
| **Role** | **Lead Systems Engineer** — aircraft-level architecture/integration, prototype test/troubleshooting, OEM technical coordination and customer-evaluation support |
| **System of interest** | complete glass-cockpit aircraft retrofit, including revised sensing, wiring harness, electrical integration, retained avionics, HMI and configuration data |
| **Prototype paths** | Dynon SkyView installed prototype; separate Garmin G900X/G950-family prototype/evaluation path; G3X retained as comparison only |
| **Engineering method** | requirements → functions → interfaces → configuration states → installed verification → discrepancy/risk control → re-test → customer validation |
| **Direct evidence** | authentic project photographs, period engineering exchanges, troubleshooting/configuration records, flight/evaluation status and OEM material |
| **International outcome** | public reporting records **80 aircraft** across four new-customer contracts in 2016–2017: Nigeria 10, Qatar 8, Türkiye 52, Azerbaijan 10 |
| **Commercial context** | public reports place the Nigeria order at ~**US$10.2M** and Türkiye agreement at ~**US$50M**; Qatar/Azerbaijan values are not invented |
| **Follow-on** | retrospective digital thread / digital-twin foundation using controlled requirements, interfaces, configurations, V&V, issues, risks, decisions and evidence |

The commercial figures above are programme context, not an assertion that one prototype or one engineer solely caused later sales. The role claim and the later market outcome are deliberately kept separate in the evidence model.

## My systems-engineering responsibility

The surviving technical record is organised around the responsibilities I performed as Lead Systems Engineer on the retrofit:

| Responsibility | What is represented here |
|---|---|
| **System boundary and architecture** | defined the problem as an aircraft-level retrofit; kept vendor architectures and aircraft-specific evidence separate |
| **Trade space** | compared candidate avionics on functional coverage, HMI, interface burden, supportability, acceptance fit and lifecycle implications |
| **Cross-domain integration** | sensing, engine/airframe indication, electrical power/protection, NAV/COM, retained avionics, audio/alerts, HMI, physical installation and harness |
| **Configuration management** | separated historical prototype states; tied test evidence to as-tested hardware/settings/database state |
| **V&V** | installed checks, flight-test observations, discrepancy capture, engineering/OEM analysis, action and re-verification |
| **Risk control** | power/transient behaviour, configuration restoration, cross-domain interaction, high-dynamic attitude behaviour, retained-system interoperability and supportability |
| **Customer validation** | repeated customer-evaluation flying, including night operation, treated as validation rather than certification evidence |
| **Lifecycle / support** | LRU replacement, spares, OEM repair loop and configuration restoration |
| **Technical leadership** | translated equipment capability into aircraft-level interfaces, test evidence and controlled engineering decisions |

The role statement is controlled as retrospective evidence **E-25**; formal appointment material is not published.

## Evidence boundary

The repository is deliberately evidence-led. It separates **period project evidence**, **OEM/reference evidence**, **public programme evidence** and **retrospective engineering derivation**.

| Evidence class | May support | Must not be promoted into |
|---|---|---|
| Direct project evidence | observed configuration, integration activity, discrepancy or test event | facts not visible or documented in that evidence |
| OEM/reference documentation | vendor functions, generic interfaces, installation concepts | the exact aircraft-installed wiring or LRU baseline |
| Public programme record | later contracts/operator/commercial history | individual technical causation |
| Retrospective programme-lead statement | executed scope / role where explicitly labelled | a fabricated period document or unsupported technical result |
| Retrospective engineering derivation | public-safe requirements, functions, logical interfaces, risks and traceability views | an assertion that the artefact existed during the original programme |
| Unknown / not reconstructed | explicit gap in the public model | an inferred value inserted for completeness |

Project-evidence imagery is authentic. Processing is limited to crop, resize, exposure/contrast correction, sharpening and narrowly targeted redaction. **No synthetic aircraft, cockpit, equipment, person, test scene or replacement background is used.**

## Programme boundary and system context

![System context](assets/system-context.svg)

The system of interest is the **aircraft glass-cockpit retrofit**, not a stand-alone display suite. Its external context includes the aircraft baseline, pilot/instructor, maintenance organisation, avionics OEMs, flight-test/evaluation activity and customer/acceptance stakeholders.

See [System context and functional decomposition](docs/system-context-and-functions.md).

## Aircraft-level functional scope

![Functional decomposition](assets/functional-decomposition.svg)

The public functional model covers:

- acquire flight-state information;
- acquire engine/airframe information;
- present primary-flight and engine information;
- integrate NAV/COM, transponder, audio and retained-aircraft functions where applicable;
- distribute aircraft electrical power and protection to the retrofit;
- manage software, settings, terrain/navigation data and configuration state;
- integrate the physical installation and complete modification harness;
- provide cockpit HMI for pilot/instructor use;
- verify the installed aircraft and close discrepancies through re-test;
- sustain the configuration through spares, LRU replacement and OEM support.

Exact pins, harness routes, connector data and precise equipment locations are intentionally outside the public model.

## Systems-engineering lifecycle

![Systems-engineering lifecycle](assets/systems-engineering-lifecycle.svg)

The reconstructed lifecycle is:

**operational need / constraints → requirements → architecture alternatives → functional and interface definition → physical/electrical integration → configuration control → installed verification → discrepancy/risk investigation → re-test / flight test → customer validation → lifecycle support**

Configuration identity and evidence provenance are cross-cutting controls rather than end-of-project documentation.

See [Systems-engineering method](docs/systems-engineering-method.md).

## Logical architecture

![Public-safe logical architecture](assets/mbse-system-architecture.svg)

This is a **retrospective public-safe logical architecture**. It represents only evidence-backed functions and interfaces at a releasable level. It is not an original programme drawing and is not a substitute for a controlled aircraft wiring diagram.

See [Interface control](docs/interface-control.md).

## Prototype and configuration identities

The programme archive contains several distinct avionics paths. They are kept separate in the model.

| Configuration | Identity | Public evidence boundary |
|---|---|---|
| **CFG-000** | Legacy aircraft baseline | baseline functions reconstructed only at public-safe level |
| **CFG-D1** | Dynon SkyView initial installed prototype | installed-aircraft / early-flight evidence |
| **CFG-D2** | Dynon post-replacement and reconfiguration state | replacement displays, restored data/settings, return to flight |
| **CFG-D3** | Dynon performance / customer-evaluation state | customer-evaluation and flight-test evidence |
| **CFG-G1** | Garmin G900X/G950-family prototype/evaluation path | partially reconstructed; exact aircraft-installed public baseline remains unknown |
| **CMP-G3X** | Garmin G3X comparative candidate | trade-study evidence only; **not** an aircraft configuration |

![Configuration evolution](assets/configuration-evolution.svg)

The period comparison material identifies Dynon SkyView and Garmin G3X as separate candidates. The Garmin G900X/G950 material is treated as a separate family and source set. Generic Garmin architecture is used to understand the design space; it is never relabelled as the exact Super Mushshak installation.

See [Architecture and trade study](docs/architecture-trade-study.md) and [Configuration management](docs/configuration-management.md).

## Interfaces and integration

The retrofit is modelled across several engineering domains rather than as a display replacement.

| Domain | Public model treatment |
|---|---|
| Flight-state sensing | air-data / attitude-heading information to cockpit functions |
| Engine / airframe sensing | revised sensor/monitoring chain to engine/airframe display functions |
| NAV/COM | retained/new navigation and communication functions integrated as applicable |
| Retained avionics | transponder, audio and other legacy interfaces assessed individually |
| Electrical | aircraft supply, protection, load/transient behaviour and discrepancy investigation |
| Physical installation | panel/equipment installation plus complete modification-harness change |
| Configuration data | software, settings, terrain/navigation databases and restoration after LRU change |
| Human-system interface | information distribution, controls, alerts and training suitability |
| Lifecycle | spares, LRU exchange/repair, configuration restoration and OEM support |

Machine-readable source: [model/interfaces.csv](model/interfaces.csv).

## Integration risk and assurance

A new evidence-bounded risk register makes the integration logic explicit without pretending that a formal historical FHA/FMEA has survived.

| Risk theme | Engineering significance |
|---|---|
| Electrical power / transient behaviour | aircraft-level supply behaviour can defeat otherwise functional avionics |
| Configuration restoration | replacement hardware is not verified until settings/databases are restored |
| Cross-domain interference | radio activity and engine-indication behaviour can expose hidden coupling |
| High-dynamic attitude behaviour | sensor/reference behaviour must be understood in training/test manoeuvres |
| Retained-system interoperability | NAV/transponder/audio functions create configuration-specific interface burden |
| Supportability / AOG exposure | spares, OEM repair and configuration recovery affect operational availability |

See [Integration risk register](docs/integration-risk-register.md) and [model/risks.csv](model/risks.csv).

## Verification, discrepancy closure and traceability

![Evidence-to-verification thread](assets/mbse-verification-thread.svg)

The principal verification rule is:

> **A verification result belongs only to the identified configuration in which it was observed.**

The surviving Dynon record supports an installed-aircraft loop of **flight/ground observation → engineering/OEM investigation → hardware or configuration action → restoration of settings/databases where required → re-test / re-flight**.

Not every historical issue has a surviving final closure record. The model therefore distinguishes **observed**, **reverified**, **explained/characterised**, and **final closure not reconstructed** rather than forcing every event to a pass/fail conclusion.

![Requirements to verification cross-reference](assets/traceability-matrix.svg)

See [Verification and flight test](docs/verification-and-flight-test.md), [Traceability and V&V](docs/traceability-and-vv.md), and the [Assurance and closure summary](docs/assurance-closure-summary.md).

## Authentic installed-aircraft and field evidence

<table>
<tr>
<td width="50%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon PFD in flight"><br><sub>Installed Dynon display in flight. Supports installed-operation evidence only to the extent visible and linked to the project record.</sub></td>
<td width="50%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Dynon prototype cockpit"><br><sub>Installed Dynon prototype cockpit. Supports configuration context visible in the photograph.</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/qaef-ground-evaluation-sanitized.jpg" alt="Customer evaluation period"><br><sub>Original customer-evaluation-period project photograph. Used as field-evaluation context, not as proof of a result not visible in the image.</sub></td>
<td width="50%"><b>Additional archive imagery</b><br><sub>Cockpit-in-flight, aerial test-flight and test-engineer photographs remain source evidence. They are released only when they add engineering value and pass the same provenance/public-release checks.</sub></td>
</tr>
</table>

## International programme outcome

The later public record provides a clear scale signal for the product path that followed the prototype work.

| Customer | Quantity | Publicly reported glass-cockpit evidence |
|---|---:|---|
| **Nigeria** | 10 | delivered aircraft described as glass-cockpit equipped; Asian Military Review identifies **Dynon** |
| **Qatar** | 8 | Asian Military Review identifies **Garmin 950** |
| **Türkiye** | 52 | Asian Military Review identifies **Garmin 950** |
| **Azerbaijan** | 10 | operator use documented; cited configuration source does not identify selected avionics |
| **Total** | **80** | four new-customer contracts in 2016–2017 |

Public reporting places the Nigeria ten-aircraft order at an estimated **US$10.2M** and the Türkiye 52-aircraft agreement at approximately **US$50M**. Those two values alone exceed **US$60M**; no commercial value is invented for Qatar or Azerbaijan.

This supports a **commercially significant international programme outcome**. It is deliberately not converted into a sole-causation claim about one engineer or one prototype.

Key sources:

- [Associated Press of Pakistan — Nigeria delivery / glass cockpit](https://www.app.com.pk/national/pakistan-supplies-four-super-mushshak-to-naf/)
- [Associated Press of Pakistan — Qatar contract](https://www.app.com.pk/national/pakistan-inks-accord-to-supply-8-mushshak-aircraft-to-qatar/)
- [Associated Press of Pakistan — Türkiye 52-aircraft contract](https://www.app.com.pk/national/pakistan-to-supply-52-trainer-aircraft-to-turkey/)
- [Associated Press of Pakistan — Azerbaijan ten-aircraft sale](https://www.app.com.pk/national/pakistan-signs-agreement-with-azerbaijan-for-sale-of-10-super-mushshak-aircraft/)
- [Asian Military Review — export glass-cockpit mapping](https://www.asianmilitaryreview.com/2019/01/super-mushshaks-super-popular/)
- [Geo News — Nigeria ~US$10.2M estimate](https://www.geo.tv/latest/110046-Three-countries-to-buy-Super-Mushshaq-training-aircraft-from-Pakistan)
- [Business Recorder — Türkiye ~US$50M report](https://www.brecorder.com/news/4454451/pakistan-to-supply-52-trainer-aircraft-to-turkey-20161124106085)

External operator photographs are now **linked at source instead of hot-linked into the README**. That removes the broken-image problem seen with AirHistory and other sites while preserving copyright/provenance boundaries.

See [Independent public glass-cockpit and operator evidence](docs/public-operator-evidence.md).

## Model depth at a glance

The current public model contains:

- **6 stakeholders**
- **14 requirements**
- **12 aircraft-level functions**
- **11 logical interfaces**
- **6 configuration/comparison states**
- **8 verification records**
- **4 discrepancy records**
- **6 integration-risk records**
- **8 engineering decisions**
- **25 evidence records**
- **12 controlled claims**

These are deliberately compact, stable objects rather than diagram decoration.

## Machine-readable systems model

- [Model guide](model/README.md)
- [Stakeholders](model/stakeholders.csv)
- [Functions](model/functions.csv)
- [Requirements](model/requirements.csv)
- [Interfaces](model/interfaces.csv)
- [Configurations](model/configurations.csv)
- [Verification records](model/verification.csv)
- [Issues / discrepancies](model/issues.csv)
- [Integration risks](model/risks.csv)
- [Decision records](model/decisions.csv)
- [Evidence](model/evidence.csv)
- [Public claims](model/claims.csv)
- [Traceability](model/traceability.csv)
- [Typed links](model/links.csv)

The diagrams are views of this engineering structure; the stable IDs and evidence links are the authoritative public thread.

## Digital-thread / digital-twin continuation

The **Super Mushshak Digital Twin** is a separate follow-on effort. It does not retroactively turn the original programme into an MBSE programme.

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

The current work establishes the digital-thread backbone: configuration states, requirements, functions, logical interfaces, verification events, discrepancies, risks, decisions and evidence provenance. Executable models such as electrical-load analysis, configuration-dependent failure behaviour or data replay remain future capability unless and until releasable source data exists.

See [Digital twin follow-on](docs/digital-twin.md).

## Technical record map

- [Systems-engineering method](docs/systems-engineering-method.md)
- [System context and functional decomposition](docs/system-context-and-functions.md)
- [Systems engineering case study](docs/engineering-case-study.md)
- [Architecture and trade study](docs/architecture-trade-study.md)
- [Interface control](docs/interface-control.md)
- [Configuration management](docs/configuration-management.md)
- [Verification and flight test](docs/verification-and-flight-test.md)
- [Traceability and V&V](docs/traceability-and-vv.md)
- [Assurance and closure summary](docs/assurance-closure-summary.md)
- [Integration risk register](docs/integration-risk-register.md)
- [Customer evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Independent public glass-cockpit and operator evidence](docs/public-operator-evidence.md)
- [Evidence register](docs/evidence-register.md)
- [Retrospective MBSE reconstruction](docs/mbse-retrospective.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources and public-release boundary](docs/references.md)

## Public-release boundary

The repository demonstrates engineering method and traceability without publishing controlled or unnecessary detail. It does not expose security markings, private correspondence, detailed wiring routes, connector/pin data, controlled drawings, precise internal equipment locations, proprietary implementation detail or private customer information.

**Executable quality gate:** `python tools/validate_model.py` checks model-ID uniqueness, reference integrity, typed links, local Markdown/image paths and external hot-linked images. The same check runs in GitHub Actions on push and pull request. Technical correctness, configuration identity, evidence provenance, terminology, release suitability and unsupported claims remain engineering-review gates.
