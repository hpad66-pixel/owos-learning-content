---
module_id: aia001:04
course_id: owos-course-ai-agents-001
version: 0.6.0
review_date: 2026-07-22
reviewer: Codex working review
score: 92
score_out_of: 100
working_status: conditional_pass
release_status: blocked
---

# Module 4 Quality-Control Report

## Decision

- Working-review result: Conditional pass
- Release result: Blocked
- Score: 92 out of 100
- One-sentence reason: All repository-verifiable technical revisions are complete, including the new visual scene, explicit playback controls, responsive lesson graph, scored application check, claim-level source map, accessibility record, and reviewer packets. Real practitioner, learner, device, and live-runtime evidence still cannot be manufactured.

The numeric score summarizes quality. It does not override a failed hard gate. The scoring weights were corrected in version 0.6.0 so the ten areas total exactly 100 points.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 12 | 12 | Visible instructor explanations, component reading guidance, debriefs, eight module scripts, and course overview script | Validate comprehension with real novice learners |
| Learning design and sequence | 12 | 12 | Consequential decision, visual record conflict, packet anatomy, cause map, orchestration, repair, authority, work product, application check, knowledge checks, and recap | No repository-verifiable design gap |
| Explanatory graphics and visual reasoning | 12 | 12 | Original outfall evidence scene, packet anatomy, failure chain, swimlane, ledger, funnel, heat grid, authority ladder, and responsive lesson graph | Complete real-device visual review |
| Interactions and simulations | 12 | 12 | Architecture choice, packet comparison, Back, Step, Play, Pause, Reset, role selection, repair laboratory, permission console, contract builder, assessments, and graph drawer | Complete real-browser state-transition review |
| Utility relevance and practitioner credibility | 10 | 8 | Harbor County stormwater evidence scenario, utility records, role boundaries, and professional contract | Qualified stormwater or regulatory practitioner review |
| Assessments and feedback | 10 | 10 | Deterministic multi-select, ordering, multiple choice, reflection, retries, plus a five-criterion scored contract, now distributed where each concept is taught | Verify mastery-event recording in the authenticated runtime |
| Professional work product | 5 | 5 | Orchestration and Handoff Contract with preview, persistence, download, and deterministic scoring | No material working-candidate gap |
| Accuracy, evidence, and citations | 10 | 9 | Controlled claims AG-009, AG-015 through AG-021, exact source register identifiers, public links, limitations, and scenario boundary | Independent final source review; private McKinsey reuse boundary remains restricted |
| Accessibility, responsive behavior, and reduced motion | 10 | 8 | Semantic controls, explicit labels, live regions, SVG title and description, visible reading guide, responsive rules, focus return, reduced motion, and static accessibility report | Keyboard, screen-reader, contrast, zoom, touch, and real-device review |
| Platform integration and release controls | 7 | 4 | Stable identifiers, versioned browser persistence, enrollment endpoint, learner-event endpoint, honest error feedback, and live-integration checklist | Authenticated API and Supabase verification, manifest, intake, and release approval |
| **Total** | **100** | **92** | **All repository-verifiable revisions complete** | **External and runtime gates remain open** |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | Claim-level source table and boundaries are visible in the lesson | Independent final source review and private-source permission decision |
| Learning design | passed for working review | Complete sequence, visual pacing, teaching, interactions, assessments, and work product | Hardeep decides whether it becomes the production benchmark |
| Utility-practitioner review | blocked | Review packet is ready at `qa/module-04-practitioner-review-form.md` | Qualified practitioner records a decision |
| Technical and accessibility review | conditional | Automated and static checks pass; static review is recorded | Real desktop, mobile, keyboard, screen-reader, touch, zoom, contrast, and reduced-motion review |
| Release control | blocked | Course remains `golden-candidate` and private | Live integration, manifest, intake review, benchmark approval, and release approval |

## Completed technical revisions

1. Added explicit Back, Step, Play, Pause, and Reset controls.
2. Made the lesson graph follow the active role and evidence concept.
3. Added a deterministic five-part application check using the learner's contract.
4. Prevented an unscored saved contract from satisfying lesson completion.
5. Added an original explanatory illustration of the outfall and conflicting records.
6. Added a visible reading guide and accessible description for the illustration.
7. Added claim-level source identifiers, public links, locators, and limitations.
8. Added a source-level accessibility review and permanent visual-pacing rule.
9. Added qualified-practitioner and novice-learner review packets.
10. Added a live API and Supabase verification checklist with required evidence.
11. Corrected the quality-score weights so the categories total 100 points.

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | passed | `tools/test-ai-agent-golden-lesson.py` |
| Application controls | passed | `tools/test-ai-agent-module-04-application.py` |
| JavaScript and component configuration | passed | JavaScript parser, curriculum checks, design-system checks, and workspace tests |
| Deterministic assessment | passed | Answer keys, five contract criteria, gating logic, and explanatory feedback |
| Instructor explanation coverage | passed | Tagged instructor explanations and scripts |
| Graphic teaching and visual pacing | passed in source | Evidence scene, reading guide, responsive graph, packet, cause map, and permanent pacing rule |
| Prohibited language and punctuation | passed for changed learner content | Changed learner-facing source contains no prohibited dashes or invalid sentinel text |
| Repository formatting | passed | Workspace scan and `git diff --check` |

## Manual review still required

- [ ] Desktop visual review in a connected browser
- [ ] Mobile visual and touch review on real breakpoints
- [ ] Keyboard-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Contrast and 200 to 400 percent zoom review
- [ ] Reduced-motion walkthrough
- [ ] Qualified stormwater or regulatory practitioner review
- [ ] Novice-learner comprehension pilot
- [ ] Authenticated learner-event, enrollment, and Supabase verification
- [ ] Independent final source review
- [ ] Hardeep approval as the production benchmark
- [ ] Course release approval

## Required remaining work

1. Run and record the real practitioner review.
2. Run and record the novice-learner pilot.
3. Complete real-browser, device, keyboard, screen-reader, contrast, zoom, touch, and reduced-motion review.
4. Verify authenticated events and persistence in the deployed OWOS and Supabase runtime.
5. Obtain explicit benchmark and release decisions.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Technical revision authorization | Hardeep Anand | 2026-07-22 | Complete all repository-verifiable items and add meaningful visual relief |
| Working-review acceptance | pending | | Score and open gates are ready for review |
| Production benchmark | pending | | Requires explicit approval after hard-gate work |
| Release | pending | | Course remains private and unreleased |

## Version 0.9.2 FAQ review

Passed mechanically: four Module 4 questions, direct plain-English answers, utility examples, visual module map, semantic disclosure controls, and Community escalation are connected. Authenticated desktop, mobile, keyboard, and novice-learner review remain required.
