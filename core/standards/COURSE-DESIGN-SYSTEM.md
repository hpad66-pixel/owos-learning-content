---
title: OWOS Course Design System
version: 1.0.0
status: APPROVED IMPLEMENTATION STANDARD
owner: Hardeep Anand
effective: 2026-07-22
---

# OWOS Course Design System

## Purpose

This is the durable design instruction for every future OWOS course, module, chapter, and lesson. It connects the approved hybrid course model to the visual arsenal, interaction library, quiz library, animation rules, Hardeep Soul, quality contract, and release process.

The golden lesson is a capability benchmark. It is not a visual mold. Future lessons must achieve the same level of teaching, evidence, interaction, accessibility, and usefulness without copying its page composition.

## What the hybrid model preserves

| Source | What OWOS preserves | What OWOS does not copy blindly |
| --- | --- | --- |
| Project Delivery Master Class | Human teaching, consequential utility situations, simulations, applied decisions, professional work products, strong pacing, and learner involvement | Its subject matter, exact layouts, or repeated visual motifs |
| Data Before AI | Controlled evidence, method versions, claims boundaries, stable identifiers, deterministic scoring, manifests, and honest release states | Dense or static presentation when the idea needs a simulation |
| Data Before AI Chapter 09 | Decision-first opening, multiple professional viewpoints, authority simulation, relationship map, operating-pack builder, deterministic checks, lesson graph, completion evidence, accessibility, and responsive behavior | Chapter 09 colors, Riverbend facts, component order, or screen composition |
| Hardeep Soul | Hardeep's natural voice, distinctions, utility grounding, argument quality, attribution, and approval boundaries | Unsupported factual claims or private material without permission |
| One Water Operating System | Identity, learner state, same-page graph context, competencies, community, work products, credentials, and release controls | Runtime data as editable curriculum source |

## Canonical design sources

Read these files before designing a module:

1. `core/standards/COURSE-OPERATING-STANDARD.md`
2. `core/standards/COURSE-DESIGN-SYSTEM.md`
3. `core/standards/VISUAL-ARSENAL.md`
4. `core/standards/WRITING-STANDARD.md`
5. `core/components/COMPONENTS.md`
6. `core/components/QUIZ-TYPES.md`
7. `core/components/component-gallery.html`
8. `core/components/quiz-gallery.html`
9. `core/components/module-template.html`
10. `core/brand/BRAND-GUIDELINES.md`

When Hardeep's knowledge is used, also read `hardeep-soul/SOUL.md` and `hardeep-soul/authoring/AUTHORING_STANDARD.md` from the canonical sibling repository.

## Design sequence for every module

### 1. Establish the learning job

Write the learner decision, professional consequence, intended roles, controlled claims, source boundaries, competency, work product, and completion evidence before selecting a visual.

### 2. Map every teaching idea to its natural shape

For each material idea, identify whether it is primarily a process, system, relationship, cause-and-effect chain, trade-off, change over time, comparison, hierarchy, quantity flow, status problem, or spatial problem.

Run the Selection Prompt in `VISUAL-ARSENAL.md`. Do not select visuals because they are convenient or were used in the previous lesson.

### 3. Create a module design fingerprint

Before authoring HTML, complete `core/templates/MODULE-DESIGN-BRIEF.md`. The fingerprint must name:

- the opening situation and first learner decision;
- the narrative structure and mental model;
- at least four varied visual types, unless a documented exception is approved;
- at least two purposeful interactions that reveal cause, consequence, sequence, or trade-off;
- at least three quiz types, with no type repeated consecutively;
- the professional work product and same-page Knowledge Graph behavior;
- the animation purpose and reduced-motion equivalent;
- the mobile transformation; and
- the design elements intentionally not repeated from adjacent modules.

### 4. Check diversity across the course

Update `core/templates/COURSE-DESIGN-MATRIX.md` as modules are planned. Adjacent modules must not use the same opening pattern, dominant visual, interaction pair, quiz sequence, and work-product format.

A different title or color does not make a different learning experience. The learner action and teaching structure must change.

### 5. Build from governed components

Copy proven markup, styles, and behavior from the component and quiz galleries. Adapt content and data, not accessibility away.

If the idea needs a component that does not exist:

1. build the new component in the shared library;
2. document when it should and should not be used;
3. provide keyboard, touch, mobile, reduced-motion, and live-feedback behavior;
4. add a rendered gallery example;
5. add a regression test; and
6. only then use it in the course.

