const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const base = "http://127.0.0.1:8787";
const lesson = "/apps/meaning-before-models/modules/module-20-one-water-knowledge-spine-lab/build/index.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captures = path.join(__dirname, "rendered/module-20-prototype");

async function completeDecisionLabs(page) {
  await page.evaluate(() => {
    const labs = [
      ["[data-knowledge-spine-live-lab]", "[data-spine-lab-case]", "[data-spine-lab-choice]", "spineLabChoice"],
      ["[data-graph-path-illuminator]", "[data-path-lab-case]", "[data-path-lab-choice]", "pathLabChoice"],
      ["[data-scenario-transfer-lab]", "[data-transfer-lab-case]", "[data-transfer-lab-choice]", "transferLabChoice"],
    ];
    labs.forEach(([labSelector, caseSelector, choiceSelector, key]) => {
      document.querySelectorAll(labSelector).forEach((lab) => {
        lab.querySelectorAll(caseSelector).forEach((card) => {
          const answer = card.dataset.answer;
          const button = [...card.querySelectorAll(choiceSelector)].find((item) => item.dataset[key] === answer);
          button?.click();
        });
      });
    });
  });
}

async function completeAssessments(page) {
  for (const group of await page.locator("[data-choice-group]").all()) {
    const correct = group.locator('[data-correct="true"]').first();
    await correct.click();
    await group.getByRole("button", {name: "Check my answer"}).click();
  }
  for (const group of await page.locator("[data-multi-select]").all()) {
    const correct = group.locator('[data-correct="true"]');
    for (let index = 0; index < await correct.count(); index += 1) await correct.nth(index).click();
    await group.getByRole("button", {name: "Check the packet"}).click();
  }
  for (const group of await page.locator("[data-matching]").all()) {
    const selects = group.locator("select");
    for (let index = 0; index < await selects.count(); index += 1) {
      const answer = await selects.nth(index).getAttribute("data-match-answer");
      await selects.nth(index).selectOption(answer);
    }
    await group.getByRole("button", {name: "Check the matches"}).click();
  }
  const cards = page.locator("[data-flip-card]");
  for (let index = 0; index < await cards.count(); index += 1) await cards.nth(index).click();
  const work = page.locator("#mbm20-use-case-configuration");
  const fields = work.locator("textarea");
  for (let index = 0; index < await fields.count(); index += 1) {
    await fields.nth(index).fill(`Prototype evidence for governed configuration field ${index + 1}.`);
  }
  await work.getByRole("button", {name: /Save/}).click();
}

async function completePromptGraphFinale(page) {
  const lab = page.locator("#mbm20-prompt-graph-finale");
  await lab.getByRole("button", {name: "Wastewater"}).click();
  await lab.getByRole("button", {name: "Run fixed trace"}).click();
  await page.waitForFunction(() => document.querySelector('[data-completion-id="prompt-graph-finale"]')?.classList.contains("done"));
}

async function inspect(browser, mode) {
  const viewport = mode === "phone" ? {width: 390, height: 844} : mode === "tablet" ? {width: 820, height: 1080} : {width: 1440, height: 1000};
  const context = await browser.newContext({viewport, hasTouch: mode !== "desktop", isMobile: mode === "phone", reducedMotion: mode === "phone" ? "reduce" : "no-preference"});
  const page = await context.newPage();
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error" && !message.text().includes("404 (File not found)")) errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(base + lesson, {waitUntil: "networkidle"});
  await page.waitForSelector("main");

  const graphButton = page.getByRole("button", {name: "Graph"}).first();
  await graphButton.click();
  const graphOpen = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const focusReturned = await graphButton.evaluate((node) => document.activeElement === node);

  await completeDecisionLabs(page);
  await completeAssessments(page);
  await completePromptGraphFinale(page);

  const state = await page.evaluate(() => ({
    title: document.querySelector("h1")?.textContent.trim(),
    visuals: document.querySelectorAll(".learning-visual").length,
    imagesLoaded: [...document.images].every((image) => image.complete && image.naturalWidth > 0),
    interactions: document.querySelectorAll("[data-purposeful-interaction]").length,
    requiredDone: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
    completeEnabled: !document.querySelector("[data-complete-module]")?.disabled,
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    emptyButtons: [...document.querySelectorAll("button")].filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
    maxTransitionMs: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
      const value = getComputedStyle(node).transitionDuration.split(",")[0];
      return value.endsWith("ms") ? Number.parseFloat(value) : Number.parseFloat(value) * 1000;
    }).filter(Number.isFinite)),
  }));

  const dir = path.join(captures, mode);
  fs.mkdirSync(dir, {recursive: true});
  await page.screenshot({path: path.join(dir, "full-page.png"), fullPage: true});
  await page.locator("#mbm20-live-lab").screenshot({path: path.join(dir, "live-lab.png")});
  await page.locator("#mbm20-prompt-graph-finale").screenshot({path: path.join(dir, "prompt-graph-finale.png")});
  await context.close();
  return {mode, errors, graphOpen, focusReturned, ...state};
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chrome});
  const results = [];
  for (const mode of ["desktop", "tablet", "phone"]) results.push(await inspect(browser, mode));
  await browser.close();
  const failures = [];
  for (const result of results) {
    if (result.errors.length) failures.push({mode: result.mode, errors: result.errors});
    if (!result.graphOpen || !result.focusReturned) failures.push({mode: result.mode, drawer: result});
    if (result.visuals !== 8 || !result.imagesLoaded) failures.push({mode: result.mode, visuals: result});
    if (result.interactions !== 12) failures.push({mode: result.mode, interactions: result.interactions});
    if (!result.requiredDone || !result.completeEnabled) failures.push({mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons) failures.push({mode: result.mode, containment: result});
    if (result.mode === "phone" && result.maxTransitionMs > 1) failures.push({mode: result.mode, reducedMotion: result.maxTransitionMs});
  }
  console.log(JSON.stringify({results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
