#!/usr/bin/env node
/**
 * ab-fold-section-schemas.js — the generator behind the theme surface.
 *
 * Reads the generic section schemas in design-kb/section-schemas/*.json and emits
 * the TARGET (--ab-base-*) LESS for three of the six layers:
 *   • L4 base-profile defaults  (--ab-base-pf-default-*), incl. dark-mode seeds
 *   • L3 pivot hooks            (--ab-base-* : var(theme, default))
 *   • a template field manifest (JSON: authorable fields per extent preset)
 *
 * Single source of truth: edit a section schema, re-fold — never hand-edit the
 * generated LESS. Output goes to exports/ab-fold/ (version-controlled, reviewable)
 * because the live --ab-* LESS does not exist until the phased rename; this proves
 * the schema -> LESS pipeline and produces the artifacts the rename will adopt.
 *
 *   node tools/ab-fold-section-schemas.js
 *
 * Spec: docs/authoring/section-schemas.md.
 */
'use strict';
const fs = require('fs');
const path = require('path');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const SCHEMA_DIR = path.join(ROOT, 'design-kb', 'section-schemas');
const OUT_DIR = path.join(ROOT, 'exports', 'ab-fold');

const PF = '--ab-base-pf-default-';   // L4 default namespace
const BASE = '--ab-base-';            // L3 pivot namespace
const THEME = '--ab-theme-pf-default-'; // L5 contract namespace

// --- helpers ---------------------------------------------------------------
function seedVar(name) { return `var(${PF}${name})`; }

// rewrite bare seed identifiers inside a derive/channel expression to var(--ab-base-pf-default-<seed>)
function resolveSeeds(expr, seedNames) {
  let out = expr;
  // longest names first so e.g. "accent-l" is not clipped by "accent"
  for (const n of [...seedNames].sort((a, b) => b.length - a.length)) {
    out = out.replace(new RegExp(`(^|[^\\w-])${n.replace(/[-]/g, '\\-')}(?![\\w-])`, 'g'), `$1${seedVar(n)}`);
  }
  return out;
}

// resolve a seed's own default value (may itself reference another seed: "var(user-l)")
function seedDefault(val, seedNames) {
  if (typeof val !== 'string') return String(val);
  const m = val.match(/^var\(([\w-]+)\)$/);
  if (m && seedNames.includes(m[1])) return seedVar(m[1]);
  return val;
}

// Utopia fluid clamp, matching cm-type.less .cm-fluid():
// min/max in rem, vwMin/vwMax in rem. preferred = intercept rem + slope*100 vw.
function clamp(minRem, maxRem, vwMinRem, vwMaxRem) {
  const slope = (maxRem - minRem) / (vwMaxRem - vwMinRem);
  const intercept = minRem - slope * vwMinRem;
  const vw = slope * 100;
  const lo = Math.min(minRem, maxRem), hi = Math.max(minRem, maxRem);
  return `clamp(${+lo.toFixed(4)}rem, ${+intercept.toFixed(4)}rem + ${+vw.toFixed(4)}vw, ${+hi.toFixed(4)}rem)`;
}
function remOf(lengthStr) { return parseFloat(String(lengthStr)); } // "1.125rem" -> 1.125

// compute an L4 default VALUE string for a token, per its kind
function tokenDefault(tok, section, seedNames) {
  switch (tok.kind) {
    case 'hsl':
      return `~"hsl(${tok.channels.map(seedVar).join(' ')})"`;
    case 'derive':
      return `~"${resolveSeeds(tok.expr, seedNames)}"`;
    case 'ref':       return `var(${BASE}${tok.ref})`;
    case 'ref-seed':  return seedVar(tok.ref);
    case 'literal':   return tok.value;
    case 'clamp': {
      const s = section.seeds;
      const ratio = s['type-ratio'].default;
      const baseMin = remOf(s['type-base-min'].default);
      const baseMax = remOf(s['type-base-max'].default);
      const vwMin = remOf(s['vw-min'].default);
      const vwMax = remOf(s['vw-max'].default);
      const f = Math.pow(ratio, tok.power);
      // escape: LESS would otherwise evaluate "<rem> + <vw>" as a unit sum and destroy the clamp
      return `~"${clamp(baseMin * f, baseMax * f, vwMin, vwMax)}"`;
    }
    case 'symbol-list': {
      const seed = section.seeds[tok.ref];
      return (seed.default || []).join(' ');
    }
    default: return `/* TODO kind=${tok.kind} */`;
  }
}

// --- read schemas ----------------------------------------------------------
const files = fs.readdirSync(SCHEMA_DIR).filter(f => f.endsWith('.json')).sort();
const sections = files.map(f => ({ file: f, data: JSON.parse(fs.readFileSync(path.join(SCHEMA_DIR, f), 'utf8')) }));

fs.mkdirSync(OUT_DIR, { recursive: true });

