# OWOS Course Production Bible

Version: 1.0.0  
Status: Review candidate, not yet pushed  
Owner: Hardeep Anand  
Companion: `core/standards/OWOS-COURSE-PRODUCTION-BIBLE.html`

## Purpose

This is the topic-neutral operating guide for creating a new One Water OS course, continuing an
approved course, retrofitting an existing course, or completing a course-level quality and release
audit.

It explains:

- where Hardeep begins;
- what Codex does at every phase;
- what evidence must exist before the next phase;
- what Hardeep reviews or approves;
- when Author Studio enters;
- what prompts to use;
- how module count is determined;
- how structured source becomes delivery HTML;
- how module and course scores are supported;
- how Git, platform intake, deployment, and live verification work.

## Running example

The examples use this hypothetical utility-industry topic:

> Preventing Lift Station Failures: A Utility Reliability Master Class

The example begins as a rough idea. It is not assumed to be a course, and no module count is chosen
in advance.

## Where to start

Start in the conversational Codex workspace.

Do not start in Author Studio. Do not begin by writing HTML. Do not decide that the course has 8,
12, or 18 modules.

Author Studio begins after:

1. research is organized;
2. the Course Brief is approved;
3. the syllabus and curriculum are approved;
4. the course experience architecture exists;
5. lesson contracts are validated; and
6. at least one structured module candidate exists.

## Complete production route

```text
Topic sparring
  -> research and evidence
  -> course formulation
  -> syllabus and curriculum
  -> experience architecture
  -> lesson contracts
  -> golden lesson
  -> structured module production
  -> Author Studio review
  -> deterministic compilation
  -> module QA and scoring
  -> course assembly and landing page
  -> course dossier
  -> Git publication
  -> platform intake
  -> production deployment
  -> custom-domain and live verification
```

## Phase 0: Topic sparring and intake

### Where

Codex conversational workspace.

### Hardeep brings

- the topic or question;
- research, articles, PDFs, notes, diagrams, and voice direction;
- the intended audience, if known;
- what people misunderstand;
- utility examples;
- personal positions or thought leadership;
- business or operational outcomes;
- boundaries and concerns.

### Running example

> I want utility leaders and operations staff to understand why lift stations fail, how maintenance,
> telemetry, work history, wet-well conditions, power quality, and operator knowledge fit together,
> and how to build a reliability program without pretending artificial intelligence predicts every
> failure.

### Prompt

```text
I want to explore a possible OWOS course about [TOPIC].

My current point of view is:
[POINT OF VIEW]

The people I think need it are:
[LEARNERS]

The utility problems or examples I care about are:
[EXAMPLES]

The research and notes I have are:
[FILES, LINKS, NOTES, OR CONVERSATION]

Spar with me. Challenge the topic, identify what is genuinely teachable, separate fact from my
position, expose missing questions, and help me decide whether this should become a course. Do not
select a module count or generate lessons yet.
```

### Exit evidence

- dated conversation record;
- topic-intake brief;
- candidate learner;
- candidate problem and promise;
- research plan;
- unresolved-question register;
- recommendation to continue, narrow, combine, or stop.

### Gate

Hardeep agrees that the topic is worth formal research and formulation.

## Phase 1: Research and evidence

### Where

Codex workspace and the course research folders.

### Codex does

- preserves originals and checksums;
- extracts complete source text with locators;
- distinguishes sourced fact, expert interpretation, Hardeep position, example, teaching direction,
  and unresolved claim;
- searches primary sources when current or external verification is required;
- records permissions and evidence boundaries;
- identifies contradictions and missing coverage.

### Running example

Research may include maintenance records, alarm histories, pump curves, operator interviews,
manufacturer manuals, reliability standards, cybersecurity restrictions, and overflow-response
procedures.

### Prompt

