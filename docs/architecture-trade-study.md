# Architecture and Trade Study

## Configuration identity first

The surviving archive contains multiple avionics names created at different points in the programme. The trade record is useful only if those identities remain separate.

1. **Dynon SkyView** — installed prototype with strong photographic, OEM-support and flight-test evidence.
2. **Garmin G900X/G950 family** — separate prototype/evaluation path supported by OEM installation material, a G950-focused technical presentation and later G900X configuration correspondence.
3. **Garmin G3X** — appears in period comparison material and is retained as a comparative candidate only.

The G3X comparison is **not** used as proof of the G900X/G950 aircraft configuration.

## Dynon SkyView track

The period comparison material describes a two-large-display SkyView arrangement. The broader project archive demonstrates that the aircraft integration extended well beyond displays to sensing, retained avionics, power, configuration data, HMI and supportability.

Strong surviving evidence on this track includes installed cockpit photography, in-flight display photography, aircraft-level troubleshooting correspondence, navigation-data interface activity, settings/database restoration after display replacement, continuing flight-test feedback, performance testing and customer evaluation.

## Garmin G900X/G950-family track

Garmin installation documentation describes the G900X/G950 as a modular integrated avionics family composed of displays and multiple LRUs, with vendor-defined digital interfaces and support for third-party integration.

That is legitimate **OEM architecture evidence**. It is not automatically the Super Mushshak physical architecture.

The public model therefore uses the Garmin material to support modular LRU architecture, PFD/MFD and integrated avionics concepts, air-data / attitude-heading / engine-airframe functions, redundancy/reversion concepts and configuration/maintainability considerations.

It does **not** use the generic manual to assert the exact installed Super Mushshak LRU list, exact aircraft wiring, exact bus topology, harness routing, pinout or equipment location.

The exact public aircraft-installed Garmin baseline remains **partially reconstructed**.

## G3X comparative material

The 2012 comparison deck records a separate trade exercise. It compares display arrangement and functional capability and contains qualitative observations concerning HMI, feature set, integration flexibility, build quality, OEM support and price.

Those observations are useful as evidence of a multi-criteria decision process. They remain **comparison evidence**, not an installed-configuration record.

## Aircraft-level trade dimensions

| Dimension | Engineering question |
|---|---|
| Functional coverage | Does the candidate provide the flight, engine, NAV/COM, alerting and mapping functions required? |
| Sensor architecture | What flight-state and engine/airframe sensing changes are required? |
| Legacy compatibility | Which existing aircraft functions can be retained and interfaced? |
| Electrical integration | Can the aircraft support the loads with acceptable protection and transient behaviour? |
| Interface burden | What digital, analogue, discrete or audio interfaces are required? |
| Physical installation | What panel, equipment, structural-support and harness changes are introduced? |
| HMI / training suitability | Is information distribution usable for pilot/instructor operation? |
| Redundancy / failure response | What capability remains after display/LRU failure? |
| Qualification / acceptance fit | Is the evidence basis appropriate to the intended aircraft/customer route? |
| Maintainability | What is replaced locally, what returns to OEM, and what spares are required? |
| Configuration management | How are software, settings and databases controlled after equipment changes? |
| Upgradeability | Can future functions be added without disproportionate redesign? |
| Lifecycle burden | What integration/support burden follows the equipment choice? |

## Trade-study conclusion

The source record does not justify a retrospective universal “winner”. It does support a stronger systems-engineering conclusion:

> **aircraft-level interface burden, supportability, acceptance fit and configuration control can be as important as headline avionics capability.**

The structured decision and configuration objects are in [model](../model/README.md).
