/**
 * course-script — emit the readable export bundle (tools/course-export.js) for
 * whatever src/course currently points to. Runs at the end of `grunt build`.
 *
 * Failure-safe by design: any problem is a warning, never a build failure. The
 * bundle is a convenience artifact; a missing manifest, short slug or anything
 * else must not stop a production build.
 */
module.exports = function(grunt) {
  grunt.registerTask('course-script', 'Export a readable bundle of the built course', function() {
    try {
      const cp = require('child_process');
      const fs = require('fs');
      const src = 'src/course';
      if (!fs.existsSync(src)) { grunt.log.warn('course-script: src/course not found; skipping'); return; }
      const real = fs.realpathSync(src);
      const r = cp.spawnSync('node', ['tools/course-export.js', '--course', real, '--out', 'exports'], { encoding: 'utf8' });
      if (r.stdout) grunt.log.writeln(r.stdout.trim());
      if (r.status !== 0) grunt.log.warn('course-script: export skipped (' + ((r.stderr || '').trim() || 'non-zero exit') + ')');
      else grunt.log.ok('course-script: bundle written to exports/');
    } catch (e) {
      grunt.log.warn('course-script: ' + e.message);
    }
  });
};
