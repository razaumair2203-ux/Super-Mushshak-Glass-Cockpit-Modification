# Verification and Flight Test

The surviving project record shows an **iterative installed-aircraft verification loop**, not a one-time installation.

![Evidence-to-verification digital thread](../assets/mbse-verification-thread.svg)

The key systems-engineering rule used in the reconstruction is simple: **a verification observation belongs to the configuration in which it was made**.

## Early Dynon prototype

An original 2010 troubleshooting exchange records that the SkyView-equipped aircraft had flown **two sorties** before a display-related internal-voltage/power failure appeared on a later engine start.

That event generated a real engineering chain:

**symptom → aircraft-power checks → OEM troubleshooting → hardware replacement → settings/database restoration → re-integration → flight**

This is materially stronger evidence than a photograph of a powered-up panel because it shows installed operation, failure, troubleshooting, configuration recovery and re-test.

## Reconfiguration and return to flight

After replacement displays and an ARINC interface unit were received, the team reinstalled the equipment, loaded databases/settings and returned the aircraft to flight. A December 2010 exchange records the first sortie after that reconfiguration and asks the team to continue feeding flight-test results back to the OEM.

![In-flight Dynon PFD](../assets/dynon-pfd-inflight-sanitized.jpg)

*Original in-flight project photograph. No synthetic content.*

## Interface and HMI verification topics

Surviving exchanges show installed-aircraft questions or checks involving:

- ARINC-429 / GNS 430-family integration;
- legacy transponder interface;
- audio-alert output;
- moving-map and synthetic-vision behaviour;
- terrain/database installation;
- configuration transfer after display replacement;
- sensor/engine indication behaviour;
- maintainability and replacement strategy.

Exact wiring, connector and pin data remain private.

## 2012 performance and customer evaluation

Before Qatar deployment, correspondence records the aircraft undergoing performance testing. During the Qatar evaluation period, direct technical exchanges describe repeated daily sorties in hot/humid conditions and troubleshooting of ADAHRS cross-check behaviour during high-rate manoeuvre/spin recovery.

Another issue concerned short-duration engine-indication fluctuations associated with radio PTT operation. The technical importance is the **cross-domain coupling**: a communications action affected an engine-indication path, requiring aircraft-level investigation rather than isolated LRU testing.

By 12 November 2012, surviving status correspondence records **10 evaluation sorties**, including a night-flying mission, with an additional night sortie planned.

![Qatar ground evaluation](../assets/qaef-ground-evaluation-sanitized.jpg)

*Original customer-evaluation-period ground photograph. Used as evaluation context; the technical claim comes from the test record, not from the photograph alone.*

## How the additional flight photographs should be used

The archive also contains cockpit-in-flight, aerial test-flight and a test-engineer selfie. These are valuable, but their evidentiary role must be precise:

| Photograph type | Strong claim it can support | Claim it should not support by itself |
|---|---|---|
| Cockpit in flight with avionics visible | installed configuration / flight operation visible in image | exact test result unless tied to test record |
| Aerial test-flight image | period flight/test operating context | specific avionics configuration |
| Test-engineer in-flight image | participation and flight-test context | sole authorship or technical verification result |
| Customer-evaluation ground image | field/customer context | performance result not visible in image |

For the repository owner's images, release processing is limited to crop/quality correction and **rank-insignia redaction where required**.

## Verification objects in the structured model

The machine-readable [verification register](../model/verification.csv) currently distinguishes:

- early installed-flight operation;
- ground discrepancy after engine start;
- replacement/reconfiguration and return to flight;
- HMI/synthetic-vision behaviour after configuration work;
- ADAHRS/performance-flight observation;
- PTT-related cross-domain engine-indication interference;
- Qatar repeated customer-evaluation sorties;
- Garmin-family architecture/configuration review.

The [traceability file](../model/traceability.csv) connects these verification objects back to requirements, interfaces, configurations and evidence IDs.

## Public-release boundary

Verification depth is demonstrated without publishing:

- exact pins or harness routing;
- controlled acceptance procedures;
- customer-private correspondence;
- precise internal equipment locations;
- proprietary vendor implementation data.

The public objective is to show **how verification was structured and closed**, not to reproduce controlled test documentation.
