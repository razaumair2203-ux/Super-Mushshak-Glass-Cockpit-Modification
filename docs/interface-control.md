# Interface Control

## Purpose

The public interface model demonstrates the **integration problem** without exposing controlled implementation detail.

An interface is published only when it is supported by project evidence, OEM/reference material, or a clearly identified engineering derivation needed to connect evidence-backed functions.

## Interface classes

| Class | Examples represented publicly | Detail intentionally withheld |
|---|---|---|
| Electrical | aircraft power/protection to retrofit avionics | feeder routing, exact breaker/wire data, connector pins |
| Sensor/data | flight-state and engine/airframe measurement paths | exact sensor wiring and installation locations |
| Digital avionics | retained navigation source / avionics interface | pin assignment, detailed bus routing |
| Retained avionics | transponder and other legacy interoperability | converter wiring and proprietary implementation |
| Audio | alerts / communication audio path | exact audio-panel wiring |
| Configuration data | software/settings/terrain/navigation database loading | private media/configuration procedures |
| HMI | pilot/instructor controls, indications and alerts | controlled test procedures |
| Lifecycle/support | LRU replacement, repair, spares, configuration restoration | private OEM correspondence |

Machine-readable source: [model/interfaces.csv](../model/interfaces.csv).

## Configuration applicability

An interface is not assumed to exist in every prototype.

Examples:

- retained-navigation integration evidence is tied to the Dynon configuration in which it was discussed and tested;
- Garmin G900X/G950 digital-network relationships are recorded as **generic OEM reference relationships** unless aircraft-specific evidence exists;
- G3X comparison material does not create an installed interface in any aircraft configuration.

## Interface evidence rule

For each interface the model records stable interface ID, source/target, interface class, configuration scope, public description and evidence IDs.

An interface may be **observed**, **documented**, **engineering-derived** or represented at **public-summary** level. “Typical” or “normal for this aircraft” is not an acceptable source.

## Harness representation

The modification included a complete wiring-harness change associated with the retrofit. The public model represents that as a physical-integration function and constraint, not as a public wiring diagram.

This gives the repository aircraft-level depth without publishing information that should remain controlled.

## Interface verification

Interface verification is linked to an identified configuration and event. If a verification record addresses subsystem behaviour but does not establish every underlying interface, the model does not infer the missing links.

See [Traceability and V&V](traceability-and-vv.md).
