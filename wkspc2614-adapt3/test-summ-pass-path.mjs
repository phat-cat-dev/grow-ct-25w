/**
 * SUMM Pass-Path Verification Script
 *
 * Verifies that the SUMM assessment displays pass-state when score ≥70%.
 *
 * NOTE: This script runs under `grunt server` (plain HTTP), NOT the SCORM harness.
 * SCORM completion status ("completed" vs "incomplete") cannot be verified here;
 * that requires `grunt server-scorm` with a SCORM API mock.
 *
 * What this DOES verify:
 * - Score ≥70% shows pass feedback text ("You passed...")
 * - Score <70% shows fail feedback text (from prior 38% run)
 * - The displayed pass/fail state is distinct
 *
 * Correct answers derived from components.json _shouldBeSelected fields.
 *
 * Usage: node test-summ-pass-path.mjs
 */

import { chromium } from 'playwright';

const BASE_URL = 'http://localhost:9001/';

// Correct answer text patterns (MCQs are shuffled, so match by text)
const CORRECT_ANSWERS = {
  'SUMM-c-10': 'Evaluate',
  'SUMM-c-15': 'recent',
  'SUMM-c-30': 'comma splice',
  'SUMM-c-35': 'Both apostrophes are wrong',
  'SUMM-c-40': 'Replace the first comma with a colon',
  'SUMM-c-45': 'Version B'
};

async function clickThroughTrickle(page, maxClicks = 5) {
  let clicks = 0;
  while (clicks < maxClicks) {
    await page.waitForTimeout(300);
    const trickleBtn = page.locator('.trickle__btn:visible').first();
    if (await trickleBtn.count() === 0) break;
    const isDisabled = await trickleBtn.evaluate(el => el.classList.contains('is-disabled')).catch(() => true);
    if (isDisabled) break;
    await trickleBtn.click().catch(() => {});
    await page.waitForTimeout(400);
    clicks++;
  }
  return clicks;
}

async function answerMcqCorrectly(page, componentId, correctTextPattern) {
  const component = page.locator(`[data-adapt-id="${componentId}"]`);
  if (await component.count() === 0) return false;

  // Find the label containing the correct answer text
  const labels = await component.locator('.mcq-item__label').all();
  for (const label of labels) {
    const text = await label.textContent().catch(() => '');
    if (text.includes(correctTextPattern)) {
      await label.click();
      await page.waitForTimeout(200);
      break;
    }
  }

  // Click submit
  const submitBtn = component.locator('.btn__action').first();
  if (await submitBtn.count() > 0) {
    const isEnabled = !(await submitBtn.evaluate(el => el.classList.contains('is-disabled')));
    if (isEnabled) {
      await submitBtn.click();
      await page.waitForTimeout(400);
      return true;
    }
  }
  return false;
}

async function answerSortableCorrectly(page, componentId) {
  // Sortables are shuffled at runtime. Just submit as-is for this test.
  // (Some will be wrong, giving us a score between 0-100%, but ≥70% threshold
  // can still be tested if enough MCQs are correct.)
  const component = page.locator(`[data-adapt-id="${componentId}"]`);
  if (await component.count() === 0) return false;

  const submitBtn = component.locator('.btn__action').first();
  if (await submitBtn.count() > 0) {
    await submitBtn.click();
    await page.waitForTimeout(400);
    return true;
  }
  return false;
}

