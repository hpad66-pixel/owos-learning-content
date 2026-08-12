# Applied and Agentic AI Competitive Curriculum Audit

## Control record

- Audit date: 2026-08-11
- Direction: Hardeep Anand
- Curriculum authority reviewed: legacy source curriculum `M00` through `M63`
- Delivery sequence also reviewed: One Water AI Executive Fellowship `M01` through `M64`
- Status: review draft, no curriculum change approved
- Release boundary: this file recommends changes. It does not revise, renumber, approve, or release a module.

## Executive judgment

The One Water AI curriculum does not have a breadth problem. It already goes further than the four
brochures in water-sector application, data readiness, knowledge graphs, provenance, human authority,
security, procurement, professional roles, utility use cases, and governed pilot design.

The important shortfall is that several advanced subjects exist only in staff guidance, a proposed
addition, or a broad module heading. A learner, buyer, or reviewer cannot yet see enough explicit
instruction, lab work, assessment, or production evidence in those areas. The competitor programs
are narrower, but they make their technical pathway, workload, projects, tools, mentorship, and
credential evidence easier to understand.

The highest-value response is not to add another collection of disconnected modules. Keep the 64
module architecture. Add explicit lesson depth and assessed studios in the right module homes.

## How coverage was judged

The audit distinguishes four states that should not be collapsed:

- **Current:** the topic is visible in the present legacy source curriculum.
- **Blueprint only:** the detailed staff guidance expects the topic, but the current lesson heading
  does not yet make the teaching or assessment visible.
- **Proposed:** the topic is already in the governed proposal inventory but has not been approved as
  current instruction.
- **Absent:** neither curriculum line provides enough explicit treatment to teach and assess it.

This distinction matters. A topic in a planning file is not yet a lesson a learner can complete.

## Sources reviewed

| Source | File pages | Curriculum evidence used |
| --- | ---: | --- |
| MIT Professional Education, Applied AI Bundle: Generative and Agentic AI | 31 | course outcomes and outlines on PDF pages 6 to 15; delivery, tools, audience, and credential treatment on pages 16 to 25 |
| MIT Professional Education, Applied AI for Digital Transformation | 32 | course promise on page 6; objectives and outline on pages 7 to 11; application and audience treatment on pages 12 to 14 |
| Johns Hopkins University, Certificate Program in Agentic AI | 19 | program outcomes and tools on pages 5 to 6; curriculum on pages 9 to 13; faculty and delivery treatment on later pages |
| Johns Hopkins University, Certificate Program in AI and Agentic AI Engineering | 16 | program structure on pages 4 and 6; curriculum on pages 7 to 8; cases and projects on pages 9 to 10; outcomes and pedagogy on pages 11 to 12 |
| Supplied learning-path screenshot | one image | visible course sequence, course hours, Azure elective, agentic user experience, metrics, developer tools, and capstone positioning |

The brochures are marketing and curriculum-description sources, not proof that every described
capability is delivered at equal depth. For example, the MIT digital-transformation brochure names
Large Language Model Operations and reinforcement learning on page 6, but its eight-module outline
does not show a dedicated lesson for either subject.

## Granular gap register

### Priority 1: add explicit core depth

