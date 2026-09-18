# Traceability and V&V

## Purpose

The retrospective model is useful only if engineering objects have stable identities and explicit relationships.

The public digital thread uses these namespaces:

- **STK-###** — stakeholders;
- **FUN-###** — functions;
- **REQ-###** — requirements / constraints;
- **IF-###** — logical interfaces;
- **CFG-### / CMP-###** — configurations / comparison-only artefacts;
- **VER-###** — verification or review events;
- **ISS-###** — discrepancies / issues;
- **DEC-###** — decisions;
- **E-##** — evidence items;
- **CLM-###** — public technical claims.

## Traceability chain

**evidence → claim → requirement → function → interface → configuration → verification / issue → decision**

![Requirements × verification cross-reference](../assets/traceability-matrix.svg)

The matrix is intentionally sparse. A blank cell means the public model does not assert a direct verification link.

## Verification semantics

Verification records distinguish:

- **Observed** — event or behaviour directly recorded;
- **Reverified** — subsequent installed check or flight recorded after change/restoration;
- **Reviewed** — architecture/configuration documentation reviewed; not equivalent to aircraft test;
- **Final closure not reconstructed** — an issue was observed and may have received analysis, but the surviving public-safe record does not prove closure.

This prevents “issue discussed with OEM” from being rewritten as “issue solved”.

## Configuration-specific evidence

A verification record carries one configuration ID. If a later configuration differs in hardware, software, settings or databases, prior evidence is not automatically inherited.

## Claim control

The public [claim register](../model/claims.csv) records statement, evidence state, configuration scope, evidence IDs and boundary/limitation.

## Typed links

[model/links.csv](../model/links.csv) provides a tool-agnostic edge list suitable for migration to a graph database, requirements tool or MBSE environment.

Relationship types include drives, allocated_to, interfaces_via, verified_by, raises_issue, followed_by, validated_by, reviewed_by, supported_by and controls.

## Quality rule

No relation exists solely because it would be normal practice on an aircraft programme. A missing relation remains missing until evidence or a justified retrospective derivation supports it.
