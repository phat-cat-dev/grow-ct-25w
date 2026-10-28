#!/usr/bin/env node
/* render-stubs.js
   Renders a lesson or course Markdown file (YAML front matter plus a body
   skeleton) from a record, using the .md.hbs templates in this folder.

     npm install handlebars          (js-yaml too, only if you use --check)

     node render-stubs.js lesson record.json [--course course.json] [--out lesson.md]
     node render-stubs.js course record.json [--out course.md]

   The input may be the record itself, { record, course } for a lesson or { course } for a course. Anything you leave
   out falls back to the placeholders in *-stub.defaults.json. Values you do not
   supply and can be derived are derived, not retyped (spec section 5):
     lesson   duration, level, learner objectives, course_id and parent_id
     course   duration, level, learner objectives
   --date YYYY-MM-DD   created and updated dates (default today)
   --check             parse the front matter back and confirm it equals the data
*/
const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

/* ---------- arguments ---------- */
const args = process.argv.slice(2);
const kind = args[0];
const inputPath = args[1];
const opt = (name) => { const i = args.indexOf(name); return i > -1 ? args[i + 1] : null; };
if (!['lesson', 'course'].includes(kind) || !inputPath) {
  console.error('Usage: node render-stubs.js <lesson|course> record.json [--course course.json] [--out file.md] [--date YYYY-MM-DD] [--check]');
  process.exit(1);
}
const dir = __dirname;
const read = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));

/* ---------- helpers ---------- */
const q = (v) => {
  if (v === undefined || (v && typeof v === 'object' && !Array.isArray(v) && v.hash)) return 'null';
  if (Array.isArray(v) && v.every((x) => x === null || typeof x !== 'object')) return `[${v.map((x) => JSON.stringify(x)).join(', ')}]`;
  return JSON.stringify(v);
};
const isBare = (v) => typeof v === 'string' && /^[A-Za-z][A-Za-z0-9._-]*$/.test(v) && !/^(true|false|null|yes|no|on|off)$/i.test(v);
const e = (v) => (isBare(v) ? v : q(v));
const fold = (text, n) => {
  const pad = ' '.repeat(typeof n === 'number' ? n : 4);
  const words = String(text == null ? '' : text).split(/\s+/).filter(Boolean);
  const lines = [];
  let line = '';
  words.forEach((w) => {
    if (line && (pad.length + line.length + 1 + w.length) > 78) { lines.push(line); line = w; }
    else line = line ? `${line} ${w}` : w;
  });
  if (line) lines.push(line);
  return lines.length ? lines.map((l) => pad + l).join('\n') : pad;
};
Handlebars.registerHelper({ q, e, fold });

/* ---------- data ---------- */
const isObj = (v) => v && typeof v === 'object' && !Array.isArray(v);
function merge(base, over) {
  if (!isObj(base) || !isObj(over)) return over === undefined ? base : over;
  const out = { ...base };
  Object.keys(over).forEach((k) => { out[k] = isObj(base[k]) && isObj(over[k]) ? merge(base[k], over[k]) : over[k]; });
  return out;
}
const minutes = (m) => (m < 60 ? `${m} min` : `${Math.floor(m / 60)} h${m % 60 ? ` ${m % 60} min` : ''}`);
const cap = (s) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : s);
/* supplied means present and not null, so an explicit null asks for the value to be derived */
const has = (obj, ...keys) => { const v = keys.reduce((o, k) => (o == null ? undefined : o[k]), obj); return v !== undefined && v !== null; };

const raw = read(inputPath);
let input = kind === 'course' ? (raw.course || raw.record || raw) : (raw.record || raw);
let course = null;
if (opt('--course')) { const c = read(opt('--course')); course = c.course || c; }
else if (kind === 'lesson' && raw.course) course = raw.course;

const today = opt('--date') || new Date().toISOString().slice(0, 10);
const defaults = read(path.join(dir, `${kind}-stub.defaults.json`));
let data = merge(defaults, input);
if (!has(input, 'created')) data.created = today;
if (!has(input, 'updated')) data.updated = today;

const pitch = course && ((course.audience || {}).learner_pitch || course.learner_pitch);

if (kind === 'lesson') {
  if (course && course.id) {
    if (!has(input, 'course_id')) data.course_id = course.id;
    if (!has(input, 'parent_id')) data.parent_id = course.id;
  }
  if (!has(input, 'frontmatter', 'meta', 'duration') && data.estimated_duration_minutes) data.frontmatter.meta.duration = minutes(data.estimated_duration_minutes);
  if (!has(input, 'frontmatter', 'meta', 'level') && pitch) data.frontmatter.meta.level = cap(pitch);
  if (!has(input, 'frontmatter', 'objectives') && has(input, 'learning_outcomes')) data.frontmatter.objectives = data.learning_outcomes.map((o) => o.statement);
} else {
  const total = data.delivery.estimated_duration_minutes || data.lesson_map.reduce((n, l) => n + (l.estimated_duration_minutes || 0), 0);
  if (!has(input, 'frontmatter', 'meta', 'duration') && total) data.frontmatter.meta.duration = minutes(total);
  if (!has(input, 'frontmatter', 'meta', 'level') && has(input, 'audience', 'learner_pitch')) data.frontmatter.meta.level = cap(data.audience.learner_pitch);
  if (!has(input, 'frontmatter', 'objectives') && has(input, 'outcomes')) data.frontmatter.objectives = data.outcomes.map((o) => o.statement);
}

/* ---------- render ---------- */
const template = Handlebars.compile(fs.readFileSync(path.join(dir, `${kind}-stub.md.hbs`), 'utf8'), { noEscape: true });
const md = template(data).replace(/\n{3,}/g, '\n\n');

const out = opt('--out');
if (out) { fs.writeFileSync(out, md); console.error('wrote', out); } else process.stdout.write(md);

/* ---------- optional round-trip check ---------- */
if (args.includes('--check')) {
  const yaml = require('js-yaml');
  const m = md.match(/^---\n([\s\S]*?)\n---\n/);
  const parsed = yaml.load(m[1]);
  /* trim strings, and treat a null field the same as a missing one */
  const norm = (v) => JSON.parse(JSON.stringify(v, (k, x) => {
    if (typeof x === 'string') return x.trim();
    if (x && typeof x === 'object' && !Array.isArray(x)) return Object.fromEntries(Object.entries(x).filter(([, y]) => y !== null));
    return x;
  }));
  const expect = norm({ ...data, document_type: kind === 'lesson' ? 'lesson' : 'course-scope', ...(kind === 'course' ? { hierarchy_level: 0 } : {}) });
  const got = norm(parsed);
  /* key order does not matter: the template writes keys in spec order */
  const canon = (v) => (Array.isArray(v) ? v.map(canon) : v && typeof v === 'object'
    ? Object.fromEntries(Object.keys(v).sort().map((k) => [k, canon(v[k])])) : v);
  const diffs = [];
  Object.keys(got).forEach((k) => { if (JSON.stringify(canon(got[k])) !== JSON.stringify(canon(expect[k]))) diffs.push(k); });
  const dropped = Object.keys(expect).filter((k) => !(k in got));
  if (dropped.length) console.error('WARNING: not written by the template (add them to the .md.hbs or remove them):', dropped.join(', '));
  if (diffs.length) { console.error('CHECK FAILED for keys:', diffs.join(', ')); process.exit(2); }
  console.error(`CHECK OK: ${Object.keys(got).length} front matter keys parse back to the same data`);
}
