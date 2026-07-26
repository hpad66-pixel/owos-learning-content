---
title: OWOS Learning Record, Credential, and Pathway Standard
version: 1.0.0
status: APPROVED IMPLEMENTATION DIRECTION
owner: Hardeep Anand
effective: 2026-07-26
---

# OWOS Learning Record, Credential, and Pathway Standard

## Purpose

OWOS records what a learner actually completed, proves which governed content and assessment
versions produced that result, issues a certificate only after every required gate passes, and
recommends useful next learning without pretending an algorithm knows the learner better than the
learner does.

This standard applies to courses, Concept Briefs, Master Classes, and approved external learning.
The curriculum repositories remain the source of instructional truth. The learning-record service
is the source of attempt, completion, certificate, and recommendation truth.

## Standard names

- **OWOS Learning Record Service** stores immutable learning events and derived completion records.
- **OWOS Credential Service** evaluates issuance gates, creates signed credentials and certificate
  documents, and manages status, expiration, supersession, and revocation.
- **OWOS Learner Dashboard** shows the learner's learning, evidence, credentials, credit ledger,
  competency graph, and next-learning choices.
- **OWOS Learning Pathway Agent** produces explainable deepen, reskill, and cross-skill
  recommendations from consented learning records and the governed skills graph.

## Interoperability

The canonical event model is an OWOS profile of xAPI 2.0. An append-only event record carries the
authenticated actor, governed activity identifier, verb, result, context, content version,
assessment version, capability registry version, timestamp, and source receipt.

- Use **cmi5** for packaged LMS launch, authorization handshake, and xAPI-based completion when an
  LMS requires a launchable course package.
- Provide a **SCORM 2004** compatibility adapter for customers whose LMS cannot launch cmi5.
  SCORM completion and score values are transport inputs, not credential authority. The adapter
  converts them into the canonical OWOS event profile with the package and adapter versions.
- Use **Open Badges 3.0** for portable achievement credentials after issuer signing and conformance
  work are complete.
- Use **Comprehensive Learner Record 2.0** for learner-controlled collections of credentials and
  competencies when that export is implemented.

No interoperability label may be claimed until the implementation passes the applicable
conformance suite.

## Learner identity and authentication

Every credit-bearing event uses one immutable OWOS learner identifier. Authentication may use OIDC,
SAML, or another approved identity provider. The system stores the minimum identity data needed for
the offering and separates login identity from public certificate display.

Before certificate issuance:

1. the learner authenticated;
2. the enrollment is linked to the exact offering;
3. any required legal-name or license-number verification is complete;
4. consent for learning-record and credential processing is recorded;
5. duplicate or conflicting identities are resolved; and
6. an administrator can trace the identity decision without exposing secrets.

Browser storage, an email address alone, or a SCORM learner name is never sufficient credential
identity evidence.

## Append-only learning record

Learning events are immutable. Corrections append a voiding, replacement, or supersession record
and never rewrite prior history. At minimum, record:

- registration and consent;
- content launch and version;
- required interaction completion;
- assessment attempts, item versions, scores, and passing result;
- active participation evidence where required;
- completion decision and rule version;
- learner evaluation where required;
- certificate issuance, download, verification, expiration, revocation, and supersession; and
- recommendation presentation, explanation, acceptance, dismissal, and correction.

Facility-sensitive operational, security, customer, personnel, and compliance data is prohibited in
public learning records.

## Credential issuance gates

A certificate or credit record is issued only when all applicable gates pass:

1. **Offering gate**: exact title, version, outcomes, audience, instructor or provider, measured
   learning time, assessment rule, credit type, jurisdiction, and approval period are approved.
2. **Content gate**: the exact source commit, compiler version, package checksum, and release
   manifest are approved.
3. **Identity gate**: authenticated learner identity and required license or registration data are
   verified.
4. **Participation gate**: required launches, interactions, time evidence, and attendance are
   present.
5. **Assessment gate**: the exact assessment version and passing rule passed.
6. **Evaluation gate**: any required learner evaluation is complete.
7. **Accreditor gate**: the named accreditor, licensing board, or customer program approved the exact
   offering and credit claim.
