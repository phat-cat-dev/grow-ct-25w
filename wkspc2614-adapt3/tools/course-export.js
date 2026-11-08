#!/usr/bin/env node
/**
 * course-export.js — generate a human-readable export BUNDLE of a built course.
 *
 * Walks a built course's content model (config.json + en/*.json) in reading
 * order (page -> article -> block -> component) and emits several views of the
 * same content into one timestamped, short-slug-named folder:
 *
 *   exports/<short-slug>_<timestamp>/
 *     html/<slug>.full.html        max metadata: every _id/_component/_classes/
 *                                  _layout/_trackingId/_skeletonKey, CXP slot
 *                                  markers, feedback/modal text, as data-* attrs
 *     html/<slug>.structural.html  clean presentational DOM (article>block>
 *                                  component>p) with classes/attributes only
 *     templates/lesson.annotated.html  one lesson as produced, annotated with
 *                                  ids, slot/coupling markers and metadata
 *     md/<slug>.script.md          the "screenplay": all prose + every activity
 *                                  + feedback/modal text, in reading order
 *     md/<slug>.course-pack.md     course + per-lesson GATED DECISIONS (not
 *                                  content), W-OPEN decisions first, W-CLOSE last
 *     yaml/<slug>.yaml             structured data twin (ids + fields)
 *     json/course-design_<slug>.json   the gated AI decisions (copied, if given)
 *     json/packs/<page>.json           the AI-output content packs (copied, if found)
 *
 * Usage:
 *   node tools/course-export.js --course <content-dir> --short-slug <slug> \
 *        [--manifest <course-design.json>] [--packs <dir>] [--label base|psych] \
 *        [--out exports]
 *
 * One-way export. A separate import tool (course-script-import.js) handles the
 * edit -> rebuild round-trip; this tool never writes to the course.
 */
'use strict';
const fs = require('fs');
const path = require('path');

function arg(name, def) { const i = process.argv.indexOf('--' + name); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : def; }
const courseDir = arg('course');
let shortSlug = arg('short-slug', null);
const subject = arg('subject', null); // appended to the manifest shortSlug for a subject build
let manifestPath = arg('manifest', null);
let packsDir = arg('packs', null);
const label = arg('label', '');
const outRoot = arg('out', 'exports');
if (!courseDir) {
  console.error('usage: node tools/course-export.js --course <content-dir> [--short-slug <slug>] [--subject <ctx>] [--manifest <file>] [--packs <dir>] [--out exports]');
  process.exit(2);
}
const rd = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const stripTags = s => String(s == null ? '' : s).replace(/<[^>]+>/g, '').trim();
// prose(): HTML -> readable text, preserving paragraph and list breaks (for the .md script).
const prose = s => String(s == null ? '' : s)
  .replace(/<li[^>]*>/gi, '\n- ')
  .replace(/<\/(p|li|h[1-6]|div|ul|ol)>/gi, '\n\n')
  .replace(/<br\s*\/?>/gi, '\n')
  .replace(/<[^>]+>/g, '')
  .replace(/\n{3,}/g, '\n\n')
  .replace(/[ \t]+\n/g, '\n')
  .trim();

