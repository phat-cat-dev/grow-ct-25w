/**
 * Reserved introductory-tier preview server.
 *
 * Locked to port 9001, serving build-introductory/ (staged via
 * `grunt stage-tier:introductory`). Runs connect directly, not through
 * grunt-concurrent, so a port clash surfaces as a real grunt.fatal instead
 * of being swallowed until a spawn callback that never fires under
 * keepalive. See grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-introductory', 'Runs the reserved introductory-tier preview server on port 9001 (locked)', ['_log-server:serverIntroductory', 'connect:serverIntroductory']);
};
