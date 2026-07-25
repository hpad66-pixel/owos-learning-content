const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const target = process.env.OWOS_TARGET || "curriculum";
const modes = {
  desktop: { width: 1440, height: 1000 },
  tablet: { width: 820, height: 1080 },
  phone: { width: 390, height: 844 },
  zoom200: { width: 720, height: 900 },
  zoom400: { width: 360, height: 800 },
  reducedMotion: { width: 390, height: 844 },
};
const url = target === "dist"
  ? `file://${path.join(root, "dist/site/course-meaning-before-models.html")}`
  : `file://${path.join(root, "curriculum/course-meaning-before-models.html")}`;

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const runs = [];
  for (const [mode, viewport] of Object.entries(modes)) {
    const context = await browser.newContext({
      viewport,
      hasTouch: mode === "tablet" || mode === "phone",
      isMobile: false,
      reducedMotion: mode === "reducedMotion" ? "reduce" : "no-preference",
    });
    const page = await context.newPage();
    const errors = [];
    page.on("console", (message) => {
      if (message.type() === "error") errors.push(message.text());
    });
    page.on("pageerror", (error) => errors.push(error.message));
    await page.goto(url, { waitUntil: "load" });
    await page.getByRole("button", { name: "Graph" }).first().click();
    const graphOpen = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "false";
    await page.keyboard.press("Escape");
    const focusReturned = await page.getByRole("button", { name: "Graph" }).first()
      .evaluate((node) => document.activeElement === node);
    const state = await page.evaluate(() => {
      const hero = document.querySelector(".hero");
      const title = document.querySelector("h1");
      const facts = document.querySelector(".course-facts");
      const links = [...document.querySelectorAll('a[href$=".html"]')]
        .filter((link) => !link.getAttribute("href").includes("course-meaning-before-models"));
      return {
        h1: document.querySelectorAll("h1").length,
        heroVisible: hero && hero.getBoundingClientRect().height > 300,
        titleLines: Math.round(title.getBoundingClientRect().height / parseFloat(getComputedStyle(title).lineHeight)),
        factsVisible: facts && facts.getBoundingClientRect().height > 50,
        lessonLinks: new Set(links.map((link) => link.getAttribute("href"))).size,
        width: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        emptyButtons: [...document.querySelectorAll("button")]
          .filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
        darkTextFailures: [...document.querySelectorAll(".hero-art *")]
          .filter((node) => {
            const color = getComputedStyle(node).color;
            return color === "rgb(16, 32, 51)" || color === "rgb(16, 42, 67)";
          }).length,
      };
    });
    const directory = path.join(__dirname, "rendered", "course-landing", mode);
    fs.mkdirSync(directory, { recursive: true });
    await page.screenshot({ path: path.join(directory, "full-page.png"), fullPage: true });
    await page.locator(".hero").screenshot({ path: path.join(directory, "hero.png") });
    runs.push({ mode, errors, graphOpen, focusReturned, ...state });
    await context.close();
  }
  await browser.close();
  const failures = runs.filter((run) =>
    run.errors.length || !run.graphOpen || !run.focusReturned || run.h1 !== 1 ||
    !run.heroVisible || !run.factsVisible || run.lessonLinks !== 18 ||
    run.scrollWidth > run.width + 1 || run.emptyButtons || run.darkTextFailures);
  console.log(JSON.stringify({ target, runs, failureCount: failures.length, failures }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