const cfg = rd(path.join(courseDir, 'config.json'));
const en = f => rd(path.join(courseDir, 'en', f));
const course = en('course.json');
const cos = en('contentObjects.json');
const articles = en('articles.json');
const blocks = en('blocks.json');
const components = en('components.json');
const courseObj = Array.isArray(course) ? course[0] : course;
// Auto-discover the base manifest and packs when not passed, so the build task
// can run with just --course. Direct: a course-design_*.json inside courseDir.
// Else (e.g. a courses/_generated/<base>-<subject> merged dir): the
// courses/v1/<d> or courses/v2/<d> (v1/v2 split, 8 Nov 2026) whose slug is a
// prefix of courseDir's basename.
let baseSlug = null;
if (!manifestPath) {
  const bn = path.basename(courseDir);
  const direct = fs.existsSync(courseDir) ? fs.readdirSync(courseDir).find(f => /^course-design_.*\.json$/.test(f)) : null;
  if (direct) { manifestPath = path.join(courseDir, direct); baseSlug = direct.replace(/^course-design_/, '').replace(/\.json$/, ''); }
  else {
    outer:
    for (const version of ['v1', 'v2']) {
      const versionDir = path.join('courses', version);
      if (!fs.existsSync(versionDir)) continue;
      for (const d of fs.readdirSync(versionDir)) {
        const mf = path.join(versionDir, d, `course-design_${d}.json`);
        if (fs.existsSync(mf) && bn.startsWith(d)) { manifestPath = mf; baseSlug = d; break outer; }
      }
    }
  }
}
if (!packsDir && baseSlug) {
  const bn = path.basename(courseDir);
  const ctx = bn.length > baseSlug.length ? bn.slice(baseSlug.length + 1) : 'baseline';
  const cand = path.join('content', 'context-packs', ctx, baseSlug);
  if (fs.existsSync(cand)) packsDir = cand;
  else { const bl = path.join('content', 'context-packs', 'baseline', baseSlug); if (fs.existsSync(bl)) packsDir = bl; }
}
const manifest = manifestPath && fs.existsSync(manifestPath) ? rd(manifestPath) : null;
// shortSlug: explicit --short-slug wins; else from onb-04_naming.shortSlug in the
// manifest, with --subject appended for a subject build.
if (!shortSlug && manifest) {
  const g = (manifest.gates || []).find(x => x.gateId === 'onb-04_naming');
  const r = g && g.records && g.records.reduce((a, b) => (b.seq > a.seq ? b : a));
  const base = r && r.decidedValue && r.decidedValue.shortSlug;
  if (base) shortSlug = base + (subject ? '-' + subject : '');
}
if (!shortSlug) { console.error('No short slug: pass --short-slug, or supply --manifest whose onb-04_naming records a shortSlug.'); process.exit(2); }

// ---- tree ----
const childrenOf = (arr, pid) => arr.filter(x => x._parentId === pid);
const menu = cos.find(o => o._type === 'menu');
const courseId = courseObj._id || (menu && menu._parentId);
// pages: content objects of _type page, in file (course) order
const pages = cos.filter(o => o._type === 'page');

// ---- component content extraction ----
// Returns an ordered list of { kind, label, text } chunks for a component,
// covering prose, activity items/options, and feedback/modal text.
function extract(c) {
  const out = [];
  const push = (kind, label, text, meta) => { if (text != null && String(text).length) out.push({ kind, label, text: String(text), ...(meta || {}) }); };
  if (c.body) push('body', null, c.body);
  const t = c._component;
  const items = c._items || [];
  if (t === 'mcq' || t === 'sortable') {
    items.forEach((it, i) => push('option', `Option ${i + 1}${it._shouldBeSelected ? ' (correct)' : ''}`, it.text));
  } else if (t === 'matching') {
    items.forEach((it, i) => {
      push('match-stem', `Row ${i + 1}`, it.text);
      (it._options || []).forEach(o => push('match-option', `  option${o._isCorrect ? ' (correct)' : ''}`, o.text));
    });
  } else if (t === 'flipcard') {
    items.forEach((it, i) => {
      push('card-front', `Card ${i + 1} front`, (it.front && (it.front.title || it.front.body)) || '');
      push('card-back', `Card ${i + 1} back`, (it.back && (it.back.body || it.back.title)) || '');
    });
  } else if (t === 'accordion' || t === 'hotgraphic') {
    items.forEach((it, i) => { push('item-title', `Item ${i + 1}`, it.title); push('item-body', null, it.body); });
  } else if (t === 'checklist' || t === 'confidence') {
    items.forEach((it, i) => push('item', `Item ${i + 1}`, it.text));
  } else if (t === 'references') {
    items.forEach((it, i) => push('reference', `Reference ${i + 1}`, [it.title, it.href].filter(Boolean).join(' — ')));
  }
  if (c.placeholder) push('placeholder', 'Placeholder', c.placeholder);
  // feedback / modal text
  const fb = c._feedback;
  if (fb) {
    if (fb.correct) push('feedback', 'Feedback — correct', fb.correct);
    if (fb._incorrect && fb._incorrect.notFinal) push('feedback', 'Feedback — incorrect (not final)', fb._incorrect.notFinal);
    if (fb._incorrect && fb._incorrect.final) push('feedback', 'Feedback — incorrect (final)', fb._incorrect.final);
    if (fb._partlyCorrect && fb._partlyCorrect.notFinal) push('feedback', 'Feedback — partly correct (not final)', fb._partlyCorrect.notFinal);
    if (fb._partlyCorrect && fb._partlyCorrect.final) push('feedback', 'Feedback — partly correct (final)', fb._partlyCorrect.final);
  }
  return out;
}

