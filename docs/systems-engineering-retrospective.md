# Systems-Engineering Retrospective

## Reconstructing the retrofit as a modern digital-engineering case study

The Super Mushshak glass-cockpit work predates the MBSE workflow I would use to structure the same problem today. The surviving archive is nevertheless rich enough to reconstruct the **engineering lifecycle** without inventing an aircraft architecture.

This page is therefore retrospective: it maps documented programme activity to contemporary systems-engineering artefacts.

## 1. Stakeholder need

The aircraft needed a modernised training cockpit while preserving safe, supportable operation of a legacy airframe and its existing systems.

A modern SE representation would capture stakeholder needs such as:

- improved flight/engine information presentation;
- training-role suitability;
- navigation/communication capability;
- maintainability and support;
- acceptable aircraft modification burden;
- verification in the installed aircraft;
- configuration repeatability.

## 2. System boundary

The retrofit boundary is wider than the instrument panel.

A defensible context model would include:

**aircraft sensors / engine / electrical system / legacy avionics ↔ retrofit avionics ↔ pilot & instructor ↔ maintenance/support ↔ OEM engineering**

This is a system-context statement, not a wiring diagram.

## 3. Requirements baseline

The private archive demonstrates requirements and constraints across:

- flight-state data;
- engine/airframe data;
- NAV/COM functions;
- aircraft electrical integration;
- installation;
- warnings/audio;
- cockpit/HMI;
- qualification;
- maintainability;
- reliability/redundancy;
- vendor support;
- verification.

In a current MBSE environment these would be captured as traceable requirements with source, rationale, verification method and configuration applicability.

## 4. Architecture trade study

The programme compared alternative commercial architectures rather than assuming one vendor solution.

A modern decision record would link each candidate to:

- functional coverage;
- interface burden;
- power/installation margin;
- training-role HMI;
- qualification evidence;
- maintainability;
- reliability/redundancy;
- upgradeability;
- cost and schedule.

The important artifact is the **decision trace**, not a decorative vendor diagram.

## 5. Interface control

Direct OEM correspondence shows that interface engineering was a major part of the work: data-bus compatibility, radio integration, database behaviour, electrical effects, sensing and post-installation operation.

A modern digital thread would capture these as interface objects with:

- source and destination;
- physical/logical type;
- data or signal definition;
- assumptions and constraints;
- verification method;
- configuration applicability;
- issue/decision history.

## 6. Parametric analysis

The historical work considered finite aircraft resources such as electrical and installation capacity.

A modern MBSE implementation would maintain parametric budgets for:

- electrical power and margin;
- equipment mass/weight where releasable;
- installation envelope;
- cooling/environmental limits where applicable.

Only releasable values should appear in the public digital twin.

## 7. Prototype configuration control

The archive shows an evolving set of prototypes and candidate configurations. This makes configuration identity critical.

Every test record should answer:

- Which aircraft baseline?
- Which cockpit architecture?
- Which hardware/software/database state?
- Which sensor/interface configuration?
- Which modifications were incorporated since the previous test?

That configuration discipline is also why this repository does not collapse all Garmin records into an invented single sub-variant.

## 8. Verification and feedback

The surviving evidence supports the following lifecycle abstraction:

```mermaid
flowchart LR
    A[Modernisation need] --> B[Requirements & constraints]
    B --> C[Architecture trade study]
    C --> D[Prototype configuration]
    D --> E[Functional / ground checks]
    E --> F[Flight test]
    F --> G[Test observations]
    G --> H[Engineering / OEM resolution]
    H --> I[Configuration update]
    I --> E
```

**This is a retrospective SE lifecycle abstraction—not an original programme artifact and not an aircraft interface diagram.**

## 9. Verification traceability

A modern verification matrix would connect:

**requirement → verification method → test configuration → evidence → result → open issue / closure**

That would make the first-sortie record, repeated evaluation sorties and OEM issue-resolution exchanges part of the same traceable engineering model rather than disconnected documents.

## 10. Recommended MBSE artefact set

For the current digital-twin follow-on, the highest-value artefacts are:

1. requirements hierarchy with source/rationale;
2. SysML-style system context and block-definition model;
3. internal-interface model;
4. interface-control register;
5. configuration-state model;
6. power/weight parametric budgets where releasable;
7. verification cross-reference matrix;
8. issue/decision log linked to evidence;
9. change history across prototype/configuration states.

The governing principle is simple: **traceability before visual complexity**. A sparse model with evidence is more credible than a detailed diagram filled with inferred interfaces.
