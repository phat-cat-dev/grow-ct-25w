#!/usr/bin/env node
/**
 * build-all-packages.js
 *
 * Builds and packages all context/tier pairs discovered in courses/_generated/.
 * Each pair becomes a SCORM-ready zip in scorm-packages/.
 *
 * Usage:
 *   node tools/build-all-packages.js           # Build all pairs
 *   node tools/build-all-packages.js --limit=1 # Build only the first pair (for testing)
 *
 * Exit codes:
 *   0 - all pairs built and verified successfully
 *   1 - at least one pair failed
 *
 * NOTE ON TRACKING IDS (verified R63, 8 Sep 2026):
 *   grunt build's tracking-insert task mutates _latestTrackingId in course.json
 *   and adds _trackingId fields to blocks.json. These writes go to src/course/,
 *   which during packaging points at courses/_generated/<pair>/. Since _generated/
 *   is gitignored and regenerated fresh on every merge-context.js run, no restore
 *   step is needed for these mutations. The only thing requiring restore is the
 *   src/course symlink target itself.
 *
 * NOTE ON scorm-packages/verified/:
 *   This script does NOT touch scorm-packages/verified/. That directory holds
 *   Moodle-proven packages per RC-1c and is managed separately.
 */

const fs = require('fs');
const path = require('path');
const { execSync, spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const GENERATED_ROOT = path.join(ROOT, 'courses', '_generated');
const COURSES_ROOT = path.join(ROOT, 'courses');
const SRC_COURSE_LINK = path.join(ROOT, 'src', 'course');
const SCORM_PACKAGES_ROOT = path.join(ROOT, 'scorm-packages');
const PACKAGE_SCRIPT = path.join(ROOT, 'package-scorm.js');

// --- Symlink save/restore ---

let originalSymlinkTarget = null;

function saveSymlink() {
  try {
    const stats = fs.lstatSync(SRC_COURSE_LINK);
    if (stats.isSymbolicLink()) {
      originalSymlinkTarget = fs.readlinkSync(SRC_COURSE_LINK);
      console.log(`[build-all] Saved original symlink: src/course -> ${originalSymlinkTarget}`);
    }
  } catch (err) {
    originalSymlinkTarget = null;
  }
}

function restoreSymlink() {
  if (originalSymlinkTarget === null) return;
  try {
    try {
      fs.unlinkSync(SRC_COURSE_LINK);
    } catch (e) {
      // Ignore if already gone
    }
    fs.symlinkSync(originalSymlinkTarget, SRC_COURSE_LINK);
    console.log(`[build-all] Restored symlink: src/course -> ${originalSymlinkTarget}`);
  } catch (err) {
    console.error(`[build-all] WARNING: Failed to restore symlink: ${err.message}`);
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
  console.error(`[build-all] Uncaught exception: ${err.message}`);
  console.error(err.stack);
  restoreSymlink();
  process.exit(1);
});

// --- Enumeration ---

function getKnownTiers() {
  // Tiers are directories in courses/ that have en/course.json (i.e., built shells)
  // Exclude _generated and any other non-tier directories
  return fs.readdirSync(COURSES_ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory() && d.name !== '_generated')
    .filter(d => fs.existsSync(path.join(COURSES_ROOT, d.name, 'en', 'course.json')))
    .map(d => d.name);
}

function enumeratePairs() {
  const tiers = getKnownTiers();
  const pairs = [];

  // Read all directories in _generated/
  const generatedDirs = fs.readdirSync(GENERATED_ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);

  for (const dir of generatedDirs) {
    // Find which tier this directory starts with
    // Tiers are sorted by length descending to match longest first
    const sortedTiers = tiers.slice().sort((a, b) => b.length - a.length);
    let matchedTier = null;
    let context = null;

    for (const tier of sortedTiers) {
      if (dir.startsWith(tier + '-')) {
        matchedTier = tier;
        context = dir.slice(tier.length + 1); // +1 for the hyphen
        break;
      }
    }

    if (matchedTier && context) {
      pairs.push({ tier: matchedTier, context, dir });
    } else {
      console.warn(`[build-all] WARNING: Could not parse directory: ${dir}`);
    }
  }

  // Sort for consistent ordering
  pairs.sort((a, b) => {
    const tierCmp = a.tier.localeCompare(b.tier);
    if (tierCmp !== 0) return tierCmp;
    return a.context.localeCompare(b.context);
  });

  return pairs;
}

// --- Build and Package ---

function runPackageScorm(context, tier) {
  const result = spawnSync('node', [PACKAGE_SCRIPT, `--context=${context}`, `--tier=${tier}`], {
    cwd: ROOT,
    encoding: 'utf8',
    timeout: 300000, // 5 minutes per package
    stdio: ['pipe', 'pipe', 'pipe']
  });
  return {
    success: result.status === 0,
    stdout: result.stdout || '',
    stderr: result.stderr || '',
    status: result.status
  };
}

function getGitCommitHash() {
  return execSync('git rev-parse --short HEAD', { cwd: ROOT, encoding: 'utf8' }).trim();
}

// --- Dirty-tree guard ---
// Refuse to build when the working tree is dirty. A package's name embeds
// the HEAD commit hash (see getGitCommitHash), but grunt build packages
// whatever is actually in src/course/ at build time. If the tree is dirty,
// that hash no longer identifies the content inside the zip, and a package
// built from uncommitted changes could still reach Moodle. Refusing forces
// a commit or stash first, rather than silently mislabelling the package.
function getDirtyFiles() {
  const output = execSync('git status --porcelain', { cwd: ROOT, encoding: 'utf8' });
  return output.split('\n').filter(line => line.trim() !== '');
}

function findPackageZip(tier, context, commitHash) {
  // Package naming: {tier}_{context}_{YYYYMMDD}_{HHMMSS}_{commitHash}.zip
  const prefix = `${tier}_${context}_`;
  const suffix = `_${commitHash}.zip`;

  const files = fs.readdirSync(SCORM_PACKAGES_ROOT)
    .filter(f => f.startsWith(prefix) && f.endsWith(suffix))
    .sort()
    .reverse(); // Most recent first

  return files.length > 0 ? path.join(SCORM_PACKAGES_ROOT, files[0]) : null;
}

// --- Verification ---

function verifyPackage(zipPath) {
  const errors = [];

  // Check file exists and get size
  if (!fs.existsSync(zipPath)) {
    return { valid: false, size: 0, errors: ['Zip file does not exist'] };
  }

  const stats = fs.statSync(zipPath);
  const sizeKB = Math.round(stats.size / 1024);

  // Check non-trivial size (at least 100KB)
  if (stats.size < 100 * 1024) {
    errors.push(`Zip is suspiciously small: ${sizeKB}KB`);
  }

  // Check imsmanifest.xml is at top level using zipinfo
  try {
    const zipContents = execSync(`unzip -l "${zipPath}"`, { encoding: 'utf8' });

    // Check for imsmanifest.xml at root (no directory prefix)
    if (!zipContents.includes('imsmanifest.xml')) {
      errors.push('imsmanifest.xml not found in zip');
    } else {
      // Verify it's at root level (line should show just "imsmanifest.xml" not "some/path/imsmanifest.xml")
      const lines = zipContents.split('\n');
      const manifestLine = lines.find(l => l.includes('imsmanifest.xml'));
      if (manifestLine && !manifestLine.trim().endsWith('imsmanifest.xml')) {
        errors.push('imsmanifest.xml is not at zip root level');
      }
    }

    // Check for course.json (in adapt/css/assets/course/{lang}/)
    if (!zipContents.includes('course.json')) {
      errors.push('course.json not found in zip');
    }
  } catch (err) {
    errors.push(`Failed to inspect zip: ${err.message}`);
  }

  return {
    valid: errors.length === 0,
    size: sizeKB,
    errors
  };
}

// --- Main ---

function main() {
  // Parse arguments
  let limit = null;
  for (const arg of process.argv.slice(2)) {
    if (arg.startsWith('--limit=')) {
      limit = parseInt(arg.split('=')[1], 10);
    }
  }

  const dirtyFiles = getDirtyFiles();
  if (dirtyFiles.length > 0) {
    console.error('[build-all] Refusing to build: working tree is dirty.');
    console.error('[build-all] Package names embed the HEAD commit hash; a dirty tree means that hash would not identify the actual packaged content, and the resulting package could still reach Moodle.');
    console.error('[build-all] Dirty files:');
    dirtyFiles.forEach(f => console.error(`  ${f}`));
    console.error('[build-all] Commit or stash these changes, then re-run.');
    process.exit(1);
  }

  saveSymlink();

  const allPairs = enumeratePairs();

  // Fail loudly, not silently: with zero pairs, the loop below runs zero
  // times and every downstream count (PASS/FAIL/attempted) is honestly
  // zero too - the previous behaviour exited 0 on that, a green build
  // that packaged nothing. Mirrors verify-all-courses.js's zero-courses
  // guard.
  if (allPairs.length === 0) {
    console.error(`[build-all] No context/tier pairs found under ${path.relative(ROOT, GENERATED_ROOT)}`);
    process.exit(1);
  }

  const pairs = limit ? allPairs.slice(0, limit) : allPairs;

  console.log(`\n${'='.repeat(80)}`);
  console.log('BUILD ALL PACKAGES');
  console.log(`${'='.repeat(80)}`);
  console.log(`Found ${allPairs.length} pairs in courses/_generated/`);
  if (limit) {
    console.log(`Limited to first ${limit} pair(s) for testing`);
  }
  console.log();

  const commitHash = getGitCommitHash();
  console.log(`Commit: ${commitHash}\n`);

  const results = [];

  for (let i = 0; i < pairs.length; i++) {
    const { tier, context, dir } = pairs[i];
    console.log(`[${i + 1}/${pairs.length}] Building ${tier} / ${context}...`);

    const buildResult = runPackageScorm(context, tier);

    if (!buildResult.success) {
      results.push({
        tier,
        context,
        status: 'BUILD FAIL',
        size: 0,
        errors: [buildResult.stderr || buildResult.stdout || `Exit code ${buildResult.status}`]
      });
      console.log(`  -> BUILD FAIL\n`);
      continue;
    }

    // Find the generated zip
    const zipPath = findPackageZip(tier, context, commitHash);
    if (!zipPath) {
      results.push({
        tier,
        context,
        status: 'ZIP NOT FOUND',
        size: 0,
        errors: ['Could not find generated zip file']
      });
      console.log(`  -> ZIP NOT FOUND\n`);
      continue;
    }

    // Verify the package
    const verification = verifyPackage(zipPath);
    if (verification.valid) {
      results.push({
        tier,
        context,
        status: 'PASS',
        size: verification.size,
        errors: [],
        zipPath
      });
      console.log(`  -> PASS (${verification.size}KB)\n`);
    } else {
      results.push({
        tier,
        context,
        status: 'VERIFY FAIL',
        size: verification.size,
        errors: verification.errors,
        zipPath
      });
      console.log(`  -> VERIFY FAIL: ${verification.errors.join('; ')}\n`);
    }
  }

  // --- Output table ---
  console.log('\n' + '='.repeat(80));
  console.log('RESULTS');
  console.log('='.repeat(80) + '\n');

  const maxTier = Math.max(...results.map(r => r.tier.length), 'TIER'.length);
  const maxContext = Math.max(...results.map(r => r.context.length), 'CONTEXT'.length);

  const header = `${'TIER'.padEnd(maxTier)}  ${'CONTEXT'.padEnd(maxContext)}  ${'SIZE'.padStart(7)}  STATUS`;
  console.log(header);
  console.log('-'.repeat(header.length));

  for (const r of results) {
    const sizeStr = r.size > 0 ? `${r.size}KB` : '-';
    console.log(`${r.tier.padEnd(maxTier)}  ${r.context.padEnd(maxContext)}  ${sizeStr.padStart(7)}  ${r.status}`);
  }

  // --- Summary ---
  const passCount = results.filter(r => r.status === 'PASS').length;
  const failCount = results.filter(r => r.status !== 'PASS').length;

  console.log('\n' + '-'.repeat(header.length));
  console.log(`${passCount} PASS, ${failCount} FAIL (of ${results.length} attempted)`);

  // --- Failure details ---
  const failures = results.filter(r => r.status !== 'PASS');
  if (failures.length > 0) {
    console.log('\n' + '='.repeat(80));
    console.log('FAILURE DETAILS');
    console.log('='.repeat(80));
    for (const f of failures) {
      console.log(`\n--- ${f.tier} / ${f.context} (${f.status}) ---`);
      for (const err of f.errors) {
        console.log(err);
      }
    }
  }

  // Repeated here, not just at the top: CLAUDE.md's own verification
  // discipline reads only "the tail plus the exit line" when output is
  // long (CLAUDE.md:79). A discovery count printed once before all the
  // per-pair build noise does not survive that reading. Restating it
  // beside the exit-determining line means a run that covered fewer
  // pairs than expected is visible in the tail, not just inferable by
  // scrolling back to the top.
  console.log(`\nPairs discovered: ${allPairs.length} (${allPairs.map(p => p.dir).join(', ')})`);

  // Exit non-zero if any failures
  process.exit(failCount > 0 ? 1 : 0);
}

main();
