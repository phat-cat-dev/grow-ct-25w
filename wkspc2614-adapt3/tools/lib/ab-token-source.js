'use strict';
/**
 * ab-token-source.js
 *
 * Shared LESS-source loading for the ab-token-* build scripts. Extracted
 * from build-ab-token-values.js so the parsing logic exists in exactly one
 * place - the two bugs fixed in that script's history (the property regex
 * matching too much, and the uuid-file header line-offset being wrong after
 * a header rewrite) both came from copies of this logic drifting apart
 * across scripts. Any future ab-token-*.less generator should read its
 * source rows via loadTokenSource() rather than re-parsing the LESS files
 * itself.
 *
 * Reads (never writes):
 *   adapt-core-vanilla-interface.less             - plain, untokenised
 *     structure + values
 *   adapt-core-vanilla-interface-uuid.tokens.less - which declarations are
 *     tokenised, their registry group/layer/number, in document order
 *   ab-token-base.less                            - registry -> --ab-
 *     <semantic> names
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const DIR = path.join(ROOT, 'undlaf-intro_261012-235924', 'adapt-less-compiles');
const SRC_PLAIN = path.join(DIR, 'adapt-core-vanilla-interface.less');
const SRC_UUID_TOKENS = path.join(DIR, 'adapt-core-vanilla-interface-uuid.tokens.less');
const SRC_AB_BASE = path.join(DIR, 'ab-token-base.less');

// 11-category functional taxonomy. Needed to recompute each token's group
// so it can be looked up in ab-token-base.less (whose LHS is
// --ab-<group>-<c|t>-<nnnn>), and reused by any generator that wants to
// sub-order rows by function (e.g. inside a utility section).
const CAT = {
  typography: `font font-display font-family font-size font-style font-variant font-weight
    line-height letter-spacing text-align text-decoration text-indent text-overflow
    text-transform white-space direction vertical-align speak src
    -moz-osx-font-smoothing -webkit-font-smoothing -webkit-text-size-adjust`,
  colour: `color background-color border-color border-bottom-color border-top-color`,
  background: `background background-position background-repeat background-size`,
  border: `border border-bottom border-right border-radius -webkit-border-radius
    -moz-border-radius border-style border-width outline outline-offset`,
  spacing: `margin margin-bottom margin-inline-end margin-inline-start margin-left
    margin-right margin-top padding padding-bottom padding-inline padding-inline-end
    padding-inline-start padding-left padding-right padding-top column-gap row-gap`,
  sizing: `width height max-width max-height min-width min-height
    --adapt-navigation-height --adapt-viewport-height`,
  layout: `display position top right bottom left float clear overflow overflow-x
    overflow-y box-sizing align-items justify-content flex-direction flex-grow
    flex-wrap order z-index scroll-padding-bottom scroll-padding-top`,
  motion: `animation transition transition-delay transform transform-origin`,
  effect: `box-shadow filter opacity visibility zoom clip`,
  interaction: `cursor pointer-events user-select -webkit-user-select -moz-user-select
    -ms-user-select -khtml-user-select -webkit-touch-callout -webkit-overflow-scrolling
    -webkit-appearance`,
  content: `content`,
};
const GROUP_LOOKUP = {};
for (const [cat, props] of Object.entries(CAT)) {
  for (const p of props.split(/\s+/).filter(Boolean)) GROUP_LOOKUP[p] = cat;
}
function groupOf(prop) {
  if (GROUP_LOOKUP[prop]) return GROUP_LOOKUP[prop];
  if (prop.startsWith('--adapt-cubic-bezier-')) return 'motion';
  if (prop.startsWith('--adapt-tooltip-')) return 'layout';
  return 'other';
}

// 11-group display order, largest to smallest, per the taxonomy table.
const GROUP_ORDER = ['layout', 'colour', 'typography', 'content', 'spacing',
  'sizing', 'motion', 'effect', 'border', 'background', 'interaction'];

const LAYER_WORD = { c: 'core', t: 'theme' };

function stripLineComments(line, state) {
  let out = '';
  let i = 0;
  if (state.inBlock) {
    const j = line.indexOf('*/');
    if (j === -1) return '';
    i = j + 2;
    state.inBlock = false;
  }
  let q = null;
  while (i < line.length) {
    const c = line[i];
    if (q) { out += c; if (c === q && line[i - 1] !== '\\') q = null; i++; continue; }
    if (c === '"' || c === "'") { q = c; out += c; i++; continue; }
    if (line.startsWith('//', i)) break;
    if (line.startsWith('/*', i)) {
      const j = line.indexOf('*/', i + 2);
      if (j === -1) { state.inBlock = true; break; }
      i = j + 2; continue;
    }
    out += c; i++;
  }
  return out;
}

