# Systems Engineering Case Study

## Engineering problem

The Super Mushshak glass-cockpit modification required integration of a modern digital flight deck into an existing basic-training aircraft.

The work extended beyond the instrument panel. Changing the cockpit architecture affected sensing, electrical interfaces, wiring, equipment installation, navigation/communication functions, engine/airframe indications, cockpit ergonomics, maintenance and verification.

## My role

I worked as **Systems Engineering Lead** for the early modification programme and also supported the programme as a test engineer.

My work covered:

- system-level requirements and architecture trade studies;
- avionics and sensor-suite selection/integration;
- definition and coordination of interfaces between new equipment and the aircraft;
- complete wiring-harness changes associated with the modification;
- prototype integration and troubleshooting;
- ground-run and flight-test support;
- configuration refinement following test observations;
- overseas evaluation and demonstration support.

## Functional decomposition

The retrofit can be viewed as a set of interacting aircraft functions.

### Flight-state sensing
Air-data and attitude/heading information had to be made available to the digital flight-deck architecture.

### Engine and airframe sensing
Existing aircraft and engine parameters had to be sensed, conditioned and presented in a form compatible with the new cockpit.

### Navigation and communication
Navigation/communication functions had to be integrated into the revised cockpit without losing the training-aircraft role of the platform.

### Pilot and instructor interface
The cockpit had to remain usable as an ab-initio training environment. Display layout, control access, readability and information loading therefore formed part of the engineering problem.

### Electrical and physical integration
Equipment installation, aircraft power, circuit protection, connectors and the aircraft wiring harness formed the physical integration layer between the new avionics and the existing platform.

### Verification
Prototype integration required an incremental verification sequence: installation and functional checks, ground operation, flight test, observation capture, configuration refinement and re-test.

## Interface management

A simplified functional view is shown below.

![System architecture](../assets/system-architecture.svg)

This diagram is intentionally at system level. It represents the engineering boundaries of the retrofit rather than aircraft wiring or pin-level implementation.

## Configuration evolution

The programme evaluated more than one cockpit architecture. The original comparison material records a Dynon SkyView candidate and a Garmin-family alternative and evaluates them across capability, cockpit layout, ergonomics, integration flexibility, reliability, support and cost.

The engineering significance is the decision process: the cockpit was treated as an aircraft-system architecture problem, not as a purchase of standalone displays.

See [Architecture Trade Study](architecture-trade-study.md).
