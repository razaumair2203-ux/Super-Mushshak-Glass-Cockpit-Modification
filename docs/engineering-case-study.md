# Systems Engineering Case Study

## Engineering problem

Modernising a legacy training aircraft with a glass cockpit created an **aircraft-level integration problem**, not a display-installation task.

The engineering boundary included:

- flight-state sensing;
- engine and airframe sensing;
- cockpit displays and controls;
- navigation and communication equipment;
- aircraft power and electrical behaviour;
- equipment installation and wiring;
- warnings and audio functions;
- databases and avionics configuration;
- pilot/instructor human-machine interface;
- maintainability and OEM support;
- verification, flight-test feedback and configuration control.

A change in any one area could propagate into several others. The project therefore had to be managed as a system of interacting functions and interfaces.

## My role

I served as the **lead systems engineer** for the retrofit programme. Surviving period documentation identifies my formal programme appointment as **PM System Engineering**.

A signed 2010 design/options study authored under that appointment is the strongest surviving evidence of role ownership. It covers the aircraft baseline, candidate glass-cockpit approaches, installation and electrical constraints, system components, trade-offs, recommendations and the proposed development path.

My work subsequently included:

- requirements interpretation and architecture trade studies;
- avionics and sensor-suite integration;
- interface definition and OEM technical coordination;
- retrofit wiring/harness and installation coordination;
- technical evaluation of alternative cockpit suites;
- prototype troubleshooting and configuration refinement;
- ground and flight-test support;
- customer-evaluation technical support;
- continued configuration/equipment follow-up.

## Requirements and constraints

The archive shows that the decision space extended well beyond display size or price.

### Aircraft configuration

The starting point was a legacy cockpit with conventional instruments, existing navigation/communication equipment, aircraft-specific sensing and finite electrical/installation capacity. Any retrofit had to respect the aircraft as-built configuration.

### Flight-state and engine sensing

The new cockpit needed dependable sources for air-data, attitude/heading and engine/airframe information. This drove sensor selection, interface definition, calibration, display configuration and failure/troubleshooting work.

### Avionics interfaces

Direct OEM exchanges from 2010 include technical questions on **ARINC-429**, third-party radio integration, database/configuration behaviour and avionics interoperability. These are direct indicators of interface-engineering work rather than generic project-management activity.

### Electrical integration

The project archive includes aircraft-power budgeting and direct troubleshooting of electrical-transient behaviour observed during integration. The public repository deliberately omits sensitive implementation values and wiring detail.

### Human-machine interface

The platform was a training aircraft. The architecture therefore had to support both aircraft operation and the instructional environment: display readability, information distribution, alerting, backup information and cockpit usability mattered alongside pure avionics capability.

### Qualification, reliability and maintainability

OEM correspondence and customer-evaluation material includes environmental qualification, reliability, maintainability, redundancy, supportability and post-installation test questions. These were part of the engineering trade space.

## Interface management in practice

Several surviving exchanges show the practical form of systems engineering on the programme:

- clarifying data-bus and equipment-interface capability with the OEM;
- resolving display and database configuration after hardware changes;
- investigating aircraft electrical effects on avionics;
- integrating navigation/communication equipment into the revised cockpit;
- addressing sensor and indication behaviour through test and configuration changes;
- feeding flight-test observations back to the vendor and engineering team.

The important point is not a particular connector or pinout. It is the **closed engineering loop between aircraft, avionics, OEM, test evidence and configuration**.

## Configuration evolution

The programme did not follow one frozen cockpit concept from day one. It explored and matured multiple candidate solutions.

Two principal tracks are retained in this public reconstruction:

1. **Dynon SkyView prototype track** — supported by original cockpit photographs, direct OEM correspondence and flight-test records.
2. **Garmin G900/G950-family track** — supported by formal trade/evaluation material and customer-facing technical work.

Other period records also reference Garmin G3X. The archive therefore reflects an evolving development programme; the public case study preserves that ambiguity instead of retrospectively forcing a single unsupported configuration label.

## Verification philosophy

The surviving records support an iterative verification pattern:

**engineering issue / requirement → configuration or installation action → functional check → ground or flight test → observation → engineering/OEM resolution → configuration update → re-test**

This is a retrospective abstraction of documented activity, not an original programme flowchart.

See [Verification & Flight Test](verification-and-flight-test.md) and [Evidence & Provenance](evidence-and-provenance.md).
