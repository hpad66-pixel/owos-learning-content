# OWOS Concept Brief Authoring Guide

The complete placement, lifecycle, control-plane, publication-transaction, and current-state model is
defined in `docs/CONCEPT-BRIEF-OPERATING-MODEL.md`.

## What you give the system

You can begin with a diagram, concept, article, technical brief, procedure, standard operating
procedure, conversation, regulation, study, or existing HTML page.

You do not need to prepare the package or run the tools. Give Codex the material and explain what
you want people to understand, discuss, decide, or do.

## What happens next

The normal production order is fixed:

```text
supplied draft and conversation
-> preservation and claim inventory
-> owner sparring and curriculum thesis
-> research white paper and scored review
-> research and original-source verification
-> evidence-backed narrative and approved storyboard
-> cited HTML compilation
-> factual, technical, rendered, and accessibility QA
-> owner-approved publication
```

An existing HTML file may enter as the supplied draft. It does not justify generating a new
learner-facing HTML version before research. If a prototype has already been generated, preserve it
as a pre-research draft, return the brief to research, and do not treat that prototype as the
evidence-backed page.

Before claim inventory or page design, ask the owner focused questions in rounds. Establish what is
being taught, why it matters, who needs it, what should change for the learner, which misconceptions
matter, the desired depth, practical situations, exclusions, and the required citation standard.
Record the answers and keep revising `white-paper.md`.

`white-paper.md` is the first generated teaching artifact. It is a clean long-form explanation, not
a page mockup. It develops the complete argument with headings and subheadings, plain-language
definitions, mechanisms, importance, examples, misconceptions, limitations, proposed diagrams,
curriculum sequence, evidence notes, and references. Its scored review becomes the gate into claim
verification, design, storyboard, graphics, interactions, and HTML.

The paper opens by orienting a reader who knows nothing about the topic. Before the subject begins,
it names what the concept is, who needs it, where and when it shows up in water-sector work, why it
matters, what the reader will be able to do afterward, how long it takes, and what it does not
cover. Every dependent term is then defined in plain English with a concrete example and an explicit
statement of what the term does not establish. Each major mechanism carries a worked example that
shows inputs, reasoning, result, and transfer boundary.

The paper and the compiled brief are the same argument at two depths. Keep them synchronized. A
teaching move in the paper with no home in the storyboard, or a rendered section with no basis in
the paper, is a defect and belongs in the QA record.

After every substantive sparring or research round, update the 100-point score inside the white
paper. Score the teaching thesis, complete plain-language explanation, utility-wide and cross-sector
value, research and sources, technical verification, visual teaching value, and editorial quality.
Show every deduction and the work needed to recover it. A paper needs at least 90 points before it
may be offered for owner approval into curriculum design. Evidence, technical review, diagram truth,
scope, and owner approval remain hard gates regardless of the number.

### 1. Intake

The original is preserved with its locator, checksum, creator, visibility, permission, extraction
coverage, and limitations. The source is not treated as correct merely because it already exists.

An “existing” source must first pass a source-identity gate. Accept explicit matching title, stable
identifier, direct locator, documented package relationship, or owner confirmation. Do not activate
a source from keyword overlap, semantic similarity, search ranking, product adjacency, or patent
adjacency. Those are discovery leads only. When multiple plausible sources remain, stop before
claim extraction and obtain the exact locator. A rejected candidate stays outside the intake,
claims, terminology, design, Graph, Community, and release records.

### 2. Claim inventory

Every material statement is separated from the design:

- sourced fact;
- regulatory requirement;
- technical standard;
- expert interpretation;
- Hardeep position;
- instructional scenario;
- commercial claim; or
- unresolved question.

The system maps each claim to the exact narrative block, visual, interaction, Graph statement, and
future correction impact.

### 3. Research and verification

Research services may locate candidate evidence. The record must resolve to the original source.

For public water-sector briefs, governing sources are United States federal authority and EPA
guidance only. AWWA material may be used as clearly labeled professional context. Do not place state
requirements or non-United States regulations, standards, government guidance, design guides,
operator guides, or health guidelines in the public claim basis, Graph evidence, or learner content.
Research performed outside the United States may appear only as clearly bounded research and never
as a governing standard.

A material claim cannot pass release unless it has:

- an exact source locator;
- an independent source trace;
- scope and limitations;
- an independent verifier;
- a verification date and next review date;
- qualified technical review when the claim affects engineering, operations, safety, compliance,
  health, or the environment; and
- jurisdiction and effective-date review when it states a requirement.

Release requires 100 percent material-claim verification coverage. It does not claim that knowledge
can never change. Freshness and corrections remain active after release.

### 4. Evidence boundary

The package states what the source supports, what requires interpretation, what remains uncertain,
what is illustrative, and what the brief must not be used to decide.

### 5. Unique design fingerprint

Start with the OWOS Graphite Visual Standard. Use graphite and charcoal as the primary surfaces,
water blue for concepts and active states, amber for caution or consequence, green for favorable or
stable meaning, and red for critical states. This is the shared identity, not a reusable page
layout.

Before the page is written, each brief defines:

- the learner job;
- opening pattern;
- narrative archetype;
- central mental model;
- signature mechanism;
- dominant visual;
- interaction signature;
- role treatment;
- closing action;
- surface rhythm;
- avoided patterns; and
- differences from adjacent briefs.

