# Super Mushshak Glass-Cockpit Retrofit

**Aircraft-level systems engineering · avionics integration · prototype verification · configuration control · flight test · customer evaluation · digital-thread reconstruction**

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

This repository reconstructs the **systems-engineering record of a Super Mushshak glass-cockpit retrofit programme** from surviving project evidence. The modification boundary was aircraft-level: displays were only one part of a change that also affected sensing, navigation/communication integration, aircraft electrical integration, the modification wiring harness, software/settings/databases, physical installation, maintainability, installed-aircraft verification and flight evaluation.

**Engineering responsibility represented:** lead systems engineering, avionics integration/test activity, OEM technical coordination, installed-aircraft troubleshooting and customer-evaluation support. Surviving correspondence independently evidences hands-on integration activity; formal appointment material is not published.

The repository is deliberately evidence-led. It separates **period project evidence**, **OEM/reference evidence**, **public programme evidence** and **retrospective engineering derivation**. Unknown or unreconstructed information stays unknown.

## Evidence boundary

| Evidence class | May support | Must not be promoted into |
|---|---|---|
| Direct project evidence | observed configuration, integration activity, discrepancy or test event | facts not visible or documented in that evidence |
| OEM/reference documentation | vendor functions, generic interfaces, installation concepts | the exact aircraft-installed wiring or LRU baseline |
| Public programme record | later contracts/operator history | individual technical causation |
| Retrospective engineering derivation | public-safe requirements, functions, logical interfaces, traceability views | an assertion that the artefact existed during the original programme |
| Unknown / not reconstructed | explicit gap in the public model | an inferred value inserted for completeness |

Project-evidence imagery in this repository is authentic. Processing is limited to crop, resize, exposure/contrast correction, sharpening and narrowly targeted redaction. Independent public/operator photographs may be source-linked as contextual corroboration, but are visually separated from project evidence and are not used to infer hidden configuration details. **No synthetic aircraft, cockpit, equipment, person, test scene or replacement background is used.**

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
- integrate the physical installation and the complete modification harness;
- provide cockpit HMI for pilot/instructor use;
- verify the installed aircraft and close discrepancies through re-test;
- sustain the configuration through spares, LRU replacement and OEM support.

Exact pins, harness routes, connector data and precise equipment locations are intentionally outside the public model.

## Systems-engineering lifecycle

![Systems-engineering lifecycle](assets/systems-engineering-lifecycle.svg)

The reconstructed lifecycle is:

**operational need / constraints → requirements → architecture alternatives → functional and interface definition → physical/electrical integration → configuration control → installed verification → discrepancy investigation → re-test / flight test → customer evaluation → lifecycle support**

Configuration identity and evidence provenance are cross-cutting controls rather than end-of-project documentation.

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
| **CFG-D3** | Dynon performance / Qatar evaluation state | customer-evaluation and flight-test evidence |
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

The machine-readable source is [model/interfaces.csv](model/interfaces.csv).

## Verification, discrepancy closure and traceability

![Evidence-to-verification thread](assets/mbse-verification-thread.svg)

The principal verification rule is:

> **A verification result belongs only to the identified configuration in which it was observed.**

The surviving Dynon record supports an installed-aircraft loop of **flight/ground observation → engineering/OEM investigation → hardware or configuration action → restoration of settings/databases where required → re-test / re-flight**.

Not every historical issue has a surviving final closure record. The model therefore distinguishes **observed**, **reverified**, **explained/characterised**, and **final closure not reconstructed** rather than forcing every event to a pass/fail conclusion.

![Requirements to verification cross-reference](assets/traceability-matrix.svg)

See [Verification and flight test](docs/verification-and-flight-test.md) and [Traceability and V&V](docs/traceability-and-vv.md).

## Authentic installed-aircraft and field evidence

<table>
<tr>
<td width="50%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon PFD in flight"><br><sub>Installed Dynon display in flight. Supports installed-operation evidence only to the extent visible and linked to the project record.</sub></td>
<td width="50%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Dynon prototype cockpit"><br><sub>Installed Dynon prototype cockpit. Supports configuration context visible in the photograph.</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/qaef-ground-evaluation-sanitized.jpg" alt="Customer evaluation period"><br><sub>Original customer-evaluation-period project photograph. Used as field-evaluation context, not as proof of a result not visible in the image.</sub></td>
<td width="50%"><b>Additional archive imagery</b><br><sub>Cockpit-in-flight, aerial test-flight and test-engineer photographs remain source evidence. They are released only when they add engineering value and pass the same provenance and public-release checks.</sub></td>
</tr>
</table>

## Independent public cockpit and operator evidence

The authentic project photographs above remain the primary evidence of the retrofit work. A separate public-evidence layer provides **independent corroboration of the glass-cockpit programme and later operator/export context** without mixing third-party imagery into the project archive.

