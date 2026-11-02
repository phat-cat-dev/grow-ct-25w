/**
 * Single source of truth for the three reserved tier-preview servers and
 * their rarely-needed SCORM-harness counterparts.
 *
 * Each tier gets two locked ports serving the SAME staged build (see
 * grunt/tasks/stage-tier.js):
 *   - previewPort: plain dev preview (index.html), for reviewing a tier as
 *     you develop it, after a rebuild + restage.
 *   - scormPort: the SCORM test harness (scorm_test_harness.html), for the
 *     rare occasions tracking behaviour needs checking before a Moodle
 *     upload.
 *
 * Both ports for a tier share one hostname, not just because they're the
 * same tier: SCORM tracking state lives in a `_spoor` cookie
 * (src/extensions/adapt-contrib-spoor/js/scorm/cookieLMS.js), and cookies
 * are scoped by host, not port. Sharing a hostname between preview and
 * harness for one tier is fine (same course, continuous tracking); what
 * must NOT share a hostname is different TIERS - three tiers all on plain
 * `localhost` would read and write the same cookie and overwrite each
 * other's tracking. `*.localhost` resolves to 127.0.0.1 in current
 * Chrome/Firefox with no server-side DNS dependency; the servers
 * themselves still bind every interface.
 *
 * Read by grunt/config/connect.js (target definitions), grunt/helpers.js
 * (_log-server's tier-aware logging) and grunt/tasks/stage-tier.js (build/
 * -> build-<tier>/ staging).
 */
module.exports = {
  introductory: {
    previewTarget: 'serverIntroductory',
    previewPort: 9001,
    scormTarget: 'serverIntroductoryScorm',
    scormPort: 9011,
    dir: 'build-introductory/',
    hostname: 'introductory.localhost'
  },
  intermediate: {
    previewTarget: 'serverIntermediate',
    previewPort: 9002,
    scormTarget: 'serverIntermediateScorm',
    scormPort: 9012,
    dir: 'build-intermediate/',
    hostname: 'intermediate.localhost'
  },
  advanced: {
    previewTarget: 'serverAdvanced',
    previewPort: 9003,
    scormTarget: 'serverAdvancedScorm',
    scormPort: 9013,
    dir: 'build-advanced/',
    hostname: 'advanced.localhost'
  }
};
