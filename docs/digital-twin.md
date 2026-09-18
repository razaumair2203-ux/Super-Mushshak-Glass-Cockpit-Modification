# Super Mushshak Digital Twin — Follow-on Work

The digital twin is a **new follow-on digital-engineering effort**, not an artefact from the original glass-cockpit programme.

The retrofit archive is valuable because it contains real examples of configuration change, interfaces, observed discrepancies, OEM technical resolution, verification events, customer-evaluation constraints, integration risks and lifecycle decisions.

![Digital twin roadmap](../assets/digital-twin-roadmap.svg)

## What exists now

The repository already implements a public-safe **digital-thread backbone**:

- stable IDs for stakeholders, requirements, functions, interfaces and configurations;
- configuration-specific verification and discrepancy records;
- evidence-bounded integration risks;
- recovered decisions and claim provenance;
- typed links between engineering objects;
- an executable quality gate for referential integrity and repository links;
- a graph-ready JSON exporter: [tools/export_digital_thread.py](../tools/export_digital_thread.py).

The exporter does not infer new aircraft detail. It serializes the controlled CSV model into nodes and typed edges that can be loaded into a graph database, MBSE adapter or later twin service.

Example:

~~~bash
python tools/validate_model.py
python tools/export_digital_thread.py --output generated/digital-thread.json
~~~

## Maturity states

### 1. Historical evidence layer — reconstructed

Available now: configuration-state history, requirements/constraints, functional decomposition, logical interfaces, verification events, discrepancy/issue records, risk records, decision records and evidence provenance.

### 2. Digital-thread backbone — implemented

The machine-readable /model directory provides stable object IDs and typed links across the evidence chain.

The current backbone is tool-agnostic and can later migrate into SysML/Capella/Cameo, a requirements database or a graph model without changing public object identities.

### 3. Behavioural / executable models — future and evidence-dependent

Potential public-safe models include:

- electrical load/state analysis where releasable source values exist;
- configuration-dependent failure/availability logic;
- maintenance and health-state representation;
- selected avionics or flight-data replay where releasable data exists;
- verification-scenario playback;
- requirements/configuration change-impact analysis.

These are **not claimed as complete**.

### 4. Operational digital twin — future

A true operational twin would require authoritative, configuration-controlled data feeds and validated behavioural models tied to a specific aircraft state.

That maturity is intentionally **not claimed** by this repository.

## Evidence-to-executable rule

No executable parameter is added merely because it would be useful.

Each value must be tagged as:

- **measured**;
- **documented**;
- **derived**;
- **assumed for a declared experiment**; or
- **unknown**.

For the public historical twin, unknown source data remains unknown.

## Proposed digital thread

~~~mermaid
flowchart LR
    E[Evidence] --> C[Claims]
    C --> R[Requirements]
    R --> F[Functions]
    F --> I[Logical interfaces]
    I --> B[Configuration baseline]
    B --> V[Verification / issue]
    V --> K[Risk]
    K --> D[Decision / change]
    D --> B
~~~

The public twin will not publish controlled wiring, pinouts, precise internal locations, private correspondence or proprietary implementation data.

## Immediate next engineering increments

The next defensible increments are:

1. generate the graph-ready JSON in CI and inspect orphan/weakly connected objects;
2. add change-impact queries such as **configuration → interfaces → requirements → V&V → risks**;
3. add public-safe configuration comparison views for Dynon versus Garmin paths without collapsing their identities;
4. introduce executable models only where a releasable parameter set exists;
5. preserve the same evidence-state tags when moving into SysML/Capella/Cameo or a graph database.

The goal is **configuration-aware engineering continuity**, not a visually complete but unsupported simulation.
