# Public Release Register

Every candidate artifact is assessed on two axes:

- **Recruiter value:** does it demonstrate engineering depth, responsibility, verification evidence or product impact?
- **Disclosure risk:** does it reveal proprietary, controlled, personally sensitive or operationally unnecessary detail?

## Current artifacts

| Artifact | Recruiter value | Disclosure risk | Decision | Reason |
|---|---:|---:|---|---|
| Ground-run aircraft photograph | High | Low–Medium | **Candidate for release after caption/date check** | Strong evidence of aircraft-level test activity; avoid unsupported customer/date claims |
| Dubai Airshow personnel/aircraft photograph | High | Medium | **Candidate for release after event/date and third-party privacy review** | Strong programme-demonstration evidence; do not identify the other person without a public source/permission |
| Test-flight cockpit photograph showing integrated Dynon displays | Very High | Medium | **Release only as a carefully selected/cropped image** | Best visual evidence of real avionics integration; crop unnecessary route/location/operational data |
| Close-up navigation-map / live flight displays | Medium | Medium–High | **Do not release by default** | Adds little recruiter value relative to operational/location information visible on screen |
| Aerial photography from test flights | Low | Medium | **Do not release** | Weak systems-engineering signal and can expose unnecessary location/route context |
| Personal cockpit selfie | Medium | Medium | **Optional; generally omit** | Human proof but less technical value than hardware/test imagery |
| Internal “Glass Cockpit Comparison” PowerPoint | Very High as source evidence | High | **Do not publish raw** | Contains internal trade-study language, architecture graphics and vendor assessments; derive a sanitized public summary instead |
| Garmin G900X/G950 manual excerpt | Medium | Low disclosure / High copyright-reuse concern | **Do not republish** | Use only as a reference; link to legitimate public manufacturer documentation where possible |
| Internal drawings / wiring diagrams / pinouts | High | Very High | **Never publish without explicit release authority** | Excess detail is unnecessary for recruiter proof and may be controlled/proprietary |
| Sanitized system-level architecture diagram | Very High | Low | **Publish** | Demonstrates systems thinking without exposing implementation-level data |
| Requirements-to-verification matrix using generic requirement IDs | Very High | Low | **Publish** | Shows engineering discipline without revealing restricted requirements |
| Public-source programme timeline | High | Low | **Publish** | Strong context and externally verifiable impact |

## Redaction is not enough

Removing logos, headers and footers does **not** automatically make an internal document safe to publish. Before release, the document must also be checked for:

- proprietary architecture;
- internal vendor assessments;
- part numbers that reveal a non-public configuration;
- wiring/pin-level detail;
- test limits and acceptance criteria;
- names, signatures, phone numbers and email addresses;
- customer information;
- classification/security markings;
- embedded metadata and revision history.

When a source document is valuable but risky, this repository will publish a **new sanitized derivative** rather than a superficially redacted original.
