#!/usr/bin/env node
/**
 * apply-vendor-patches.js
 *
 * Applies all .patch files in patches/ to their target files.
 * Safe to run multiple times: detects already-applied patches and skips them.
 *
 * Part of the Adapt install chain: package.json's `adapt-install` script runs
 * it after `adapt install`, so it must stay at scripts/apply-vendor-patches.js.
 * Paths resolve from __dirname, so the pwd you invoke it from does not matter.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PATCHES_DIR = path.join(__dirname, '..', 'patches');
const PROJECT_ROOT = path.join(__dirname, '..');

function getPatchFiles() {
  if (!fs.existsSync(PATCHES_DIR)) {
    return [];
  }
  return fs.readdirSync(PATCHES_DIR)
    .filter(f => f.endsWith('.patch'))
    .map(f => path.join(PATCHES_DIR, f));
}

function extractTargetPath(patchContent) {
  // Look for +++ b/path/to/file line in unified diff
  const match = patchContent.match(/^\+\+\+ [ab]\/(.+)$/m);
  if (match) {
    return match[1];
  }
  return null;
}

function isPatchApplied(patchFile) {
  // Use patch --dry-run --reverse to check if already applied
  try {
    execSync(`patch -p1 --dry-run --reverse < "${patchFile}"`, {
      cwd: PROJECT_ROOT,
      stdio: 'pipe'
    });
    return true; // Reverse succeeded = patch is already applied
  } catch (e) {
    return false; // Reverse failed = patch not yet applied
  }
}

function canApplyPatch(patchFile) {
  // Use patch --dry-run to check if patch can be applied
  try {
    execSync(`patch -p1 --dry-run < "${patchFile}"`, {
      cwd: PROJECT_ROOT,
      stdio: 'pipe'
    });
    return true;
  } catch (e) {
    return false;
  }
}

function applyPatch(patchFile) {
  execSync(`patch -p1 < "${patchFile}"`, {
    cwd: PROJECT_ROOT,
    stdio: 'pipe'
  });
}

function main() {
  console.log('=== Applying vendor patches ===\n');

  const patches = getPatchFiles();

  if (patches.length === 0) {
    console.log('No patches found in patches/');
    process.exit(0);
  }

  const results = {
    applied: [],
    skipped: [],
    failed: []
  };

  for (const patchFile of patches) {
    const patchName = path.basename(patchFile);
    const patchContent = fs.readFileSync(patchFile, 'utf8');
    const targetPath = extractTargetPath(patchContent);

    console.log(`Processing: ${patchName}`);
    if (targetPath) {
      console.log(`  Target: ${targetPath}`);
    }

    // Check if already applied
    if (isPatchApplied(patchFile)) {
      console.log('  Status: Already applied (skipped)\n');
      results.skipped.push(patchName);
      continue;
    }

    // Check if can be applied
    if (!canApplyPatch(patchFile)) {
      console.log('  Status: FAILED (patch does not apply cleanly)\n');
      results.failed.push(patchName);
      continue;
    }

    // Apply the patch
    try {
      applyPatch(patchFile);
      console.log('  Status: Applied successfully\n');
      results.applied.push(patchName);
    } catch (e) {
      console.log(`  Status: FAILED (${e.message})\n`);
      results.failed.push(patchName);
    }
  }

  // Summary
  console.log('=== Summary ===');
  console.log(`Applied:  ${results.applied.length}`);
  if (results.applied.length > 0) {
    results.applied.forEach(p => console.log(`  - ${p}`));
  }
  console.log(`Skipped:  ${results.skipped.length} (already applied)`);
  if (results.skipped.length > 0) {
    results.skipped.forEach(p => console.log(`  - ${p}`));
  }
  console.log(`Failed:   ${results.failed.length}`);
  if (results.failed.length > 0) {
    results.failed.forEach(p => console.log(`  - ${p}`));
  }

  if (results.failed.length > 0) {
    process.exit(1);
  }
}

main();