```text
Organize and evaluate all research for the proposed course.

Preserve every original and checksum. Build a source register, claims register, evidence-boundary
register, research-coverage map, and unresolved-question list.

For every important statement, identify whether it is:
- sourced fact;
- expert interpretation;
- my position;
- utility example;
- teaching direction; or
- unresolved.

Use primary sources for claims that carry technical, legal, safety, financial, regulatory, or
operational weight. Do not draft the curriculum until the evidence coverage and limitations are
visible.
```

### Exit evidence

- source register;
- claims register;
- evidence boundaries;
- extraction coverage;
- permissions;
- contradiction log;
- unresolved questions.

### Gate

The evidence is adequate for course formulation, or limitations are explicitly accepted.

## Phase 2: Course formulation

### Where

Codex workspace.

### Questions answered

- Who is the learner?
- What do they already know?
- What should they be able to do after the course?
- What decisions should change?
- What should they produce?
- What does the course refuse to claim?
- Is the course written-first, video-supported, or another approved modality?

### Running example

Graduation capability:

> Given one lift-station reliability problem, the learner can frame the failure question, identify
> the evidence needed, distinguish symptoms from causes, choose monitoring and maintenance controls,
> assign accountable owners, and define when a recommendation requires engineering or operational
> approval.

### Prompt

```text
Formulate the course from the research.

Define:
- primary and secondary learners;
- prerequisite knowledge;
- course promise;
- graduation capability;
- measurable outcomes;
- common, practitioner, and leader depth;
- work-product progression;
- assessment strategy;
- modality;
- evidence and safety boundaries;
- relationship to other OWOS courses.

Do not create modules yet. First prove that the proposed graduation capability is useful,
assessable, and supported by the evidence.
```

### Exit evidence

- approved Course Brief;
- learner definition;
- course promise;
- graduation capability;
- outcomes;
- depth and modality model;
- boundaries.

### Gate

Hardeep approves the Course Brief and graduation capability.

## Phase 3: Syllabus and curriculum architecture

### Where

Codex workspace.

### Method

Work backward from graduation:

1. What must the learner do at the end?
2. What must they understand immediately before that?
3. What prerequisites support that understanding?
4. What must come first?
5. Which learning jobs deserve separate modules?
6. Which ideas belong together?
7. Where is practice required?
8. Where is synthesis required?

The module count emerges from the learning jobs.

### Running example

A possible sequence might begin with:

1. What failure means operationally.
2. Asset identity and system boundaries.
3. Failure modes and causal evidence.
4. Telemetry, alarms, and missing context.
5. Work history and operator observations.
6. Reliability decisions and maintenance strategies.
7. Governance, authority, and action boundaries.
8. A bounded lift-station reliability pilot.

This is only an example. Research may produce a different count or order.

### Prompt

```text
Design the syllabus and curriculum from the approved graduation capability.

Determine explicitly:
- what must come first;
- what comes second and why;
- what comes third and why;
- the prerequisite chain thereafter;
- where recognition becomes practice;
- where practice becomes professional transfer;
- where synthesis and capstone work belong.

Let the required learning jobs determine the number of modules. Reject overloaded modules,
unnecessary repetition, missing prerequisites, and arbitrary module counts.

For every proposed module, provide:
- title;
- learner question;
- one learning job;
- prerequisite;
- outcome;
- misconception;
- transfer task;
- work product;
- relationship to adjacent modules.

Also produce the syllabus, curriculum sequence review, dependency map, work-product progression,
assessment progression, and course design matrix.
```

### Exit evidence

- syllabus;
- curriculum sequence;
- dependency map;
- module inventory;
- work-product progression;
- assessment progression;
- course design matrix.

### Gate

Hardeep approves the curriculum and module count.

## Phase 4: Course experience architecture

### Where

Codex workspace.

### Decisions

- teaching voice;
- utility world and recurring cases;
- visual grammar;
- interaction philosophy;
- artifact family;
- pacing;
- accessibility;
- prohibited motifs;
- how the course differs from other OWOS courses.

### Running example

The lift-station course might use a reliability investigation fieldbook, evidence boards,
degradation timelines, failure trees, maintenance decision rooms, and operating envelopes. It should
not reuse the semantic-graph visual language of Meaning Before Models.

