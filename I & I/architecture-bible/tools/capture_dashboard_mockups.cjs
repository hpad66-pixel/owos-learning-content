const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const packageDir = path.resolve(__dirname, "..");
const source = path.join(packageDir, "dashboard-mockups", "index.html");
const outputDir = path.join(packageDir, "dashboard-mockups", "screenshots");
const views = [
  ["fleet", "01-fleet-command-center.png"],
  ["basin", "02-basin-and-ii-workspace.png"],
  ["station", "03-station-hydraulics-resiliency.png"],
  ["operations", "04-operations-cycling-energy.png"],
  ["economics", "05-program-economics.png"],
  ["manuals", "06-asset-manual-compliance.png"],
  ["gaps", "07-data-gap-center.png"],
  ["actions", "08-action-approval-center.png"],
  ["lineage", "09-calculation-lineage-explorer.png"],
];

(async () => {
  fs.mkdirSync(outputDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1000 },
    deviceScaleFactor: 1,
  });
  const errors = [];
  page.on("pageerror", error => errors.push(String(error)));
  await page.goto(`file://${source}`, { waitUntil: "load" });
  for (const [view, filename] of views) {
    await page.click(`[data-view="${view}"]`);
    await page.waitForTimeout(80);
    const visibleText = await page.locator("#ii-dashboard-prototype").innerText();
    if (visibleText.includes("undefined")) {
      throw new Error(`Visible undefined value in dashboard ${view}`);
    }
    await page.locator("#ii-dashboard-prototype").screenshot({
      path: path.join(outputDir, filename),
      animations: "disabled",
    });
  }
  await browser.close();
  if (errors.length) {
    throw new Error(`Dashboard JavaScript errors: ${errors.join(" | ")}`);
  }
  console.log(`PASS: captured ${views.length} populated dashboard mockups`);
})();