const coupling = c => {
  const m = String(c._classes || '').match(/slot__([A-Za-z0-9-]+)__([A-Za-z0-9-]+)(?:__([A-Za-z0-9-]+))?/);
  return m ? { page: m[1], slot: m[2], part: m[3] || null } : null;
};

// =====================================================================
// 1. SCRIPT (.md) — the screenplay
// =====================================================================
function scriptMd() {
  const L = [];
  L.push(`# ${stripTags(courseObj.displayTitle || courseObj.title || slug)} — course script  <!-- ${shortSlug} -->`);
  L.push(`\n_Reading-order export of all authored text (prose, activities, feedback/modal). Generated ${new Date().toISOString()}._`);
  for (const page of pages) {
    L.push(`\n## ${stripTags(page.displayTitle || page.title || page._id)}  <!-- page ${page._id} -->`);
    for (const a of childrenOf(articles, page._id)) {
      if (a.displayTitle) L.push(`\n### ${stripTags(a.displayTitle)}  <!-- article ${a._id} -->`);
      for (const b of childrenOf(blocks, a._id)) {
        for (const c of childrenOf(components, b._id)) {
          const head = stripTags(c.displayTitle) || b.title || `(${c._component})`;
          L.push(`\n#### ${head}  <!-- ${c._id} ${c._component} -->`);
          const cpl = coupling(c);
          const chunks = extract(c);
          if (cpl && !chunks.length) L.push(`\n_⟦ CXP slot ${cpl.page}/${cpl.slot}${cpl.part ? '/' + cpl.part : ''} — subject-filled at merge; empty in the base ⟧_`);
          if (c.instruction) L.push(`\n_${stripTags(c.instruction)}_`);
          for (const ch of chunks) {
            if (ch.kind === 'feedback') L.push(`\n> **${ch.label}:** ${stripTags(ch.text)}`);
            else if (ch.label) L.push(`\n- **${ch.label}:** ${stripTags(ch.text)}`);
            else L.push(`\n${prose(ch.text)}`);
          }
        }
      }
    }
  }
  return L.join('\n') + '\n';
}

