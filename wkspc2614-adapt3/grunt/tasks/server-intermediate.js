/**
 * Reserved intermediate-tier preview server.
 *
 * Locked to port 9002, serving build-intermediate/ (staged via
 * `grunt stage-tier:intermediate`). See grunt/tasks/server-introductory.js
 * for why this runs connect directly, and grunt/tier-servers.js for the
 * full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-intermediate', 'Runs the reserved intermediate-tier preview server on port 9002 (locked)', ['_log-server:serverIntermediate', 'connect:serverIntermediate']);
};
