# Module 18 Remaining Human-Review Package

Module: Graph-Grounded Agentic Applications  
Course: Meaning Before Models  
Approved Phase 14 checksum:
`3e22f25705f3c3efaab6e6ed53c703b72dfd8fdbdada357724b31dc724bb8e8e`  
Owner approval: Hardeep Anand, 2026-07-25  
Release status: blocked pending completed human evidence

## Immutable-candidate rule

Every reviewer must inspect the candidate carrying the checksum above. If the checksum changes,
Codex must identify which reviews are affected and reroute those lanes. A name without completed
evidence, a review of another checksum, or an automated result cannot pass a human gate.

Review location:

- Author Studio: `https://owos.ai/capture#studio?tab=courses`
- Direct working candidate: `https://owos.ai/lesson-author-module-18.html`
- Phase 13 evidence: `../module-18-phase-13-deterministic-qa-report.md`
- Quality-control scorecard:
  `../module-18-graph-grounded-agentic-applications-quality-control-report.md`

## Severity and decision vocabulary

| Value | Meaning |
| --- | --- |
| Release blocker | Incorrect, unsafe, inaccessible, misleading, unusable, or inconsistent enough to prevent release |
| Important correction | Material improvement required; reviewer states whether it blocks release |
| Optional improvement | Useful enhancement that does not block release |
| Approve | No blocking finding |
| Approve with notes | Only explicitly nonblocking findings remain |
| Block | One or more release blockers remain |

## Required lanes

### 1. Utility practitioner realism

Reviewer qualification: current or recent wastewater operations, maintenance, work management,
engineering, governance, or supervisory responsibility.

Confirm:

- LS-7, overflow, inspection, work-order, escalation, stale-evidence, and approval behavior are
  recognizable and responsibly bounded.
- Operator, supervisor, maintenance, cybersecurity, and governance responsibilities are not
  misleading.
- Stop, ask, refresh, reconcile, retry, verify, and audit outcomes are operationally credible.
- The Agent Action Contract could support a real cross-functional design review.

### 2. Novice-learner comprehension

Reviewer qualification: intelligent utility professional who has not previously worked with
graph-grounded agents.

Observe without coaching:

- Can the learner explain why a grounded answer does not grant permission to act?
- Can the learner follow the graph-to-action trace?
- Can the learner distinguish stale evidence, limited authority, human approval, stop conditions,
  idempotency, verification, and audit recording?
- Can the learner complete and defend the Agent Action Contract?
- Record confusing terms, skipped controls, and moments requiring instructor intervention.

### 3. Factual and source accuracy

Reviewer qualification: semantic-technology, AI-governance, or evidence-management specialist.

Confirm:

- RDF, graph evidence, validation, provenance, authority, and inference language remain within the
  cited evidence.
- Illustrative utility assumptions are labeled as assumptions.
- The lesson does not imply that grounding guarantees truth, authorization, determinism, or safe
  action.
- Source titles, links, uses, and limitations are accurate.

### 4. Cybersecurity and industrial-control safety

Reviewer qualification: utility cybersecurity, operational technology, industrial-control, or
critical-infrastructure security specialist.

Confirm:

- The lesson does not encourage direct uncontrolled actuation.
- Least privilege, identity, approval, bounded tools, stop conditions, retries, reconciliation,
  verification, and audit controls are defensible.
- The distinction between proposing, drafting, approving, assigning priority, and executing an
  operational change is clear.
- Credentials, network boundaries, incident response, and human authority are not overstated.

### 5. Accessibility and screen reader

Reviewer qualification: accessibility specialist or experienced screen-reader user.

Test:

- heading and landmark sequence;
- alternative text and structured text equivalents;
- reading-guide and learner-conclusion relationships;
- detailed-view dialog name, focus entry, keyboard zoom, keyboard pan, reset, Escape, close, and
  focus return;
- assessments, feedback, work-product fields, drawers, and completion status;
- 200 and 400 percent reflow and reduced-motion meaning.

### 6. Physical iPhone and iPad

Reviewer qualification: named reviewer using physical Apple devices and current supported browser.

Test both devices:

- all five default overviews fit with no forced horizontal scrolling;
- all five vertical mobile reading sequences are legible;
- detail viewers open, zoom, pan, reset, and close by touch;
- no sticky header, dialog, keyboard, or focus behavior hides controls;
- assessments and the Agent Action Contract are usable;
- record device model, operating-system version, browser, and orientation.

### 7. Credential and authority boundary

Reviewer qualification: OWOS credential owner, course owner, compliance owner, or delegated
authority.

Confirm:

- completion does not imply operational authorization, engineering competence, cybersecurity
  approval, or certification beyond the approved credential;
- assessment evidence is adequate for any proposed credential;
- release, graph-publication, and operational-authority statements are correct;
- the final credential claim, if any, is explicitly written and approved.

### 8. Module 17, Module 18, and Module 19 coherence

Reviewer qualification: instructional designer, course owner, or semantic-domain reviewer.

Confirm:

- Module 17 prepares the answer-architecture distinctions needed by Module 18.
- Module 18 teaches governed action without duplicating Module 17.
- The Agent Action Contract creates a testable prerequisite for Module 19.
- Module 19 can be designed from scratch without silently inheriting an obsolete capstone page.
- Vocabulary, work products, prerequisites, and transitions remain coherent.

## Reviewer evidence form

Copy this section once for each lane.

```text
Review lane:
Candidate checksum:
Reviewer name:
Reviewer role and qualification:
Organization, optional:
Review date:
Device or assistive technology, when applicable:

Decision: Approve / Approve with notes / Block

Evidence inspected:

Release-blocking findings:

Important corrections:

Optional improvements:

What the candidate does well:

Reviewer attestation:
I reviewed the candidate identified by the checksum above and recorded my actual findings.

Signature or recorded approval:
```

## Completion register

| Lane | Reviewer | Date | Checksum matches | Decision | Evidence file | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| Utility practitioner | pending | | | | | blocked |
| Novice learner | pending | | | | | blocked |
| Factual and source | pending | | | | | blocked |
| Cybersecurity and industrial control | pending | | | | | blocked |
| Accessibility and screen reader | pending | | | | | blocked |
| Physical iPhone and iPad | pending | | | | | blocked |
| Credential and authority | pending | | | | | blocked |
| Course coherence | pending | | | | | blocked |

## Final-release gate

Final release may proceed only when every required lane has a named reviewer, matching checksum,
completed evidence, and an Approve or Approve with notes decision with no release blocker. Hardeep
then gives explicit final-release approval for that exact checksum.
