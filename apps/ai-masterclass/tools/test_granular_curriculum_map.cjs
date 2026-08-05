const { chromium } = require("playwright");
const path = require("path");

const pagePath = path.resolve(
  __dirname,
  "../output/html/one-water-ai-granular-curriculum-map.html",
);
const url = `file://${pagePath}`;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

(async () => {
  const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const errors = [];
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  page.on("console", (msg) => {
    if (msg.type() === "error") errors.push(`console: ${msg.text()}`);
  });
  page.on("pageerror", (err) => errors.push(`pageerror: ${err.message}`));
  await page.goto(url, { waitUntil: "load" });

  assert((await page.locator("details.module").count()) === 64, "Expected all 64 modules.");
  assert((await page.locator(".metric").count()) === 4, "Expected four summary metrics.");
  assert((await page.locator(".gap-row:not(.header)").count()) === 37, "Expected 37 gap records.");

  const firstModule = page.locator("details.module").first();
  await firstModule.locator("summary.module-summary").click();
  assert(await firstModule.evaluate((node) => node.open), "Module did not expand.");

  await page.locator("#search").fill("M40.P06");
  assert((await page.locator("details.module").count()) === 1, "Stable-ID search did not isolate Module 40.");
  await page.locator("#search").fill("");
  await page.locator('[data-filter="duplicate"]').click();
  assert((await page.locator(".gap-row:not(.header)").count()) === 1, "Duplicate filter did not isolate the one duplicate.");
  await page.locator('[data-filter="all"]').click();

  const desktopOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  assert(!desktopOverflow, "Desktop view has page-level horizontal overflow.");
  await page.screenshot({ path: "/tmp/one-water-ai-granular-map-desktop.png", fullPage: true });

  await page.setViewportSize({ width: 390, height: 844 });
  await page.reload({ waitUntil: "load" });
  const mobileOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  assert(!mobileOverflow, "Mobile view has page-level horizontal overflow.");
  await page.locator("details.module").first().locator("summary.module-summary").click();
  assert(await page.locator("details.module").first().evaluate((node) => node.open), "Mobile module did not expand.");
  await page.screenshot({ path: "/tmp/one-water-ai-granular-map-mobile.png", fullPage: true });

  assert(errors.length === 0, errors.join("\n"));
  await browser.close();
  console.log(JSON.stringify({
    modules: 64,
    gaps: 37,
    desktopOverflow,
    mobileOverflow,
    errors,
    screenshots: [
      "/tmp/one-water-ai-granular-map-desktop.png",
      "/tmp/one-water-ai-granular-map-mobile.png",
    ],
  }, null, 2));
})().catch((err) => {
  console.error(err.stack || err.message);
  process.exit(1);
});
