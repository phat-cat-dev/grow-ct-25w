/**
 * A80 (Option 4) build gate. Runs tools/verify-all-courses.js, which runs
 * the four canonical validators against every course under courses/ and
 * gates on three of them (voice-lint, conformance-lint,
 * validate-design-schemas). See tools/verify-all-courses.js's own header
 * for the full contract.
 *
 * docs/project/audit-2026-09/audit-actions-arising.md:93 (A80, Option 4).
 *
 * PR-1-15, 17 Sep 2026: the wrapped script now exits 2 for zero discovery
 * (nothing found to check), distinct from exit 1 (found something and a
 * gating tool failed). Both still stop the build - zero discovery is not
 * a pass - but this task must branch on the code, not just on
 * result.status !== 0, or the distinction the script now makes is
 * erased again at this, its only caller that reads the code at all.
 */
module.exports = function(grunt) {
  const { spawnSync } = require('child_process');
  const path = require('path');

  grunt.registerTask('verify-all-courses', 'Runs the four canonical validators against every course; gates the build on three of them (A80)', function() {
    const result = spawnSync('node', [path.join('tools', 'verify-all-courses.js')], {
      cwd: process.cwd(),
      stdio: 'inherit'
    });

    if (result.status === 2) {
      grunt.fail.fatal('verify-all-courses found zero courses to check - see output above. Build stopped: zero discovery is not a pass (PR-1-15).');
    } else if (result.status !== 0) {
      grunt.fail.fatal('verify-all-courses failed - see output above. Build stopped per A80 (Option 4): voice-lint, conformance-lint and validate-design-schemas gate the build.');
    }
  });
};
