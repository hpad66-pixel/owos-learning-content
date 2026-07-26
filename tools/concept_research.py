#!/usr/bin/env python3
"""Secure Perplexity research gateway for governed OWOS Concept Briefs.

This tool discovers candidate evidence. It never verifies a claim, modifies
claims.yaml or sources.yaml, or participates in deterministic compilation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import yaml


ROOT = Path(__file__).resolve().parents[1]
API_ROOT = "https://api.perplexity.ai"
ASYNC_CREATE_PATH = "/v1/async/sonar"
MODEL = "sonar-deep-research"
POLICY_VERSION = "owos-concept-research/1"
KEYCHAIN_SERVICE = "ai.onewateros.concept-research.perplexity"
KEYCHAIN_ACCOUNT = "PERPLEXITY_API_KEY"
SECRET_NAME = "PERPLEXITY_API_KEY"
LOCAL_SECRET_FILE = ROOT / ".env.local"
MATERIAL_CLAIM_TYPES = {
    "sourced_fact",
    "regulatory_requirement",
    "technical_standard",
    "expert_interpretation",
    "commercial_claim",
}


class ConceptResearchError(RuntimeError):
    """Raised when research cannot proceed safely."""


@dataclass(frozen=True)
class Credential:
    value: str
    source: str


def secure_urlopen(request: urllib.request.Request, *, timeout: int) -> Any:
    """Open HTTPS with an explicit trusted CA bundle when Python lacks one."""
    try:
        import certifi

        context = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        context = ssl.create_default_context()
    return urllib.request.urlopen(request, timeout=timeout, context=context)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def redact(value: Any, secrets: tuple[str, ...]) -> Any:
    """Recursively remove exact secret values from diagnostic data."""
    active = tuple(secret for secret in secrets if secret)
    if isinstance(value, dict):
        return {str(key): redact(item, active) for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item, active) for item in value]
    if isinstance(value, tuple):
        return tuple(redact(item, active) for item in value)
    if isinstance(value, str):
        result = value
        for secret in active:
            result = result.replace(secret, "[REDACTED]")
        return result
    return value


def parse_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise ConceptResearchError(f"{path}:{number}: expected NAME=value")
        name, raw_value = line.split("=", 1)
        name = name.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            raise ConceptResearchError(f"{path}:{number}: invalid environment name")
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[name] = value
    return values


def read_keychain() -> str | None:
    if platform.system() != "Darwin":
        return None
    try:
        result = subprocess.run(
            [
                "/usr/bin/security",
                "find-generic-password",
                "-a",
                KEYCHAIN_ACCOUNT,
                "-s",
                KEYCHAIN_SERVICE,
                "-w",
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value if result.returncode == 0 and value else None


def resolve_credential(
    *,
    environ: dict[str, str] | None = None,
    local_secret_file: Path = LOCAL_SECRET_FILE,
    keychain_reader: Callable[[], str | None] = read_keychain,
) -> Credential:
    """Resolve a key once without ever copying it into a Concept Brief."""
    keychain_value = keychain_reader()
    if keychain_value:
        return Credential(keychain_value, "macOS Keychain")

    environment = os.environ if environ is None else environ
    environment_value = environment.get(SECRET_NAME, "").strip()
    if environment_value:
        return Credential(environment_value, "environment")

    file_value = parse_env_file(local_secret_file).get(SECRET_NAME, "").strip()
    if file_value:
        return Credential(file_value, str(local_secret_file))

    raise ConceptResearchError(
        "Perplexity is not configured. Run `python3 tools/concept_research.py configure` "
        "once on this Mac, or set PERPLEXITY_API_KEY in the deployment secret store."
    )


def configure_keychain() -> None:
    if platform.system() != "Darwin":
        raise ConceptResearchError(
            "Secure interactive Keychain configuration is available on macOS. "
            "Use the deployment secret store or a git-ignored .env.local elsewhere."
        )
    print("Enter the Perplexity API key in the secure macOS Keychain prompt.")
    print("The value will not be written to this repository.")
    try:
        subprocess.run(
            [
                "/usr/bin/security",
                "add-generic-password",
                "-a",
                KEYCHAIN_ACCOUNT,
                "-s",
                KEYCHAIN_SERVICE,
                "-l",
                "OWOS Concept Research: Perplexity",
                "-j",
                "Used by the OWOS Concept Research gateway",
                "-U",
                "-w",
            ],
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise ConceptResearchError("The Perplexity credential was not saved.") from error
    print("Perplexity is configured for OWOS Concept Research.")


def remove_keychain_credential() -> None:
    if platform.system() != "Darwin":
        raise ConceptResearchError("No macOS Keychain is available on this system.")
    result = subprocess.run(
        [
            "/usr/bin/security",
            "delete-generic-password",
            "-a",
            KEYCHAIN_ACCOUNT,
            "-s",
            KEYCHAIN_SERVICE,
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ConceptResearchError("No OWOS Perplexity Keychain credential was removed.")
    print("The OWOS Perplexity Keychain credential was removed.")


def load_package_claims(package_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    brief_path = package_dir / "brief.yaml"
    claims_path = package_dir / "claims.yaml"
    if not brief_path.is_file() or not claims_path.is_file():
        raise ConceptResearchError(
            f"{package_dir}: expected a governed Concept Brief with brief.yaml and claims.yaml"
        )
    try:
        brief_data = yaml.safe_load(brief_path.read_text(encoding="utf-8")) or {}
        claims_data = yaml.safe_load(claims_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as error:
        raise ConceptResearchError(f"Cannot read Concept Brief YAML: {error}") from error
    brief = brief_data.get("brief")
    claims = claims_data.get("claims")
    if not isinstance(brief, dict) or not isinstance(claims, list):
        raise ConceptResearchError("Concept Brief identity or claim register is malformed.")
    return brief, [claim for claim in claims if isinstance(claim, dict)]


def select_claims(
    claims: list[dict[str, Any]],
    claim_ids: list[str],
    max_claims: int,
) -> list[dict[str, Any]]:
    by_id = {str(claim.get("claim_id")): claim for claim in claims if claim.get("claim_id")}
    if claim_ids:
        missing = [claim_id for claim_id in claim_ids if claim_id not in by_id]
        if missing:
            raise ConceptResearchError(f"Unknown claim IDs: {', '.join(missing)}")
        selected = [by_id[claim_id] for claim_id in claim_ids]
    else:
        selected = [
            claim
            for claim in claims
            if claim.get("claim_type") in MATERIAL_CLAIM_TYPES
            and claim.get("verification_status") == "pending"
        ]
    if not selected:
        raise ConceptResearchError("No pending material claims were selected for research.")
    if len(selected) > max_claims:
        raise ConceptResearchError(
            f"Selected {len(selected)} claims; the traceability limit is {max_claims}. "
            "Use --claim-id to submit smaller claim clusters."
        )
    return selected


def research_prompt(brief: dict[str, Any], claims: list[dict[str, Any]]) -> str:
    claim_lines = []
    for claim in claims:
        claim_lines.append(
            json.dumps(
                {
                    "claim_id": claim.get("claim_id"),
                    "claim_type": claim.get("claim_type"),
                    "claim_text": claim.get("claim_text"),
                    "scope": claim.get("scope"),
                    "jurisdiction": claim.get("jurisdiction"),
                    "limitations": claim.get("limitations"),
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
    return f"""You are performing source discovery for an OWOS Concept Brief.