This is how the system stays consistent in trust and different in experience.

The compiler enforces the shared Concept Brief shell proven by the Coagulation vs Flocculation
reference. That shell includes the 1160-pixel desktop wrapper, controlled prose measure, numbered
section-band hierarchy, dark instructional and Connected Learning surfaces, ivory Community,
commercial, recap, and feedback closing plane, light connected-learning drawers, and the responsive
gutter and stacking rules. A package may vary the learning composition, visuals, interactions, and
surface rhythm inside the instructional core. It may not silently replace the shared shell or
flatten the dark-to-ivory closing transition.

The compiler does not force monument numbers, a simulator, a protocol, a correction table, or a
diagnostic. It renders the approved storyboard in the order the learning problem requires.

### 6. Storyboard

Each beat records the learner question, instructor purpose, content, claims, visual or interaction,
learner action, intended realization, transition, surface, mobile treatment, and reduced-motion
treatment.

Implementation begins after storyboard approval.

### 7. Structured authoring and compilation

The author edits structured records rather than delivery HTML. The compiler validates the package,
resolves declared assets and connections, preserves the storyboard sequence, adds provenance and
release metadata, and produces a deterministic preview.

Working previews show unresolved verification. They cannot be mistaken for release-ready guidance.

The OWOS Concept Engine uses the same governed learning-capability registry as the OWOS Course
Engine. Select visual, interactive, animated, and quiz capabilities by stable identifier from
`core/learning-capabilities/registry.yaml`. Do not copy their definitions into a brief. Store the
topic-specific configuration, teaching explanation, evidence boundary, and review in the package.

A full brief is one focused learning module. Its `learning.yaml` and `assessments.yaml` records
define outcomes, cross-sector transfer, dynamic explanation, distributed checks, applied transfer,
completion evidence, and continuing-education readiness. Credit claims remain disabled until the
named accreditor approves the exact offering.

### Learner-facing editorial pass

Before compilation, separate internal rigor from public usefulness:

- open with the instructional orientation: what this is about, who it is for, why it matters, what
  the learner will be able to do, how long it takes, and what it does not cover;
- render the learning objectives on the page. They already exist in `learning.yaml`; the learner
  must see the promise the package makes;
- define every dependent term in plain English, with an example and a statement of what the term
  does not establish, before the learner meets it in a graphic;
- give every major mechanism a worked example and every graphic a caption saying what to notice and
  what it does not prove;
- provide an “In 30 seconds” orientation;
- keep primary navigation to four controls or fewer;
- include top Graph and Community controls that open same-screen right-side drawers;
- make Close, Escape, backdrop selection, and browser Back remove the active drawer, restore the
  unchanged brief, and return focus to the control that opened it;
- remove claim counts and raw governance or Graph machinery from promotional copy;
- keep public SOP value to a useful outline unless a separate authenticated agent is approved;
- show only active commercial connections after the teaching;
- end with “What changed,” “What to observe,” and “What not to assume”;
- place one compact comment form at the true end, immediately before the footer; and
- send deeper discussion to the existing Community drawer or route.

These decisions live in `learning.yaml`, the public preview configuration, the design brief, and QA.
Do not hand-edit them only into the compiled HTML.

### 8. Graph and Community

The package declares exact Graph nodes and relationships. It also reserves the same-page Community
mount and carries the brief identifier and version into the forum context.

Community discussion remains discussion. A proposed correction becomes a tracked item and re-enters
source and technical review before it changes verified instruction.

Positive feedback can add visible community value without becoming an ungoverned marketing quote.
The learner may submit “What worked for me” and separately consent to publication of the exact
comment with the named identity fields. An OWOS learning steward must approve it before the runtime
shows it in the brief's reader-voices section. The steward can remove it from the page without
deleting its Community and moderation history. The label must state that it is learner experience,
not technical evidence or a vendor endorsement.

The protected administrator view reports views, recent unique viewers, engaged reads, completion
reaches, comments, reviewed comments, consented appreciations, and featured testimonials for each
brief. These events must not contain facility-sensitive operating information.

### 9. Commercial participation

Commercial relationships are represented separately from evidence and editorial authority.

The system supports:

- verified directory relevance;
- attributed contribution;
- disclosed sponsorship; and
- private tenant briefs for internal methods and standard operating procedures.

A sponsor cannot approve a claim, choose an evidence tier, suppress a source, remove a correction,
or act as evidence merely because it paid.

### 10. Quality and release

The release gate checks:

- source preservation;
- claim verification and accuracy;
- learning and editorial design;
- qualified utility or technical practice;
- visual, interaction, accessibility, and responsive quality;
- Graph and Community integrity;
- commercial integrity; and
- release control.

Required manual reviews include independent source, qualified practitioner, editorial, desktop,
tablet, phone, keyboard, touch, screen reader, reduced motion, no JavaScript, read without
animation, novice reader, Graph, Community, commercial conflict, and owner release review.

No numeric score overrides a blocked gate.

## Commands used internally

```bash
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief>
python3 tools/concept_brief_compiler.py build concept-briefs/<brief> \
  --output concept-briefs/<brief>/dist/preview.html
python3 tools/concept_brief_compiler.py portfolio-check concept-briefs
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief> --release-ready
```

The final release manifest is created only after release-ready validation passes.
