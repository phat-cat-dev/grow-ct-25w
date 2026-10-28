#!/usr/bin/env node
/**
 * build-abbott-token-layers.js
 *
 * Sandbox discovery pass: tokenise EVERY literal value Adapt core+vanilla LESS
 * bakes in, as a non-semantic registry, then an Abbott-namespaced mirror, then
 * a first-pass semantic rename. Independent of, and not cross-referenced
 * against, the real documented L1-L6 --ab-base-* architecture
 * (docs/authoring/theming-layers-map.md) - this is raw-material discovery for
 * that later curated adapter, not the adapter itself.
 *
 * Reads (never writes):
 *   undlaf-intro_261012-235924/adapt-less-compiles/adapt-core-vs-vanilla-combined.less
 *     - untokenised, structural source of truth (selectors, nesting, @media,
 *       guards, comma groups, LESS `&`)
 *   undlaf-intro_261012-235924/adapt-less-compiles/adapt-core-vs-vanilla-combined.tokens.less
 *     - the CURRENT tokenised file; read only to learn which declarations are
 *       already tokenised, and their existing layer + registry number. This
 *       script renames tokens, it does not mint new ones.
 *
 * Writes:
 *   adapt-core-vs-vanilla-combined.tokens.less   (Layer 1, overwritten in place)
 *   adapt-abbott-interface-token.less            (Layer 2, overwritten)
 *   ab-token-base.less                           (Layer 3, created/overwritten)
 *
 * Usage: node tools/build-abbott-token-layers.js
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DIR = path.join(ROOT, 'undlaf-intro_261012-235924', 'adapt-less-compiles');
const SRC_PLAIN = path.join(DIR, 'adapt-core-vs-vanilla-combined.less');
const SRC_TOK = path.join(DIR, 'adapt-core-vs-vanilla-combined.tokens.less');
const OUT_L1 = SRC_TOK;
const OUT_L2 = path.join(DIR, 'adapt-abbott-interface-token.less');
const OUT_L3 = path.join(DIR, 'ab-token-base.less');

// ===================================================================
// Taxonomy - verified to cover all 2083 current tokens, zero unmapped
// ===================================================================
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

// ===================================================================
// LESS parser: quote-aware comment stripper + quote/paren-aware splitter
// ===================================================================
function stripLineComments(line, state) {
  // state.inBlock carries an unterminated /* ... */ across lines
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
    if (q) {
      out += c;
      if (c === q && line[i - 1] !== '\\') q = null;
      i++; continue;
    }
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

// Yields {head, ch} for each {, }, or top-level ; in rest. ch is null for a
// trailing fragment with no terminator yet (carried to the next line).
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
 * Parse the untokenised plain .less into:
 *   rules: Map<key, {chain: string[], decls: string[]}>
 *   declsByLine: Map<lineNo, Array<{prop, key}>>  (document order preserved per line)
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
          const m = d.match(/^(-{0,2}[a-zA-Z][a-zA-Z-]*)\s*:/);
          if (m) {
            if (!declsByLine.has(n)) declsByLine.set(n, []);
            declsByLine.get(n).push({ prop: m[1], key: k });
          }
        }
      } else {
        // trailing fragment, carry to next line only if non-empty
        if (head.trim()) pending = head;
      }
    }
  }
  return { rules, declsByLine };
}

// ===================================================================
// Extract existing tokens from the current tokenised file, in document order
// ===================================================================
function parseExistingTokens(text) {
  const lines = text.split('\n');
  const toks = []; // {line, prop, layer, num}
  const re = /([-a-zA-Z]+)\s*:\s*--ad-[a-z0-9-]+-(core|vanilla)-(\d{6})/g;
  for (let n = 1; n <= lines.length; n++) {
    let m;
    re.lastIndex = 0;
    while ((m = re.exec(lines[n - 1]))) {
      toks.push({ line: n, prop: m[1], layer: m[2] === 'core' ? 'c' : 't', num: parseInt(m[3], 10) });
    }
  }
  return toks;
}

