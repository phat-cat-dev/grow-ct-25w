/**
 * Single source of truth for the three reserved tier-preview servers.
 *
 * Each tier gets a locked port serving a dedicated, staged copy of a build
 * (see grunt/tasks/stage-tier.js). The hostname is distinct per tier, not
 * just the port: SCORM tracking state lives in a `_spoor` cookie
 * (src/extensions/adapt-contrib-spoor/js/scorm/cookieLMS.js), and cookies
 * are scoped by host, not port - three harnesses on plain `localhost` would
 * all read and write the same cookie and overwrite each other's tracking.
 * `*.localhost` resolves to 127.0.0.1 in current Chrome/Firefox with no
 * server-side DNS dependency; the server itself still binds every interface.
 *
 * Read by grunt/config/connect.js (target definitions), grunt/helpers.js
 * (_log-server's tier-aware logging) and grunt/tasks/stage-tier.js (build/
 * -> build-<tier>/ staging).
 */
module.exports = {
  introductory: {
    target: 'serverIntroductory',
    port: 9001,
    dir: 'build-introductory/',
    hostname: 'introductory.localhost'
  },
  intermediate: {
    target: 'serverIntermediate',
    port: 9002,
    dir: 'build-intermediate/',
    hostname: 'intermediate.localhost'
  },
  advanced: {
    target: 'serverAdvanced',
    port: 9003,
    dir: 'build-advanced/',
    hostname: 'advanced.localhost'
  }
};
