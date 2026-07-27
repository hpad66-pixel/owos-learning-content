---
title: OWOS Concept Brief Production Contract
version: 2.2.0
contract: owos-concept-brief/2
status: APPROVED FOR IMPLEMENTATION
owner: Hardeep Anand
approved: 2026-07-25
revised: 2026-07-27
---

# OWOS Concept Brief Production Contract

## Purpose

A Concept Brief is the governed explanation between a Dictionary definition and a complete course.
It helps a person understand how a concept works, where it applies, what can fail, what evidence
supports it, and what to do next.

The Concept Engine is the authoring, verification, compilation, connection, correction, and release
system that produces Concept Briefs.

This contract is separate from `owos-course-compiler/1`. Concept Briefs may share OWOS identity,
components, Graph behavior, Community behavior, evidence controls, and accessibility rules with
courses. They do not inherit a course page layout or silently change the course compiler.

## Accepted source types

An intake may begin with one or more of:

- a diagram or image;
- a concept or question;
- an article;
- a technical brief;
- a regulation, standard, study, or guidance document;
- a procedure or standard operating procedure;
- a conversation or field explanation;
- an existing web page or HTML prototype; or
- a mixed source package.

The source is evidence and direction. It is not automatically a published Concept Brief.

### Shared public presentation shell

Public Concept Briefs use the compiler-enforced Graphite shell proven by the Coagulation vs
Flocculation reference. The shell locks the desktop and phone gutter rhythm, section-band
hierarchy, readable prose measure, dark instructional and Connected Learning surfaces, ivory
Community-through-feedback closing plane, light connected-learning drawers, and accessible
responsive stacking. These are shared trust and navigation conventions, not a license to clone the
reference's treatment-train narrative, visuals, interactions, or topic-specific page composition.
Any exception requires an explicit design-brief decision, rendered comparison, and owner approval.

### United States water-sector authority scope

Water, wastewater, stormwater, and One Water Concept Briefs use United States governing authorities
only. The public evidence hierarchy is:

1. current United States federal statute and regulation;
2. current federal agency guidance tied to that authority;
3. United States professional standards and practice references, including AWWA material when
   clearly labeled as professional context rather than federal authority; and
4. peer-reviewed research presented within its actual scope.

Non-United States regulations, standards, government guidance, design guides, operator guides, and
health guidelines are excluded from governing evidence, benchmark comparisons, learner-facing
context, Graph evidence, and reviewer approval. Research conducted outside the United States may be
used only as research, never as a governing standard, and must expose its experimental conditions,
geographic context, and transfer limitations.

State requirements are also excluded from public Concept Brief authority statements, claims,
citations, comparisons, and Graph evidence. A public Concept Brief explains the federal and EPA
frame; it does not attempt to assemble state-by-state compliance guidance. A separate private,
jurisdiction-specific work product may address state requirements only under its own approved
scope, current source review, and qualified legal or regulatory review.

## Lifecycle

Every Concept Brief moves through visible states:

```text
intake
-> source preservation
-> owner sparring and curriculum thesis
-> research white paper
-> white-paper quality review and owner approval
-> extraction and claim inventory
-> research and verification
-> evidence boundary
-> design fingerprint
-> storyboard approval
-> structured authoring
-> deterministic compilation
-> factual and technical review
-> rendered and accessibility review
-> Graph and Community validation
-> commercial-integrity review
-> owner approval
-> release
-> monitored corrections and freshness review
```

No stage may claim completion before its evidence exists.

## Required package

The governed source package contains:

- `intake.yaml`
- `brief.yaml`
- `white-paper.md`
- `design-brief.md`
- `storyboard.yaml`
- `narrative.yaml`
- `learning.yaml`
- `assessments.yaml`
- `claims.yaml`
- `sources.yaml`
- `visuals/visual-manifest.yaml`
- `interactions.yaml`
- `graph.yaml`
- `community.yaml`
- `commercial.yaml`
- `qa.yaml`
- `approvals.yaml`

Compiled HTML is delivery output. The structured package is the source of truth.

## Curriculum thesis and white-paper gate

A Concept Brief starts as teaching, not page production. Before design or learner-facing HTML, the
owner and author spar over the topic until the curriculum thesis is explicit.

The sparring record must answer:

