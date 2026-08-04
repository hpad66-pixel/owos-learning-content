# One Water AI Authoring Workspace

## Download set

- Complete inclusive curriculum HTML: `output/html/one-water-ai-applied-intelligence-curriculum.html`
- Complete inclusive curriculum PDF: `output/pdf/one-water-ai-applied-intelligence-curriculum.pdf`
- Complete HTML program book: `output/html/one-water-ai-executive-fellowship-program-book.html`
- Complete PDF program book: `output/pdf/one-water-ai-executive-fellowship-program-book.pdf`
- Master curriculum PDF: `output/pdf/one-water-ai-executive-fellowship-master-curriculum.pdf`
- Fieldbook PDF: `output/pdf/one-water-ai-fieldbook-working-edition.pdf`
- Complete ZIP package: `output/package/one-water-ai-executive-fellowship-document-package.zip`

**One Water AI: The Applied Intelligence Curriculum for the Water Sector** is the inclusive umbrella
curriculum. It provides one shared foundation and seven role-based tracks for the full water-sector
audience. **One Water AI Executive Fellowship** remains a premium cohort and delivery option within
that broader curriculum. The original 686-page Master Class compilation is a preserved legacy source
library. It is not overwritten by either current product.

Rebuild and verify the complete inclusive curriculum with:

```bash
python3 tools/build_applied_intelligence_curriculum.py
python3 tools/build_applied_intelligence_curriculum.py --check
```

The inclusive curriculum uses the approved black, warm ivory, and gold document system. Its cover
and interactive reader belong to the same family as the One Water AI Fieldbook. The contents and
long-form lesson pages use cream reading surfaces for legibility and practical printing.

This is the governed source workspace for the One Water OS AI Master Class series.

It is not a public course page and it is not an Articulate export. It is the place where research,
Hardeep's direction, instructional design, evidence, source files, Articulate-ready manuscripts,
and quality records remain connected and version controlled.

Open `index.html` for the staff-facing visual map of how a module moves from value proposition and
Perplexity-assisted source discovery to verified claims, a complete Markdown manuscript, graphic
directions, Articulate production, QA, and release.

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

For every new module, begin with
`research/MODULE-RESEARCH-AND-VISUAL-BRIEF-TEMPLATE.md`. The completed copy becomes the module's
`MODULE-MANUSCRIPT.md`. Perplexity may discover and compare source leads. The original source, not
the Perplexity response, supports the claim.

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