function* splitStatements(rest) {
  let i = 0, depth = 0, start = 0, q = null;
  while (i < rest.length) {
    const c = rest[i];
    if (q) { if (c === q) q = null; i++; continue; }
    if (c === '"' || c === "'") { q = c; i++; continue; }
    if (c === '(') depth++;
    else if (c === ')') depth = Math.max(0, depth - 1);
    else if (c === '{' || c === '}' || (c === ';' && depth === 0)) {
      yield { head: rest.slice(start, i), ch: c };
      start = i + 1;
    }
    i++;
  }
  yield { head: rest.slice(start), ch: null };
}

/**
 * rules: Map<key, {chain: string[], decls: string[]}>
 * declsByLine: Map<lineNo, Array<{prop, key, value}>>
 */
function parsePlain(text) {
  const lines = text.split('\n');
  const rules = new Map();
  const declsByLine = new Map();
  const stack = [];
  const cur = [];
  let key = 0;
  const state = { inBlock: false };
  let pending = '';
  for (let n = 1; n <= lines.length; n++) {
    const raw = lines[n - 1];
    const stripped = stripLineComments(raw, state);
    let rest = pending + stripped;
    pending = '';
    for (const { head, ch } of splitStatements(rest)) {
      if (ch === '{') {
        const sel = head.trim().replace(/\s+/g, ' ');
        stack.push(sel);
        key++;
        cur.push(key);
        rules.set(key, { chain: stack.slice(), decls: [] });
      } else if (ch === '}') {
        stack.pop();
        cur.pop();
      } else if (ch === ';') {
        const d = head.trim().replace(/\s+/g, ' ');
        if (d && cur.length) {
          const k = cur[cur.length - 1];
          rules.get(k).decls.push(d);
          const m = d.match(/^(-{0,2}[a-zA-Z][a-zA-Z-]*)\s*:\s*(.*)$/);
          if (m) {
            if (!declsByLine.has(n)) declsByLine.set(n, []);
            declsByLine.get(n).push({ prop: m[1], key: k, value: m[2] });
          }
        }
      } else {
        if (head.trim()) pending = head;
      }
    }
  }
  return { rules, declsByLine };
}

function parseExistingTokens(text) {
  const lines = text.split('\n');
  const toks = [];
  const re = /([-a-zA-Z]+)\s*:\s*--ad-([a-z]+)-([ct])-(\d{4})/g;
  for (let n = 1; n <= lines.length; n++) {
    let m;
    re.lastIndex = 0;
    while ((m = re.exec(lines[n - 1]))) {
      toks.push({ line: n, prop: m[1], group: m[2], layer: m[3], num: m[4] });
    }
  }
  return toks;
}

function alignTokens(toks, declsByLine) {
  const used = new Set();
  const aligned = [];
  let miss = 0;
  for (const t of toks) {
    let hit = null;
    for (let nn = t.line; nn < t.line + 8 && hit === null; nn++) {
      const arr = declsByLine.get(nn);
      if (!arr) continue;
      for (let i = 0; i < arr.length; i++) {
        const uid = `${nn}:${i}`;
        if (used.has(uid)) continue;
        if (arr[i].prop.replace(/^-+/, '') === t.prop.replace(/^-+/, '')) {
          hit = { key: arr[i].key, value: arr[i].value };
          used.add(uid);
          break;
        }
      }
    }
    if (hit === null) miss++;
    aligned.push({ ...t, key: hit && hit.key, value: hit && hit.value });
  }
  return { aligned, miss };
}

/**
 * Loads and aligns the three source LESS files into one row list.
 *
 * Returns { rows, rules, reorderedGroups }:
 *   - rows: [{ sem, a }] in document order, EXCEPT that within any group of
 *     rows sharing the same `sem` (semantic name), core-layer entries are
 *     placed before theme-layer entries (matching Adapt's real build order,
 *     where all of core compiles before any theme) - every other row's
 *     position is untouched. `a` is { line, prop, group, layer, num, key,
 *     value }; `a.key` indexes into `rules`.
 *   - rules: Map<key, {chain: string[], decls: string[]}>, the full parsed
 *     rule tree from adapt-core-vanilla-interface.less.
 *   - reorderedGroups: count of same-name groups that were out of
 *     core-before-theme order and got fixed (diagnostic only).
 *
 * Exits the process with a FATAL message on any alignment/lookup failure,
 * matching this project's "fail loud, don't silently drop rows" convention.
 */
