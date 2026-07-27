#!/usr/bin/env python3
"""Verify a QA/QC certificate against owos-qaqc-certificate/1.

A published document is a claim about quality. This checks that the claim has a
record behind it: that a certificate exists, that it certifies the version
actually being published, that every required section is present, and that no
citation quietly rests on an archived agency URL.

Usage:
    python3 tools/check_qaqc_certificate.py <certificate.md> [--artifact <file>]
    python3 tools/check_qaqc_certificate.py --all
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "owos-qaqc-certificate/1"

REQUIRED_SECTIONS = (
    "Identification",
    "Graphics",
    "Analysis and physics",
    "Factual accuracy",
    "Citations",
    "Editorial and instructional",
    "Rendered quality",
    "Defects found and disposition",
    "Open items and limitations",
    "Correction and version history",
)

REQUIRED_FRONTMATTER = (
    "contract",
    "document_id",
    "document_version",
    "artifact_checksum_sha256",
    "certificate_version",
    "reviewer",
    "date",
)

# An archived copy proves a document once existed at an agency, not that the
# agency publishes it now. Allowed, but only when the certificate says so.
ARCHIVE_MARKERS = (
    "snapshot.epa.gov",
    "19january2017snapshot",
    "web.archive.org",
    "webharvest.gov",
    "archive-it.org",
)
ARCHIVE_ACKNOWLEDGEMENT = re.compile(
    r"archiv|snapshot", re.IGNORECASE
)


class CertificateError(ValueError):
    """Raised when a certificate is missing, incomplete, or unsafe."""


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.strip().startswith("#"):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check(cert_path: Path, artifact: Path | None = None) -> list[str]:
    errors: list[str] = []
    if not cert_path.is_file():
        raise CertificateError(f"no certificate at {cert_path}")

    text = cert_path.read_text(encoding="utf-8")
    front = parse_frontmatter(text)

    for field in REQUIRED_FRONTMATTER:
        if not front.get(field):
            errors.append(f"frontmatter: missing {field}")

    if front.get("contract") and front["contract"] != CONTRACT:
        errors.append(
            f"frontmatter: contract must be {CONTRACT}, found {front['contract']}"
        )

    # Sections are matched on their heading text, so a renamed section reads as
    # a missing one. That is intentional.
    headings = re.findall(r"^#{2,3}\s*(?:\d+\.\s*)?(.+?)\s*$", text, re.MULTILINE)
    normalised = {h.strip().lower() for h in headings}
    for section in REQUIRED_SECTIONS:
        if section.lower() not in normalised:
            errors.append(f"missing required section: {section}")

    # Archived citations are permitted only when named as archived.
    #
    # The acknowledgement must be prose, not the URL. Archive hostnames contain
    # the words "archive" and "snapshot" themselves, so searching raw text for
    # those words matches the very citation being flagged and the check passes
    # every time. URL-like tokens are stripped from the window first.
    for marker in ARCHIVE_MARKERS:
        for hit in re.finditer(re.escape(marker), text):
            window = text[max(0, hit.start() - 700) : hit.end() + 700]
            window = re.sub(r"https?://\S+", " ", window)
            window = re.sub(r"[\w.-]*(?:archive|snapshot)[\w.-]*\.(?:gov|org|com)\S*", " ", window)
            window = re.sub(r"`[^`]*`", " ", window)
            if not ARCHIVE_ACKNOWLEDGEMENT.search(window):
                errors.append(
                    f"citation uses an archived URL ({marker}) without identifying "
                    "it as archived in prose and stating the live-authority position"
                )
                break

    if artifact is not None:
        if not artifact.is_file():
            errors.append(f"artifact not found: {artifact}")
        else:
            actual = sha256(artifact)
            claimed = front.get("artifact_checksum_sha256", "")
            if claimed and claimed != actual:
                errors.append(
                    "artifact checksum does not match the certificate: "
                    f"certificate {claimed[:16]}..., artifact {actual[:16]}..."
                )

    # A zero-defect certificate must still show the work.
    defects = re.search(
        r"#{2,3}\s*(?:\d+\.\s*)?Defects found and disposition(.*?)(?=\n#{2,3}\s|\Z)",
        text,
        re.S | re.IGNORECASE,
    )
    if defects and len(defects.group(1).strip()) < 200:
        errors.append(
            "defects section is too thin to evidence a review; state what was "
            "examined even when nothing was found"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", help="path to QA-QC-CERTIFICATE.md")
    parser.add_argument("--artifact", help="published artifact to checksum against")
    parser.add_argument(
        "--all", action="store_true", help="check every certificate in the repository"
    )
    args = parser.parse_args()

    targets: list[tuple[Path, Path | None]] = []
    if args.all:
        for path in sorted(ROOT.rglob("QA-QC-CERTIFICATE.md")):
            targets.append((path, None))
        if not targets:
            print("no certificates found")
            return 1
    elif args.certificate:
        targets.append(
            (Path(args.certificate), Path(args.artifact) if args.artifact else None)
        )
    else:
        parser.error("give a certificate path or --all")

    failed = 0
    for cert_path, artifact in targets:
        try:
            errors = check(cert_path, artifact)
        except CertificateError as error:
            print(f"FAIL {cert_path}: {error}")
            failed += 1
            continue
        if errors:
            failed += 1
            print(f"FAIL {cert_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {cert_path}")

    if failed:
        print(f"\n{failed} certificate(s) failed. Publication is blocked.")
        return 1
    print("\nAll certificates satisfy owos-qaqc-certificate/1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