- What exactly are we teaching?
- Why does this concept matter?
- Who needs to understand it?
- What should the learner understand, notice, explain, compare, or do differently?
- Which common misunderstandings or false shortcuts must be repaired?
- Which practical water-sector situations make the concept consequential?
- How deep should the explanation go?
- What belongs outside the brief?
- Which citation and editorial standard governs the white paper?

The first generated teaching artifact is `white-paper.md`. It is revised after each sparring round
and becomes the basis for research, claim extraction, verification, scoring, curriculum design,
storyboarding, visuals, interactions, and later HTML.

The white paper must contain:

- a clear title and executive teaching thesis;
- the curriculum purpose, learner need, and importance of the concept;
- a reader orientation that names the subject, the audience, the assumed prior knowledge, the
  consequence of not understanding the concept, the learner-facing outcomes, the time required, and
  the scope boundary, before the topic itself begins;
- an explicit answer to what the concept is, who needs it, where and when it appears in water-sector
  work, why it matters, and how it works;
- a complete plain-language explanation of what the concept is and how it works;
- headings and subheadings that form a coherent argument;
- plain-English definitions of every dependent term, each with a concrete example and an explicit
  statement of what the term does not establish;
- distinctions, mechanisms, boundaries, practical consequences, misconceptions, and examples;
- at least one worked example per major mechanism, showing inputs, reasoning, result, and transfer
  boundary;
- proposed diagrams and graphics with an instructional job and reading explanation;
- source notes, limitations, unresolved questions, and a complete reference list;
- a section explaining what should be taught, in what order, and why; and
- a scored quality review that separates writing quality, research depth, claim confidence,
  teaching completeness, visual-explanation readiness, and unresolved work.

The white paper and the compiled brief are the same argument at two depths. The paper carries the
full reasoning and evidence; the brief carries the learner's path through it. A teaching move that
exists in the paper but has no home in the storyboard, or a rendered section with no basis in the
paper, is a synchronization defect and is reported in the QA record.

The white paper is not a page mockup, a storyboard, or a collection of cards. It uses a calm,
empty-format reading surface with controlled line length and generous margins. No learner-facing
HTML, interaction, graphic production, or storyboard approval may begin until Hardeep approves the
teaching thesis and white-paper direction. A prior prototype must be frozen as a pre-research draft
and cannot supply evidence or curriculum authority.

### White-paper scoring gate

Every substantive sparring or research round updates a visible 100-point score inside
`white-paper.md`. The score uses this fixed rubric:

| Dimension | Points |
| --- | ---: |
| Teaching thesis and importance | 15 |
| Complete plain-language explanation | 20 |
| Utility-wide and cross-sector value | 15 |
| Research depth and source quality | 15 |
| Technical accuracy and claim verification | 20 |
| Diagrams and visual teaching value | 10 |
| Editorial quality, boundaries, and originality | 5 |
| **Total** | **100** |

Each scoring update must show:

- the score awarded in every dimension;
- the evidence supporting the awarded points;
- every deduction and the reason for it;
- unresolved questions and required next work;
- the score change from the prior version; and
- the current advancement decision.

The decision bands are:

- 90 to 100: eligible for owner approval into curriculum design;
- 80 to 89: strong, but revision is required;
- 70 to 79: material teaching or evidence gaps remain; and
- below 70: return to sparring and research.

The paper cannot advance regardless of score unless:

- every material technical claim has a source and claim classification;
- terminology and system boundaries are internally consistent;
- technical content has qualified practitioner review;
- every proposed diagram has an instructional job, evidence basis, and truth boundary;
- scope exclusions remain visible; and
- Hardeep approves the teaching argument.

Use `core/templates/CONCEPT-BRIEF-WHITE-PAPER-SCORE.md`. A polished outline with no research receives
no research or verification points.

## Shared learning capabilities

Concept Briefs and courses select visuals, interactions, animations, and assessment types from the
single registry at `core/learning-capabilities/registry.yaml`. The registry points to the canonical
Visual Arsenal, component catalog and gallery, and quiz catalog and gallery. A package records only
the stable capability identifier and topic-specific configuration. It must not fork or copy a
shared capability definition.

The standard internal names are **OWOS Concept Engine** and **OWOS Course Engine**. Their renderers
are the **OWOS Concept Brief Compiler** and **OWOS Course Compiler**.

