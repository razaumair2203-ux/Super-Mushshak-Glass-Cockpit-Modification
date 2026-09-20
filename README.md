# Super Mushshak Glass-Cockpit Retrofit

**Muhammad Umair Raza · Lead Systems Engineer · aircraft-level avionics integration and prototype verification**

A historical aerospace case study supporting lead/principal systems-integration and technical programme roles. The engineering problem was to integrate modern displays, revised sensing and a complete modification harness into an existing trainer aircraft, then resolve installed-aircraft behaviour through ground and flight testing.

[Engineering case](docs/engineering-case-study.md) · [Verification and open dispositions](docs/assurance-closure-summary.md) · [Original photographs](docs/media-gallery.md) · [Digital model](model/README.md) · [Contact / evidence requests](docs/evidence-register.md#request-a-technical-review)

[Applied AI & autonomous systems portfolio](https://github.com/razaumair2203-ux/applied-ai-portfolio)

## Executive snapshot

<table>
<tr>
<td align="center"><b>Lead Systems Engineer</b><br><sub>aircraft-level retrofit ownership</sub></td>
<td align="center"><b>2 prototype paths</b><br><sub>Dynon SkyView · Garmin G900X</sub></td>
<td align="center"><b>Complete modification scope</b><br><sub>sensors · harness · avionics · power · HMI</sub></td>
<td align="center"><b>Ground + flight V&amp;V</b><br><sub>discrepancy isolation · OEM action · re-test</sub></td>
</tr>
</table>

I led systems engineering for the Super Mushshak glass-cockpit retrofit across **architecture, interfaces, physical/electrical integration, configuration control, verification, troubleshooting, OEM coordination and international customer evaluation**. The modification replaced/reworked the aircraft sensing chain, introduced a **complete modification wiring harness**, integrated modern display and navigation/communication equipment, and matured the aircraft through installed ground and flight testing. My programme role also extended into **in-country Qatar customer-evaluation support and Dubai Airshow display activity**, taking the engineering work into an international customer-facing environment.

The programme developed two principal prototype paths: **Dynon SkyView** and **Garmin G900X**. A project comparison deck also contains **Garmin G3X** candidate material; that remains trade-study evidence and is kept separate from the G900X prototype identity.

**Contribution boundary:** I led systems integration, test/troubleshooting and OEM coordination. Fabrication, installation, flight operations and customer evaluation were multidisciplinary programme work. My role and harness/sensor scope are programme-lead statements [E-24/E-25](docs/evidence-register.md); later aircraft sales are wider programme outcomes.

![Installed Dynon SkyView cockpit](assets/dynon-skyview-installed-prototype.jpg)

*Original project photograph of the installed Dynon SkyView cockpit. It supports configuration and installation context; it does not establish certification or the closure of every test discrepancy.*

**Historical work and current modelling:** the retrofit and prototype flight work are historical. The CSV model and systems diagrams are current retrospective engineering representations. An executable aircraft digital twin remains future work.

## Engineering flow

**operational need → architecture & trade studies → sensor / avionics / harness integration → ground integration → flight test → discrepancy isolation → OEM engineering action → configuration update → re-test → customer evaluation → product maturity**

![Systems engineering lifecycle](assets/systems-engineering-lifecycle.svg)

This is the level at which the work was executed: the **aircraft was the system boundary**. Display selection was only one element of a coupled modification involving sensing, power/protection, data and audio interfaces, retained avionics, installation, maintainability, software/settings/databases and pilot/instructor HMI.

## Aircraft-level architecture

The integration boundary includes flight and engine sensing, displays, NAV/COM and audio, aircraft power/protection, retained avionics, configuration data and maintainability. Dynon and Garmin paths remain separate.

[Architecture and trade study](docs/architecture-trade-study.md) · [System context and functions](docs/system-context-and-functions.md) · [Interface control](docs/interface-control.md)

## Prototype identity & configuration control

| Configuration | Engineering identity |
|---|---|
| **CFG-000** | legacy aircraft baseline |
| **CFG-D1** | Dynon initial installed prototype |
| **CFG-D2** | Dynon post-replacement / reconfiguration state |
| **CFG-D3** | Dynon performance / customer-evaluation state |
| **CFG-G1** | Garmin G900X prototype / evaluation path |
| **CMP-G3X** | Garmin G3X comparison artefact — trade study only |

This separation is deliberate: requirements, interfaces, discrepancies and V&amp;V results remain tied to the **as-tested configuration**.

## Verification, troubleshooting & re-flight

![Verification thread](assets/mbse-verification-thread.svg)

The project record shows an installed-aircraft engineering loop:

**observe → isolate interface / configuration → engineer with OEM → implement hardware / configuration action → restore settings / data → re-test / re-flight**

<p align="center">
  <img src="assets/flight-test/cockpit-overview-inflight.jpg" alt="Original full-frame cockpit overview from flight test" width="92%">
</p>

<p align="center"><sub><b>Installed-aircraft sortie context.</b> Original period photograph showing the aircraft operating in the real flight-test environment.</sub></p>

![Traceability matrix](assets/traceability-matrix.svg)

The machine-readable model in [model/](model/README.md) links requirements, functions, interfaces, configurations, verification records, issues, risks, decisions and supporting evidence.

## International product-line outcome

The prototype work included Qatar customer-evaluation support and Dubai Airshow display activity. Later public reports record **80 aircraft across four customer orders**: Qatar 8, Nigeria 10, Türkiye 52 and Azerbaijan 10. Those orders provide programme context, not a personal revenue result or evidence that every export aircraft used the same configuration.

[Independent public sources](docs/public-operator-evidence.md) · [Customer-evaluation record](docs/field-evaluation-and-programme-context.md) · [Historical commercial source context](docs/programme-value-context.md)

## Why this project matters

| Systems-engineering dimension | Evidence in this portfolio |
|---|---|
| **Architecture & trade studies** | distinct Dynon / Garmin prototype paths; candidate comparison discipline |
| **Interface engineering** | aircraft power, revised sensing, NAV/COM, audio, retained avionics, data/settings |
| **Physical integration** | complete modification harness and aircraft installation scope |
| **Configuration management** | as-tested hardware/software/settings state tied to V&amp;V evidence |
| **Verification & validation** | installed checks, flight observations, discrepancy isolation, re-test |
| **Supplier / OEM engineering** | technical coordination through observed issues and configuration actions |
| **Customer-facing delivery** | international evaluation / demonstration context |
| **Product lifecycle** | supportability, spares/repair logic and digital-thread continuation |

## Current digital thread and future digital twin

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

The current **retrospective digital-engineering model** links historical evidence. Executable digital-twin behaviour is proposed and has not been validated. Original project evidence and engineering knowledge are structured as:

**claims → requirements → functions → interfaces → configurations → verification → issues / risks → decisions**

The next stage is an executable Super Mushshak digital twin using releasable engineering data for interface behaviour, failure-state logic, maintenance / health state, data replay and verification scenarios.

## Public-release scope

Detailed wiring, pin-level interconnects, proprietary installation drawings, private correspondence, personal data and restricted material are intentionally omitted. Published aircraft and cockpit photographs are **original project images**. No new presentation crop or zoom is introduced; existing publication derivatives are identified in [visual provenance](assets/approved-visual-provenance.json); any processing is limited to non-generative image-quality improvement such as exposure/contrast correction, sharpening, metadata removal and strictly necessary privacy/security treatment. No new collage is created from the source photographs. **No synthetic aircraft or cockpit imagery is used.**

## Technical record

- [Systems-engineering case study](docs/engineering-case-study.md)
- [System context and functions](docs/system-context-and-functions.md)
- [Architecture and trade study](docs/architecture-trade-study.md)
- [Interface control](docs/interface-control.md)
- [Configuration management](docs/configuration-management.md)
- [Verification and flight test](docs/verification-and-flight-test.md)
- [Traceability and V&V](docs/traceability-and-vv.md)
- [Integration risk register](docs/integration-risk-register.md)
- [International customer evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Independent public evidence](docs/public-operator-evidence.md)
- [Public programme-value context](docs/programme-value-context.md)
- [Project media gallery](docs/media-gallery.md)
- [Evidence register](docs/evidence-register.md)
- [MBSE / digital-thread representation](docs/mbse-digital-thread.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources](docs/references.md)
- [Machine-readable systems model](model/README.md)

**Quality gate:** `python tools/validate_model.py` checks model IDs, typed references, local links and local image paths.
