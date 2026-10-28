#!/usr/bin/env node
/**
 * export-references.js — per-course references worksheet (export + round-trip import).
 *
 * EXPORT (default): collect every `references` component in a course (each
 * lesson's "Lesson Sources" and the course-level "Course Sources" at the end),
 * ordered by page, and write an editable Markdown worksheet with a LINK slot
 * under each reference entry. You paste the URLs in, then:
 *
 * IMPORT (--import): read the filled worksheet back and write each LINK into the
 * matching component's _items[n].href in en/components.json.
 *
 *   node tools/export-references.js [--course=<slug>] [--import]
 *
 * --course defaults to whatever src/course points at. Worksheet lives at
 * exports/references/<course>.md (stable path, re-exported/overwritten each run).
 *
 * Each entry is anchored as `[<componentId> #<itemIndex>]` so import maps links
 * back precisely; keep those anchors intact when editing.
 */
'use strict';
const fs = require('fs');
const path = require('path');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);

function arg(name) { const p = process.argv.find(a => a.startsWith(`--${name}=`)); return p ? p.split('=').slice(1).join('=') : null; }
const IMPORT = process.argv.includes('--import');

function resolveCourseDir(slug) {
  if (!slug) {
    const link = path.join(ROOT, 'src', 'course');
    const t = fs.readlinkSync(link);
    return path.resolve(path.dirname(link), t);
  }
  for (const p of [path.join(ROOT, 'courses', slug), path.join(ROOT, 'courses', '_generated', slug)])
    if (fs.existsSync(p)) return p;
  throw new Error(`course not found: ${slug}`);
}

const courseDir = resolveCourseDir(arg('course'));
const courseName = path.basename(courseDir);
const enDir = path.join(courseDir, 'en');
const read = f => JSON.parse(fs.readFileSync(path.join(enDir, f), 'utf8'));

const components = read('components.json');
const blocks = read('blocks.json');
const articles = read('articles.json');
const contentObjects = read('contentObjects.json');

// map id -> parent, and page order/title
const parentOf = {};
for (const a of [...components, ...blocks, ...articles, ...contentObjects]) parentOf[a._id] = a._parentId;
const pageById = {};
contentObjects.forEach((co, i) => { pageById[co._id] = { title: co.title || co._id, order: i, id: co._id }; });

function pageOf(componentId) {
  let id = componentId, guard = 0;
  while (id && guard++ < 20) { if (pageById[id]) return pageById[id]; id = parentOf[id]; }
  return { title: '(unknown page)', order: 999, id: '?' };
}

// every references component, ordered by page then by id
const refs = components.filter(c => c._component === 'references')
  .map(c => ({ c, page: pageOf(c._id) }))
  .sort((a, b) => a.page.order - b.page.order || a.c._id.localeCompare(b.c._id));

const worksheetDir = path.join(ROOT, 'exports', 'references');
const worksheetPath = path.join(worksheetDir, `${courseName}.md`);

// ----------------------------------------------------------------------------
if (!IMPORT) {
  const lines = [];
  lines.push(`# References worksheet — ${courseName}`);
  lines.push('');
  lines.push('Paste each source URL on the `LINK:` line below its entry, then run:');
  lines.push('`node tools/export-references.js --import` (same --course). Keep the `[id #n]` anchors.');
  lines.push('');
  for (const { c, page } of refs) {
    const label = `${page.id} · ${page.title} — ${c.displayTitle || c.title || 'References'}`;
    lines.push(`## ${label}  (${c._id})`);
    lines.push('');
    (c._items || []).forEach((it, i) => {
      lines.push(`- [${c._id} #${i}] ${it.title || '(untitled source)'}`);
      lines.push(`  LINK: ${it.href && it.href !== '#' ? it.href : ''}`);
      if (it.type) lines.push(`  _(type: ${it.type})_`);
      lines.push('');
    });
  }
  fs.mkdirSync(worksheetDir, { recursive: true });
  fs.writeFileSync(worksheetPath, lines.join('\n'));
  console.log(`Wrote worksheet: ${path.relative(ROOT, worksheetPath)}`);
  console.log(`  ${refs.length} references component(s), ${refs.reduce((n, r) => n + (r.c._items || []).length, 0)} source(s).`);
  console.log('Fill the LINK: lines, then re-run with --import to write them into components.json.');
  process.exit(0);
}

// ----------------------------------------------------------------------------
// IMPORT: parse the worksheet, write hrefs back
if (!fs.existsSync(worksheetPath)) { console.error(`No worksheet at ${path.relative(ROOT, worksheetPath)} — run export first.`); process.exit(2); }
const text = fs.readFileSync(worksheetPath, 'utf8');
const byId = Object.fromEntries(components.map(c => [c._id, c]));
const lines = text.split(/\r?\n/);
let current = null, applied = 0, skipped = 0;
const anchorRe = /^- \[([A-Za-z0-9_-]+) #(\d+)\]/;
const linkRe = /^\s*LINK:\s*(\S.*)?$/;
for (let i = 0; i < lines.length; i++) {
  const m = lines[i].match(anchorRe);
  if (m) { current = { id: m[1], idx: parseInt(m[2], 10) }; continue; }
  const l = lines[i].match(linkRe);
  if (l && current) {
    const url = (l[1] || '').trim();
    if (url) {
      const comp = byId[current.id];
      if (comp && comp._items && comp._items[current.idx]) {
        comp._items[current.idx].href = url;
        applied++;
      } else { skipped++; console.warn(`  ! no item ${current.id} #${current.idx}`); }
    }
    current = null;
  }
}
if (applied) fs.writeFileSync(path.join(enDir, 'components.json'), JSON.stringify(components, null, 2) + '\n');
console.log(`Import: wrote ${applied} link(s) into ${path.relative(ROOT, path.join(enDir, 'components.json'))}${skipped ? `, skipped ${skipped}` : ''}.`);
console.log('Rebuild to see them (viewer: cr / build).');
