#!/usr/bin/env node
/**
 * set-profile.js
 *
 * D1 (distillation-unblock-decisions.md, Abbott-ruled): the only tool that
 * can set a manifest's top-level `profile` field once the manifest already
 * exists. `tools/new-course.js` writes `profile` once, at creation, and only
 * on the `pitch === "all"` multi-tier path (D1's evidence); it hard-refuses
 * to touch a manifest that already carries one (`new-course.js:240-246`).
 * `tools/reopen.js` appends only gate records and sweep events
 * (`applyReopen`); it cannot reach a top-level field. Neither tool can
 * change `profile` on an existing single-tier manifest, which is exactly
 * the three `presenting-*` courses' situation.
 *
 * String-asserted edit (CLAUDE.md): the caller must name the manifest's
 * CURRENT profile value (or "absent") before this tool writes the new one,
 * so drift between what the caller believes and what the manifest actually
 * holds surfaces as a refusal, not a silent wrong-target write.
 *
 * Usage:
 *   node tools/set-profile.js --course=<slug> --from=<current-profile|absent> --profile=<new-profile>
 *
 * --from must equal the manifest's current `profile` value exactly
 * (the literal string "absent" when the manifest carries no `profile` key
 * at all). --profile must be one of the three ids
 * schemas/course-design.schema.json's `profile` enum allows.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

function fail(message) {
  console.error(`REFUSED: ${message}`);
  process.exit(1);
}

function loadProfileEnum() {
  const schemaPath = path.join(ROOT, 'schemas', 'course-design.schema.json');
  if (!fs.existsSync(schemaPath)) fail(`schema not found: ${schemaPath}`);
  let schema;
  try { schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8')); }
  catch (err) { fail(`schema is not valid JSON: ${schemaPath} (${err.message})`); }
  const profileDef = schema.properties && schema.properties.profile;
  if (!profileDef || !Array.isArray(profileDef.enum)) {
    fail(`${schemaPath} carries no properties.profile.enum: cannot validate the new value against it`);
  }
  return profileDef.enum;
}

function parseArgs(argv) {
  const args = { course: null, from: null, profile: null };
  argv.forEach(param => {
    const eq = param.indexOf('=');
    if (eq === -1) return;
    const key = param.slice(2, eq);
    const value = param.slice(eq + 1);
    if (key === 'course') args.course = value;
    if (key === 'from') args.from = value;
    if (key === 'profile') args.profile = value;
  });
  return args;
}

function findManifestPath(slug) {
  const courseDir = path.join(ROOT, 'courses', slug);
  if (!fs.existsSync(courseDir)) fail(`no course directory at ${courseDir}`);
  const manifestPath = path.join(courseDir, `course-design_${slug}.json`);
  if (!fs.existsSync(manifestPath)) fail(`no manifest at ${manifestPath}`);
  return manifestPath;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.course) fail('--course=<slug> is required.');
  if (!args.from) fail('--from=<current-profile|absent> is required (string-asserted edit: name what the manifest currently holds).');
  if (!args.profile) fail('--profile=<new-profile> is required.');

  const profileEnum = loadProfileEnum();
  if (!profileEnum.includes(args.profile)) {
    fail(`--profile="${args.profile}" is not one of schemas/course-design.schema.json's allowed values: ${profileEnum.join(', ')}.`);
  }

  const manifestPath = findManifestPath(args.course);
  let manifest;
  try { manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8')); }
  catch (err) { fail(`manifest is not valid JSON: ${manifestPath} (${err.message})`); }

  const currentProfile = Object.prototype.hasOwnProperty.call(manifest, 'profile') ? manifest.profile : 'absent';
  if (currentProfile !== args.from) {
    fail(`${manifestPath} currently carries profile="${currentProfile}", not "${args.from}" as asserted. Refusing to write: re-check --from against the manifest's actual current value.`);
  }
  if (currentProfile === args.profile) {
    fail(`${manifestPath} already carries profile="${args.profile}": nothing to change.`);
  }

  manifest.profile = args.profile;
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');

  console.log(`Wrote ${manifestPath}`);
  console.log(`profile: "${currentProfile}" -> "${args.profile}"`);
}

main();