function loadTokenSource() {
  const plainText = fs.readFileSync(SRC_PLAIN, 'utf8');
  const uuidText = fs.readFileSync(SRC_UUID_TOKENS, 'utf8');
  const abBaseText = fs.readFileSync(SRC_AB_BASE, 'utf8');

  const { rules, declsByLine } = parsePlain(plainText);
  const toks = parseExistingTokens(uuidText);

  // The uuid tokens file's header was rewritten by build-abbott-token-layers.js
  // and is no longer the same number of lines as the plain file's original
  // header, so absolute line numbers between the two files differ by a
  // constant offset for the rest of the document. Measure it from a shared
  // marker and correct for it before aligning.
  const MARKER = 'SECTION A - CORE FOUNDATION';
  const plainMarkerLine = plainText.split('\n').findIndex(l => l.includes(MARKER)) + 1;
  const uuidMarkerLine = uuidText.split('\n').findIndex(l => l.includes(MARKER)) + 1;
  if (plainMarkerLine === 0 || uuidMarkerLine === 0) {
    console.error('FATAL: could not find shared marker to compute header-line offset.');
    process.exit(1);
  }
  const offset = uuidMarkerLine - plainMarkerLine;
  for (const t of toks) t.line -= offset;

  const { aligned, miss } = alignTokens(toks, declsByLine);
  if (miss > 0) {
    console.error(`FATAL: ${miss} tokens could not be aligned to a declaration in ${path.basename(SRC_PLAIN)}.`);
    process.exit(1);
  }

  // registry key -> bare --ab-<semantic> name
  const semMap = new Map();
  const rowRe = /--ab-([a-z]+)-([ct])-(\d{4}):\s*var\((--ab-[a-zA-Z0-9-]+)\)/g;
  let rm;
  while ((rm = rowRe.exec(abBaseText))) {
    semMap.set(`${rm[1]}-${rm[2]}-${rm[3]}`, rm[4]);
  }

  let groupMisses = 0;
  const rows = [];
  for (const a of aligned) {
    const key = `${a.group}-${a.layer}-${a.num}`;
    const sem = semMap.get(key);
    if (!sem) { groupMisses++; continue; }
    rows.push({ sem, a });
  }
  if (groupMisses > 0) {
    console.error(`FATAL: ${groupMisses} tokens had no matching row in ab-token-base.less.`);
    process.exit(1);
  }

  // This comparison document interleaves theme-only and core-only sections,
  // so document order alone does not guarantee core-before-theme for a given
  // semantic name (unlike Adapt's real build, which always compiles all of
  // core before any theme). Array.prototype.sort cannot be trusted to fix
  // this on its own: a 0-returning comparator never forces two far-apart
  // elements to be compared (TimSort only merges adjacent runs), so a
  // same-name pair sitting hundreds of rows apart can survive a sort
  // untouched. Instead, group by semantic name, collect the exact index
  // positions each group occupies in the row list, and reassign only those
  // positions - core-layer entries first, then theme, otherwise preserving
  // each entry's relative order - so every other row's position is
  // completely untouched and every pair spanning any distance is fixed.
  const groups = new Map();
  rows.forEach((r, idx) => {
    if (!groups.has(r.sem)) groups.set(r.sem, []);
    groups.get(r.sem).push(idx);
  });
  let reorderedGroups = 0;
  for (const idxs of groups.values()) {
    if (idxs.length < 2) continue;
    const entries = idxs.map(i => rows[i]);
    const reordered = entries
      .map((r, i) => ({ r, i }))
      .sort((x, y) => {
        const xc = x.r.a.layer === 'c' ? 0 : 1;
        const yc = y.r.a.layer === 'c' ? 0 : 1;
        if (xc !== yc) return xc - yc;
        return x.i - y.i; // stable: preserve original relative order within same layer
      })
      .map(({ r }) => r);
    if (reordered.some((r, i) => r !== entries[i])) reorderedGroups++;
    idxs.forEach((pos, i) => { rows[pos] = reordered[i]; });
  }

  return { rows, rules, reorderedGroups };
}

module.exports = {
  DIR,
  CAT,
  GROUP_ORDER,
  LAYER_WORD,
  groupOf,
  loadTokenSource,
};