// ===================================================================
// Align each existing token to its declaration/rule in the parsed plain file
// ===================================================================
function alignTokens(toks, declsByLine) {
  const used = new Set(); // `${line}:${idx}`
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
          hit = arr[i].key;
          used.add(uid);
          break;
        }
      }
    }
    if (hit === null) miss++;
    aligned.push({ ...t, key: hit });
  }
  return { aligned, miss };
}

// ===================================================================
// Layer 3 selector resolution -> semantic name
// ===================================================================
const MEDIA_MODIFIER = {
  '@media (min-width: @device-width-medium)': 'md',
  '@media (min-width: @device-width-small)': 'sm',
  '@media (min-width: @media-query)': 'mq',
  '@media (min-width: @slider-affix-breakpoint)': 'slider-affix',
  '@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none)': 'high-contrast',
  '@media (prefers-reduced-motion)': 'reduced-motion',
  '@media (min-width: @@breakpoint)': 'breakpoint',
};

function slug(s) {
  s = s.replace(/:not\([^)]*\)/g, '');
  s = s.replace(/@\{([a-zA-Z0-9-]+)\}/g, '$1');
  s = s.replace(/\[[^\]]*?["']([^"']+)["'][^\]]*\]/g, '-$1');
  s = s.replace(/\[[^\]]*\]/g, '');
  s = s.replace(/::/g, '-').replace(/:/g, '-');
  s = s.replace(/[^a-zA-Z0-9]+/g, '-').toLowerCase();
  return s.replace(/-+/g, '-').replace(/^-|-$/g, '');
}

function resolveChain(chain) {
  let sel = '';
  const mods = [];
  for (const item of chain) {
    if (item.startsWith('@media')) {
      mods.push(MEDIA_MODIFIER[item] || slug(item));
      continue;
    }
    if (item.startsWith('@font-face')) { sel = 'font-face'; continue; }
    if (item.startsWith('@keyframes')) {
      const rest = item.split(/\s+/).slice(1).join(' ');
      sel = 'kf-' + slug(rest || 'anon');
      continue;
    }
    const guard = item.match(/^&?\s*when\s*\((.+)\)$/);
    if (guard) {
      const cond = guard[1].trim();
      const eq = cond.match(/@?([a-zA-Z0-9-]+)\s*=\s*([a-zA-Z0-9-]+)/);
      mods.push(eq ? slug(eq[2]) : slug(cond));
      continue;
    }
    const first = item.split(',')[0].trim();
    if (first.includes('&')) {
      sel = sel ? first.replace(/&/g, sel) : first.replace(/&/g, '');
    } else {
      sel = sel ? (sel + ' ' + first).trim() : first;
    }
  }
  return { selSlug: slug(sel), mods };
}

function buildSemanticName(chain, prop) {
  const { selSlug, mods } = resolveChain(chain);
  const propSlug = prop.replace(/^-+/, '');
  const segs = selSlug ? selSlug.split('-').filter(Boolean) : [];
  let parts = [...segs, ...mods, propSlug];
  let name = '--ab-' + parts.join('-').replace(/-+/g, '-');
  const CAP = 72;
  if (name.length > CAP && segs.length > 5) {
    const kept = [...segs.slice(0, 2), ...segs.slice(-3)];
    parts = [...kept, ...mods, propSlug];
    name = '--ab-' + parts.join('-').replace(/-+/g, '-');
  }
  return name;
}

