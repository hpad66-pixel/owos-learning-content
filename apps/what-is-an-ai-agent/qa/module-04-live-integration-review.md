# Module 4 Live Integration Review

Status: Blocked until the golden lesson is approved for OWOS runtime intake

## Required verification

- [ ] Authenticated learner can enroll in course `aia001`.
- [ ] Started, explored, progressed, and completed events reach the OWOS API.
- [ ] Version 0.6.0 idempotency keys prevent duplicate completion records.
- [ ] Supabase stores the correct user, course, module, event, timestamp, and page.
- [ ] A failed request produces honest learner feedback and does not lose browser work.
- [ ] A page refresh restores the learner contract and lesson requirements.
- [ ] Course manifest, source package, and OWOS runtime refer to the same version.

## Evidence to attach

- API response identifiers
- Supabase row identifiers or an approved redacted screenshot
- Authenticated browser test date
- Manifest commit and OWOS platform commit
- Reviewer name and release decision
