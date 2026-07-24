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
