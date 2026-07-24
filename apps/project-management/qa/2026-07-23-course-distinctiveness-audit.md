# Utility Project Delivery Course Distinctiveness Audit

Date: 2026-07-23
Status: passed after targeted correction

## Decision

This remains the strongest current end-to-end learner experience. Its schedules, cost models,
commercial reviews, field decisions, risk simulations, project artifacts, and capstone are genuinely
subject-specific.

The initial gate found one course-level repetition blocker: Modules 10, 12, 15, and 17 used an
identical quiz sequence. The targeted correction is complete. The course does not require a
wholesale visual rebuild.

## Completed correction

- Module 10 now uses `diagnostic-repair` followed by `quality-record-gate`.
- Module 12 now uses `role-conversation` followed by `stakeholder-brief-gate`.
- Module 15 now uses `dashboard-forensics` followed by `status-brief-gate`.
- Module 17 now uses `readiness-gate` followed by `readiness-pack-gate`.

## Verification

- `python3 tools/course_distinctiveness.py --course apps/project-management`
- Result: `PASSED: 21 lessons, 21 archetypes`
- Scoped regression result: four targeted lessons, four unique quiz sequences, 32 component
  configurations parsed, and preserved simulations verified.

Read-without-video reviews for schedule, earned-value, contract, and risk lessons remain outside this
targeted four-module correction and are not represented as complete here.
