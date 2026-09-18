# Engineering Case Study

## 1. Engineering objective

Modernise the Super Mushshak cockpit from a predominantly analogue training-aircraft environment to an integrated digital flight deck while preserving the aircraft's basic-training role, instructor/student usability, aircraft safety, maintainability and future upgrade path.

The systems-engineering challenge was aircraft-level: display replacement drove changes to sensing, data interfaces, electrical integration, panel layout, wiring, configuration, maintenance philosophy and verification.

## 2. Functional decomposition

A glass-cockpit modification can be decomposed into the following aircraft functions:

1. **Flight-state sensing** — attitude, heading, acceleration, airspeed, altitude, vertical speed and temperature.
2. **Navigation** — position, map/navigation database, route guidance and radio navigation as configured.
3. **Communication** — cockpit radio control, audio and associated control/annunciation.
4. **Engine/airframe monitoring** — conversion of analogue sensor signals into digital indications and alerts.
5. **Pilot display/HMI** — PFD/MFD presentation, reversionary use, alerting, training readability and instructor awareness.
6. **Aircraft interfacing** — electrical power, circuit protection, discrete I/O, serial data, antennas, sensors and existing equipment.
7. **Maintenance/configuration** — replaceable modules, configuration control, calibration and fault isolation.

## 3. Early architecture trade space

The programme evaluated more than one digital-flight-deck approach. Surviving project material shows:

- **Dynon SkyView** as a dual large-display candidate with strong integration/customisation flexibility.
- A **Garmin-family** candidate as the alternative integrated architecture.

Later public Super Mushshak material identifies Garmin G950 and Dynon SkyView as production/export options. Because archival project files contain inconsistent early Garmin nomenclature, this public repository deliberately avoids assigning a precise model to the earliest Garmin prototype until the original integration records are reconciled.

### Representative architecture concerns

- display count and cockpit symmetry;
- PFD/MFD redundancy and reversion;
- AHRS/ADAHRS and magnetometer installation constraints;
- air-data sensor integration and calibration;
- engine/airframe sensor conversion;
- GPS / NAV / COM integration;
- transponder and audio-panel integration;
- data-bus and serial-interface compatibility;
- electrical load, power quality and protection;
- wiring-harness routing and maintainability;
- panel structural/layout constraints;
- human factors for ab-initio training;
- OEM support and long-term upgradeability.

## 4. Interface-control problem

The modification crossed multiple aircraft domains. A simplified interface model is:

    Aircraft sensors ──┐
    Air-data sources ──┤
    Attitude/heading ──┤
    Engine sensors ────┤
    GPS/NAV/COM ───────┼──> Avionics integration layer ──> PFD / MFD / alerts
    Audio / radio ─────┤
    Power & discretes ─┤
    Existing systems ──┘
                             │
                             └──> configuration / calibration / maintenance

The engineering value lies in managing the **interfaces and verification closure**, not the screens themselves.

## 5. Integration work represented by this portfolio

The public case study will document only high-level, non-sensitive evidence of:

- system-level requirements and trade-offs;
- sensor-suite replacement;
- complete aircraft harness/interface coordination;
- panel and equipment integration;
- ground functional testing;
- flight-test participation;
- overseas evaluation/trial support;
- configuration evolution from prototype to later production/export offerings.

Detailed wiring diagrams, pinouts, configuration files, test limits and restricted programme data will not be published.

## 6. Recruiter relevance

This project is most relevant to roles in:

- aircraft systems engineering;
- avionics integration;
- platform modification / retrofit;
- V&V and flight test;
- technical programme leadership;
- certification/airworthiness support;
- supplier/OEM integration;
- defence and civil aerospace product development.
