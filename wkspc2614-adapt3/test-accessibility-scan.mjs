/**
 * Accessibility Scan — Academic Writing: Introductory Stage
 *
 * Uses axe-core via @axe-core/playwright to check WCAG 2.1 A and AA compliance
 * across all 9 pages. For dynamic pages (SUMM assessment, confidence components),
 * scans both before and after interaction to catch state-dependent issues.
 *
 * Usage: node test-accessibility-scan.mjs
 * Requires: Playwright, @axe-core/playwright, dev server running on localhost:9001
 */

import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const BASE_URL = 'http://localhost:9001/';

// Severity order for sorting
const SEVERITY_ORDER = { critical: 0, serious: 1, moderate: 2, minor: 3 };

/**
 * Run axe-core scan on current page
 */
async function runAxeScan(page, label) {
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  return {
    label,
    violations: results.violations,
    passes: results.passes.length,
    inapplicable: results.inapplicable.length
  };
}

/**
 * Format a single violation for display
 */
function formatViolation(v) {
  const wcagTags = v.tags.filter(t => t.startsWith('wcag')).join(', ');
  const lines = [
    `  [${v.impact.toUpperCase()}] ${v.id}`,
    `    Description: ${v.description}`,
    `    WCAG: ${wcagTags}`,
    `    Help: ${v.helpUrl}`
  ];

  // List affected elements (limit to first 5)
  const nodes = v.nodes.slice(0, 5);
  for (const node of nodes) {
    const selector = node.target.join(' > ');
    lines.push(`    Element: ${selector}`);
    if (node.html && node.html.length < 200) {
      lines.push(`      HTML: ${node.html}`);
    }
  }
  if (v.nodes.length > 5) {
    lines.push(`    ... and ${v.nodes.length - 5} more elements`);
  }

  return lines.join('\n');
}

/**
 * Click through visible trickle buttons until none remain
 */
async function clickThroughTrickle(page, maxClicks = 20) {
  let clicks = 0;
  while (clicks < maxClicks) {
    await page.waitForTimeout(300);
    const trickleBtn = page.locator('.trickle__btn:visible').first();
    if (await trickleBtn.count() === 0) break;
    const isDisabled = await trickleBtn.evaluate(el => el.classList.contains('is-disabled')).catch(() => true);
    if (isDisabled) break;
    await trickleBtn.click().catch(() => {});
    await page.waitForTimeout(500);
    clicks++;
  }
  return clicks;
}

/**
 * Rate all confidence items (select middle option)
 */
async function rateConfidenceItems(page) {
  const items = await page.locator('.confidence__item').all();
  let rated = 0;

  for (let i = 0; i < items.length; i++) {
    const option = page.locator(`.confidence__item[data-item-index="${i}"] .confidence__option`).nth(2);
    if (await option.isVisible().catch(() => false)) {
      await option.click();
      await page.waitForTimeout(100);
      rated++;
    }
  }
  return rated;
}

/**
 * Submit confidence component
 */
async function submitConfidence(page) {
  const submitBtn = page.locator('.js-confidence-submit').first();
  if (await submitBtn.isEnabled().catch(() => false)) {
    await submitBtn.click();
    await page.waitForTimeout(500);
    return true;
  }
  return false;
}

/**
 * Answer an MCQ by clicking the first option and submitting
 */
async function answerMcq(page, componentSelector) {
  const component = page.locator(componentSelector);
  if (await component.count() === 0) return false;

  const label = component.locator('.mcq-item__label').first();
  if (await label.count() > 0) {
    await label.click();
    await page.waitForTimeout(300);
  }

  const submitBtn = component.locator('.btn__action').first();
  if (await submitBtn.count() > 0) {
    const isEnabled = !(await submitBtn.evaluate(el => el.classList.contains('is-disabled')));
    if (isEnabled) {
      await submitBtn.click();
      await page.waitForTimeout(500);
      return true;
    }
  }
  return false;
}

/**
 * Answer a sortable by submitting (default order)
 */
async function answerSortable(page, componentSelector) {
  const component = page.locator(componentSelector);
  if (await component.count() === 0) return false;

  const submitBtn = component.locator('.btn__action').first();
  if (await submitBtn.count() > 0) {
    const isEnabled = !(await submitBtn.evaluate(el => el.classList.contains('is-disabled')));
    if (isEnabled) {
      await submitBtn.click();
      await page.waitForTimeout(500);
      return true;
    }
  }
  return false;
}

