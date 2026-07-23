# Standardization Failure Audit

## Decision

The current Module 01 and Module 05 lesson candidates do not demonstrate conformance with the
binding OWOS Course Production Contract. Prior automated-pass language is withdrawn.

## Why the pass was invalid

The checks that passed were a minimum technical floor and a custom browser path. They proved that
controls worked, completion was deterministic, mobile width did not overflow, reduced-motion rules
existed, and no browser error occurred. They did not prove full production-contract compliance.

The repository-wide contract tests verify that standards, templates, and skill instructions contain
required phrases. The AI Agents master-class tests inspect `apps/what-is-an-ai-agent`. They do not
inspect `apps/meaning-before-models`.

`tools/course_quality.py` accepts the course setting
`minimum_purposeful_interactions: 2`. It checks for interaction markers, a viewport, responsive
rules, reduced motion, live feedback, keyboard controls, and invalid sentinels. It does not enforce
the full module contract.

## Confirmed gaps in Module 05

| Contract requirement | What the brief promised | What the lesson currently provides | Result |
| --- | --- | --- | --- |
| Governed components | Gallery-selected comparison, flow, cause map, packet anatomy, RACI, and method | Custom local cards, tables, and controls | failed |
| Original editorial illustration | Pressure-event evidence desk | No editorial illustration or SVG scene | failed |
| Visual types | Seven planned visual shapes | Several planned shapes are represented as simplified cards or static tables | not demonstrated |
| Artifact classification | Sort 15 to 25 artifacts | Sorts 8 artifacts | underbuilt |
| Quiz sequence | Matching, classify, ordering, multiple choice, multi-select, reflection, applied check | Matching, select-based classification, multiple choice, and multi-select | incomplete |
| Final applied assessment | Deterministic check tied to the Five-Layer Meaning Map | Saving nonempty fields satisfies the work-product requirement | failed |
| Knowledge Graph | Drawer follows concepts, sources, mappings, evidence, controls, and competency | Static list of seven text items | underbuilt |
| Community | Search, filters, bookmarks, threaded replies, presence, and instructor treatment | Search field plus two static text blocks | failed |
| Tooltip coverage | Every new term and acronym | One learner-facing term wrapper in Module 05 | failed |
| QA report | Template score out of 100 plus five hard gates | Custom unscored report without the required template structure | failed |
| Course-specific enforcement | Module test comparable to AI Agents tests | No Meaning Before Models production-contract test | failed |

## Process failure

1. The module design brief was treated as planning evidence instead of a build checklist.
2. A new course-local component runtime was hand-built instead of reusing the governed galleries or
   first adding missing components to the shared library.
3. The minimum release-floor checker was treated as if it were the full Course Production Contract.
4. Passing tests for the standards and the AI Agents course were presented as proof that the new
   course passed.
5. The QA report was written outside the required template, so the missing score and five hard gates
   were not mechanically exposed.
6. Visual inspection focused on polish and responsiveness instead of comparing the implementation
   line by line with the approved design brief and golden capability benchmark.

## Control required before rebuilding

Create a course-specific conformance test before revising the lesson. It must fail the current
candidate for gallery provenance, visual inventory, quiz variety and order, final applied assessment,
tooltip coverage, Graph and Community capability, template-based QA, and design-brief-to-HTML
traceability. Rebuild only after that failing test exists, then require it to pass.
