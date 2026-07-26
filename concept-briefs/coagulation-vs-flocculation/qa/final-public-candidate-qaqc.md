---
brief_id: owos:concept-brief:001
brief_version: 0.2.0-research-working
compiler_version: owos-concept-brief-compiler/1
release_status: blocked
review_date: 2026-07-26
---

# Integrated Public Candidate Quality Report

## Revised score

The score separates product quality from release authority.

| Dimension | Weight | Score | Weighted contribution | Evidence and unresolved work |
| --- | ---: | ---: | ---: | --- |
| Teaching and editorial quality | 20 | 96 | 19.20 | Clear mental model, strong sequence, role relevance, FAQ, clean public copy, and one bounded tangible action. Independent editorial and novice-reader reviews remain. |
| Research discovery and source mapping | 15 | 97 | 14.55 | Four research clusters completed, United States source hierarchy applied, public sources linked, and all supplied originals preserved with matching checksums. |
| Claim verification and technical confidence | 25 | 55 | 13.75 | Direct authority checks and safe public wording are complete. Independent verification, qualified practitioner review, jurisdiction review, freshness records, and formal claim acceptance remain incomplete. |
| Visual design and interaction | 15 | 96 | 14.40 | Graphite direction is owner-approved. The qualitative jar, treatment train, related-learning surface, Community handoff, and SOP outline are visually coherent and testable. |
| Accessibility and responsive behavior | 15 | 90 | 13.50 | Desktop, tablet, phone, keyboard focus, focus return, reduced motion, no JavaScript, live feedback, alternative text, and containment pass. Manual touch, screen-reader, zoom, and device review remain. |
| Connected product implementation | 10 | 94 | 9.40 | Library navigation, curated related learning, Community context, SOP outline, governed commercial registry, administrator controls, directory linkage, and vendor reporting are built. Platform deployment, moderation ownership, real-vendor review, and release approval remain. |
| **Governed package score** | **100** |  | **84.80** | The cross-repository system is complete as a review candidate. Human release gates remain open. |

- Public learning-experience score: **96 out of 100**.
- Governed package score: **85 out of 100**.
- Release-readiness score: **66 out of 100**.
- Formal material-claim verification coverage: **0 percent**.
- Release decision: **blocked**.

The score rose because the previously empty implementation layers now exist and pass automated
checks. It does not rise to release because implementation cannot substitute for independent
technical, editorial, accessibility, moderation, commercial-conflict, and owner review.

## What is now built

- The Graphite public Concept Brief remains the primary learning experience.
- `All briefs` connects to the new Graphite Concept Brief library.
- `Related learning` opens a white right-side drawer and has a full bottom section.
- Raw node identifiers, edge types, and internal Graph machinery remain private.
- `Discuss` opens a bounded Community drawer with seed questions, privacy guidance, and focus return.
- The Community link carries the brief, version, topics, and discussion-space context into the
  existing OWOS Community route.
- `SOP outline` explains the public-to-private product boundary and opens a concise eight-section
  SOP outline.
- `Copy the outline` gives the reader one tangible action: paste the structure into the utility's
  approved workspace. The public page collects and stores no facility information.
- A full facility-specific SOP builder is reserved for a separate authenticated agent product with
  controlled inputs, evidence, reviewers, versions, and approvals.
- A public APAS house block and visibly non-live vendor placeholder are built into the compiled
  candidate without entering the lesson or evidence sequence.
- The existing OWOS commercial registry now controls logo, copy, link, disclosure, placement kind,
  Concept Brief targeting, vendor directory key, vendor account assignment, dates, pause, resume,
  and soft archive.
- `/console#sponsors` is the administrator control surface; `/sponsor-dashboard` gives an assigned
  vendor aggregate impression, click, and contact-start reporting without editorial controls.
- All three supplied originals are preserved inside the governed package with matching SHA-256
  checksums.
- `integration.yaml` records what is implemented, what remains private, and what still requires a
  runtime or owner decision.

## Verification coverage

- Material claims in the governed package: 36.
- Release-verified claims: 0.
- Verification coverage: 0 percent.
- Regulatory claims with completed independent jurisdiction and effective-date review: 0.
- Technical claims with qualified reviewer approval: 0.
- Unresolved, pending, or rejected material claims: 36.

