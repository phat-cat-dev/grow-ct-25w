/**
 * Bespoke a11y + focus-sequence check for adapt-grow-phasenotes, scoped to
 * L01-co-01 on the reflective-practice-introductory course (port 9025).
 *
 * This is NOT a run of the repo's test-accessibility-scan.mjs /
 * test-focus-sequence-scan.mjs — those are hardcoded to a different course
 * (localhost:9000, "Academic Writing: Introductory Stage", a fixed 9-page
 * set) and do not target this page at all. Written separately, using the
 * same axe-core/playwright libraries, to avoid misreporting a scan of the
 * wrong course as verification of this extension.
 */
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const BASE = 'http://127.0.0.1:9025/';
const PAGE_HASH = '#/id/L01-co-01';
const SEVERITY_ORDER = { critical: 0, serious: 1, moderate: 2, minor: 3 };

function report(label, violations) {
  if (violations.length === 0) {
    console.log(`PASS — ${label}: 0 violations`);
    return 0;
  }
  console.log(`FAIL — ${label}: ${violations.length} violation(s)`);
  for (const v of violations.sort((a, b) => SEVERITY_ORDER[a.impact] - SEVERITY_ORDER[b.impact])) {
    console.log(`  [${v.impact}] ${v.id}: ${v.help} (${v.nodes.length} node(s))`);
    for (const n of v.nodes.slice(0, 3)) console.log(`    - ${n.target.join(' ')}`);
  }
  return violations.length;
}

async function scan(page, label) {
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();
  return report(label, results.violations);
}

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
let totalViolations = 0;

await page.goto(BASE + PAGE_HASH, { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);
totalViolations += await scan(page, '1. page load, panel closed, notes not yet eligible');

const toggle = page.locator('.grow-phasenotes__toggle');
await toggle.click();
await page.waitForTimeout(200);
totalViolations += await scan(page, '2. nav panel open');

await page.keyboard.press('Escape');
await page.waitForTimeout(200);

// Drive the growOutcomes gate to reveal articles 2-5 and the a-02/a-03 notes
// (same interaction as phasenotes-browser-check.mjs; see that file's comment
// for why this is the correct real-page interaction rather than the real
// trickle button directly).
const revealBtn = page.locator('.js-grow-outcomes-reveal');
for (let i = 0; i < 10; i++) {
  if (!(await revealBtn.isVisible().catch(() => false))) break;
  await revealBtn.click();
  await page.waitForTimeout(400);
}
await page.waitForTimeout(1200);
totalViolations += await scan(page, '3. articles 2-5 revealed, notes visible');

await toggle.click();
await page.waitForTimeout(200);
totalViolations += await scan(page, '4. nav panel open with set-switcher populated');

const setRadios = page.locator('.grow-phasenotes__opt[data-set]:not([data-set="all"])');
if (await setRadios.count() >= 1) {
  await setRadios.nth(0).click();
  await page.waitForTimeout(200);
  totalViolations += await scan(page, '5. one set selected, filtered notes visible');
}
await toggle.click();
await page.waitForTimeout(200);

// Focus-sequence trace: Tab through the whole nav button + panel widget only
// (not the full page — that duplicates the repo's existing focus scanner's
// job for content outside this extension's scope).
console.log('\n--- Focus sequence through grow-phasenotes nav widget ---');
await toggle.focus();
await page.waitForTimeout(100);
const seen = [];
let trapped = false;
for (let i = 0; i < 12; i++) {
  const info = await page.evaluate(() => {
    const el = document.activeElement;
    return el ? { tag: el.tagName.toLowerCase(), cls: Array.from(el.classList).join(' '), role: el.getAttribute('role') } : null;
  });
  const key = JSON.stringify(info);
  console.log(`  [${i}] ${key}`);
  if (seen.length >= 2 && seen[seen.length - 1] === key && seen[seen.length - 2] === key) {
    trapped = true;
    break;
  }
  seen.push(key);
  await page.keyboard.press('Tab');
  await page.waitForTimeout(80);
}
console.log(trapped ? 'FAIL — focus appears trapped (same element 3x running)' : 'PASS — no repeated-element focus trap detected in nav widget sequence');
if (trapped) totalViolations += 1;

await browser.close();
console.log(`\nTotal violations/failures across all checks: ${totalViolations}`);
process.exit(totalViolations ? 1 : 0);