const l4 = [':root {'];                 // L4 defaults
const l4dark = [];                      // dark-mode seed overrides
const l3 = [':root {'];                 // L3 pivot hooks
const contract = [];                    // L5 contract token list (comment)
const template = { presets: { basic: [], standard: [], full: [] }, bespokeNote: 'a bespoke template names sections (+ optional tokens) to include' };
let counts = { sections: 0, seeds: 0, themeableSeeds: 0, tokens: 0, themeable: 0, darkSeeds: 0, fields: 0 };

for (const { data } of sections) {
  const sec = data.section;
  const seedNames = Object.keys(data.seeds || {});
  counts.sections++;
  l4.push(`  /* ${sec} — seeds */`);
  for (const [name, seed] of Object.entries(data.seeds || {})) {
    counts.seeds++;
    const def = seedDefault(seed.default, seedNames);
    const hasDark = seed.modes && seed.modes.dark !== undefined;
    // A themeable seed gets its OWN L5 hook, so a user theme can re-dial the seed
    // itself (e.g. re-hue the whole theme via --ab-theme-pf-default-user-h) — not
    // just override the final roles derived from it. A non-themeable seed stays a
    // hard default.
    if (seed.themeable) {
      counts.themeableSeeds++;
      l4.push(`  ${PF}${name}: var(${THEME}${name}, ${def});`);
      contract.push(`${THEME}${name}`);
    } else {
      l4.push(`  ${PF}${name}: ${def};`);
    }
    // Dark-mode seed override. A themeable seed with a dark value exposes a
    // SEPARATE dark hook (--ab-theme-pf-default-<name>-dark) so a theme can set
    // its light and dark values independently; each falls back to the base
    // default for its own mode. (A non-themeable dark seed stays a hard override.)
    if (hasDark) {
      counts.darkSeeds++;
      if (seed.themeable) {
        l4dark.push(`  ${PF}${name}: var(${THEME}${name}-dark, ${seed.modes.dark});`);
        contract.push(`${THEME}${name}-dark`);
      } else {
        l4dark.push(`  ${PF}${name}: ${seed.modes.dark};`);
      }
    }
    addField(seed, name, sec, 'seed');
  }
  l4.push(`  /* ${sec} — token defaults */`);
  for (const [name, tok] of Object.entries(data.tokens || {})) {
    counts.tokens++;
    // A ref-seed token carries no L4 default of its own — the seed it points at owns
    // that slot (emitting one would be a circular self-reference when names match).
    const isRefSeed = tok.kind === 'ref-seed';
    if (!isRefSeed) l4.push(`  ${PF}${name}: ${tokenDefault(tok, data, seedNames)};`);
    const l4ref = isRefSeed ? `${PF}${tok.ref}` : `${PF}${name}`;
    // L3 pivot hook
    if (tok.themeable) {
      counts.themeable++;
      l3.push(`  ${BASE}${name}: var(${THEME}${name}, var(${l4ref}));`);
      contract.push(`${THEME}${name}`);
    } else {
      l3.push(`  ${BASE}${name}: var(${l4ref});`);
    }
    addField(tok, name, sec, 'token');
  }
}

function addField(entry, name, sec, kind) {
  if (!entry.template) return;
  counts.fields++;
  const field = { section: sec, name, kind, label: entry.template.label, input: entry.template.input };
  for (const p of entry.template.presets || []) if (template.presets[p]) template.presets[p].push(field);
}

l4.push('}');
l3.push('}');
if (l4dark.length) {
  l4.push('', '/* dark mode — seed overrides only; tokens re-derive */',
    ':root[data-theme="dark"], :root.ab-dark {', ...l4dark, '}');
}

const header = (name) => `// GENERATED by tools/ab-fold-section-schemas.js from design-kb/section-schemas/*.json\n// Do not hand-edit — edit the schema and re-fold. (${name})\n\n`;
fs.writeFileSync(path.join(OUT_DIR, 'ab-base-pf-default.less'), header('L4 base-profile defaults') + l4.join('\n') + '\n');
fs.writeFileSync(path.join(OUT_DIR, 'ab-base-pivot.less'), header('L3 pivot hooks') + l3.join('\n') + '\n' +
  `\n// L5 contract (${contract.length} hooks across ${counts.themeableSeeds} themeable seeds + ${counts.themeable} themeable tokens, plus a -dark variant per themeable seed that has a dark value; declared by a user-theme profile, else the hook falls to the L4 default):\n// ` + contract.join('\n// ') + '\n');
fs.writeFileSync(path.join(OUT_DIR, 'ab-templates.json'), JSON.stringify(template, null, 2) + '\n');

console.log(`folded ${counts.sections} sections: ${counts.seeds} seeds (${counts.themeableSeeds} themeable), ${counts.tokens} tokens (${counts.themeable} themeable), ${counts.darkSeeds} dark-mode seeds, ${counts.fields} template fields`);
console.log(`wrote ab-base-pf-default.less, ab-base-pivot.less, ab-templates.json to ${path.relative(ROOT, OUT_DIR)}/`);
