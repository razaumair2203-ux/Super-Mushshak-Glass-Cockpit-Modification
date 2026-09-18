# Retrospective MBSE Reconstruction

## Purpose

The original retrofit predates the MBSE workflow I would use today. The surviving engineering evidence is nevertheless sufficient to reconstruct a **traceable, public-safe system model** without inventing aircraft detail.

This is not a claim that SysML/MBSE artefacts existed during the original programme. It is a retrospective transformation of real project evidence into modern systems-engineering objects.

## Recruiter-scale architecture view

![Public-safe logical architecture](../assets/mbse-system-architecture.svg)

The diagram is deliberately rendered as a large SVG rather than a compact Mermaid figure so the system boundary, sensor/power interfaces, retrofit functions, test/evaluation loop and lifecycle-support interfaces remain legible on a normal GitHub page.

It is a logical representation of evidence-backed functions and interfaces. It deliberately omits exact harness routing, connector/pin data and equipment location.

## Model chain

**Evidence → requirement/constraint → interface → configuration → verification → decision**

![Evidence-to-verification digital thread](../assets/mbse-verification-thread.svg)

The machine-readable source for that chain is in the [model directory](../model/README.md).

## Stakeholder / system context

The reconstructed context includes:

- pilot / instructor;
- legacy training-aircraft baseline;
- glass-cockpit retrofit;
- aircraft sensing and electrical systems;
- avionics OEMs and technical support;
- maintenance / fleet support;
- test and evaluation organisation;
- customer / acceptance authority.

The purpose of this level is not to draw every aircraft connection. It is to expose the **system boundary, external actors, engineering interfaces and evidence flow** that drove integration decisions.

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

![Configuration evolution](../assets/configuration-evolution.svg)

The historical programme evolved. The model therefore separates:

- legacy aircraft baseline;
- early Dynon installed configuration;
- Dynon post-replacement/reconfiguration state;
- Dynon Qatar customer-evaluation state;
- Garmin G900X/G950-family prototype/evaluation track;
- Garmin G3X comparison artefact, which is **not** treated as an aircraft configuration.

## Verification model

![Requirements-to-verification cross-reference](../assets/traceability-matrix.svg)

Verification records are linked to the configuration in which the event occurred. This prevents a common retrospective error: treating a test result from one hardware/software/database state as evidence for every later state. The matrix is intentionally sparse where the surviving archive does not justify a direct link.

The evidence supports a closed loop of **installed check → flight test → observed discrepancy → engineering/OEM resolution → configuration update → re-test**. Examples are abstracted in the public model rather than exposing controlled implementation detail.

## Decision model

Decision records capture engineering rationale that can be recovered safely, for example:

- using an avionics interface to integrate retained navigation equipment;
- treating LRU spares/OEM exchange as part of the maintenance concept;
- separating certification suitability from flight functionality;
- preserving G3X and G900X/G950 configuration identities;
- keeping the public model abstract where release evidence is insufficient.

## Why this is MBSE rather than diagram decoration

The diagrams are views. The model is the linked data underneath them:

**evidence IDs ↔ requirement IDs ↔ interface IDs ↔ configuration IDs ↔ verification IDs ↔ decision records**

The CSV objects therefore correspond conceptually to requirement, block/interface, configuration, verification and decision elements that can later be migrated into SysML/Capella/Cameo or connected to a requirements tool. The key property already exists: **stable identity and traceability**.

The result is intentionally smaller than a full aircraft model, but it is auditable. **Traceability is treated as more important than visual complexity.**
