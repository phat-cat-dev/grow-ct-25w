const tierServers = require('../tier-servers');

module.exports = function(grunt, options) {

  const port = parseInt(grunt.option('port')) || 9000;
  const host = grunt.option('host') || 'localhost';

  const config = {
    server: {
      options: {
        port,
        base: '<%= outputdir %>',
        keepalive: true,
        open: true
      }
    },
    'server-silent': {
      options: {
        port,
        base: '<%= outputdir %>',
        keepalive: true,
        open: false
      }
    },
    spoorOffline: {
      options: {
        port,
        base: '<%= outputdir %>',
        keepalive: true,
        open: 'http://' + host + ':' + port + '/scorm_test_harness.html'
      }
    }
  };

  // Reserved tier-preview and tier-SCORM targets: port and base are
  // literals, not grunt options, so --port/--outputdir cannot move them.
  // See grunt/tier-servers.js.
  Object.values(tierServers).forEach(({ previewTarget, previewPort, scormTarget, scormPort, dir }) => {
    config[previewTarget] = {
      options: {
        port: previewPort,
        base: dir,
        keepalive: true,
        open: false
      }
    };
    config[scormTarget] = {
      options: {
        port: scormPort,
        base: dir,
        keepalive: true,
        open: false
      }
    };
  });

  return config;
};
