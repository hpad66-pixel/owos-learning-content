#!/usr/bin/env python3
"""Build role-track records and first-pass research starters for all Fellowship modules."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYLLABUS = ROOT / "SYLLABUS.md"
TRACKS_OUTPUT = ROOT / "curriculum" / "role-tracks.json"
TRACKS_MARKDOWN = ROOT / "curriculum" / "ROLE-TRACKS.md"
STARTER_DIR = ROOT / "curriculum" / "research-starters"
STARTER_INDEX = STARTER_DIR / "index.json"


COURSE_CONTEXT = {
    1: {
        "name": "AI Fluency for One Water",
        "scene": "A utility meeting stalls because the operator, finance lead, engineer, and vendor use the same AI words to mean different things.",
        "analogy": "Treat the shared vocabulary like the legend on a utility map. Without the legend, everyone sees the same lines and reaches a different conclusion.",
        "water": "A drinking-water team is deciding whether an assistant may summarize standard operating procedures or advise on a treatment change.",
        "wastewater": "A wastewater supervisor is comparing a chatbot, retrieval search, and a bounded workflow for shift reports.",
        "stormwater": "A stormwater team wants to combine rainfall, complaint, inspection, and work-order information without confusing prediction with authority.",
        "one_water": "The shared language must survive movement across drinking water, wastewater, stormwater, finance, engineering, and public accountability.",
        "visuals": ["nested circles", "governed comparison table", "spectrum", "network diagram"],
    },
    2: {
        "name": "Data, Knowledge, and Trusted Context",
        "scene": "Three systems hold three versions of the same asset, and every version looks official until someone has to make a decision.",
        "analogy": "This is like reconciling three bank statements before writing one check. The answer is not trustworthy until the records agree or the conflict is visible.",
        "water": "A drinking-water team must connect laboratory results, asset records, procedures, and sampling locations before asking for an answer.",
        "wastewater": "A wastewater team is tracing a permit question across operating logs, laboratory data, maintenance history, and the approved procedure.",
        "stormwater": "A stormwater team must reconcile map features, inspection records, rainfall events, complaints, and ownership boundaries.",
        "one_water": "Trusted context connects records, definitions, people, permissions, and evidence without erasing the authority of each domain.",
        "visuals": ["utility data estate map", "provenance network", "before and after slider", "quality heat grid"],
    },
    3: {
        "name": "Agents, Skills, and Orchestration",
        "scene": "A tool can reach the work-order system, but nobody has decided what it may read, what it may change, or when a person must step in.",
        "analogy": "An agent is closer to a new employee with a badge than a magic answer box. The badge, job description, supervisor, and stop rules matter as much as intelligence.",
        "water": "A drinking-water agent retrieves approved procedures and drafts a work package without touching supervisory control and data acquisition controls.",
        "wastewater": "A wastewater workflow assembles a shift summary, flags missing evidence, and routes the draft to the accountable supervisor.",
        "stormwater": "A stormwater workflow reviews inspection evidence, rainfall, and complaint records, then asks a person to decide the field response.",
        "one_water": "Tools and handoffs must carry purpose, evidence, identity, permissions, limitations, and human authority across organizational boundaries.",
        "visuals": ["agent loop stepper", "swimlane", "RACI grid", "failure propagation chain"],
    },
    4: {
        "name": "Utility Applications and Opportunity Design",
        "scene": "The team has twenty AI ideas and no shared way to decide which one is useful, ready, affordable, and safe enough to test.",
        "analogy": "An opportunity portfolio works like a capital improvement plan. Good ideas compete for limited money, attention, evidence, and operating capacity.",
        "water": "A drinking-water team compares advisory support for treatment, distribution, laboratory, customer, and capital decisions.",
        "wastewater": "A wastewater team compares maintenance, process, compliance, energy, and overflow opportunities against evidence and consequence.",
        "stormwater": "A stormwater team compares inspection, forecasting, complaint, asset, planning, and public-communication opportunities.",
        "one_water": "The portfolio reveals shared data and capability needs while preserving domain-specific authority and operating limits.",
        "visuals": ["2x2 opportunity matrix", "map or corridor view", "driver tree", "portfolio heat grid"],
    },
    5: {
        "name": "Governance, Security, and Human Authority",
        "scene": "A pilot gives a useful answer, but the review room cannot say who approved the sources, who checked the result, or who owns the failure.",
        "analogy": "Governance is the chain of custody for a decision. If the handoffs disappear, a polished answer has less standing than a signed field sample.",
        "water": "A drinking-water use case must protect customer, facility, laboratory, and operational information while keeping treatment authority with qualified people.",
        "wastewater": "A wastewater use case must preserve permit evidence, operator authority, cyber boundaries, and incident escalation.",
        "stormwater": "A stormwater use case must separate public records, sensitive infrastructure, predictive uncertainty, field verification, and enforcement authority.",
        "one_water": "Controls follow the decision and the consequence, not the excitement surrounding the technology.",
        "visuals": ["risk matrix", "authority swimlane", "permission grid", "provenance network"],
    },
    6: {
        "name": "Strategy, Economics, and Organizational Change",
        "scene": "A pilot looks inexpensive because the budget counts the model and ignores integration, data cleanup, human review, security, support, and failure.",
        "analogy": "Buying the model is like buying a pump without counting the station, power, controls, maintenance, permits, and people who keep it running.",
        "water": "A drinking-water organization builds an investment case that connects service, risk, operating effort, capital, and public responsibility.",
        "wastewater": "A wastewater organization sequences data, process, workforce, security, and application investments instead of funding isolated demonstrations.",
        "stormwater": "A stormwater program builds a practical roadmap across planning, field work, engineering, grants, regulation, and public communication.",
        "one_water": "The operating model connects decision rights, funding, capability, evidence, and adoption across the entire utility system.",
        "visuals": ["total-cost iceberg", "tornado sensitivity chart", "roadmap", "operating-model RACI"],
    },
    7: {
        "name": "Applied AI Studios",
        "scene": "The demonstration works once in a clean room, then fails when the source is stale, the tool times out, or the user asks an unexpected question.",
        "analogy": "A studio is the wet test of the system. A drawing can look perfect, but the water still has to move through the pipe under pressure.",
        "water": "A drinking-water studio tests a bounded source-grounded task with approved documents and human review.",
        "wastewater": "A wastewater studio tests tool use, failure, retry, and escalation against a realistic shift or maintenance task.",
        "stormwater": "A stormwater studio tests mixed documents, maps, event data, and field evidence without overstating prediction quality.",
        "one_water": "The studio rewards visible evidence, failure, correction, and a useful work product rather than a theatrical demo.",
        "visuals": ["test stepper", "before and after comparison", "failure fishbone", "evaluation dashboard"],
    },
    8: {
        "name": "Capstone: From Opportunity to Governed Pilot",
        "scene": "Leadership likes the idea but cannot yet see the baseline, owner, controls, test cases, cost limits, stop conditions, or decision date.",
        "analogy": "A capstone is a pilot brief, not a wish list. It should read like a flight plan with a destination, instruments, crew, fuel limit, alternate landing, and authority to stop.",
        "water": "A drinking-water pilot protects operating authority while testing one measurable task against historical cases.",
        "wastewater": "A wastewater pilot connects the current process, approved evidence, accountable roles, failure response, and measurable result.",
        "stormwater": "A stormwater pilot makes data gaps, seasonal variation, field verification, public consequence, and funding limits visible.",
        "one_water": "The defended pilot shows how operations, data, engineering, finance, governance, workforce, and leadership reach one accountable decision.",
        "visuals": ["phase-gate roadmap", "architecture stack", "control matrix", "measurement scorecard"],
    },
}


TRACK_SPECS = [
    {
        "id": "administrator",
        "title": "Administrator",
        "audience": "Administrative professionals coordinating records, meetings, correspondence, approvals, procurement, and service workflows.",
        "promise": "Use AI to reduce repeat work while preserving the official record, the approval path, and the person accountable for the decision.",
        "required": [1, 3, 6, 9, 10, 11, 20, 22, 28, 31, 34, 36, 37, 40, 49, 57],
        "elective": [21, 32, 38, 45, 46, 63],
        "portfolio": ["administrative workflow map", "records and approval checklist", "bounded assistant specification"],
        "profile": "Shows that the learner can connect service, records, privacy, approvals, and AI-assisted work without confusing speed with authority.",
        "bridge": "Operations supplies the context, finance supplies the controls, information technology supplies access, and administration keeps the institutional record intact.",
        "headline": "Make the work move without losing the record.",
        "cta": "Build your governed administrative workflow",
    },
    {
        "id": "clerk-records",
        "title": "Clerk and Records Professional",
        "audience": "Clerks, records coordinators, public-records staff, board support, document-control professionals, and customer correspondence teams.",
        "promise": "Turn scattered documents into findable, traceable knowledge while protecting retention, privacy, legal holds, and the official version.",
        "required": [1, 6, 9, 10, 11, 12, 13, 15, 16, 22, 28, 31, 34, 40, 50, 59],
        "elective": [7, 20, 21, 27, 36, 38],
        "portfolio": ["record lineage trace", "retention-aware retrieval brief", "public-record response control card"],
        "profile": "Shows skill in provenance, classification, retrieval, privacy, retention, and source-backed communication.",
        "bridge": "The clerk connects the person asking the question to the record that can support the answer and the authority that may release it.",
        "headline": "Make the official record findable, explainable, and defensible.",
        "cta": "Design your trusted records workflow",
    },
    {
        "id": "finance-executive",
        "title": "Finance Executive and Chief Financial Officer",
        "audience": "Chief financial officers, finance directors, controllers, treasurers, and executives responsible for financial capacity and accountability.",
        "promise": "Connect operating evidence, capital needs, risk, cost, rates, procurement, and AI investment into decisions leadership can defend.",
        "required": [1, 9, 11, 13, 24, 29, 31, 32, 39, 41, 42, 43, 44, 47, 48, 62],
        "elective": [26, 30, 45, 46, 63, 64],
        "portfolio": ["AI total-cost model", "investment decision record", "one-year finance and capability roadmap"],
        "profile": "Shows the ability to price the complete system, challenge unsupported value claims, and connect utility outcomes to financial choices.",
        "bridge": "Finance translates operating and engineering need into affordability, sequence, risk, and public accountability.",
        "headline": "Know the full cost before the pilot becomes a program.",
        "cta": "Build the financial case for useful AI",
    },
    {
        "id": "budget-capital-finance",
        "title": "Budget and Capital Finance Professional",
        "audience": "Budget analysts, capital planners, grant professionals, rate analysts, financial analysts, and program-control staff.",
        "promise": "Use connected evidence to compare need, timing, affordability, risk, funding, and measurable benefit across operating and capital portfolios.",
        "required": [9, 10, 11, 13, 26, 29, 31, 32, 41, 42, 43, 44, 47, 58, 62, 63],
        "elective": [25, 27, 30, 39, 45, 48],
        "portfolio": ["value baseline", "portfolio prioritization model", "funding and measurement plan"],
        "profile": "Shows practical command of evidence, assumptions, sensitivity, portfolio comparison, and fiscal controls.",
        "bridge": "Budget professionals make the connection between a field problem, a measurable baseline, a funding path, and the evidence needed to keep the investment alive.",
        "headline": "Connect every dollar to evidence, consequence, and a decision date.",
        "cta": "Build a measurable AI investment portfolio",
    },
    {
        "id": "c-suite",
        "title": "C-Suite and General Management",
        "audience": "General managers, executive directors, deputies, chief operating officers, and enterprise leaders.",
        "promise": "Lead a cross-functional AI program that connects utility purpose, human authority, data readiness, risk, economics, workforce, and public trust.",
        "required": [1, 5, 8, 13, 16, 24, 30, 32, 33, 37, 40, 41, 43, 45, 47, 48, 64],
        "elective": [22, 29, 39, 44, 46, 63],
        "portfolio": ["executive AI decision field card", "operating-model canvas", "one-year organizational roadmap"],
        "profile": "Shows that the learner can convene specialists, ask the right questions, preserve authority, and make a staged investment decision.",
        "bridge": "The executive track teaches enough of every discipline to keep specialists connected without pretending the executive replaces them.",
        "headline": "Lead the system, not the demonstration.",
        "cta": "Build your One Water AI operating model",
    },
    {
        "id": "elected-public-leader",
        "title": "Elected Official and Public Leader",
        "audience": "Mayors, council members, commissioners, board members, public administrators, and policy leaders.",
        "promise": "Understand what AI can support, what it cannot decide, how public money and data are protected, and what questions responsible leadership must ask.",
        "required": [1, 2, 5, 8, 13, 24, 28, 30, 32, 33, 34, 37, 39, 43, 48, 64],
        "elective": [27, 29, 31, 44, 46, 63],
        "portfolio": ["public AI question card", "governance review record", "constituent-facing decision brief"],
        "profile": "Shows public leadership grounded in evidence, limits, fiscal responsibility, equity, transparency, and human authority.",
        "bridge": "Elected officials do not need to become engineers. They need to understand the connections among service, evidence, cost, risk, people, and accountability.",
        "headline": "Ask better questions before public systems buy or use AI.",
        "cta": "Build your public leadership AI brief",
    },
    {
        "id": "vendor-solution-provider",
        "title": "Vendor and Solution Provider",
        "audience": "Technology vendors, software companies, integrators, product leaders, sales engineers, and service providers working with utilities.",
        "promise": "Understand the utility buyer, operating environment, evidence burden, procurement path, integration limits, and proof required to earn trust.",
        "required": [1, 5, 9, 13, 20, 24, 25, 30, 31, 32, 33, 35, 39, 43, 44, 50, 63],
        "elective": [27, 28, 29, 45, 55, 56],
        "portfolio": ["utility value and evidence brief", "integration and authority boundary", "procurement-ready proof package"],
        "profile": "Shows that the learner can speak utility, disclose limits, design for governance, and sell proof instead of generic promises.",
        "bridge": "The vendor sees how operations, security, procurement, finance, engineering, and public accountability shape one buying decision.",
        "headline": "Earn utility trust by showing the work.",
        "cta": "Build a procurement-ready utility offer",
    },
    {
        "id": "consultant-advisor",
        "title": "Consultant and Advisor",
        "audience": "Management consultants, engineering consultants, strategic advisors, program managers, and independent specialists.",
        "promise": "Frame problems, connect disciplines, preserve source and authority boundaries, and help clients move from idea to governed pilot.",
        "required": [1, 6, 9, 11, 13, 16, 20, 24, 29, 30, 32, 37, 39, 41, 44, 45, 57, 64],
        "elective": [21, 23, 35, 43, 48, 63],
        "portfolio": ["cross-functional diagnosis", "opportunity and risk portfolio", "governed pilot advisory package"],
        "profile": "Shows that the learner can synthesize without hiding disagreement, unsupported claims, or client decision rights.",
        "bridge": "The consultant connects specialists while keeping the client as the accountable owner of the decision.",
        "headline": "Turn advice into a traceable path from problem to pilot.",
        "cta": "Build your governed advisory method",
    },
    {
        "id": "engineer-capital-delivery",
        "title": "Engineer and Capital-Delivery Professional",
        "audience": "Engineers, project managers, program managers, construction professionals, asset managers, and technical reviewers.",
        "promise": "Connect requirements, assets, models, records, risk, cost, schedule, change, and decision history across the life of a project.",
        "required": [1, 9, 10, 11, 13, 20, 24, 26, 29, 30, 32, 35, 38, 41, 42, 52, 58, 60],
        "elective": [18, 19, 27, 43, 55, 61],
        "portfolio": ["engineering evidence chain", "capital-delivery opportunity card", "architecture and control decision"],
        "profile": "Shows command of connected requirements, evidence, tradeoffs, tool boundaries, and professional responsibility.",
        "bridge": "Engineering connects physical reality to records, models, money, procurement, operations, and long-term service.",
        "headline": "Connect the drawing, the field, the record, and the decision.",
        "cta": "Build your AI-assisted delivery control",
    },
    {
        "id": "planner-strategist",
        "title": "Planner and Program Strategist",
        "audience": "Utility planners, master planners, resilience planners, capital planners, program strategists, and policy analysts.",
        "promise": "Connect future demand, assets, risk, communities, finance, data, engineering, operations, and uncertainty into defensible choices.",
        "required": [1, 9, 10, 11, 13, 16, 24, 29, 30, 32, 41, 42, 43, 47, 48, 58, 59, 63],
        "elective": [25, 27, 28, 44, 57, 61],
        "portfolio": ["One Water relationship map", "scenario and evidence register", "sequenced program roadmap"],
        "profile": "Shows the ability to use AI without hiding uncertainty, distributional effects, dependencies, or the source of a forecast.",
        "bridge": "Planning is where operations, engineering, finance, policy, community need, and future uncertainty must become one visible argument.",
        "headline": "Plan the connected system, with uncertainty left visible.",
        "cta": "Build your evidence-backed One Water roadmap",
    },
    {
        "id": "operator-maintenance",
        "title": "Operator and Maintenance Professional",
        "audience": "Operators, maintainers, supervisors, reliability staff, field technicians, and operations managers.",
        "promise": "Use AI as bounded support for finding knowledge, recognizing exceptions, preparing work, and preserving experience while qualified people remain in control.",
        "required": [1, 3, 5, 6, 8, 9, 10, 15, 20, 22, 24, 25, 26, 27, 30, 35, 37, 49, 55],
        "elective": [18, 21, 46, 50, 52, 53],
        "portfolio": ["operator support boundary card", "knowledge-capture workflow", "failure and escalation log"],
        "profile": "Shows practical judgment about usefulness, source quality, tool permissions, failure, and the line between advice and control.",
        "bridge": "Operators connect the physical system to the records and decisions that everyone else depends on.",
        "headline": "Keep the person who knows the system in control of the system.",
        "cta": "Build a bounded operator-support workflow",
    },
    {
        "id": "builder-product-creator",
        "title": "Builder and Product Creator",
        "audience": "People with ideas who want to build useful tools, prototypes, products, workflows, and companies for the water sector.",
        "promise": "Move from idea to a working, testable, governed product without skipping the user, data, evidence, security, economics, or operating reality.",
        "required": [1, 3, 5, 6, 7, 9, 13, 15, 17, 18, 19, 20, 21, 24, 32, 35, 41, 43, 44, 49, 50, 51, 52, 53, 55, 56, 60],
        "elective": [22, 23, 29, 38, 42, 63],
        "portfolio": ["product problem brief", "working prototype evidence package", "90-day governed product pilot"],
        "profile": "Shows that the learner can build, test, break, price, explain, and govern a useful product in a consequential sector.",
        "bridge": "The builder learns enough operations, engineering, data, governance, finance, and procurement to stop building in a vacuum.",
        "headline": "Build the thing, then prove it belongs in the real system.",
        "cta": "Turn your water-sector idea into a governed pilot",
    },
    {
        "id": "cio-ciso-caio",
        "title": "Chief Information, Security, and AI Officer",
        "audience": "Chief information officers, chief information security officers, chief AI officers, technology directors, data leaders, and enterprise architects.",
        "promise": "Connect architecture, identity, security, data, model, vendor, governance, operating authority, cost, and organizational adoption.",
        "required": [1, 5, 9, 10, 11, 13, 16, 19, 20, 22, 23, 24, 33, 34, 35, 36, 37, 38, 39, 40, 43, 45, 47, 60, 61],
        "elective": [15, 18, 21, 42, 55, 63],
        "portfolio": ["enterprise AI architecture record", "identity and permission matrix", "governed AI operating model"],
        "profile": "Shows the ability to make technical and governance decisions that respect utility operations and executive accountability.",
        "bridge": "This track translates between the people who run the system, the people who secure it, the people who fund it, and the people who answer to the public.",
        "headline": "Connect the technology decision to the utility consequence.",
        "cta": "Build your governed enterprise AI architecture",
    },
    {
        "id": "data-governance-assurance",
        "title": "Data, Governance, Privacy, and Assurance Professional",
        "audience": "Data stewards, governance leads, privacy professionals, auditors, risk leaders, compliance professionals, and evaluation teams.",
        "promise": "Make sources, definitions, identity, permissions, quality, evaluation, retention, decisions, and correction visible from beginning to end.",
        "required": [1, 9, 10, 11, 12, 13, 14, 15, 16, 22, 24, 27, 33, 34, 35, 36, 37, 38, 39, 40, 50, 55, 59, 61],
        "elective": [20, 23, 28, 31, 45, 63],
        "portfolio": ["data and knowledge readiness map", "evaluation and control plan", "governed application record"],
        "profile": "Shows that the learner can make trust testable through evidence, control ownership, traceability, and correction.",
        "bridge": "Assurance connects the source to the answer, the answer to the decision, and the decision to the person responsible for it.",
        "headline": "Make trust visible enough to test.",
        "cta": "Build your AI evidence and control record",
    },
    {
        "id": "one-water-cross-functional",
        "title": "Cross-Functional One Water Leader",
        "audience": "Leaders whose work crosses drinking water, wastewater, stormwater, watershed, planning, finance, community, and technology boundaries.",
        "promise": "See the entire connected system, understand what each profession protects, and lead shared decisions without flattening expertise or authority.",
        "required": [1, 5, 8, 9, 11, 13, 16, 20, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 37, 40, 45, 47, 48, 54, 57, 64],
        "elective": [26, 34, 39, 43, 46, 61],
        "portfolio": ["One Water system relationship map", "cross-role decision record", "shared 90-day pilot charter"],
        "profile": "Shows the ability to make relationships visible, preserve domain authority, and organize a shared response around evidence and public purpose.",
        "bridge": "This is the track for understanding everybody without pretending to become everybody.",
        "headline": "See the connected system and keep every accountable voice in the room.",
        "cta": "Build your cross-functional One Water decision map",
    },
]


def parse_modules() -> list[dict[str, object]]:
    text = SYLLABUS.read_text(encoding="utf-8")
    course_matches = list(re.finditer(r"^## Course (\d+): (.+)$", text, re.MULTILINE))
    modules: list[dict[str, object]] = []
    for index, course_match in enumerate(course_matches):
        course_number = int(course_match.group(1))
        end = course_matches[index + 1].start() if index + 1 < len(course_matches) else len(text)
        section = text[course_match.start():end]
        for line in section.splitlines():
            match = re.match(r"\|\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", line)
            if not match:
                continue
            modules.append({
                "id": f"fellowship:M{int(match.group(1)):02d}",
                "code": f"M{int(match.group(1))}",
                "number": int(match.group(1)),
                "title": match.group(2).strip(),
                "learningJob": match.group(3).strip(),
                "appliedResult": match.group(4).strip(),
                "courseNumber": course_number,
                "courseTitle": course_match.group(2).strip(),
            })
    if len(modules) != 64:
        raise ValueError(f"Expected 64 Fellowship modules, found {len(modules)}")
    return modules


def research_prompt(module: dict[str, object], context: dict[str, object]) -> str:
    return f"""You are the research team for One Water AI Academy. Prepare the governed research brief for {module['code']}: {module['title']}.