Perplexity was used for source discovery. It did not independently verify the claims. The public
candidate withholds rejected, experimental, overbroad, and facility-ready material, but the package
cannot claim 100 percent accuracy until every material claim completes the required verifier,
qualified-reviewer, and freshness records.

## Hard gates

| Gate | Status | Evidence | Missing work |
| --- | --- | --- | --- |
| Source preservation | Passed | Original HTML, strategy handoff, and visual-reference deck are preserved with matching checksums. | None for the current intake set. |
| Claim verification and accuracy | Blocked | Research discovery and direct United States source checks are complete. | Independent trace, exact accepted locators, verifier names, review dates, freshness dates, and 100 percent coverage. |
| Learning and editorial design | Provisional pass | Public-output regression, clean-reading audit, visual review, and prohibited-language checks pass. | Independent editorial and novice-reader reviews. |
| Utility or technical practice | Blocked | Universal settings and operating advice are withheld. | Qualified United States drinking-water practitioner approval. |
| Visual, interaction, accessibility, and responsive quality | Blocked | Automated desktop, tablet, phone, keyboard, drawer, focus-return, reduced-motion, no-JavaScript, outline-copy, and containment checks pass. | Manual touch, screen-reader, 200 and 400 percent zoom, and device review. |
| Graph and Community integrity | Blocked from publication | Curated related learning, Community boundary, context handoff, and correction path are built. | Graph review, moderation owner, Community accessibility review, platform acceptance, and owner approval. |
| Commercial integrity | Provisional pass, not released | Owner approved the controlled APAS and placeholder implementation. Compiler and platform checks enforce explicit labeling, no editorial rights, independence attestation, neutral ranking, aggregate-only reporting, and soft archive. | Real-vendor conflict review, logo authorization, terms, privacy/legal review, production deployment, and final owner review. |
| Release control | Blocked | Integrated candidate, library, checksums, and QA evidence exist. | All required approvals and release-ready validation. |

## Automated and rendered checks

| Check | Result |
| --- | --- |
| Package validation | Passed as a working package. |
| Deterministic compiler regression | Passed. |
| Public-output gate | Passed. |
| Research integration regression | Passed. |
| Portfolio distinctiveness | Passed for the current one-brief portfolio. |
| United States public-source allowlist | Passed. |
| Internal research-language exclusion | Passed. |
| Desktop 1440 by 1000 | Passed, no page overflow or JavaScript errors. |
| Tablet 820 by 1180 | Passed, no page overflow or JavaScript errors. |
| Phone 390 by 844 | Passed after the mobile title correction. |
| Qualitative jar | Passed state change, live explanation, and animated/static behavior. |
| Reduced motion | Passed, canvas remains static and scrolling is automatic. |
| Keyboard | Passed visible focus and drawer focus return. |
| Related-learning drawer | Passed open, close, Escape, and focus return. |
| SOP drawer and outline copy | Passed with the complete eight-section outline and announced result. |
| No JavaScript | Passed model boundary, text equivalent, and containment. |
| Commercial block at desktop, tablet, and phone | Passed containment, legibility, disclosure, APAS house labeling, placeholder labeling, and evidence separation. |
| Release-ready validation | Failed closed as required. |

Rendered evidence is retained in `dist/browser-qa/`.

## Manual reviews

- [ ] Independent source review
- [ ] Qualified technical or practitioner review
- [ ] Independent editorial review
- [x] Desktop visual review
- [ ] Tablet human visual review
- [x] Phone visual review
- [x] Keyboard behavior review
- [ ] Touch review on a physical device
- [ ] Screen-reader review
- [x] Reduced-motion automated and visual-equivalent review
- [x] No-JavaScript meaning review
- [x] Read-without-animation review
- [ ] Novice-reader review
- [ ] Graph relationship review
- [ ] Community moderation and accessibility review
- [ ] Commercial-conflict and legal review
- [ ] Owner approval of the exact release checksum

## Approval boundary

| Decision | State |
| --- | --- |
| Graphite visual direction | Approved by Hardeep Anand. |
| Integrated working implementation | Built and mechanically checked. |
| Technical accuracy | Pending qualified United States drinking-water reviewer. |
| Graph publication | Pending explicit approval. |
| Community release | Pending moderation, accessibility, platform, and owner approval. |
| Commercial placement | Candidate build approved by Hardeep Anand on July 26, 2026; real-vendor, legal, conflict, deployment, and release reviews remain. |
| Public release | Blocked until release-ready validation passes and Hardeep approves the exact build. |
