/**
 * Reserved introductory-tier SCORM harness server.
 *
 * Locked to port 9011, serving the SAME staged build-introductory/ as
 * server-introductory.js (port 9001), but via scorm_test_harness.html -
 * for the rare occasions SCORM tracking behaviour needs checking before a
 * Moodle upload, not for day-to-day review. Runs connect directly; see
 * server-introductory.js for why, and grunt/tier-servers.js for the full
 * tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-introductory-scorm', 'Runs the reserved introductory-tier SCORM harness server on port 9011 (locked)', ['_log-server:serverIntroductoryScorm', 'connect:serverIntroductoryScorm']);
};
