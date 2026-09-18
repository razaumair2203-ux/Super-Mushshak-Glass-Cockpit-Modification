# Configuration Management

## Why configuration is part of the engineering evidence

The project archive contains multiple prototype branches and multiple hardware/software/data states. Treating them as one timeless “glass cockpit” would corrupt the technical record.

The public configuration model therefore separates **branch identity**, **hardware change**, **software/settings/database state** and **as-tested evidence**.

![Configuration evolution](../assets/configuration-evolution.svg)

## Controlled configuration states

| ID | State | Evidence boundary |
|---|---|---|
| CFG-000 | legacy aircraft baseline | detailed baseline withheld; public functions only |
| CFG-D1 | initial installed Dynon SkyView prototype | early installed-aircraft / flight evidence |
| CFG-D2 | Dynon after display replacement and configuration restoration | replacement hardware + databases/settings + return to flight |
| CFG-D3 | Dynon performance/customer-evaluation state | later performance and customer-evaluation evidence |
| CFG-G1 | Garmin G900X/G950-family prototype/evaluation path | public-summary baseline; detailed configuration not published |
| CMP-G3X | G3X comparison artefact | trade-study only; never an installed-aircraft state |

Source: [model/configurations.csv](../model/configurations.csv).

## Configuration item types

The public model treats the following as configuration-bearing items where evidence exists:

- display/LRU identity;
- avionics interface equipment;
- software state;
- settings/configuration files;
- terrain/navigation databases;
- sensor / monitoring configuration;
- physical installation and modification harness;
- evidence tied to the tested state.

Exact part numbers, serial numbers, wiring revisions and private configuration files are outside the public repository unless specifically released.

## Replacement / restoration example

After replacement displays were received on the Dynon track, project records document reinstallation, database loading, settings restoration and a subsequent flight.

That sequence demonstrates why **configuration restoration is part of verification**. Replacing an LRU without restoring its required settings/data is not the same as restoring the aircraft to a known operational baseline.

## Branch discipline

The following merges are prohibited in the systems model:

- G3X trade-study evidence → G900X/G950 installed-aircraft evidence;
- generic Garmin OEM interconnect → exact Super Mushshak wiring;
- test result from CFG-D1 → automatic proof for CFG-D2 or CFG-D3;
- later field observation → assumption that the same condition existed in earlier software/data state.

## Unknowns

The model uses “public-summary” or “not published” when exact historical configuration detail is outside the public-release boundary.

That is a configuration-control feature, not a documentation defect.
