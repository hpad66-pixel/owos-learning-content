const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const base = "http://127.0.0.1:8765/";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const courses = [
  "apps/project-management/curriculum",
  "apps/data-ai-governance/curriculum",
  "apps/meaning-before-models/curriculum",
];

const targets = courses.flatMap((directory) => (
  fs.readdirSync(path.join(root, directory))
    .filter((name) => /^module-\d\d-.*\.html$/.test(name) && !name.includes(".artifact."))
    .sort()
    .map((name) => `${directory}/${name}`)
));

function durationMs(value) {
  if (!value) return 0;
  return value.endsWith("ms") ? Number.parseFloat(value) : Number.parseFloat(value) * 1000;
}

async function inspect(browser, target, mobile) {
  const page = await browser.newPage({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 },
    reducedMotion: mobile ? "reduce" : "no-preference",
  });
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error" && !message.text().startsWith("Failed to load resource:")) {
      errors.push(message.text());
    }
  });
  page.on("pageerror", (error) => errors.push(error.message));
  page.on("response", (response) => {
    if (response.status() >= 400 && !response.url().endsWith("/favicon.ico")) {
      errors.push(`${response.status()} ${response.url()}`);
    }
  });
  await page.goto(base + target, { waitUntil: "commit", timeout: 15000 });
  await page.waitForSelector("main", { timeout: 10000 });
  await page.waitForTimeout(250);

  const graphTrigger = page.locator("[data-open-graph]:visible, #openGraphHero:visible").first();
  const richGraph = page.locator("#lessonGraph").first();
  const graphDrawer = await richGraph.count()
    ? richGraph
    : page.locator('[data-drawer="graph"]').first();
  let graphOpen = false;
  let graphClosed = false;
  let focusReturned = false;
  if (await graphTrigger.count() && await graphDrawer.count()) {
    await graphTrigger.click();
    graphOpen = await graphDrawer.evaluate((node) => (
      !node.hidden
      || node.getAttribute("aria-hidden") === "false"
      || node.classList.contains("open")
      || node.hasAttribute("open")
    ));
    await page.keyboard.press("Escape");
    graphClosed = await graphDrawer.evaluate((node) => (
      node.hidden
      || node.getAttribute("aria-hidden") === "true"
      || (!node.classList.contains("open") && !node.hasAttribute("open"))
    ));
    focusReturned = await graphTrigger.evaluate((node) => document.activeElement === node);
  }

  const state = await page.evaluate(() => {
    const drawer = document.querySelector('[data-drawer="graph"]');
    const transition = drawer ? getComputedStyle(drawer).transitionDuration : "0s";
    return {
      h1: document.querySelectorAll("h1").length,
      main: document.querySelectorAll("main").length,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      transition,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label")
      ).length,
    };
  });
  await page.close();
  return {
    target,
    mode: mobile ? "mobile-reduced-motion" : "desktop",
    errors,
    graphOpen,
    graphClosed,
    focusReturned,
    ...state,
    transitionMs: durationMs(state.transition),
  };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const target of targets) {
    results.push(await inspect(browser, target, false));
    results.push(await inspect(browser, target, true));
  }
  await browser.close();

  const failures = results.filter((item) => (
    item.errors.length
    || !item.graphOpen
    || !item.graphClosed
    || !item.focusReturned
    || item.h1 !== 1
    || item.main !== 1
    || item.scrollWidth > item.width + 1
    || item.emptyButtons
    || (item.mode === "mobile-reduced-motion" && item.transitionMs > 0.01)
  ));
  console.log(JSON.stringify({
    lessons: targets.length,
    pageRuns: results.length,
    failureCount: failures.length,
    failures,
  }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
