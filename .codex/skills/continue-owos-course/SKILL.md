---
name: continue-owos-course
description: Continue an OWOS course from new PDFs, Word files, research, annotations, Wispr Flow dictation, and typed direction. Use when the user says continue this course, update the course from new material, ingest course research, shape the curriculum, build or revise a golden lesson, produce course modules, or prepare an OWOS course release. Operate inside the selected course folder under owos-learning-content/apps and automatically apply Hardeep Soul, course standards, provenance, state, approval, and release controls.
---

# Continue an OWOS Course

Give the user one conversational workspace. Never make the user operate internal scripts.

Use the standard name **OWOS Course Engine** for this lifecycle and **OWOS Course Compiler** for its
renderer. Visuals, interactions, animations, and quizzes resolve through the shared
`core/learning-capabilities/registry.yaml`; do not create a course-only copy of a shared capability.

## Start

1. Identify the course under `apps/`. If ambiguous, list the likely course folders and ask one question.
2. Read, in order:
   - the course `AGENTS.md`, `COURSE-BRIEF.md`, `STATE.md`, `APPROVALS.md`, `course.yaml`, and `SYLLABUS.md`;
   - `../../../hardeep-soul/SOUL.md` and `../../../hardeep-soul/authoring/AUTHORING_STANDARD.md`;
   - `../../core/standards/COURSE-PRODUCTION-CONTRACT.md`, `../../core/standards/COURSE-OPERATING-STANDARD.md`, `../../core/standards/COURSE-DESIGN-SYSTEM.md`, `../../core/standards/COURSE-EXPERIENCE-ARCHITECTURE.md`, `../../core/standards/VISUAL-ARSENAL.md`, and `../../core/standards/WRITING-STANDARD.md`;
   - `../../core/components/COMPONENTS.md`, `../../core/components/QUIZ-TYPES.md`, and the rendered component and quiz galleries, resolving paths from the course directory.
   - `../../core/standards/OWOS-COURSE-PRODUCTION-ACTIVATION-PROMPT.md` and
     `../../core/templates/COURSE-QUALITY-CONTROL-DOSSIER.md`.
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
3. Golden lesson: approve the module design brief and storyboard, then build one complete structured
   module package for Hardeep's approval.
4. Production: build remaining structured module packages from their own approved briefs and
   storyboards, without repetitive template writing.
5. Validation: compile deterministic HTML, then run the Course Quality Contract and relevant visual,
   mobile, accessibility, content, and release checks against the rendered experience.
6. Release: commit source and reproducible output, push a reviewed GitHub change, and intake the exact release into OWOS only after approval.

Never skip from research to bulk lesson generation. Never publish because a file was added.

## Design every module as its own learning experience

- Treat Chapter 09 as a capability benchmark, never as a page template.
- Complete `core/templates/COURSE-EXPERIENCE-BRIEF.md` before the first module design brief. Define a
  course-specific teaching voice, utility world, visual language, archetype rhythm, signature
  mechanisms, artifact family, and prohibited motifs.
- Complete `core/templates/MODULE-DESIGN-BRIEF.md` and an approved module storyboard before
  implementation. HTML is compiled delivery output and is never the authoring source for a new or
  materially rebuilt module.
- Maintain a course-level design matrix from `core/templates/COURSE-DESIGN-MATRIX.md`.
- Run the Visual Arsenal Selection Prompt against the actual teaching ideas.
- Create the structured module under `apps/<course>/modules/<module>/`. Keep `design-brief.md`, `module.yaml`,
  `storyboard.yaml`, `visuals/visual-manifest.yaml`, `interactions.yaml`, `assessments.yaml`,
  `sources.yaml`, `glossary.yaml`, and `qa.yaml` separately reviewable.
- Use `python3 tools/course_compiler.py validate <module-directory>` before building a preview. Use
  `python3 tools/course_compiler.py build <module-directory>` only after validation passes.
- Preserve the `owos-course-compiler/1` contract. Do not silently reinterpret an approved source
  package. Run `python3 tools/audit-structured-authoring.py` before stating that an existing course
  or portfolio is migrated; the audit must distinguish structured, hybrid, and legacy modules.
- Count a visual only when its manifest identifier resolves to a real asset or registered executable
  component. A visual label, card grid, colored box, icon row, or declared data attribute is not
  visual evidence.
- Require every visual manifest record to carry a teaching idea, learner conclusion, reading guide,
  alternative text, mobile treatment, reduced-motion treatment, creator, source, license,
  permission state, originality state, storyboard state, and rendered-review state.
- Use Author Studio for module-by-module review when visual or narrative control is needed. It edits
  structured source, preserves snapshots, validates the package, and previews the compiler output.
- Use the two to five substantial visual explanations the ideas require. Give every lesson one
  subject-specific signature mechanism. Select assessments from the thinking being taught instead of
  imposing the same quiz inventory.
