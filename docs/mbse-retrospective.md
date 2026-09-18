# Retrospective MBSE Reconstruction

## Purpose

The original retrofit predates the MBSE workflow I would use today. The surviving engineering evidence is nevertheless sufficient to reconstruct a **traceable, public-safe system model** without inventing aircraft detail.

This is not a claim that SysML/MBSE artefacts existed during the original programme. It is a retrospective transformation of real project evidence into modern systems-engineering objects.

## Model chain

**Evidence → requirement/constraint → interface → configuration → verification → decision**

The machine-readable source for that chain is in the [model directory](../model/README.md).

## Stakeholder / system context

~~~mermaid
flowchart TB
    P[Pilot / instructor]
    A[Legacy training aircraft]
    R[Glass-cockpit retrofit]
    M[Maintenance / support]
    O[Avionics OEMs]
    T[Test / evaluation organisation]
    C[Customer / acceptance authority]

    P <--> R
    A <--> R
    R <--> M
    R <--> O
    T <--> R
    C <--> T
~~~

## Logical architecture

~~~mermaid
flowchart LR
    subgraph Aircraft
      PWR[Aircraft power]
      FS[Flight-state sensing]
      ES[Engine / airframe sensing]
      NAV[Legacy / retained NAV-COM]
      XPDR[Transponder]
      INT[Intercom / audio]
    end

    subgraph Retrofit
      AD[Air-data / attitude-heading functions]
      EMS[Engine-monitoring function]
      DISP[Glass displays / HMI]
      GW[Avionics interface / gateway]
      CFG[Software, settings & databases]
    end

    PWR --> AD
    PWR --> EMS
    PWR --> DISP
    FS --> AD --> DISP
    ES --> EMS --> DISP
    NAV <--> GW <--> DISP
    XPDR <--> GW
    DISP --> INT
    CFG --> DISP
    CFG --> EMS
~~~

This is a logical representation of evidence-backed functions and interfaces. It deliberately omits exact harness routing, connector/pin data and equipment location.

## Requirement model

The requirements file contains retrospectively normalised statements such as:

- primary flight information must be available in installed-aircraft operation;
- engine/airframe information must be integrated into the new cockpit;
- retained NAV/COM equipment must interoperate with the glass cockpit;
- aircraft electrical integration must support the avionics without unacceptable power/transient behaviour;
- replacement LRUs must allow controlled restoration of software/settings/databases;
- maintenance and spares support must be considered at fleet scale;
- qualification/certification fit must be assessed independently from functional capability.

Each requirement points to evidence and a verification method.

## Interface model

The interface register captures only interfaces demonstrated or clearly required by the surviving archive: aircraft power, sensing, display/HMI, GNS 430-family/ARINC integration, transponder, audio/alerting and configuration data.

The register intentionally uses logical interface names rather than publishing pins or wiring.

## Configuration model

The historical programme evolved. The model therefore separates:

- legacy aircraft baseline;
- early Dynon installed configuration;
- Dynon post-replacement/reconfiguration state;
- Dynon Qatar customer-evaluation state;
- Garmin G900X/G950-family prototype/evaluation track;
- Garmin G3X comparison artefact, which is **not** treated as an aircraft configuration.

## Verification model

Verification records are linked to the configuration in which the event occurred. This prevents a common retrospective error: treating a test result from one hardware/software/database state as evidence for every later state.

## Decision model

Decision records capture the engineering rationale that can be recovered safely, for example:

- using an avionics interface to integrate retained navigation equipment;
- treating LRU spares/OEM exchange as part of the maintenance concept;
- separating certification suitability from flight functionality;
- preserving G3X and G900X/G950 configuration identities;
- keeping the public model abstract where release evidence is insufficient.

## Digital-thread view

~~~mermaid
flowchart LR
    E[Evidence] --> R[Requirement]
    R --> I[Interface]
    R --> C[Configuration]
    I --> C
    C --> V[Verification]
    V --> D[Decision / disposition]
    D --> C
    V --> E2[Test evidence]
~~~

The result is intentionally smaller than a full aircraft model, but it is auditable. **Traceability is treated as more important than visual complexity.**
