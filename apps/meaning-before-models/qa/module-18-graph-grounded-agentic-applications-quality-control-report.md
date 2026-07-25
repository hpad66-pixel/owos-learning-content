---
module_id: mbm001:18
course_id: owos-course-semantic-data-ai-001
version: 0.1.0-structured-candidate
review_date: 2026-07-25
reviewer: Codex repository and rendered review
score: 96
score_out_of: 100
working_status: automated_gates_passed_human_review_pending
release_status: blocked
package_checksum: 34f8325bd83447a1bb549da13a02b79c44b5d3e7c99b83e0b6aeaa9b8d8cf4ca
compiler_version: 1.1.0
---

# Module Quality-Control Report: Graph-Grounded Agentic Applications

## Decision

- Working-review result: Passed structured validation, deterministic compilation, rendered browser
  testing, visual containment, and course distinctiveness.
- Release result: Blocked pending the normal human and course-assembly gates.
- Evidence-backed score: 96 out of 100.
- One-sentence reason: The agent authorization control room teaches that grounding supports a
  proposal while policy and authority govern action, then makes stop, approval, retry,
  reconciliation, verification, and audit behavior executable.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 14 | 14 | Seven conversational beats and wastewater case | Novice observation |
| Learning design and sequence | 12 | 12 | Two-key distinction through contract defense | Human learning review |
| Course distinctiveness and lesson identity | 10 | 10 | Authorization console differs from Modules 17 and 19 | Sequence review |
| Explanatory graphics and visual reasoning | 10 | 10 | Five original visual classes and 76-file containment pass | Human visual inspection |
| Interactions and simulations | 10 | 10 | Five action cases and five retry cases | Practitioner stress test |
| Utility relevance and practitioner credibility | 10 | 9 | LS-7 work-order scenario and limited authority | Operations and cybersecurity review |
| Assessments and feedback | 10 | 10 | Multiple choice, matching, multi-select, flip cards, applied artifact | Learner observation |
| Professional work product | 5 | 5 | Fourteen-field Agent Action Contract | Field-use review |
| Accuracy, evidence, and citations | 8 | 7 | W3C RDF, SHACL, PROV-O, and OWASP boundaries | Independent source review |
| Accessibility, responsive behavior, and reduced motion | 6 | 5 | Desktop, tablet, phone, touch, drawers, focus, zero overflow | Screen-reader and physical-device review |
| Platform integration and release controls | 5 | 4 | Permanent Author Studio review candidate; final release intentionally blocked | Module 19 and course assembly |
| **Total** | **100** | **96** | Exact evidence below | Human gates remain |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | Primary sources and explicit evidence boundary | Independent semantic, agent-security, and utility review |
| Learning design | passed | Contract, brief, storyboard, compiled lesson, and browser completion | Hardeep working review |
| Course distinctiveness | passed | 18 lessons and 18 archetypes; adjacent-module comparison | Complete Module 19 sequence review |
| Utility-practitioner review | blocked | Not yet performed | Wastewater operations, maintenance, cybersecurity, and governance review |
| Technical and accessibility review | conditional | Automated desktop, tablet, phone, keyboard, focus, 200%/400% reflow, overflow, and motion pass | Screen-reader and physical-device review |
| Release control | blocked | Module candidate only | Course assembly and explicit release workflow |

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Lesson-contract gate | passed | 19 contracts validated |
| Structured package validation | passed | revised checksum `34f8325bd83447a1bb549da13a02b79c44b5d3e7c99b83e0b6aeaa9b8d8cf4ca`; requested baseline `466bd24a0d94b09360dd7ccaa55425d78fbfde7dc288a4afa2195432dc3741e4` retained in Phase 13 chain of custody |
| Deterministic compilation | passed | `modules/module-18-graph-grounded-agentic-applications/build/index.html` |
| Visual truth | passed automated | Five real SVG assets resolve through the visual manifest |
| SVG containment | passed | 76 files, 1,244 text elements, zero violations |
| Browser behavior | passed | Desktop, tablet, phone, 200% reflow, and 400% reflow; zero runtime errors |
| Responsive layout | passed | 1440, 820, 390, 720, and 360 CSS-pixel widths; zero horizontal overflow |
| Reduced motion | passed | Phone maximum transition duration 0.01 milliseconds |
| Drawers and focus | passed | Graph, Glossary, and Community open; Escape closes; keyboard focus returns |
| Completion contract | passed | Seven required IDs complete and completion control enables |
| Assessment variety | passed | Four conventional types plus two executable simulations, scored contract defense, and exported JSON artifact |
| FAQ | passed | Eight module-specific questions |
| Course distinctiveness | passed | 18 lessons, 18 archetypes |
| Portfolio structured-authoring audit | passed after rebuild | Shared runtime checksums synchronized for Modules 01 through 17 |

## Rendered evidence

- Desktop full-page capture:
  `qa/rendered/module-18/desktop/full-page.png`
- Tablet full-page capture:
  `qa/rendered/module-18/tablet/full-page.png`
- Phone full-page capture:
  `qa/rendered/module-18/phone/full-page.png`
- 200 percent reflow capture:
  `qa/rendered/module-18/zoom200/full-page.png`
- 400 percent reflow capture:
  `qa/rendered/module-18/zoom400/full-page.png`
- Executable QA:
  `qa/module-18-structured-browser-validation.cjs`
- Visual containment audit:
  `qa/svg-text-containment-audit.cjs`

## Exact commands and results

```text
python3 tools/validate-lesson-contracts.py --course meaning-before-models
Result: passed, 19 contracts

python3 tools/course_compiler.py validate apps/meaning-before-models/modules/module-18-graph-grounded-agentic-applications
Result: valid

python3 tools/course_compiler.py build apps/meaning-before-models/modules/module-18-graph-grounded-agentic-applications
Result: built

NODE_PATH=/private/tmp/owos-module18-qa/node_modules node apps/meaning-before-models/qa/svg-text-containment-audit.cjs
Result: passed, 76 files, 1,244 text elements, zero violations

NODE_PATH=/private/tmp/owos-module18-qa/node_modules node apps/meaning-before-models/qa/module-18-structured-browser-validation.cjs
Result: passed, five page runs, zero failures

python3 tools/course_distinctiveness.py --course apps/meaning-before-models
Result: passed, 18 lessons, 18 archetypes

python3 tools/audit-structured-authoring.py
Result: passed after all affected structured curriculum outputs were rebuilt against the shared runtime
```

## Manual review still required

- [ ] Hardeep working review
- [ ] Independent semantic-technology and agent-security review
- [ ] Wastewater operations, maintenance, cybersecurity, and governance practitioner review
- [ ] Novice learner observation
- [ ] Screen-reader and physical-device review
- [ ] Module 19 course-coherence review
- [ ] Platform, live URL, authentication, and release review

## Required revisions

- Repaired the structured-compiler compatibility path in the legacy full-module conformance checker.
- Added Author Studio desktop, iPad, iPhone, 200 percent, and 400 percent review controls.
- Keep practitioner, independent source, screen-reader, physical-device, Module 19 coherence,
  credential, and final-release gates pending until named human evidence exists.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | pending Hardeep Anand | | Structured candidate ready |
| Capability benchmark | Module 05 remains governing benchmark | 2026-07-24 | Capability standard, not page template |
| Module release | blocked | | Module 19 and course assembly remain |
