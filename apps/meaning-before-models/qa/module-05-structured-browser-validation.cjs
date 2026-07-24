const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const lesson = process.env.OWOS_LESSON_URL || "file:///Users/apas/dev/owos-learning-content/apps/meaning-before-models/modules/module-05-five-layers-of-meaning/build/index.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-05");

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
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lesson, {waitUntil: "load"});
  await page.waitForSelector("main");

  const graph = page.getByRole("button", {name: "Graph"}).first();
  await graph.click();
  const graphDrawer = page.locator('[data-drawer="graph"]');
  const graphOpen = await graphDrawer.getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await graphDrawer.getAttribute("aria-hidden") === "true";
  const graphFocusReturned = await graph.evaluate((node) => document.activeElement === node);

  const glossary = page.getByRole("button", {name: "Glossary"});
  await glossary.click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");

  async function choose(id, text) {
    const group = page.locator(`#${id}`);
    await group.getByRole("button", {name: text, exact: true}).click();
    await group.getByRole("button", {name: "Check my answer"}).click();
  }

  await choose("mbm05-opening-decision", "A governed definition and relationship model, resolved through tested mappings and bounded by current context");

  const matching = page.locator("#mbm05-job-question-match");
  const matchFields = matching.locator("[data-match-answer]");
  for (let index = 0; index < await matchFields.count(); index += 1) {
    const field = matchFields.nth(index);
    await field.selectOption(await field.getAttribute("data-match-answer"));
  }
  await matching.getByRole("button", {name: "Check the matches"}).click();

  const triage = page.locator("#mbm05-meaning-triage-desk");
  const triageItems = triage.locator("[data-triage-item]");
  for (let index = 0; index < await triageItems.count(); index += 1) {
    const item = triageItems.nth(index);
    await item.locator("select").selectOption(await item.getAttribute("data-answer"));
  }
  await triage.getByRole("button", {name: "Check the desk"}).click();

  await choose("mbm05-broken-boundary", "Semantic layer, because the concept-to-source mapping drifted");

  const packet = page.locator("#mbm05-context-omission-excess");
  const packetOptions = packet.locator("[data-multi-option]");
  for (let index = 0; index < await packetOptions.count(); index += 1) {
    const option = packetOptions.nth(index);
    if (await option.getAttribute("data-correct") === "true") await option.check();
  }
  await packet.getByRole("button", {name: "Check the packet"}).click();

  const failure = page.locator("#mbm05-missing-job-trace");
  const triggers = failure.locator("[data-failure-trigger]");
  for (let index = 0; index < await triggers.count(); index += 1) {
    await triggers.nth(index).click();
  }

  await choose("mbm05-diagnose-and-repair", "Repair and regression-test the semantic mapping");
  await choose("mbm05-transfer-diagnosis", "AI context, because effective time and current authority were not enforced");

  const artifact = page.locator("#mbm05-five-layer-map form");
  const fields = artifact.locator("[required]");
  for (let index = 0; index < await fields.count(); index += 1) {
    await fields.nth(index).fill(`Specific reviewable Module 05 evidence ${index + 1}`);
  }
  await artifact.getByRole("button", {name: "Save Five-Layer Meaning Map"}).click();

  const state = await page.evaluate(() => {
    const images = [...document.images];
    const darkSurfaces = [...document.querySelectorAll(".component-header, .conclusion, .connected article, .failure-result, footer")];
    return {
      h1Count: document.querySelectorAll("h1").length,
      sectionCount: document.querySelectorAll(".lesson-section").length,
      visualCount: document.querySelectorAll(".learning-visual").length,
      visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
      imagesLoaded: images.every((image) => image.complete && image.naturalWidth > 0),
      requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
      completeEnabled: !document.querySelector("[data-complete-module]").disabled,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label")
      ).length,
      darkTextFailures: darkSurfaces.filter((node) => {
        const color = getComputedStyle(node).color;
        const match = color.match(/\d+/g)?.map(Number) || [];
        return match.length >= 3 && match[0] < 180 && match[1] < 180 && match[2] < 180;
      }).length,
      maxTransitionMs: Math.max(
        0,
        ...[...document.querySelectorAll("*")].map((node) => {
          const duration = getComputedStyle(node).transitionDuration.split(",")[0];
          return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
        }).filter(Number.isFinite)
      ),
    };
  });

  const captureDir = path.join(captureRoot, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await page.locator("#mbm05-pressure-room").screenshot({path: path.join(captureDir, "pressure-room.png")});
  await page.locator("#mbm05-meaning-triage-desk").screenshot({path: path.join(captureDir, "triage-desk.png")});
  await page.locator("#mbm05-missing-job-trace").screenshot({path: path.join(captureDir, "failure-lab.png")});
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
    if (!result.graphOpen || !result.graphClosed || !result.graphFocusReturned || !result.glossaryOpen) {
      failures.push({mode: result.mode, drawers: result});
    }
    if (result.h1Count !== 1 || result.sectionCount !== 9 || result.visualCount !== 5 || !result.imagesLoaded) {
      failures.push({mode: result.mode, visuals: result});
    }
    if (new Set(result.visualTypes).size !== 5) failures.push({mode: result.mode, visualTypes: result.visualTypes});
    if (!result.requiredComplete || !result.completeEnabled) failures.push({mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons || result.darkTextFailures) {
      failures.push({mode: result.mode, layout: result});
    }
    if (result.mode === "phone" && result.maxTransitionMs > 1) {
      failures.push({mode: result.mode, reducedMotionMs: result.maxTransitionMs});
    }
  }
  console.log(JSON.stringify({pageRuns: results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
