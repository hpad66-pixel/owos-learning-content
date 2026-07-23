---
module_id: aia001:04
course_id: owos-course-ai-agents-001
version: 0.5.0
review_date: 2026-07-22
reviewer: Codex working review
score: 86
score_out_of: 100
working_status: conditional_pass
release_status: blocked
---

# Module 4 Quality-Control Report

## Decision

- Working-review result: Conditional pass
- Release result: Blocked
- Score: 86 out of 100
- One-sentence reason: The lesson is a strong working candidate with complete teaching, graphics, simulations, assessments, and a work product, but it has not passed practitioner review, live mobile and assistive-technology testing, source-level review, or runtime integration verification.

The numeric score summarizes quality. It does not override a failed hard gate.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 15 | 14 | Ten visible instructor-explanation blocks, component reading guidance, debrief, eight module scripts, and course overview script | Run a novice-learner comprehension pilot and revise language that causes hesitation |
| Learning design and sequence | 15 | 13 | Consequential opening decision, packet anatomy, cause map, orchestration, repair, authority, work product, checks, and recap | Strengthen role-specific teaching beyond the short Foundation, Practitioner, and Leader introductions |
| Explanatory graphics and visual reasoning | 15 | 12 | Handoff packet anatomy, failure-propagation chain, swimlane, ledger, funnel, heat grid, authority ladder, and lesson graph | Complete live desktop and mobile visual review; improve the lesson graph so it follows active evidence as the design brief specifies |
| Interactions and simulations | 15 | 12 | Architecture choice, packet comparison, handoff playback, repair laboratory, permission console, contract builder, assessments, and graph drawer | Add explicit Step, Pause, and Reset controls promised by the design brief and test every state transition in a browser |
| Utility relevance and practitioner credibility | 10 | 8 | Harbor County stormwater evidence scenario, utility roles, operating boundaries, and professional contract | Obtain a qualified stormwater or regulatory practitioner review |
| Assessments and feedback | 10 | 8 | Deterministic multi-select, ordering, multiple choice, reflection, retries, and explanatory feedback | Add a scored application check using the saved contract and verify mastery-event recording |
| Professional work product | 5 | 5 | Orchestration and Handoff Contract with preview, saved state, and download | No material design gap in the working candidate |
| Accuracy, evidence, and citations | 10 | 6 | Public source map, scenario boundary, primary guidance links, provenance concepts, and controlled claims register | Complete claim-level citation review, verify exact locators, and resolve the private-source permission boundary |
| Accessibility, responsive behavior, and reduced motion | 10 | 5 | Viewport, responsive rules, reduced-motion CSS, live regions, button labels, focus return, and static accessibility checks | Run keyboard-only, screen-reader, touch, contrast, reduced-motion, and real-device mobile reviews |
| Platform integration and release controls | 5 | 3 | Stable course and module identifiers, browser persistence, enrollment endpoint, learner-event endpoint, and honest release state | Verify events against the live API and Supabase, build the release manifest, run platform intake, and obtain release approval |
| **Total** | **100** | **86** | **Strong working candidate** | **Not production ready** |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | Source map and instructional boundary exist | Claim-level citation and source-locator review; private-source boundary resolved |
| Learning design | passed for working review | Complete lesson sequence, teaching, graphics, interactions, assessments, and work product | Hardeep decides whether it becomes the production benchmark |
| Utility-practitioner review | blocked | Scenario is grounded in stormwater evidence work | Qualified practitioner signs off or records revisions |
| Technical and accessibility review | conditional | Automated contract and static accessibility checks pass | Live desktop, mobile, keyboard, screen-reader, touch, and reduced-motion review |
| Release control | blocked | Course remains `golden-candidate` and private preview | Live event verification, manifest, intake review, and explicit release approval |

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | passed | `tools/test-ai-agent-golden-lesson.py` |
| JavaScript and component configuration | passed | JavaScript parsed successfully; component gallery script parsed successfully |
| Deterministic assessment | passed | Answer keys and explanatory feedback are present |
| Instructor explanation coverage | passed | Ten tagged instructor explanations are enforced |
| Graphic teaching coverage | passed | Packet anatomy and cause-map requirements are enforced |
| Prohibited language and punctuation | passed | Changed lesson and script files contain no prohibited dashes or blocked filler |
| Repository scan and formatting | passed | Course workspace scan and `git diff --check` passed |

## Manual review still required

- [ ] Desktop visual review after the current browser connection is available
- [ ] Mobile visual and touch review on real breakpoints
- [ ] Keyboard-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Reduced-motion walkthrough
- [ ] Qualified stormwater or regulatory practitioner review
- [ ] Novice-learner comprehension pilot
- [ ] Live learner-event, enrollment, and Supabase verification
- [ ] Final claim-level source and citation review
- [ ] Hardeep approval as the production benchmark
- [ ] Course release approval

## Required revisions

1. Add explicit Step, Pause, and Reset controls to the orchestration simulator so the implementation matches the approved design brief.
2. Make the lesson graph respond to the active role and evidence path instead of remaining a static concept view.
3. Complete practitioner, mobile, assistive-technology, citation, and live integration reviews.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | pending | | Score and gaps are ready for Hardeep review |
| Production benchmark | pending | | Requires explicit approval after hard-gate work |
| Release | pending | | Course remains private and unreleased |