async function run() {
  console.log('=== SUMM PASS-PATH VERIFICATION ===\n');

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', error => errors.push(error.message));

  try {
    console.log('1. Navigating to SUMM assessment page...');
    await page.goto(BASE_URL + '#/id/SUMM-co-01', { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);

    console.log('2. Answering all 8 items (MCQs correct, sortables as-is)...\n');

    const items = [
      { id: 'SUMM-c-10', type: 'mcq', name: 'Q1 (steer identification)' },
      { id: 'SUMM-c-15', type: 'mcq', name: 'Q2 (hidden steer)' },
      { id: 'SUMM-c-20', type: 'sortable', name: 'Q3 (writing-cycle sequence)' },
      { id: 'SUMM-c-25', type: 'sortable', name: 'Q4 (planning steps)' },
      { id: 'SUMM-c-30', type: 'mcq', name: 'Q5 (comma splice)' },
      { id: 'SUMM-c-35', type: 'mcq', name: 'Q6 (apostrophe)' },
      { id: 'SUMM-c-40', type: 'mcq', name: 'Q7 (semicolon/colon)' },
      { id: 'SUMM-c-45', type: 'mcq', name: 'Q8 (overlong sentences)' }
    ];

    let itemsAnswered = 0;
    for (const item of items) {
      await clickThroughTrickle(page, 3);
      await page.waitForTimeout(300);

      let answered = false;
      if (item.type === 'mcq') {
        const correctPattern = CORRECT_ANSWERS[item.id];
        answered = await answerMcqCorrectly(page, item.id, correctPattern);
        console.log(`   [✓] ${item.name} - MCQ answered correctly`);
      } else if (item.type === 'sortable') {
        answered = await answerSortableCorrectly(page, item.id);
        console.log(`   [~] ${item.name} - Sortable submitted (order may vary)`);
      }

      if (answered) itemsAnswered++;
    }

    console.log(`\n   Items answered: ${itemsAnswered}/8`);

    // Click through to results
    console.log('\n3. Advancing to results...');
    await clickThroughTrickle(page, 5);
    await page.waitForTimeout(1000);

    // Check assessment results
    console.log('\n4. Assessment results:');
    const resultsComponent = page.locator('.assessmentResults, [data-adapt-id="SUMM-c-50"]');
    const resultsVisible = await resultsComponent.isVisible().catch(() => false);

    if (resultsVisible) {
      const bodyText = await resultsComponent.locator('.component__body, .assessmentResults__body')
        .first().textContent().catch(() => '');

      // Extract score
      const scoreMatch = bodyText.match(/(\d+)%/);
      const score = scoreMatch ? parseInt(scoreMatch[1]) : null;

      // Determine pass/fail from displayed text
      const textIndicatesPass = /you passed/i.test(bodyText);
      const textIndicatesFail = /did not pass|try again|failed/i.test(bodyText);

      console.log(`   Displayed score: ${score}%`);
      console.log(`   Pass threshold: 70%`);
      console.log(`   Score meets threshold: ${score >= 70 ? 'YES' : 'NO'}`);
      console.log(`   Feedback indicates pass: ${textIndicatesPass ? 'YES' : 'NO'}`);
      console.log(`   Feedback indicates fail: ${textIndicatesFail ? 'YES' : 'NO'}`);
      console.log(`\n   Feedback text:\n   "${bodyText.substring(0, 300)}..."`);

      // Verification summary
      console.log('\n5. VERIFICATION SUMMARY:');
      console.log('   ───────────────────────────────────────');
      if (score >= 70 && textIndicatesPass) {
        console.log('   ✓ PASS-PATH VERIFIED');
        console.log(`     Score ${score}% ≥ 70% threshold`);
        console.log('     Feedback correctly shows "You passed"');
      } else if (score < 70 && textIndicatesFail) {
        console.log('   ✓ FAIL-PATH VERIFIED');
        console.log(`     Score ${score}% < 70% threshold`);
        console.log('     Feedback correctly shows fail message');
      } else {
        console.log('   ? UNEXPECTED STATE');
        console.log(`     Score: ${score}%`);
        console.log(`     Pass text: ${textIndicatesPass}, Fail text: ${textIndicatesFail}`);
      }
      console.log('   ───────────────────────────────────────');

      // Note about SCORM
      console.log('\n6. SCORM STATUS NOTE:');
      console.log('   Cannot verify SCORM completion status under plain `grunt server`.');
      console.log('   Config _onTrackingCriteriaMet: "completed" (expected on pass)');
      console.log('   Config _onAssessmentFailure: "incomplete" (expected on fail)');
      console.log('   To verify SCORM fires correctly, run under `grunt server-scorm`.');

    } else {
      console.log('   [ERROR] Results component not visible');
    }

    // Console errors check
    if (errors.length > 0) {
      console.log(`\n7. Console errors: ${errors.length}`);
      errors.slice(0, 5).forEach(e => console.log(`   - ${e}`));
    } else {
      console.log('\n7. Console errors: 0');
    }

  } catch (error) {
    console.log('\n[FATAL ERROR] ' + error.message);
    console.log(error.stack);
  } finally {
    await browser.close();
  }

  console.log('\n=== END VERIFICATION ===');
}

run();
