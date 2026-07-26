# OWOS Credential and Learning Pathway Operating Model

## Outcome

OWOS will be able to prove what a learner completed, issue a verifiable certificate when every
applicable gate passes, maintain a professional-credit ledger, and recommend useful next learning
across water, wastewater, stormwater, and adjacent One Water practice.

The product is an **AI-assisted skills-based learning pathway**. Each suggestion is a
**next-best-learning recommendation** in one of three lanes:

- **Deepen**: advance within the learner's current domain.
- **Reskill**: build a materially different capability or role path.
- **Cross-skill**: transfer a mental model into an adjacent water sector.

## 1. Resolve the credit authority before claiming credit

“NCCS CUs” is not yet an authenticated program identity. Keep
`accreditor:nccs-cu-unresolved` disabled until the owner supplies or approves:

1. the legal entity and official program name;
2. the program URL and contact;
3. the exact definition of a CU and its conversion, if any;
4. provider and course approval requirements;
5. identity, attendance, assessment, evaluation, and instructor requirements;
6. certificate wording and required fields;
7. retention, audit, reporting, correction, and revocation rules; and
8. whether approval applies nationally, by state, by profession, or only to a customer program.

NCEES Continuing Professional Competency tracking is a possible match, not a confirmed one.
MyNCEES can hold course records and supporting documents, while state licensing boards retain their
own acceptance requirements. If NCEES is confirmed, OWOS should produce a board-ready evidence
package and never imply that a tracker entry guarantees acceptance.

## 2. Approve the exact offering

Create a versioned credit profile for each approved combination of course, delivery mode, credit
type, jurisdiction, and approval period. The profile binds:

- title, outcomes, audience, prerequisites, provider, and instructor of record;
- source commit, compiler version, package checksum, and release manifest;
- measured instructional and participation time;
- assessment version, passing rule, retry policy, and accommodations;
- attendance or active-participation rule;
- evaluation requirement;
- approved credit label, amount, jurisdiction, and approval identifier; and
- approval start, approval end, retention period, and certificate language.

A content revision that changes outcomes, duration, assessment meaning, or instructor evidence
creates a new offering version and triggers approval review.

## 3. Authenticate enrollment and consent

Use an approved identity provider and one immutable OWOS learner identifier. A credit-bearing
enrollment records the offering, learner consent, identity-verification level, and any required
license or registration number. Display name is stored separately from login identity.

Browser storage, an email address alone, or an LMS-provided name cannot authorize credential
issuance. Account merging and corrections append an auditable identity decision.

## 4. Record learning once and translate at the edges

xAPI is the canonical OWOS event model. cmi5 is the preferred packaged LMS launch because it
combines LMS launch rules with xAPI statements. A SCORM 2004 package remains available as a legacy
adapter, but its values are translated into the OWOS record:

| SCORM 2004 value | OWOS record use |
| --- | --- |
| `cmi.completion_status` | Completion evidence input |
| `cmi.success_status` | Assessment-result input |
| `cmi.score.scaled` | Versioned score input |
| `cmi.session_time` | Session evidence, never the sole credit clock |
| `cmi.interactions.n.*` | Versioned assessment-attempt evidence |
| `cmi.learner_id` | LMS subject reference, not sufficient identity proof |

Every translated event records the package, adapter, content, assessment, and registry versions.
Corrections append voiding or replacement events; prior history is not overwritten.

## 5. Decide completion and issue fail closed

The Credential Service evaluates the offering, content, identity, participation, assessment,
evaluation, accreditor, and issuer/status gates. One failed or missing required gate produces
`evidence_pending`; it does not produce an issued certificate.

When every gate passes, the service:

1. assigns an immutable credential identifier;
2. signs the machine-readable credential;
3. publishes a status and verification record;
4. generates the human-readable certificate PDF and QR code;
5. adds the record to the learner's credit ledger;
6. emits an issuance event; and
7. supports later expiration, supersession, revocation, or correction without erasing history.

Open Badges 3.0 is the target for portable achievement credentials. Comprehensive Learner Record
2.0 is the target for a learner-controlled collection of credentials and competencies. Do not claim
conformance until the applicable conformance work passes.

## 6. Learner dashboard

The dashboard has four connected views:

1. **Learning**: enrolled, in progress, completed, paused, and recommended items.
2. **Credentials**: evidence pending, eligible, issued, expired, superseded, and revoked records,
   with certificate download and verification.
3. **Credit ledger**: credit program, jurisdiction, renewal period, unit type, approved amount, and
   evidence package.
4. **Skills and pathways**: demonstrated, developing, and unassessed competencies plus deepen,
   reskill, and cross-skill recommendations.

The learner can inspect evidence, export records, correct profile data, manage consent, dismiss or
snooze recommendations, and distinguish OWOS completion from third-party credit and licensure.

## 7. AI-assisted pathways

Rules first determine what is eligible, safe, current, and prerequisite-complete. AI then ranks
eligible choices and explains tradeoffs. Each recommendation records:

- lane, target item, version, competency, and cross-sector relationship;
- reason, supporting learner evidence, prerequisites, and missing evidence;
- confidence, source freshness, and whether ranking was rules-based, AI-ranked, or both; and
- learner actions to accept, dismiss, snooze, or correct.

The pathway agent must not use protected traits, private facility data, disciplinary records,
undisclosed employer surveillance, or inferred job performance. It cannot grant credit, waive
prerequisites, certify competence, or determine employment suitability.

## 8. Quality, security, and operations

Before production activation, complete:

- privacy impact, data retention, access-control, recovery, and breach-response reviews;
- xAPI profile, LRS, cmi5, and any SCORM adapter conformance and replay testing;
- identity duplication, merge, correction, and account-recovery tests;
- deterministic completion, retry, accommodation, and version-migration tests;
- certificate signing, verification, status, revocation, and supersession tests;
- desktop, tablet, phone, keyboard, screen-reader, zoom, and reduced-motion dashboard reviews;
- recommendation relevance, bias, explanation, freshness, dismissal, and correction tests;
- accreditor or licensing-board review for each credit profile; and
- explicit owner approval before enabling credential issuance.

## Delivery sequence

1. Confirm the meaning of “NCCS CUs” and approve the first credit profile.
2. Implement authenticated learner identity and the append-only xAPI Learning Record Service.
3. Add cmi5 launch and the tested SCORM 2004 compatibility adapter.
4. Implement the gate evaluator, signed credential record, verification endpoint, and status list.
5. Connect the learner dashboard to real records.
6. Pilot one course and one Concept Brief in non-credit mode.
7. Complete accreditor review and an auditable shadow issuance.
8. Enable live issuance only after owner approval.
9. Activate rules-based pathways, then add AI ranking after recommendation QA passes.
