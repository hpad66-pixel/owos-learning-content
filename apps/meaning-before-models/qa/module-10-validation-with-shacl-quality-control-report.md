---
module_id: mbm001:10
course_id: owos-course-semantic-data-ai-001
version: retrofit-working-candidate
review_date: 2026-07-23
reviewer: Codex working review
score: 94
score_out_of: 100
working_status: accepted_for_human_review
release_status: blocked
---

# Module 10 Quality-Control Report

## Decision

- Working-review result: Accepted as a distinct inspection-lab working candidate.
- Release result: Blocked pending human factual, practitioner, accessibility, mobile, and release gates.
- Score: 94/100
- One-sentence reason: The module now makes SHACL concrete through a live shape console, actionable result packet, and remediation workflow.

The numeric score summarizes quality. It never overrides a failed hard gate.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 14 | 14 | Data graph, shapes graph, focus node, result, and boundary explanations | Novice pilot |
| Learning design and sequence | 12 | 12 | Failed intake through Constraint Card | Human learning review |
| Course distinctiveness and lesson identity | 10 | 10 | Inspection station and unique signature | Whole-course diagnostic |
| Explanatory graphics and visual reasoning | 10 | 10 | Packet, comparison, propagation chain | Manual visual review |
| Interactions and simulations | 10 | 10 | Shape console and result router | Browser walkthrough |
| Utility relevance and practitioner credibility | 10 | 9 | Pump handoff and remediation | Practitioner review |
| Assessments and feedback | 10 | 10 | Four distinct checks and retry | Live event verification |
| Professional work product | 5 | 5 | SHACL Constraint Card | Practitioner usefulness review |
| Accuracy, evidence, and citations | 8 | 7 | W3C SHACL sources | Final factual review |
| Accessibility, responsive behavior, and reduced motion | 6 | 4 | Semantic inputs, live regions, responsive and reduced-motion CSS | Manual assistive review |
| Platform integration and release controls | 5 | 3 | Drawers, persistence, completion | Production integration review |
| **Total** | **100** | **94** | | |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | W3C SHACL sources and caveats | Human factual review |
| Learning design | passed | Distinct inspection sequence | None for working review |
| Course distinctiveness | conditional | Unique local fingerprint | Whole-course diagnostic |
| Utility-practitioner review | not reviewed | Utility examples are instructional | Practitioner sign-off |
| Technical and accessibility review | conditional | Responsive implementation and accessible feedback | Browser and assistive review |
| Release control | blocked | Working-candidate metadata | Human release approval |

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | passed | Module conformance returned full-module working conformance |
| JavaScript and component configuration | source reviewed | Console and router handlers |
| Deterministic assessment | passed by inspection | Exact configuration and routing checks |
| Distributed quiz placement and feedback | passed by inspection | Intake, console, route, transfer |
| Instructor explanation coverage | passed by inspection | Coach blocks precede governed items |
| Read-without-video teaching coverage | passed by inspection | Written-first lesson |
| Course-level structural distinctiveness | blocked outside this module batch | Diagnostic blockers are confined to unrevised Modules 14-18 |
| Module-specific FAQ coverage and answer quality | passed by inspection | Six SHACL questions |
| Graphic teaching coverage | passed by inspection | Three governed visual types |
| Visual pacing and editorial illustration | passed by inspection | Inspection surfaces break prose |
| Header Graph, Community, and Start actions, side drawers, and bottom connected-learning section | passed by inspection | Present |
| Explicit bottom connected-learning anchor and rendered DOM order | passed by inspection | Correct order |
| Dark-surface contrast guard | passed by inspection | Shape console and shared drawer |
| Prohibited language and punctuation | passed | Conformance scan |
| Repository scan and formatting | passed | Scoped `git diff --check` |

## Manual review still required

- [ ] Desktop visual review
- [ ] Mobile visual and touch review
- [ ] Keyboard-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Reduced-motion walkthrough
- [ ] Dense-text and visual-pacing walkthrough
- [ ] Read-without-video novice walkthrough
- [ ] Adjacent-module and whole-course distinctiveness walkthrough
- [ ] Graph and Community drawer, close, focus-return, and bottom-section walkthrough
- [ ] Dark blue, navy, and gradient contrast walkthrough
- [ ] Quiz discoverability and section-placement walkthrough
- [ ] FAQ accuracy, plain-language, utility-example, disclosure, and mobile walkthrough
- [ ] Utility-practitioner review
- [ ] Novice-learner comprehension pilot
- [ ] Live learner-event and enrollment verification
- [ ] Final source and citation review
- [ ] Release approval

## Required revisions

1. Confirm SHACL terminology and severity explanations in human factual review.
2. Validate touch, keyboard, screen-reader, and reduced-motion behavior.
3. Clear the full-course distinctiveness gate after remaining retrofits.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | Codex | 2026-07-23 | Accepted for human review |
| Production benchmark |  |  | Pending |
| Release |  |  | Blocked |