8. **Issuance gate**: issuer identity, signer, unique credential identifier, verification URL,
   status record, and retention period are active.

Failure of one required gate blocks issuance. An administrator may correct evidence, but may not
manually bypass the rule without a separately recorded exception authority and reason.

## Credit terminology

Do not treat CU, CEU, PDH, contact hour, CPC credit, certificate, badge, and certification as
interchangeable.

- A **certificate of completion** proves completion of an OWOS offering. It does not automatically
  prove third-party credit.
- A **PDH, CEU, CU, or contact hour** is recorded only under a named, verified program rule.
- A **badge** is a portable digital achievement record.
- A **certification** normally represents a broader assessment and maintenance program and must not
  be claimed for ordinary course completion.

The proposed “NCCS CU” label remains unresolved. The system may prepare evidence, but it must display
`credit claim disabled` until the legal entity, program name, unit definition, provider process,
acceptance rules, and verification method are confirmed.

## Certificate contract

Every issued certificate contains:

- learner display name;
- immutable credential identifier;
- offering title, version, and completion date;
- measured instructional or participation time;
- assessment result and completion basis;
- credit type and amount only when approved;
- provider and instructor-of-record;
- applicable jurisdiction or accreditor statement;
- issue date and expiration date when applicable;
- verification URL and QR code;
- source release identifier and content checksum in the verification record;
- signer identity and signature method;
- status of active, expired, superseded, or revoked; and
- a plain statement of what the certificate does and does not authorize.

The PDF is a human-readable rendering. The signed credential record and status endpoint are the
verification authority.

## Learner dashboard

Every authenticated learner dashboard provides:

- learning in progress and completed learning;
- credentials with active, pending, expired, superseded, and revoked states;
- a credit ledger grouped by program, jurisdiction, renewal period, and credit type;
- downloadable certificates and portable credential exports;
- the evidence behind each completion and credit decision;
- competencies demonstrated, developing, and not yet assessed;
- recommendations in deepen, reskill, and cross-skill lanes;
- prerequisites and gaps for every suggested next step;
- consent, privacy, export, correction, and deletion controls; and
- a visible distinction between OWOS completion, third-party credit, and professional licensure.

## AI learning pathways

The standard product term is **AI-assisted skills-based learning pathways**. Individual suggestions
are **next-best-learning recommendations**.

The Learning Pathway Agent may use:

- completed and in-progress learning;
- assessment and work-product evidence;
- learner-declared role, goals, and interests;
- competencies explicitly mapped to governed content;
- prerequisite, remediation, adjacency, and cross-sector Graph relationships; and
- the freshness and confidence of those relationships.

It must not use protected traits, private facility data, inferred job performance, disciplinary
records, or undisclosed employer surveillance.

Every recommendation must show:

- the lane: deepen, reskill, or cross-skill;
- the suggested learning item and version;
- the reason and evidence;
- the competency gained or strengthened;
- prerequisites and missing evidence;
- cross-sector transfer boundaries;
- confidence and freshness;
- whether the suggestion is rules-based, AI-ranked, or both; and
- controls to accept, dismiss, snooze, or correct the learner profile.

Rules establish eligibility and safety. AI may rank eligible choices and explain tradeoffs. AI does
not grant credit, waive a prerequisite, issue a credential, or determine employment suitability.

## Quality and release

Before production use, complete:

- privacy impact and retention review;
- identity, access-control, and account-recovery review;
- xAPI profile and LRS conformance testing;
- cmi5 or SCORM adapter testing where used;
- certificate signing, verification, revocation, and supersession testing;
- dashboard desktop, tablet, phone, keyboard, screen-reader, zoom, and reduced-motion review;
- bias, relevance, explanation, dismissal, and correction tests for recommendations;
- accreditor or jurisdiction review for each credit profile; and
- explicit owner approval for credential issuance.

An attractive certificate or successful LMS completion event is never evidence that these gates
passed.
