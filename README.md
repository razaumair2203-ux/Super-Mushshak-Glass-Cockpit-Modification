# Super Mushshak Glass-Cockpit Retrofit

**Lead Systems Engineer case study · aircraft-level avionics integration · prototype development · ground/flight test · customer evaluation · configuration control · digital-engineering follow-on**

<table>
<tr>
<td width="34%"><img src="assets/dynon-cockpit-prototype-sanitized.jpg" alt="Installed Dynon SkyView prototype cockpit"></td>
<td width="33%"><img src="assets/dynon-pfd-inflight-sanitized.jpg" alt="Dynon SkyView cockpit in flight"></td>
<td width="33%"><img src="assets/qaef-ground-evaluation-sanitized.jpg" alt="Customer evaluation period project photograph"></td>
</tr>
<tr>
<td><sub><b>Installed prototype:</b> Dynon SkyView glass cockpit.</sub></td>
<td><sub><b>Flight test:</b> installed Dynon cockpit operating in flight.</sub></td>
<td><sub><b>Customer evaluation:</b> project aircraft during international evaluation activity.</sub></td>
</tr>
</table>

I was the **Lead Systems Engineer** for the Super Mushshak glass-cockpit retrofit. The job was an aircraft-level modification: integrate new displays, sensing, NAV/COM, retained avionics, aircraft power, the complete modification wiring harness, configuration data and HMI into an existing military trainer, then take the integrated aircraft through ground test, flight test, troubleshooting and customer evaluation.

The programme pursued two prototype paths: **Dynon SkyView** and **Garmin G900X**. A surviving comparison deck also evaluates **Garmin G3X**; that deck is retained as trade-study evidence and is not used to relabel the separate G900X prototype path.

## The hook: early prototype work became a much larger product path

Independent aviation reporting shows that the glass-cockpit Super Mushshak moved well beyond the initial development activity documented here:

