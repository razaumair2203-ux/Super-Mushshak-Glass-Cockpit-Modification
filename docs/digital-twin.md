# Super Mushshak Digital Twin — Follow-on Work

The digital twin is a **new follow-on effort**, not an artefact from the original glass-cockpit programme.

The retrofit archive is valuable because it contains real examples of:

- configuration change;
- interface definition and integration;
- observed discrepancies;
- OEM technical resolution;
- verification events;
- customer-evaluation constraints;
- lifecycle/supportability decisions.

These are the inputs needed for a credible digital thread.

## Proposed digital-thread backbone

~~~mermaid
flowchart LR
    B[Aircraft configuration baseline] --> R[Requirements]
    R --> LA[Logical architecture]
    LA --> PA[Physical configuration]
    PA --> IF[Interfaces / ICD]
    IF --> V[Verification cross-reference]
    V --> TE[Test evidence]
    TE --> CS[As-tested configuration state]
    CS --> CH[Change / decision history]
    CH --> R
~~~

## Near-term model content

1. system boundary and functional decomposition;
2. public-safe requirements hierarchy;
3. logical interface model;
4. configuration-state history;
5. verification cross-reference matrix;
6. issue/decision history;
7. power/weight/environmental parameters only where releasable source data exists;
8. explicit distinction between measured, documented, derived and unknown information.

The first version of that backbone already exists in this repository under [model](../model/README.md).

## What the twin will not do

The public model will not fabricate missing aircraft data simply to look complete. It will not publish controlled wiring, pinouts, internal locations, proprietary installation detail or sensitive aircraft data.

Where exact historical data is unavailable, the model records an **unknown / not publicly reconstructed** state rather than filling the gap with inference.

## Longer-term direction

If sufficient releasable data becomes available, the next layer can add executable/parametric behaviour such as electrical loading, configuration-dependent failure effects, maintenance state and selected flight/avionics data replay. Those capabilities are future work; they are not claimed as complete today.
