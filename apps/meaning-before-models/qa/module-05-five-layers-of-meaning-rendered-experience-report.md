# Module 05 Rendered Experience Report

Date: 2026-07-24
Candidate: Five Layers of Meaning
Compiler: `owos-course-compiler/1`, implementation version 1.1.0
Release state: working golden candidate, not released

## Result

Automated rendered experience: passed
Human owner review: pending
Independent accessibility review: pending
Practitioner and novice review: pending

## Evidence

| View or behavior | Result | Evidence |
| --- | --- | --- |
| Desktop, 1440 by 1000 | passed | `qa/rendered/module-05/desktop/full-page.png` |
| Tablet, 820 by 1080, touch | passed | `qa/rendered/module-05/tablet/full-page.png` |
| Phone, 390 by 844, touch and reduced motion | passed | `qa/rendered/module-05/phone/full-page.png` |
| Five explanatory visuals | passed | Five loaded assets with five distinct visual classes |
| Meaning Triage Desk | passed | All twelve artifacts classified with explanatory feedback and retry |
| Failure laboratory | passed | All five failure paths selectable and completion recorded |
| Matching and context selection | passed | Correct completion behavior and explanatory feedback |
| Five-Layer Meaning Map | passed | All required fields save locally and produce a reviewable preview |
| Graph and Glossary drawers | passed | Open, close, Escape, and focus return work in all three runs |
| Completion | passed | All nine required evidence identifiers complete and final control enables |
| Runtime errors | passed | Zero console or page errors |
| Responsive width | passed | No horizontal overflow at desktop, tablet, or phone |
| Empty controls | passed | Zero empty unlabeled buttons |
| Dark-surface text | passed | Zero automated dark-text failures |
| Reduced motion | passed | Maximum computed phone transition duration is 0.01 milliseconds |

## Visual inspection

The pressure decision room has a clear reading order from event to evidence, disputed meaning, and
governed decision. The Meaning Triage Desk uses a reviewable two-column evidence layout on desktop
and a single-column transformation on phone. The failure laboratory visibly separates the first
broken responsibility from the downstream answer symptom.

The visual language is specific to the lesson. It does not use a generic node cloud, decorative
stock art, black blobs, a repeated flip-card wall, or Module 01's triple-construction grammar.

## Remaining human gates

- Hardeep Anand rendered golden-candidate review
- Independent semantic-architecture and source review
- Water, wastewater, stormwater, governance, and operations practitioner review
- Novice comprehension pilot
- Keyboard-only and screen-reader review by a human reviewer
- Zoom, contrast, and touch inspection on representative physical devices

Automated passing evidence does not convert these human gates into approvals.
