/**
 * content-version.js — shared content-version record for a course's exported
 * output, used by both tools/course-script-md.js (export) and
 * tools/course-script-import.js (edit -> rebuild round-trip).
 *
 * Record: exports/<shortSlug>.version.json
 *   { shortSlug, version: "1.03", history: [{ version, timestamp, event, ...meta }] }
 *
 * Versioning scheme: major.minor, e.g. "1.00" -> "1.01" -> "1.02". The first
 * call for a given shortSlug creates the record at "1.00" (no bump — nothing
 * came before it); every call after that increments the minor digit by one
 * (rolling the major digit at .99 -> next major, .00). Small edits and
 * regenerations are both "events" that bump it; this file doesn't
 * distinguish how big a change was, only that one happened.
 */
'use strict';
const fs = require('fs');
const path = require('path');

function parseVersion(v) {
  const m = /^(\d+)\.(\d{2})$/.exec(String(v || '').trim());
  if (!m) return { major: 1, minor: 0 };
  return { major: parseInt(m[1], 10), minor: parseInt(m[2], 10) };
}
function formatVersion(major, minor) { return `${major}.${String(minor).padStart(2, '0')}`; }
function nextVersion(v) {
  const { major, minor } = parseVersion(v);
  let nm = minor + 1, nM = major;
  if (nm > 99) { nm = 0; nM += 1; }
  return formatVersion(nM, nm);
}

function versionFile(shortSlug, outRoot) { return path.join(outRoot || 'exports', `${shortSlug}.version.json`); }

/** Read the current version without bumping it. '1.00' if no record yet. */
function currentVersion(shortSlug, outRoot) {
  const f = versionFile(shortSlug, outRoot);
  if (!fs.existsSync(f)) return '1.00';
  try { return JSON.parse(fs.readFileSync(f, 'utf8')).version || '1.00'; } catch (e) { return '1.00'; }
}

/**
 * Bump the version record for shortSlug and append a history entry.
 * event: short label, e.g. 'script-export', 'edit-import'.
 * meta: extra fields merged into the history entry (e.g. { file, fields }).
 * Returns the new version string.
 */
function bumpVersion(shortSlug, event, meta, outRoot) {
  outRoot = outRoot || 'exports';
  fs.mkdirSync(outRoot, { recursive: true });
  const f = versionFile(shortSlug, outRoot);
  let record = { shortSlug, version: '1.00', history: [] };
  if (fs.existsSync(f)) {
    try { record = JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { /* corrupt — start fresh at 1.00 */ }
    record.version = nextVersion(record.version);
  }
  record.history = record.history || [];
  record.history.push(Object.assign({ version: record.version, timestamp: new Date().toISOString(), event }, meta || {}));
  fs.writeFileSync(f, JSON.stringify(record, null, 2) + '\n');
  return record.version;
}

// ---- manifest / short-slug discovery (shared convention with course-export.js) ----

/**
 * Auto-discover a course's course-design_*.json manifest from a content dir,
 * when not passed explicitly. Direct: a course-design_*.json inside courseDir.
 * Else (e.g. a courses/_generated/<base>-<subject> merged dir): the
 * courses/<d> whose slug is a prefix of courseDir's basename.
 */
function resolveManifest(courseDir, manifestPath) {
  let mp = manifestPath, baseSlug = null;
  if (!mp) {
    const bn = path.basename(courseDir);
    const direct = fs.existsSync(courseDir) ? fs.readdirSync(courseDir).find(f => /^course-design_.*\.json$/.test(f)) : null;
    if (direct) { mp = path.join(courseDir, direct); baseSlug = direct.replace(/^course-design_/, '').replace(/\.json$/, ''); }
    else if (fs.existsSync('courses')) {
      for (const d of fs.readdirSync('courses')) {
        if (d === '_generated') continue;
        const mf = path.join('courses', d, `course-design_${d}.json`);
        if (fs.existsSync(mf) && bn.startsWith(d)) { mp = mf; baseSlug = d; break; }
      }
    }
  }
  const manifest = mp && fs.existsSync(mp) ? JSON.parse(fs.readFileSync(mp, 'utf8')) : null;
  return { manifestPath: mp, baseSlug, manifest };
}

/** shortSlug from onb-04_naming in a manifest, optionally with a subject suffix. */
function shortSlugFromManifest(manifest, subject) {
  if (!manifest) return null;
  const g = (manifest.gates || []).find(x => x.gateId === 'onb-04_naming');
  const r = g && g.records && g.records.length && g.records.reduce((a, b) => (b.seq > a.seq ? b : a));
  const base = r && r.decidedValue && r.decidedValue.shortSlug;
  if (!base) return null;
  return subject ? `${base}-${subject}` : base;
}

/** Compact UTC timestamp in YYMMDDHHMMSS form, for filenames. */
function stamp() {
  const d = new Date();
  const p = n => String(n).padStart(2, '0');
  return p(d.getUTCFullYear() % 100) + p(d.getUTCMonth() + 1) + p(d.getUTCDate()) + p(d.getUTCHours()) + p(d.getUTCMinutes()) + p(d.getUTCSeconds());
}

module.exports = { parseVersion, formatVersion, nextVersion, currentVersion, bumpVersion, resolveManifest, shortSlugFromManifest, stamp };