Do not hand-roll a weaker version inside one lesson.

### 6. Make animation instructional

Every animation must show change, cause, consequence, sequence, dependency, or a meaningful reveal. Decorative movement does not count. Every animated explanation requires a reduced-motion equivalent that preserves the meaning.

### 7. Make the learner produce something useful

Every substantive lesson should create or improve a professional artifact such as a decision record, responsibility map, risk register, evidence plan, operating brief, implementation roadmap, calculation, policy draft, or review checklist. The work product must be useful beyond course completion.

### 8. Validate the complete experience

Validation includes factual and citation review, utility-practice review, deterministic scoring, malformed-data checks, desktop and mobile rendering, keyboard and touch operation, screen-reader labels, reduced-motion behavior, contrast, typography, same-page graph behavior, persistence, completion evidence, and comparison against adjacent lessons for repetition.

### 9. Teach the interface in the interface

A learner must never meet an unexplained animation, simulation, diagram, assessment, or builder. Before each major component, include one or two instructor paragraphs that answer five questions:

1. What am I seeing?
2. What should I do?
3. What should I notice?
4. Why does this matter in utility work?
5. What does the result mean?

Add a short debrief after a mechanism when the meaning of the change may not be obvious. Tooltips define terms, but they do not carry the lesson.

### 10. Prepare the instructor recording package

Every module must have a spoken-language recording script before production is complete. Every course must maintain one overview script that explains all lessons in order. Scripts must separate visual directions from spoken words, explain technical terms in ordinary language, include a utility example, name the learner action and work product, and close with a transition to the next lesson.

### 11. Use graphics to explain, not decorate

An explanatory graphic has a specific teaching job. It may reveal the parts of a concept, the steps of a method, the relationships in a framework, the path of evidence, the cause of a failure, a change over time, or a comparison that prose alone makes hard to see.

For every proposed graphic, record:

1. the idea and its visual shape;
2. the selected Visual Arsenal pattern;
3. the sentence the learner should be able to say after reading it;
4. the instructor explanation that tells the learner how to read it;
5. the accessible text and mobile transformation; and
6. the reduced-motion equivalent when movement carries meaning.

Reject a graphic when it is decorative, repeats the heading, uses generic stock imagery, creates visual noise, or has no conclusion the learner can explain. A module does not pass by placing icons around existing prose.

## Required diversity contract

The default minimum for each full module is:

- four different visual types;
- two purposeful interactions or simulations;
- three different quiz types;
- one consequential opening decision;
- one role-sensitive perspective when roles change the decision;
- one professional work product;
- one same-page Knowledge Graph experience;
- one explicit evidence boundary; and
- one deterministic completion rule.

These numbers are a floor, not a formula. A short lesson may request a documented exception. A long lesson may need more. Meeting the count with irrelevant components fails the standard.

## Variation patterns

Use different narrative and interaction architectures across a course. Examples include:

- decision room, authority simulation, and operating-pack builder;
- field incident, root-cause investigation, and corrective-action plan;
- control-room timeline, threshold model, and escalation decision;
- map-based exploration, option comparison, and capital brief;
- before-and-after diagnosis, identity-resolution simulation, and stewardship record;
- role-based case conference, evidence challenge, and peer-review package;
- data journey, provenance network, and quality-by-use builder; and
- scenario branching, consequence model, and executive recommendation.

Do not turn these examples into eight new templates. Select the architecture from the learning problem.

## Chapter 09 capability benchmark

Chapter 09 demonstrates the required level through a consequential Riverbend decision, a five-voice decision-room handoff, an accountability relationship map, an authority simulator, a segregation-of-duties exercise, an operating-pack builder, deterministic checks, a same-page graph drawer, stateful completion, responsive layouts, and reduced-motion support.

A future lesson should be equally complete while using the components and structure best suited to its own learning problem.

## Failure conditions

A module fails design review when it clones Chapter 09 or the prior module, relies on prose where a mechanism should be simulated, uses decorative visuals, repeats one interaction shape, repeats quizzes consecutively, uses meaningless animation, offers an unstructured work product, navigates away for graph access, fails mobile transformation, claims completion from scrolling, or creates variety only through colors and icons.

## Definition of design readiness

HTML production may begin only when the module design brief, course design matrix, evidence boundaries, and work-product specification are reviewable. Bulk production may begin only after Hardeep approves the golden lesson as a capability benchmark.
