# INT-002 Technical Foundations Integration Matrix

## Decision summary

All 56 topics supplied by Shreya have a stable ID, source page, primary curriculum home, coverage decision, matched curriculum IDs, and governed next action.

- Already done exactly in the current curriculum: 20
- Already planned exactly in an existing proposal: 7
- Partially covered and marked for expansion: 18
- New governed additions: 11

Already planned does not mean already taught. New and expanded items remain proposals until evidence review and blueprint approval.

## Item-by-item placement

| ID | Shreya's topic | Decision | Primary home | Existing match | Integration action |
| --- | --- | --- | --- | --- | --- |
| STF-001 | Version control and GitHub | Already planned exactly | M40 | M40.P02, M53.P01 | Retain the existing Git and GitHub proposal and record Shreya as an independent reinforcing contributor. |
| STF-002 | Environment variables and secrets | Already planned exactly | M00 | M00.P02, M25.P01, M27.P01, M40.P03, M43.P01 | Retain the existing API key and .env proposal and attach Shreya's reinforcement. |
| STF-003 | APIs, endpoints, and API keys | New addition | M39 | M38, M41 | Add an API literacy foundation before learners wire connectors, webhooks, or MCP tools. |
| STF-004 | Localhost, servers, and ports | Already planned exactly | M39 | M39.P02, M40.P07, M43.P04 | Retain the existing web app and localhost proposal and attach Shreya's reinforcement. |
| STF-005 | Development, test, staging, and production environments | Already planned exactly | M43 | M43.P05f | Keep the existing deployment subtopic and expand its exercise into promotion gates and no-testing-in-production behavior. |
| STF-006 | Cloud, hosting, SaaS, and on-premises | Partially covered, expand | M43 | M42, M43, M27 | Add a plain-language deployment-location decision model covering ownership, residency, control, and operating responsibility. |
| STF-007 | JSON, YAML, CSV, and Markdown | New addition | M00 | M16.P01, M34 | Add a file-format field guide and a small identify, open, edit, and validate exercise. |
| STF-008 | Command line and terminal | Already planned exactly | M00 | M00.P01, M40.P01 | Retain the existing terminal proposal and attach Shreya's reinforcement. |
| STF-009 | Database basics, SQL, and NoSQL | Partially covered, expand | M16 | M15, M18, M43.P08 | Add a relational and non-relational database primer before vector and graph databases. |
| STF-010 | Authentication and authorization | Partially covered, expand | M25 | M27, M43.P08 | Add an identity foundation that distinguishes who you are from what you may do, then connect keys, OAuth, SSO, and roles. |
| STF-011 | HTTP, HTTPS, URLs, and encryption | Partially covered, expand | M25 | M43.P07, M27 | Add basic web request and encryption-in-transit versus encryption-at-rest literacy. |
| STF-012 | Integrations, connectors, and webhooks | Partially covered, expand | M38 | M38.P01l, M41 | Make system-to-system events, payloads, credentials, and failure handling explicit before MCP practice. |
| STF-013 | Packages, dependencies, and versions | Already planned exactly | M40 | M40.P05, M43.P02 | Retain the existing dependency-install proposal and attach Shreya's reinforcement. |
| STF-014 | Logs and audit trails | Partially covered, expand | M31 | M31, M25 | Distinguish operational logs, security logs, model traces, and governance audit records, including retention and access. |
| STF-015 | Rate limits, quotas, and token billing | Already planned exactly | M43 | M00.P02h, M32.P05, M43.P03, M43.P06 | Retain the existing cost and API proposals and attach Shreya's reinforcement. |
| STF-016 | Deploy, release, and rollback | Partially covered, expand | M43 | M43.P05 | Expand deployment into versioned release, health check, rollback trigger, rollback execution, and decision record. |
| STF-017 | Structured and unstructured data | Partially covered, expand | M16 | M13, M16 | Add an explicit classification exercise because data shape determines ingestion, retrieval, validation, and storage. |
| STF-018 | Hosted model API versus self-hosted model | Partially covered, expand | M42 | M42, M43 | Add a side-by-side architecture and governance decision table for API-hosted and self-hosted inference. |
| STF-019 | CPU versus GPU | Partially covered, expand | M43 | M43, M62 | Add a non-engineer compute primer tied to workload, latency, cost, energy, and hosting choices. |
| STF-020 | IP addresses, DNS, firewalls, and VPNs | Partially covered, expand | M43 | M25, M43.P07 | Expand the domain lesson into a connectivity diagnostic for utility IT and OT boundaries. |
| STF-021 | Data pipelines and ETL | Already done exactly | M16 | M16.04, M19, M25 | Already taught. Preserve Shreya's input as confirmation and link it to the existing data pipeline treatment. |
| STF-022 | Batch versus real-time and streaming processing | New addition | M16 | M54, M57, M61 | Add an architecture decision lesson using overnight reporting and live SCADA examples. |
| STF-023 | Latency and throughput | New addition | M43 | M54, M57 | Add performance vocabulary and a simple workload sizing exercise. |
| STF-024 | Monitoring, metrics, and alerts | Partially covered, expand | M24 | M24, M25, M31 | Extend evaluation into day-two operational monitoring, alert ownership, drift, and service health. |
| STF-025 | Timeouts, retries, and failure modes | New addition | M41 | M26, M53 | Add resilient tool and agent behavior, including bounded retries, idempotency, graceful failure, and human escalation. |
| STF-026 | Testing basics and why AI testing differs | Already done exactly | M24 | M24 | Already taught through evaluation sets, metrics, scoring, and continuous assurance. Use Shreya's framing as an entry bridge from software testing. |
| STF-027 | Backups, restore, and retention | Partially covered, expand | M31 | M27, M31 | Add restore testing, recovery objectives, retention windows, and ownership to the governed record treatment. |
| STF-028 | Data classification and PII | Already done exactly | M27 | M21, M27 | Already taught. Preserve Shreya's input as confirmation and emphasize hands-on classification practice. |
| STF-029 | Open source, proprietary software, and licensing | Partially covered, expand | M42 | M42, M63 | Add license obligations, model and data licenses, commercial-use limits, support, lock-in, and procurement checks. |
| STF-030 | Caching and stale data | Partially covered, expand | M43 | M14, M32.P05k, M43.P03k | Expand beyond prompt caching to browser, application, retrieval, and data caches, with freshness controls. |
| STF-031 | Containers and Docker | Already done exactly | M43 | M43, M43.P05c | Already taught and practiced in the infrastructure and deployment module. |
| STF-032 | Frontend versus backend | New addition | M39 | M39.P08i, M43.P08i | Add a browser, server, API, database, and trust-boundary diagram before learners build a web application. |
| STF-033 | Sandboxing and least privilege | Already done exactly | M25 | M25, M26 | Already taught as a core AI security principle. Add Shreya as reinforcing contributor. |
| STF-034 | Data validation and schemas | Partially covered, expand | M16 | M16, M18 | Add required fields, types, formats, constraints, validation failures, and schema evolution before SHACL. |
| STF-035 | Entity resolution and deduplication | Already done exactly | M17 | M17, M20, M16.P02e | Already taught as identity resolution and reinforced in the spreadsheet cleanup proposal. |
| STF-036 | Time-series data | Partially covered, expand | M16 | M54, M55, M56, M57, M58, M61 | Add the foundational properties of timestamped operational data before lifecycle applications use it. |
| STF-037 | GIS and geospatial data | New addition | M16 | M19, M54, M57, M58 | Add coordinate systems, layers, shapes, GeoJSON, spatial joins, and map-data governance for utility use cases. |
| STF-038 | Hashing and checksums | New addition | M31 | M31 | Add a tamper-evidence lab that hashes a file, changes it, and verifies the checksum no longer matches. |
| STF-039 | File and object storage versus databases | New addition | M16 | M13, M15, M18 | Add a storage-selection primer for documents, tabular records, vectors, and graph relationships. |
| STF-040 | Load, scaling, and uptime | Already done exactly | M43 | M43 | Already taught in the infrastructure and deployment module. Link the production-readiness decision to explicit service objectives. |
| STF-041 | Cloud and GPU providers | Already done exactly | M43 | M43 | Already taught through infrastructure, DigitalOcean, deployment, and model hosting. Treat named providers as dated examples, not endorsements. |
| STF-042 | Graph databases | Already done exactly | M18 | M17, M18 | Already taught in the knowledge graph machinery module, including Neo4j and GraphDB. |
| STF-043 | What a model is | Already done exactly | M02 | M02, M03, M04 | Already taught across the foundational mental-model sequence. |
| STF-044 | Training versus inference | Already done exactly | M05 | M04, M05 | Already taught in how a model is made and how it produces an answer. |
| STF-045 | Hallucination and confident wrongness | Already done exactly | M06 | M06, M13, M24, M31 | Already taught throughout trust, retrieval, evaluation, and provenance. |
| STF-046 | Knowledge cutoff | Already done exactly | M13 | M13 | Already taught explicitly as a reason retrieval and source grounding are needed. |
| STF-047 | Temperature and randomness | Already done exactly | M03 | M03, M04 | Already taught explicitly in the AI lexicon and inference explanation. |
| STF-048 | Prompting versus RAG versus fine-tuning | Already done exactly | M35 | M13, M35 | Already taught as a dedicated decision framework. |
| STF-049 | Bias in AI | Already done exactly | M22 | M22, M27, M60 | Already taught in responsible AI, governance, privacy, and equity contexts. |
| STF-050 | Unreliable math and counting, and tool use | New addition | M41 | M24, M41 | Add a calculator and database tool-use exercise that separates language generation from deterministic computation. |
| STF-051 | Structured model output | New addition | M41 | M38, M41 | Add schema-constrained JSON output, validation, repair, and refusal handling as the bridge from chat to integration. |
| STF-052 | Vendor data use, retention, and prompt privacy | Already done exactly | M27 | M27, M63 | Already taught in data privacy and vendor evaluation. Preserve the exact executive question as a practical checklist prompt. |
| STF-053 | Model guardrails and application controls | Partially covered, expand | M26 | M22, M26, M30 | Make the boundary explicit between provider refusals and application-owned input filters, output checks, permissions, and human gates. |
| STF-054 | Evals and evaluation metrics | Already done exactly | M24 | M24 | Already taught in a dedicated module, including precision, recall, false positives, and false negatives. |
| STF-055 | Model families and sizes | Already done exactly | M32 | M32.P05, M43.P03 | Already covered in the current model landscape and exactly planned as a cost, latency, and capability selection exercise. |
| STF-056 | System prompt | Already done exactly | M33 | M03, M33 | Already taught as the standing role and rules behind user instructions and expanded in prompt engineering. |

## Attribution and change control

Shreya remains the source contributor on all 56 records. Where her topic duplicates existing curriculum, the original curriculum authorship is not reassigned; her contribution is recorded as independent reinforcement. Any later change must retain the stable STF ID, editor identity, timestamp, revision number, decision note, and source link.

## Release boundary

Curriculum review input. It does not approve learner-facing publication. Technical claims and named vendor examples require evidence review before release.