Brief ID: {brief.get("brief_id")}
Brief version: {brief.get("version")}
Topic: {brief.get("title")}

This is discovery, not final verification. Investigate each claim separately.

Mandatory evidence policy:
- For water, wastewater, stormwater, and One Water governing claims, use United States authorities only.
- Start with current United States federal primary authority, then applicable state authority with the state, applicability, and effective date stated.
- Do not use non-United States regulations, standards, government guidance, design guides, operator guides, or health guidelines as governing evidence or benchmarks.
- Research conducted outside the United States may be reported only as peer-reviewed research with experimental, geographic, and transfer limitations.
- Prefer original regulations, official publications, standards, papers, datasets, and issuing organizations.
- Search deliberately for contrary evidence, superseding material, exceptions, and ambiguous terminology.
- A summary page, search snippet, vendor blog, or AI answer is not an original authority.
- Do not report a claim as verified. Report candidate evidence and unresolved questions.

For every claim, return:
- claim_id;
- proposed bounded wording;
- candidate source URL, title, issuer, document type, country and jurisdiction;
- publication or effective date;
- exact section, page, table, figure, or paragraph locator;
- authority tier and whether the source could have governing use;
- evidence supporting the claim;
- contrary or qualifying evidence;
- limitations and transfer boundaries;
- unresolved questions;
- a suggested next-review date; and
- discovery confidence, which describes source relevance rather than factual truth.

