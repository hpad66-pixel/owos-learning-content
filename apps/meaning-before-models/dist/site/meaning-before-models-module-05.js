(() => {
  "use strict";

  const storageKey = "mbm001:module-05:v1";
  const required = [
    "opening", "matching", "sorter", "flow", "ordering", "failure",
    "myths", "context", "raci", "artifact", "applied"
  ];
  const state = readState();
  let playTimer = null;
  let processIndex = 0;
  let lastDrawerTrigger = null;
  let activeCommunityFilter = "all";

  function readState() {
    try {
      return JSON.parse(localStorage.getItem(storageKey)) || { done: {}, artifact: {}, replies: {}, bookmarks: {} };
    } catch {
      return { done: {}, artifact: {}, replies: {}, bookmarks: {} };
    }
  }

  function saveState() {
    localStorage.setItem(storageKey, JSON.stringify(state));
  }

  function setFeedback(root, message, good) {
    const box = root.querySelector(".feedback");
    if (!box) return;
    box.textContent = message;
    box.className = `feedback show ${good ? "good" : "bad"}`;
  }

  function markDone(name) {
    state.done[name] = true;
    saveState();
    renderCompletion();
  }

  function renderCompletion() {
    required.forEach((name) => {
      const item = document.querySelector(`[data-requirement="${name}"]`);
      if (item) item.classList.toggle("done", Boolean(state.done[name]));
    });
    const count = required.filter((name) => state.done[name]).length;
    const button = document.querySelector("[data-complete]");
    const status = document.querySelector("[data-completion-status]");
    if (status) status.textContent = `${count} of ${required.length} required pieces complete.`;
    if (button) button.disabled = count !== required.length;
  }

  function escapeText(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  document.querySelectorAll("[data-lens]").forEach((button) => {
    if (!button.closest(".lenses")) return;
    button.addEventListener("click", () => {
      document.body.dataset.lens = button.dataset.lens;
      document.querySelectorAll(".lenses [data-lens]").forEach((item) => {
        const selected = item === button;
        item.classList.toggle("on", selected);
        item.setAttribute("aria-selected", String(selected));
      });
    });
  });

  const readingBar = document.querySelector(".reading");
  addEventListener("scroll", () => {
    const available = document.documentElement.scrollHeight - innerHeight;
    const percent = available > 0 ? scrollY / available : 0;
    readingBar.style.transform = `scaleX(${Math.min(1, Math.max(0, percent))})`;
  }, { passive: true });

  const tooltip = document.querySelector("#tt");
  document.querySelectorAll(".term").forEach((term) => {
    term.setAttribute("tabindex", "0");
    const show = () => {
      tooltip.textContent = term.dataset.def;
      tooltip.classList.add("show");
      const rect = term.getBoundingClientRect();
      tooltip.style.left = `${Math.max(12, Math.min(innerWidth - 332, rect.left))}px`;
      tooltip.style.top = `${rect.bottom + 8}px`;
    };
    const hide = () => tooltip.classList.remove("show");
    term.addEventListener("mouseenter", show);
    term.addEventListener("focus", show);
    term.addEventListener("mouseleave", hide);
    term.addEventListener("blur", hide);
  });

  const opening = document.querySelector("#opening-quiz");
  opening.querySelectorAll(".choice").forEach((choice) => {
    choice.addEventListener("click", () => {
      opening.querySelectorAll(".choice").forEach((item) => item.classList.remove("selected"));
      choice.classList.add("selected");
    });
  });
  opening.querySelector("[data-check-quiz]").addEventListener("click", () => {
    const selected = opening.querySelector(".choice.selected");
    if (!selected) {
      setFeedback(opening, "Choose one answer before checking.", false);
      return;
    }
    const good = selected.dataset.correct === "1";
    setFeedback(opening, good
      ? "Correct. Shared meaning must cross systems and remain connected to approved mappings and time rules."
      : `${opening.dataset.retry} Choose again and retry.`, good);
    if (good) markDone("opening");
  });

  const layerDetails = {
    model: ["Data model", "How is information structured for this source or use?", "CIS account fields, GIS premise-zone keys, and SCADA event records."],
    taxonomy: ["Taxonomy", "How are terms placed into controlled categories?", "Critical facility, residential customer, and commercial customer classifications."],
    ontology: ["Ontology", "What do shared concepts mean and how do they relate?", "An account serves a premise. An event affects a pressure zone."],
    semantic: ["Semantic layer", "How does shared meaning resolve to approved enterprise data?", "CIS status A plus effective dates resolves to ActiveAccount through a tested mapping."],
    context: ["AI context", "What does this task need now?", "Event 771, current evidence, definitions, procedure, permissions, workflow state, conflicts, and output limit."]
  };
  const layerDetail = document.querySelector("[data-layer-detail]");
  function showLayer(name) {
    const [title, question, example] = layerDetails[name];
    layerDetail.innerHTML = `<b>${title}</b><p>${question}</p><small>Zone 3 example: ${example}</small>`;
    document.querySelectorAll("[data-layer]").forEach((button) => button.classList.toggle("on", button.dataset.layer === name));
  }
  document.querySelectorAll("[data-layer]").forEach((button) => button.addEventListener("click", () => showLayer(button.dataset.layer)));
  showLayer("model");

  const matches = [
    ["How is information structured?", "Data model"],
    ["How are terms classified?", "Taxonomy"],
    ["What do shared concepts mean?", "Ontology"],
    ["How is meaning connected to enterprise data?", "Semantic layer"],
    ["What does this task need now?", "AI context"]
  ];
  const matchLeft = document.querySelector("[data-match-left]");
  const matchRight = document.querySelector("[data-match-right]");
  let selectedQuestion = null;
  let selectedJob = null;
  let matched = new Set();
  matches.forEach(([question], index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "match-item";
    button.textContent = question;
    button.dataset.matchQuestion = String(index);
    matchLeft.append(button);
  });
  [2, 4, 0, 3, 1].forEach((index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "match-item";
    button.textContent = matches[index][1];
    button.dataset.matchJob = String(index);
    matchRight.append(button);
  });
  function checkMatchPair() {
    if (selectedQuestion === null || selectedJob === null) return;
    const panel = document.querySelector("#layer-matching");
    const good = selectedQuestion === selectedJob;
    if (good) {
      matched.add(selectedQuestion);
      panel.querySelector(`[data-match-question="${selectedQuestion}"]`).classList.add("correct");
      panel.querySelector(`[data-match-job="${selectedJob}"]`).classList.add("correct");
      setFeedback(panel, `Correct. ${matches[selectedQuestion][0]} is the question answered by ${matches[selectedQuestion][1]}.`, true);
    } else {
      panel.querySelectorAll(".selected").forEach((item) => item.classList.remove("selected"));
      setFeedback(panel, `${panel.dataset.retry} Retry this pair.`, false);
    }
    selectedQuestion = null;
    selectedJob = null;
    if (matched.size === matches.length) {
      setFeedback(panel, "All five jobs are correctly matched. You separated structure, classification, meaning, connection, and runtime packaging.", true);
      markDone("matching");
    }
  }
  matchLeft.addEventListener("click", (event) => {
    const button = event.target.closest("[data-match-question]");
    if (!button || button.classList.contains("correct")) return;
    matchLeft.querySelectorAll(".selected").forEach((item) => item.classList.remove("selected"));
    button.classList.add("selected");
    selectedQuestion = Number(button.dataset.matchQuestion);
    checkMatchPair();
  });
  matchRight.addEventListener("click", (event) => {
    const button = event.target.closest("[data-match-job]");
    if (!button || button.classList.contains("correct")) return;
    matchRight.querySelectorAll(".selected").forEach((item) => item.classList.remove("selected"));
    button.classList.add("selected");
    selectedJob = Number(button.dataset.matchJob);
    checkMatchPair();
  });

  const sorterItems = [
    ["CIS account table and primary key", "Structure", "It organizes records inside one source."],
    ["GIS premise geometry and zone foreign key", "Structure", "It defines fields and keys for spatial records."],
    ["SCADA pressure-event schema", "Structure", "It structures operational event records."],
    ["Work-order status constraint", "Structure", "It limits permitted values in one application."],
    ["Laboratory sample identifier format", "Structure", "It defines a stable source identifier."],
    ["Critical-facility category list", "Classification", "It groups facilities under controlled terms."],
    ["Customer-class hierarchy", "Classification", "It arranges controlled customer categories."],
    ["Incident-severity levels", "Classification", "It classifies events into named levels."],
    ["Asset-type code list", "Classification", "It standardizes categories for assets."],
    ["Preferred synonym list for service interruption", "Classification", "It controls preferred and alternate terms."],
    ["Account serves premise", "Meaning", "It defines a shared relationship."],
    ["Pressure event affects zone", "Meaning", "It defines how shared concepts relate."],
    ["Critical facility is a facility class", "Meaning", "It states a shared class relationship."],
    ["Active account definition", "Meaning", "It defines a reusable business concept."],
    ["Premise and service location identity rule", "Meaning", "It clarifies shared identity."],
    ["CIS status A maps to ActiveAccount", "Connection", "It resolves a shared concept to source data."],
    ["GIS zone identifier maps to PressureZone", "Connection", "It connects a source field to shared meaning."],
    ["Approved customer count metric", "Connection", "It governs how a shared measure resolves to records."],
    ["Virtual graph mapping over the lakehouse", "Connection", "It exposes data in place through shared concepts."],
    ["Mapping freshness test", "Connection", "It tests the governed connection to source data."],
    ["Event 771 at 2:10 a.m.", "Runtime", "It supplies the current task identity and time."],
    ["Current advisory procedure for this jurisdiction", "Runtime", "It supplies effective policy for this request."],
    ["User permission and draft-only limit", "Runtime", "It bounds what this request may do."],
    ["Known stale GIS link and escalation flag", "Runtime", "It exposes a current conflict and control."],
    ["Requested output schema for operations review", "Runtime", "It constrains this task's output."]
  ];
  const sorter = document.querySelector("[data-sorter]");
  let sorterCorrect = 0;
  sorterItems.forEach(([label, answer, explanation], index) => {
    const row = document.createElement("div");
    row.className = "sort-row";
    row.dataset.sortIndex = String(index);
    row.dataset.answer = answer;
    row.innerHTML = `<div><b>${index + 1}. ${label}</b><small data-sort-feedback>Choose the primary job.</small></div><div class="sort-actions">${["Structure", "Classification", "Meaning", "Connection", "Runtime"].map((job) => `<button type="button" data-sort-job="${job}">${job}</button>`).join("")}</div>`;
    sorter.append(row);
    row.addEventListener("click", (event) => {
      const button = event.target.closest("[data-sort-job]");
      if (!button || row.classList.contains("correct")) return;
      row.querySelectorAll("button").forEach((item) => item.classList.remove("selected"));
      button.classList.add("selected");
      const good = button.dataset.sortJob === answer;
      const note = row.querySelector("[data-sort-feedback]");
      if (good) {
        row.classList.add("correct");
        note.textContent = `Correct: ${answer}. ${explanation}`;
        sorterCorrect += 1;
      } else {
        note.textContent = `Not yet. ${explanation} Choose again.`;
      }
      const panel = document.querySelector("#artifact-sorter");
      setFeedback(panel, good ? `${sorterCorrect} of ${sorterItems.length} correct.` : panel.dataset.retry, good);
      if (sorterCorrect === sorterItems.length) {
        setFeedback(panel, "All 25 artifacts are correctly classified by primary job.", true);
        markDone("sorter");
      }
    });
  });

  const processStates = [
    ["Question received", "Draft the active critical-facility exposure summary for Pressure Event 771.", ["Task identity", "Draft-only output"]],
    ["Source structure read", "CIS, GIS, and SCADA models provide fields, keys, statuses, zones, and event values.", ["Source contracts", "Stable identifiers"]],
    ["Shared meaning applied", "The ontology resolves account, premise, zone, event, active, serves, and affects.", ["Concept definitions", "Named relationships"]],
    ["Enterprise connection resolved", "Approved mappings connect those concepts to source records and reveal a stale GIS link.", ["Mappings", "Source authority", "Tests"]],
    ["Context package assembled", "The context engine adds time, current procedure, user permission, workflow state, conflicts, and output limits.", ["Evidence", "Policy", "Permission", "Limits"]],
    ["Human review boundary", "The model produces a cited draft. The operations authority reviews and decides whether action is warranted.", ["Traceable draft", "Named decision owner"]]
  ];
  const processStage = document.querySelector("[data-process-stage]");
  processStates.forEach(([title, body, additions], index) => {
    const stateNode = document.createElement("div");
    stateNode.className = "process-state";
    stateNode.innerHTML = `<span class="tag">State ${index + 1} of ${processStates.length}</span><h3>${title}</h3><p>${body}</p><div class="process-flow">${processStates.map((state, step) => `<div class="flowbox ${step <= index ? "active" : ""}"><b>${step + 1}</b><span>${state[0]}</span></div>${step < processStates.length - 1 ? '<span class="flowarrow">→</span>' : ""}`).join("")}</div><div class="debrief"><b>What this state adds</b>${additions.join(" | ")}</div>`;
    processStage.append(stateNode);
  });
  function showProcess(index) {
    processIndex = Math.max(0, Math.min(processStates.length - 1, index));
    processStage.querySelectorAll(".process-state").forEach((node, position) => node.classList.toggle("active", position === processIndex));
    document.querySelector("#exposure-process .meter i").style.width = `${((processIndex + 1) / processStates.length) * 100}%`;
    if (processIndex === processStates.length - 1) markDone("flow");
  }
  function stopPlay() {
    clearInterval(playTimer);
    playTimer = null;
  }
  document.querySelector("[data-back]").addEventListener("click", () => { stopPlay(); showProcess(processIndex - 1); });
  document.querySelector("[data-next]").addEventListener("click", () => { stopPlay(); showProcess(processIndex + 1); });
  document.querySelector("[data-reset]").addEventListener("click", () => { stopPlay(); showProcess(0); });
  document.querySelector("[data-pause]").addEventListener("click", stopPlay);
  document.querySelector("[data-play]").addEventListener("click", () => {
    stopPlay();
    if (processIndex === processStates.length - 1) showProcess(0);
    playTimer = setInterval(() => {
      if (processIndex === processStates.length - 1) stopPlay();
      else showProcess(processIndex + 1);
    }, 1300);
  });
  showProcess(0);

  const orderLabels = [
    "Read stable source structure",
    "Resolve shared concepts and relationships",
    "Apply approved mappings and source authority",
    "Retrieve current evidence, policy, time, and permission",
    "Assemble bounded AI context",
    "Send cited draft to human authority"
  ];
  let order = [3, 0, 4, 1, 5, 2];
  const orderBox = document.querySelector("[data-order]");
  function renderOrder() {
    orderBox.innerHTML = order.map((item, position) => `<div class="order-row"><i>${position + 1}</i><span>${orderLabels[item]}</span><div><button type="button" aria-label="Move up" data-move-up="${position}">↑</button><button type="button" aria-label="Move down" data-move-down="${position}">↓</button></div></div>`).join("");
  }
  orderBox.addEventListener("click", (event) => {
    const up = event.target.closest("[data-move-up]");
    const down = event.target.closest("[data-move-down]");
    const position = Number((up || down)?.dataset[up ? "moveUp" : "moveDown"]);
    if (!Number.isInteger(position)) return;
    const nextPosition = up ? position - 1 : position + 1;
    if (nextPosition < 0 || nextPosition >= order.length) return;
    [order[position], order[nextPosition]] = [order[nextPosition], order[position]];
    renderOrder();
  });
  document.querySelector("[data-check-order]").addEventListener("click", () => {
    const panel = document.querySelector("#process-order");
    const good = order.every((value, index) => value === index);
    setFeedback(panel, good
      ? "Correct. Meaning and mappings are resolved before runtime context is assembled, and human authority remains last."
      : `${panel.dataset.retry} Move the steps and retry.`, good);
    if (good) markDone("ordering");
  });
  renderOrder();

  const failures = {
    ontology: {
      labels: ["Shared definition missing", "Active means different things", "Mappings target conflicting meanings", "Exposure list changes by system", "Operations cannot defend the answer"],
      repair: "Repair: approve the shared ActiveAccount and affected-by relationships, with named owners and scope."
    },
    semantic: {
      labels: ["Approved mapping missing", "Concept cannot resolve to records", "The model guesses which fields count", "Evidence path is not testable", "A fluent answer hides source drift"],
      repair: "Repair: map the shared concepts to authoritative CIS and GIS fields, transformations, and tests."
    },
    context: {
      labels: ["Runtime controls missing", "Stale policy or excessive data enters", "Permission and workflow state disappear", "Model may exceed the task", "Human receives an unsafe draft"],
      repair: "Repair: assemble current evidence, policy, time, permission, conflicts, and output limits for the task."
    },
    model: {
      labels: ["Source structure unstable", "Keys and statuses cannot be interpreted", "Mappings break or silently drift", "Records cannot be joined reliably", "Exposure answer is incomplete"],
      repair: "Repair: stabilize source entities, fields, identifiers, constraints, and change control before mapping."
    }
  };
  document.querySelectorAll("[data-failure]").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll("[data-failure]").forEach((item) => item.classList.toggle("on", item === button));
      const failure = failures[button.dataset.failure];
      document.querySelector("[data-cause-chain]").innerHTML = failure.labels.map((label, index) => `<div class="cause"><i>${index + 1}</i><span>${label}</span></div>${index < failure.labels.length - 1 ? '<span class="cause-arrow">→</span>' : ""}`).join("");
      document.querySelector("[data-failure-debrief]").innerHTML = `<b>Repair the first broken boundary</b>${failure.repair}`;
      markDone("failure");
    });
  });

  const claims = [
    ["SHACL validation proves that every real-world fact is true.", false, "SHACL checks declared graph constraints. It does not inspect the physical world."],
    ["OWL reasoning can derive a new statement from declared semantics.", true, "Reasoning can infer statements that follow from the declared model and data."],
    ["Good context can reduce ambiguity without making generative output perfectly deterministic.", true, "Evidence and controls stabilize the task, while generation can still vary."],
    ["A retrieved document becomes authoritative because it was ranked first.", false, "Retrieval rank does not establish authority, currency, jurisdiction, or permission."]
  ];
  const tfBox = document.querySelector("[data-true-false]");
  claims.forEach(([claim], index) => {
    const row = document.createElement("div");
    row.className = "tf-row";
    row.dataset.answer = String(answer);
    row.innerHTML = `<p><b>${index + 1}.</b> ${claim}</p><div><button type="button" data-tf="${index}" data-value="true">True</button><button type="button" data-tf="${index}" data-value="false">False</button></div><small data-tf-note="${index}"></small>`;
    tfBox.append(row);
  });
  tfBox.addEventListener("click", (event) => {
    const button = event.target.closest("[data-tf]");
    if (!button) return;
    button.parentElement.querySelectorAll("button").forEach((item) => item.classList.remove("selected"));
    button.classList.add("selected");
  });
  document.querySelector("[data-check-tf]").addEventListener("click", () => {
    const panel = document.querySelector("#myth-check");
    let correct = 0;
    claims.forEach(([, answer, explanation], index) => {
      const selected = tfBox.querySelector(`[data-tf="${index}"].selected`);
      const good = selected && (selected.dataset.value === "true") === answer;
      if (good) correct += 1;
      tfBox.querySelector(`[data-tf-note="${index}"]`).textContent = `${good ? "Correct." : "Not yet."} ${explanation}`;
    });
    const good = correct === claims.length;
    setFeedback(panel, good ? "All four claims are correct." : `${correct} of ${claims.length} correct. ${panel.dataset.retry} Retry any statement.`, good);
    if (good) markDone("myths");
  });

  const contextPanel = document.querySelector("#context-quiz");
  contextPanel.querySelectorAll(".option-check").forEach((button) => {
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      const selected = !button.classList.contains("selected");
      button.classList.toggle("selected", selected);
      button.setAttribute("aria-pressed", String(selected));
    });
  });
  contextPanel.querySelector("[data-check-multi]").addEventListener("click", () => {
    const options = [...contextPanel.querySelectorAll(".option-check")];
    const good = options.every((option) => option.classList.contains("selected") === (option.dataset.correct === "1"));
    setFeedback(contextPanel, good
      ? "Correct. The packet is relevant, current, authorized, conflict-aware, and bounded to a draft."
      : `${contextPanel.dataset.retry} Change your selections and retry.`, good);
    if (good) markDone("context");
  });

  const raciRows = [
    ["Approve ActiveAccount meaning", "Customer executive", "Domain steward", "Legal, operations, data governance"],
    ["Approve CIS and GIS mappings", "Data governance lead", "Semantic engineer", "Source owners, domain steward"],
    ["Approve effective advisory procedure", "Operations executive", "Policy owner", "Legal, emergency management"],
    ["Configure context and tool permissions", "AI product owner", "Security and platform team", "Operations, privacy, data governance"],
    ["Issue or withhold the advisory", "Authorized operations leader", "Incident commander", "Communications, legal, field operations"]
  ];
  const ownerOptions = ["Select", "Customer executive", "Data governance lead", "Operations executive", "AI product owner", "Authorized operations leader"];
  const responsibleOptions = ["Select", "Domain steward", "Semantic engineer", "Policy owner", "Security and platform team", "Incident commander"];
  const raciBody = document.querySelector("[data-raci-body]");
  raciRows.forEach(([decision, owner, responsible, consulted], index) => {
    const row = document.createElement("tr");
    row.innerHTML = `<td><b>${decision}</b></td><td><select aria-label="Accountable owner for ${escapeText(decision)}" data-raci-owner="${index}">${ownerOptions.map((item) => `<option>${item}</option>`).join("")}</select></td><td><select aria-label="Responsible role for ${escapeText(decision)}" data-raci-responsible="${index}">${responsibleOptions.map((item) => `<option>${item}</option>`).join("")}</select></td><td>${consulted}</td>`;
    row.dataset.owner = owner;
    row.dataset.responsible = responsible;
    raciBody.append(row);
  });
  document.querySelector("[data-check-raci]").addEventListener("click", () => {
    const panel = document.querySelector("#raci-visual");
    let correct = 0;
    [...raciBody.rows].forEach((row) => {
      const good = row.querySelector("select:first-of-type").value === row.dataset.owner
        && row.querySelector("select:last-of-type").value === row.dataset.responsible;
      row.classList.toggle("correct", good);
      correct += good ? 1 : 0;
    });
    const good = correct === raciRows.length;
    setFeedback(panel, good
      ? "Correct. Meaning, mappings, policy, controls, and the operational decision have explicit accountability."
      : `${correct} of ${raciRows.length} decisions are correctly assigned. Review who approves each decision and who performs the work, then retry.`, good);
    if (good) markDone("raci");
  });

  const form = document.querySelector("#meaning-map");
  Object.entries(state.artifact || {}).forEach(([name, value]) => {
    const field = form.elements.namedItem(name);
    if (field) field.value = value;
  });
  function artifactData() {
    return Object.fromEntries(new FormData(form).entries());
  }
  function renderArtifact(data) {
    const labels = {
      question: "OPERATIONAL QUESTION", model: "DATA MODEL", taxonomy: "TAXONOMY",
      ontology: "ONTOLOGY", semantic: "SEMANTIC LAYER", context: "AI CONTEXT CONTRACT",
      reviewers: "NAMED REVIEWERS", boundary: "HUMAN AUTHORITY BOUNDARY"
    };
    document.querySelector("[data-artifact-preview]").textContent = Object.entries(labels)
      .map(([key, label]) => `${label}\n${data[key] || "Not yet defined"}`)
      .join("\n\n");
  }
  renderArtifact(state.artifact || {});
  form.addEventListener("input", () => renderArtifact(artifactData()));
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = artifactData();
    const short = Object.entries(data).filter(([, value]) => String(value).trim().length < 12);
    if (short.length) {
      setFeedback(form, "Every field needs a specific statement of at least 12 characters. Revise and save again.", false);
      return;
    }
    state.artifact = data;
    saveState();
    renderArtifact(data);
    setFeedback(form, "Working draft saved locally. Now evaluate it against the applied criteria.", true);
    markDone("artifact");
  });

  const criteria = [
    ["Bounded operational question", (data) => data.question?.length >= 24],
    ["All five architecture jobs are specific", (data) => ["model", "taxonomy", "ontology", "semantic", "context"].every((key) => data[key]?.length >= 20)],
    ["Ontology names at least one relationship", (data) => /\b(serves|affects|located|belongs|connected|relates|feeds|contains|has)\b/i.test(data.ontology || "")],
    ["Semantic layer names a source or mapping", (data) => /\b(map|mapping|CIS|GIS|SCADA|table|field|API|source)\b/i.test(data.semantic || "")],
    ["Context names control factors", (data) => /\b(time|policy|permission|state|conflict|limit|current|effective)\b/i.test(data.context || "")],
    ["Reviewers and human authority boundary are explicit", (data) => data.reviewers?.length >= 12 && /\b(cannot|must not|may not|human|approve|review|decide|issue)\b/i.test(data.boundary || "")]
  ];
  const criteriaBox = document.querySelector("[data-criteria]");
  function renderCriteria(results = criteria.map(() => false)) {
    criteriaBox.innerHTML = criteria.map(([label], index) => `<div class="criterion ${results[index] ? "pass" : ""}"><i>${results[index] ? "✓" : "○"}</i><span>${label}</span></div>`).join("");
  }
  renderCriteria();
  document.querySelector("[data-check-applied]").addEventListener("click", () => {
    const panel = document.querySelector("#applied-check");
    if (!state.done.artifact) {
      setFeedback(panel, "Save the Five-Layer Meaning Map first. The assessment evaluates the saved work product.", false);
      return;
    }
    const results = criteria.map(([, test]) => Boolean(test(state.artifact)));
    renderCriteria(results);
    const correct = results.filter(Boolean).length;
    const good = correct === criteria.length;
    setFeedback(panel, good
      ? "Applied assessment passed. The saved map is specific enough for another team to review."
      : `${correct} of ${criteria.length} criteria pass. ${panel.dataset.retry}`, good);
    if (good) markDone("applied");
  });

  const graphDetails = {
    "source-systems": ["Source", "CIS, GIS, and SCADA provide governed records through their own data models.", "provides records to semantic layer"],
    "data-model": ["Concept", "A data model structures information for one system or use.", "supports source mapping"],
    taxonomy: ["Concept", "A taxonomy controls categories and preferred terms.", "classifies ontology concepts"],
    ontology: ["Concept", "An ontology defines shared concepts and relationships independently of one source.", "is resolved by semantic layer"],
    "semantic-layer": ["Relationship", "The semantic layer connects shared meaning to authoritative fields, metrics, services, and tests.", "supplies governed evidence to context engine"],
    "context-engine": ["Role", "The context engine retrieves, filters, validates, and assembles the task package.", "assembles AI context"],
    competency: ["Competency", "The learner can separate structure, classification, meaning, connection, and runtime context.", "demonstrated by Five-Layer Meaning Map"]
  };
  document.querySelectorAll("[data-graph-id]").forEach((node) => {
    node.addEventListener("click", () => {
      document.querySelectorAll("[data-graph-id]").forEach((item) => item.classList.toggle("active", item === node));
      const [kind, meaning, relationship] = graphDetails[node.dataset.graphId];
      document.querySelector("[data-graph-detail]").innerHTML = `<b>${kind}: ${node.textContent}</b><p>${meaning}</p><small>Named relationship: ${relationship}.</small>`;
    });
  });

  function openDrawer(name, trigger) {
    closeDrawers();
    lastDrawerTrigger = trigger;
    const drawer = document.querySelector(`[data-drawer="${name}"]`);
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    document.body.classList.add("drawer-open");
    document.querySelector(".drawer-scrim").classList.add("open");
    drawer.querySelector("button, input")?.focus();
    if (name === "graph" && trigger?.dataset.focusGraph) {
      document.querySelector(`[data-graph-id="${trigger.dataset.focusGraph}"]`)?.click();
    }
  }
  function closeDrawers() {
    document.querySelectorAll("[data-drawer]").forEach((drawer) => {
      drawer.classList.remove("open");
      drawer.setAttribute("aria-hidden", "true");
    });
    document.querySelector(".drawer-scrim").classList.remove("open");
    document.body.classList.remove("drawer-open");
    if (lastDrawerTrigger) {
      const trigger = lastDrawerTrigger;
      lastDrawerTrigger = null;
      setTimeout(() => trigger.focus(), 0);
    }
  }
  document.querySelectorAll("[data-open-graph]").forEach((button) => button.addEventListener("click", () => openDrawer("graph", button)));
  document.querySelectorAll("[data-open-community]").forEach((button) => button.addEventListener("click", () => openDrawer("community", button)));
  document.querySelectorAll("[data-close-drawer]").forEach((button) => button.addEventListener("click", closeDrawers));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeDrawers();
  });

  const threads = [...document.querySelectorAll("[data-thread]")];
  function filterThreads() {
    const query = document.querySelector("[data-community-search]").value.trim().toLowerCase();
    threads.forEach((thread) => {
      const matchesRole = activeCommunityFilter === "all" || thread.dataset.role === activeCommunityFilter;
      const matchesQuery = !query || thread.textContent.toLowerCase().includes(query);
      thread.hidden = !(matchesRole && matchesQuery);
    });
  }
  document.querySelector("[data-community-search]").addEventListener("input", filterThreads);
  document.querySelectorAll("[data-filter]").forEach((button) => {
    button.addEventListener("click", () => {
      activeCommunityFilter = button.dataset.filter;
      document.querySelectorAll("[data-filter]").forEach((item) => item.classList.toggle("on", item === button));
      filterThreads();
    });
  });
  document.querySelectorAll("[data-bookmark]").forEach((button, index) => {
    button.classList.toggle("on", Boolean(state.bookmarks?.[index]));
    button.textContent = state.bookmarks?.[index] ? "Bookmarked" : "Bookmark";
    button.addEventListener("click", () => {
      state.bookmarks ||= {};
      state.bookmarks[index] = !state.bookmarks[index];
      button.classList.toggle("on", state.bookmarks[index]);
      button.textContent = state.bookmarks[index] ? "Bookmarked" : "Bookmark";
      saveState();
    });
  });
  document.querySelectorAll("[data-reply-form]").forEach((replyForm, index) => {
    const replies = state.replies?.[index] || [];
    const box = replyForm.parentElement.querySelector(".replies");
    replies.forEach((reply) => {
      const paragraph = document.createElement("p");
      paragraph.innerHTML = `<b>Your local draft:</b> ${escapeText(reply)}`;
      box.append(paragraph);
    });
    replyForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const input = replyForm.querySelector("input");
      const value = input.value.trim();
      if (!value) return;
      state.replies ||= {};
      state.replies[index] ||= [];
      state.replies[index].push(value);
      saveState();
      const paragraph = document.createElement("p");
      paragraph.innerHTML = `<b>Your local draft:</b> ${escapeText(value)}`;
      box.append(paragraph);
      input.value = "";
    });
  });

  document.querySelector("[data-complete]").addEventListener("click", () => {
    const live = document.querySelector("#live");
    live.textContent = "Module 05 is marked complete in this browser. This is not a credential or release record.";
    live.className = "feedback show good";
    state.moduleComplete = true;
    saveState();
  });

  renderCompletion();
})();
