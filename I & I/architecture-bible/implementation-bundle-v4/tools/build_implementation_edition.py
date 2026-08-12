#!/usr/bin/env python3
"""Compile the Version 4 implementation bundle into one reviewable Markdown volume."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml


HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fenced(title: str, path: Path, language: str) -> str:
    return (
        f"# Appendix: {title}\n\n"
        f"Source file: `{path.relative_to(BUNDLE)}`\n\n"
        f"```{language}\n{path.read_text().rstrip()}\n```\n"
    )


def build() -> Path:
    sections = [
        "# PumpOS and I&I Intelligence Version 4\n\n"
        "## Compiled Implementation Edition and Agent Execution Bundle\n\n"
        "**Status:** Internal implementation candidate  \n"
        "**Parent:** PumpOS and I&I Intelligence System Bible, Version 3  \n"
        "**Production authority:** Not granted\n\n"
        "This compiled volume is a review convenience. The separately reviewable source files in the "
        "Version 4 folder remain the implementation authority.\n\n---\n\n",
        (BUNDLE / "COPY-PASTE-AGENT-HANDOFF.md").read_text(),
        "\n\n---\n\n",
        (BUNDLE / "implementation-edition.md").read_text(),
        "\n\n---\n\n",
        fenced("Work packages", BUNDLE / "work-packages.yaml", "yaml"),
        "\n\n---\n\n",
        fenced("Acceptance matrix", BUNDLE / "acceptance-matrix.yaml", "yaml"),
        "\n\n---\n\n",
        fenced("First-slice OpenAPI contract", BUNDLE / "openapi.yaml", "yaml"),
        "\n\n---\n\n",
        fenced("Bounded agent tools", BUNDLE / "agent-tools.yaml", "yaml"),
        "\n\n---\n\n",
        fenced("Formula contract template", BUNDLE / "formula-contract-template.yaml", "yaml"),
    ]

    for path in sorted((BUNDLE / "schemas").glob("*.schema.json")):
        sections.extend(
            [
                "\n\n---\n\n",
                fenced(f"JSON Schema: {path.stem}", path, "json"),
            ]
        )

    sections.extend(
        [
            "\n\n---\n\n",
            fenced(
                "Golden-case register",
                BUNDLE / "golden-cases/golden-case-register.yaml",
                "yaml",
            ),
            "\n\n---\n\n",
            "# Version 4 release boundary\n\n"
            "This bundle is separately actionable but not production-approved. Target-repository "
            "identification, owner approval, formula review, numerical verification, model assurance, "
            "security review, utility pilot review, and production release remain blocked.\n",
        ]
    )

    content = "".join(sections)
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    output = BUNDLE / "ii-intelligence-implementation-edition-v4.md"
    output.write_text(content)

    input_files = [
        BUNDLE / "AGENTS.md",
        BUNDLE / "COPY-PASTE-AGENT-HANDOFF.md",
        BUNDLE / "implementation-edition.md",
        BUNDLE / "work-packages.yaml",
        BUNDLE / "acceptance-matrix.yaml",
        BUNDLE / "openapi.yaml",
        BUNDLE / "agent-tools.yaml",
        BUNDLE / "formula-contract-template.yaml",
        BUNDLE / "golden-cases/golden-case-register.yaml",
        *sorted((BUNDLE / "schemas").glob("*.schema.json")),
    ]
    manifest = {
        "artifact": "pumpos_ii_implementation_bundle_v4_build",
        "version": "0.4.0",
        "status": "candidate",
        "generated_at": "2026-07-29",
        "builder": {
            "path": "tools/build_implementation_edition.py",
            "sha256": sha256(HERE / "build_implementation_edition.py"),
        },
        "validator": {
            "path": "tools/validate_bundle.py",
            "sha256": sha256(HERE / "validate_bundle.py"),
        },
        "inputs": [
            {
                "path": str(path.relative_to(BUNDLE)),
                "sha256": sha256(path),
            }
            for path in input_files
        ],
        "output": {
            "path": output.name,
            "sha256": sha256(output),
            "lines": len(content.splitlines()),
            "words": len(content.split()),
            "bytes": len(output.read_bytes()),
        },
        "validation": {
            "command": "python3 tools/validate_bundle.py",
            "status": "pending",
        },
        "release": {
            "approved": False,
            "reason": "Owner, repository, engineering, numerical, model, security, pilot, and release gates remain open.",
        },
    }
    (BUNDLE / "build-manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=False)
    )
    return output


if __name__ == "__main__":
    print(build())
