# OWOS Concept Briefs

This directory contains governed Concept Brief source packages.

Each package follows `owos-concept-brief/2` and is compiled with:

```bash
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief>
python3 tools/concept_brief_compiler.py build concept-briefs/<brief> \
  --output concept-briefs/<brief>/dist/preview.html
python3 tools/concept_brief_compiler.py portfolio-check concept-briefs
```

Release validation is separate:

```bash
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief> --release-ready
```

A working preview is not a release. The release gate requires complete claim verification, qualified
technical review, manual experience reviews, Graph and Community approval, commercial-integrity
approval, and owner approval.

The compiler also enforces the approved learner-facing economy: an “In 30 seconds” orientation,
four-or-fewer primary controls, no claim-count marketing, a useful outline-only public SOP boundary,
one compact end-of-brief feedback entry, a three-part transfer recap, and hidden inactive vendor
placements. Deep claims, provenance, Graph records, Community moderation, commercial controls, and
version history remain in the governed package and administrator surfaces.

Public water-sector briefs use federal and EPA authority only. AWWA references must be labeled as
professional context; state and non-United States requirements do not enter the public authority
frame.

See `core/standards/CONCEPT-BRIEF-PRODUCTION-CONTRACT.md` and
`docs/CONCEPT-BRIEF-AUTHORING-GUIDE.md`.