| ID | Subject | Competitor evidence | Current One Water AI position | Verdict | Recommended module homes and teaching requirement |
| --- | --- | --- | --- | --- | --- |
| AAI-01 | Production artificial intelligence lifecycle | JHU Engineering pages 6 to 11 covers Artificial Intelligence Operations, Machine Learning Operations, Large Language Model Operations, deployment, monitoring, and production operation | M05 guidance names deployment and monitoring. M40 guidance names tests, deployment, monitoring, and rollback. M43 guidance names environments, observability, resilience, and recovery. The current source headings do not expose a complete lifecycle. | Blueprint only, materially under-taught | Build one continuous lifecycle across M05, M24, M40, and M43: data and experiment, version, test, release, observe, incident, rollback, learn. Require an operations runbook and release evidence. |
| AAI-02 | Machine Learning Operations pipeline | JHU Engineering pages 8 to 10 explicitly covers pipeline architecture, continuous integration and delivery, experiment tracking, deployment strategies, version control, and reproducibility | Pieces exist in M05, M40, and M43 guidance. No current lesson explicitly teaches or assesses a model pipeline. | Partial | Add a vendor-neutral pipeline lesson in M43 and a builder lab in M40. The learner should trace a change from data and code through tests, artifact version, deployment, monitoring, and rollback. |
| AAI-03 | Large Language Model Operations and agent operations | JHU Engineering pages 8 and 11 covers production deployment, continuous evaluation, observability, security, and agentic systems | M24, M26, M31, M40, M41, and M43 collectively contain the right controls, but no visible lesson unifies them as an operating discipline. | Partial and fragmented | Add an explicit operating model linking prompt and context versions, retrieval sources, tool permissions, evaluation sets, traces, cost, incidents, and human review. Make the work product an agent operations record. |
| AAI-04 | Formal agent foundations | JHU Agentic AI page 11 covers rational agents, goal-directedness, reactivity, environment types using Performance, Environment, Actuators, Sensors, and perceived agency | M03, M06, M10, and M41 cover vocabulary, anthropomorphism, autonomy, and orchestration. The formal model of an agent in an environment is not explicit. | Partial | Add a short plain-English foundation in M41, cross-linked to M06 and M10. Learners should classify one utility task by goal, observations, actions, environment uncertainty, authority, and stop conditions. |
| AAI-05 | Agent planning patterns | JHU Agentic AI page 12 covers classical and language-model planning, chain-of-thought, Reason and Act, and agentic retrieval | M07 covers reasoning effort. M33 covers goal, plan, evidence, tools, and retry. M41 covers the loop. Specific planning patterns and their failure modes are not explicit. | Partial | Add plan-and-execute, Reason and Act, reflection, tool-use loops, and fixed-workflow comparison to M07, M33, and M41. Do not teach hidden reasoning as reliable evidence. Assess the observable plan, actions, evidence, and stop decision. |
| AAI-06 | Multi-agent coordination and failure | JHU Agentic AI page 12 covers communication, coordination, game theory basics, and language-model multi-agent systems | Legacy M41 includes multi-agent nests. Fellowship M23 and M54 are much stronger and already require handoffs, shared evidence, disagreement, synthesis, and human decision. Formal coordination, conflict, deadlock, duplicated work, and cascading failure are not explicit. | Strong blueprint, incomplete source instruction | Promote the Fellowship handoff contract and decision-room studio into the legacy teaching plan. Add coordination topology, shared-state conflict, arbitration, cost multiplication, deadlock, and failure propagation. Game theory should remain a small decision lens, not a mathematical detour. |
| AAI-07 | Human-agent interaction and agentic user experience | JHU Agentic AI page 13 covers trust and common ground. The supplied learning path includes Agentic UX Design and Transparency. | Human authority is strong in M10, M22, M24, M31, M41, M45 to M52, and the Fellowship. The interface behavior that earns calibrated trust is not a named learning job. | Material gap | Add a core lesson thread across M10, M24, M41, and role modules: visible status, source display, confidence limits, preview before action, confirmation, cancel, interrupt, correction, recovery, escalation, accessibility, and plain-language explanations. Require an agent interaction and recovery specification. |
| AAI-08 | Agent-specific evaluation | MIT Bundle pages 13 to 14 covers success metrics, sandboxing, A/B tests, safety checks, and operational risks. JHU Engineering pages 8 and 11 covers continuous evaluation and agent security. | M24 guidance is strong on accuracy, source coverage, refusal, resilience, cost, drift, and human effort. M41 adds evaluation, retry, escalation, and stop. The current M24 section headings remain general. | Strong blueprint, insufficiently explicit | Extend M24 with task success, tool-call correctness, trajectory quality, groundedness, policy compliance, refusal, recovery, latency, cost, human review effort, and regression tests. Require an evaluation dataset and failure log. |
| AAI-09 | Observability, drift, degradation, and incident response | JHU Engineering pages 8 to 11 repeatedly names monitoring, performance degradation, drift detection, observability, incident management, and reliability | M05, M24, M25, M26, M31, and M43 guidance collectively covers monitoring and recovery. The source curriculum does not show an integrated operational exercise. | Partial | Add a water-sector reliability studio. Learners inspect a change in data, retrieval source, model, prompt, tool, or environment, identify the failure signal, pause the system, and complete an incident and correction record. |
| AAI-10 | Software release discipline for AI builders | JHU Engineering pages 8 to 10 includes continuous integration and delivery, version control, reproducibility, and deployment. The supplied learning path includes Developer Tools and Product Readiness. | M40 has proposed Git, terminal, dependencies, error handling, and AI coding work. M43 has proposed live deployment, domains, authentication, and databases. Much of this remains proposed. | Proposed, not current | Approve a Builder Readiness Lab before advanced building. Require branches, pull requests, automated tests, environment separation, dependency locking, secret handling, release notes, rollback, and a reproducible build. |
| AAI-11 | Cloud foundations and managed AI platforms | JHU Engineering page 7 starts with cloud concepts and ecosystems. Its tool set includes Azure AI Studio and Amazon Bedrock. The supplied learning path includes an Azure agent course. | M42 and M43 cover hosted versus local operation and infrastructure, but not a visible vendor-neutral cloud foundation or platform comparison. | Partial | Add a vendor-neutral cloud map in M43: identity, compute, storage, networking, secrets, logs, managed model endpoints, and cost. Offer Azure, Amazon Web Services, and another platform as optional implementation labs, not as the curriculum's governing architecture. |
| AAI-12 | Content integrity, synthetic media, and disinformation | MIT Digital Transformation page 9 and MIT Bundle page 8 explicitly covers disinformation, deepfakes, and content integrity | M08 and M37 cover multimodal generation. M22, M26, M28, M31, M48, and M60 cover governance, security, regulation, provenance, public leadership, and communication. The integrity threat is not explicit. | Material gap | Add a cross-module case in M08, M22, M26, M31, M37, and M60. Require source verification, media provenance, disclosure, approval, public correction, and incident response for a false water-quality or service message. |
| AAI-13 | Explainability and transparency by decision consequence | MIT Digital Transformation page 9 asks when explainability is required for auditable AI | M22, M24, M31, and M47 provide governance, evaluation, provenance, and executive decision evidence. The difference among explanation, evidence, trace, model interpretability, and justification is not explicit. | Partial | Teach the distinction and match the explanation burden to the decision. Require the learner to state what can be explained, what can only be traced, what remains unknown, and who may approve use despite that uncertainty. |
| AAI-14 | Organizational adoption mechanics | MIT Digital Transformation page 10 covers psychological safety, Kotter, ADKAR, internal champions, the chief data and artificial intelligence roles, and an Artificial Intelligence Center of Excellence | M47, M51, and M52 are strong on readiness, executive decision rights, workforce identity, participation, support, and adoption. Named change methods, champions, and center-of-excellence operating choices are not explicit. | Partial | Keep M52's people-first stance. Add a comparison of adoption methods, champion networks, participation, training, feedback, labor and privacy boundaries, and centralized versus federated operating models. Avoid treating concern as resistance. |
| AAI-15 | Value measurement and benefit realization | MIT Bundle page 13 and Digital Transformation pages 7 and 10 emphasize key performance indicators, return, opportunity maps, business cases, and roadmaps. The supplied path names Metrics, Go-to-Market, and Return on Investment. | Legacy M12, M47, M50, and M53 and Fellowship M42, M43, M47, M48, and M62 already cover baseline, full cost, value, portfolio sequencing, go-to-market, and success criteria. | Covered, but market visibility can improve | Do not add a duplicate module. Make the measurement spine visible: baseline, target, adoption, quality, risk, cost, review effort, time to value, benefit owner, measurement frequency, and stop rule. Show a worked utility example. |

