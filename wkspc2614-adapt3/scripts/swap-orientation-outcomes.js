#!/usr/bin/env node
/**
 * swap-orientation-outcomes.js
 *
 * RUN HISTORY:
 *   - 7 Sep 2026: LS-2 retrofit (R25). All 15 lessons across 3 courses.
 *     Retained for provenance; idempotent, safe to re-run for verification.
 *
 * Swaps array positions of "Learning outcomes" and "Orientation" blocks
 * in lesson articles so that Orientation renders first (LS-2 retrofit).
 *
 * DOES NOT change any _id, _parentId, or _trackingId values.
 * Only swaps array positions — Adapt renders by array order, not by _id.
 *
 * Scope:
 *   academic-writing-introductory: L02–L07 (6 lessons)
 *   academic-writing-intermediate: L02–L06 (5 lessons)
 *   academic-writing-advanced:     L02–L05 (4 lessons)
 *
 * W-OPEN is explicitly excluded (outcomes-first by design).
 *
 * Usage, from the repo root:
 *   node scripts/swap-orientation-outcomes.js
 *
 * Course paths resolve from __dirname, so the pwd does not matter. It writes to
 * courses/<slug>/en/blocks.json, so commit before running it.
 */

const fs = require('fs');
const path = require('path');

const COURSES = [
  {
    name: 'academic-writing-introductory',
    lessons: ['L02', 'L03', 'L04', 'L05', 'L06', 'L07']
  },
  {
    name: 'academic-writing-intermediate',
    lessons: ['L02', 'L03', 'L04', 'L05', 'L06']
  },
  {
    name: 'academic-writing-advanced',
    lessons: ['L02', 'L03', 'L04', 'L05']
  }
];

function swapBlocksInCourse(coursePath, lessons) {
  const blocksPath = path.join(coursePath, 'en', 'blocks.json');

  if (!fs.existsSync(blocksPath)) {
    console.log(`  SKIP: ${blocksPath} not found`);
    return { swapped: 0, skipped: 0 };
  }

  const blocks = JSON.parse(fs.readFileSync(blocksPath, 'utf8'));
  let swappedCount = 0;
  let skippedCount = 0;

  for (const lessonPrefix of lessons) {
    // Find the article ID for this lesson
    // Handles both conventions:
    //   - Introductory: L02-a-01
    //   - Intermediate/Advanced: academic-writing-intermediate-L02-a-01
    const articlePattern = new RegExp(`(^|-)${lessonPrefix}-a-`);

    // Find all blocks belonging to this lesson's article
    const lessonBlocks = blocks
      .map((block, index) => ({ block, index }))
      .filter(({ block }) => articlePattern.test(block._parentId));

    // Find the specific blocks we need to swap
    const outcomesEntry = lessonBlocks.find(({ block }) => block.title === 'Learning outcomes');
    const orientationEntry = lessonBlocks.find(({ block }) => block.title === 'Orientation');

    if (!outcomesEntry || !orientationEntry) {
      console.log(`  SKIP ${lessonPrefix}: missing Learning outcomes or Orientation block`);
      skippedCount++;
      continue;
    }

    const outcomesIdx = outcomesEntry.index;
    const orientationIdx = orientationEntry.index;

    // Check current order: if Orientation is already before Learning outcomes, skip
    if (orientationIdx < outcomesIdx) {
      console.log(`  SKIP ${lessonPrefix}: already orientation-first (indices ${orientationIdx}, ${outcomesIdx})`);
      skippedCount++;
      continue;
    }

    // Swap array positions
    const temp = blocks[outcomesIdx];
    blocks[outcomesIdx] = blocks[orientationIdx];
    blocks[orientationIdx] = temp;

    console.log(`  SWAP ${lessonPrefix}: indices ${outcomesIdx} <-> ${orientationIdx}`);
    swappedCount++;
  }

  // Write back with same formatting (2-space indent)
  fs.writeFileSync(blocksPath, JSON.stringify(blocks, null, 2) + '\n', 'utf8');

  return { swapped: swappedCount, skipped: skippedCount };
}

function main() {
  console.log('LS-2 Block Order Retrofit: Swap Orientation above Learning Outcomes\n');

  let totalSwapped = 0;
  let totalSkipped = 0;

  for (const course of COURSES) {
    const coursePath = path.join(__dirname, '..', 'courses', course.name);
    console.log(`Processing ${course.name}:`);

    const { swapped, skipped } = swapBlocksInCourse(coursePath, course.lessons);
    totalSwapped += swapped;
    totalSkipped += skipped;

    console.log(`  Result: ${swapped} swapped, ${skipped} skipped\n`);
  }

  console.log(`\nTotal: ${totalSwapped} lessons swapped, ${totalSkipped} skipped`);
  console.log('Done. Run verification commands to confirm.');
}

main();