### Prompt

```text
Create the course experience architecture.

Define the teaching voice, utility world, recurring cases, visual language, signature mechanisms,
interaction rhythm, assessment rhythm, artifact family, accessibility treatments, and prohibited
motifs.

Compare this proposed experience with existing OWOS courses. Prevent shared quality standards from
creating a shared appearance. Produce the Course Experience Brief and update the Course Design
Matrix.
```

### Exit evidence

- Course Experience Brief;
- visual and interaction language;
- artifact family;
- prohibited patterns;
- distinctiveness baseline.

### Gate

Hardeep accepts the course experience direction.

## Phase 5: Lesson contracts

### Where

Codex workspace and `apps/<course>/modules/<module>/lesson-contract.yaml`.

### Prompt

```text
Create and validate one lesson contract for every approved curriculum module.

Each contract must lock:
- module identity and curriculum role;
- learner question;
- one learning job;
- prior knowledge;
- misconception;
- transfer task;
- common, practitioner, and leader depth;
- archetype;
- opening;
- mental model;
- signature mechanism;
- visual jobs;
- assessment jobs;
- professional work product;
- source and claim references;
- evidence boundary;
- prerequisite and preparation relationships.

Audit the complete contract set for missing prerequisites, duplicate jobs, overloaded lessons, and
weak transitions. Do not begin bulk production until the contract gate passes.
```

### Exit evidence

- one contract per module;
- validated contract report;
- adjacency audit.

### Gate

Contracts pass and the golden-lesson candidate can be selected.

## Phase 6: Golden lesson

### Where

Codex first. Author Studio after the structured candidate exists.

### Prompt

```text
Select the golden lesson that best tests the course's hardest teaching, visual, interaction,
assessment, and professional-transfer requirements.

Create its design brief, Visual Arsenal selection, storyboard, structured source, real visual
assets, simulations, assessments, professional work product, FAQ, evidence boundary, and QA plan.

Compile and test it on desktop, tablet, and phone. Complete its evidence-backed Module
Quality-Control Report. Present the rendered lesson and evidence for approval.

Treat approval as a capability and quality benchmark. Do not turn its page composition into a
template for the remaining modules.
```

### Exit evidence

- complete structured module;
- compiled preview;
- rendered screenshots;
- browser results;
- score and hard gates;
- approval or revision decision.

### Gate

Hardeep approves the golden lesson as the production benchmark.

## Phase 7: Structured module production

### Where

Codex produces. Author Studio reviews.

### Required package

```text
modules/<module>/
  lesson-contract.yaml
  design-brief.md
  module.yaml
  storyboard.yaml
  visuals/
    visual-manifest.yaml
    real assets
  interactions.yaml
  assessments.yaml
  sources.yaml
  glossary.yaml
  qa.yaml
  build/index.html
```

### Prompt

```text
Produce the next approved module or batch in prerequisite order.

For every module:
- preserve its unique contract and design brief;
- run the Visual Arsenal selection;
- author complete conversational written teaching;
- create real, lesson-specific graphics;
- create the subject-specific signature mechanism;
- select assessments from the cognitive jobs;
- create the professional work product;
- add module-specific FAQs;
- preserve source and evidence boundaries;
- validate structured source;
- compile deterministic HTML;
- compare it with adjacent modules for repetition;
- run rendered and behavioral QA;
- complete the module scorecard.

Do not stop at scaffolding or source generation. Do not hand-edit delivery HTML.
```

## Phase 8: Author Studio

### Where it is

Hardeep opens the permanent studio inside One Water OS:

```text
https://owos.ai/capture#studio?tab=courses
```

This is the production Author Studio. It works without a local server, terminal command, or
repository navigation. The Content Desk is a separate downstream publishing-approval queue; it is
not the course-authoring workspace.

Module 18 currently opens from the Courses tab at:

```text
https://owos.ai/lesson-author-module-18.html
```

