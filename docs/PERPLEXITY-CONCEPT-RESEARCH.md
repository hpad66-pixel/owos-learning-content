# Perplexity Deep Research for OWOS Concept Briefs

Perplexity is a candidate-source discovery service inside the Concept Brief lifecycle. It is not an
evidence authority and cannot mark a claim verified.

## Configure once

On macOS, use the secure Keychain configuration:

```bash
python3 tools/concept_research.py configure
```

The command asks for the key through macOS Keychain. It does not write the value into this
repository. Automated environments should provide `PERPLEXITY_API_KEY` through their managed secret
store. A git-ignored `.env.local` file is supported only as a local fallback:

```text
PERPLEXITY_API_KEY=replace-with-the-real-key
```

Check connectivity without printing the secret:

```bash
python3 tools/concept_research.py credential-status
```

## Submit a traceable research cluster

```bash
python3 tools/concept_research.py research \
  concept-briefs/coagulation-vs-flocculation \
  --claim-id claim-example
```

The gateway:

- uses `sonar-deep-research`;
- submits an asynchronous research job;
- applies the permanent United States water-sector evidence boundary;
- asks for original sources, exact locators, contrary evidence, limitations, and freshness;
- stores a candidate-research receipt under `research/perplexity/`; and
- does not change `claims.yaml`, `sources.yaml`, verification coverage, or release state.

Refresh a submitted job:

```bash
python3 tools/concept_research.py research-status \
  concept-briefs/coagulation-vs-flocculation/research/perplexity/<job-id>.json
```

Completed findings must still be checked against the original authority, given exact locators,
independently traced, and reviewed by a qualified United States technical practitioner before a
material claim can become verified.
