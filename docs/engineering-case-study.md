# Systems Engineering Case Study

## Engineering problem

Modernising a legacy trainer with a glass cockpit is an aircraft-level integration problem. A display can work correctly on the bench and still fail to meet the aircraft need because power quality, sensor behaviour, legacy avionics, databases, configuration state, human-machine interface and maintainability all interact.

The modification boundary therefore included:

- primary flight-state sensing and presentation;
- engine/airframe sensing and indication;
- navigation and communication equipment;
- aircraft electrical supply and protection;
- cockpit displays, controls and alerting;
- avionics data interfaces;
- aircraft wiring/harness changes and physical installation;
- software, settings and database configuration;
- maintenance/support concept;
- installed-aircraft verification and flight-test feedback.

## Role

I served as the **lead systems engineer** for the modification and also performed hands-on avionics integration/test activity. Surviving period correspondence identifies me operationally as an **Integration Engineer** during the early Dynon work.

The public case study does not publish internal appointment documents or private correspondence. Instead, it reconstructs the engineering work from the technical issues, configuration changes, photographs and test events that survive.

## System boundary

~~~mermaid
flowchart LR
    A[Aircraft electrical system] --> R[Retrofit avionics]
    S[Flight / engine sensors] --> R
    L[Legacy NAV/COM / transponder] <--> R
    R <--> H[Pilot / instructor HMI]
    R <--> M[Maintenance / configuration]
    O[OEM engineering support] <--> M
    O <--> R
    T[Ground / flight test] --> R
    R --> T
~~~

The diagram is intentionally logical. It does not reproduce wiring, connector, pinout or installation-location data.

## What the surviving record demonstrates

### Installed-aircraft integration

The Dynon SkyView suite was installed and flown on the aircraft. An early troubleshooting exchange records that the aircraft flew two sorties before a display/power-related failure was observed on a subsequent engine start. This is direct evidence of installed-aircraft operation, not a laboratory-only demonstrator.

### Interface engineering

The archive contains direct technical exchanges covering:

- Garmin GNS 430-family integration;
- ARINC-429 interfacing;
- transponder interfacing;
- audio/alert-output questions;
- synthetic-vision and terrain-database behaviour;
- display/database configuration;
- sensor and indication behaviour.

The public model abstracts those interfaces and omits implementation details.

### Electrical integration and fault closure

The early prototype experienced a display power/internal-voltage failure during aircraft operation. Troubleshooting included aircraft power delivery, protection, hardware replacement, configuration restoration and re-test. This is a useful example of why COTS avionics retrofit requires system-level verification.

### Configuration management

After replacement displays were received, settings and databases had to be restored deliberately. OEM correspondence discusses backup settings, EMS configuration, terrain data and individual display state. The project therefore had a real configuration-management problem: the same physical aircraft could behave differently depending on hardware/software/database state.

### Maintainability and lifecycle support

The team asked the OEM how failed modules would be supported at fleet scale, what maintenance depth was realistic, and whether spares/LRU exchange was preferable to local board-level repair. This moved the decision space beyond acquisition price to operational supportability.

### Qualification and certification fit

The archive includes questions on environmental qualification, TSO status and suitability for the intended customer/aircraft context. Functional performance and certification acceptability were treated as separate engineering questions.

### Flight-test feedback

Flight-test observations were returned to engineering/OEM support and used to refine the configuration. Later records cover ADAHRS cross-check behaviour during performance testing/high-rate manoeuvre, EMS indication interference associated with radio PTT, and continued customer-evaluation flying.

## Engineering lifecycle reconstructed from evidence

~~~mermaid
flowchart TD
    N[Need / operational constraint] --> RQ[Requirement or engineering question]
    RQ --> TR[Trade / architecture decision]
    TR --> IN[Integration action]
    IN --> FC[Functional check]
    FC --> FT[Ground / flight verification]
    FT --> OB[Observation]
    OB --> AN[Analysis + OEM coordination]
    AN --> CC[Configuration change]
    CC --> FC
~~~

This is a retrospective abstraction. The project did not originally use this repository's MBSE notation.

## What is not claimed

This case study does not claim that:

- the public diagrams are original programme drawings;
- the G3X comparison configuration was the G900X/G950 prototype;
- generic Garmin reference architecture proves the exact aircraft-installed LRU set;
- the early retrofit alone caused later export sales;
- private/customer/OEM records are public release material.

The point of the repository is the engineering chain: **problem definition → architecture → interfaces → prototype → verification → issue closure → field evaluation**.
