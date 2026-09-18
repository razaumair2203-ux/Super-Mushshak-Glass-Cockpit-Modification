# Systems Engineering Case Study

## Engineering problem

Modernising a legacy trainer with a glass cockpit is an **aircraft-level retrofit programme**, not a display-swap exercise. Bench-compatible COTS equipment can still fail at aircraft level because power quality, sensors, retained avionics, physical installation, databases, configuration state, pilot/instructor HMI, qualification evidence, maintainability and flight behaviour interact.

The modification boundary therefore included:

- primary flight-state sensing and presentation;
- engine/airframe sensing and indication;
- navigation and communication equipment;
- aircraft electrical supply, protection and transient behaviour;
- cockpit displays, controls, audio and alerting;
- avionics data interfaces;
- complete aircraft wiring/harness and associated installation changes;
- software, settings and database configuration;
- maintainability, spares and OEM support;
- installed-aircraft verification and discrepancy closure;
- flight-test feedback and customer evaluation.

## Role and engineering accountability

I served as the **lead systems engineer** for the modification and also performed hands-on avionics integration/test activity. Surviving period correspondence identifies me operationally as an **Integration Engineer** during the early Dynon work.

The portfolio intentionally demonstrates the role through the engineering chain rather than through an unsupported job-title claim: architecture decisions, interface questions, installed-aircraft discrepancies, configuration restoration, OEM resolution, flight-test feedback and customer evaluation are all traceable to surviving evidence.

## System boundary and interfaces

![Public-safe logical architecture](../assets/mbse-system-architecture.svg)

This is the public-safe logical view of the retrofit. It is deliberately large enough to be read on GitHub without opening a tiny embedded diagram.

The architecture separates:

1. **aircraft baseline** — power, retained avionics and audio;
2. **sensor suite** — air-data/attitude-heading and engine/airframe sensing;
3. **retrofit avionics** — displays, NAV/COM interface layer and configuration data;
4. **human system** — pilot/instructor HMI and alerts;
5. **verification system** — ground checks, flight test and discrepancy feedback;
6. **lifecycle system** — OEM support, spares, LRU replacement and configuration restoration.

Exact wiring, connector, pinout and installation-location data are intentionally omitted.

## Architecture alternatives and configuration identity

Two genuine prototype/evaluation tracks are kept separate:

- **Dynon SkyView** — strongest surviving installed-aircraft and flight-test evidence;
- **Garmin G900X/G950 family** — separate integrated-flight-deck prototype/evaluation path.

A 2012 **Garmin G3X** comparison deck is retained only as a trade-study artefact. It is not renamed to make the Garmin prototype look better or simpler. This distinction matters because systems-engineering evidence loses value if configuration identities are merged retrospectively.

## What the surviving record demonstrates

### 1. Installed-aircraft integration

The Dynon SkyView suite was installed and flown on the aircraft. An early troubleshooting exchange records that the aircraft flew two sorties before a display/power-related failure was observed on a subsequent engine start. This is direct evidence of an installed-aircraft prototype, not a laboratory-only demonstrator.

### 2. Interface engineering

The archive contains direct technical exchanges covering:

- Garmin GNS 430-family integration;
- ARINC-429 interfacing;
- transponder interfacing;
- audio/alert-output questions;
- synthetic-vision and terrain-database behaviour;
- display/database configuration;
- sensor and engine-indication behaviour.

The public model abstracts those interfaces rather than exposing implementation detail.

### 3. Electrical integration and fault closure

The early prototype experienced a display power/internal-voltage failure during aircraft operation. Troubleshooting covered aircraft power delivery, protection, hardware replacement, configuration restoration and re-test. The lesson is aircraft-level: **COTS avionics capability does not remove platform integration risk**.

### 4. Configuration management

After replacement displays were received, settings and databases had to be restored deliberately. OEM correspondence discusses backup settings, EMS configuration, terrain data and individual display state. The same physical aircraft could therefore behave differently depending on hardware/software/database state.

The retrospective model records those states separately rather than writing a single timeless “prototype configuration.”

### 5. Maintainability and lifecycle support

The team asked the OEM how failed modules would be supported at fleet scale, what maintenance depth was realistic, and whether spares/LRU exchange was preferable to local board-level repair. This moves the trade space beyond purchase price into **availability, repair concept and fleet supportability**.

### 6. Qualification and certification fit

The archive includes questions on environmental qualification, TSO status and suitability for the intended customer/aircraft context. Functional performance and certification/acceptance suitability were therefore treated as separate engineering questions.

### 7. Flight-test feedback

Flight-test observations were returned to engineering/OEM support and used to refine the configuration. Later records cover ADAHRS cross-check behaviour during performance testing/high-rate manoeuvre, EMS indication interference associated with radio PTT, and continued customer-evaluation flying.

![Evidence-to-verification digital thread](../assets/mbse-verification-thread.svg)

This is the central engineering loop:

**known configuration → test/flight event → observation → analysis/OEM coordination → disposition → configuration change → re-test**

## Original visual evidence

The repository prioritises **authentic photographs** over decorative imagery:

- installed Dynon prototype cockpit;
- in-flight Dynon display;
- Qatar customer-evaluation period;
- period cockpit-in-flight / aerial test-flight archive;
- test-engineer in-flight context.

An aerial or personal photograph is used only for what it proves: **flight/test context and participation**. It is not silently promoted into configuration or verification evidence.

## Programme scale after the early retrofit work

![Programme impact timeline](../assets/programme-impact.svg)

Public records document **80 aircraft in four new-customer contracts during 2016–2017**: Nigeria 10, Qatar 8, Türkiye 52 and Azerbaijan 10. Public reporting also records Super Mushshak already in service with Saudi Arabia, Oman, Iran and South Africa, giving a documented 2017 foreign customer/service footprint across at least eight countries.

Nigeria's first delivery was explicitly reported as **glass-cockpit equipped**. That is useful evidence of product-modernisation continuity.

Two public value estimates — Nigeria at about **US$10.2m** and Türkiye at around **US$2m per aircraft** — imply more than **US$114m** for those two deals alone. The repository does not invent values for Qatar or Azerbaijan and does not attribute programme revenue to a single engineer.

## Evidence-to-model chain

The public MBSE reconstruction converts surviving evidence into linked model objects:

**evidence → requirement → interface → configuration → verification → decision**

The machine-readable files under [model](../model/README.md) give each object a stable ID so the diagrams are views of an auditable model rather than presentation graphics.

## What is not claimed

This case study does not claim that:

- the public diagrams are original programme drawings;
- SysML/MBSE tooling was used on the original programme;
- the G3X comparison configuration was the G900X/G950 prototype;
- generic Garmin reference architecture proves the exact aircraft-installed LRU set;
- an aerial/test-engineer photograph proves a technical test result by itself;
- the early retrofit or one engineer alone caused later export sales;
- private/customer/OEM records are public-release material.

The engineering value is the complete chain:

**need → trade study → architecture → interfaces → installation → configuration control → verification → discrepancy closure → customer evaluation → downstream programme context → digital-thread reconstruction**