The learner must be able to {str(module['learningJob']).lower()}. The professional work product is: {module['appliedResult']}.

Research this module in the context of United States drinking water, wastewater, stormwater, and cross-functional One Water work. Begin with the real decisions people make, the records they use, the systems they touch, the people affected, and the consequence of getting the answer wrong. Do not begin with technology.

Deliver:
1. A plain-English explanation for an intelligent learner who is new to the topic.
2. One drinking-water case, one wastewater case, and one stormwater case. Label invented cases as instructional scenarios.
3. The Foundation, Practitioner, and Leader views. Show how the question and responsibility change by role.
4. A relationship map connecting data, knowledge, operations, planning, engineering, finance, governance, security, procurement, workforce, products, and public accountability where applicable.
5. A source table using current United States primary authorities, official guidance, standards adopted for the course, and qualified research. Give exact locators, dates, applicability, and limitations.
6. A claim register separating sourced fact, expert interpretation, Hardeep Anand position, instructional scenario, and unresolved question.
7. Four diagram candidates selected by the natural shape of the idea. For each, state what the learner should be able to explain after reading it, the interaction, accessible text, and mobile behavior.
8. At least six likely novice questions and direct plain-English answers to research further.
9. Failure cases, counterexamples, edge conditions, and what the system must refuse or send to a human.
10. A proposed applied exercise that produces the {module['appliedResult']} and can be assessed deterministically.
11. Open questions for a utility practitioner, technical reviewer, evidence reviewer, and novice learner.
12. A short recommendation explaining what belongs in this module, what belongs elsewhere, and what should be left out.

