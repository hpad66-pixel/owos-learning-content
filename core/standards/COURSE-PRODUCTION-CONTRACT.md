---
title: OWOS Course Production Contract
version: 1.0.0
status: APPROVED IMPLEMENTATION STANDARD
owner: Hardeep Anand
effective: 2026-07-23
---

# OWOS Course Production Contract

This is the binding build and quality contract for every OWOS course, Master Class, module, chapter, and lesson. It consolidates the decisions accumulated through the Project Delivery, Data Before AI, and What Is an AI Agent course builds. Other standards provide depth. This file defines the minimum complete result.

## 1. Repository and evidence foundation

- The curriculum source lives in `owos-learning-content`. Runtime copies never become the curriculum source of truth.
- Preserve every original source, checksum, locator, permission state, author, visibility, and limitation.
- Separate sourced fact, expert interpretation, Hardeep Anand position, instructional scenario, and unresolved question.
- Load Hardeep Soul when Hardeep's knowledge is used. The Soul file controls voice and boundaries, not factual evidence.
- Record substantive user direction in `conversations/`, then update course state and approvals.
- No private, internal, sealed, or permission-pending material becomes public without approval.

## 2. Syllabus and blueprint gate

Before lesson production, the syllabus must define:

- the learner promise, intended roles, prerequisites, duration, level, and mastery standard;
- observable course and module outcomes;
- the complete module sequence and the reason for that sequence;
- utility situations, role-sensitive decisions, and professional consequences;
- the progressive work products, capstone, competencies, assessment plan, and completion evidence;
- the concept, source, contributor, competency, and course relationships proposed for the Knowledge Graph;
- the evidence boundary and permission status for every module; and
- one course overview recording script that follows the approved sequence.

Complete a course design matrix and one module design brief per module. Bulk production begins only after a golden lesson is approved as a capability benchmark.

## 3. Complete lesson experience

Every full lesson must provide:

1. A consequential utility situation and an initial learner decision.
2. Plain-English instructor teaching that stands on its own without video.
3. One clear mental model and at least four relevant visual types. At least three must be lesson-specific explanatory graphics with genuinely different natural shapes.
4. At least two purposeful interactions or simulations.
5. Foundation, Practitioner, and Leader perspectives when roles change the decision.
6. At least three different quiz types, distributed beside the ideas they assess.
7. Immediate explanatory feedback, retry, and a final applied check.
8. A professional work product the learner can use after the course.
9. A source map, evidence boundary, release state, and limitations.
10. Deterministic completion evidence and a transition to the next lesson.
11. A complete instructor recording script with visual directions separated from spoken words.

A short lesson may request a documented exception. Counts never excuse irrelevant components or weak teaching.

## 4. Instructor voice and explanation

- Write as an experienced instructor speaking to one intelligent utility professional who is new to the topic.
- Explain every technical term in ordinary language and define every acronym on first use.
- Connect every abstraction to water, wastewater, stormwater, a utility role, an asset, a record, or a real decision.
- Before each major visual, animation, simulation, assessment, and builder, explain what the learner sees, what to do, what to notice, why it matters, and what the result means.
- Add a debrief when the consequence or change is not self-evident.
- Use tooltips for definitions. A tooltip never replaces instruction.
- Do not use em dashes, en dashes, corporate filler, unsupported claims, cryptic fragments, or generic artificial-intelligence prose.

## 5. Graphics, interaction, and pacing

- Select graphics through the Visual Arsenal according to the natural shape of the idea.
- A renamed component does not count as a new visual. Every counted graphic must declare and render a structural shape or family that matches the teaching idea.
- Every full lesson must use at least three different explanatory shapes. Four are preferred. Adjacent lessons must not reuse the same dominant shape or the same ordered visual sequence.
- Use question flip cards when prediction, misconception repair, terminology, or retrieval practice benefits from them. The front asks a real question. The back teaches the answer and utility consequence. A decorative card grid does not count.
- Graphics must explain a concept, method, framework, relationship, sequence, comparison, quantity, location, or cause.
- Every graphic needs accessible text, a plain-English reading guide, a learner conclusion, and a mobile transformation.
- Animation must reveal change, cause, consequence, sequence, dependency, or hidden structure.
- Every animation needs a reduced-motion equivalent that preserves the meaning.
- Do not place more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout.
- Do not repeat adjacent modules' opening pattern, dominant visual, interaction pair, quiz sequence, and work-product format without an instructional reason.
- Course QA must compare rendered DOM fingerprints, visual-shape sequences, and quiz sequences across lessons. Different labels on the same markup are repetition and fail the diversity gate.
- Decorative stock art, generic technology imagery, repeated icon grids, and motion without a teaching purpose do not count.

## 6. Course navigation and connected learning

