/**
 * Prompt 139 Unit 5 (task 9). Runs tools/check-build-target.js, which
 * refuses if src/course does not exist, or is a symlink resolving
 * outside courses/. See that script's own header for the full contract.
 *
 * WIRED into the 'build' and 'dev' task chains (grunt/tasks/build.js,
 * grunt/tasks/dev.js) as of Prompt 140 CSTR-1 (21 Sep 2026). Prompt 139
 * left this unwired because src/course then resolved to
 * archive/courses-2026-09/academic-writing-introductory, and wiring it
 * in would have halted every build immediately as an unreviewed side
 * effect. CSTR-1 removed that symlink (so src/course is now absent) and
 * asked for this task to be wired in at the same time, so a build now
 * refuses cleanly here - naming /new-course as the fix - rather than
 * failing later, deeper in the chain, for a reason that looks unrelated.
 */
module.exports = function(grunt) {
  const { spawnSync } = require('child_process');
  const path = require('path');

  grunt.registerTask('check-build-target', 'Refuses if src/course is absent, or is a symlink resolving outside courses/ (Prompt 139 task 9, Prompt 140 CSTR-1)', function() {
    const result = spawnSync('node', [path.join('tools', 'check-build-target.js')], {
      cwd: process.cwd(),
      stdio: 'inherit'
    });

    if (result.status !== 0) {
      grunt.fail.fatal('check-build-target failed - see output above.');
    }
  });
};
