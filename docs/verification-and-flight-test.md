# Verification and Flight Test

Project records document an **iterative installed-aircraft verification loop** rather than a one-time installation demonstration.

![Evidence-to-verification digital thread](../assets/mbse-verification-thread.svg)

The principal rule is:

> **A verification observation belongs to the configuration in which it was made.**

## Verification-event register

| Verification ID | Configuration | Event / observation | Public status |
|---|---|---|---|
| VER-001 | CFG-D1 | early installed-aircraft SkyView operation; two sorties recorded before a later discrepancy | **Observed** |
| VER-002 | CFG-D1 | display internal-voltage/power-related indication on a later engine start | **Observed; investigation initiated** |
| VER-003 | CFG-D2 | replacement displays plus settings/databases restored; aircraft returned to flight | **Reverified by return to flight** |
| VER-004 | CFG-D2 | synthetic-vision / terrain / configuration behaviour assessed during continuing integration | **Observed / supported; exact acceptance record not published** |
| VER-005 | CFG-D3 | ADAHRS compare / attitude-recovery behaviour during high-rate manoeuvre or spin recovery | **Observed; OEM behaviour explanation recorded; detailed programme closure record not published** |
| VER-006 | CFG-D3 | short-duration CHT/EGT indication fluctuation associated with radio PTT operation | **Observed; OEM engaged; detailed closure record not published** |
| VER-007 | CFG-D3 | repeated customer-evaluation sorties, including night operation | **Observed validation context** |
| VER-008 | CFG-G1 | G900X/G950 architecture/configuration review | **Documented architecture/configuration evidence; not flight verification** |

Source: [model/verification.csv](../model/verification.csv).

## Early Dynon prototype

A 2010 troubleshooting exchange records that the SkyView-equipped aircraft flew **two sorties** before a display-related internal-voltage/power indication appeared on a later engine start.

The public record preserves the engineering chain without exposing connector-level troubleshooting detail:

**symptom → aircraft-power checks → OEM troubleshooting → replacement hardware → configuration/data restoration → re-flight**

## Reconfiguration and return to flight

After replacement displays and interface equipment were received, the team reinstalled the equipment, loaded required databases/settings and returned the aircraft to flight. Project correspondence records continuing flight-test feedback to the OEM.

![In-flight Dynon PFD](../assets/dynon-pfd-inflight-sanitized.jpg)

*Authentic in-flight project photograph. It supports visible installed operation; the technical event claims come from the project record.*

## Interface and HMI verification topics

Project exchanges include installed-aircraft work involving navigation-data / avionics-interface integration, retained transponder interoperability, audio-alert path, moving-map/synthetic-vision behaviour, terrain/database loading, configuration transfer, sensor/engine-indication behaviour and maintainability/replacement strategy.

Exact pins, connector data and harness routes are deliberately omitted.

## Performance testing and ADAHRS behaviour

Ahead of customer deployment, the aircraft was undergoing performance testing. During later evaluation, a high-rate-manoeuvre/spin-related attitude-recovery / compare behaviour was raised with the OEM.

The OEM provided an explanation of vendor-system behaviour under high rotational rate. That supports **characterisation of the observation**. It does not by itself establish final programme acceptance or closure, so the public issue is marked “detailed closure record not published”.

## PTT-associated engine-indication interference

The record also documents short-duration CHT/EGT indication fluctuations associated with radio PTT operation.

This is an aircraft-level verification example because it crosses subsystem boundaries: a communications action coincided with an engine-indication disturbance. The issue was raised with the OEM.

The public release does **not** include detailed final corrective-action closure material, so the repository does not speculate beyond the published evidence.

## Customer evaluation

By 12 November 2012, status correspondence records **10 evaluation sorties**, including a night-flying mission. Separate correspondence during the evaluation describes repeated daily flying.

![Customer-evaluation ground photograph](../assets/qaef-ground-evaluation-sanitized.jpg)

*Authentic project photograph used as evaluation context. It does not prove a performance result by itself.*

Customer evaluation is modelled as validation context. It does not prove certification or qualification status.

## Photograph-evidence rule

| Photograph type | Strong claim it can support | Claim it should not support by itself |
|---|---|---|
| cockpit in flight with avionics visible | visible installed configuration / flight operation | exact test result without linked record |
| display close-up in flight | visible display mode / installed operation | full system acceptance |
| aerial test-flight image | period flight/test context | specific avionics configuration |
| test-engineer image | participation / test context | sole authorship or verification result |
| customer-evaluation ground image | field/customer context | a performance result not visible in the image |

## Traceability

The [traceability file](../model/traceability.csv) connects verification objects to requirements, functions, interfaces, configurations, issues, decisions and evidence.

The [issues register](../model/issues.csv) separately records discrepancy status so an observation cannot silently become a “closed” result.

## Public-release boundary

The verification record demonstrates method and technical depth without publishing controlled acceptance procedures, exact wiring/pin data, private customer correspondence, precise internal equipment locations or proprietary vendor implementation data.