// =====================================================================
// 2. FULL HTML — maximum Adapt id + metadata
// =====================================================================
function fullHtml() {
  const H = [];
  H.push('<!doctype html><html><head><meta charset="utf-8"><title>' + esc(shortSlug) + ' — full structure</title>');
  H.push('<style>body{font-family:system-ui,sans-serif;margin:2rem;line-height:1.5}.page{border:2px solid #456;margin:1.5rem 0;padding:1rem}.article{border-left:4px solid #789;margin:1rem 0;padding:.5rem 1rem}.block{border-left:3px solid #9ab;margin:.75rem 0;padding:.25rem 1rem}.component{border-left:2px solid #bcd;margin:.5rem 0;padding:.25rem 1rem}.meta{font:12px monospace;color:#468;background:#f4f7fa;padding:2px 6px;border-radius:3px}.slot{color:#a40;font-weight:700}.fb{color:#063;font-style:italic}h1,h2,h3,h4{margin:.3rem 0}</style></head><body>');
  H.push(`<h1>${esc(courseObj.displayTitle || courseObj.title || slug)} <span class="meta">course ${esc(courseId)}</span></h1>`);
  for (const page of pages) {
    H.push(`<section class="page"><h2>${esc(stripTags(page.displayTitle || page.title))} <span class="meta">page · ${esc(page._id)}</span></h2>`);
    for (const a of childrenOf(articles, page._id)) {
      H.push(`<div class="article"><h3>${esc(stripTags(a.displayTitle) || '(untitled article)')} <span class="meta">article · ${esc(a._id)} · classes="${esc(a._classes || '')}"</span></h3>`);
      for (const b of childrenOf(blocks, a._id)) {
        H.push(`<div class="block"><span class="meta">block · ${esc(b._id)} · trackingId=${esc(b._trackingId)} · skeletonKey=${esc(b._skeletonKey || '')}</span>`);
        for (const c of childrenOf(components, b._id)) {
          const cp = coupling(c);
          H.push(`<div class="component"><h4>${esc(stripTags(c.displayTitle) || '(' + c._component + ')')} <span class="meta">component · ${esc(c._id)} · ${esc(c._component)} · layout=${esc(c._layout || '')} · classes="${esc(c._classes || '')}"</span></h4>`);
          if (cp) H.push(`<p class="slot">⟦ CXP slot: page=${esc(cp.page)} slot=${esc(cp.slot)}${cp.part ? ' part=' + esc(cp.part) : ''} — subject-filled at merge ⟧</p>`);
          if (c.instruction) H.push(`<p><em>${esc(stripTags(c.instruction))}</em></p>`);
          for (const ch of extract(c)) {
            if (ch.kind === 'feedback') H.push(`<p class="fb">${esc(ch.label)}: ${esc(stripTags(ch.text))}</p>`);
            else if (ch.label) H.push(`<p><strong>${esc(ch.label)}:</strong> ${esc(stripTags(ch.text))}</p>`);
            else H.push(`<div class="body">${ch.text}</div>`);
          }
          H.push('</div>');
        }
        H.push('</div>');
      }
      H.push('</div>');
    }
    H.push('</section>');
  }
  H.push('</body></html>');
  return H.join('\n');
}

// =====================================================================
// 3. STRUCTURAL HTML — clean presentational DOM only
// =====================================================================
function structuralHtml() {
  const H = [];
  H.push('<!doctype html><html><head><meta charset="utf-8"><title>' + esc(shortSlug) + '</title></head><body>');
  for (const page of pages) {
    H.push(`<section class="page" data-id="${esc(page._id)}"><h1 class="page__title">${esc(stripTags(page.displayTitle || page.title))}</h1>`);
    for (const a of childrenOf(articles, page._id)) {
      H.push(`<article class="article ${esc(a._classes || '')}">${a.displayTitle ? `<h2 class="article__title">${esc(stripTags(a.displayTitle))}</h2>` : ''}`);
      for (const b of childrenOf(blocks, a._id)) {
        H.push('<div class="block">');
        for (const c of childrenOf(components, b._id)) {
          H.push(`<div class="component ${esc(c._component)}__container ${esc(c._classes || '')}">`);
          if (c.displayTitle) H.push(`<div class="component__title"><h3>${esc(stripTags(c.displayTitle))}</h3></div>`);
          if (c.instruction) H.push(`<div class="component__instruction">${esc(stripTags(c.instruction))}</div>`);
          if (c.body) H.push(`<div class="component__body">${c.body}</div>`);
          const items = extract(c).filter(x => x.kind !== 'body' && x.kind !== 'feedback');
          if (items.length) { H.push('<ul class="component__items">'); items.forEach(x => H.push(`<li>${x.label ? '<b>' + esc(x.label) + ':</b> ' : ''}${esc(stripTags(x.text))}</li>`)); H.push('</ul>'); }
          H.push('</div>');
        }
        H.push('</div>');
      }
      H.push('</article>');
    }
    H.push('</section>');
  }
  H.push('</body></html>');
  return H.join('\n');
}