### Priority 2: add a controlled technical bridge

| ID | Subject | Competitor evidence | Current One Water AI position | Verdict | Recommendation |
| --- | --- | --- | --- | --- | --- |
| AAI-16 | Python foundation | JHU Agentic AI pages 9 to 10 covers data structures, functions, classes, libraries, and a preparatory assessment. The supplied path provides a 12-hour optional refresher. | M00 and M40 contain proposed terminal and editor work. M40 and M43 mention a Python environment. There is no coherent Python course. | Missing as structured instruction | Create an optional Builder Bridge, not a new requirement for every learner. Cover Python basics, data structures, functions, classes, packages, JavaScript Object Notation, Hypertext Transfer Protocol, application programming interfaces, notebooks, tests, and debugging. Gate it with a readiness diagnostic. |
| AAI-17 | Application programming interface practice | MIT Bundle page 12 and page 6 covers integration with tools, systems, and application programming interfaces | M41 proposes a Model Context Protocol connection lab. M43 proposes keys, authentication, a database, and deployment. | Proposed | Require a read-only water-data or document-system integration lab with explicit identity, permission, request, response, rate, error, log, and human-approval handling. |
| AAI-18 | Model Context Protocol practice | JHU Agentic AI page 11 makes the Model Context Protocol part of agent communication. The supplied path names Model Context and Tooling Protocol. | Fellowship M20 covers it explicitly. Legacy M41 has a proposed hands-on addition. | Covered in delivery line, proposed in legacy line | Keep the concept in Fellowship M20. Approve one bounded practical lab in legacy M41 after security review. Distinguish a tool connection protocol from agent-to-agent communication and from authority. |
| AAI-19 | Local models | MIT Digital Transformation page 6 mentions local lightweight models. | Legacy M42 is dedicated to open, closed, hosted, and local models, with Ollama and LM Studio proposed. | Strong coverage, proposed hands-on work | Approve a model-hosting comparison exercise. Do not promise that local operation automatically solves privacy, security, licensing, provenance, or support. |
| AAI-20 | Concrete build milestones | JHU Agentic AI pages 10, 12, and 13 uses an expense agent, research agent, and knowledge-grounded customer-support agent. JHU Engineering pages 9 to 10 uses two production projects. | The Fellowship has eight applied studios and a capstone. The legacy source line has broad build modules and use cases. | Covered architecturally, not yet built | Build three water-specific milestones: governed research assistant, read-only utility workflow agent, and evaluated multi-agent decision room. Each must show failure, correction, evidence, cost, and human authority. |

