#!/usr/bin/env python3
"""Fail-closed convergence audit for an OWOS Concept Brief inventory repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_PROMPT = ROOT / "core/standards/OWOS-CONCEPT-BRIEF-ACTIVATION-PROMPT.md"
EXPECTED = {
    "schema_version": 1,
    "upstream_repository": "hpad66-pixel/owos-learning-content",
    "concept_contract": "owos-concept-brief/2",
    "concept_contract_version": "2.1.0",
    "capability_registry_id": "owos-learning-capabilities/1",
    "capability_registry_version": 1,
    "canonical_activation_prompt": (
        "core/standards/OWOS-CONCEPT-BRIEF-ACTIVATION-PROMPT.md"
    ),
    "public_authority_policy": "us-federal-epa-public/1",
    "portfolio_role": "candidate_inventory_and_activation_only",
}
REQUIRED_HEADINGS = (
    "# ",
    "## Value thesis",
    "## Intended outcome",
    "## Activation seed",
)
FORBIDDEN_PUBLIC_STATE_PATTERNS = (
    r"applicable state requirements",
    r"state requirements must be labeled",
    r"keep state requirements in .*branches",
    r"preserve state-specific requirements as .*branches",
    r"label state, local, and permit requirements separately",
    r"expose state or permit variation",
)
FORBIDDEN_DEFINITION_MARKERS = (
    "assessment_types:",
    "interaction_components:",
    "visual_component_ids:",
)


class PortfolioConvergenceError(RuntimeError):
    pass


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise PortfolioConvergenceError(f"{path}: expected a YAML object")
    return data


def audit(portfolio: Path) -> dict:
    errors: list[str] = []
    manifest_path = portfolio / "owos-upstream.yaml"
    prompt_path = portfolio / "ACTIVATION-PROMPT.md"
    if not manifest_path.is_file():
        errors.append("missing owos-upstream.yaml")
        manifest = {}
    else:
        manifest = load_yaml(manifest_path)
    for key, expected in EXPECTED.items():
        if manifest.get(key) != expected:
            errors.append(
                f"owos-upstream.yaml: {key} must be {expected!r}, "
                f"found {manifest.get(key)!r}"
            )

    if not prompt_path.is_file():
        errors.append("missing ACTIVATION-PROMPT.md")
    elif prompt_path.read_bytes() != CANONICAL_PROMPT.read_bytes():
        errors.append(
            "ACTIVATION-PROMPT.md diverges from the canonical upstream activation prompt"
        )

    candidate_files = sorted((portfolio / "briefs").glob("*/*.md"))
    if len(candidate_files) != 42:
        errors.append(f"expected 42 candidate records, found {len(candidate_files)}")
    for path in candidate_files:
        text = path.read_text(encoding="utf-8")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.relative_to(portfolio)}: missing {heading.strip()}")
        lowered = text.lower()
        for pattern in FORBIDDEN_PUBLIC_STATE_PATTERNS:
            if re.search(pattern, lowered, re.DOTALL):
                errors.append(
                    f"{path.relative_to(portfolio)}: public state-requirement drift: "
                    f"{pattern}"
                )

    for path in portfolio.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN_DEFINITION_MARKERS:
            if marker in text:
                errors.append(
                    f"{path.relative_to(portfolio)}: duplicated shared definition {marker}"
                )

    if errors:
        raise PortfolioConvergenceError("\n".join(errors))
    return {
        "status": "passed",
        "portfolio": str(portfolio.resolve()),
        "candidates": len(candidate_files),
        "concept_contract": EXPECTED["concept_contract"],
        "capability_registry": EXPECTED["capability_registry_id"],
        "authority_policy": EXPECTED["public_authority_policy"],
        "activation_prompt": "exact_match",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("portfolio", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(audit(args.portfolio), indent=2))
    except (PortfolioConvergenceError, OSError, yaml.YAMLError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