// =====================================================================
// 4. YAML — structured data twin
// =====================================================================
function yamlStr(s) { return '"' + String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n') + '"'; }
function yaml() {
  const Y = [];
  Y.push(`course: ${yamlStr(courseObj.displayTitle || courseObj.title || slug)}`);
  Y.push(`shortSlug: ${yamlStr(shortSlug)}`);
  Y.push('pages:');
  for (const page of pages) {
    Y.push(`  - id: ${yamlStr(page._id)}`);
    Y.push(`    title: ${yamlStr(stripTags(page.displayTitle || page.title))}`);
    Y.push('    articles:');
    for (const a of childrenOf(articles, page._id)) {
      Y.push(`      - id: ${yamlStr(a._id)}`);
      Y.push(`        title: ${yamlStr(stripTags(a.displayTitle || ''))}`);
      Y.push(`        classes: ${yamlStr(a._classes || '')}`);
      Y.push('        components:');
      for (const b of childrenOf(blocks, a._id)) {
        for (const c of childrenOf(components, b._id)) {
          Y.push(`          - id: ${yamlStr(c._id)}`);
          Y.push(`            component: ${yamlStr(c._component)}`);
          Y.push(`            classes: ${yamlStr(c._classes || '')}`);
          if (c.displayTitle) Y.push(`            displayTitle: ${yamlStr(stripTags(c.displayTitle))}`);
          const chunks = extract(c);
          if (chunks.length) {
            Y.push('            content:');
            chunks.forEach(ch => Y.push(`              - { kind: ${ch.kind}, label: ${yamlStr(ch.label || '')}, text: ${yamlStr(stripTags(ch.text))} }`));
          }
        }
      }
    }
  }
  return Y.join('\n') + '\n';
}

// =====================================================================
// 5. COURSE-PACK (.md) — gated decisions, not content
// =====================================================================
function lastRecord(gateId) {
  if (!manifest) return null;
  const g = (manifest.gates || []).find(x => x.gateId === gateId);
  if (!g || !g.records || !g.records.length) return null;
  return g.records.reduce((a, b) => (b.seq > a.seq ? b : a));
}
function coursePackMd() {
  if (!manifest) return '# Course pack\n\n_(no manifest supplied — run with --manifest to include gated decisions)_\n';
  const L = [];
  L.push(`# ${courseObj.displayTitle || courseObj.title || slug} — course-pack spec`);
  L.push(`\n_Gated design decisions (not content). Generated ${new Date().toISOString()}._\n`);
  const gateBlock = (gateId, heading) => {
    const r = lastRecord(gateId);
    if (!r) return;
    L.push(`\n## ${heading}  <!-- ${gateId} seq ${r.seq} ${r.state}/${r.provenance || ''} -->`);
    L.push('\n```json\n' + JSON.stringify(r.decidedValue, null, 2) + '\n```');
  };
  gateBlock('wra-01_wrapper-open', 'W-OPEN — course opening (decisions)');
  ['onb-02_course-theme', 'onb-03_pitch', 'onb-04_naming', 'crs-02_thematic-scope', 'crs-03_course-outcomes'].forEach(g => gateBlock(g, g));
  // per-lesson gated decisions
  const lm = lastRecord('crs-04_lesson-map');
  if (lm && lm.decidedValue && lm.decidedValue.lessons) {
    for (const lesson of lm.decidedValue.lessons) {
      L.push(`\n## Lesson ${lesson.key} — ${lesson.title}  <!-- conceptTitle: ${lesson.conceptTitle || ''} -->`);
      L.push('\n```json\n' + JSON.stringify(lesson, null, 2) + '\n```');
      const les = lastRecord(`${manifest.slug}-${lesson.key}-les-01`);
      if (les) { L.push(`\n**les-01 (${lesson.key}) decisions:**`); L.push('\n```json\n' + JSON.stringify(les.decidedValue, null, 2) + '\n```'); }
    }
  }
  gateBlock('wra-03_summative', 'SUMM — summative (decisions)');
  gateBlock('wra-04_confidence', 'C-PRE / C-POST — confidence (decisions)');
  gateBlock('wra-02_wrapper-close', 'W-CLOSE — course close (decisions)');
  return L.join('\n') + '\n';
}

// =====================================================================
// 6. Annotated lesson template (first lesson) — ids + coupling + metadata
// =====================================================================
function lessonTemplate() {
  const lp = pages.find(p => /(^|[^A-Za-z])L0?1\b/.test(p._id) || p._id.startsWith('L01'));
  if (!lp) return '<!-- no lesson page found -->';
  const H = ['<!doctype html><html><head><meta charset="utf-8"><title>lesson template</title></head><body>',
    `<!-- Annotated template of lesson page ${lp._id} as produced. Shows ids, section classes, CXP slot markers and skeleton keys for agent authoring. -->`];
  H.push(`<section class="page" data-id="${esc(lp._id)}"><!-- page title: ${esc(stripTags(lp.displayTitle))} -->`);
  for (const a of childrenOf(articles, lp._id)) {
    H.push(`  <article class="article ${esc(a._classes || '')}" data-id="${esc(a._id)}"><!-- section: ${esc(stripTags(a.displayTitle))} -->`);
    for (const b of childrenOf(blocks, a._id)) {
      H.push(`    <div class="block" data-id="${esc(b._id)}" data-skeleton="${esc(b._skeletonKey || '')}">`);
      for (const c of childrenOf(components, b._id)) {
        const cp = coupling(c);
        H.push(`      <div class="component ${esc(c._component)}__container ${esc(c._classes || '')}" data-id="${esc(c._id)}" data-component="${esc(c._component)}">` +
          (cp ? ` {{! CXP slot ${esc(cp.page)}/${esc(cp.slot)}${cp.part ? '/' + esc(cp.part) : ''} — subject-filled at merge }}` : ''));
        H.push(`        {{! ${esc(c._component)} — ${esc(stripTags(c.displayTitle) || '(no title)')} }}`);
        H.push('      </div>');
      }
      H.push('    </div>');
    }
    H.push('  </article>');
  }
  H.push('</section>', '</body></html>');
  return H.join('\n');
}

// =====================================================================
// 7. EDIT (.md) — faithful, field-anchored round-trip source
// =====================================================================
// Each editable field is a fenced block tagged `<!-- edit:<id>:<path> -->` with
// the value VERBATIM (HTML, tokens, classes preserved). course-script-import.js
// reads these back into the base course JSON. v1 covers the flat prose fields
// (body, displayTitle, instruction) and the feedback/modal strings; item/option
// arrays are read-only for now.
function editMd() {
  const L = [];
  L.push(`<!-- course-export edit source for ${shortSlug}. Edit the content inside each fenced block; keep the <!-- edit:ID:PATH --> markers and fences intact. Re-import with: node tools/course-script-import.js --edit <this file> --course <base-content-dir> -->`);
  const fld = (id, pathStr, val) => {
    L.push(`\n<!-- edit:${id}:${pathStr} -->`);
    L.push('```html');
    L.push(val == null ? '' : String(val));
    L.push('```');
  };
  for (const page of pages) {
    L.push(`\n\n<!-- ===== page ${page._id}: ${stripTags(page.displayTitle || page.title)} ===== -->`);
    for (const a of childrenOf(articles, page._id))
      for (const b of childrenOf(blocks, a._id))
        for (const c of childrenOf(components, b._id)) {
          L.push(`\n<!-- component ${c._id} (${c._component}) -->`);
          fld(c._id, 'displayTitle', c.displayTitle);
          fld(c._id, 'body', c.body);
          if (c.instruction != null) fld(c._id, 'instruction', c.instruction);
          const fb = c._feedback;
          if (fb) {
            if (fb.correct != null) fld(c._id, 'feedback.correct', fb.correct);
            if (fb._incorrect && fb._incorrect.notFinal != null) fld(c._id, 'feedback.incorrect.notFinal', fb._incorrect.notFinal);
            if (fb._incorrect && fb._incorrect.final != null) fld(c._id, 'feedback.incorrect.final', fb._incorrect.final);
            if (fb._partlyCorrect && fb._partlyCorrect.notFinal != null) fld(c._id, 'feedback.partlyCorrect.notFinal', fb._partlyCorrect.notFinal);
            if (fb._partlyCorrect && fb._partlyCorrect.final != null) fld(c._id, 'feedback.partlyCorrect.final', fb._partlyCorrect.final);
          }
        }
  }
  return L.join('\n') + '\n';
}

// ---- write bundle ----
const stamp = new Date().toISOString().replace(/[:]/g, '').replace(/\.\d+Z$/, 'Z');
const folderName = `${shortSlug}${label ? '-' + label : ''}_${stamp}`;
const root = path.join(outRoot, folderName);
for (const d of ['html', 'templates', 'md', 'yaml', 'json', 'json/packs']) fs.mkdirSync(path.join(root, d), { recursive: true });
const w = (rel, content) => { fs.writeFileSync(path.join(root, rel), content); return rel; };
const written = [];
written.push(w(`html/${shortSlug}.full.html`, fullHtml()));
written.push(w(`html/${shortSlug}.structural.html`, structuralHtml()));
written.push(w(`templates/lesson.annotated.html`, lessonTemplate()));
written.push(w(`md/${shortSlug}.script.md`, scriptMd()));
written.push(w(`md/${shortSlug}.course-pack.md`, coursePackMd()));
written.push(w(`md/${shortSlug}.edit.md`, editMd()));
written.push(w(`yaml/${shortSlug}.yaml`, yaml()));
// real component templates — modern Adapt (>=5.19) renders components with
// React JSX templates (templates/*.jsx); core/menu may still carry .hbs. We copy
// whatever is present. Contrib templates arrive via `adapt install`; this
// checkout holds the committed custom (adapt-abbott-*) ones.
fs.mkdirSync(path.join(root, 'templates/src'), { recursive: true });
let hbsN = 0;
for (const base of ['src/components', 'src/extensions', 'src/menu', 'src/theme']) {
  if (!fs.existsSync(base)) continue;
  for (const plugin of fs.readdirSync(base)) {
    const tdir = path.join(base, plugin, 'templates');
    if (!fs.existsSync(tdir)) continue;
    for (const f of fs.readdirSync(tdir)) if (/\.(jsx|hbs)$/.test(f)) { fs.copyFileSync(path.join(tdir, f), path.join(root, 'templates/src', `${plugin}__${f}`)); hbsN++; }
  }
}
if (!hbsN) fs.writeFileSync(path.join(root, 'templates/src', 'README.txt'), 'No component templates present in this checkout. Contrib templates (.jsx) are fetched by `adapt install`; run this export on the build machine (or after npm run adapt-install) to capture them.\n');
if (manifest) written.push(w(`json/course-design.json`, JSON.stringify(manifest, null, 2)));
if (packsDir && fs.existsSync(packsDir)) {
  for (const f of fs.readdirSync(packsDir).filter(f => f.endsWith('.json'))) { fs.copyFileSync(path.join(packsDir, f), path.join(root, 'json/packs', f)); written.push(`json/packs/${f}`); }
}
console.log(`Course export bundle: ${root}`);
written.forEach(f => console.log('  ' + f));
console.log(`  templates/src/ (${hbsN} real component template(s) captured${hbsN ? '' : ' — none in this checkout; run after adapt install'})`);
console.log(`\nPages: ${pages.length} | articles: ${articles.length} | blocks: ${blocks.length} | components: ${components.length}`);