<table>
<tr>
<td width="50%"><a href="https://commons.wikimedia.org/wiki/File:PAC_Super_Mushshak_cockpit.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/PAC_Super_Mushshak_cockpit.jpg" alt="Public Super Mushshak cockpit at Dubai Air Show 2017"></a><br><sub><b>Public glass-cockpit view.</b> Dubai Air Show 2017; Mztourist / Wikimedia Commons, CC BY-SA 4.0. Exact suite identity is not inferred from the photograph alone.</sub></td>
<td width="50%"><a href="https://www.defensenews.com/training-sim/2016/12/07/nigeria-takes-delivery-of-pakistani-made-super-mushshak-trainer-aircraft/"><img src="https://cloudfront-us-east-1.images.arcpublishing.com/archetype/3CWBD5KEEJHJZAE63QCMWZY5G4.jpg" alt="Super Mushshak associated with Nigerian delivery"></a><br><sub><b>Nigeria.</b> External source image: Defense News. APP independently described the delivered aircraft as glass-cockpit equipped; Asian Military Review identifies the Nigerian fleet as Dynon-equipped.</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://www.airhistory.net/photo/417432/QA306"><img src="https://www.airhistory.net/photos/0417432.jpg" alt="Qatar Emiri Air Force Super Mushshak formation"></a><br><sub><b>Qatar.</b> External source image: AirHistory.net / photographer copyright. Qatar News Agency documents continuing Super Mushshak use at Al Zaeem Air Academy; Asian Military Review identifies the Qatar aircraft as Garmin 950-equipped.</sub></td>
<td width="50%"><a href="https://mod.gov.az/en/news/azerbaijani-military-pilots-conduct-the-next-training-flights-video-54557.html"><img src="https://mod.gov.az/images/gallery/77218ac0dd1ad25c1952444953e98d36.jpg" alt="Azerbaijan Air Force Super Mushshak training"></a><br><sub><b>Azerbaijan.</b> External source image: Ministry of Defence of Azerbaijan. Current training activity is independently documented; the cited avionics comparison source does not identify Azerbaijan's selected suite.</sub></td>
</tr>
</table>

Public reporting provides an important configuration cross-check: **Qatar — Garmin 950; Nigeria — Dynon; Türkiye — Garmin 950; Azerbaijan — avionics selection not identified in the cited configuration source.** This is programme-level continuity evidence, not proof that an early prototype was reproduced unchanged.

See [Independent public glass-cockpit and operator evidence](docs/public-operator-evidence.md) for the source-by-source record, Türkiye imagery, operator cross-checks and attribution rules.

## Customer evaluation and programme context

The surviving record shows the Dynon-configured aircraft progressing into performance testing and customer evaluation. Evaluation evidence includes repeated flight activity, night operation and configuration-specific technical observations. Customer evaluation is treated as **validation context**, not as a substitute for certification evidence or formal verification.

Later public records document new-customer Super Mushshak contracts in 2016–2017 and a Nigeria delivery explicitly described as glass-cockpit equipped. These later records establish programme context and product-modernisation continuity; they are **not used to claim that one prototype or one engineer caused later sales**.

![Programme context](assets/programme-context.svg)

See [Customer evaluation and programme context](docs/field-evaluation-and-programme-context.md).

## Machine-readable systems model

The retrospective model gives stable identities to engineering objects rather than hiding the logic inside diagrams.

- [Model guide](model/README.md)
- [Stakeholders](model/stakeholders.csv)
- [Functions](model/functions.csv)
- [Requirements](model/requirements.csv)
- [Interfaces](model/interfaces.csv)
- [Configurations](model/configurations.csv)
- [Verification records](model/verification.csv)
- [Issues / discrepancies](model/issues.csv)
- [Decision records](model/decisions.csv)
- [Evidence](model/evidence.csv)
- [Public claims](model/claims.csv)
- [Traceability](model/traceability.csv)
- [Typed links](model/links.csv)

The diagrams are views of this engineering structure; the stable IDs and evidence links are the authoritative public thread.

## Digital-thread / digital-twin continuation

The **Super Mushshak Digital Twin** is a separate follow-on effort. It does not retroactively turn the original programme into an MBSE programme.

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

The current work establishes the digital-thread backbone: configuration states, requirements, functions, logical interfaces, verification events, discrepancies, decisions and evidence provenance. Executable models such as electrical-load analysis, configuration-dependent failure behaviour or data replay remain future capability unless and until releasable source data exists.

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
- [Customer evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Independent public glass-cockpit and operator evidence](docs/public-operator-evidence.md)
- [Evidence register](docs/evidence-register.md)
- [Retrospective MBSE reconstruction](docs/mbse-retrospective.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources and public-release boundary](docs/references.md)

## Public-release boundary

The repository demonstrates engineering method and traceability without publishing controlled or unnecessary detail. It does not expose security markings, private correspondence, detailed wiring routes, connector/pin data, controlled drawings, precise internal equipment locations, proprietary implementation detail or private customer information.

**Quality gate:** every public artefact is expected to pass checks for technical correctness, configuration identity, evidence provenance, readability, link integrity, terminology consistency, release suitability, duplication and unsupported claims.