### Priority 3: elective or advanced material, not core for everyone

| ID | Subject | Competitor evidence | Current One Water AI position | Verdict | Recommendation |
| --- | --- | --- | --- | --- | --- |
| AAI-21 | Reinforcement learning and continual learning | JHU Agentic AI page 13 covers reinforcement learning, deep and verbal reinforcement learning, and lifelong learning. MIT Digital Transformation page 6 names reinforcement learning without an outlined module. | M05 and M07 explain model training and inference. The curriculum does not teach reinforcement learning as a distinct subject. | Absent | Add an advanced elective for technical learners. The core should teach the practical distinction among context, memory, feedback, retrieval, fine-tuning, and reinforcement learning, including why a production agent does not simply learn from every interaction. |
| AAI-22 | Embodied artificial intelligence and vision-language-action models | JHU Agentic AI page 13 covers simulation, embodied agents, and vision-language-action models | M08, M37, M54 to M61 cover vision, media, physical infrastructure use cases, and Decision Twins, but not embodied agents. | Absent | Add an advanced water robotics and field-systems elective. Use inspection, mobile robotics, laboratory automation, and simulation. Preserve the boundary that probabilistic artificial intelligence does not receive unreviewed operating authority. |
| AAI-23 | Game theory for multi-agent systems | JHU Agentic AI page 12 includes game theory basics | Legacy M41 and Fellowship M23 and M54 cover coordination and disagreement without game theory terminology. | Absent but low-priority | Add only the minimum needed to reason about cooperation, incentives, conflict, and shared resources. Do not turn the curriculum into a mathematical game-theory course. |
| AAI-24 | Deep technical model training | JHU Engineering includes model training, Scikit-learn, MLflow, Random Forest, and XGBoost | M05 explains the model lifecycle for decision makers. The program is not positioned as a data-science model-building certificate. | Deliberate scope difference | Offer a separate technical specialization or partner pathway. Do not dilute the One Water core with an unrelated generic machine-learning boot camp. |
| AAI-25 | Platform-specific certifications | The supplied path includes Azure and Copilot Studio electives. JHU promotes Azure AI Studio and Amazon Bedrock. | The curriculum is intentionally vendor-neutral. | Deliberate scope difference | Offer optional platform labs after the vendor-neutral architecture and governance lessons. Date every product feature and keep platform credentials separate from the One Water credential. |