Claims:
{chr(10).join(claim_lines)}
"""


def request_body(
    brief: dict[str, Any],
    claims: list[dict[str, Any]],
    reasoning_effort: str,
) -> dict[str, Any]:
    return {
        "request": {
            "model": MODEL,
            "messages": [{"role": "user", "content": research_prompt(brief, claims)}],
            "reasoning_effort": reasoning_effort,
        }
    }


def idempotency_key(brief: dict[str, Any], claims: list[dict[str, Any]], body: dict[str, Any]) -> str:
    material = json.dumps(
        {
            "policy": POLICY_VERSION,
            "brief_id": brief.get("brief_id"),
            "version": brief.get("version"),
            "claim_ids": [claim.get("claim_id") for claim in claims],
            "request": body,
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(material).hexdigest()


class PerplexityClient:
    def __init__(
        self,
        credential: Credential,
        *,
        api_root: str = API_ROOT,
        opener: Callable[..., Any] = secure_urlopen,
    ) -> None:
        self.credential = credential
        self.api_root = api_root.rstrip("/")
        self.opener = opener

    def _json_request(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, Any] | None = None,
        idempotency: str | None = None,
    ) -> dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.credential.value}",
            "Accept": "application/json",
        }
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")
        if idempotency:
            headers["Idempotency-Key"] = idempotency
        request = urllib.request.Request(
            f"{self.api_root}{path}",
            data=data,
            headers=headers,
            method=method,
        )
        try:
            with self.opener(request, timeout=60) as response:
                result = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            detail = str(redact(detail, (self.credential.value,)))
            raise ConceptResearchError(
                f"Perplexity returned HTTP {error.code}: {detail[:800]}"
            ) from error
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            safe_error = redact(str(error), (self.credential.value,))
            raise ConceptResearchError(f"Perplexity request failed: {safe_error}") from error
        if not isinstance(result, dict):
            raise ConceptResearchError("Perplexity returned an unexpected response.")
        return result

    def submit(self, body: dict[str, Any], idempotency: str) -> dict[str, Any]:
        return self._json_request(
            "POST",
            ASYNC_CREATE_PATH,
            body=body,
            idempotency=idempotency,
        )

    def status(self, request_id: str) -> dict[str, Any]:
        safe_id = urllib.parse.quote(request_id, safe="")
        return self._json_request("GET", f"{ASYNC_CREATE_PATH}/{safe_id}")


def response_request_id(response: dict[str, Any]) -> str:
    request_id = response.get("id") or response.get("request_id")
    if not isinstance(request_id, str) or not request_id:
        raise ConceptResearchError("Perplexity did not return an asynchronous request ID.")
    return request_id


def receipt_path(package_dir: Path, request_id: str) -> Path:
    safe_id = re.sub(r"[^A-Za-z0-9._-]+", "_", request_id)
    return package_dir / "research" / "perplexity" / f"{safe_id}.json"


def write_receipt(path: Path, receipt: dict[str, Any], secrets: tuple[str, ...] = ()) -> None:
    safe_receipt = redact(receipt, secrets)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(safe_receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.chmod(temporary, 0o600)
    temporary.replace(path)


def submit_research(args: argparse.Namespace) -> None:
    package_dir = args.package.resolve()
    brief, all_claims = load_package_claims(package_dir)
    claims = select_claims(all_claims, args.claim_id, args.max_claims)
    body = request_body(brief, claims, args.reasoning_effort)
    request_key = idempotency_key(brief, claims, body)
    credential = resolve_credential()
    client = PerplexityClient(credential)
    response = client.submit(body, request_key)
    request_id = response_request_id(response)
    path = receipt_path(package_dir, request_id)
    write_receipt(
        path,
        {
            "schema": POLICY_VERSION,
            "research_role": "candidate_source_discovery_only",
            "verification_effect": "none",
            "brief_id": brief.get("brief_id"),
            "brief_version": brief.get("version"),
            "claim_ids": [claim.get("claim_id") for claim in claims],
            "credential_source": credential.source,
            "submitted_at": utc_now(),
            "idempotency_key": request_key,
            "request": body,
            "perplexity_response": response,
        },
        (credential.value,),
    )
    print(f"Submitted Perplexity Deep Research job {request_id}.")
    print(f"Candidate-research receipt: {path}")
    print("No claim or source was marked verified.")


def update_research_status(args: argparse.Namespace) -> None:
    path = args.receipt.resolve()
    if not path.is_file():
        raise ConceptResearchError(f"Research receipt not found: {path}")
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ConceptResearchError(f"Cannot read research receipt: {error}") from error
    prior_response = receipt.get("perplexity_response") or {}
    if not isinstance(prior_response, dict):
        raise ConceptResearchError("Research receipt has no valid Perplexity response.")
    request_id = response_request_id(prior_response)
    credential = resolve_credential()
    response = PerplexityClient(credential).status(request_id)
    receipt["last_checked_at"] = utc_now()
    receipt["perplexity_response"] = response
    receipt["credential_source"] = credential.source
    write_receipt(path, receipt, (credential.value,))
    print(f"Perplexity research job {request_id}: {response.get('status', 'UNKNOWN')}")
    print(f"Updated candidate-research receipt: {path}")
    print("The result still requires original-source and qualified technical verification.")


def credential_status() -> None:
    try:
        credential = resolve_credential()
    except ConceptResearchError:
        print("Perplexity credential: not configured")
        raise
    print(f"Perplexity credential: configured via {credential.source}")
    print("Secret value: hidden")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Secure Perplexity source discovery for OWOS Concept Briefs."
    )
    commands = result.add_subparsers(dest="command", required=True)

    configure = commands.add_parser(
        "configure",
        help="Store the Perplexity key once in macOS Keychain.",
    )
    configure.set_defaults(handler=lambda _args: configure_keychain())

    status = commands.add_parser(
        "credential-status",
        help="Report whether a credential can be resolved without showing it.",
    )
    status.set_defaults(handler=lambda _args: credential_status())

    clear = commands.add_parser(
        "clear-credential",
        help="Remove the OWOS Perplexity credential from macOS Keychain.",
    )
    clear.set_defaults(handler=lambda _args: remove_keychain_credential())

    research = commands.add_parser(
        "research",
        help="Submit pending claims to Perplexity Deep Research as candidate-source discovery.",
    )
    research.add_argument("package", type=Path)
    research.add_argument("--claim-id", action="append", default=[])
    research.add_argument(
        "--max-claims",
        type=int,
        default=10,
        help="Maximum claims in one traceable research cluster (default: 10).",
    )
    research.add_argument(
        "--reasoning-effort",
        choices=("low", "medium", "high"),
        default="medium",
    )
    research.set_defaults(handler=submit_research)

    research_status = commands.add_parser(
        "research-status",
        help="Refresh one asynchronous research receipt.",
    )
    research_status.add_argument("receipt", type=Path)
    research_status.set_defaults(handler=update_research_status)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        args.handler(args)
    except ConceptResearchError as error:
        print(f"Concept Research blocked: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
