/**
 * Reserved intermediate-tier dev preview server.
 *
 * Locked to port 9002, serving build-intermediate/ (staged via
 * `grunt stage-tier:intermediate`) as a plain page. For the rarer SCORM
 * tracking check, see server-intermediate-scorm.js (port 9012, same
 * staged build). See grunt/tasks/server-introductory.js for why this runs
 * connect directly, and grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-intermediate', 'Runs the reserved intermediate-tier preview server on port 9002 (locked)', ['_log-server:serverIntermediate', 'connect:serverIntermediate']);
};
