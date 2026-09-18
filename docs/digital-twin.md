# Super Mushshak Digital Twin — Follow-on Work

The digital twin is a **new follow-on digital-engineering effort**, not an artefact from the original glass-cockpit programme.

The retrofit archive is valuable because it contains real examples of configuration change, interfaces, observed discrepancies, OEM technical resolution, verification events, customer-evaluation constraints and lifecycle decisions.

![Digital twin roadmap](../assets/digital-twin-roadmap.svg)

## Maturity states

### 1. Historical evidence layer — reconstructed

Available now: configuration-state history, requirements/constraints, functional decomposition, logical interfaces, verification events, discrepancy/issue records, decision records and evidence provenance.

### 2. Digital-thread backbone — first public version implemented

The machine-readable `/model` directory provides stable object IDs and typed links across the evidence chain.

The current backbone is tool-agnostic and can later migrate into SysML/Capella/Cameo, a requirements database or a graph model without changing public object identities.

### 3. Executable twin layer — future / incremental

Potential future models include electrical loading, configuration-dependent failure effects, maintenance/health state, selected avionics or flight-data replay, verification-scenario playback and change-impact analysis.

These are **not claimed as complete**.

## Evidence-to-executable rule

No executable parameter is added merely because it would be useful.

Each value must be tagged as measured, documented, derived, assumed for a declared experiment, or unknown.

For the public historical twin, unknown source data remains unknown.

## Proposed thread

~~~mermaid
flowchart LR
    E[Evidence] --> C[Claims]
    C --> R[Requirements]
    R --> F[Functions]
    F --> I[Logical interfaces]
    I --> B[Configuration baseline]
    B --> V[Verification / issue]
    V --> D[Decision / change]
    D --> B
~~~

The public twin will not publish controlled wiring, pinouts, precise internal locations, private correspondence or proprietary implementation data.

The goal is **configuration-aware engineering continuity**, not a visually complete but unsupported simulation.