- Keep the main lesson reading surface calm and uncluttered.
- Place compact Graph, Community, and Start actions in the lesson header. Start moves directly to the beginning of the lesson. Do not use floating cards, hanging rails, or a persistent bottom dock.
- Open the Graph and Community in white, right-side drawers on larger screens and full-screen drawers on small screens.
- Closing a drawer must return focus and the learner to the same place in the course.
- Keep the complete graph and community section at the bottom of the lesson for discovery, context, and extended use.
- Every course and lesson HTML file must reserve an explicit `#owos-course-community` anchor inside `main`, immediately before bottom course navigation. Runtime code must never choose a generic `.wrap` as the connected-learning mount.
- The Graph must open the current course or lesson context without navigating away.
- The Community must support search, filters, bookmarks, threaded replies, member presence, and distinct instructor treatment.
- Previous, next, all modules, progress, and completion behavior must remain predictable across the course.
- End every module with a visible FAQ before the evidence boundary and bottom connected-learning section. Questions must anticipate the module's likely novice misunderstandings. Answers must teach in conversational plain English and use a utility example, diagram, comparison, or worked sequence when that improves understanding.
- FAQ controls must use semantic disclosure behavior, work with keyboard and touch, and remain readable on mobile. A generic FAQ repeated across modules is not acceptable.

## 7. Visual and accessibility contract

- New public course and lesson surfaces use the OWOS Graphite Visual Standard by default. Graphite
  controls brand identity, not the learning composition. Course and module experience plans still
  determine the narrative shape, visuals, interactions, and surface rhythm.
- Use the OWOS typeface, spacing, color tokens, component geometry, and responsive breakpoints.
- Every dark blue, navy, or gradient surface must use white or tested light text. Black or dark gray text on a dark surface is a release blocker.
- Verify contrast at runtime for dynamic content and during desktop and mobile visual review.
- All controls must work with keyboard, touch, and visible focus.
- Use semantic headings, labels, live feedback regions, descriptive alternative text, and logical focus order.
- No learner-facing value may render as `undefined`, empty placeholder content, or a broken component.

## 8. Deterministic learning and records

The default completion rule is:

```text
required teaching sections viewed
+ required interaction completed
+ required knowledge check passed
+ required work product saved
= lesson complete
```

- Scoring rules, accepted responses, feedback, retry, and completion requirements must be explicit and testable.
- Scrolling alone never means completion.
- Browser state is a convenience cache. Supabase is the learner-record authority after consent and authentication.
- Stable course, lesson, competency, graph, assessment, and event identifiers are required.
- Credentials and certification claims stay disabled until their separate evidence and approval gates pass.

## 9. Quality assurance and release

After every material module revision:

1. Complete `core/templates/MODULE-QA-REPORT.md`.
2. Score instructor teaching, learning design, graphics, interaction, utility credibility, assessment, work product, evidence, accessibility, and platform integration.
3. Run mechanical tests for lesson structure, JavaScript, undefined values, deterministic assessment, distributed quizzes, instructor explanation, module-specific FAQ coverage, visual pacing, contrast, responsive behavior, reduced motion, and prohibited language.
4. Perform desktop, mobile, keyboard, screen-reader, reduced-motion, novice-learner, and utility-practitioner reviews.
5. Keep accuracy, learning design, utility practice, technical quality, and release control as hard gates.

A high score cannot override a blocked gate. A release identifies the exact source commit, manifest, checksums, runtime intake, deployment, and approval.

When `quality_contract.require_rendered_browser_qa` is true, release also requires a current
`owos-rendered-course-qa/v1` receipt whose source digest matches the lesson HTML, visual system, and
interaction runtime. The receipt must cover desktop and phone views for every lesson, verify final
learner-visible component states after animation, operate required quizzes and work products, check
keyboard and reduced-motion behavior, and record zero unresolved failures. Counting classes, data
attributes, files, or declared component names is not rendered quality assurance.

Before a multi-module course is released, create and inspect course-level contact sheets or an
equivalent all-module visual comparison. A module-by-module screenshot pass must block repeated hero
composition, dark visual slabs, clipped text, stale runtime assets, and variety created only through
color changes.

Before creating or checking the checksum manifest, run the course-specific runtime packaging command.
The release gate must compare lesson visual-shape sequences, quiz sequences, interaction runtime, and
visual-system assets between curriculum source and packaged `dist/site`. A new manifest that merely
checksums stale runtime files fails release.

## 10. Definition of done

A course is complete only when:

- the approved syllabus, design matrix, module briefs, scripts, work products, evidence registers, and QA reports exist;
- every lesson meets this contract and the machine-enforced quality floor;
- all modules form a coherent sequence without unnecessary repetition;
- the live runtime matches the governed source release;
- Graph and Community work on the same page and remain available at the bottom;
- every module includes a module-specific, plain-English FAQ with useful examples and visual explanation where appropriate;
- contrast and responsive behavior pass on representative devices;
- Hardeep has approved the release scope; and
- GitHub and production deployment identify the same version and source commit.
