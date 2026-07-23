# Claims Register

| Claim ID | Proposed claim | Source locator | Status | Limitations | Reviewer |
| --- | --- | --- | --- | --- | --- |
| AG-001 | An agent acts for a user or system to perform tasks. | SRC-001, PDF page 2 | supported with limitation | Broad executive definition; refine with technical sources. | Codex research review |
| AG-002 | A stronger technical definition requires model-directed workflow execution, approved tool use, and guardrails. | SRC-002, What is an agent? and Agent design foundations | verified | Applies to the cited large-language-model agent pattern, not every historic software-agent taxonomy. | Codex research review |
| AG-003 | A chatbot or single model call is not automatically an agent. | SRC-002, What is an agent? | verified | A chatbot may contain an agent behind its interface. | Codex research review |
| AG-004 | Retrieval-augmented generation can provide external context to an agent but is not, by itself, an agent. | SRC-003, Building block: the augmented LLM; SRC-001, PDF pages 8-9 | verified | Retrieval may be one capability inside a broader system. | Codex research review |
| AG-005 | Workflows use predefined code paths, while agents dynamically direct their process and tool use. | SRC-003, What are agents? | verified | Industry terminology varies; teach the distinction and disclose the variation. | Codex research review |
| AG-006 | Agentic systems is a broader category that can include workflows and agents. | SRC-003, What are agents? | verified | Not a universal formal taxonomy. | Codex research review |
| AG-007 | An agent commonly operates through a loop of planning, acting, observing results, adjusting, and stopping or escalating. | SRC-001, PDF pages 3-5; SRC-002, What is an agent? | supported with limitation | Implementations vary and may combine steps. | Codex research review |
| AG-008 | Agents may use browsers, application programming interfaces, databases, files, and action tools. | SRC-001, PDF page 3; SRC-002, Defining tools | verified | Access must be authenticated, authorized, scoped, and monitored. | Codex research review |
| AG-009 | Multi-agent systems require orchestration and explicit handoffs among specialized roles. | SRC-001, PDF pages 3-5; SRC-002, Orchestration | verified | Multiple agents add cost, latency, coordination failure, and evaluation burden. | Codex research review |
| AG-010 | Guardrails should be layered and combined with authentication, authorization, access control, and human intervention. | SRC-002, Guardrails | verified | Guardrails do not guarantee safe or correct behavior. | Codex research review |
| AG-011 | High-risk or irreversible actions should trigger human oversight. | SRC-002, Plan for human intervention | verified | Risk classification must be use-case specific. | Codex research review |
| AG-012 | Agentic systems can trade latency and cost for flexibility and task performance. | SRC-003, When and when not to use agents | verified | Benefits require evaluation against a simpler deterministic alternative. | Codex research review |
| AG-013 | Agenticness should be taught as a degree of goal-directed adaptation and delegated control, not as a synonym for one software agent. | Synthesis of SRC-002 and SRC-003 | expert interpretation | Requires Hardeep approval as the course's teaching model. | pending Hardeep review |
| AG-014 | Water, wastewater, and stormwater examples should begin with advisory and administrative work rather than autonomous operational control. | Hardeep Soul boundary and course direction | Hardeep Anand position | Utility practitioner, cybersecurity, regulatory, and safety review still required. | pending Hardeep review |

Statuses: proposed, verified, supported with limitation, expert interpretation, Hardeep Anand position, unresolved, rejected.