A Concept Brief is one focused learning module. It requires a rendered instructional orientation,
plain-English definitions of its dependent terms placed before first use, at least two substantial
explanatory visuals, at least one worked example, one dynamic concept mechanism, two distributed
checks, one final applied check, deterministic completion evidence, and an explicit cross-sector
connection. Motion must reveal change, cause, consequence, sequence, dependency, or hidden
structure. Reduced-motion, no-JavaScript, mobile, and structured-text equivalents must preserve the
same conclusion.

The package may store continuing-education readiness evidence. No contact-hour, professional-
development-hour, continuing-education-unit, or accreditor claim may be enabled without verification
of the named accreditor's current rules and explicit approval of the exact offering.

Every Concept Brief also implements
`core/standards/OWOS-LEARNING-RECORD-CREDENTIAL-AND-PATHWAY-STANDARD.md`. Its `learning.yaml`
must bind to the shared xAPI event profile, cmi5 launch preference, SCORM 2004 compatibility
adapter, portable-credential targets, fail-closed credit profile, and explainable deepen, reskill,
and cross-skill recommendation lanes. These are shared system contracts, not Concept Brief-only
copies.

Every `learning.yaml` also preserves six migration-sensitive contracts:

1. **Placement**: prerequisites, remediation, next learning, and exact course or pathway use.
2. **Capability lock**: registry identifier, registry version, selected capability identifiers, and
   compatibility policy.
3. **Learning events and privacy**: stable event namespace, attempt and completion events, record
   authority, privacy classification and review, consent boundary, retention rule, supersession and
   material-correction notification, and a prohibition on facility-sensitive information unless a
   separately governed workflow requires it.
4. **Assessment governance**: item-level versions, passing rule, retry policy, explanatory feedback,
   accommodations, and assessment review state.
5. **Simulation assurance**: model version, visible assumptions, illustrative-value labeling,
   deterministic replay, and qualified review requirements.
6. **Language, units, and time**: primary language, reading target, unit policy, localization state,
   instructional minutes, active-participation minutes, assessment minutes, and timing method.
7. **Credential readiness**: event, launch, adapter, portable credential, learner-record export,
   accreditor profile, credit-claim, and certificate state.
8. **Learning pathways**: recommendation policy; deepen, reskill, and cross-skill lanes;
   explainability; learner control; and prohibited-data controls.

These records allow the learning system, future accreditor package, analytics, corrections, and
superseding releases to identify the exact experience completed without storing unsafe operational
data.

## Source preservation

Every intake item records:

- a stable source identifier;
- source type and title;
- original locator;
- preserved snapshot locator when available;
- SHA-256 checksum for a preserved file;
- creator or issuing authority;
- capture date;
- visibility;
- permission and license state;
- extraction coverage;
- limitations; and
- disposition.

A release is blocked when a material supplied source has no preserved snapshot or approved durable
locator.

## Claim and fact verification

The system cannot promise that knowledge will never change or that a qualified source cannot contain
an error. It can require complete verification coverage and honest uncertainty.

Every material statement must be classified as one of:

- `sourced_fact`
- `regulatory_requirement`
- `technical_standard`
- `expert_interpretation`
- `hardeep_position`
- `instructional_scenario`
- `commercial_claim`
- `unresolved_question`

Every material claim records:

- exact claim text;
- scope and jurisdiction where applicable;
- claim type;
- evidence tier;
- source identifiers and exact locators;
- verification methods;
- verification status;
- author;
- independent verifier;
- qualified technical reviewer when the claim affects engineering, operations, safety, compliance,
  health, or the environment;
- verification date and next review date;
- limitations and uncertainty;
- affected narrative blocks, visuals, interactions, Graph statements, and work outputs; and
- correction history.

Release requires:

- 100 percent material-claim verification coverage;
- zero material claims in pending, rejected, or unresolved status;
- exact source locators;
- an independent source trace;
- qualified technical review for technical claims;
- jurisdiction and effective-date review for regulatory claims;
- separate labeling for interpretation, position, scenario, and commercial claims;
- no expired freshness date; and
- explicit accuracy approval.

One claim may remain contested only when the disagreement itself is accurately represented, each
material position is sourced, the boundary is visible, and the release approval explicitly accepts
the contested presentation.

External research services may help discover sources. They are not evidence authorities. Release
evidence must resolve to the original regulation, standard, paper, dataset, manufacturer document,
or other controlled source.

