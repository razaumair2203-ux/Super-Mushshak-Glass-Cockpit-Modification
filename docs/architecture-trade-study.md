# Architecture and Trade Study

## Why configuration identity matters

The surviving archive contains several Garmin names created at different points in the programme. They must not be collapsed into one architecture.

1. **Dynon SkyView** — installed prototype with strong photographic, OEM-correspondence and flight-test evidence.
2. **Garmin G900X/G950 family** — separate prototype/evaluation track supported by G900X/G950 technical material, a G950 customer-focused presentation and later G900X configuration correspondence.
3. **Garmin G3X** — appears in a 2012 Dynon-vs-G3X comparison deck. It is treated here as a comparative candidate, not as proof of the G900X/G950 aircraft configuration.

## Dynon SkyView track

The period comparison material describes a two-large-display SkyView layout with a central navigation/communication display. The broader project archive shows that the aircraft integration also involved flight/engine sensing, legacy avionics, aircraft power, configuration databases and supportability.

Strongest evidence on this track:

- original installed-cockpit photographs;
- in-flight display photographs;
- OEM interface and troubleshooting correspondence;
- GNS 430-family / ARINC integration activity;
- first-sortie and continuing flight-test feedback;
- Qatar evaluation records.

## Garmin G900X/G950-family track

The Garmin G900X/G950 installation material describes an integrated modular architecture with PFD/MFD displays and multiple LRUs for air data, attitude/heading, engine/airframe data, NAV/COM, audio and transponder functions. The official reference architecture uses redundant/high-speed data paths and modular LRUs.

That OEM architecture is useful for understanding the design space, but this repository does **not** copy the generic vendor diagram and present it as the exact Super Mushshak installation.

The Qatar-focused G950 presentation also treats the system as a dual-display integrated flight deck with reversionary capability, air-data/AHRS, engine indication and integrated communication/navigation functions. Again, it is used as architecture/evaluation evidence rather than as a substitute for an aircraft-specific released drawing.

## G3X comparative deck

The 2012 comparison deck records a separate trade exercise. It describes:

- Dynon SkyView as a two-10.4-inch-display solution with a centre NAV/COM display;
- Garmin G3X as a three-7-inch-display solution with a centre NAV/COM display;
- both candidates providing PFD/MFD, engine display, radio/NAV integration, synthetic vision, GPS and moving-map capability;
- qualitative differences in ergonomics, display arrangement, warnings/features, integration flexibility, build quality, OEM support and price.

Those observations are useful because they show a multi-criteria decision process. They are not used to rewrite the identity of the G900X/G950 prototype.

## Aircraft-level trade dimensions

| Dimension | Engineering question |
|---|---|
| Functional coverage | Does the candidate provide the flight, engine, NAV/COM, alerting and mapping functions required? |
| Sensor architecture | What air-data, attitude/heading and engine/airframe sensing must change? |
| Legacy compatibility | Which existing radios/transponder/aircraft systems can be retained and interfaced? |
| Electrical integration | Can the aircraft supply the loads with adequate protection and acceptable transient behaviour? |
| Interface burden | What digital, analogue or discrete interfaces are required? |
| Physical installation | What panel, equipment, harness and installation changes are introduced? |
| HMI / training suitability | Is information distribution usable for instructor/student operation? |
| Redundancy / failure response | What capability remains after display/LRU failure? |
| Qualification / certification | Is the evidence basis appropriate to the aircraft and customer acceptance route? |
| Maintainability | What can be replaced locally, what requires OEM repair, and what spares are needed? |
| Configuration management | How are software, settings and databases controlled after equipment changes? |
| Upgradeability | Can future equipment/functions be incorporated without major redesign? |
| Lifecycle cost | What is the aircraft-level integration/support burden, not only purchase price? |

## Trade-study conclusion

The engineering value is not a retrospective declaration of a single universal winner. The programme explored more than one COTS architecture and discovered that **interface burden, supportability, certification fit and configuration control can dominate headline equipment capability**.

See [Structured model](../model/README.md) for the linked requirements, interfaces, decisions and verification evidence.
