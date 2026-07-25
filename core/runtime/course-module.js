(() => {
  "use strict";

  const required = JSON.parse(document.body.dataset.requiredIds || "[]");
  const stateKey = `owos-module:${document.body.dataset.moduleId}:${document.body.dataset.sourceVersion}`;
  const completed = new Set();
  let lastDrawerTrigger = null;

  try {
    const saved = JSON.parse(localStorage.getItem(stateKey) || "[]");
    saved.forEach((id) => completed.add(id));
  } catch {
    localStorage.removeItem(stateKey);
  }

  function saveState() {
    localStorage.setItem(stateKey, JSON.stringify([...completed].sort()));
  }

  function refreshCompletion() {
    document.querySelectorAll("[data-completion-id]").forEach((item) => {
      item.classList.toggle("done", completed.has(item.dataset.completionId));
    });
    const ready = required.every((id) => completed.has(id));
    const button = document.querySelector("[data-complete-module]");
    const status = document.querySelector("[data-completion-status]");
    if (button) button.disabled = !ready;
    if (status) {
      const count = required.filter((id) => completed.has(id)).length;
      status.textContent = ready
        ? "All required evidence is complete. You can complete this working candidate."
        : `${count} of ${required.length} required activities complete.`;
    }
  }

  function mark(id) {
    if (!id) return;
    completed.add(id);
    saveState();
    refreshCompletion();
  }

  document.querySelectorAll("[data-choice-group]").forEach((group) => {
    let selected = null;
    group.querySelectorAll("[data-choice]").forEach((button) => {
      button.addEventListener("click", () => {
        group.querySelectorAll("[data-choice]").forEach((item) => item.classList.remove("selected"));
        button.classList.add("selected");
        selected = button;
      });
    });
    group.querySelector("[data-check-choice]")?.addEventListener("click", () => {
      const feedback = group.querySelector("[data-feedback]");
      if (!selected) {
        feedback.textContent = "Choose one response first.";
        feedback.className = "feedback bad";
        return;
      }
      const correct = selected.dataset.correct === "true";
      selected.classList.add(correct ? "correct" : "incorrect");
      feedback.textContent = correct ? group.dataset.correctFeedback : group.dataset.incorrectFeedback;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(group.dataset.completion);
    });
  });

  document.querySelectorAll("[data-flip-group]").forEach((group) => {
    const cards = [...group.querySelectorAll("[data-flip-card]")];
    cards.forEach((card) => {
      card.addEventListener("click", () => {
        const revealed = !card.classList.contains("revealed");
        card.classList.toggle("revealed", revealed);
        card.setAttribute("aria-pressed", String(revealed));
        if (cards.every((item) => item.classList.contains("revealed"))) {
          mark(group.dataset.completion);
          const feedback = group.querySelector("[data-feedback]");
          feedback.textContent = group.dataset.correctFeedback;
          feedback.className = "feedback good";
        }
      });
    });
  });

  document.querySelectorAll("[data-matching]").forEach((group) => {
    group.querySelector("[data-check-matching]")?.addEventListener("click", () => {
      const rows = [...group.querySelectorAll("[data-match-answer]")];
      const feedback = group.querySelector("[data-feedback]");
      let correctCount = 0;
      rows.forEach((field) => {
        const correct = field.value === field.dataset.matchAnswer;
        field.classList.toggle("correct-field", correct);
        field.classList.toggle("incorrect-field", !correct);
        if (correct) correctCount += 1;
      });
      const correct = correctCount === rows.length;
      feedback.textContent = correct
        ? group.dataset.correctFeedback
        : `${group.dataset.incorrectFeedback} ${correctCount} of ${rows.length} are correctly matched.`;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(group.dataset.completion);
    });
  });

  document.querySelectorAll("[data-multi-select]").forEach((group) => {
    group.querySelector("[data-check-multi]")?.addEventListener("click", () => {
      const options = [...group.querySelectorAll("[data-multi-option]")];
      const feedback = group.querySelector("[data-feedback]");
      const correct = options.every(
        (option) => option.checked === (option.dataset.correct === "true")
      );
      options.forEach((option) => {
        option.closest(".select-option")?.classList.toggle(
          "selected-correct",
          option.checked && option.dataset.correct === "true"
        );
        option.closest(".select-option")?.classList.toggle(
          "selected-incorrect",
          option.checked && option.dataset.correct !== "true"
        );
      });
      feedback.textContent = correct
        ? group.dataset.correctFeedback
        : group.dataset.incorrectFeedback;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(group.dataset.completion);
    });
  });

  document.querySelectorAll("[data-triple-builder]").forEach((builder) => {
    const selects = [...builder.querySelectorAll("select")];
    const correct = JSON.parse(builder.dataset.correct);
    const output = builder.querySelector("[data-triple-output]");
    const feedback = builder.querySelector("[data-feedback]");
    const reverseButton = builder.querySelector("[data-reverse]");
    let built = false;
    let reversed = false;

    builder.querySelector("[data-check-triple]").addEventListener("click", () => {
      const values = selects.map((field) => field.value);
      output.textContent = values.every(Boolean) ? values.join("  →  ") : "Choose all three positions.";
      built = values.every((value, index) => value === correct[index]);
      reverseButton.disabled = !built;
      feedback.textContent = built
        ? "Correct. Now reverse the ends and inspect what the statement says."
        : "Use Pump_P104 as subject, serves as predicate, and Pressure_Zone_3 as object.";
      feedback.className = `feedback ${built ? "good" : "bad"}`;
    });

    reverseButton.addEventListener("click", () => {
      const first = selects[0].value;
      selects[0].value = selects[2].value;
      selects[2].value = first;
      reversed = true;
      output.textContent = selects.map((field) => field.value).join("  →  ");
      feedback.textContent = "The words are familiar, but the direction now says the pressure zone serves the pump.";
      feedback.className = "feedback bad";
    });

    builder.querySelector("[data-finish-triple]").addEventListener("click", () => {
      const explanation = builder.querySelector("textarea").value.trim();
      const enough = explanation.length >= Number(builder.dataset.minimumExplanation);
      if (built && reversed && enough) {
        mark(builder.dataset.completion);
        feedback.textContent = "Complete. You showed that direction carries meaning.";
        feedback.className = "feedback good";
      } else {
        feedback.textContent = "Build the correct triple, reverse it, and explain the changed meaning in one full sentence.";
        feedback.className = "feedback bad";
      }
    });
  });

  document.querySelectorAll("[data-path-tracer]").forEach((tracer) => {
    const edges = [...tracer.querySelectorAll("[data-edge-index]")];
    const feedback = tracer.querySelector("[data-feedback]");
    let expected = 0;
    edges.forEach((edge) => {
      edge.addEventListener("click", () => {
        const index = Number(edge.dataset.edgeIndex);
        if (index !== expected) {
          feedback.textContent = `Start with edge ${expected + 1}. A path only works when its relationships connect in order.`;
          feedback.className = "feedback bad";
          return;
        }
        edge.classList.add("active");
        expected += 1;
        feedback.textContent = edge.dataset.explanation;
        feedback.className = "feedback good";
        if (expected === edges.length) mark(tracer.dataset.completion);
      });
    });
    tracer.querySelector("[data-reset-path]").addEventListener("click", () => {
      expected = 0;
      edges.forEach((edge) => edge.classList.remove("active"));
      feedback.textContent = "Path reset. Begin with edge 1.";
      feedback.className = "feedback";
    });
  });

  document.querySelectorAll("[data-artifact-classifier]").forEach((desk) => {
    const items = [...desk.querySelectorAll("[data-triage-item]")];
    const feedback = desk.querySelector("[data-feedback]");
    desk.querySelector("[data-check-triage]")?.addEventListener("click", () => {
      let correctCount = 0;
      items.forEach((item) => {
        const field = item.querySelector("select");
        const correct = field.value === item.dataset.answer;
        const itemFeedback = item.querySelector("[data-item-feedback]");
        item.classList.toggle("correct-card", correct);
        item.classList.toggle("incorrect-card", !correct);
        itemFeedback.textContent = correct
          ? `Correct. ${item.dataset.explanation}`
          : `Try again. Ask what primary job this artifact performs here. ${item.dataset.explanation}`;
        if (correct) correctCount += 1;
      });
      const correct = correctCount === items.length;
      feedback.textContent = correct
        ? "The desk is organized. The same event now has distinct structures, classifications, meanings, mappings, and runtime controls."
        : `${correctCount} of ${items.length} artifacts are correctly placed. Use the explanation under each artifact and retry.`;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(desk.dataset.completion);
    });
    desk.querySelector("[data-reset-triage]")?.addEventListener("click", () => {
      items.forEach((item) => {
        item.querySelector("select").value = "";
        item.classList.remove("correct-card", "incorrect-card");
        item.querySelector("[data-item-feedback]").textContent = "";
      });
      feedback.textContent = "The triage desk is reset.";
      feedback.className = "feedback";
    });
  });

  document.querySelectorAll("[data-failure-trace]").forEach((lab) => {
    const triggers = [...lab.querySelectorAll("[data-failure-trigger]")];
    const visited = new Set();
    const feedback = lab.querySelector("[data-feedback]");
    triggers.forEach((trigger) => {
      trigger.addEventListener("click", () => {
        const job = trigger.dataset.failureTrigger;
        visited.add(job);
        triggers.forEach((item) => {
          item.classList.toggle("active", item === trigger);
          item.setAttribute("aria-pressed", String(item === trigger));
        });
        lab.querySelectorAll("[data-failure-result]").forEach((result) => {
          result.hidden = result.dataset.failureResult !== job;
        });
        feedback.textContent =
          visited.size === triggers.length
            ? "All five paths inspected. The symptom appears in the answer, but the first repair belongs at the first broken job."
            : `${visited.size} of ${triggers.length} failure paths inspected.`;
        feedback.className = "feedback good";
        if (visited.size === triggers.length) mark(lab.dataset.completion);
      });
    });
  });

  document.querySelectorAll("[data-object-router]").forEach((router) => {
    const items = [...router.querySelectorAll("[data-route-item]")];
    const feedback = router.querySelector("[data-feedback]");
    items.forEach((item) => {
      item.querySelectorAll("[data-route-choice]").forEach((button) => {
        button.addEventListener("click", () => {
          item.querySelectorAll("[data-route-choice]").forEach((choice) => choice.classList.remove("active"));
          button.classList.add("active");
          const correct = button.dataset.routeChoice === item.dataset.answer;
          item.dataset.complete = String(correct);
          const itemFeedback = item.querySelector("[data-item-feedback]");
          itemFeedback.textContent = correct
            ? `Correct. ${item.dataset.explanation}`
            : `Try the other branch. ${item.dataset.explanation}`;
          itemFeedback.className = `item-feedback ${correct ? "good-text" : "bad-text"}`;
          if (items.every((candidate) => candidate.dataset.complete === "true")) {
            feedback.textContent = "Every object is correctly routed. Resource objects continue relationships; literals carry values.";
            feedback.className = "feedback good";
            mark(router.dataset.completion);
          }
        });
      });
    });
  });

  document.querySelectorAll("[data-triple-repair-bench]").forEach((bench) => {
    const cards = [...bench.querySelectorAll("[data-repair-card]")];
    const feedback = bench.querySelector("[data-feedback]");
    bench.querySelector("[data-check-repairs]")?.addEventListener("click", () => {
      let correctCount = 0;
      cards.forEach((card) => {
        const defectCorrect = card.querySelector("[data-defect-field]").value === card.dataset.defect;
        const repairCorrect = card.querySelector("[data-repair-field]").value === card.dataset.repair;
        const correct = defectCorrect && repairCorrect;
        const itemFeedback = card.querySelector("[data-item-feedback]");
        card.classList.toggle("correct-card", correct);
        card.classList.toggle("incorrect-card", !correct);
        itemFeedback.textContent = correct
          ? `Repair accepted. ${card.dataset.explanation}`
          : `Inspect both the failed position and the smallest repair. ${card.dataset.explanation}`;
        if (correct) correctCount += 1;
      });
      const correct = correctCount === cards.length;
      feedback.textContent = correct
        ? "All four statements are repaired without claiming more than their evidence supports."
        : `${correctCount} of ${cards.length} repairs pass review. Read each explanation and retry.`;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(bench.dataset.completion);
    });
  });

  document.querySelectorAll("[data-identity-adjudication]").forEach((docket) => {
    const records = [...docket.querySelectorAll("[data-docket-record]")];
    const feedback = docket.querySelector("[data-feedback]");
    docket.querySelector("[data-check-docket]")?.addEventListener("click", () => {
      let correct = 0;
      records.forEach((record) => {
        const passed = record.querySelector("select").value === record.dataset.answer;
        record.classList.toggle("passed", passed);
        record.classList.toggle("failed", !passed);
        record.querySelector("[data-item-feedback]").textContent = passed
          ? `Finding accepted. ${record.dataset.explanation}`
          : "That finding does not fit the evidence. Separate the physical asset from records about it, and preserve contradictions.";
        if (passed) correct += 1;
      });
      if (correct === records.length) {
        feedback.textContent = "Docket complete. Approved identity, related records, and the unresolved conflict remain visibly different.";
        feedback.className = "feedback good";
        mark(docket.dataset.completion);
      } else {
        feedback.textContent = `${correct} of ${records.length} findings are supported. Review the evidence and retry.`;
        feedback.className = "feedback bad";
      }
    });
    docket.querySelector("[data-reset-docket]")?.addEventListener("click", () => {
      records.forEach((record) => {
        record.querySelector("select").value = "";
        record.classList.remove("passed", "failed");
        record.querySelector("[data-item-feedback]").textContent = "";
      });
      feedback.textContent = "Review all five records.";
      feedback.className = "feedback";
    });
  });

  document.querySelectorAll("[data-graph-growth-lab]").forEach((lab) => {
    const sources = JSON.parse(lab.dataset.sourceStatements || "[]");
    const loaded = new Set();
    const tested = new Set();
    const ledger = lab.querySelector("[data-statement-ledger]");
    const count = lab.querySelector("[data-graph-count]");
    const result = lab.querySelector("[data-query-result]");
    const feedback = lab.querySelector("[data-feedback]");

    function renderLedger() {
      const statements = sources.filter((source) => loaded.has(source.source))
        .flatMap((source) => source.statements.map((statement) => ({ ...statement, source: source.source })));
      count.textContent = `${statements.length} statements loaded from ${loaded.size} source packets`;
      ledger.innerHTML = statements.length
        ? statements.map((statement) => `<article class="ledger-statement"><span>${statement.source}</span><code>${statement.subject} → ${statement.predicate} → ${statement.object}</code></article>`).join("")
        : '<p class="empty-state">Choose a source packet. Every statement remains attributable to its source.</p>';
      lab.querySelectorAll("[data-source-packet]").forEach((button) => {
        const active = loaded.has(button.dataset.sourcePacket);
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", String(active));
      });
    }

    lab.querySelectorAll("[data-source-packet]").forEach((button) => {
      button.setAttribute("aria-pressed", "false");
      button.addEventListener("click", () => {
        const source = button.dataset.sourcePacket;
        loaded.has(source) ? loaded.delete(source) : loaded.add(source);
        tested.clear();
        lab.querySelectorAll("[data-graph-question]").forEach((question) => question.classList.remove("answered"));
        result.textContent = "The graph changed. Test the competency questions again.";
        renderLedger();
      });
    });

    lab.querySelectorAll("[data-graph-question]").forEach((button) => {
      button.addEventListener("click", () => {
        const requires = JSON.parse(button.dataset.requires || "[]");
        const missing = requires.filter((source) => !loaded.has(source));
        tested.add(button.dataset.graphQuestion);
        if (missing.length) {
          result.innerHTML = `<strong>Not answerable yet.</strong><span>Missing reviewed statements from: ${missing.join(", ")}.</span>`;
          button.classList.remove("answered");
        } else {
          result.innerHTML = `<strong>${button.dataset.answer}</strong><span>Evidence path: ${button.dataset.path}</span>`;
          button.classList.add("answered");
        }
        const allAnswerable = [...lab.querySelectorAll("[data-graph-question]")].every((question) => {
          const needed = JSON.parse(question.dataset.requires || "[]");
          return tested.has(question.dataset.graphQuestion) && needed.every((source) => loaded.has(source));
        });
        feedback.textContent = allAnswerable
          ? "All three questions are answerable through explicit, source-bounded paths."
          : "Keep growing the graph until every question has a complete evidence path.";
        feedback.className = `feedback ${allAnswerable ? "good" : ""}`;
        if (allAnswerable) mark(lab.dataset.completion);
      });
    });

    lab.querySelector("[data-reset-graph]")?.addEventListener("click", () => {
      loaded.clear();
      tested.clear();
      result.textContent = "No question tested yet.";
      lab.querySelectorAll("[data-graph-question]").forEach((button) => button.classList.remove("answered"));
      renderLedger();
    });
    renderLedger();
  });

  document.querySelectorAll("[data-hierarchy-repair]").forEach((lab) => {
    const cases = [...lab.querySelectorAll("[data-hierarchy-case]")];
    const feedback = lab.querySelector("[data-feedback]");
    cases.forEach((card) => card.querySelectorAll("[data-hierarchy-choice]").forEach((button) => button.addEventListener("click", () => {
      const correct = button.dataset.hierarchyChoice === card.dataset.answer;
      card.querySelectorAll("button").forEach((item) => item.classList.toggle("selected", item === button));
      card.dataset.passed = String(correct);
      card.querySelector("[data-item-feedback]").textContent = correct ? card.dataset.explanation : `Review the semantic consequence. ${card.dataset.explanation}`;
      const passed = cases.filter((item) => item.dataset.passed === "true").length;
      feedback.textContent = passed === cases.length ? "The hierarchy now preserves the intended utility meanings." : `${passed} of ${cases.length} decisions are defensible.`;
      if (passed === cases.length) mark(lab.dataset.completion);
    })));
  });

  document.querySelectorAll("[data-ontology-canvas]").forEach((canvas) => {
    canvas.querySelector("[data-check-canvas]")?.addEventListener("click", () => {
      const fields = [...canvas.querySelectorAll("[data-canvas-answer]")];
      let correct = 0;
      fields.forEach((field) => {
        const passed = field.value === field.dataset.canvasAnswer;
        field.closest(".canvas-card").querySelector("[data-item-feedback]").textContent = passed
          ? field.closest(".canvas-card").querySelector("[data-item-feedback]").dataset.explanation
          : "Recheck the competency question, scope, and evidence boundary.";
        if (passed) correct += 1;
      });
      const feedback = canvas.querySelector("[data-feedback]");
      feedback.textContent = correct === fields.length ? "The ontology slice is bounded, testable, and ready for domain review." : `${correct} of ${fields.length} modeling decisions pass.`;
      feedback.className = `feedback ${correct === fields.length ? "good" : "bad"}`;
      if (correct === fields.length) mark(canvas.dataset.completion);
    });
  });

  document.querySelectorAll("[data-sparql-builder]").forEach((lab) => {
    const clauses = [...lab.querySelectorAll("[data-query-clause]")];
    const selected = [];
    const code = lab.querySelector("[data-query-code]");
    const effect = lab.querySelector("[data-query-effect]");
    const feedback = lab.querySelector("[data-feedback]");
    clauses.forEach((button, index) => button.addEventListener("click", () => {
      if (index !== selected.length) {
        effect.textContent = `Clause ${index + 1} cannot run yet. Add clause ${selected.length + 1} first.`;
        return;
      }
      selected.push(button.dataset.code);
      button.classList.add("selected");
      button.disabled = true;
      code.textContent = selected.join("\n");
      effect.textContent = button.dataset.effect;
      feedback.textContent = selected.length === clauses.length ? "The complete query pattern returns source-traceable bindings." : `Clause ${selected.length} added. Continue in order.`;
      if (selected.length === clauses.length) mark(lab.dataset.completion);
    }));
    lab.querySelector("[data-reset-query]")?.addEventListener("click", () => {
      selected.length = 0;
      clauses.forEach((button) => { button.disabled = false; button.classList.remove("selected"); });
      code.textContent = "# Select clause 1 to begin";
      effect.textContent = "The graph pattern will illuminate here.";
    });
  });

  [
    ["[data-inference-court]", "[data-inference-case]", "[data-inference-choice]", "inferenceChoice", "The court has resolved every proposed inference."],
    ["[data-shacl-clinic]", "[data-shacl-case]", "[data-shacl-choice]", "shaclChoice", "Every record now has a defensible validation disposition."],
    ["[data-evidence-reconciliation]", "[data-evidence-case]", "[data-evidence-choice]", "evidenceChoice", "Every claim now has an explicit governing-use disposition."]
    ,["[data-knowledge-spine-router]", "[data-spine-case]", "[data-spine-choice]", "spineChoice", "Every capability now sits in its defensible operating layer."]
    ,["[data-accountability-handoff]", "[data-handoff-case]", "[data-handoff-choice]", "handoffChoice", "Every operating decision now has an accountable owner."]
    ,["[data-mapping-workbench]", "[data-mapping-case]", "[data-mapping-choice]", "mappingChoice", "Every source field now resolves to a bounded semantic target."]
    ,["[data-mapping-break-repair]", "[data-map-repair-case]", "[data-map-repair-choice]", "mapRepairChoice", "Every mapping defect now has a governed repair."]
    ,["[data-access-pattern-stress-test]", "[data-access-case]", "[data-access-choice]", "accessChoice", "Every workload now has a defensible access pattern."]
    ,["[data-stale-copy-diagnosis]", "[data-stale-case]", "[data-stale-choice]", "staleChoice", "Every stale-copy failure now has an effective control."]
  ].forEach(([labSelector, caseSelector, choiceSelector, choiceKey, success]) => {
    document.querySelectorAll(labSelector).forEach((lab) => {
      const cases = [...lab.querySelectorAll(caseSelector)];
      const feedback = lab.querySelector("[data-feedback]");
      cases.forEach((card) => card.querySelectorAll(choiceSelector).forEach((button) => button.addEventListener("click", () => {
        const correct = button.dataset[choiceKey] === card.dataset.answer;
        card.querySelectorAll(choiceSelector).forEach((item) => item.classList.toggle("selected", item === button));
        card.classList.toggle("passed", correct);
        card.classList.toggle("failed", !correct);
        card.dataset.passed = String(correct);
        card.querySelector("[data-item-feedback]").textContent = correct ? card.dataset.explanation : `Reopen the evidence and declared control. ${card.dataset.explanation}`;
        const passed = cases.filter((item) => item.dataset.passed === "true").length;
        feedback.textContent = passed === cases.length ? success : `${passed} of ${cases.length} cases resolved correctly.`;
        feedback.className = `feedback ${passed === cases.length ? "good" : ""}`;
        if (passed === cases.length) mark(lab.dataset.completion);
      })));
    });
  });

  document.querySelectorAll("[data-work-product]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const fields = [...form.querySelectorAll("[required]")];
      const complete = fields.every((field) => field.value.trim());
      const feedback = form.querySelector("[data-feedback]");
      if (!complete) {
        feedback.textContent = form.dataset.incorrectFeedback;
        feedback.className = "feedback bad";
        return;
      }
      const record = Object.fromEntries(fields.map((field) => [field.name, field.value.trim()]));
      form.querySelector("[data-artifact-preview]").textContent = JSON.stringify(record, null, 2);
      localStorage.setItem(`${stateKey}:artifact:${form.dataset.workProduct}`, JSON.stringify(record));
      feedback.textContent = form.dataset.correctFeedback;
      feedback.className = "feedback good";
      mark(form.dataset.completion);
    });
  });

  function openDrawer(name, trigger) {
    const drawer = document.querySelector(`[data-drawer="${name}"]`);
    if (!drawer) return;
    lastDrawerTrigger = trigger;
    document.querySelector("[data-drawer-scrim]").classList.add("open");
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    drawer.querySelector("button, a, input")?.focus();
  }

  function closeDrawers() {
    document.querySelector("[data-drawer-scrim]").classList.remove("open");
    document.querySelectorAll("[data-drawer]").forEach((drawer) => {
      drawer.classList.remove("open");
      drawer.setAttribute("aria-hidden", "true");
    });
    lastDrawerTrigger?.focus();
  }

  document.querySelectorAll("[data-open-drawer]").forEach((button) => {
    button.addEventListener("click", () => openDrawer(button.dataset.openDrawer, button));
  });
  document.querySelectorAll("[data-close-drawer], [data-drawer-scrim]").forEach((button) => {
    button.addEventListener("click", closeDrawers);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeDrawers();
  });

  document.querySelector("[data-complete-module]")?.addEventListener("click", () => {
    const status = document.querySelector("[data-completion-status]");
    status.textContent = "Working candidate completed locally. This does not issue a credential or operational authority.";
  });

  refreshCompletion();
})();
