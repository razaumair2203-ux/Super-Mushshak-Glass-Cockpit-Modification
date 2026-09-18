# Retrospective MBSE Reconstruction

## Purpose

The original retrofit predates the current retrospective MBSE reconstruction. The surviving engineering evidence is sufficient to build a **traceable, public-safe system model** without inventing aircraft detail.

This is not a claim that SysML/MBSE artefacts existed during the original programme. It is a modern transformation of surviving evidence into controlled systems-engineering objects.

## System context and functions

![System context](../assets/system-context.svg)

![Functional decomposition](../assets/functional-decomposition.svg)

The reconstruction begins with the system boundary and stakeholders, then separates equipment-independent functions from configuration-specific implementation.

This prevents two common retrospective errors:

- filling gaps with “typical aircraft” detail; and
- treating a generic OEM architecture as the installed aircraft baseline.

## Logical architecture

![Public-safe logical architecture](../assets/mbse-system-architecture.svg)

The logical view represents evidence-backed functions and interfaces. It deliberately omits exact harness routing, connector/pin data, precise internal locations and controlled implementation detail.

## Model chain

**Evidence → claim → requirement → function → interface → configuration → verification / issue / risk → decision**

![Evidence-to-verification digital thread](../assets/mbse-verification-thread.svg)

The machine-readable source is in the [model directory](../model/README.md).

## Stakeholder / system context

The public context includes pilot/instructor, legacy aircraft baseline, integration engineering, maintenance/fleet support, avionics OEM support, flight-test/evaluation activity and customer/acceptance stakeholders.

The purpose of this level is to expose the **system boundary, external actors, engineering interfaces and evidence flow** that drove integration decisions, not organisational structure.

## Requirement model

The requirements file contains retrospectively normalised statements for:

- primary flight information;
- engine/airframe information;
- NAV/COM and retained-system integration;
- aircraft electrical integration;
- physical installation / modification harness;
- configuration restoration;
- installed-aircraft verification;
- maintainability and spares;
- qualification/acceptance fit;
- failure response;
- HMI/training suitability;
- configuration identity;
- evidence integrity.

Each requirement points to functions, evidence and a verification method.

## Function and interface model

The function model remains equipment-independent. The interface register then captures only interfaces demonstrated or clearly required by the evidence: aircraft power, sensing, display/HMI, retained-navigation integration, transponder, audio/alerting, configuration data, physical/harness integration and lifecycle support.

The register intentionally uses logical interface names rather than publishing pins or wiring.

## Configuration model

![Configuration evolution](../assets/configuration-evolution.svg)

The historical programme is separated into:

- legacy aircraft baseline;
- early Dynon installed configuration;
- Dynon post-replacement/reconfiguration state;
- Dynon customer-evaluation state;
- Garmin G900X/G950-family prototype/evaluation track;
- Garmin G3X comparison artefact, which is **not** treated as an aircraft configuration.

## Verification, issue and risk model

![Requirements-to-verification cross-reference](../assets/traceability-matrix.svg)

Verification records are linked to the configuration in which the event occurred. Issues are separate objects so an observed discrepancy cannot silently become a “closed” result.

The evidence supports an iterative loop of **installed check → flight test → observed discrepancy → engineering/OEM analysis → disposition/configuration update → re-test**. Where final closure evidence is absent, the issue remains explicitly **not reconstructed**.

The risk register then abstracts the engineering concern exposed by those events — for example power/transient behaviour, configuration restoration or cross-domain interaction — and traces it back to the requirements/interfaces it threatens.

This separation matters:

- **ISS-###** = something observed;
- **RSK-###** = the engineering exposure that must be controlled.

No historical formal safety process is invented.

## Decision model

Decision records capture recoverable engineering rationale such as:

- using/assessing an avionics interface for retained navigation integration;
- treating LRU spares/OEM exchange as part of the maintenance concept;
- separating acceptance/certification suitability from flight functionality;
- preserving G3X and G900X/G950 configuration identities;
- withholding implementation detail while retaining logical traceability;
- not inventing closure when evidence is incomplete.

## Role and programme claims

The model also separates claims that sit outside the technical requirement chain:

- **CLM-011 / E-25** — retrospective Lead Systems Engineer role statement;
- **CLM-010 / E-16** — later four-customer 80-aircraft programme sequence;
- **CLM-012 / E-17/E-18** — attributed public commercial-value context.

This prevents a role claim or later market outcome from contaminating the technical evidence chain.

## Stable identities

The diagrams are views. The model is the linked data underneath them:

**E / CLM ↔ REQ ↔ FUN ↔ IF ↔ CFG ↔ VER / ISS / RSK ↔ DEC**

The CSV objects can later migrate into SysML/Capella/Cameo, a requirements tool or graph database without changing their public identities.

The quality criterion is **stable identity, evidence provenance, configuration specificity, traceability, risk discipline and explicit handling of unknowns**.
