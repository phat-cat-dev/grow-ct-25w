/**
 * Reserved advanced-tier dev preview server.
 *
 * Locked to port 9003, serving build-advanced/ (staged via
 * `grunt stage-tier:advanced`) as a plain page. For the rarer SCORM
 * tracking check, see server-advanced-scorm.js (port 9013, same staged
 * build). See grunt/tasks/server-introductory.js for why this runs
 * connect directly, and grunt/tier-servers.js for the full tier map.
 */
module.exports = function(grunt) {
  grunt.registerTask('server-advanced', 'Runs the reserved advanced-tier preview server on port 9003 (locked)', ['_log-server:serverAdvanced', 'connect:serverAdvanced']);
};
