# Traceability and V&V

## Purpose

The digital-thread model is useful only if engineering objects have stable identities and explicit relationships.

The public digital thread uses these namespaces:

- **STK-###** — stakeholders;
- **FUN-###** — functions;
- **REQ-###** — requirements / constraints;
- **IF-###** — logical interfaces;
- **CFG-### / CMP-###** — configurations / comparison-only artefacts;
- **VER-###** — verification or review events;
- **ISS-###** — discrepancies / issues;
- **RSK-###** — integration risks;
- **DEC-###** — decisions;
- **E-##** — evidence items;
- **CLM-###** — public technical / programme claims.

## Traceability chain

**evidence → claim → requirement → function → interface → configuration → verification / issue / risk → decision**

![Requirements × verification cross-reference](../assets/traceability-matrix.svg)

The matrix is intentionally sparse. A blank cell means the public model does not assert a direct verification link.

The machine-readable [traceability table](../model/traceability.csv) now carries risk IDs alongside verification, issue and decision links so that an integration concern can be traced back to the requirement/interface it threatens and the evidence that exposed it.

## Verification semantics

Verification records distinguish:

- **Observed** — event or behaviour directly recorded;
- **Reverified** — subsequent installed check or flight recorded after change/restoration;
- **Reviewed** — architecture/configuration documentation reviewed; not equivalent to aircraft test;
- **Detailed closure record not published** — the issue and analysis path are represented, while detailed programme closure material remains outside the public repository.

This prevents “issue discussed with OEM” from being rewritten as “issue solved”.

## Risk semantics

The risk register is evidence-bounded. It captures integration risks documented in project records, including power/transient behaviour, configuration restoration, cross-domain interaction, high-dynamic attitude-reference behaviour, retained-avionics interoperability and supportability/AOG exposure.

No probability, severity or formal hazard classification is invented.

See [Integration risk register](integration-risk-register.md).

## Configuration-specific evidence

A verification record carries one configuration ID. If a later configuration differs in hardware, software, settings or databases, prior evidence is not automatically inherited.

## Claim control

The public [claim register](../model/claims.csv) records statement, evidence state, configuration scope, evidence IDs and boundary/limitation.

Technical claims, role claims and commercial/programme claims are controlled separately so that an individual role statement cannot silently become a causation claim for later sales.

## Typed links

[model/links.csv](../model/links.csv) provides a tool-agnostic edge list suitable for migration to a graph database, requirements tool or MBSE environment.

Relationship types now include drives, allocated_to, interfaces_via, verified_by, raises_issue, followed_by, validated_by, reviewed_by, has_risk, observed_in, controlled_by, supported_by and controls.

## Quality rule

No relation exists solely because it would be normal practice on an aircraft programme. A missing relation remains missing until evidence or a justified engineering derivation supports it.