### When it is used

Use Author Studio after a structured module candidate exists. It is not used for initial topic
sparring, research, course formulation, or deciding the curriculum.

### Views

- Design brief
- Narrative
- Storyboard
- Visuals
- Interactions
- Assessments
- Sources
- Glossary
- QA
- Compiled preview

Every save creates a prior-source snapshot under the module `.history/` folder.

### Prompts to give Codex before opening Author Studio

```text
Open One Water OS Author Studio for [COURSE] and [MODULE], navigate me to Courses, and tell me which
views require review. Use the permanent production route, never localhost. Do not change approved
source merely to make the page look different.
```

```text
Prepare [MODULE] for Author Studio review. Summarize the learning job, storyboard, visual jobs,
interactions, assessment sequence, work product, evidence boundary, current score, and unresolved
gates before I inspect it.
```

### Directions inside Author Studio

Author Studio edits structured files, so instructions should name the view and intended learning
change.

Good Narrative prompt:

```text
In the Narrative view, rewrite the explanation of cavitation for a nontechnical utility supervisor.
Keep the approved claim boundary, add one wastewater example, and do not change the storyboard.
```

Good Storyboard prompt:

```text
In the Storyboard view, move the failure-tree simulation immediately after the causal explanation.
Preserve completion IDs and explain why the new sequence improves learning.
```

Good Visuals prompt:

```text
In the Visuals view, replace the generic comparison graphic with a pump-degradation timeline.
Preserve the teaching idea, reading guide, learner conclusion, alternative text, source, license,
mobile treatment, and reduced-motion treatment.
```

Good Interactions prompt:

```text
In the Interactions view, change the scenario from a generic asset to Lift Station 7. Preserve the
decision states, immediate feedback, retry, keyboard behavior, and completion contract.
```

Good Assessments prompt:

```text
In the Assessments view, replace the second multiple-choice check with an ordering task because the
learner must sequence the escalation process. Keep explanatory feedback and retry.
```

Good Sources prompt:

```text
In the Sources view, add the approved manufacturer manual reference to the cavitation claim. Do not
promote the operator interview from interpretation to independent fact.
```

Good QA prompt:

```text
In the QA view, record the completed visual review and link the screenshot evidence. Keep
screen-reader and practitioner review pending because they have not been performed.
```

### After Author Studio changes

```text
Validate the saved structured package, rebuild the preview, compare the source checksum, rerun the
affected module tests, and show me exactly what changed. Do not publish yet.
```

## Phase 9: Visual, interaction, and assessment QA

### Prompt

```text
Run the complete module QA suite.

Verify:
- every visual resolves to a real asset or governed component;
- SVG text stays inside intended boxes;
- text does not clip, overlap, or become unreadable;
- connectors preserve their relationships;
- desktop, tablet, phone, zoom, touch, keyboard, focus return, and reduced motion;
- no dark-text contrast failures;
- no horizontal overflow;
- no empty controls;
- simulations and assessments complete correctly;
- immediate feedback and retry;
- work-product completion;
- Graph, Community, Start, drawers, and bottom connected learning;
- no console or page errors;
- source and evidence boundaries;
- distinctiveness from adjacent lessons.

Save screenshots and results. Complete the Module Quality-Control Report with a score out of 100 and
five hard gates. Do not convert an unperformed human review into a pass.
```

## Phase 10: Course landing page

### Prompt

```text
Build the course-specific landing page from the approved curriculum and experience architecture.

Show:
- course promise;
- intended learner;
- graduation capability;
- learning route;
- course parts;
- module sequence and prerequisites;
- expected work products;
- duration or effort when evidence supports it;
- current release state;
- where to begin.

Give the landing page its own visual identity. Test typography, hierarchy, line length, spacing,
links, navigation, drawers, desktop, tablet, phone, zoom, contrast, and overflow. Do not use a
generic course catalog layout.
```

## Phase 11: Course Quality-Control Dossier

### Prompt

