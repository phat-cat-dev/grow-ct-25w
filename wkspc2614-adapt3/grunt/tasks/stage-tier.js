/**
 * stage-tier:<tier> - copies a finished build/ into build-<tier>/ for one
 * of the three reserved tier-preview servers (see grunt/tier-servers.js and
 * grunt/tasks/server-introductory.js etc).
 *
 * WHY NOT grunt build --outputdir=build-<tier>/: grunt/config/copy.js's
 * nonServerTasks (courseAssets, courseJson) are dropped entirely whenever
 * --outputdir is set, and grunt/helpers.js's generateConfigData reads
 * config.json from the output dir in that mode, silently losing
 * build.excludes through a bare try/catch. A --outputdir build produces a
 * structurally valid but contentless course. Staging a normal build/ is
 * the only correct way to populate a tier directory.
 *
 * Usage:
 *   npx grunt build                      # into build/, as normal
 *   npx grunt stage-tier:introductory    # copies build/ -> build-introductory/
 *   npx grunt stage-tier:advanced --force  # skip the staleness check
 */
module.exports = function(grunt) {
  const fs = require('fs-extra');
  const path = require('path');
  const tierServers = require('../tier-servers');

  const ROOT = path.resolve(__dirname, '..', '..');
  const BUILD_DIR = path.join(ROOT, 'build');
  const SRC_COURSE = path.join(ROOT, 'src', 'course');

  function newestMtimeUnder(dir) {
    let newest = 0;
    (function walk(current) {
      let entries;
      try {
        entries = fs.readdirSync(current, { withFileTypes: true });
      } catch (err) {
        return;
      }
      for (const entry of entries) {
        const full = path.join(current, entry.name);
        if (entry.isDirectory()) {
          walk(full);
          continue;
        }
        const mtime = fs.statSync(full).mtimeMs;
        if (mtime > newest) newest = mtime;
      }
    })(dir);
    return newest;
  }

  grunt.registerTask('stage-tier', 'Copies build/ into build-<tier>/ for a reserved tier-preview server [stage-tier:introductory|intermediate|advanced]', function(tier) {
    const tierNames = Object.keys(tierServers);

    if (!tier || !tierServers[tier]) {
      grunt.fatal(`stage-tier: unknown tier '${tier || ''}'. Valid tiers: ${tierNames.join(', ')}`);
      return;
    }

    const manifestPath = path.join(BUILD_DIR, 'imsmanifest.xml');
    if (!fs.existsSync(manifestPath)) {
      grunt.fatal(`stage-tier: ${manifestPath} does not exist. Run 'npx grunt build' first.`);
      return;
    }

    // build/ is gitignored and can hold a stale manifest from an earlier
    // run (see docs/RUNBOOK.md); mere existence of imsmanifest.xml is not
    // proof the build matches the course currently linked at src/course.
    const force = Boolean(grunt.option('force'));
    if (!force && fs.existsSync(SRC_COURSE)) {
      const sourceRoot = fs.realpathSync(SRC_COURSE);
      const buildMtime = fs.statSync(manifestPath).mtimeMs;
      const sourceMtime = newestMtimeUnder(sourceRoot);
      if (sourceMtime > buildMtime) {
        grunt.fatal(`stage-tier: build/imsmanifest.xml is older than the course linked at src/course (${sourceRoot}). Run 'npx grunt build' again, or pass --force to stage anyway.`);
        return;
      }
    }

    const { dir } = tierServers[tier];
    const destDir = path.join(ROOT, dir);

    fs.removeSync(destDir);
    fs.copySync(BUILD_DIR, destDir, {
      filter: (src) => {
        const rel = path.relative(BUILD_DIR, src);
        return rel !== '.cache' && rel !== '.temp' &&
          !rel.startsWith('.cache' + path.sep) && !rel.startsWith('.temp' + path.sep);
      }
    });

    const manifest = fs.readFileSync(path.join(destDir, 'imsmanifest.xml'), 'utf8');
    const titleMatch = manifest.match(/<title>(?:<!\[CDATA\[)?([^<]*?)(?:\]\]>)?<\/title>/);
    const title = titleMatch && titleMatch[1].trim();

    const { port, hostname } = tierServers[tier];
    grunt.log.ok(`stage-tier: staged '${title || '(title unknown)'}' into ${dir}`);
    grunt.log.ok(`Serve it with: npx grunt server-${tier}  ->  http://${hostname}:${port}/scorm_test_harness.html`);
  });
};
