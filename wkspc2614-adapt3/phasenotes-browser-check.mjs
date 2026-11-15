import { chromium } from 'playwright';

const BASE = 'http://127.0.0.1:9025/';
const PAGE_HASH = '#/id/L01-co-01';

const results = [];
function record(label, ok, detail) {
  results.push({ label, ok, detail });
  console.log(`${ok ? 'PASS' : 'FAIL'} — ${label}${detail ? ' :: ' + detail : ''}`);
}

const browser = await chromium.launch();
const page = await browser.newPage();
page.on('pageerror', err => console.log('  [pageerror]', err.message));

await page.goto(BASE + PAGE_HASH, { waitUntil: 'networkidle' });
await page.waitForTimeout(1200);

// 1. Nav button present, panel opens, Escape closes + returns focus
const toggle = page.locator('.grow-phasenotes__toggle');
record('1a. ink_pen nav button present', await toggle.count() === 1);
await toggle.click();
await page.waitForTimeout(200);
record('1b. panel opens on click', await page.locator('.grow-phasenotes__panel').isVisible());
await page.keyboard.press('Escape');
await page.waitForTimeout(200);
const panelClosed = !(await page.locator('.grow-phasenotes__panel').isVisible());
const focusReturnedToToggle = await page.evaluate(() => document.activeElement?.classList.contains('grow-phasenotes__toggle'));
record('1c. Escape closes panel and returns focus to toggle', panelClosed && focusReturnedToToggle);

// 2. Initial DOM state: only article 1, no notes, no mirror (a-02 not eligible yet)
record('2a. exactly 1 article in DOM on load', await page.locator('.article').count() === 1);
record('2b. no notes in DOM yet', await page.locator('.grow-phasenotes__note').count() === 0);
record('2c. no mirror button yet', await page.locator('.grow-phasenotes__mirror').count() === 0);

// Drive article 1's own growOutcomes gate to completion (this page's trickle
// button is configured hidden before/after click — growOutcomes is the only
// visible affordance and proxies to the real, always-invisible trickle
// button once its own reveal sequence completes). This is a *different*
// plugin's interaction, not part of adapt-grow-phasenotes.
const revealBtn = page.locator('.js-grow-outcomes-reveal');
for (let i = 0; i < 10; i++) {
  if (!(await revealBtn.isVisible().catch(() => false))) break;
  await revealBtn.click();
  await page.waitForTimeout(400);
}
await page.waitForTimeout(1200);

const articleCountAfter = await page.locator('.article').count();
record('3a. all 5 articles present after the gate clears', articleCountAfter === 5, `found ${articleCountAfter}`);

// Since this page's trickle button is styled hidden both before and after
// click (_styleBeforeCompletion/_styleAfterClick: "hidden"), it is never a
// "real, visible" button per mirrorButton.js's own isRealButtonUsable()
// check — so no mirror is expected here; a-02/a-03's notes should reveal in
// full as soon as each article is eligible (Pattern B/no-visible-button row
// of the mirror table).
const mirrorCount = await page.locator('.grow-phasenotes__mirror').count();
record('3b. no mirror for a hidden-styled trickle button (correct per spec)', mirrorCount === 0, `found ${mirrorCount}`);

const visibleNotes = await page.locator('.grow-phasenotes__note:not([hidden])').count();
record('3c. a-02/a-03 notes reveal in full once eligible (no mirror claimed them)', visibleNotes >= 3, `found ${visibleNotes} visible`);

// 6. Untick show notes -> hide, retick -> restore, no replay/node churn
await toggle.click();
await page.waitForTimeout(200);
const visBtn = page.locator('.grow-phasenotes__vis');
const visibleBefore = await page.locator('.grow-phasenotes__note:not([hidden])').count();
const nodeCountBefore = await page.locator('.grow-phasenotes__note').count();
await visBtn.click();
await page.waitForTimeout(200);
const visibleAfterHide = await page.locator('.grow-phasenotes__note:not([hidden])').count();
record('6a. hide toggle hides all visible notes', visibleAfterHide === 0, `before=${visibleBefore} after=${visibleAfterHide}`);
const visOffClass = await visBtn.evaluate(el => el.classList.contains('is-off') && el.getAttribute('aria-checked') === 'false');
record('6b. vis toggle reflects is-off + aria-checked=false while hidden', visOffClass);
await visBtn.click();
await page.waitForTimeout(200);
const visibleAfterReshow = await page.locator('.grow-phasenotes__note:not([hidden])').count();
const nodeCountAfterReshow = await page.locator('.grow-phasenotes__note').count();
record('6c. re-show restores exactly the previous set, no node churn', visibleAfterReshow === visibleBefore && nodeCountBefore === nodeCountAfterReshow);

// 7. Set switcher: select a-02's set, only that set's notes visible
const setRadios = page.locator('.grow-phasenotes__opt[data-set]:not([data-set="all"])');
const setCount = await setRadios.count();
record('7a. set switcher lists per-article sets', setCount === 2, `found ${setCount} (expect 2: a-02, a-03)`);
if (setCount >= 1) {
  await setRadios.nth(0).click();
  await page.waitForTimeout(200);
  const checked = await setRadios.nth(0).getAttribute('aria-checked');
  const visibleAfterFilter = await page.locator('.grow-phasenotes__note:not([hidden])').count();
  record('7b. selecting a set marks it aria-checked and filters visible notes', checked === 'true' && visibleAfterFilter < visibleBefore,
    `checked=${checked} visible=${visibleAfterFilter} (was ${visibleBefore})`);
  const allRadio = page.locator('.grow-phasenotes__opt[data-set="all"]');
  await allRadio.click();
  await page.waitForTimeout(200);
  const visibleAfterAll = await page.locator('.grow-phasenotes__note:not([hidden])').count();
  record('7c. "All notes" restores the full visible set', visibleAfterAll === visibleBefore, `visible=${visibleAfterAll}`);
}

// 13. Shared drawing assets injected exactly once each (shared with adapt-grow-pagenotes guards)
const assetCount = await page.locator('#grow-pagenotes-marks-css, #grow-pagenotes-chalk-css, #am-ink').count();
record('13. shared drawing assets injected exactly once each', assetCount === 3, `found ${assetCount}`);

// 10. A page with no authored notes gets no nav button at all (menu page)
await page.goto(BASE + '#/', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);
const navBtnOnMenu = await page.locator('.grow-phasenotes__toggle').count();
record('10. no nav button at all on the course menu (no authored notes)', navBtnOnMenu === 0, `found ${navBtnOnMenu}`);

await browser.close();

const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} checks passed.`);
process.exit(failed.length ? 1 : 0);
