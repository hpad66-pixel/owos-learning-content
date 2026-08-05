# One Water AI Academy Author Studio Planning Direction

Date: 2026-08-04

Owner: Hardeep Anand

## Direction

Hardeep wants the complete One Water AI curriculum to become an internal, editable Academy
production system. The team must be able to expand, edit, annotate, and review the curriculum without
needing a Codex prompt for ordinary work. Every meaningful change must retain its author, reason,
review state, approval, and release lineage.

The product is more than a document editor. It must coordinate the complete module lifecycle:

1. research brief and research production;
2. research quality control and claim verification;
3. manuscript and instructional development;
4. graphic brief, production, and graphic quality control;
5. script and Articulate production;
6. integrated content, accessibility, and technical quality control;
7. packaging and final release review;
8. hosting and live verification;
9. corrections, new versions, and rollback.

Quality control must be visible at every stage. A handoff must carry the artifact, evidence,
checklist result, unresolved work, owner, reviewer, due date, and requested decision. A status change
alone must never authorize the next controlled action or publish a module.

## Team context

- Hardeep Anand is CEO and final authority.
- Simi organizes the Academy with Hardeep and supports marketing administration.
- Rohit supports marketing administration.
- Amritpal is the graphic designer.
- Dhruman, Anmol, and Shreya are technical team members.

Permanent role authority has not been assigned. The plan proposes capability-based roles and a
responsibility matrix for Hardeep's approval.

## Product direction

Hardeep approved creation of a durable implementation plan after a four-agent discovery pass. The
master plan lives in the platform repository because OWOS Author Studio, authentication, Supabase,
workflow APIs, and internal web delivery are platform responsibilities:

`../../../onewater-os-platform/product/one-water-ai-academy-author-studio-plan.md`

The curriculum, sources, claims, manuscripts, QA records, builders, and release records remain
governed in `owos-learning-content`.

The interface should draw inspiration from `apas.ai`: deep ink and Graphite application chrome,
warm cream reading surfaces, water-blue actions, restrained depth, editorial typography, strong
evidence cues, and one clear job per page. The internal application must preserve accessibility and
working clarity instead of copying marketing-page scale or effects.

## Discovery finding requiring an owner decision

The current repository contains two distinct 64-module curriculum lines with overlapping display
numbers:

1. the legacy M00 through M63 curriculum that produces the current 788-page PDF and HTML reader;
2. the separate eight-course M1 through M64 Executive Fellowship syllabus.

The planning decision is to register both lines separately before enabling edits. They may be
aligned or consolidated only after Hardeep approves their relationship. No current module, planned
addition, source, or generated output is silently merged or renumbered.

## Approved planning boundary

The completed plan is for review. Hardeep's `ok` authorized writing the plan and durable records. It
did not authorize application implementation, curriculum-line consolidation, a blueprint lock,
Articulate production, public release, deployment, Graph publication, or credential claims.

The recommended first implementation slice is a read-only Curriculum Registry and Command Center,
followed by one controlled Module 01 editing and review pilot after Hardeep identifies the intended
curriculum line.
