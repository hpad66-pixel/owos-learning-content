---
name: continue-owos-course
description: Continue an OWOS course from new PDFs, Word files, research, annotations, Wispr Flow dictation, and typed direction. Use when the user says continue this course, update the course from new material, ingest course research, shape the curriculum, build or revise a golden lesson, produce course modules, or prepare an OWOS course release. Operate inside the selected course folder under owos-learning-content/apps and automatically apply Hardeep Soul, course standards, provenance, state, approval, and release controls.
---

# Continue an OWOS Course

Give the user one conversational workspace. Never make the user operate internal scripts.

## Start

1. Identify the course under `apps/`. If ambiguous, list the likely course folders and ask one question.
2. Read, in order:
   - the course `AGENTS.md`, `COURSE-BRIEF.md`, `STATE.md`, `APPROVALS.md`, `course.yaml`, and `SYLLABUS.md`;
   - `../../../hardeep-soul/SOUL.md` and `../../../hardeep-soul/authoring/AUTHORING_STANDARD.md`;
   - `../../core/standards/COURSE-OPERATING-STANDARD.md` and `../../core/standards/WRITING-STANDARD.md`, resolving paths from the course directory.
3. Treat the current user message as course input. Preserve the user's substantive wording in a dated file under `conversations/` unless it is already recorded.
4. Run the internal workspace scan. Do not ask the user to run it:

   ```bash
   python3 tools/course_workspace.py scan --course <slug>
   ```

5. Report what is new, what changed, and what approval is needed. Then continue useful work without waiting when no material decision is missing.

## Process new material

- Preserve originals. Never overwrite or summarize away the only copy.
- Move accepted inbox files into `research/originals/` only after recording the original filename and checksum.
- Extract complete documents with page or section locators. Treat extraction coverage as a measurable result.
- Separate sourced fact, expert interpretation, Hardeep Anand position, utility example, teaching instruction, and unresolved question.
- Update `research/SOURCE-REGISTER.md`, `research/CLAIMS-REGISTER.md`, and `research/EVIDENCE-BOUNDARIES.md` as evidence changes.
- Use primary sources for load-bearing claims. Browse when current or external verification is required.
- Do not expose private, internal, sealed, or permission-pending material.

## Build the course

Follow the current phase in `STATE.md`:

1. Research: inventory, extraction, claims, limitations, and Hardeep direction.
2. Blueprint: course promise, audience, outcomes, modules, work products, competencies, assessments, and graph plan.
3. Golden lesson: build one complete lesson for Hardeep's approval.
4. Production: build remaining lessons from the approved benchmark without repetitive template writing.
5. Validation: run the Course Quality Contract and relevant visual, mobile, accessibility, content, and release checks.
6. Release: commit source and reproducible output, push a reviewed GitHub change, and intake the exact release into OWOS only after approval.

Never skip from research to bulk lesson generation. Never publish because a file was added.

## Apply Hardeep Soul

- Use the approved Soul file as the voice and boundary constitution, not as factual evidence.
- Preserve spoken cadence, utility grounding, and Hardeep's distinctions.
- Attribute Hardeep's positions to Hardeep. Do not disguise them as independent facts.
- Do not edit `SOUL.md`. Queue candidate improvements in the course state for Hardeep's approval.
- Enforce no em dashes, no corporate filler, no unsupported claims, and no sealed material.

## Maintain durable memory

Before ending every material course turn:

- append the user's new direction to `conversations/`;
- update `STATE.md` with completed work, current phase, new sources, unresolved decisions, and next action;
- update `APPROVALS.md` when Hardeep approves or rejects a blueprint, golden lesson, claim boundary, or release;
- update the source and claims registers when evidence changed;
- leave all changed artifacts readable in Git;
- commit and push when the user asked to publish or when the established repository workflow explicitly requires it.

The repository is the memory. Do not rely on chat history as the only record.

## Approval gates

Require Hardeep's explicit approval before:

- promoting a personal statement into Hardeep Soul;
- locking the curriculum blueprint;
- using the golden lesson as the production benchmark;
- publishing to the shared graph;
- issuing a credential claim;
- releasing or deploying the course.

Ordinary extraction, research organization, draft improvement, validation, and state maintenance do not require repeated permission.

## Internal controls

Run tools yourself. Keep their output concise and translate failures into plain English. The user should see decisions, progress, evidence, and results, not command choreography.

Read [course-contract.md](references/course-contract.md) when creating a new course, preparing a release, or resolving repository ownership.