## Unique design

The compiler enforces a stable trust shell, not a fixed page recipe.

Every new public Concept Brief uses
`core/standards/OWOS-GRAPHITE-VISUAL-STANDARD.md` as its default visual identity. Graphite fixes the
palette, typography, contrast, depth, and accent semantics. It does not fix the opening pattern,
page composition, dominant visual, interaction, surface sequence, or closing action. A departure
requires a recorded design exception approved by Hardeep.

Every brief defines a design fingerprint:

- learner job;
- opening pattern;
- narrative archetype;
- central mental model;
- signature mechanism;
- dominant visual;
- interaction signature;
- role treatment;
- closing action;
- surface rhythm;
- intentionally avoided patterns; and
- differences from adjacent briefs.

The storyboard opens with the instructional orientation and defines its dependent terms before use.
Those two moves are mandatory and their position is fixed. Everything after them is selected and
ordered from the learning problem. The following are available coverage jobs, not mandatory
sections:

- concept anchors;
- why it matters;
- interactive or worked mechanism;
- plain-language terms;
- system fit and downstream consequences;
- corrections and contested claims;
- runnable protocol;
- do and do-not decisions;
- diagnostic;
- role applications;
- frequently asked questions;
- next action; and
- connected learning.

A brief must not force monument numbers, a protocol, a simulator, a quiz, or a commercial section
when the topic does not support it.

The portfolio check blocks identical full fingerprints and flags adjacent reuse of the same opening,
archetype, dominant visual, interaction signature, and closing action.

## Instructional orientation contract

A Concept Brief is one focused learning module, not a masterclass and not an encyclopedia entry. It
has one document to do the whole instructional job. Because there is no module sequence to carry the
setup, the brief must orient the learner inside itself before it teaches.

A brief may not open directly on its topic. Before the first mechanism, diagram, or interaction, the
rendered page must answer, in plain language and in this order:

1. **What is this about?** The subject named in ordinary words, not a definition the learner must
   already understand to parse.
2. **Who is this for?** The named audience and the prior knowledge assumed. A learner must be able
   to tell within seconds whether this brief is written for them.
3. **Why does it matter?** The consequence of not understanding the concept, stated in terms of real
   water-sector work, cost, risk, or public accountability. Not a claim that the topic is important.
4. **What will you be able to do?** The learning objectives, written as learner-facing outcomes in
   second person. These are the same outcomes recorded in `learning.yaml`. The learner sees the
   promise the package already makes internally.
5. **How long will this take, and what does it not cover?** The reading and participation estimate
   and the visible scope boundary.

This orientation is a rendered requirement, not a package-only record. `learning.yaml` already
carries `outcomes`, `prior_knowledge`, `misconception`, and `cross_sector_connections`. The compiler
renders them. A brief whose objectives exist only inside the package fails the learning and
editorial-design gate.

The "In 30 seconds" takeaway is a summary of the answer. It does not replace the orientation. A
learner who reads only the takeaway should understand the conclusion; a learner who reads the
orientation should understand why the conclusion is worth their time.

### Define before use

Every term the brief depends on is defined in plain English before the learner is asked to use it,
reason with it, or read it inside a graphic.

A definition block records:

- the term;
- a plain-English meaning that avoids the term itself and avoids other undefined terms;
- at least one concrete example a non-specialist can picture;
- what the term does **not** establish, where the term is commonly over-read; and
- the claim identifiers supporting the definition where it is technical.

A glossary appended at the end does not satisfy this requirement. Definitions are placed where the
learner first needs them. A diagram may not introduce a labeled term that the prose has not already
defined.

### Show the concept, do not only assert it

Explanation carries an instructional job or it does not belong in the brief. Each substantive
teaching move must reach the learner through more than prose:

- a diagram, cutaway, flowchart, sequence, comparison, or other explanatory graphic;
- a worked example that moves from a concrete situation to a conclusion with the reasoning visible;
  or
- an interaction that lets the learner change something and observe the consequence.

Every graphic carries a caption stating what to notice and what the graphic does not prove. A
worked example states its inputs, its reasoning, its result, and its transfer boundary. Illustrative
values are labeled illustrative wherever they appear.

### Wholeness