Evidence boundaries:
- Use United States governing authorities for water-sector requirements.
- Do not treat a vendor page as independent proof of performance.
- Do not copy confidential utility data into research tools.
- Do not claim that artificial intelligence operates or decides autonomously.
- Keep named product features, prices, regulations, and standards dated and verified.
- If a claim cannot be supported, label it unresolved instead of filling the gap.

Use this framing while researching:
- Drinking water: {context['water']}
- Wastewater: {context['wastewater']}
- Stormwater: {context['stormwater']}
- One Water: {context['one_water']}
"""


def starter_markdown(module: dict[str, object]) -> str:
    context = COURSE_CONTEXT[int(module["courseNumber"])]
    starter_id = f"RS-F{int(module['number']):02d}"
    visuals = context["visuals"]
    module_slug = re.sub(r"[^a-z0-9]+", "-", str(module["title"]).lower()).strip("-")
    repo_path = f"curriculum/research-starters/fellowship-m{int(module['number']):02d}-{module_slug}.md"
    prompt = research_prompt(module, context)
    return f"""# {starter_id}: {module['code']} {module['title']}

## Control record

- Research starter ID: `{starter_id}`
- Curriculum ID: `{module['id']}`
- Course: {module['courseNumber']}. {module['courseTitle']}
- Status: proposed research starter
- Repository path: `{repo_path}`
- Source authority: `SYLLABUS.md`
- Owner: unassigned
- Contributor: Hardeep Anand direction, structured by APAS Academy Studio
- Reviewer: unassigned
- Revision: 1
- Release boundary: This is a research blueprint, not approved learner-facing instruction.

