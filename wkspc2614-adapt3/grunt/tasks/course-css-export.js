/**
 * course-css-export — copy the built course's compiled CSS (build/adapt.css)
 * into exports/ (tools/course-css-export.js). Runs at the end of
 * `grunt build`, replacing the former course-script-md auto-export.
 *
 * Failure-safe by design: any problem is a warning, never a build failure.
 * The export is a convenience artifact; a missing manifest, short slug or
 * anything else must not stop a production build.
 */
module.exports = function(grunt) {
  grunt.registerTask('course-css-export', 'Export the built course\'s compiled CSS to exports/', function() {
    try {
      const cp = require('child_process');
      const fs = require('fs');
      const src = 'src/course';
      if (!fs.existsSync(src)) { grunt.log.warn('course-css-export: src/course not found; skipping'); return; }
      const real = fs.realpathSync(src);
      const outputdir = grunt.config('outputdir') || 'build/';
      const r = cp.spawnSync('node', ['tools/course-css-export.js', '--course', real, '--out', 'exports', '--build', outputdir], { encoding: 'utf8' });
      if (r.stdout) grunt.log.writeln(r.stdout.trim());
      if (r.status !== 0) grunt.log.warn('course-css-export: export skipped (' + ((r.stderr || '').trim() || 'non-zero exit') + ')');
      else grunt.log.ok('course-css-export: CSS written to exports/');
    } catch (e) {
      grunt.log.warn('course-css-export: ' + e.message);
    }
  });
};
