'use strict';
/**
 * script-sync.js — shared model for round-tripping an edited `.script.md`
 * "screenplay" export back into a course's source JSON.
 *
 * `course-export.js`'s scriptMd() prints one chunk per line/paragraph, each
 * component anchored by a heading comment `<!-- ID COMPONENT -->`. This module
 * re-derives that exact chunk shape from live JSON (extract()/coupling(), kept
 * byte-for-byte identical to course-export.js's own copies so chunk identity
 * matches) and parses the same markdown shape back out of an edited file, so
 * the two can be diffed chunk-by-chunk.
 *
 * Deliberately duplicated rather than required from course-export.js: that
 * file executes immediately against process.argv when loaded and is not
 * require()-safe. Keeping these pure functions here avoids touching a working
 * CLI tool to make this one possible.
 */
const fs = require('fs');
const path = require('path');

const rd = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const stripTags = s => String(s == null ? '' : s).replace(/<[^>]+>/g, '').trim();
const prose = s => String(s == null ? '' : s)
  .replace(/<li[^>]*>/gi, '\n- ')
  .replace(/<\/(p|li|h[1-6]|div|ul|ol)>/gi, '\n\n')
  .replace(/<br\s*\/?>/gi, '\n')
  .replace(/<[^>]+>/g, '')
  .replace(/\n{3,}/g, '\n\n')
  .replace(/[ \t]+\n/g, '\n')
  .trim();

function loadCourseTree(courseDir) {
  const en = f => rd(path.join(courseDir, 'en', f));
  const contentObjects = en('contentObjects.json');
  const articles = en('articles.json');
  const blocks = en('blocks.json');
  const components = en('components.json');
  const childrenOf = (arr, pid) => arr.filter(x => x._parentId === pid);
  const pages = contentObjects.filter(o => o._type === 'page');
  return { contentObjects, articles, blocks, components, childrenOf, pages };
}

// extract(): identical logic/order to course-export.js's extract(), so chunk
// identity (kind + label + order) matches what scriptMd() printed.
function extract(c) {
  const out = [];
  const push = (kind, label, text) => { if (text != null && String(text).length) out.push({ kind, label, text: String(text) }); };
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

function coupling(c) {
  const m = String(c._classes || '').match(/slot__([A-Za-z0-9-]+)__([A-Za-z0-9-]+)(?:__([A-Za-z0-9-]+))?/);
  return m ? { page: m[1], slot: m[2], part: m[3] || null } : null;
}

// ---------------------------------------------------------------------------
// parseScriptMd: inverse of scriptMd()'s per-component rendering.
// Returns [{ id, component, head, instruction, chunks: [{kind,label,text}] }]
// ---------------------------------------------------------------------------
function parseScriptMd(text) {
  const headingRe = /^#### (.*?)  <!-- (\S+) (\S+) -->$/;
  // scriptMd() also interleaves page (##) and article (###) heading lines
  // between component sections; these carry no chunk data and must be
  // dropped, not swept into the preceding component's raw lines (where
  // they'd otherwise show up as a bogus extra unlabelled body block).
  const skipRe = /^(## .*<!-- page \S+ -->|### .*<!-- article \S+ -->)$/;
  const lines = text.split('\n');
  const sections = [];
  let cur = null;
  for (const line of lines) {
    const m = headingRe.exec(line);
    if (m) {
      cur = { head: m[1], id: m[2], component: m[3], raw: [] };
      sections.push(cur);
      continue;
    }
    if (skipRe.test(line)) continue;
    if (cur) cur.raw.push(line);
  }
  for (const sec of sections) {
    // join raw lines back, then split into blank-line-delimited blocks
    const body = sec.raw.join('\n');
    const blocks = body.split(/\n{2,}/).map(b => b.trim()).filter(Boolean);
    const chunks = [];
    let instruction = null;
    let sawNonBody = false; // once true, a later unlabelled block is NOT the top-level body
    let pendingItemTitle = null; // for accordion/hotgraphic: item-title chunk awaiting its item-body
    for (const block of blocks) {
      if (/^_⟦ CXP slot/.test(block)) continue; // informational marker, not data
      let mm;
      if (!instruction && !chunks.length && /^_(.*)_$/.test(block) && !/^\*\*/.test(block)) {
        instruction = block.replace(/^_(.*)_$/, '$1');
        continue;
      }
      if ((mm = /^> \*\*(.+?):\*\*\s*([\s\S]*)$/.exec(block))) {
        chunks.push({ kind: 'feedback', label: mm[1], text: mm[2].trim() });
        sawNonBody = true;
        pendingItemTitle = null;
        continue;
      }
      if ((mm = /^- \*\*(.+?):\*\*\s*([\s\S]*)$/.exec(block))) {
        const label = mm[1];
        const itemTitleMatch = /^Item (\d+)$/.exec(label);
        chunks.push({ kind: itemTitleMatch ? 'item-title' : 'labelled', label, text: mm[2].trim() });
        sawNonBody = true;
        pendingItemTitle = itemTitleMatch ? Number(itemTitleMatch[1]) : null;
        continue;
      }
      // unlabelled prose block
      if (!sawNonBody) {
        chunks.push({ kind: 'body', label: null, text: block });
      } else if (pendingItemTitle != null) {
        chunks.push({ kind: 'item-body', label: null, text: block, forItem: pendingItemTitle });
        pendingItemTitle = null;
      } else {
        chunks.push({ kind: 'body-unplaced', label: null, text: block });
      }
    }
    sec.instruction = instruction;
    sec.chunks = chunks;
    delete sec.raw;
  }
  return sections;
}

// ---------------------------------------------------------------------------
// HTML fidelity guard + reconstruction, for writing an edited plain-text
// body/item-body chunk back into a BASE component's HTML field.
//
// script.md's prose() is lossy: it keeps paragraph/list/line breaks but
// strips every tag, including inline ones (<strong>, <em>, <a>...). A body
// field built from only <p>, <ul>, <li>, <br> survives that round trip
// losslessly (those are exactly the tags prose() turns into plain-text
// breaks); anything else does not. isSimpleHtml() checks a field is in that
// safe set before htmlFromPlain() is trusted to rebuild it; callers must
// refuse the write (report it as a manual edit) when it returns false.
// ---------------------------------------------------------------------------
function isSimpleHtml(html) {
  const stripped = String(html == null ? '' : html).replace(/<\/?(p|ul|ol|li|br)\s*\/?>/gi, '');
  return !/</.test(stripped);
}

// Inverse of prose(): rebuilds <p>/<ul><li> HTML from the plain text a
// script.md body block round-trips to. Paragraphs are blank-line separated;
// a paragraph whose every line starts with "- " becomes a <ul>; any other
// paragraph becomes a <p>, with internal single line breaks as <br>.
function htmlFromPlain(text) {
  const paragraphs = String(text == null ? '' : text).split(/\n{2,}/).map(p => p.trim()).filter(Boolean);
  return paragraphs.map(p => {
    const lines = p.split('\n').map(l => l.trim()).filter(Boolean);
    const isList = lines.length > 0 && lines.every(l => l.startsWith('- '));
    if (isList) return '<ul>' + lines.map(l => `<li>${l.slice(2)}</li>`).join('') + '</ul>';
    return `<p>${lines.join('<br>')}</p>`;
  }).join('');
}

module.exports = { loadCourseTree, extract, coupling, stripTags, prose, parseScriptMd, isSimpleHtml, htmlFromPlain };
