---
title: OWOS Quality Control Certificate Standard
version: 1.0.0
contract: owos-qaqc-certificate/1
status: APPROVED FOR IMPLEMENTATION
owner: Hardeep Anand
approved: 2026-07-27
---

# OWOS Quality Control Certificate Standard

## Why this exists

A published document is a claim about quality. Without a record of what was checked, by what method,
and what was found, that claim rests on the author's word. This standard replaces the author's word
with evidence.

Every OWOS document that reaches a live site ships with a Quality Control Certificate. The
certificate is not a summary written after the fact. It is the record of the checks, including the
ones that failed and what was done about them.

## The rule

**No document publishes without a certificate at the same version, in the same repository, in the
same commit.**

A certificate that arrives later is not a certificate. It is a reconstruction.

## Naming and location

The certificate lives beside the document it certifies:

```text
<document-directory>/QA-QC-CERTIFICATE.md          the current version
<document-directory>/qa-qc/QA-QC-<version>.md      every superseded version, retained
```

The certificate's `document_version` must equal the version of the artifact published. If the
document changes in any way that reaches a reader, the version increments and a new certificate is
written. There is no such thing as an uncertified correction, including a correction to a single
graphic.

## Required sections

A certificate is incomplete unless every section below is present and answered. "Not applicable" is
an acceptable answer only with a stated reason.

### 1. Identification

Document identifier, title, version, artifact checksum, published URL, commit hash, certificate
version, reviewer, date, and the version this supersedes.

### 2. Graphics

Every graphic listed individually. For each one:

- what it claims to show;
- whether it remains true with its caption removed;
- whether it contradicts anything in the governing white paper or source dossier;
- whether every physical relationship it draws is consistent with the governing mechanism, not
  merely plausible in shape;
- whether it displays any quantity that could be mistaken for a design value;
- whether it states what it does not prove;
- alternative text, reduced-motion, and no-JavaScript behaviour; and
- defects found and their disposition.

A graphic that has not been individually assessed is a graphic that has not been checked.

### 3. Analysis and physics

Every quantitative relationship, curve, model, animation, or calculated readout the document
presents. For each one: the governing relationship, the check performed, the numeric result, and
whether the presented behaviour satisfies the physics rather than only looking correct.

This section exists because a graphic can be legible, accessible, well captioned, and wrong. A curve
that violates the mechanism it illustrates will pass every other check in this document.

### 4. Factual accuracy

Every material claim, its classification, and its verification state. Numbers, thresholds, units,
and any quantity a reader could act on receive individual confirmation. Illustrative values are
confirmed as labelled illustrative.

### 5. Citations

Every source: full citation, issuing authority, exact retrieved URL, retrieval date, the specific
passage relied on, and an authority tier.

Authority tiers, highest first:

1. current United States federal statute or regulation;
2. current federal agency guidance on a live agency URL;
3. federal technical reference on a live agency URL;
4. peer-reviewed research within its stated scope; and
5. professional standards and practice references, clearly labelled as professional context.

**An archived or snapshot URL is not tier 1 through 3.** It is evidence that a document once existed
at an agency, not that the agency currently publishes it. A claim resting only on an archived copy
must be identified as such and either replaced with live authority, downgraded to what the live
record supports, or removed. This is a publication gate, not a footnote.

### 6. Editorial and instructional

Reading level, defined-before-use compliance, orientation completeness, scope boundary visibility,
and prohibited-phrase check.

### 7. Rendered quality

Output of `tools/audit-concept-brief-rendering.cjs` at desktop, tablet, and phone: contrast, gutter,
layout integrity, horizontal overflow, and touch targets. Plus keyboard, focus, reduced-motion, and
no-JavaScript results.

### 8. Defects found and disposition

Every defect discovered during the pass, whether it was corrected, and how it was verified after
correction. **A certificate reporting zero defects found is treated as an incomplete review unless
the pass is documented in enough detail to show what was actually examined.** Finding nothing is
possible. Finding nothing without saying what you looked at is not a review.

### 9. Open items and limitations

What remains unverified, what review is outstanding, and what a reader must not conclude from this
document.

### 10. Correction and version history

Every version, what changed, what triggered it, and which certificate covers it. Community-raised
corrections are recorded here with their outcome, including corrections that were examined and
rejected, with the reason.

## The correction cycle

When a reader raises an issue:

1. the issue is recorded against the exact sentence, graphic, or number;
2. it is checked against the governing sources;
3. if it holds, the document is corrected and its version increments;
4. a new certificate is written covering the change, and the previous certificate moves to `qa-qc/`;
5. both the corrected document and the new certificate publish in the same commit; and
6. the outcome is recorded in section 10 whether the correction was adopted or rejected.

A rejected correction is still recorded. The reasoning is part of the document's quality history.

## Enforcement

`tools/check_qaqc_certificate.py` verifies that a certificate exists, that its version matches the
document it certifies, that every required section is present, and that no citation relies on an
archived URL without being flagged. It runs before publication and its output is pasted into the
certificate.

A numeric result never overrides a missing section, a missing certificate, or an unflagged archived
citation.