A Concept Brief is complete when a learner who knew nothing about the topic can, without leaving the
page: say what the concept is, explain how it works, recognize where it applies, name what commonly
goes wrong, tell the difference between the concept and the things it is confused with, and state
what they would need to know before acting. A brief that requires an outside glossary, a prior
course, or a follow-up conversation to be understood is not finished.

## Learner economy and completion

A Concept Brief must feel complete without becoming an administrative dashboard, a full Community
page, or a facility procedure builder. The governed package may remain extensive; the public page
shows only what helps the learner understand and act.

Every public brief must:

- open with the instructional orientation defined above: subject, audience, why it matters,
  learner-facing objectives, time, and scope boundary;
- provide an “In 30 seconds” orientation near the beginning;
- define every dependent term in plain English, with an example, before the learner is asked to use
  it or read it in a graphic;
- limit primary in-page navigation to no more than four high-value controls;
- include compact Graph and Community controls in the top navigation; each opens a right-side drawer
  on larger screens and a full-screen drawer on small screens without navigating away;
- treat each drawer as a temporary layer over the brief: Close, Escape, backdrop selection, and
  browser Back remove it, restore the unchanged HTML brief, and return focus to its top control;
- allow only one Graph or Community drawer to be open at a time;
- keep claim counts, verification inventories, Graph machinery, and workflow metadata out of
  learner-facing promotional copy;
- use one compact same-page comment form and route the complete discussion experience to the
  existing Community drawer or dedicated Community route;
- place that comment form at the true end of the experience, after teaching and any active
  commercial placement, immediately before the footer;
- end with exactly three recap prompts: “What changed,” “What to observe,” and “What not to
  assume”;
- keep public SOP value to a useful outline or checklist unless a separate authenticated,
  governed agent has been approved to create facility-specific work;
- place APAS and active commercial connections after teaching, hide inactive vendor placeholders,
  and preserve the editorial-independence disclosure; and
- use the short plain-language disclaimer: “This brief explains the concept. Facility decisions
  still require your approved procedures and qualified judgment.”

These constraints are part of the reusable compiler contract, design brief, package validation,
QA report, and browser regression suite. They are not one-off edits to a compiled page.

## Storyboard gate

Before production implementation, the storyboard records each beat's:

- learner question;
- instructor purpose;
- content blocks;
- claims;
- visual or interaction;
- learner action;
- intended realization;
- transition;
- surface treatment; and
- mobile and reduced-motion behavior.

The owner approves the storyboard before a pilot can become a release candidate.

## Visual and interaction truth

Every counted visual resolves to a real asset or registered executable component. Every visual
records its teaching idea, learner conclusion, reading guide, alternative text, mobile treatment,
reduced-motion treatment, creator, source, license, permission, originality, storyboard state, and
rendered-review state.

Every interaction records its model boundary, inputs, outputs, failure states, keyboard behavior,
touch behavior, live feedback, mobile behavior, reduced-motion behavior, and completion evidence.

Illustrative values must be labeled as illustrative. A user-interface trigger must never resemble a
universal operating, regulatory, design, safety, or health threshold.

## Graph contract

The package may publish only declared, reviewed Graph relationships. Supported relationships include:

- `DEFINES`
- `EXPLAINS`
- `CITES`
- `CORRECTS`
- `CONTESTS`
- `CAUSES`
- `FAILS_DOWNSTREAM_IN`
- `ADJACENT_TO`
- `PREREQUISITE_FOR`
- `TEACHES_INTO`
- `ANSWERS`
- `APPLIES_TO_ROLE`
- `DEVELOPS_COMPETENCY`
- `GENERATES_WORK_PRODUCT`
- `CONTRIBUTED_TO`
- `REVIEWED_BY`
- `SPONSORED_BY`

Each edge records provenance, review state, visibility, and source claim where applicable.

`SPONSORED_BY` is never evidence. The compiler rejects a sponsored relationship used as a citation,
claim basis, evidence edge, or editorial approval.

Graph publication requires separate approval. A compiled preview is not a graph publication.

## Community contract

Every brief reserves a same-page `#owos-concept-community` mount.

The Community connection records:

- forum space identifier;
- brief and version context;
- seed questions;
- moderation owner;
- verified-answer policy;
- distinction between discussion and verified instruction;
- correction escalation path;
- abuse and conflict handling;
- accessibility behavior; and
- focus-return behavior for drawers.

