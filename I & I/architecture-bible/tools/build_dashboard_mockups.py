#!/usr/bin/env python3
"""Build populated PumpOS and I&I dashboard mockups from the traceability manifest."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

import yaml


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
MOCKUP_DIR = PACKAGE / "dashboard-mockups"
SCREENSHOT_DIR = MOCKUP_DIR / "screenshots"
MANIFEST_PATH = PACKAGE / "operationalization-manifest.yaml"


VIEWS = [
    {
        "id": "fleet",
        "number": "DASH-01",
        "title": "Fleet Command Center",
        "question": "Which basin, station, or decision needs attention first?",
        "metric_ids": ["M-07", "M-10", "M-14", "M-21", "M-29", "M-32"],
        "decision_ids": ["DEC-02", "DEC-03", "DEC-06"],
        "screenshot": "01-fleet-command-center.png",
    },
    {
        "id": "basin",
        "number": "DASH-02",
        "title": "Basin and I&I Workspace",
        "question": "What did the event produce, and how was that conclusion calculated?",
        "metric_ids": [f"M-{index:02d}" for index in range(1, 11)],
        "decision_ids": ["DEC-01", "DEC-02"],
        "screenshot": "02-basin-and-ii-workspace.png",
    },
    {
        "id": "station",
        "number": "DASH-03",
        "title": "Station Hydraulics and Resiliency",
        "question": "Can the station convey the event under normal and contingency conditions?",
        "metric_ids": [f"M-{index:02d}" for index in range(10, 22)],
        "decision_ids": ["DEC-03"],
        "screenshot": "03-station-hydraulics-resiliency.png",
    },
    {
        "id": "operations",
        "number": "DASH-04",
        "title": "Operations, Cycling, and Energy",
        "question": "What operating burden did the flow create?",
        "metric_ids": [f"M-{index:02d}" for index in range(22, 27)],
        "decision_ids": ["DEC-04", "DEC-05"],
        "screenshot": "04-operations-cycling-energy.png",
    },
    {
        "id": "economics",
        "number": "DASH-05",
        "title": "Program and Economics Workspace",
        "question": "Does the stated rehabilitation scenario justify further development?",
        "metric_ids": [f"M-{index:02d}" for index in range(27, 35)],
        "decision_ids": ["DEC-06"],
        "screenshot": "05-program-economics.png",
    },
    {
        "id": "manuals",
        "number": "DASH-06",
        "title": "Asset and Manual Compliance",
        "question": "Which approved requirement applies to the asset, and what evidence is due?",
        "metric_ids": ["M-22", "M-23", "M-25"],
        "decision_ids": ["DEC-04"],
        "screenshot": "06-asset-manual-compliance.png",
    },
    {
        "id": "gaps",
        "number": "DASH-07",
        "title": "Data Gap Center",
        "question": "What missing contract prevents a result from becoming production-authoritative?",
        "metric_ids": ["M-10", "M-11", "M-18", "M-23", "M-27", "M-29"],
        "decision_ids": ["DEC-02", "DEC-03", "DEC-04", "DEC-06"],
        "screenshot": "07-data-gap-center.png",
    },
    {
        "id": "actions",
        "number": "DASH-08",
        "title": "Action and Approval Center",
        "question": "What decision is proposed, who must approve it, and what evidence supports it?",
        "metric_ids": ["M-08", "M-14", "M-18", "M-20", "M-21", "M-32"],
        "decision_ids": ["DEC-02", "DEC-03", "DEC-06"],
        "screenshot": "08-action-approval-center.png",
    },
    {
        "id": "lineage",
        "number": "DASH-09",
        "title": "Calculation Lineage Explorer",
        "question": "Can every displayed number be traced to its accepted source and calculation?",
        "metric_ids": [f"M-{index:02d}" for index in range(1, 35)],
        "decision_ids": [f"DEC-{index:02d}" for index in range(1, 7)],
        "screenshot": "09-calculation-lineage-explorer.png",
    },
]


def load_manifest() -> dict[str, Any]:
    return yaml.safe_load(MANIFEST_PATH.read_text())


def public_metric(metric: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": metric["id"],
        "number": metric["number"],
        "dashboard": metric["dashboard"],
        "label": metric["label"],
        "value": metric["sample_display"],
        "path": metric["result_path"],
        "sources": metric["source_classes"],
        "formulas": metric["formula_ids"],
        "evidence": metric["evidence_class"],
        "importance": metric["importance"],
        "decisionUse": metric["decision_use"],
    }


def build_html(manifest: dict[str, Any]) -> str:
    payload = {
        "metrics": [public_metric(item) for item in manifest["dashboard_metrics"]],
        "decisions": manifest["decision_bindings"],
        "gaps": manifest["lineage_gaps"],
        "views": VIEWS,
    }
    data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f"""<div id="ii-dashboard-prototype" class="ii-shell">
  <header class="ii-topbar">
    <div>
      <p class="ii-eyebrow">PUMPOS / I&amp;I INTELLIGENCE / WORKED DATASET MD-EX-01</p>
      <h1 id="view-title">Fleet Command Center</h1>
      <p id="view-question" class="ii-question">Which basin, station, or decision needs attention first?</p>
    </div>
    <div class="ii-state">
      <span class="ii-state-dot" aria-hidden="true"></span>
      <span>Illustrative calculation run</span>
      <code>RUN-MD-EX-01</code>
    </div>
  </header>

  <nav class="ii-tabs" aria-label="Dashboard mockups" id="dashboard-tabs"></nav>

  <main>
    <section class="ii-context" aria-label="Analysis context">
      <span><strong>Basin</strong> MD-EX-01</span>
      <span><strong>Station</strong> PS-EX-01</span>
      <span><strong>Event</strong> EVT-SYNTH-3.20</span>
      <span><strong>Registry</strong> 0.2.0</span>
      <span><strong>State</strong> Candidate, not production-authoritative</span>
    </section>

    <section id="view-body" class="ii-view" aria-live="polite"></section>

    <section class="ii-lineage-panel" aria-labelledby="trace-title">
      <div class="ii-lineage-head">
        <div>
          <p class="ii-eyebrow">WHY THIS NUMBER?</p>
          <h2 id="trace-title">Select any numbered value</h2>
        </div>
        <span id="trace-evidence" class="ii-chip">Evidence class</span>
      </div>
      <div id="trace-body" class="ii-trace-grid">
        <p>Each metric opens its exact source class, formula chain, result path, use, and boundary.</p>
      </div>
    </section>
  </main>

  <footer>
    Every displayed value is illustrative and comes from the governed sample result. Dashboard
    rounding is presentation only. Downstream calculations use stored full-precision values.
  </footer>