- [Times Aerospace, 2017](https://www.timesaerospace.aero/features/defence/nigeria-opts-for-super-mushshaks) reported that the two-display glass-cockpit Super Mushshak first appeared publicly at **Dubai Airshow 2011**, with **Dynon and Garmin** versions available.
- [Asian Military Review, 2019](https://www.asianmilitaryreview.com/2019/01/super-mushshaks-super-popular/) documented an **80-aircraft** new-customer sequence in 2016–2017: **Qatar 8, Nigeria 10, Türkiye 52 and Azerbaijan 10**. It identified Qatar and Türkiye with **Garmin 950** and Nigeria with **Dynon**.
- [Times Aerospace, 2024](https://www.timesaerospace.aero/sites/aerospace/times/files/magazines/2024/das24-wds-d3/content/das24-wds-d3.pdf) reported that **more than 100 Super Mushshaks had been upgraded or sold with new avionics since 2016**, using Dynon, GenesyS or Garmin systems.

That is the programme-scale continuation of the glass-cockpit product path. It does not imply that every later production aircraft reproduced an early prototype unchanged.

## Independent media: the product after the prototype phase

<table>
<tr>
<td width="33%"><a href="https://commons.wikimedia.org/wiki/File:96-6385_PAC_MFI-17_Super_Mushshak_(7970352052).jpg"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/96-6385%20PAC%20MFI-17%20Super%20Mushshak%20%287970352052%29.jpg" alt="Super Mushshak at Dubai Airshow 2011"></a></td>
<td width="34%"><a href="https://commons.wikimedia.org/wiki/File:PAC_Super_Mushshak_cockpit.jpg"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/PAC%20Super%20Mushshak%20cockpit.jpg" alt="Super Mushshak cockpit at Dubai Airshow 2017"></a></td>
<td width="33%"><a href="https://commons.wikimedia.org/wiki/File:PAC_MFI-17_Super_Mushshak_Turkish_Air_Force.jpg"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/PAC%20MFI-17%20Super%20Mushshak%20Turkish%20Air%20Force.jpg" alt="Turkish Air Force Super Mushshak"></a></td>
</tr>
<tr>
<td><sub><b>Dubai Airshow 2011:</b> Super Mushshak on public display. Kurush Pawar / DXBSpotter, CC BY-SA 2.0.</sub></td>
<td><sub><b>Dubai Airshow 2017:</b> later Super Mushshak glass-cockpit display. Mztourist, CC BY-SA 4.0.</sub></td>
<td><sub><b>Export service:</b> Turkish Air Force Super Mushshak. CeeGee, Wikimedia Commons; licence on source page.</sub></td>
</tr>
</table>

See the fuller [project + independent media gallery](docs/media-gallery.md).

## 30-second engineering view

| Dimension | What this project demonstrates |
|---|---|
| **Role** | **Lead Systems Engineer** — aircraft-level architecture/integration, test, troubleshooting, OEM coordination and customer-evaluation support |
| **System of interest** | complete glass-cockpit retrofit: revised sensing, displays/HMI, retained avionics, NAV/COM, power/protection, physical installation, modification harness and configuration data |
| **Prototype tracks** | Dynon SkyView installed prototype and a separate Garmin G900X prototype path; G3X retained as comparison/trade-study material |
| **Engineering flow** | architecture and interfaces → installation → ground test → flight test → discrepancy isolation → engineering/OEM action → re-test |
| **Configuration discipline** | results tied to the as-tested hardware/software/data state |
| **Customer validation** | repeated customer-evaluation flying documented in the surviving programme record |
| **Later impact** | glass-cockpit Super Mushshak subsequently entered multi-country export service at significant scale |

## Aircraft-level systems engineering

![System context](assets/system-context.svg)

The system boundary is the **aircraft**, not the display. The retrofit touched four coupled technical areas:

- **flight and engine sensing**;
- **cockpit displays, HMI and alerts**;
- **NAV/COM, audio and retained avionics interfaces**;
- **aircraft power, physical installation and the complete modification wiring harness**.

It also required configuration management, verification, maintainability and OEM/customer coordination.

![Functional decomposition](assets/functional-decomposition.svg)

## Architecture, interfaces and lifecycle

<table>
<tr>
<td width="50%"><img src="assets/mbse-system-architecture.svg" alt="Logical aircraft-level system architecture"></td>
<td width="50%"><img src="assets/systems-engineering-lifecycle.svg" alt="Retrospective systems engineering lifecycle"></td>
</tr>
</table>

These are **retrospective public-safe engineering views** built from the surviving project record. They are not substitutes for controlled aircraft wiring or proprietary installation drawings.

## Prototype identity and configuration control

![Configuration evolution](assets/configuration-evolution.svg)

| ID | Configuration |
|---|---|
| **CFG-000** | legacy aircraft baseline |
| **CFG-D1** | Dynon initial installed prototype |
| **CFG-D2** | Dynon post-replacement / reconfiguration state |
| **CFG-D3** | Dynon performance / customer-evaluation state |
| **CFG-G1** | Garmin G900X prototype/evaluation path |
| **CMP-G3X** | Garmin G3X comparison artefact; trade study only |

The separation matters because flight-test observations are valid only for the configuration in which they were obtained.

## Verification and discrepancy closure

![Verification thread](assets/mbse-verification-thread.svg)

The surviving record supports a genuine installed-aircraft loop:

**observe → isolate interface/configuration → engineer/OEM disposition → hardware/configuration action → restore settings/data → re-test / re-flight**

![Traceability matrix](assets/traceability-matrix.svg)

The detailed relationship set is machine-readable in [model/traceability.csv](model/traceability.csv), linking requirements, functions, interfaces, configurations, verification records, issues, risks, decisions and evidence.

## Source-backed export continuity

| Customer / operator | Publicly reported quantity | Source used here |
|---|---:|---|
| **Qatar** | 8 | [APP contract report](https://www.app.com.pk/national/pakistan-inks-accord-to-supply-8-mushshak-aircraft-to-qatar/) + [Qatar News Agency operational use](https://qna.org.qa/en/news/news-details?date=23%2F01%2F2024&id=0033-hh%C2%A0the-amir-patronizes%C2%A0graduation-ceremony-of%C2%A0al-zaeem-air-academy) |
| **Nigeria** | 10 | [APP delivery report — glass-cockpit aircraft](https://www.app.com.pk/national/pakistan-supplies-four-super-mushshak-to-naf/) + [Nigerian Air Force](https://airforce.mil.ng/news/pakistan-to-strengthen-technical%2C-defence-cooperation-with-nigerian-air-force361186473) |
| **Türkiye** | 52 | [APP contract report](https://www.app.com.pk/national/pakistan-to-supply-52-trainer-aircraft-to-turkey/) + [Turkish Ministry of National Defence induction](https://www.msb.gov.tr/SlaytHaber/1d609ba0df7c40039347230972cec89b) |
| **Azerbaijan** | 10 | [APP / PAC-PAF sale report](https://www.app.com.pk/national/pakistan-signs-agreement-with-azerbaijan-for-sale-of-10-super-mushshak-aircraft/) |
| **2016–2017 total** | **80** | cross-checked by [Asian Military Review](https://www.asianmilitaryreview.com/2019/01/super-mushshaks-super-popular/) |

For the avionics mapping in that export sequence, the specialist source identifies **Qatar — Garmin 950; Nigeria — Dynon; Türkiye — Garmin 950; Azerbaijan — not identified in that article**.

## Digital thread → digital twin

![Digital twin roadmap](assets/digital-twin-roadmap.svg)

The historical reconstruction now feeds a digital-engineering backbone:

**evidence → claims → requirements → functions → interfaces → configurations → verification → issues/risks → decisions**

The next step is an executable Super Mushshak digital twin built only from releasable, defensible source data: electrical/interface behaviour, failure-state logic, maintenance/health state, data replay and verification scenarios.

## Public-release boundary

The repository excludes security markings, private correspondence, personal data, controlled drawings, detailed pin/connector data, exact harness routes and proprietary internal installation detail. Project photographs may be cropped, enhanced and redacted for privacy/security, but aircraft/cockpit content is not synthetically generated or replaced.

## Technical record

- [Systems-engineering case study](docs/engineering-case-study.md)
- [System context and functions](docs/system-context-and-functions.md)
- [Architecture and trade study](docs/architecture-trade-study.md)
- [Interface control](docs/interface-control.md)
- [Configuration management](docs/configuration-management.md)
- [Verification and flight test](docs/verification-and-flight-test.md)
- [Traceability and V&V](docs/traceability-and-vv.md)
- [Integration risk register](docs/integration-risk-register.md)
- [Customer evaluation and programme context](docs/field-evaluation-and-programme-context.md)
- [Independent public evidence](docs/public-operator-evidence.md)
- [Project + independent media gallery](docs/media-gallery.md)
- [Evidence register](docs/evidence-register.md)
- [Digital twin follow-on](docs/digital-twin.md)
- [Sources](docs/references.md)
- [Machine-readable model](model/README.md)

**Quality gate:** `python tools/validate_model.py` checks ID uniqueness, reference integrity, typed links and local Markdown/image paths. Engineering correctness and public-release suitability remain human review gates.
