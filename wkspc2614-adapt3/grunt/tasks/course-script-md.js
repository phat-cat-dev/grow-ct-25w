/**
 * course-script-md — emit just the .script.md screenplay (tools/course-script-md.js)
 * for whatever src/course currently points to. Runs at the end of `grunt build`.
 *
 * This is the lightweight default. It overwrites a single file in exports/ each
 * run, so routine builds don't create a new timestamped folder. The full
 * multi-format bundle (html/templates/yaml/json/packs) is on-request only — run
 * `npx grunt course-script` or `npm run course-export` when you want that.
 *
 * Failure-safe by design: any problem is a warning, never a build failure. The
 * script is a convenience artifact; a missing manifest, short slug or anything
 * else must not stop a production build.
 */
module.exports = function(grunt) {
  grunt.registerTask('course-script-md', 'Export just the .script.md screenplay of the built course', function() {
    try {
      const cp = require('child_process');
      const fs = require('fs');
      const src = 'src/course';
      if (!fs.existsSync(src)) { grunt.log.warn('course-script-md: src/course not found; skipping'); return; }
      const real = fs.realpathSync(src);
      const r = cp.spawnSync('node', ['tools/course-script-md.js', '--course', real, '--out', 'exports'], { encoding: 'utf8' });
      if (r.stdout) grunt.log.writeln(r.stdout.trim());
      if (r.status !== 0) grunt.log.warn('course-script-md: export skipped (' + ((r.stderr || '').trim() || 'non-zero exit') + ')');
      else grunt.log.ok('course-script-md: screenplay written to exports/');
    } catch (e) {
      grunt.log.warn('course-script-md: ' + e.message);
    }
  });
};
