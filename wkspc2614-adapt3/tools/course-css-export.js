#!/usr/bin/env node
/**
 * course-css-export.js — copy the built course's compiled CSS (adapt.css)
 * into exports/, versioned the same way as course-script-md.js.
 *
 * Runs automatically at the end of `grunt build` (see grunt/tasks/
 * course-css-export.js), replacing the former course-script-md auto-export.
 *
 * Usage:
 *   node tools/course-css-export.js --course <content-dir> [--short-slug <slug>]
 *        [--subject <ctx>] [--manifest <course-design.json>] [--out exports]
 *        [--build build]
 *
 * Output: <out>/<short-slug>-<YYMMDDHHMMSS>.css (a new, timestamped file each
 * run — see tools/lib/content-version.js for the version record kept
 * alongside it at <out>/<short-slug>.version.json).
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { resolveManifest, shortSlugFromManifest, bumpVersion, stamp } = require('./lib/content-version');

function arg(name, def) { const i = process.argv.indexOf('--' + name); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : def; }
const courseDir = arg('course');
let shortSlug = arg('short-slug', null);
const subject = arg('subject', null); // appended to the manifest shortSlug for a subject build
let manifestPath = arg('manifest', null);
const outRoot = arg('out', 'exports');
const buildDir = arg('build', 'build');
if (!courseDir) {
  console.error('usage: node tools/course-css-export.js --course <content-dir> [--short-slug <slug>] [--subject <ctx>] [--manifest <file>] [--out exports] [--build build]');
  process.exit(2);
}

const cssPath = path.join(buildDir, 'adapt.css');
if (!fs.existsSync(cssPath)) {
  console.error(`course-css-export: no compiled CSS found at ${cssPath} — run grunt build first`);
  process.exit(2);
}

// Auto-discover the base manifest when not passed, same convention as
// course-export.js / course-script-md.js, so the build task can run with
// just --course.
const resolved = resolveManifest(courseDir, manifestPath);
manifestPath = resolved.manifestPath;
// shortSlug: explicit --short-slug wins; else from onb-04_naming.shortSlug in the
// manifest, with --subject appended for a subject build.
if (!shortSlug) shortSlug = shortSlugFromManifest(resolved.manifest, subject);
if (!shortSlug) { console.error('No short slug: pass --short-slug, or supply --manifest whose onb-04_naming records a shortSlug.'); process.exit(2); }

const fileStamp = stamp();
const fileName = `${shortSlug}-${fileStamp}.css`;
const version = bumpVersion(shortSlug, 'css-export', { file: fileName }, outRoot);
fs.mkdirSync(outRoot, { recursive: true });
const outFile = path.join(outRoot, fileName);
fs.copyFileSync(cssPath, outFile);
const { size } = fs.statSync(outFile);
console.log(`Course CSS: ${outFile}`);
console.log(`Content version: ${shortSlug} -> v${version}`);
console.log(`Size: ${(size / 1024).toFixed(1)} KiB`);
