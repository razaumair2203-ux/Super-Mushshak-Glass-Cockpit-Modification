# Super Mushshak Glass-Cockpit Retrofit

**International aircraft-modernisation case study · Lead Systems Engineer · avionics integration · prototype development · ground/flight V&V · customer evaluation · configuration control · product-line scale · digital-twin continuation**

<p align="center">
  <img src="assets/recruiter/hero-super-mushshak-retrofit.jpg" alt="Super Mushshak glass-cockpit retrofit programme overview built from authentic period project imagery" width="100%">
</p>

<p align="center">
  <img src="assets/recruiter/hero-flight-test-evidence.jpg" alt="Flight-test evidence and visual asset overview built from authentic period project imagery" width="100%">
</p>

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

### Programme evidence at a glance

<p align="center">
  <img src="assets/dynon-skyview-flight-test.jpg" alt="Original in-flight Dynon glass-cockpit photograph" width="92%">
</p>

<p align="center"><sub><b>Installed avionics in flight.</b> Original project photograph showing the Dynon glass-cockpit configuration operating on the aircraft during flight-test activity.</sub></p>

![Programme scale](assets/programme-impact.svg)

## Engineering flow

**operational need → architecture & trade studies → sensor / avionics / harness integration → ground integration → flight test → discrepancy isolation → OEM engineering action → configuration update → re-test → customer evaluation → product maturity**

![Systems engineering lifecycle](assets/systems-engineering-lifecycle.svg)

This is the level at which the work was executed: the **aircraft was the system boundary**. Display selection was only one element of a coupled modification involving sensing, power/protection, data and audio interfaces, retained avionics, installation, maintainability, software/settings/databases and pilot/instructor HMI.

## Aircraft-level architecture

![System context](assets/system-context.svg)

![Functional decomposition](assets/functional-decomposition.svg)

<table>
<tr>
<td width="50%"><img src="assets/mbse-system-architecture.svg" alt="Logical aircraft-level system architecture"></td>
<td width="50%"><img src="assets/configuration-evolution.svg" alt="Prototype and configuration evolution"></td>
</tr>
</table>

The diagrams are current systems-engineering representations of the executed programme. They communicate architecture, interface ownership, configuration discipline and V&amp;V structure while keeping controlled installation detail, pin-level interconnects and proprietary drawings outside the public repository.

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

The engineering programme progressed through prototype development, flight test, customer evaluation and public display activity. Public reporting subsequently shows the glass-cockpit Super Mushshak product line scaling into a multi-country export programme.

<p align="center">
  <img src="assets/programme-support/usafa-dubai-airshow.jpg" alt="Original Dubai Airshow programme-support photograph with USAFA counterpart" width="82%">
</p>
<p align="center"><sub><b>International programme support.</b> Authentic period photograph from Dubai Airshow context, supporting the customer-facing display/programme-support phase described here. It is context evidence, not a technical-performance result.</sub></p>

| Customer / operator | Publicly reported quantity | Public evidence |
|---|---:|---|
| **Qatar** | 8 | [APP contract report](https://www.app.com.pk/national/pakistan-inks-accord-to-supply-8-mushshak-aircraft-to-qatar/) |
| **Nigeria** | 10 | [APP delivery report](https://www.app.com.pk/national/pakistan-supplies-four-super-mushshak-to-naf/) |
| **Türkiye** | 52 | [APP contract report](https://www.app.com.pk/national/pakistan-to-supply-52-trainer-aircraft-to-turkey/) |
| **Azerbaijan** | 10 | [APP sale report](https://www.app.com.pk/national/pakistan-signs-agreement-with-azerbaijan-for-sale-of-10-super-mushshak-aircraft/) |
| **2016–2017 new-customer sequence** | **80** | customer totals above |

Specialist reporting also states that the two-display glass-cockpit Super Mushshak appeared publicly at **Dubai Airshow 2011**, with Dynon and Garmin versions available, and that by 2024 **more than 100 Super Mushshaks had been upgraded or sold with new avionics since 2016**. See [Independent Public Evidence](docs/public-operator-evidence.md).

### Public programme-value context

A 2016 [Business Recorder report](https://www.brecorder.com/news/4454451/pakistan-to-supply-52-trainer-aircraft-to-turkey-20161124106085) placed the **52-aircraft Türkiye programme at around US$50M**. That implies a public scale benchmark of about **US$0.962M per aircraft**.

Applied only as a transparent scale reference to the 80-aircraft sequence above:

**80 × (US$50M / 52) ≈ US$76.9M → ≈ US$78M aircraft-value equivalent**

Public sources also document **operational training and technical support** in the Nigeria and Azerbaijan packages, plus simulator and engine-support activity around the Türkiye programme. Because those support values are not publicly standardized, they are not presented as actual contract totals. An illustrative 10–30% support sensitivity around the weighted public benchmark places the campaign at roughly **US$85–101M**.

> **Portfolio interpretation:** the engineering work shown here sat on a product path that progressed from prototype integration and flight test into an internationally fielded aircraft family operating at substantial programme scale. Commercial figures are public-market context, not confidential contract disclosure or individual revenue attribution.

Full assumptions and arithmetic: [Public Programme-Value Context](docs/programme-value-context.md).

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

## Digital thread → digital twin

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

The programme is now being carried forward into a **digital-engineering / digital-twin initiative**. Original project evidence and engineering knowledge are structured as:

**claims → requirements → functions → interfaces → configurations → verification → issues / risks → decisions**

The next stage is an executable Super Mushshak digital twin using releasable engineering data for interface behaviour, failure-state logic, maintenance / health state, data replay and verification scenarios.

## Public-release scope

Detailed wiring, pin-level interconnects, proprietary installation drawings, private correspondence, personal data and restricted material are intentionally omitted. Published aircraft and cockpit photographs are **original project images**. They are not cropped or zoomed for presentation; any processing is limited to non-generative image-quality improvement such as exposure/contrast correction, sharpening, metadata removal and strictly necessary privacy/security treatment. No new collage is created from the source photographs. Only composite boards explicitly approved by the programme lead are used as composite visuals. **No synthetic aircraft or cockpit imagery is used.**

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