```text
Complete the Course Quality-Control Dossier.

Include:
- score out of 100;
- evidence supporting every score;
- module score register;
- curriculum and contract evidence;
- structured-source inventory and checksums;
- visual containment results;
- rendered screenshots;
- browser and accessibility results;
- distinctiveness and coherence;
- source and claims status;
- defect and correction ledger;
- human-review register;
- hard release gates;
- release manifest;
- Git and deployment proof when published.

A numeric score cannot override a blocked factual, practitioner, accessibility, technical,
security, credential, or release gate.
```

## Phase 12: Git, platform, and production

### Prompt

```text
Publish the approved course end to end.

Run all source, compiler, module, course, distinctiveness, visual, accessibility, release, and
formatting gates. Commit intentional source and reproducible output. Push GitHub. Import the exact
learning-content commit into the OWOS platform. Run platform registry, navigation, release, and
build tests. Push the exact production commit. Deploy it. Verify custom-domain files byte for byte.
Run the live desktop, tablet, and phone browser suite.

Do not stop between approved publication, Git push, platform intake, deployment, and live
verification. Do not claim publication until the custom domain is verified.
```

## Generic master build prompt

```text
Activate the complete OWOS Course Production System for the topic and research developed in this
conversation.

Treat this as a new governed course unless the repository already contains an approved course
folder. Do not assume a module count, syllabus, curriculum sequence, delivery format, visual style,
or page structure.

Begin by preserving this conversation and all supplied research. Determine the current phase from
repository evidence.

Execute:
1. topic sparring and intake;
2. research and evidence organization;
3. course formulation;
4. syllabus and curriculum architecture;
5. course experience architecture;
6. lesson contracts;
7. golden lesson selection, production, testing, scoring, and approval;
8. structured module production in prerequisite order;
9. Author Studio-compatible review;
10. deterministic compilation;
11. module-level rendered QA and evidence-backed scoring;
12. course coherence and distinctiveness review;
13. course-specific landing-page production;
14. Course Quality-Control Dossier;
15. Git publication, platform intake, production deployment, custom-domain verification, and live
    browser QA when publication is authorized.

For the curriculum, determine what the learner must understand first, second, third, and
thereafter. Let learning jobs and prerequisites determine the module count.

Give every module its own contract, design brief, storyboard, narrative structure, opening, visual
reasoning, signature mechanism, simulation strategy, assessment rhythm, professional work product,
FAQ, and evidence boundary.

Apply one common quality standard without producing one common appearance. Prevent repeated
openings, visual shapes, interaction pairs, quiz sequences, work-product formats, FAQs, and factory
prose.

Use structured source. Treat HTML as compiled delivery output. Use Author Studio after curriculum
architecture and structured module candidates exist.

Require complete conversational teaching that works without video. Define terms, spell out
acronyms, explain every visual and interaction, use concrete utility examples, and preserve source,
authority, time, uncertainty, and permission boundaries.

Count only real visual assets and governed executable components. Render and measure every graphic.
Text clipping, overlap, escape from boxes, unreadable compression, insufficient padding, broken
connectors, contrast failures, and desktop, tablet, phone, zoom, or reduced-motion failures are
release blockers.

Select interactions and assessments from the cognitive job. Require immediate feedback, retry,
distributed checks, an applied demonstration, and a professional work product.

Complete an evidence-backed Module Quality-Control Report for every module and a Course
Quality-Control Dossier for the course. A score cannot override blocked factual, practitioner,
accessibility, technical, security, credential, or release gates.

Do not report publication until the exact source commit is imported, platform tests pass,
production deployment completes, custom-domain files match, and live desktop, tablet, and phone
tests pass.

Before each major phase, report:
- completed work;
- available evidence;
- unresolved decisions;
- required approval;
- next-phase output.

Do not ask me to operate internal scripts. Preserve all substantive direction and evidence in the
repository.
```

## Review status

These Bible files are review candidates. They must not be pushed to GitHub until Hardeep reviews and
approves them.