## Topics that are already stronger than the brochures

These should not be duplicated merely because a competitor gives them a different title:

| Subject | Current One Water AI strength |
| --- | --- |
| Water, wastewater, stormwater, and One Water application | The competitors use cross-industry examples. One Water AI follows real utility decisions, records, assets, roles, consequences, and public accountability across the full program. |
| Data readiness | M16 and Fellowship M09 to M16 connect quality, identity, meaning, permissions, ownership, lineage, retrieval, and trusted context. |
| Knowledge graphs and shared meaning | M17 to M19 and the Fellowship treat taxonomy, ontology, graphs, relationships, and the One Water model as curriculum, not a passing tool mention. |
| Provenance and audit | M31 and Fellowship M11 and M40 require source, version, identity, transformation, approval, limitation, and correction records. |
| Human authority | M10, M22 to M31, M41, role modules, and the Fellowship make accountability, prohibited actions, escalation, and stop conditions part of design. |
| Water cybersecurity and governance | M22 to M30 includes the National Institute of Standards and Technology, International Organization for Standardization, Water Information Sharing and Analysis Center, America's Water Infrastructure Act, privacy, regulation, policy, and artificial intelligence security. |
| Procurement and vendor evaluation | M63 and Fellowship M39 and M44 cover claim evidence, architecture, data rights, total cost, acceptance, service, lock-in, exit, and build-buy-partner-stop decisions. |
| Applied professional work | The Fieldbook, 64 module work products, applied studios, governed pilot portfolio, and capstone defense are more connected to real work than three isolated generic projects. |
| Cross-role judgment | Foundation, Practitioner, and Leader views plus operators, managers, executives, elected officials, consultants, vendors, and chief officers are a clear differentiator. |
| Sustainability and public consequences | M62 explicitly addresses the water and energy footprint of artificial intelligence, which is not a visible core subject in the reviewed offerings. |

## Program-design and market-readiness gaps

The competitor advantage is often not curriculum content. It is the clarity of the offer.

