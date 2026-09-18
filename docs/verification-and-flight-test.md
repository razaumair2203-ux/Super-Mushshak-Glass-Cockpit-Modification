# Verification & Flight Test

This page describes the **verification logic** of the modification at a public, non-sensitive level. It does not publish test limits, restricted procedures, customer data, raw flight logs or internal acceptance criteria.

## Verification ladder

### 1. Installation inspection

Typical closure items include:

- equipment installation and mounting;
- wiring continuity and segregation;
- power/ground integrity;
- antenna and sensor installation;
- connector/security checks;
- cockpit-control accessibility;
- configuration identification.

### 2. Power-on / bench-to-aircraft integration

Representative objectives:

- controlled first power-on;
- display and LRU communication;
- sensor validity;
- radio/navigation interface checks;
- annunciation and alert behaviour;
- fault isolation and correction.

### 3. Ground functional test

Representative objectives:

- air-data and attitude/heading reasonableness;
- engine/airframe indication verification;
- navigation/communication functions;
- display-mode and reversion behaviour;
- electrical-load and power-transition checks;
- pilot/instructor ergonomic observations.

### 4. Ground run

Engine-running tests allow validation of aircraft-installed behaviour under vibration, operating electrical loads, live engine sensing and radio/navigation use before flight release.

### 5. Flight test

Flight verification then closes the gap between static integration and operational aircraft behaviour. At portfolio level, relevant engineering themes include:

- cross-check of displayed flight parameters;
- attitude/heading and air-data behaviour in representative manoeuvres;
- navigation and situational-awareness functions;
- engine/airframe indication behaviour;
- HMI workload and training suitability;
- defect recording, troubleshooting and regression testing.

### 6. Customer / overseas evaluation

Overseas trials add a second layer of engineering: demonstrating a stable configuration to a customer, supporting pilot/engineering feedback and separating genuine technical defects from configuration, training or operational-use issues.

## Evidence policy

Photographs can demonstrate participation and the existence of integrated hardware, but they are **not treated as proof of a requirement being met**. Engineering claims in this repository are tied to one of three evidence levels:

- **Publicly documented** — supported by traceable external sources.
- **Personal project record** — supported by personally owned photographs or contemporaneous material.
- **Archive verification pending** — not published as a definitive claim until original records are checked.

See [evidence-matrix.md](evidence-matrix.md).
