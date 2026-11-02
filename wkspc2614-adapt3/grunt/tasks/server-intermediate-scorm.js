/**
 * Reserved intermediate-tier SCORM harness server.
 *
 * Locked to port 9012, serving the SAME staged build-intermediate/ as
 * server-intermediate.js (port 9002), but via scorm_test_harness.html.
 * See server-introductory-scorm.js for why this is separate from the
 * dev preview, and grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-intermediate-scorm', 'Runs the reserved intermediate-tier SCORM harness server on port 9012 (locked)', ['_log-server:serverIntermediateScorm', 'connect:serverIntermediateScorm']);
};
