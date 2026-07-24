const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const lesson = process.env.OWOS_LESSON_URL || "file:///Users/apas/dev/owos-learning-content/apps/meaning-before-models/modules/module-04-from-triples-to-a-utility-knowledge-graph/build/index.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-04");

async function inspect(browser, mode) {
  const mobile = mode === "phone";
  const tablet = mode === "tablet";
  const context = await browser.newContext({
    viewport: mobile ? {width: 390, height: 844} : tablet ? {width: 820, height: 1080} : {width: 1440, height: 1000},
    reducedMotion: mobile ? "reduce" : "no-preference",
    hasTouch: mobile || tablet,
    isMobile: mobile,
  });
  const page = await context.newPage();
  const errors = [];
  page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lesson, {waitUntil: "load"});
  await page.waitForSelector("main");
  await page.evaluate(async () => Promise.all([...document.images].map((image) => image.complete && image.naturalWidth > 0 ? Promise.resolve() : image.decode())));

  const graph = page.getByRole("button", {name: "Graph"}).first();
  await graph.click();
  const graphDrawer = page.locator('[data-drawer="graph"]');
  const graphOpen = await graphDrawer.getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await graphDrawer.getAttribute("aria-hidden") === "true";
  const graphFocusReturned = await graph.evaluate((node) => document.activeElement === node);
  await page.getByRole("button", {name: "Glossary"}).click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");

  async function choose(id) {
    const group = page.locator(`#${id}`);
    await group.locator("[data-choice][data-correct=true]").click();
    await group.getByRole("button", {name: "Check my answer"}).click();
  }
  await choose("mbm04-opening-edge");

  const flips = page.locator("#mbm04-graph-literacy [data-flip-card]");
  for (let index = 0; index < await flips.count(); index += 1) await flips.nth(index).click();

  const matching = page.locator("#mbm04-relationship-match");
  const matchFields = matching.locator("[data-match-answer]");
  for (let index = 0; index < await matchFields.count(); index += 1) {
    const field = matchFields.nth(index);
    await field.selectOption(await field.getAttribute("data-match-answer"));
  }
  await matching.getByRole("button", {name: "Check the matches"}).click();

  const growth = page.locator("#mbm04-graph-growth");
  const packets = growth.locator("[data-source-packet]");
  for (let index = 0; index < await packets.count(); index += 1) await packets.nth(index).click();
  const questions = growth.locator("[data-graph-question]");
  for (let index = 0; index < await questions.count(); index += 1) await questions.nth(index).click();

  const pathLab = page.locator("#mbm04-path-defense");
  const edges = pathLab.locator("[data-edge-index]");
  for (let index = 0; index < await edges.count(); index += 1) await edges.nth(index).click();

  const boundary = page.locator("#mbm04-boundary-check");
  const options = boundary.locator("[data-multi-option]");
  for (let index = 0; index < await options.count(); index += 1) {
    const option = options.nth(index);
    if (await option.getAttribute("data-correct") === "true") await option.check();
  }
  await boundary.getByRole("button", {name: "Check the packet"}).click();
  await choose("mbm04-transfer-decision");

  const artifact = page.locator("#mbm04-mini-graph form");
  const fields = artifact.locator("[required]");
  for (let index = 0; index < await fields.count(); index += 1) {
    await fields.nth(index).fill(`Specific reviewable Module 04 graph evidence ${index + 1}`);
  }
  await artifact.getByRole("button", {name: "Save Utility Mini-Graph"}).click();

  const state = await page.evaluate(() => ({
    h1Count: document.querySelectorAll("h1").length,
    sectionCount: document.querySelectorAll(".lesson-section").length,
    visualCount: document.querySelectorAll(".learning-visual").length,
    visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
    imagesLoaded: [...document.images].every((image) => image.complete && image.naturalWidth > 0),
    requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
    completeEnabled: !document.querySelector("[data-complete-module]").disabled,
    statementCount: document.querySelectorAll(".ledger-statement").length,
    answeredQuestions: document.querySelectorAll(".graph-question.answered").length,
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    emptyButtons: [...document.querySelectorAll("button")].filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
    maxTransitionMs: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
      const duration = getComputedStyle(node).transitionDuration.split(",")[0];
      return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
    }).filter(Number.isFinite)),
  }));
  const captureDir = path.join(captureRoot, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await growth.screenshot({path: path.join(captureDir, "graph-growth-lab.png")});
  await pathLab.screenshot({path: path.join(captureDir, "answer-path.png")});
  await context.close();
  return {mode, errors, graphOpen, graphClosed, graphFocusReturned, glossaryOpen, ...state};
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chrome});
  const results = [];
  for (const mode of ["desktop", "tablet", "phone"]) results.push(await inspect(browser, mode));
  await browser.close();
  const failures = [];
  for (const result of results) {
    if (result.errors.length) failures.push({mode: result.mode, errors: result.errors});
    if (!result.graphOpen || !result.graphClosed || !result.graphFocusReturned || !result.glossaryOpen) failures.push({mode: result.mode, drawers: result});
    if (result.h1Count !== 1 || result.sectionCount !== 9 || result.visualCount !== 5 || !result.imagesLoaded) failures.push({mode: result.mode, visuals: result});
    if (new Set(result.visualTypes).size !== 5) failures.push({mode: result.mode, visualTypes: result.visualTypes});
    if (!result.requiredComplete || !result.completeEnabled || result.statementCount !== 30 || result.answeredQuestions !== 3) failures.push({mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons) failures.push({mode: result.mode, layout: result});
    if (result.mode === "phone" && result.maxTransitionMs > 1) failures.push({mode: result.mode, reducedMotionMs: result.maxTransitionMs});
  }
  console.log(JSON.stringify({pageRuns: results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
