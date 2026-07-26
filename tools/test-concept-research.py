#!/usr/bin/env python3
"""Regression checks for secure OWOS Perplexity research wiring."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from concept_research import (
    POLICY_VERSION,
    Credential,
    PerplexityClient,
    idempotency_key,
    parse_env_file,
    redact,
    request_body,
    resolve_credential,
    response_request_id,
    select_claims,
    write_receipt,
)


SECRET = "pplx-test-secret-that-must-never-leak"


with tempfile.TemporaryDirectory() as directory:
    env_file = Path(directory) / ".env.local"
    env_file.write_text(
        "# local only\nexport PERPLEXITY_API_KEY='file-secret'\n",
        encoding="utf-8",
    )
    if parse_env_file(env_file)["PERPLEXITY_API_KEY"] != "file-secret":
        raise AssertionError("local secret parser did not recover the configured key")

    keychain = resolve_credential(
        environ={"PERPLEXITY_API_KEY": "environment-secret"},
        local_secret_file=env_file,
        keychain_reader=lambda: "keychain-secret",
    )
    if keychain.source != "macOS Keychain" or keychain.value != "keychain-secret":
        raise AssertionError("macOS Keychain did not take precedence")

    environment = resolve_credential(
        environ={"PERPLEXITY_API_KEY": "environment-secret"},
        local_secret_file=env_file,
        keychain_reader=lambda: None,
    )
    if environment.source != "environment":
        raise AssertionError("deployment environment secret did not resolve")

    local = resolve_credential(
        environ={},
        local_secret_file=env_file,
        keychain_reader=lambda: None,
    )
    if local.value != "file-secret":
        raise AssertionError("git-ignored local fallback did not resolve")


safe = redact(
    {"header": f"Bearer {SECRET}", "nested": [f"failure: {SECRET}"]},
    (SECRET,),
)
if SECRET in json.dumps(safe):
    raise AssertionError("recursive redaction leaked the Perplexity key")


brief = {
    "brief_id": "owos:concept-brief:test",
    "version": "0.1.0",
    "title": "A water concept",
}
claims = [
    {
        "claim_id": "claim-test",
        "claim_type": "technical_standard",
        "claim_text": "A material technical proposition.",
        "scope": "United States",
        "jurisdiction": "United States",
        "limitations": "Requires verification.",
    }
]
body = request_body(brief, claims, "medium")
prompt = body["request"]["messages"][0]["content"]
for required in (
    "United States authorities only",
    "Do not use non-United States regulations",
    "Search deliberately for contrary evidence",
    "Do not report a claim as verified",
):
    if required not in prompt:
        raise AssertionError(f"research policy prompt is missing: {required}")
if body["request"]["model"] != "sonar-deep-research":
    raise AssertionError("research request did not select Sonar Deep Research")
if idempotency_key(brief, claims, body) != idempotency_key(brief, claims, body):
    raise AssertionError("research idempotency key is not deterministic")

selection_fixture = claims + [
    {
        "claim_id": "claim-rejected",
        "claim_type": "sourced_fact",
        "claim_text": "A rejected historical proposition.",
        "verification_status": "rejected",
    },
    {
        "claim_id": "claim-pending",
        "claim_type": "sourced_fact",
        "claim_text": "A pending proposition.",
        "verification_status": "pending",
    },
]
claims[0]["verification_status"] = "pending"
selected_ids = {
    claim["claim_id"] for claim in select_claims(selection_fixture, [], max_claims=10)
}
if "claim-rejected" in selected_ids or "claim-pending" not in selected_ids:
    raise AssertionError("default research selection did not isolate pending material claims")


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return None

    def read(self):
        return b'{"id":"async-test-001","status":"CREATED"}'


captured = {}


def fake_opener(request, timeout):
    captured["authorization"] = request.headers.get("Authorization")
    captured["idempotency"] = request.headers.get("Idempotency-key")
    captured["timeout"] = timeout
    return FakeResponse()


client = PerplexityClient(Credential(SECRET, "test"), opener=fake_opener)
response = client.submit(body, "stable-idempotency")
if response_request_id(response) != "async-test-001":
    raise AssertionError("asynchronous request ID did not resolve")
if captured["authorization"] != f"Bearer {SECRET}":
    raise AssertionError("API authorization header was not attached in memory")
if captured["idempotency"] != "stable-idempotency":
    raise AssertionError("API idempotency header was not attached")


with tempfile.TemporaryDirectory() as directory:
    receipt = Path(directory) / "receipt.json"
    write_receipt(
        receipt,
        {
            "schema": POLICY_VERSION,
            "authorization": f"Bearer {SECRET}",
            "response": response,
        },
        (SECRET,),
    )
    receipt_text = receipt.read_text(encoding="utf-8")
    if SECRET in receipt_text or "[REDACTED]" not in receipt_text:
        raise AssertionError("research receipt did not redact the key")
    if os.stat(receipt).st_mode & 0o077:
        raise AssertionError("research receipt permissions are broader than owner-only")


print(
    "OWOS Concept Research QA passed: one-time credential resolution, United States evidence "
    "policy, deterministic async requests, secret redaction, and owner-only receipts are enforced."
)
