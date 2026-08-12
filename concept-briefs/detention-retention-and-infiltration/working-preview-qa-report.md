---
module_id: owos:concept-brief:003
course_id: owos-concept-briefs
version: PREVIEW 0.3
review_date: 2026-07-26
reviewer: Codex working-preview QA
score: 80
score_out_of: 100
working_status: owner_review_required
release_status: blocked
---

# Detention, Retention, and Infiltration Working-Preview QA Report

## Decision

- Working-review result: Preview 0.3 is ready for owner review after preview 0.2 was rejected.
- Release result: Blocked.
- Score: 80/100.
- One-sentence reason: The definition-first opening, instructor explanations, editorial gutters, visual frames, pathway tracer, assessments, responsive layouts, and fallbacks now work, but owner acceptance, independent verification, qualified reviews, and required accessibility reviews remain incomplete.

The numeric score summarizes working-preview quality. It never overrides a failed hard gate.

## Scored quality review

| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 12 | 11 | Visible definitions and expanded introductions now precede the route, storage, infiltration, hydrograph, maintenance, I&I, permit, finance, and role components | Owner, editorial, and novice-reader review |
| Learning design and sequence | 12 | 11 | Thirteen-beat sequence introduces the terms before applying them to one storm | Owner review and learner pilot |
| Explanatory graphics and visual reasoning | 12 | 11 | Ten graphics use aligned frames, reading guides, conclusions, desktop views, and phone views | Specialist visual-truth and mobile graphic-text review |
| Interactions and simulations | 12 | 11 | Three-route tracer, deterministic controls, live region, and no-JavaScript fallback | Screen-reader walkthrough |
| Utility relevance and practitioner credibility | 10 | 7 | Stormwater, wastewater, finance, leadership, permit, maintenance, and public-accountability explanations are visible | Qualified practitioner review |
| Assessments and feedback | 10 | 9 | Terminology check and applied work product passed deterministic browser tests | Human editorial review |
| Professional work product | 5 | 5 | Four-field pathway statement | Practitioner acceptance |
| Accuracy, evidence, and citations | 10 | 2 | Federal/EPA source identities and locators preserved | Independent claim verification is 0% |
| Accessibility, responsive behavior, and reduced motion | 10 | 8 | Desktop, phone, reduced-motion, focus, live-region, and no-JavaScript checks passed | Tablet, screen-reader, and manual keyboard/touch reviews |
| Platform integration and release controls | 7 | 5 | Graph and Community drawers, focus return, recap, and feedback form work | Publication and release approvals |
| **Total** | **100** | **80** | | |

## Hard gates

| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | blocked | Verification coverage is 0% | Independent source and qualified technical review |
| Learning design | blocked | Owner rejected preview 0.2; preview 0.3 implements the requested corrections | Owner, editorial, and learner review |
| Utility-practitioner review | blocked | Not performed | Qualified practitioner review |
| Technical and accessibility review | conditional | Automated and rendered working-preview checks passed | Screen-reader, manual keyboard/touch, and tablet review |
| Release control | blocked | Working-preview approval only | Graph, Community, commercial, credentials, and explicit release approvals |

## Automated checks

| Check | Result | Evidence |
| --- | --- | --- |
| Concept Brief package contract | Passed for working state | `python3 tools/concept_brief_compiler.py validate concept-briefs/detention-retention-and-infiltration` |
| Compiler regression | Passed | `python3 tools/test-concept-brief-compiler.py` |
| HTML compilation | Passed | Internal and clean public-review working previews compiled |
| Deterministic interaction and assessments | Passed | Tracer, distributed checks, failure trace, and 12-part applied work product completed in both JavaScript browser modes |
| Desktop and phone containment | Passed | No horizontal overflow elements at 1440 or 390 pixels; the definition table becomes stacked labeled records on phones |
| Reduced motion | Passed | Phone run reported reduced motion and automatic scroll behavior |
| No-JavaScript equivalent | Passed | Three structured text routes, boundaries, and both explanatory images remained available |
| Graph and Community controls | Passed | Both drawers opened, closed, and returned focus |
| Runtime errors and empty controls | Passed | Zero console/page errors, no empty buttons, no visible `undefined` or `NaN` |

## Manual review still required

- [x] Desktop visual review
- [x] Mobile visual review
- [x] Reduced-motion visual review
- [x] No-JavaScript visual review
- [ ] Tablet visual review
- [ ] Keyboard-only walkthrough
- [ ] Touch-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Qualified technical practitioner review
- [ ] Independent source and claim review
- [ ] Editorial review
- [ ] Novice-reader comprehension review
- [ ] Graph and Community publication review
- [ ] Commercial conflict review
- [ ] Owner release approval

## Required revisions

1. Independently verify every material claim and complete qualified technical review.
2. Obtain owner review of the preview 0.3 introduction, margins, diagrams, and instructional depth.
3. Complete the unresolved accessibility, device, editorial, practitioner, and learner reviews.
4. Keep the artifact in working-preview state until every publication and release approval is explicit.

## Approval record

| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Preview 0.2 rendered review | Hardeep Anand | 2026-07-26 | Rejected for weak instruction, late definitions, margins, and graphic-text alignment |
| Preview 0.3 rendered review |  |  | Pending |
| Production benchmark |  |  | Pending |
| Release |  |  | Pending |