## Why this module exists

The learner's job is to {str(module['learningJob']).lower()}. The practical result is a usable
**{module['appliedResult']}**. This matters because {context['scene'].lower()}

## The scene

{context['scene']}

The research should follow the decision from the first question through the records, systems,
people, review, and resulting work product. It should show what changes when the same question moves
from a drinking-water plant to a wastewater facility, a stormwater program, or a One Water planning
table.

## The analogy

{context['analogy']}

The analogy is an opening bridge. The final lesson must return to actual utility work and must not
let the analogy replace technical explanation.

## Four water-sector frames

### Drinking water

{context['water']}

### Wastewater

{context['wastewater']}

### Stormwater

{context['stormwater']}

### One Water

{context['one_water']}

## Connections the research must make

- **Data and knowledge:** Which records, definitions, identifiers, sources, dates, and limitations
  determine whether the answer can be trusted?
- **Operations:** What is happening in the physical system, and which qualified person retains
  operating authority?
- **Planning and engineering:** What requirements, assets, assumptions, models, alternatives, and
  decision history shape the work?
- **Finance and procurement:** What baseline, full cost, contract, funding, lock-in, and exit
  questions matter?
- **Governance and security:** Who may ask, read, recommend, approve, write, administer, stop, and
  investigate?
- **Products and adoption:** Who is the user, what problem is being solved, what must fit existing
  work, and what evidence would justify continued investment?
