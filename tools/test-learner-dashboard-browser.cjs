const { chromium } = require("playwright");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

const root = path.resolve(__dirname, "..");
const target = path.join(root, "examples/learner-dashboard/index.html");
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const modes = [
  { name: "desktop", width: 1440, height: 1000, reducedMotion: "no-preference" },
  { name: "tablet", width: 820, height: 1180, reducedMotion: "no-preference" },
  { name: "phone-reduced-motion", width: 390, height: 844, reducedMotion: "reduce" },
];

async function inspect(browser, mode) {
  const page = await browser.newPage({
    viewport: { width: mode.width, height: mode.height },
    reducedMotion: mode.reducedMotion,
  });
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(pathToFileURL(target).href, { waitUntil: "load" });

  await page.locator("body").click({ position: { x: 2, y: 2 } });
  for (let index = 0; index < 4; index += 1) {
    await page.keyboard.press("Tab");
    const focusedButton = await page.evaluate(
      () => document.activeElement?.tagName === "BUTTON",
    );
    if (focusedButton) break;
  }
  const focus = await page.evaluate(() => ({
    tag: document.activeElement?.tagName || "",
    outline: getComputedStyle(document.activeElement).outlineStyle,
  }));

  const state = await page.evaluate(() => ({
    h1: document.querySelectorAll("h1").length,
    main: document.querySelectorAll("main").length,
    stats: document.querySelectorAll(".stat").length,
    credentialStates: document.querySelectorAll(".credential .status").length,
    pathways: document.querySelectorAll(".path").length,
    lanes: [...document.querySelectorAll(".path")].map((node) => node.dataset.lane).sort(),
    buttons: document.querySelectorAll("button").length,
    labeledProgress: Boolean(document.querySelector(".progress[aria-label]")),
    ledger: Boolean(document.querySelector("table.ledger")),
    boundary: /specimen/i.test(document.querySelector(".boundary")?.innerText || ""),
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    reduced: matchMedia("(prefers-reduced-motion: reduce)").matches,
    emptyButtons: [...document.querySelectorAll("button")].filter(
      (button) => !button.textContent.trim() && !button.getAttribute("aria-label"),
    ).length,
  }));
  await page.close();
  return { mode: mode.name, errors, focus, ...state };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const mode of modes) results.push(await inspect(browser, mode));
  await browser.close();

  const expectedLanes = ["cross-skill", "deepen", "reskill"];
  const failures = results.filter((item) => (
    item.errors.length
    || item.h1 !== 1
    || item.main !== 1
    || item.stats !== 4
    || item.credentialStates !== 1
    || item.pathways !== 3
    || JSON.stringify(item.lanes) !== JSON.stringify(expectedLanes)
    || item.buttons !== 6
    || !item.labeledProgress
    || !item.ledger
    || !item.boundary
    || item.scrollWidth > item.width + 1
    || item.emptyButtons !== 0
    || item.focus.tag !== "BUTTON"
    || item.focus.outline === "none"
    || (item.mode === "phone-reduced-motion" && !item.reduced)
  ));

  console.log(JSON.stringify(results, null, 2));
  if (failures.length) {
    console.error(`Learner dashboard browser QA failed in ${failures.length} mode(s).`);
    process.exit(1);
  }
  console.log("Learner dashboard browser QA passed in desktop, tablet, and reduced-motion phone modes.");
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
