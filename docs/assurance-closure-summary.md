# Assurance and Closure Summary

This page answers a systems-engineering question that a diagram alone cannot answer:

> **What is actually demonstrated, what is only reviewed/derived, and what remains unreconstructed?**

It is a public-safe assurance view of the retrospective model. It does not convert missing evidence into a pass.

| Requirement | Public assurance position | Main evidence / V&V | Residual boundary |
|---|---|---|---|
| **REQ-001 Flight information** | installed operation demonstrated | VER-001, VER-003, VER-004, VER-007 | no claim that every later configuration was identical |
| **REQ-002 Engine/airframe information** | function represented and configuration-specific behaviour observed | VER-006; E-01/E-05/E-06 | full acceptance closure for later observed fluctuation not reconstructed |
| **REQ-003 NAV/COM integration** | integration activity and installed re-test represented | VER-003, VER-004 | pin-level/interface implementation withheld |
| **REQ-004 Electrical integration** | discrepancy observed, action taken, return to flight evidenced | VER-002, VER-003 | detailed root cause and repair implementation not public |
| **REQ-005 Configuration management** | restoration/re-test loop demonstrated | VER-003, VER-004 | exact private software/database versions withheld |
| **REQ-006 Retained-avionics interfaces** | compatibility work represented | VER-004; E-05 | no public exhaustive interface test matrix |
| **REQ-007 Physical integration** | executed scope documented | E-23, E-24 | no separate public verification record for the complete installation/harness baseline |
| **REQ-008 Installed verification** | repeated ground/flight/evaluation loop demonstrated | VER-001 to VER-007 as applicable | some later discrepancy closures remain unreconstructed |
| **REQ-009 Maintainability** | spare/LRU/OEM support concept represented | E-05, E-12; VER-003 | no quantitative fleet availability/AOG dataset published |
| **REQ-010 Qualification / acceptance** | assessment concern represented; customer evaluation documented | VER-007, VER-008 | certification/type-acceptance approval is not claimed |
| **REQ-011 Failure response** | architecture review plus real discrepancy experience represented | VER-002, VER-008 | no public exhaustive failure-injection test set |
| **REQ-012 HMI / training suitability** | flight/evaluation feedback represented | VER-004, VER-007 | no formal human-factors campaign is claimed |
| **REQ-013 Configuration identity** | configuration-specific evidence discipline implemented | model/configurations.csv + traceability | some exact historical software/LRU baselines remain partially reconstructed |
| **REQ-014 Evidence integrity** | repository-level provenance and quality rules implemented | evidence/claims/traceability + CI quality gate | public completeness is constrained by releasability and surviving records |

## Closure logic

The public model uses four practical assurance states:

1. **Demonstrated** — installed-aircraft or direct project evidence supports the requirement/function in an identified configuration.
2. **Reverified** — a change/restoration was followed by an evidenced return to check/flight.
3. **Reviewed / partially reconstructed** — architecture, qualification or supportability evidence exists, but not a complete aircraft-level closure record.
4. **Gap explicit** — the need/scope is evidenced, but a public verification record is not available.

The purpose is not to maximise “passes”. The purpose is to make the **evidence boundary auditable**.

## Strongest closure thread

The most complete surviving engineering thread is the Dynon installed-aircraft loop:

**CFG-D1 early flight → ISS-001 power/display discrepancy → engineering/OEM investigation → CFG-D2 replacement/configuration restoration → VER-003 return to flight → continued integration/evaluation → CFG-D3 performance/customer-evaluation observations**

That is the clearest end-to-end systems-engineering evidence in the archive.

## What remains deliberately open

The public reconstruction does not force closure for:

- the final corrective action for the PTT-associated engine-indication fluctuation;
- the final programme acceptance disposition for the high-rate ADAHRS observation;
- a separate public verification record for the complete physical/harness baseline;
- exact historical software/database/LRU baselines where source evidence is incomplete;
- certification/type-acceptance status beyond what identified sources support.

These are not weaknesses hidden from view; they are controlled gaps in the assurance case.
