---
module_id:
course_id:
version:
review_date:
reviewer:
score: 0
score_out_of: 100
working_status: not_reviewed
release_status: blocked
---

# Module Quality-Control Report

## Decision

- Working-review result:
- Release result:
- Score:
- One-sentence reason:

The numeric score summarizes quality. It never overrides a failed hard gate.
Keep `release_status: blocked` until every manual review and hard gate is complete and the Release
approval record is signed. Only then may an authorized human reviewer set `release_status: approved`.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 14 | 0 | | |
| Learning design and sequence | 12 | 0 | | |
| Course distinctiveness and lesson identity | 10 | 0 | | |
| Explanatory graphics and visual reasoning | 10 | 0 | | |
| Interactions and simulations | 10 | 0 | | |
| Utility relevance and practitioner credibility | 10 | 0 | | |
| Assessments and feedback | 10 | 0 | | |
| Professional work product | 5 | 0 | | |
| Accuracy, evidence, and citations | 8 | 0 | | |
| Accessibility, responsive behavior, and reduced motion | 6 | 0 | | |
| Platform integration and release controls | 5 | 0 | | |
| **Total** | **100** | **0** | | |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | not reviewed | | |
| Learning design | not reviewed | | |
| Course distinctiveness | not reviewed | | |
| Utility-practitioner review | not reviewed | | |
| Technical and accessibility review | not reviewed | | |
| Release control | not reviewed | | |

Allowed gate states are `passed`, `conditional`, `blocked`, and `not reviewed`.

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | | |
| Structured module package and compiler validation | | |
| Storyboard approval and beat coverage | | |
| Visual manifest asset resolution, license, and originality | | |
| Whole-course full-module conformance inventory | | |
| JavaScript and component configuration | | |
| Deterministic assessment | | |
| Distributed quiz placement and feedback | | |
| Instructor explanation coverage | | |
| Read-without-video teaching coverage | | |
| Course-level structural distinctiveness | | |
| Module-specific FAQ coverage and answer quality | | |
| Graphic teaching coverage | | |
| Visual pacing and editorial illustration | | |
| Rendered desktop, tablet, and phone evidence | | |
| Course coherence dependencies and terminology | | |
| Header Graph, Community, and Start actions, side drawers, and bottom connected-learning section | | |
| Explicit bottom connected-learning anchor and rendered DOM order | | |
| Dark-surface contrast guard | | |
| Prohibited language and punctuation | | |
| Repository scan and formatting | | |

## Manual review still required

- [ ] Desktop visual review
- [ ] Tablet visual and touch review
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

1.
2.
3.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | | | |
| Production benchmark | | | |
| Release | | | |
