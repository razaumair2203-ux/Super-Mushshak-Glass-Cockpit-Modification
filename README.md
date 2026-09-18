# Super Mushshak Glass-Cockpit Modification

**Aircraft systems engineering · avionics integration · prototype development · ground and flight test**

This repository documents my work on the early Super Mushshak glass-cockpit modification programme, where I served as **Systems Engineering Lead** and supported integration, ground test, flight test and overseas evaluation activity.

The modification was an aircraft-level retrofit rather than a display replacement. It required coordinated changes across the cockpit displays, aircraft sensors, navigation/communication equipment, electrical interfaces, wiring harnesses, installation, configuration and verification.

<p align="center">
  <img src="assets/photos/flight-test-cockpit.jpg" width="900" alt="Super Mushshak glass-cockpit flight-test configuration">
</p>

## Engineering scope

The programme included:

- evaluation of alternative glass-cockpit architectures, including Dynon SkyView and Garmin-family solutions;
- replacement and integration of the aircraft sensor suite;
- cockpit and equipment-layout integration;
- complete aircraft wiring-harness and interface changes associated with the retrofit;
- integration of flight, navigation, communication and engine/airframe information;
- prototype troubleshooting and configuration refinement;
- ground-run and flight-test activity;
- technical support during overseas customer evaluation and international demonstration.

The surviving project comparison material shows that the candidate architectures were evaluated on more than display specifications. The trade study considered cockpit layout, engine display, navigation/communication integration, synthetic vision, training cues, alerting, ergonomics, reliability, third-party integration, OEM support and cost.

![System engineering view](assets/system-architecture.svg)

## Systems-engineering view

The central engineering problem was managing interfaces between the existing aircraft and a new integrated avionics environment:

| Workstream | Engineering focus |
|---|---|
| Requirements & architecture | Training-aircraft needs, cockpit functions, candidate architecture trade-offs |
| Sensors & data | Air data, attitude/heading, engine and airframe sensing |
| Avionics integration | Displays, navigation/communication equipment and associated interfaces |
| Electrical & installation | Power, protection, equipment installation and aircraft wiring harness |
| Human-machine interface | Instructor/student usability, readability and cockpit layout |
| Verification | Integration checks, ground run, flight test and defect closure |
| Configuration | Prototype changes, interface consistency and repeatable aircraft configuration |

More detail is provided in [Systems Engineering Case Study](docs/engineering-case-study.md) and [Architecture Trade Study](docs/architecture-trade-study.md).

## Prototype and test evidence

<table>
<tr>
<td width="50%"><img src="assets/photos/ground-run-trial.jpg" alt="Super Mushshak ground-run test"></td>
<td width="50%"><img src="assets/photos/international-airshow.jpg" alt="Super Mushshak international airshow display"></td>
</tr>
<tr>
<td><b>Ground-run / overseas evaluation activity.</b> Location-identifying background detail has been removed.</td>
<td><b>International airshow display period.</b> Personal identification details have been removed.</td>
</tr>
</table>

The photographs in this repository are original project-period images. They have only been cropped, exposure/contrast corrected where necessary, and redacted for privacy; aircraft or equipment content has not been synthetically generated or replaced.

## From retrofit to digital twin

The glass-cockpit programme is now being carried forward into a **Super Mushshak Digital Twin** project.

The digital-twin work is a new, ongoing effort. Its systems-engineering foundation is the same one used during the aircraft retrofit: establish the platform configuration, decompose the aircraft into systems and interfaces, connect requirements to verification evidence, and progressively build a traceable digital representation of the aircraft.

![Digital twin systems view](assets/digital-twin-systems-view.svg)

See [Digital Twin — Current Follow-on Work](docs/digital-twin.md).

## Programme progression

The glass-cockpit Super Mushshak was publicly displayed at the Dubai Airshow in 2011. Later public reporting shows the aircraft family being offered with glass-cockpit configurations and subsequently exported to additional customers. This repository separates that programme-level history from my individual engineering contribution.

See [Programme Progression](docs/programme-impact.md) and [References](docs/references.md).

## Repository contents

- [Systems Engineering Case Study](docs/engineering-case-study.md)
- [Architecture Trade Study](docs/architecture-trade-study.md)
- [Verification & Flight Test](docs/verification-and-flight-test.md)
- [Programme Progression](docs/programme-impact.md)
- [Digital Twin — Current Follow-on Work](docs/digital-twin.md)
- [References](docs/references.md)