Community discussion never silently edits verified instruction. A useful correction becomes a
tracked correction proposal and re-enters the verification lifecycle.

Positive learner feedback may become a public topic-specific testimonial only when the learner
explicitly consents to publication, a moderator approves the exact comment, and the learner can
request withdrawal. The public rendering may show only the approved comment text and the identity
fields covered by that consent. Testimonials remain learner-experience evidence. They are never
technical evidence, verified answers, vendor endorsements, or inputs to claim ranking.

The administrator must be able to see topic-level views, recent unique viewers, engaged reads,
completion reaches, comments, reviewed comments, consented appreciation, and featured testimonials.
Public analytics events must avoid facility-sensitive content and must follow the approved privacy,
retention, and consent boundary.

## Commercial integrity

Commercial participation is allowed through:

- verified directory relevance;
- attributed contribution;
- disclosed sponsorship; and
- private tenant briefs.

The package keeps contributor, reviewer, sponsor, advertiser, and evidence-source roles separate.

Public release is blocked when:

- a sponsor controls a claim, tier, source, correction, or review;
- a commercial relationship is unlabeled;
- a paid relationship is encoded as evidence;
- a sponsor can suppress a correction;
- a commercial claim lacks its own evidence and label; or
- a conflict of interest is missing.

## Rendered-quality gate

Structural validation cannot see the page. A package can satisfy every schema rule and still compile
to something unreadable, because contrast, gutters, overflow, and touch targets are properties of the
rendered result rather than of the record.

Every brief therefore passes an automated rendered audit at desktop, tablet, and phone widths before
it is offered for owner review:

- text meets WCAG 2.1 contrast against its real composited background: 4.5:1 for normal text and
  3:1 for large text;
- no text starts closer to the viewport edge than the page's own content inset;
- the document has no horizontal overflow at any width; and
- interactive controls are at least 24 by 24 pixels.

Run `node tools/audit-concept-brief-rendering.cjs <compiled.html>`. A non-zero exit blocks the
review. Findings are recorded in the QA report and the build manifest.

The accessibility floor is compiled after the package brand stylesheet and the shared shell, and it
uses literal colour values rather than theme variables. A package can define its own palette; it
cannot lower the floor, and it cannot lower the floor by accident by remapping a shared variable.

Components inherit their text colour from the card that contains them. A brief may use a light or a
dark variant of the same component, so a rule that forces one colour breaks the other.

## Quality gates

Every brief has these hard gates:

1. source preservation;
2. claim verification and accuracy;
3. learning and editorial design;
4. qualified utility or technical practice review;
5. visual, interaction, accessibility, and responsive quality;
6. Graph and Community integrity;
7. commercial integrity; and
8. release control.

A numeric score cannot override a blocked gate.

Required manual reviews include:

- independent source review;
- qualified technical or practitioner review;
- editorial review;
- desktop, tablet, and phone review;
- keyboard and touch review;
- screen-reader review;
- reduced-motion review;
- no-JavaScript and read-without-animation review;
- novice-reader review;
- Graph review;
- Community review;
- commercial-conflict review; and
- owner release approval.

## Deterministic compilation

The same approved structured package, compiler version, and runtime assets produce the same output.
The compiled output records:

- `owos-concept-brief/2`;
- compiler version;
- package checksum;
- brief identifier and version;
- evidence cutoff;
- release state; and
- build timestamp supplied by the release record, never an implicit current time.

The compiler does not research, invent instruction, approve a claim, choose a visual, or approve a
release.

## Correction and freshness lifecycle

Corrections retain the original claim, affected versions, correction reason, evidence, reviewer,
decision, and replacement.

A correction identifies every affected:

- brief release;
- narrative block;
- visual;
- interaction;
- Graph statement;
- course module;
- work product;
- saved learner assignment; and
- external distribution.

Expired claims block a new release. Previously released versions remain traceable and visibly
superseded when necessary.

## Definition of done

A Concept Brief is released only when:

- the complete package validates;
- the storyboard is approved;
- the design fingerprint passes the portfolio check;
- claim verification coverage is 100 percent;
- every hard gate passes;
- every required manual review is complete;
- the rendered experience matches the storyboard;
- Graph and Community connections pass;
- commercial relationships pass the editorial firewall;
- Hardeep approves the exact release;
- the release manifest identifies source and output checksums; and
- the OWOS runtime identifies the same version and source commit.