- Distribute those quiz types across the lesson at the point of instruction. Label them clearly, provide immediate explanatory feedback and retry, and require one final applied check tied to the professional work product. Never hide the entire assessment experience at the bottom.
- Select narrative structure, simulations, graphics, animation, and work products from the learning problem. Do not create variety through colors alone.
- Copy governed components from the galleries. When the needed mechanism is missing, add an accessible, responsive, tested shared component before using it.
- Require every animation to teach change, cause, consequence, sequence, dependency, or reveal. Preserve meaning under reduced motion.
- Compare adjacent modules and change repeated opening patterns, dominant visuals, interaction pairs, quiz sequences, and work-product formats unless repetition is instructionally necessary.
- Keep the Knowledge Graph on the lesson page in a responsive panel or drawer. Closing it returns focus to the course.
- Use compact Graph, Community, and Start actions in the lesson header. Graph and Community open in white side drawers, never floating cards or hanging rails. Start moves to the beginning of the lesson. Reserve an explicit `#owos-course-community` anchor inside `main`, immediately before bottom lesson navigation, so the complete connected-learning section cannot mount inside a header or hero.
- End every module with an accessible, module-specific FAQ before the evidence boundary and bottom connected-learning section. Anticipate real novice questions, answer them in conversational plain English, and use a utility example, explanatory diagram, comparison, or worked sequence when it makes the answer easier to understand. A generic FAQ copied across modules does not pass.
- Treat dark text on a dark blue, navy, or gradient surface as a release blocker. Run the shared contrast guard and complete desktop and mobile contrast review.
- Teach every major visual, animation, simulation, assessment, and work-product interface in the lesson itself. Add one or two plain-English instructor paragraphs that explain what the learner is seeing, what action to take, what to notice, why it matters in utility work, and what the result means. A tooltip never replaces this teaching.
- Treat the written lesson as the complete instruction. Recording scripts are optional and are created
  only when the course modality plan includes video or narration. Media never substitutes for
  conversational teaching, worked examples, interface explanation, and debriefs in the lesson.
- Use explanatory graphics when a concept, method, framework, relationship, or cause chain has a visual shape. Select the graphic through the Visual Arsenal, explain how to read it, and state what it proves or clarifies. Do not add decorative stock art, repeated icon tiles, or graphics that merely restate a heading.
- Plan visual pacing before HTML production. Do not place more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout unless the module brief records why uninterrupted prose is necessary. Use an original editorial illustration when a utility setting, physical asset, record conflict, or accountable decision can be taught as a scene. Give it accessible text, a reading guide, and a learner conclusion.
- Complete `core/templates/MODULE-QA-REPORT.md` after every built module. Record a score out of 100, the evidence checked, missing work, automated results, manual reviews, and five hard gates. A numeric score never overrides a blocked accuracy, practitioner, accessibility, technical, or release gate. Store the course report under `apps/<course>/qa/` and show it to Hardeep after each module.
- Complete `core/templates/RENDERED-EXPERIENCE-REPORT.md` after browser review and
  `core/templates/COURSE-COHERENCE-REPORT.md` before release. Source inspection cannot substitute for
  rendered desktop, tablet, phone, keyboard, touch, reduced-motion, and read-without-video evidence.
- At course completion, create `qa/course-quality-control-dossier.md` from
  `core/templates/COURSE-QUALITY-CONTROL-DOSSIER.md`. Back every score with an exact artifact,
  checksum, screenshot, test result, review record, commit, deployment, or live verification.
  Package the evidence so Hardeep can inspect the basis of the score without reconstructing the run.
- Audit every rendered SVG text element against its intended container. Text clipping, overlap,
  escape, unreadable compression, insufficient padding, broken connector relationships, and
  desktop, tablet, phone, or zoom failures are release blockers. Keep a repeatable containment audit
  and rerun it after source-asset changes.
- After every three produced lessons and before release, run
  `python3 tools/course_distinctiveness.py --course apps/<course>`. Stop bulk production when the
  rendered lessons repeat archetypes, quiz sequences, interaction signatures, generic frequently
  asked questions, or factory-pattern control counts.
- Never use one large page generator that substitutes module content into fixed section, quiz, visual,
  FAQ, and artifact slots. Generators may create the accessible site shell. Lesson teaching and
  experience architecture must come from the approved module brief.
- A compiler may render governed block types, but it must preserve the authored storyboard sequence
  and reject unresolved assets, unknown components, missing approvals, unsupported completion IDs,
  and unreviewed release evidence. The compiler does not invent teaching.
- Run the full implementation gate against every completed full module:

  ```bash
  python3 tools/course_conformance.py \
    --lesson apps/<course>/curriculum/<module>.html \
    --qa apps/<course>/qa/<module>-quality-control-report.md \
    --brief apps/<course>/curriculum/design-briefs/<module>.md \
    --contract apps/<course>/.course/full-module-contract.json
  ```

  Add `--script` only when the approved course modality includes a recording. The gate must inspect
  the actual lesson, design brief, optional modality script, and scored QA report.
  Do not use `test-course-production-contract.py`, folder existence, generated scaffolding, or a
  minimum-floor test as evidence that a full module conforms. Do not report conformance unless this
  command passes. Do not convert an unperformed browser, mobile, accessibility, practitioner,
  learner, source, authentication, or release review into a pass.

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
- retain the structured source checksum, compiler version, storyboard approval, visual manifest, and
  rendered evidence used for each candidate;
- leave all changed artifacts readable in Git;
- record the exact full-module conformance command and result in `STATE.md`;
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
