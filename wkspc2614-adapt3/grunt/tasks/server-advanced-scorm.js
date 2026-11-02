/**
 * Reserved advanced-tier SCORM harness server.
 *
 * Locked to port 9013, serving the SAME staged build-advanced/ as
 * server-advanced.js (port 9003), but via scorm_test_harness.html.
 * See server-introductory-scorm.js for why this is separate from the
 * dev preview, and grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-advanced-scorm', 'Runs the reserved advanced-tier SCORM harness server on port 9013 (locked)', ['_log-server:serverAdvancedScorm', 'connect:serverAdvancedScorm']);
};