- **People and professional growth:** What can the learner show in a portfolio that proves judgment,
  collaboration, technical fluency, and responsibility?

## Role questions

- **Foundation:** What does the term mean, what does it not mean, and what simple utility example
  makes the distinction clear?
- **Practitioner:** How would someone use this in a real task, check the result, record the evidence,
  and respond when it fails?
- **Leader:** What decision, investment, authority, risk, workforce, and public-accountability
  questions must be settled before scaling?
- **Cross-role:** What does the operator need the engineer, finance lead, administrator, technology
  lead, vendor, and executive to understand, and what does each need in return?

## Proposed work product

Build a **{module['appliedResult']}** that names the problem, user, approved evidence, assumptions,
roles, limits, review steps, decision, and next accountable action. The artifact should be useful in
a real meeting after the course.

## Diagram direction

| Teaching job | Candidate | Learner conclusion | Interaction |
| --- | --- | --- | --- |
| Show the core mechanism | {visuals[0]} | Explain how {module['title'].lower()} changes a utility decision. | Step, select, or reveal the mechanism. |
| Show the handoffs | {visuals[1]} | Identify where evidence, authority, or meaning can be lost between roles. | Highlight one role or handoff at a time. |
| Show the tradeoff | {visuals[2]} | Compare value, readiness, consequence, and control without hiding uncertainty. | Change one input and observe the decision effect. |
| Show operating status | {visuals[3]} | State what is ready, what is weak, and what must happen next. | Filter by drinking water, wastewater, stormwater, or One Water. |

