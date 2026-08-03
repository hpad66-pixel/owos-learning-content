# AI Master Class Authoring Workspace

This is the governed source workspace for the One Water OS AI Master Class series.

It is not a public course page and it is not an Articulate export. It is the place where research,
Hardeep's direction, instructional design, evidence, source files, Articulate-ready manuscripts,
and quality records remain connected and version controlled.

## Start here

1. Place a new PDF, transcript, white paper, or source file in `inbox/`.
2. Add spoken or typed direction to `author-input/` or send it in Codex. Codex records substantive
   direction under `conversations/`.
3. Keep the course-wide purpose, audience, outcomes, and planned sequence in `SYLLABUS.md`.
4. Build a module only after its source and teaching intent are clear. Module 01 is the working
   example at `curriculum/modules/module-01-ai-in-utility-work/`.
5. When a module is approved, use its Articulate import package in `articulate/` to make the
   initial Rise or Storyline draft. Articulate accelerates production. This repository remains the
   source of truth.

## Structure

```text
research/                 original sources, claims, evidence boundaries, annotations
author-input/             Hardeep's direction and approved examples
curriculum/               syllabus, design matrix, module briefs, manuscripts, scripts
curriculum/modules/       one folder per approved module
articulate/               controlled import packages and assembly runbook
assessments/              assessment blueprints and answer rationales
assets/                   approved images, diagrams, audio, and release-safe media
work-products/            learner tools created through the course
qa/                       module and course QA reports
release/                  build receipts, release notes, and delivery records
```

Do not create 64 empty module folders in advance. When the approved syllabus has 64 modules,
`curriculum/modules/` will contain 64 identically structured module folders. Creating them only
when their position and learning job are approved prevents a maze of empty folders and preserves
one clear source of truth.

## Delivery boundary

- **This repository:** research, evidence, authoring, review, reusable package, and history.
- **Articulate Rise or Storyline:** responsive course assembly, interactions, narration, and
  SCORM or cmi5 compatible package.
- **LearnWorlds:** learner-facing enrollment, delivery, community, cohorts, and commerce.
- **OWOS GraphDB:** governed concepts, claims, sources, relationships, and contextual retrieval.

Nothing moves to public delivery or the shared knowledge graph without the approval recorded in
`APPROVALS.md`.
