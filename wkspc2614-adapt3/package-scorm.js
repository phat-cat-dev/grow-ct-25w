/**
 * package-scorm.js
 *
 * Packages a context's generated course as a SCORM-ready zip, per
 * courses/README.md's packaging instructions (imsmanifest.xml at the
 * zip's top level, not nested).
 *
 * Usage:
 *   node package-scorm.js --context=criminology --tier=academic-writing-introductory
 *
 * Runs merge-context.js first (guarantees fresh output rather than
 * trusting stale courses/_generated/ content), swaps src/course,
 * builds, zips, restores the symlink, and cleans up build/.
 */

const fs = require('fs-extra');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = __dirname;
const COURSE_SYMLINK = path.join(ROOT, 'src', 'course');
const GENERATED_ROOT = path.join(ROOT, 'courses', '_generated');
const OUTPUT_ROOT = path.join(ROOT, 'scorm-packages');
const BUILD_DIR = path.join(ROOT, 'build');

function getGitCommitHash() {
  return execSync('git rev-parse --short HEAD', { cwd: ROOT, encoding: 'utf8' }).trim();
}

function getDateStamp() {
  const d = new Date();
  // YYYYMMDD format (no separators) for chronological sorting in directory listings
  return `${d.getFullYear()}${String(d.getMonth() + 1).padStart(2, '0')}${String(d.getDate()).padStart(2, '0')}`;
}

function getTimeStamp() {
  const d = new Date();
  return `${String(d.getHours()).padStart(2, '0')}${String(d.getMinutes()).padStart(2, '0')}${String(d.getSeconds()).padStart(2, '0')}`;
}

const acceptedArgs = ['context', 'tier'];
const argumentValues = { context: null, tier: 'academic-writing-introductory' };

function parseArgs() {
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (!acceptedArgs.includes(parts[0])) {
      console.error(`Unrecognised argument: --${parts[0]}. Accepted: ${acceptedArgs.join(', ')}`);
      process.exit(1);
    }
    argumentValues[parts[0]] = parts[1];
  });
  if (!argumentValues.context) {
    console.error('ERROR: --context is required. Package naming requires a context value.');
    console.error('Usage: node package-scorm.js --context=<slug> [--tier=<slug>]');
    console.error('  Use --context=baseline for the un-overlaid base course.');
    process.exit(1);
  }
}

function run(cmd) {
  console.log(`> ${cmd}`);
  execSync(cmd, { cwd: ROOT, stdio: 'inherit' });
}

async function main() {
  parseArgs();
  const { context, tier } = argumentValues;
  // Directory uses hyphen-join (tier-context) — intentionally separate from the
  // underscore-joined package naming. This matches merge-context.js output paths.
  const courseDir = path.join(GENERATED_ROOT, `${tier}-${context}`);
  const commitHash = getGitCommitHash();
  const dateStamp = getDateStamp();
  const timeStamp = getTimeStamp();
  // Naming convention (30 July 2026): {tier}_{context}_{YYYYMMDD}_{HHMMSS}_{commitHash}.zip
  // Underscore separators allow machine-parsing (tier names contain hyphens)
  // Date-then-time adjacency means filenames sort chronologically in directory listings
  const zipName = `${tier}_${context}_${dateStamp}_${timeStamp}_${commitHash}.zip`;
  const zipPath = path.join(OUTPUT_ROOT, zipName);

  const originalSymlinkTarget = await fs.readlink(COURSE_SYMLINK).catch(() => null);

  try {
    console.log(`\n=== Packaging ${context} (${tier}) ===`);
    console.log(`    Date: ${dateStamp} | Time: ${timeStamp} | Commit: ${commitHash}\n`);

    console.log('Step 1: merge-context.js');
    run(`node merge-context.js --context=${context} --tier=${tier}`);

    console.log('\nStep 2: swap src/course symlink');
    await fs.remove(COURSE_SYMLINK);
    await fs.symlink(path.relative(path.join(ROOT, 'src'), courseDir), COURSE_SYMLINK);

    console.log('\nStep 3: grunt build');
    run('grunt build');

    console.log('\nStep 4: zip build/ contents (imsmanifest.xml at top level)');
    await fs.ensureDir(OUTPUT_ROOT);
    await fs.remove(zipPath).catch(() => {});
    run(`cd ${BUILD_DIR} && zip -rq ${zipPath} .`);

    const stats = await fs.stat(zipPath);
    console.log(`\nDone. ${zipName} (${(stats.size / 1024).toFixed(0)} KB)`);
    console.log(`Built from commit: ${commitHash}`);

  } finally {
    console.log('\nStep 5: restore original src/course symlink');
    await fs.remove(COURSE_SYMLINK).catch(() => {});
    if (originalSymlinkTarget) {
      await fs.symlink(originalSymlinkTarget, COURSE_SYMLINK);
      console.log(`Restored: src/course -> ${originalSymlinkTarget}`);
    }
  }
}

main().catch(err => {
  console.error('package-scorm.js failed:', err);
  process.exit(1);
});