```mermaid
flowchart LR
    A[Utility situation] --> B[{module['title']}]
    B --> C[Evidence and limitations]
    C --> D[Role decision and human authority]
    D --> E[{module['appliedResult']}]
    E --> F[Review, learning, and next action]
```

The final design brief must run the Visual Arsenal selection process and may replace these candidates
when the research reveals a better natural shape.

## Research prompt

```text
{prompt.rstrip()}
```

## Required review

- Evidence reviewer verifies source quality, exact locators, dates, and applicability.
- Utility practitioner checks the scenes, decisions, artifacts, and professional consequences.
- Technical reviewer checks architecture, data, security, evaluation, and failure claims.
- Novice learner identifies unexplained terms, missing steps, and confusing assumptions.
- Hardeep Anand approves the blueprint before learner-facing production begins.
"""


def build_tracks(modules: list[dict[str, object]]) -> list[dict[str, object]]:
    module_ids = {int(module["number"]): str(module["id"]) for module in modules}
    tracks = []
    for spec in TRACK_SPECS:
        required = [module_ids[number] for number in spec["required"]]
        elective = [module_ids[number] for number in spec["elective"] if number not in spec["required"]]
        tracks.append({
            "id": spec["id"],
            "title": spec["title"],
            "audience": spec["audience"],
            "promise": spec["promise"],
            "requiredModuleIds": required,
            "electiveModuleIds": elective,
            "portfolioEvidence": spec["portfolio"],
            "professionalProfile": spec["profile"],
            "crossRoleBridge": spec["bridge"],
            "landingPage": {
                "eyebrow": "One Water AI role track",
                "headline": spec["headline"],
                "subhead": spec["promise"],
                "primaryCta": spec["cta"],
                "proofNeeded": ["approved module outcomes", "sample work product", "named instructor or reviewer", "verified learner result"],
                "objections": ["I am not technical", "I do not have time", "Our data is not ready", "AI cannot make this decision for me"],
                "channels": ["onewater.ai", "onewater.foundation", "email", "LinkedIn", "partner briefing"],
            },
            "status": "proposed",
            "owner": "",
            "reviewer": "",
            "revision": 1,
        })
    return tracks


def main() -> None:
    modules = parse_modules()
    STARTER_DIR.mkdir(parents=True, exist_ok=True)
    starter_records = []
    for module in modules:
        slug = re.sub(r"[^a-z0-9]+", "-", str(module["title"]).lower()).strip("-")
        filename = f"fellowship-m{int(module['number']):02d}-{slug}.md"
        path = STARTER_DIR / filename
        text = starter_markdown(module)
        path.write_text(text, encoding="utf-8")
        starter_records.append({
            "id": f"RS-F{int(module['number']):02d}",
            "moduleId": module["id"],
            "moduleCode": module["code"],
            "moduleTitle": module["title"],
            "courseNumber": module["courseNumber"],
            "courseTitle": module["courseTitle"],
            "learningJob": module["learningJob"],
            "appliedResult": module["appliedResult"],
            "path": str(path.relative_to(ROOT)),
            "markdown": text,
            "status": "proposed",
            "revision": 1,
        })
    STARTER_INDEX.write_text(json.dumps({
        "schema": "owos-module-research-starters/v1",
        "generated": "2026-08-05",
        "authority": "First-pass research blueprints. Not approved learner-facing lessons.",
        "moduleCount": len(starter_records),
        "items": starter_records,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    tracks = build_tracks(modules)
    TRACKS_OUTPUT.write_text(json.dumps({
        "schema": "owos-role-tracks/v1",
        "generated": "2026-08-05",
        "authority": "Tracks are governed views over shared modules. They do not duplicate or approve curriculum.",
        "trackCount": len(tracks),
        "tracks": tracks,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    module_lookup = {module["id"]: module for module in modules}
    lines = [
        "# One Water AI Role Tracks",
        "",
        "These tracks organize one shared 64-module curriculum around the decisions, work products, and professional growth of different roles. A track is a governed view, not a copied course.",
        "",
    ]
    for track in tracks:
        lines.extend([
            f"## {track['title']}",
            "",
            track["promise"],
            "",
            f"**Audience:** {track['audience']}",
            "",
            f"**Cross-role bridge:** {track['crossRoleBridge']}",
            "",
            "### Required sequence",
            "",
        ])
        lines.extend(
            f"- {module_lookup[module_id]['code']}: {module_lookup[module_id]['title']}"
            for module_id in track["requiredModuleIds"]
        )
        lines.extend(["", "### Portfolio evidence", ""])
        lines.extend(f"- {item}" for item in track["portfolioEvidence"])
        lines.extend([
            "",
            "### Landing-page starting point",
            "",
            f"**{track['landingPage']['headline']}**",
            "",
            track["landingPage"]["subhead"],
            "",
            f"Call to action: {track['landingPage']['primaryCta']}",
            "",
        ])
    TRACKS_MARKDOWN.write_text("\n".join(lines), encoding="utf-8")
    print(f"Built {len(starter_records)} research starters and {len(tracks)} role tracks")


if __name__ == "__main__":
    main()
