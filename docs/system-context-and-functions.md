# System Context and Functional Decomposition

## System of interest

The system of interest is the **aircraft glass-cockpit retrofit**. Treating the display suite alone as the system boundary would omit the integration work that made the modification an aircraft programme.

![System context](../assets/system-context.svg)

The public context contains the actors and systems that materially affect the retrofit:

- pilot / instructor;
- legacy aircraft baseline;
- maintenance / fleet support;
- avionics OEM / technical support;
- flight-test and evaluation activity;
- customer / acceptance authority.

The model intentionally does not expose internal organisational structures or controlled aircraft details.

## Stakeholder needs

| Stakeholder | Public need represented |
|---|---|
| Pilot / instructor | usable flight/engine information, controls, alerts and training suitability |
| Integration engineering | controlled interfaces, configuration identity, discrepancy closure and evidence |
| Maintenance / fleet support | replaceability, configuration restoration, spares and supportability |
| OEM technical support | enough configuration and symptom information to resolve vendor-system issues |
| Flight test / evaluation | known as-tested configuration and traceable observations |
| Customer / acceptance authority | operational suitability and an evidence basis appropriate to the intended acceptance route |

Machine-readable source: [model/stakeholders.csv](../model/stakeholders.csv).

## Functional decomposition

![Functional decomposition](../assets/functional-decomposition.svg)

The functions are equipment-independent so that Dynon and Garmin alternatives can be compared without merging their implementation details.

| Function ID | Function | Configuration use |
|---|---|---|
| FUN-001 | acquire flight-state information | common need; implementation is configuration-specific |
| FUN-002 | acquire engine/airframe information | common need; sensor/monitoring path varies |
| FUN-003 | present primary flight information | common |
| FUN-004 | present engine/airframe information | common where configured |
| FUN-005 | integrate NAV/COM and retained avionics | configuration-specific |
| FUN-006 | provide audio / alerting integration | configuration-specific |
| FUN-007 | manage software, settings and databases | configuration-specific |
| FUN-008 | integrate aircraft electrical power/protection | aircraft-level |
| FUN-009 | integrate physical installation / modification harness | aircraft-level |
| FUN-010 | provide pilot/instructor HMI | common need |
| FUN-011 | verify installed aircraft and close discrepancies | aircraft-level |
| FUN-012 | support maintenance / LRU replacement / OEM loop | lifecycle |

Machine-readable source: [model/functions.csv](../model/functions.csv).

## Functional boundary versus physical architecture

A function does not prove a particular LRU was installed. For example, “acquire air data” is a valid aircraft-level function across candidate architectures; the public model identifies a particular vendor LRU only when the evidence supports that configuration.

That distinction protects the model from a common retrospective error: turning a generic OEM architecture into an aircraft-specific physical baseline.

## Harness and physical integration

The modification included a complete aircraft wiring-harness change associated with the retrofit. The public model captures **the existence and engineering purpose of that physical-integration work**, while deliberately withholding routes, connector details, pin assignments and controlled installation drawings.

## Traceability

Requirements map to functions, functions map to logical interfaces, verification events map to an as-tested configuration, and all derived objects map back to evidence.

See [Traceability and V&V](traceability-and-vv.md).