</div>

<style>
  #ii-dashboard-prototype {{
    --g: #1c1b19;
    --c: #292826;
    --c2: #302f2c;
    --process: #10232e;
    --white: #f2f1ec;
    --body: #d9d6cf;
    --muted: #a29c91;
    --water: #7dc6e8;
    --amber: #e0a64a;
    --green: #4ac88c;
    --red: #ee7968;
    color: var(--white);
    background: var(--g);
    font-family: Arial, Barlow, sans-serif;
    padding: 24px;
    min-height: 920px;
  }}
  #ii-dashboard-prototype * {{ box-sizing: border-box; }}
  .ii-topbar {{
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-start;
    border-bottom: 1px solid #4b4944;
    padding-bottom: 18px;
  }}
  .ii-eyebrow {{
    margin: 0 0 7px;
    color: var(--water);
    font: 500 12px/1.4 "Courier New", monospace;
    letter-spacing: .08em;
  }}
  .ii-topbar h1, .ii-lineage-head h2 {{
    margin: 0;
    color: var(--white);
  }}
  .ii-topbar h1 {{ font-size: 30px; line-height: 1.1; }}
  .ii-question {{ margin: 8px 0 0; color: var(--body); }}
  .ii-state {{
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 5px 9px;
    align-items: center;
    color: var(--body);
    font-size: 13px;
    text-align: right;
  }}
  .ii-state code {{ grid-column: 2; color: var(--muted); }}
  .ii-state-dot {{
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--amber);
  }}
  .ii-tabs {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 18px 0;
  }}
  .ii-tab {{
    appearance: none;
    border: 1px solid #56534e;
    background: transparent;
    color: var(--body);
    padding: 9px 12px;
    border-radius: 5px;
    cursor: pointer;
    font-weight: 500;
  }}
  .ii-tab[aria-selected="true"] {{
    color: #10232e;
    background: var(--water);
    border-color: var(--water);
  }}
  .ii-context {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px 18px;
    padding: 11px 14px;
    background: var(--process);
    border-left: 3px solid var(--water);
    color: var(--body);
    font: 400 12px/1.5 "Courier New", monospace;
  }}
  .ii-view {{ padding: 20px 0; }}
  .ii-kpis {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
  }}
  .ii-metric {{
    appearance: none;
    width: 100%;
    min-height: 132px;
    text-align: left;
    color: var(--white);
    background: var(--c);
    border: 1px solid #4b4944;
    border-radius: 7px;
    padding: 14px;
    cursor: pointer;
  }}
  .ii-metric:hover, .ii-metric:focus-visible {{
    border-color: var(--water);
    outline: 2px solid transparent;
  }}
  .ii-metric.is-selected {{ border-color: var(--water); box-shadow: inset 3px 0 var(--water); }}
  .ii-metric-top {{ display: flex; justify-content: space-between; gap: 10px; }}
  .ii-number {{
    color: var(--water);
    font: 500 12px/1.4 "Courier New", monospace;
  }}
  .ii-evidence {{
    color: var(--muted);
    font: 400 11px/1.4 "Courier New", monospace;
    text-align: right;
  }}
  .ii-value {{
    display: block;
    margin: 14px 0 8px;
    font-size: 25px;
    line-height: 1.1;
    font-weight: 500;
  }}
  .ii-value.long {{ font-size: 17px; line-height: 1.3; color: var(--amber); }}
  .ii-label {{ display: block; color: var(--body); font-size: 13px; line-height: 1.35; }}
  .ii-band {{
    margin-top: 16px;
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 14px;
  }}
  .ii-process, .ii-decisions, .ii-special {{
    background: var(--process);
    border: 1px solid #28414e;
    border-radius: 7px;
    padding: 15px;
  }}
  .ii-process h3, .ii-decisions h3, .ii-special h3 {{ margin: 0 0 11px; font-size: 15px; }}
  .ii-flow {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    align-items: stretch;
    gap: 7px;
  }}
  .ii-flow span {{
    padding: 11px 8px;
    background: #1c303b;
    border-bottom: 2px solid var(--water);
    color: var(--body);
    font-size: 12px;
    text-align: center;
  }}
  .ii-decision {{
    padding: 9px 0;
    border-top: 1px solid #3d505a;
    color: var(--body);
    font-size: 12px;
  }}
  .ii-decision:first-of-type {{ border-top: 0; }}
  .ii-decision strong {{ color: var(--white); }}
  .ii-chip {{
    display: inline-block;
    padding: 4px 7px;
    border-radius: 999px;
    background: #27414e;
    color: var(--water);
    font: 500 11px/1.3 "Courier New", monospace;
  }}
  .ii-lineage-panel {{
    margin-top: 2px;
    background: var(--c2);
    border-top: 3px solid var(--water);
    padding: 17px;
  }}
  .ii-lineage-head {{ display: flex; justify-content: space-between; gap: 16px; }}
  .ii-lineage-head h2 {{ font-size: 20px; }}
  .ii-trace-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
    margin-top: 14px;
  }}
  .ii-trace-item {{
    min-width: 0;
    border-top: 1px solid #56534e;
    padding-top: 9px;
  }}
  .ii-trace-item strong {{
    display: block;
    margin-bottom: 4px;
    color: var(--muted);
    font: 500 11px/1.4 "Courier New", monospace;
    text-transform: uppercase;
  }}
  .ii-trace-item span, .ii-trace-item code {{
    color: var(--body);
    font-size: 12px;
    overflow-wrap: anywhere;
  }}
  .ii-table-wrap {{ overflow-x: auto; border-top: 1px solid #56534e; }}
  .ii-table {{ width: 100%; border-collapse: collapse; font-size: 11px; }}
  .ii-table th, .ii-table td {{
    padding: 8px 7px;
    text-align: left;
    border-bottom: 1px solid #45433f;
    vertical-align: top;
  }}
  .ii-table th {{ color: var(--water); font-family: "Courier New", monospace; }}
  .ii-table td {{ color: var(--body); }}
  .ii-table button {{
    border: 0;
    background: transparent;
    color: var(--water);
    cursor: pointer;
    padding: 0;
    font: inherit;
  }}
  .ii-gap-list {{ display: grid; gap: 8px; }}
  .ii-gap {{
    display: grid;
    grid-template-columns: 90px 90px 1fr;
    gap: 10px;
    padding: 10px 0;
    border-top: 1px solid #3d505a;
    color: var(--body);
    font-size: 12px;
  }}
  .ii-gap code {{ color: var(--amber); }}
  .ii-manual {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    margin-top: 16px;
  }}
  .ii-manual p {{ color: var(--body); margin: 8px 0; font-size: 12px; }}
  .ii-manual strong {{ color: var(--white); }}
  footer {{
    margin-top: 16px;
    color: var(--muted);
    font-size: 11px;
    line-height: 1.5;
  }}
  @media (max-width: 760px) {{
    #ii-dashboard-prototype {{ padding: 15px; min-height: 0; }}
    .ii-topbar, .ii-lineage-head {{ display: block; }}
    .ii-state {{ margin-top: 14px; text-align: left; grid-template-columns: auto 1fr; }}
    .ii-kpis {{ grid-template-columns: 1fr; }}
    .ii-band, .ii-manual {{ grid-template-columns: 1fr; }}
    .ii-flow {{ grid-template-columns: 1fr; }}
    .ii-trace-grid {{ grid-template-columns: 1fr; }}
  }}
</style>

<script>
(() => {{
  const root = document.getElementById("ii-dashboard-prototype");
  const data = {data_json};
  const metricMap = Object.fromEntries(data.metrics.map(metric => [metric.id, metric]));
  const decisionMap = Object.fromEntries(data.decisions.map(decision => [decision.id, decision]));
  const tabs = root.querySelector("#dashboard-tabs");
  const body = root.querySelector("#view-body");
  const title = root.querySelector("#view-title");
  const question = root.querySelector("#view-question");

  const esc = value => String(value).replace(/[&<>"']/g, char => ({{
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }}[char]));

  function metricButton(metric) {{
    const longClass = metric.value.length > 22 ? " long" : "";
    return `<button class="ii-metric" type="button" data-metric="${{esc(metric.id)}}">
      <span class="ii-metric-top">
        <span class="ii-number">${{esc(metric.id)}} / #${{metric.number}}</span>
        <span class="ii-evidence">${{esc(metric.evidence.replaceAll("_", " "))}}</span>
      </span>
      <span class="ii-value${{longClass}}">${{esc(metric.value)}}</span>
      <span class="ii-label">${{esc(metric.label)}}</span>
    </button>`;
  }}

  function decisionBlock(ids) {{
    return ids.map(id => {{
      const item = decisionMap[id];
      return `<div class="ii-decision">
        <strong>${{esc(item.id)}} ${{esc(item.name)}}</strong><br>
        Uses ${{item.metric_ids.map(esc).join(", ")}}<br>
        Output: <code>${{esc(item.output)}}</code>
      </div>`;
    }}).join("");
  }}

  function standardView(view) {{
    const metrics = view.metric_ids.map(id => metricMap[id]).filter(Boolean);
    return `<div class="ii-kpis">${{metrics.map(metricButton).join("")}}</div>
      <div class="ii-band">
        <section class="ii-process">
          <h3>Evidence-to-decision flow</h3>
          <div class="ii-flow">
            <span>Accepted source</span><span>Normalized input</span><span>Versioned formula</span>
            <span>Numbered result</span><span>Reviewed decision</span>
          </div>
        </section>
        <section class="ii-decisions">
          <h3>Decisions supported</h3>
          ${{decisionBlock(view.decision_ids)}}
        </section>
      </div>`;
  }}

  function manualView(view) {{
    return standardView(view) + `<div class="ii-manual">
      <section class="ii-special">
        <h3>Applicable documents</h3>
        <p><strong>M-44 Rev C</strong> Approved for pump P-17A</p>
        <p><strong>IB-12</strong> Installation bulletin, approved</p>
        <p><strong>M-44 Rev B</strong> Superseded, historical only</p>
        <p><strong>PS-MAINT-08</strong> Utility procedure, approved</p>
      </section>
      <section class="ii-special">
        <h3>Requirement and evidence state</h3>
        <p><strong>Seal inspection</strong> Due in 60 runtime hours</p>
        <p><strong>Starts review</strong> ${{metricMap["M-22"].value}}</p>
        <p><strong>Event energy</strong> ${{metricMap["M-23"].value}}</p>
        <p><strong>Vibration record</strong> Data gap, acquisition required</p>
      </section>
    </div>`;
  }}

  function gapView(view) {{
    return standardView(view) + `<section class="ii-special" style="margin-top:16px">
      <h3>Visible formula-contract gaps</h3>
      <div class="ii-gap-list">${{data.gaps.map(gap => `<div class="ii-gap">
        <code>${{esc(gap.id)}}</code>
        <span>${{gap.metric_ids.map(esc).join(", ")}}</span>
        <span>${{esc(gap.missing_contract)}} <strong>Required:</strong> ${{esc(gap.required_resolution)}}</span>
      </div>`).join("")}}</div>
    </section>`;
  }}

  function actionView(view) {{
    return standardView(view) + `<div class="ii-manual">
      <section class="ii-special">
        <h3>Draft action A-220</h3>
        <p><strong>Basis:</strong> ${{metricMap["M-18"].value}} derated storage shortfall,
        ${{metricMap["M-20"].value}} outage shortfall, and ${{metricMap["M-21"].value}} time to exhaustion.</p>
        <p><strong>Proposed:</strong> Verify pump availability, usable storage, and high-flow metering.</p>
        <p><strong>Authority:</strong> Draft only. No equipment command is authorized.</p>
      </section>
      <section class="ii-special">
        <h3>Approval state</h3>
        <p><strong>Requested by:</strong> Operations supervisor</p>
        <p><strong>Required reviewers:</strong> Pump-station engineer and operations supervisor</p>
        <p><strong>Current state:</strong> Awaiting named human approval</p>
        <p><strong>Completion evidence:</strong> Inspection record, meter check, wet-well verification</p>
      </section>
    </div>`;
  }}

  function lineageView() {{
    return `<div class="ii-table-wrap"><table class="ii-table">
      <thead><tr><th>ID</th><th>Displayed value</th><th>Result path</th><th>Sources</th><th>Formula chain</th></tr></thead>
      <tbody>${{data.metrics.map(metric => `<tr>
        <td><button type="button" data-metric="${{esc(metric.id)}}">${{esc(metric.id)}}</button></td>
        <td><strong>${{esc(metric.value)}}</strong><br>${{esc(metric.label)}}</td>
        <td><code>${{esc(metric.path)}}</code></td>
        <td>${{metric.sources.map(esc).join(", ")}}</td>
        <td>${{metric.formulas.length ? metric.formulas.map(esc).join(" → ") : "Direct accepted input"}}</td>
      </tr>`).join("")}}</tbody>
    </table></div>`;
  }}

  function showTrace(metricId) {{
    const metric = metricMap[metricId];
    if (!metric) return;
    root.querySelectorAll("[data-metric]").forEach(node =>
      node.classList.toggle("is-selected", node.dataset.metric === metricId)
    );
    root.querySelector("#trace-title").textContent = `${{metric.id}} / #${{metric.number}} ${{metric.label}}`;
    root.querySelector("#trace-evidence").textContent = metric.evidence.replaceAll("_", " ");
    root.querySelector("#trace-body").innerHTML = `
      <div class="ii-trace-item"><strong>Displayed value</strong><span>${{esc(metric.value)}}</span></div>
      <div class="ii-trace-item"><strong>Exact result path</strong><code>${{esc(metric.path)}}</code></div>
      <div class="ii-trace-item"><strong>Source classes</strong><span>${{metric.sources.map(esc).join(", ")}}</span></div>
      <div class="ii-trace-item"><strong>Formula chain</strong><span>${{metric.formulas.length ? metric.formulas.map(esc).join(" → ") : "Direct accepted input"}}</span></div>
      <div class="ii-trace-item"><strong>Why it matters</strong><span>${{esc(metric.importance)}}</span></div>
      <div class="ii-trace-item"><strong>Decision boundary</strong><span>${{esc(metric.decisionUse)}}</span></div>`;
  }}

  function render(viewId) {{
    const view = data.views.find(item => item.id === viewId) || data.views[0];
    title.textContent = `${{view.number}}. ${{view.title}}`;
    question.textContent = view.question;
    tabs.querySelectorAll("button").forEach(button =>
      button.setAttribute("aria-selected", button.dataset.view === view.id ? "true" : "false")
    );
    if (view.id === "lineage") body.innerHTML = lineageView();
    else if (view.id === "manuals") body.innerHTML = manualView(view);
    else if (view.id === "gaps") body.innerHTML = gapView(view);
    else if (view.id === "actions") body.innerHTML = actionView(view);
    else body.innerHTML = standardView(view);
    body.querySelectorAll("[data-metric]").forEach(button =>
      button.addEventListener("click", () => showTrace(button.dataset.metric))
    );
    showTrace(view.metric_ids[0]);
    location.hash = view.id;
  }}

  tabs.innerHTML = data.views.map(view =>
    `<button class="ii-tab" type="button" data-view="${{esc(view.id)}}" aria-selected="false">${{esc(view.number)}}</button>`
  ).join("");
  tabs.querySelectorAll("button").forEach(button =>
    button.addEventListener("click", () => render(button.dataset.view))
  );
  render(location.hash.slice(1) || "fleet");
}})();
</script>
"""


def metric_table(metrics: list[dict[str, Any]]) -> str:
    rows = [
        "| Dashboard number | Worked value | Result path | Source class | Formula chain |",
        "| --- | --- | --- | --- | --- |",
    ]
    for metric in metrics:
        formulas = " -> ".join(metric["formula_ids"]) or "Direct accepted input"
        rows.append(
            f"| `{metric['id']}` / #{metric['number']} {metric['label']} | "
            f"**{metric['sample_display']}** | `{metric['result_path']}` | "
            f"{', '.join(metric['source_classes'])} | {formulas} |"
        )
    return "\n".join(rows)


def build_markdown(manifest: dict[str, Any]) -> str:
    metric_map = {item["id"]: item for item in manifest["dashboard_metrics"]}
    decision_map = {item["id"]: item for item in manifest["decision_bindings"]}
    out = [
        "# Part VII. Fully populated dashboard mockups",
        "",
        "This section shows the actual dashboard compositions that were missing from the earlier candidate. "
        "Every numbered value is populated from sample calculation run `RUN-MD-EX-01`. "
        "The screenshots and interactive prototype are development mockups, not evidence that these screens are implemented in PumpOS.",
        "",
        "## How to read every mockup",
        "",
        "Each visible `M-##` identifier is the stable dashboard metric identifier. Selecting that value in "
        "the prototype opens its displayed value, exact result path, source class, formula chain, importance, "
        "and decision boundary. The screens use rounded display values, while calculation dependencies consume "
        "stored full-precision results.",
        "",
        "The standalone prototype is stored at "
        "[`dashboard-mockups/index.html`](dashboard-mockups/index.html).",
        "",
    ]
    for view in VIEWS:
        metrics = [metric_map[mid] for mid in view["metric_ids"]]
        out.extend(
            [
                f"## {view['number']}. {view['title']}",
                "",
                f"**Decision question:** {view['question']}",
                "",
                f"![{view['title']} populated with the MD-EX-01 worked values]"
                f"(dashboard-mockups/screenshots/{view['screenshot']})",
                "",
                "### Values displayed and their wiring",
                "",
                metric_table(metrics),
                "",
                "### Decisions supported",
                "",
            ]
        )
        for decision_id in view["decision_ids"]:
            decision = decision_map[decision_id]
            out.append(
                f"- `{decision_id}` {decision['name']}: consumes "
                f"{', '.join(decision['metric_ids'])}; requires "
                f"{', '.join(decision['required_roles'])}; produces "
                f"`{decision['output']}`."
            )
        out.extend(
            [
                "",
                "### What this screen does not establish",
                "",
                "This mockup demonstrates information architecture and traceability using illustrative sample "
                "data. It does not approve the event, certify station capacity, establish regulatory compliance, "
                "authorize a project, or prove that the screen exists in the current PumpOS production build.",
                "",
            ]
        )

    out.extend(
        [
            "## Dashboard coverage statement",
            "",
            "The nine mockups collectively display all 34 numbered metrics. The lineage explorer displays the "
            "entire set in one auditable table. The other eight screens organize the same values around the "
            "operational questions that a fleet manager, I&I analyst, station engineer, asset manager, compliance "
            "reviewer, finance reviewer, and approving authority must answer.",
            "",
        ]
    )
    return "\n".join(line.rstrip() for line in out) + "\n"


def build() -> list[Path]:
    manifest = load_manifest()
    MOCKUP_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    html_path = MOCKUP_DIR / "index.html"
    markdown_path = PACKAGE / "dashboard-mockups.md"
    html_path.write_text(build_html(manifest))
    markdown_path.write_text(build_markdown(manifest))
    return [html_path, markdown_path]


if __name__ == "__main__":
    for path in build():
        print(path)