async function runAccessibilityScan() {
  console.log('=== ACCESSIBILITY SCAN ===');
  console.log('Academic Writing: Introductory Stage');
  console.log('WCAG 2.1 A and AA via axe-core\n');

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  const allResults = [];

  try {
    // ==================== W-OPEN ====================
    console.log('Scanning W-OPEN...');
    await page.goto(BASE_URL + '#/id/W-OPEN-co-01', { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);

    // Click through trickle to reveal confidence component
    await clickThroughTrickle(page, 15);
    await page.waitForTimeout(500);

    // Scan BEFORE confidence interaction
    const wopenBefore = await runAxeScan(page, 'W-OPEN (before confidence interaction)');
    allResults.push(wopenBefore);

    // Rate confidence items (but don't submit yet)
    const hasConfidence = await page.locator('.confidence').count() > 0;
    if (hasConfidence) {
      await rateConfidenceItems(page);
      await page.waitForTimeout(300);

      // Scan AFTER rating (aria-checked states now applied)
      const wopenAfterRating = await runAxeScan(page, 'W-OPEN (after confidence rating, before submit)');
      allResults.push(wopenAfterRating);

      // Submit and scan final state
      await submitConfidence(page);
      await page.waitForTimeout(500);
      const wopenAfterSubmit = await runAxeScan(page, 'W-OPEN (after confidence submit)');
      allResults.push(wopenAfterSubmit);
    }

    // ==================== L02-L07 ====================
    const lessons = [
      { id: 'L02-co-01', name: 'L02' },
      { id: 'L03-co-01', name: 'L03' },
      { id: 'L04-co-01', name: 'L04' },
      { id: 'L05-co-01', name: 'L05' },
      { id: 'L06-co-01', name: 'L06' },
      { id: 'L07-co-01', name: 'L07' }
    ];

    for (const lesson of lessons) {
      console.log(`Scanning ${lesson.name}...`);
      await page.goto(BASE_URL + '#/id/' + lesson.id, { waitUntil: 'networkidle' });
      await page.waitForTimeout(1500);

      // Click through trickle to reveal full page
      await clickThroughTrickle(page, 15);
      await page.waitForTimeout(500);

      const result = await runAxeScan(page, lesson.name);
      allResults.push(result);
    }

    // ==================== SUMM (Assessment) ====================
    console.log('Scanning SUMM...');
    await page.goto(BASE_URL + '#/id/SUMM-co-01', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);

    // Scan initial state (before any answers)
    const summBefore = await runAxeScan(page, 'SUMM (initial state)');
    allResults.push(summBefore);

    // Assessment items
    const assessmentItems = [
      { id: 'SUMM-c-10', type: 'mcq' },
      { id: 'SUMM-c-15', type: 'mcq' },
      { id: 'SUMM-c-20', type: 'sortable' },
      { id: 'SUMM-c-25', type: 'sortable' },
      { id: 'SUMM-c-30', type: 'mcq' },
      { id: 'SUMM-c-35', type: 'mcq' },
      { id: 'SUMM-c-40', type: 'mcq' },
      { id: 'SUMM-c-45', type: 'mcq' }
    ];

    // Answer all assessment items
    for (const item of assessmentItems) {
      await clickThroughTrickle(page, 3);
      await page.waitForTimeout(300);

      const selector = `[data-adapt-id="${item.id}"]`;
      if (item.type === 'mcq') {
        await answerMcq(page, selector);
      } else if (item.type === 'sortable') {
        await answerSortable(page, selector);
      }
    }

    // Click through to results
    await clickThroughTrickle(page, 5);
    await page.waitForTimeout(1000);

    // Scan after answering (results page state)
    const summAfter = await runAxeScan(page, 'SUMM (after answering, results page)');
    allResults.push(summAfter);

    // ==================== W-CLOSE ====================
    console.log('Scanning W-CLOSE...');
    await page.goto(BASE_URL + '#/id/W-CLOSE-co-01', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);

    // Click through trickle to reveal confidence POST
    await clickThroughTrickle(page, 10);
    await page.waitForTimeout(500);

    // Scan BEFORE confidence interaction
    const wcloseBefore = await runAxeScan(page, 'W-CLOSE (before confidence interaction)');
    allResults.push(wcloseBefore);

    // Check for confidence POST
    const hasConfidencePost = await page.locator('.confidence').count() > 0;
    if (hasConfidencePost) {
      await rateConfidenceItems(page);
      await page.waitForTimeout(300);

      // Scan after rating
      const wcloseAfterRating = await runAxeScan(page, 'W-CLOSE (after confidence rating)');
      allResults.push(wcloseAfterRating);

      // Submit and scan
      await submitConfidence(page);
      await page.waitForTimeout(500);
      const wcloseAfterSubmit = await runAxeScan(page, 'W-CLOSE (after confidence submit)');
      allResults.push(wcloseAfterSubmit);
    }

  } catch (error) {
    console.log('\n[FATAL ERROR] ' + error.message);
    console.log(error.stack);
  } finally {
    await browser.close();
  }

  // ==================== REPORT ====================
  console.log('\n\n' + '='.repeat(70));
  console.log('ACCESSIBILITY SCAN REPORT');
  console.log('='.repeat(70));

  let totalViolations = 0;
  const violationsByRule = {};
  const violationsByPage = {};

  for (const result of allResults) {
    const pageViolationCount = result.violations.reduce((sum, v) => sum + v.nodes.length, 0);
    violationsByPage[result.label] = pageViolationCount;

    console.log(`\n--- ${result.label} ---`);
    console.log(`Violations: ${result.violations.length} rules, ${pageViolationCount} elements`);
    console.log(`Passed: ${result.passes} rules`);

    if (result.violations.length > 0) {
      // Sort by severity
      const sorted = [...result.violations].sort((a, b) =>
        SEVERITY_ORDER[a.impact] - SEVERITY_ORDER[b.impact]
      );

      for (const v of sorted) {
        console.log(formatViolation(v));

        // Aggregate by rule
        if (!violationsByRule[v.id]) {
          violationsByRule[v.id] = {
            description: v.description,
            impact: v.impact,
            wcag: v.tags.filter(t => t.startsWith('wcag')),
            helpUrl: v.helpUrl,
            pages: [],
            totalNodes: 0
          };
        }
        violationsByRule[v.id].pages.push(result.label);
        violationsByRule[v.id].totalNodes += v.nodes.length;
      }

      totalViolations += result.violations.length;
    } else {
      console.log('  No violations found.');
    }
  }

  // ==================== SUMMARY ====================
  console.log('\n\n' + '='.repeat(70));
  console.log('SUMMARY');
  console.log('='.repeat(70));

  console.log(`\nTotal scans: ${allResults.length}`);
  console.log(`Total unique violation rules: ${Object.keys(violationsByRule).length}`);

  if (Object.keys(violationsByRule).length > 0) {
    console.log('\n--- Violations by Rule (aggregated) ---');

    // Sort rules by severity then by total nodes
    const sortedRules = Object.entries(violationsByRule).sort((a, b) => {
      const sevDiff = SEVERITY_ORDER[a[1].impact] - SEVERITY_ORDER[b[1].impact];
      if (sevDiff !== 0) return sevDiff;
      return b[1].totalNodes - a[1].totalNodes;
    });

    for (const [ruleId, data] of sortedRules) {
      console.log(`\n  [${data.impact.toUpperCase()}] ${ruleId}`);
      console.log(`    ${data.description}`);
      console.log(`    WCAG: ${data.wcag.join(', ')}`);
      console.log(`    Affected pages: ${data.pages.length}`);
      console.log(`    Total elements: ${data.totalNodes}`);
      console.log(`    Pages: ${[...new Set(data.pages)].join(', ')}`);
    }

    console.log('\n--- Violations by Page ---');
    for (const [pageName, count] of Object.entries(violationsByPage)) {
      if (count > 0) {
        console.log(`  ${pageName}: ${count} elements`);
      }
    }
  } else {
    console.log('\nNo WCAG 2.1 A/AA violations found!');
  }

  console.log('\n' + '='.repeat(70));
  console.log('END OF REPORT');
  console.log('='.repeat(70) + '\n');

  process.exit(totalViolations > 0 ? 1 : 0);
}

runAccessibilityScan();