| ID | Missing or unclear signal | Competitor treatment | One Water AI recommendation |
| --- | --- | --- | --- |
| PKG-01 | Entry assessment and prerequisites | JHU uses preparatory modules and Python readiness. MIT clearly states that coding is not required. | Publish a short readiness diagnostic that routes learners to Core, Builder Bridge, or advanced technical electives without making technical background a status hierarchy. |
| PKG-02 | Module-level time and workload | The brochures show program weeks, weekly hours, total hours, and screenshot course hours. | The Fellowship states 24 weeks, 5 to 6 hours per week, and about 132 hours. Add time estimates at course, module, live forum, studio, and capstone levels. Separate guided, independent, and review time. |
| PKG-03 | Visible learning modes | Competitors display recorded lessons, live sessions, masterclasses, mentorship, projects, peer groups, and support. | Name the exact rhythm for every course: self-paced lesson, live forum, studio, reviewer office hour, peer challenge, Fieldbook work, and capstone checkpoint. |
| PKG-04 | Named projects and demonstrations | JHU names three agent projects and two engineering projects. | Name and preview the three water-specific milestones and the final governed pilot. Show sample deliverables, failure evidence, and assessment rubrics. |
| PKG-05 | Tool and platform map | Competitors list tools and cloud platforms visibly. | Publish a dated tool map by job, not a logo wall: assistant, retrieval, orchestration, evaluation, observability, repository, deployment, and optional cloud platform. State what is taught conceptually versus used hands-on. |
| PKG-06 | Faculty, mentor, and reviewer roles | Competitors foreground faculty and industry mentors. | Publish the instructional team by role: curriculum authority, water practitioner, technical reviewer, evidence reviewer, graphics and learning designer, mentor, and capstone panel. Do not imply unconfirmed participation. |
| PKG-07 | Portfolio visibility | JHU promises an electronic portfolio. One Water AI has a much stronger Fieldbook and implementation portfolio, but it is not yet as easy to picture from the offer. | Show redacted specimen artifacts, the portfolio assembly map, private versus shareable evidence, revision history, and the capstone defense standard. |
| PKG-08 | Credential and continuing education evidence | MIT and JHU foreground certificates and continuing education units. | Keep credential claims disabled until approved. Complete the independent evidence, attendance, assessment, identity, completion, records, and accreditor requirements before marketing continuing education units. |
| PKG-09 | Learner support and professional community | Competitors name program managers, peer groups, forums, and alumni communities. | Define response times, office hours, progress interventions, community moderation, evidence status of peer posts, accessibility support, and post-program professional community. |
| PKG-10 | Marketable technical pathway | The supplied path makes the technical sequence obvious from Python through agents, product readiness, platform deployment, and capstone. | Display the universal One Water AI Core first, then a Builder Path and an Advanced Agent Systems elective. Keep role lenses as contextual views, not duplicate curricula. |

## Recommended teaching architecture

Do not replace the current 64-module map. Add three visible threads that run through it.

### Thread 1: Governed agent systems

M03 and M06 establish vocabulary and perceived agency. M07 and M14 teach reasoning and agentic
retrieval. M10 sets authority. M24 and M26 test and attack the system. M31 preserves evidence. M33
defines prompt, context, tools, and outputs. M41 teaches agents, planning, state, orchestration, and
multi-agent coordination. M45 to M52 translate the design across roles.

### Thread 2: Production and reliability

M05 establishes the lifecycle. M16 establishes data readiness. M24 defines evaluation. M25 and M26
define security and incident controls. M31 defines traceability. M40 teaches governed building. M42
defines model hosting choices. M43 teaches environments, release, observability, resilience, cost,
and recovery. M53 requires a production evidence package without authorizing a live operational
change.

### Thread 3: Builder Bridge and advanced electives

Use M00's readiness diagnostic to route learners. The optional Builder Bridge covers Python,
application programming interfaces, Git, testing, and cloud basics. Advanced electives cover
reinforcement learning, embodied systems, deeper multi-agent theory, and platform-specific labs.
These should not become prerequisites for the universal core.

## Recommended first change set, subject to approval

1. Make AAI-01 through AAI-13 visible in the module learning jobs, lesson outlines, work products,
   assessments, and studios.
2. Approve the Builder Bridge represented by AAI-16 through AAI-18 and the existing M00, M40, M41,
   and M43 proposals.
3. Keep AAI-21 through AAI-25 outside the universal core as advanced electives or partner pathways.
4. Implement PKG-01 through PKG-10 in the program book and Academy experience only after the
   underlying delivery commitments and credential evidence are real.
5. Do not renumber either curriculum line. Do not create 25 new modules. Use stable subsection IDs,
   cross-module threads, studios, and optional pathways.

## Decision required from Hardeep Anand

Before curriculum files change, approve, reject, or revise these four decisions:

1. Production engineering becomes an explicit assessed thread, not only background guidance.
2. Formal agent planning, multi-agent coordination, and agentic user experience become core depth.
3. Python, cloud practice, reinforcement learning, and embodied artificial intelligence remain
   optional pathways rather than universal prerequisites.
4. Program packaging work begins only where delivery, faculty, mentorship, assessment, and
   credential claims can be supported by real evidence.

