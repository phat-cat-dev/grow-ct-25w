#!/usr/bin/env node
/**
 * merge-health.js
 *
 * Runs merge-context.js for every context/tier pair discovered in the
 * filesystem and reports pass/fail status. Designed to gate builds and
 * catch regressions introduced by pack or shell edits.
 *
 * Usage:
 *   node tools/merge-health.js
 *
 * Exit codes:
 *   0 - all mergeable pairs passed
 *   1 - at least one mergeable pair failed
 *
 * NOT BUILT pairs (no shell exists) are reported but do not trip the exit code.
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');
const CONTEXT_PACKS_ROOT = path.join(ROOT, 'content', 'context-packs');
const SRC_COURSE_LINK = path.join(ROOT, 'src', 'course');
const MERGE_SCRIPT = path.join(ROOT, 'merge-context.js');

// --- Symlink save/restore ---

let originalSymlinkTarget = null;

function saveSymlink() {
  try {
    const stats = fs.lstatSync(SRC_COURSE_LINK);
    if (stats.isSymbolicLink()) {
      originalSymlinkTarget = fs.readlinkSync(SRC_COURSE_LINK);
    }
  } catch (err) {
    // Symlink doesn't exist — nothing to restore
    originalSymlinkTarget = null;
  }
}

function restoreSymlink() {
  if (originalSymlinkTarget === null) return;
  try {
    // Remove current link if it exists
    try {
      fs.unlinkSync(SRC_COURSE_LINK);
    } catch (e) {
      // Ignore if already gone
    }
    fs.symlinkSync(originalSymlinkTarget, SRC_COURSE_LINK);
  } catch (err) {
    console.error(`[merge-health] WARNING: Failed to restore symlink: ${err.message}`);
  }
}

// Ensure restore on any exit path
process.on('exit', restoreSymlink);
process.on('SIGINT', () => {
  restoreSymlink();
  process.exit(130);
});
process.on('SIGTERM', () => {
  restoreSymlink();
  process.exit(143);
});
process.on('uncaughtException', (err) => {
  console.error(`[merge-health] Uncaught exception: ${err.message}`);
  restoreSymlink();
  process.exit(1);
});

// --- Enumeration ---

function enumeratePairs() {
  const pairs = [];
  const contexts = fs.readdirSync(CONTEXT_PACKS_ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory() && d.name !== '_template')
    .map(d => d.name);

  for (const context of contexts) {
    const contextDir = path.join(CONTEXT_PACKS_ROOT, context);
    const tiers = fs.readdirSync(contextDir, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    for (const tier of tiers) {
      pairs.push({ context, tier });
    }
  }

  return pairs;
}

function shellExists(tier) {
  // A shell is "built" if <tier>'s en/course.json exists under courses/.
  // Uses the shared resolver (PR-1-11) so this check cannot independently
  // drift from the other tools that share the same assumption; scope
  // (courses/ only) is unchanged from before this fix - merge-context.js's
  // own hardcode (merge-context.js:591, not one of PR-1-11's named tools) is
  // untouched, so widening this check to another root would not make a
  // merge succeed regardless.
  const resolved = resolveCourse(tier, ['courses']);
  return resolved.found && fs.existsSync(path.join(resolved.courseDir, 'en', 'course.json'));
}

// --- Run merge ---

function runMerge(context, tier) {
  const result = spawnSync('node', [MERGE_SCRIPT, `--context=${context}`, `--tier=${tier}`], {
    cwd: ROOT,
    encoding: 'utf8',
    timeout: 60000
  });
  return {
    success: result.status === 0,
    stdout: result.stdout || '',
    stderr: result.stderr || '',
    status: result.status
  };
}

// --- Main ---

function main() {
  saveSymlink();

  const pairs = enumeratePairs();
  const results = [];

  for (const { context, tier } of pairs) {
    if (!shellExists(tier)) {
      results.push({ context, tier, status: 'NOT BUILT', error: null });
      continue;
    }

    const mergeResult = runMerge(context, tier);
    if (mergeResult.success) {
      results.push({ context, tier, status: 'PASS', error: null });
    } else {
      results.push({
        context,
        tier,
        status: 'FAIL',
        error: mergeResult.stderr || mergeResult.stdout || `Exit code ${mergeResult.status}`
      });
    }
  }

  // --- Output table ---
  console.log('\n' + '='.repeat(70));
  console.log('MERGE HEALTH CHECK');
  console.log('='.repeat(70) + '\n');

  // Calculate column widths
  const maxContext = Math.max(...results.map(r => r.context.length), 'CONTEXT'.length);
  const maxTier = Math.max(...results.map(r => r.tier.length), 'TIER'.length);

  const header = `${'CONTEXT'.padEnd(maxContext)}  ${'TIER'.padEnd(maxTier)}  STATUS`;
  console.log(header);
  console.log('-'.repeat(header.length));

  for (const r of results) {
    console.log(`${r.context.padEnd(maxContext)}  ${r.tier.padEnd(maxTier)}  ${r.status}`);
  }

  // --- Summary ---
  const passCount = results.filter(r => r.status === 'PASS').length;
  const failCount = results.filter(r => r.status === 'FAIL').length;
  const notBuiltCount = results.filter(r => r.status === 'NOT BUILT').length;

  console.log('\n' + '-'.repeat(header.length));
  console.log(`${passCount} PASS, ${failCount} FAIL, ${notBuiltCount} NOT BUILT`);

  // --- Failures detail ---
  const failures = results.filter(r => r.status === 'FAIL');
  if (failures.length > 0) {
    console.log('\n' + '='.repeat(70));
    console.log('FAILURE DETAILS');
    console.log('='.repeat(70));
    for (const f of failures) {
      console.log(`\n--- ${f.context} / ${f.tier} ---`);
      console.log(f.error);
    }
  }

  // Exit non-zero if any failures (NOT BUILT does not count)
  process.exit(failCount > 0 ? 1 : 0);
}

main();
