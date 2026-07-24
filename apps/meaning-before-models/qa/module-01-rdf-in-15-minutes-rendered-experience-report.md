# OWOS Rendered Experience Report

## Identity

- Course and module: Meaning Before Models, Module 01
- Structured source version: 1.0.0-structured-candidate
- Compiler version: 1.1.0
- Build checksum: `11eb2966db7cfda9f9055561cc6c1c336e628e874a537734ab416766caa9b72b`
- Reviewer: pending
- Date: 2026-07-24

## Device and behavior evidence

| Review | Status | Evidence path | Finding |
| --- | --- | --- | --- |
| Desktop | automated pass, human review pending | `qa/rendered/module-01/desktop/` | Distributed lesson: zero runtime errors, no overflow, three packaged visual assets loaded, all required activities completed |
| Tablet | automated pass, human review pending | `qa/rendered/module-01/tablet/` | Distributed lesson: zero runtime errors, no overflow, touch-capable context completed all activities |
| Phone | automated pass, human review pending | `qa/rendered/module-01/phone/` | Distributed lesson: zero runtime errors, no overflow, reduced-motion equivalent and touch-capable completion passed |
| Keyboard | automated partial pass, human review pending | `qa/structured-module-browser-validation.cjs` | Escape closes drawers and focus returns to the trigger |
| Touch | automated pass, human review pending | `qa/structured-module-browser-validation.cjs` | Tablet and phone touch-capable browser contexts completed all controls |
| Screen reader | pending human review | | |
| Reduced motion | automated pass, human review pending | `qa/rendered/module-01/phone/` | Maximum computed transition duration was 0.01 milliseconds |
| Read without video | pending novice review | | |

## Component truth review

| Manifest ID | Asset loaded | Legible | Interaction works | Teaching conclusion supported | Status |
| --- | --- | --- | --- | --- | --- |
| `mbm01-utility-scene` | passed | passed automated | not applicable | human review pending | blocked |
| `mbm01-triple-anatomy` | passed | passed automated | not applicable | human review pending | blocked |
| `mbm01-graph-growth` | passed | passed automated | not applicable | human review pending | blocked |
| `mbm01-triple-builder` | not applicable | passed automated | passed | human review pending | blocked |
| `mbm01-path-tracer` | not applicable | passed automated | passed | human review pending | blocked |
| `mbm01-term-cards` | not applicable | passed automated | passed | human review pending | blocked |

## Release decision

- Status: approved for live-review replacement; final credential-bearing release remains blocked
- Required revisions: complete the named rendered and human reviews before final release or credential claims.