// ===================================================================
// Main
// ===================================================================
function main() {
  const plainText = fs.readFileSync(SRC_PLAIN, 'utf8');
  const tokText = fs.readFileSync(SRC_TOK, 'utf8');

  const { rules, declsByLine } = parsePlain(plainText);
  const toks = parseExistingTokens(tokText);
  const { aligned, miss } = alignTokens(toks, declsByLine);
  if (miss > 0) {
    console.error(`FATAL: ${miss} existing tokens could not be aligned to a declaration.`);
    process.exit(1);
  }

  // ---- Layer 1: rewrite tokens.less in place with new names ----
  // Replace each `--ad-<old>-<core|vanilla>-<nnnnnn>` occurrence, in document
  // order, with `--ad-<group>-<c|t>-<nnnn>`. Walk the file text with the same
  // regex used to extract, substituting the i-th match with the i-th aligned
  // entry (order is guaranteed identical: both are a single left-to-right scan).
  let idx = 0;
  const oldTokenRe = /--ad-[a-z0-9-]+-(core|vanilla)-(\d{6})/g;
  const newL1Body = tokText.replace(oldTokenRe, () => {
    const a = aligned[idx++];
    const g = groupOf(a.prop);
    return `--ad-${g}-${a.layer}-${String(a.num).padStart(4, '0')}`;
  });
  if (idx !== aligned.length) {
    console.error(`FATAL: Layer 1 substitution count mismatch: replaced ${idx}, expected ${aligned.length}.`);
    process.exit(1);
  }
  const l1Header = `/* =====================================================
   CORE vs VANILLA THEME - COMBINED COMPARISON VIEW
   =====================================================

   PURPOSE: pair up core/less and theme/adapt-contrib-vanilla/less files
   that share the same module name, so you can see exactly where the
   vanilla theme re-declares (and therefore overrides, via normal CSS
   cascade - same selector, later rule wins) a core module, versus where
   core has no theme equivalent at all and so runs completely unmodified.

   IMPORTANT - this is a COMPARISON AID, not the literal build order.
   The real Adapt build compiles ALL of src/core/less first (mandatory
   block), THEN ALL of src/theme/<theme>/less afterwards (src block).
   For the literal build-order output, read adapt-core-less-concat.less
   followed by adapt-vanilla-theme-less-concat.less.

   TOKENISED VARIANT (registry grammar): every declaration value below has
   been replaced with --ad-<group>-<c|t>-<nnnn>, a non-semantic registry
   token; <group> is one of 11 taxonomy groups (layout, colour, typography,
   content, spacing, sizing, motion, effect, border, background,
   interaction), <c|t> is core/theme, <nnnn> is the stable registry number
   (unique, monotonic in document order). The selector is deliberately NOT
   in the token name - see ab-token-base.less for the selector-derived
   semantic rename. Original value preserved in the trailing // comment.

   Sections: A core foundation (no theme equiv) | B core/theme pairs |
   C core-only modules | D theme-only new core/ files | E theme-only
   defaults | F theme-only plugin styling | G theme-only project layer
   ===================================================== */`;
  const oldHeaderRe = /\/\* =====================================================\n   CORE vs VANILLA THEME[\s\S]*?===================================================== \*\//;
  const l1Final = newL1Body.replace(oldHeaderRe, l1Header);

  // ---- Layer 2: interface :root mapping, --ad-X: var(--ab-X), no comments ----
  const l2Lines = [];
  l2Lines.push('/* =====================================================');
  l2Lines.push('   ADAPT <- ABBOTT INTERFACE');
  l2Lines.push('   =====================================================');
  l2Lines.push('');
  l2Lines.push('   Every --ad-<group>-<c|t>-<nnnn> registry token (Layer 1, consumed by the');
  l2Lines.push('   tokenised Adapt rules) takes its value FROM the equivalent --ab-<group>-');
  l2Lines.push('   <c|t>-<nnnn> Abbott registry token (Layer 3 names those). Adapt reads --ad-*,');
  l2Lines.push('   so this interface is live: whatever ab-token-base.less resolves --ab-* to');
  l2Lines.push('   is what Adapt\'s rules render.');
  l2Lines.push('   ===================================================== */');
  l2Lines.push('');
  l2Lines.push(':root {');
  const seenNums = new Set();
  for (const a of aligned) {
    const key = `${a.layer}-${a.num}`;
    if (seenNums.has(key)) continue; // a number appears once; guard just in case
    seenNums.add(key);
    const g = groupOf(a.prop);
    const n4 = String(a.num).padStart(4, '0');
    l2Lines.push(`  --ad-${g}-${a.layer}-${n4}: var(--ab-${g}-${a.layer}-${n4});`);
  }
  l2Lines.push('}');
  l2Lines.push('');
  const l2Final = l2Lines.join('\n');

  // ---- Layer 3: --ab-<group>-<c|t>-<nnnn> -> var(--ab-<semantic>), full ruleset comment ----
  const l3Lines = [];
  l3Lines.push('/* =====================================================');
  l3Lines.push('   AB TOKEN BASE - REGISTRY TO SEMANTIC RENAME (first pass)');
  l3Lines.push('   =====================================================');
  l3Lines.push('');
  l3Lines.push('   Sandbox discovery pass, independent of the documented L1-L6 --ab-base-*');
  l3Lines.push('   architecture (docs/authoring/theming-layers-map.md) - this is raw-material');
  l3Lines.push('   discovery for that curated adapter, not the adapter itself. Names below are');
  l3Lines.push('   machine-derived 1:1 from the LESS-resolved selector + property; this is a');
  l3Lines.push('   rename, not a reduction in vocabulary (colour palettes, spacing scales etc.');
  l3Lines.push('   still need a hand curation pass). The trailing comment carries the FULL');
  l3Lines.push('   original ruleset so the mapping is reviewable before comments get stripped');
  l3Lines.push('   and the cascade gets minified.');
  l3Lines.push('   ===================================================== */');
  l3Lines.push('');
  l3Lines.push(':root {');
  const nameCount = new Map(); // semanticName -> count, for collision suffixing
  const usedBySignature = new Map(); // signature -> assigned name (for the 73 many-to-one collapses)
  const l3Rows = [];
  for (const a of aligned) {
    const rule = rules.get(a.key);
    const g = groupOf(a.prop);
    const n4 = String(a.num).padStart(4, '0');
    const regTok = `--ab-${g}-${a.layer}-${n4}`;
    const { selSlug, mods } = resolveChain(rule.chain);
    const signature = JSON.stringify([selSlug, mods, a.prop.replace(/^-+/, '')]);
    let semName = usedBySignature.get(signature);
    if (!semName) {
      let base = buildSemanticName(rule.chain, a.prop);
      let candidate = base;
      let suffix = 2;
      const takenNames = new Set(usedBySignature.values());
      while (takenNames.has(candidate)) {
        candidate = `${base}-${suffix++}`;
      }
      semName = candidate;
      usedBySignature.set(signature, semName);
    }
    const comment = rule.chain.join(' ').trim() + ' { ' + rule.decls.join('; ') + '; }';
    l3Rows.push({ regTok, semName, comment });
  }
  for (const row of l3Rows) {
    l3Lines.push(`  ${row.regTok}: var(${row.semName}); // ${row.comment}`);
  }
  l3Lines.push('}');
  l3Lines.push('');
  const l3Final = l3Lines.join('\n');

  fs.writeFileSync(OUT_L1, l1Final);
  fs.writeFileSync(OUT_L2, l2Final);
  fs.writeFileSync(OUT_L3, l3Final);

  const uniqueSemNames = new Set(l3Rows.map(r => r.semName));
  console.log(`Layer 1 written: ${OUT_L1} (${aligned.length} tokens renamed)`);
  console.log(`Layer 2 written: ${OUT_L2} (${l2Lines.filter(l => l.startsWith('  --ad-')).length} mappings)`);
  console.log(`Layer 3 written: ${OUT_L3} (${l3Rows.length} rows, ${uniqueSemNames.size} unique semantic names)`);
}

main();
