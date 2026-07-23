---
module_id: mbm001:08
course_id: owos-course-semantic-data-ai-001
version: production-candidate-1
review_date: 2026-07-23
reviewer: Codex repository review
score: 86
score_out_of: 100
working_status: conditional_candidate
release_status: blocked
---

# Module Quality-Control Report: Ask the Graph with SPARQL

## Decision
- Working-review result: Conditional production candidate.
- Release result: Blocked.
- Score: 86 out of 100.
- One-sentence reason: Repository-verifiable implementation is complete; human and runtime gates remain.

## Scored quality review
| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 12 | 11 | Instructor explanations before all major components | Novice pilot |
| Learning design and sequence | 12 | 11 | Decision, model, mechanism, boundary, artifact | Human review |
| Explanatory graphics and visual reasoning | 12 | 10 | Four traced visual types | Rendered inspection |
| Interactions and simulations | 12 | 10 | Mechanism, boundary selection, artifact | Browser walkthrough |
| Utility relevance and practitioner credibility | 10 | 8 | Named utility scenario | Practitioner review |
| Assessments and feedback | 10 | 10 | Four quiz types and retry | Learner observation |
| Professional work product | 5 | 5 | Question-to-Query Sheet | Practitioner review |
| Accuracy, evidence, and citations | 10 | 8 | W3C sources and boundary | Independent factual review |
| Accessibility, responsive behavior, and reduced motion | 10 | 7 | Static labels, CSS, focus code | Manual accessibility |
| Platform integration and release controls | 7 | 6 | IDs, local persistence, blocked release | Authenticated events |
| **Total** | **100** | **86** | Repository evidence | Human gates remain |

## Hard gates
| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | W3C links and explicit limits | Independent review |
| Learning design | passed | Complete lesson contract | Hardeep working review |
| Utility-practitioner review | blocked | Not yet performed | Qualified practitioner review |
| Technical and accessibility review | conditional | Static checks only | Browser, device, keyboard, screen-reader, contrast |
| Release control | blocked | Candidate metadata | Explicit release approval |

## Automated checks
| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | passed | Full-module conformance validator |
| JavaScript and component configuration | passed static check | Shared runtime and governed sources |
| Deterministic assessment | passed by code inspection | Explicit answers and criteria |
| Distributed quiz placement and feedback | passed | Four quiz types across lesson |
| Instructor explanation coverage | passed | Every governed component traced |
| Module-specific FAQ coverage and answer quality | passed repository check | Five questions |
| Graphic teaching coverage | passed | Reading guides and conclusions |
| Visual pacing and editorial illustration | passed repository check | Design brief trace |
| Header Graph, Community, and Start actions, side drawers, and bottom connected-learning section | passed repository check | Required markers |
| Explicit bottom connected-learning anchor and rendered DOM order | passed | Anchor before navigation |
| Dark-surface contrast guard | passed static check | Light text rules |
| Prohibited language and punctuation | passed | Validator scan |
| Repository scan and formatting | passed | Course regression suite |

## Manual review still required
- [ ] Desktop visual review
- [ ] Mobile visual and touch review
- [ ] Keyboard-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Reduced-motion walkthrough
- [ ] Dense-text and visual-pacing walkthrough
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
1. Complete factual and practitioner review.
2. Complete rendered accessibility and device review.
3. Obtain explicit release approval.

## Approval record
| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | pending Hardeep Anand | | |
| Production benchmark | working benchmark | 2026-07-23 | Module 05 capability level |
| Release | blocked | | |
