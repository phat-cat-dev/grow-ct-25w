/**
 * Reserved introductory-tier dev preview server.
 *
 * Locked to port 9001, serving build-introductory/ (staged via
 * `grunt stage-tier:introductory`) as a plain page - for reviewing the
 * tier as you develop it, after a rebuild + restage. For the rarer SCORM
 * tracking check, see server-introductory-scorm.js (port 9011, same
 * staged build). Runs connect directly, not through grunt-concurrent, so
 * a port clash surfaces as a real grunt.fatal instead of being swallowed
 * until a spawn callback that never fires under keepalive. See
 * grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-introductory', 'Runs the reserved introductory-tier preview server on port 9001 (locked)', ['_log-server:serverIntroductory', 'connect:serverIntroductory']);
};
