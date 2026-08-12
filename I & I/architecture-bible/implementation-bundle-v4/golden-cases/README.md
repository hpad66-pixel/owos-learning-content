# Golden Numerical Cases

Golden cases convert the Version 3 worked methods into executable verification assets.

Each case must contain:

```text
case-id/
  case.yaml
  source-data/
  accepted-input-snapshot.json
  calculation-request.json
  expected-results.json
  expected-warnings.json
  expected-lineage.json
  reviewer-notes.md
  review-disposition.yaml
```

## Rules

- Golden values are reviewed expectations, not values copied from the implementation under test.
- Each formula needs a positive case and at least one blocked or failure case.
- Units, time basis, boundary, precision, and tolerances are explicit.
- A reviewer identifies the independent calculation or trusted comparison method.
- A changed formula version creates a new case version.
- Old cases remain available for reproducibility.
- Synthetic cases are labeled and never represented as facility evidence.

The included `golden-case-001` is a contract fixture. It demonstrates file shape and the
rainfall-volume result carried from Version 3. It does not constitute independent formula approval.
