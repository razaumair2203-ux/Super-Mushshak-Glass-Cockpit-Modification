# Systems-Engineering Method

This case study is organised around the **aircraft-level engineering lifecycle**, not around equipment features or presentation material.

![Systems-engineering lifecycle](../assets/systems-engineering-lifecycle.svg)

## 1. System-of-interest definition

The system of interest is the **Super Mushshak glass-cockpit retrofit**. The public boundary includes sensing, displays, navigation/communication integration, retained avionics, aircraft electrical integration, physical installation and modification harness, configuration data, HMI, verification and lifecycle support.

The public boundary excludes exact pins, harness routes, controlled drawings, precise internal locations, proprietary implementation detail and private correspondence.

See [System context and functional decomposition](system-context-and-functions.md).

## 2. Operational need and constraints

The retrofit addressed modernisation of a legacy training aircraft while retaining suitability for training use, installed-aircraft operation, maintainability and customer/acceptance evaluation.

Project records show that constraints were not limited to display capability. Integration had to consider:

- aircraft electrical supply and protection;
- sensor and engine/airframe measurement paths;
- retained navigation/communication and other avionics;
- physical installation and cabling;
- software, settings and databases;
- pilot/instructor interaction;
- qualification / certification suitability;
- maintenance depth, spares and OEM support.

## 3. Requirement normalisation

Project records are mapped into public requirement statements where they support the underlying system need. Each requirement has a stable identifier, basis, verification method and evidence links.

The requirement set covers primary flight information, engine/airframe information, NAV/COM integration, electrical integration, configuration restoration, retained-system interfaces, installed-aircraft V&V, maintainability, qualification/certification fit, failure response, HMI/training suitability and configuration identity.

Source: [model/requirements.csv](../model/requirements.csv).

## 4. Functional decomposition

Functions are separated from equipment so that the architecture remains valid across configuration alternatives.

The top-level functions are:

1. sense flight state;
2. sense engine/airframe state;
3. present flight and engine information;
4. integrate NAV/COM and retained systems;
5. provide alert/audio and HMI functions;
6. integrate aircraft electrical and physical/harness changes;
7. manage software/settings/databases and configuration state;
8. verify the installed aircraft and close discrepancies;
9. support maintenance, replacement and OEM interaction.

Source: [model/functions.csv](../model/functions.csv).

## 5. Architecture alternatives

Architecture is modelled as functions and logical interfaces first, then tied to identified configuration states.

The critical configuration rule is:

- **Dynon SkyView** installed-prototype evidence remains on the Dynon branch;
- **Garmin G900X/G950-family** material remains on its separate prototype/evaluation branch;
- **Garmin G3X** comparison material is retained as trade-study evidence only.

Generic OEM architecture can inform design understanding but cannot be promoted into aircraft-specific installation evidence.

## 6. Interface control

Interfaces are controlled at the public logical level: power, sensor/data, NAV/COM, transponder, audio/alerts, configuration data, HMI and maintenance/OEM support.

The public model remains at logical-interface level; pin-level implementation and routing detail remain controlled.

See [Interface control](interface-control.md) and [model/interfaces.csv](../model/interfaces.csv).

## 7. Physical and electrical integration

The retrofit is represented as a real aircraft modification:

- revised sensor-suite integration;
- instrument/panel and equipment installation;
- aircraft electrical supply/protection integration;
- complete modification wiring-harness change;
- retained-aircraft-system interfaces;
- software/settings/database loading.

The period engineering record shows that power quality, configuration restoration and cross-domain interference were practical integration issues rather than theoretical concerns.

## 8. Configuration management

An aircraft test result is meaningful only when the hardware/software/database state is identifiable.

Configuration states therefore track:

- prototype branch;
- significant hardware/LRU change;
- software/settings/database restoration where evidenced;
- evaluation/test state;
- evidence boundary and open / unpublished detail.

See [Configuration management](configuration-management.md).

## 9. Verification and discrepancy closure

The closed-loop rule is:

**identified configuration → installed check / flight event → observation → analysis → disposition → configuration update → re-verification**

A result observed in one configuration is not inherited automatically by another.

Where final closure evidence is absent, the public repository marks the detailed closure record as **not published** rather than inventing a closure state.

See [Verification and flight test](verification-and-flight-test.md) and [Assurance and closure summary](assurance-closure-summary.md).

## 10. Integration-risk control

The systems model separates **issues** from **risks**.

Issues describe something actually observed. Risks capture the broader engineering concern that observation exposes, for example:

- power/transient susceptibility;
- loss of valid configuration after LRU replacement;
- cross-domain radio/sensing interaction;
- high-dynamic attitude-reference behaviour;
- retained-avionics compatibility;
- supportability / aircraft-on-ground exposure.

The public model does not assign probability or severity values because the programme safety artefacts are controlled and outside this release.

See [Integration risk register](integration-risk-register.md) and [model/risks.csv](../model/risks.csv).

## 11. Validation / customer evaluation

Customer evaluation is treated as system-validation context. It can demonstrate repeated operation and expose operational suitability issues, but it does not substitute for qualification or certification evidence.

## 12. Evidence and claim control

Every public claim is linked to one of five states:

- **observed** — directly evidenced by project material;
- **documented** — stated by OEM/reference or public programme source;
- **engineering-derived** — current engineering normalisation from identified evidence;
- **public-summary** — the engineering point is represented while detailed historical baseline data is not published;
- **not published** — detail is outside the public evidence/release boundary.

Technical claims, role claims and programme/commercial claims are controlled separately.

The public claim register is [model/claims.csv](../model/claims.csv).

## 13. Quality gate

Before publication, each artefact is checked for:

- technical correctness;
- configuration identity;
- evidence provenance;
- readability at normal GitHub scale;
- link integrity;
- terminology consistency;
- public-release suitability;
- duplication;
- unsupported claims;
- actual systems-engineering value.

The aim is an auditable, recruiter-readable technical record with engineering depth rather than decorative diagram density.
