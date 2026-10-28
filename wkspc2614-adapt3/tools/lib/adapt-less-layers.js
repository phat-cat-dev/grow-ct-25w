'use strict';
/**
 * adapt-less-layers.js
 *
 * Shared primitives for the tools/theme-mapping/layers/lX-*-generator.js
 * family (L2 core, L3 core-components, L4 vanilla, L5 vanilla-components,
 * the four lX-*-template generators, and the two L6 output generators).
 *
 * Why this exists: L2/L3/L4 each carried a verbatim ~300-line copy of the
 * same file-order / lessc-driving / CSS-parsing / token-matching code before
 * this lib was lifted out of them (see the retro-fit note in each of their
 * _index.md files). tools/lib/ab-map-structure.js's own banner records two
 * historical bugs caused by exactly that kind of drift between near-copies -
 * that precedent is why a shared lib is justified here even though this
 * project otherwise avoids premature abstraction.
 *
 * Reads only. Never writes. Every generator that uses this lib still does
 * its own fs.writeFileSync for its own .less/.json - this module has no
 * knowledge of any one layer's output shape.
 */
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..');
const CONFIG_SCHEMA = path.join(ROOT, 'src', 'core', 'schema', 'config.schema.json');

function rel(p) { return path.relative(ROOT, p).replace(/\\/g, '/'); }

// ---------------------------------------------------------------------------
// 0. CLI / JSON loading helpers
// ---------------------------------------------------------------------------

// Faithful to each generator's own historical parseArgs, extended with the
// two new flags later layers need. Callers that only ever passed --json-only
// get exactly the same { jsonOnly } behaviour as before - withValues/theme
// are additive, default to false/null, and do not change existing behaviour
// for a caller that never reads them.
function parseArgs(argv) {
  const out = { jsonOnly: false, withValues: false, theme: null };
  for (const a of argv) {
    if (a === '--json-only') out.jsonOnly = true;
    else if (a === '--with-values') out.withValues = true;
    else if (a.startsWith('--theme=')) out.theme = a.slice('--theme='.length);
  }
  return out;
}

// Read a JSON file a generator depends on, or exit(1) with a message naming
// which upstream generator produces it - the same FATAL pattern L2/L3/L4
// already used inline for L1_JSON_PATH/L2_JSON_PATH, lifted so every later
// generator (L5, the templates, L6) reports missing upstream JSON the same way.
function readJsonOrFatal(jsonPath, producedByHint) {
  if (!fs.existsSync(jsonPath)) {
    console.error(`FATAL: required input not found at ${rel(jsonPath)}.${producedByHint ? ` Run ${producedByHint} first.` : ''}`);
    process.exit(1);
  }
  return JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
}

// Resolve --theme=<name> (default 'adapt-contrib-vanilla'), FATAL if the
// theme directory does not exist under src/theme, and - when an upstream
// JSON is supplied - FATAL if that JSON was generated against a different
// theme, so a mismatch surfaces instead of silently mixing two themes' data.
function resolveTheme(args, upstreamJson) {
  const name = args.theme || 'adapt-contrib-vanilla';
  const dir = path.join(ROOT, 'src', 'theme', name);
  if (!fs.existsSync(dir)) {
    console.error(`FATAL: --theme=${name} not found at ${rel(dir)}.`);
    process.exit(1);
  }
  if (upstreamJson && upstreamJson.theme && upstreamJson.theme !== name) {
    console.error(`FATAL: --theme=${name} does not match the theme (${upstreamJson.theme}) the upstream JSON (${upstreamJson.generatedBy || 'unknown generator'}) was built against.`);
    process.exit(1);
  }
  return { name, dir };
}

// ---------------------------------------------------------------------------
// 1. file order: faithful copy of grunt/config/less.js's sortLESSFilePaths
// (grunt/config/less.js:7-18 - re-implemented, not required, because that
// file is a grunt option factory (module.exports = function(grunt, options)
// {...}), not a plain function export.)
// ---------------------------------------------------------------------------
function alphanumericOrder(a, b) { return a > b ? 1 : a < b ? -1 : 0; }
function lengthOrder(a, b) { return a.length > b.length ? 1 : a.length < b.length ? -1 : 0; }
function compareFilePaths(a, b) {
  const aParsed = path.parse(a);
  const bParsed = path.parse(b);
  if (aParsed.dir !== bParsed.dir) return alphanumericOrder(a, b);
  const aStartsB = bParsed.name.startsWith(aParsed.name);
  const bStartsA = aParsed.name.startsWith(bParsed.name);
  if (!aStartsB && !bStartsA) return alphanumericOrder(a, b);
  return lengthOrder(aParsed.name, bParsed.name);
}
function walkLessFiles(dir) {
  let out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) out = out.concat(walkLessFiles(p));
    else if (entry.name.endsWith('.less')) out.push(p);
  }
  return out;
}

// ---------------------------------------------------------------------------
// 2. Stage-0 device variables: schema defaults (grunt/tasks/less.js:19-51)
// ---------------------------------------------------------------------------
function loadScreenSizeDefaults() {
  const schema = JSON.parse(fs.readFileSync(CONFIG_SCHEMA, 'utf8'));
  const props = schema.properties.screenSize.properties;
  const out = {};
  for (const [name, def] of Object.entries(props)) out[name] = def.default;
  return out;
}
function screenSizeToLessVars(screenSize) {
  const threshold = 300;
  const baseFontSize = 16;
  let vars = '';
  for (const [name, value] of Object.entries(screenSize)) {
    const em = value > threshold ? value / baseFontSize : value;
    vars += `@adapt-device-${name}: ${em}em;\n`;
  }
  return vars;
}

// ---------------------------------------------------------------------------
// 3. compile via lessc (same spawnSync('npx', ['lessc', ...]) precedent every
// layer has used so far; see the L5 _index.md note on why in-process
// less.render() was not substituted without a measured byte-identity check).
// `labelPrefix` is the caller's own tmp-file naming convention (e.g.
// 'l2-core-whole', 'l4-vanilla-file') - cosmetic only, does not affect output.
// ---------------------------------------------------------------------------
function runLessc(bundleText, labelPrefix) {
  const tmpFile = path.join(require('os').tmpdir(), `${labelPrefix}-${process.pid}-${Math.random().toString(36).slice(2)}.less`);
  fs.writeFileSync(tmpFile, bundleText);
  const r = spawnSync('npx', ['lessc', tmpFile], { encoding: 'utf8', shell: true, cwd: ROOT });
  fs.unlinkSync(tmpFile);
  return r;
}

// ---------------------------------------------------------------------------
// 4. split compiled CSS into top-level rule blocks (depth-aware bracket walk)
// ---------------------------------------------------------------------------
function splitCssRules(css) {
  const rules = [];
  let depth = 0;
  let buf = '';
  for (let i = 0; i < css.length; i++) {
    const ch = css[i];
    if (ch === '{') {
      if (depth === 0) rules.push({ selector: buf.trim(), bodyStart: i + 1 });
      depth++;
      buf = '';
      continue;
    }
    if (ch === '}') {
      depth--;
      if (depth === 0 && rules.length && rules[rules.length - 1].body === undefined) {
        rules[rules.length - 1].body = css.slice(rules[rules.length - 1].bodyStart, i).trim();
      }
      buf = '';
      continue;
    }
    if (depth === 0) buf += ch;
  }
  return rules.filter((r) => r.selector && !r.selector.startsWith('@') && r.body !== undefined);
}

// ---------------------------------------------------------------------------
// 5. resolve every selector a .less file itself declares (source attribution)
// ---------------------------------------------------------------------------
function stripComments(text) {
  return text.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');
}
function splitTopLevelCommas(text) {
  const parts = [];
  let depth = 0;
  let buf = '';
  for (const ch of text) {
    if (ch === '(') depth++;
    if (ch === ')') depth--;
    if (ch === ',' && depth === 0) { parts.push(buf.trim()); buf = ''; continue; }
    buf += ch;
  }
  if (buf.trim()) parts.push(buf.trim());
  return parts;
}
function scanDeclaredSelectors(text, file) {
  const clean = stripComments(text);
  const found = []; // { selector, file, line }
  const stack = []; // { alts: string[], isTransparent }
  let depth = 0;
  let buf = '';
  let line = 1;
  let bufLine = 1;
  for (let i = 0; i < clean.length; i++) {
    const ch = clean[i];
    if (ch === '\n') { line++; }
    if (ch === '{') {
      const rawParts = splitTopLevelCommas(buf.trim());
      const parentAlts = depth === 0 ? [''] : (stack[depth - 1]?.alts || ['']);
      let alts = [];
      let isTransparent = false;
      if (/^@/.test(rawParts[0] || '')) {
        // @media / @supports etc - pass the parent context straight through
        alts = parentAlts;
        isTransparent = true;
      } else {
        for (const parentAlt of parentAlts) {
          for (const raw of rawParts) {
            let resolved;
            if (raw.includes('&')) resolved = raw.replace(/&/g, parentAlt);
            else resolved = parentAlt ? `${parentAlt} ${raw}` : raw;
            alts.push(resolved);
          }
        }
      }
      if (!isTransparent) {
        for (const a of alts) found.push({ selector: a, file, line: bufLine });
      }
      stack.push({ alts, isTransparent });
      depth++;
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === '}') {
      depth--;
      stack.pop();
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === ';') { buf = ''; bufLine = line; continue; }
    buf += ch;
    if (!buf.trim()) bufLine = line;
  }
  return found;
}

// ---------------------------------------------------------------------------
// 5b. guard-transparent variant of scanDeclaredSelectors, for L5.
//
// Finding (see l5-adapt-vanilla-components-less/_index.md): 37 `& when (...)`
// guard blocks occur across 15 of vanilla's 19 plugin directories (zero in
// src/components). `& when (...) { ... }` is NOT a new selector - it is a
// conditional-compile guard wrapping the SAME parent selector, exactly like
// `@media` is transparent above. The plain scanner treats `& when (...)` as
// an ordinary nested rule and appends the guard text onto the selector
// itself, producing garbage like `.accordion-item when (@item-color-style =
// filled)__btn` (543 selectors, 193 (36%) garbage, measured). This variant
// treats `& when (...)` the same way `@media`/`@supports` are already
// treated - transparent, passing the parent alt(s) straight through - and
// additionally records the guard expression on each selector it covers, so
// guard-liveness can be probed later without re-parsing.
function scanDeclaredSelectorsGuardAware(text, file) {
  const clean = stripComments(text);
  const found = []; // { selector, file, line, guard: string|null }
  const stack = []; // { alts, isTransparent, guard }
  let depth = 0;
  let buf = '';
  let line = 1;
  let bufLine = 1;
  const WHEN_GUARD_RE = /^&\s*when\s*\((.*)\)$/;
  for (let i = 0; i < clean.length; i++) {
    const ch = clean[i];
    if (ch === '\n') { line++; }
    if (ch === '{') {
      const rawTrimmed = buf.trim();
      const parentFrame = depth === 0 ? { alts: [''], guard: null } : (stack[depth - 1] || { alts: [''], guard: null });
      const parentAlts = parentFrame.alts || [''];
      const whenMatch = rawTrimmed.match(WHEN_GUARD_RE);
      let alts = [];
      let isTransparent = false;
      let guard = parentFrame.guard || null;
      if (whenMatch) {
        // `& when (...)` - transparent guard on the SAME parent selector(s).
        alts = parentAlts;
        isTransparent = true;
        guard = whenMatch[1].trim();
      } else {
        const rawParts = splitTopLevelCommas(rawTrimmed);
        if (/^@/.test(rawParts[0] || '')) {
          alts = parentAlts;
          isTransparent = true;
        } else {
          for (const parentAlt of parentAlts) {
            for (const raw of rawParts) {
              let resolved;
              if (raw.includes('&')) resolved = raw.replace(/&/g, parentAlt);
              else resolved = parentAlt ? `${parentAlt} ${raw}` : raw;
              alts.push(resolved);
            }
          }
        }
      }
      if (!isTransparent) {
        for (const a of alts) found.push({ selector: a, file, line: bufLine, guard });
      }
      stack.push({ alts, isTransparent, guard });
      depth++;
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === '}') {
      depth--;
      stack.pop();
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === ';') { buf = ''; bufLine = line; continue; }
    buf += ch;
    if (!buf.trim()) bufLine = line;
  }
  return found;
}

// ---------------------------------------------------------------------------
// 6. token-set matching between a declared/compiled selector and an L1 spine selector
// ---------------------------------------------------------------------------
function classTokens(sel) {
  return (sel.match(/\.[A-Za-z0-9_-]+/g) || []).map((s) => s.slice(1));
}
function tokensEqual(a, b) {
  if (a.length !== b.length) return false;
  const sb = new Set(b);
  return a.every((t) => sb.has(t));
}
function tokensSubset(a, b) {
  if (!a.length) return false;
  const sb = new Set(b);
  return a.every((t) => sb.has(t));
}
function selectorsRelated(declaredTokens, rungTokens) {
  return tokensSubset(declaredTokens, rungTokens) || tokensSubset(rungTokens, declaredTokens);
}

// ---------------------------------------------------------------------------
// 7. find the L1 .less line number for each spine rung (self-updating cross-reference)
// ---------------------------------------------------------------------------
function buildL1LineIndex(l1LessText, spine) {
  const lines = l1LessText.split('\n');
  const index = {};
  for (const rung of spine) {
    // exact rule line: "<selector> {}"  OR, for the two comment-only placeholder
    // rungs (no own {} line), the preceding comment line itself.
    let found = null;
    for (let i = 0; i < lines.length; i++) {
      const escaped = rung.selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      if (new RegExp(`^${escaped}\\s*\\{\\}`).test(lines[i].trim())) { found = i + 1; break; }
      if (lines[i].includes(`/* ${rung.selector}`)) { found = i + 1; }
    }
    index[rung.selector] = found;
  }
  return index;
}

// ---------------------------------------------------------------------------
// 8. real compiled property-name extraction (L4's propertyNamesOf, lifted
// unchanged - used by L4's relationToL2 and L5's relationToL3 alike).
// ---------------------------------------------------------------------------
function propertyNamesOf(bodyText) {
  if (!bodyText) return new Set();
  const names = new Set();
  for (const decl of bodyText.split(';')) {
    const m = decl.trim().match(/^([a-zA-Z-]+)\s*:/);
    if (m) names.add(m[1].toLowerCase());
  }
  return names;
}
function combinedBody(hooks) {
  return hooks.filter((h) => h.compiled).map((h) => h.compiled).join('; ');
}

// ---------------------------------------------------------------------------
// 9. variable + mixin contract scanner (new - needed from L5 onward).
//
// Must run on RAW lines, never on stripComments() output: stripComments'
// `//.*` rule mangles `url('https://fonts.googleapis.com/...')` at
// src/theme/adapt-contrib-vanilla/less/_defaults/_font-config.less:3 into
// `url('https:` (the `//` inside the URL is read as a line comment). Variable
// and mixin declarations are themselves single-line in every real file this
// was measured against (41/41 core variables, 531/531 vanilla variables, 0
# unparsed), so no comment-stripping is needed for the two regexes below -
// scanning raw lines side-steps the bug entirely rather than working around it.
// ---------------------------------------------------------------------------
const VAR_DECL_RE = /^(\s*)@([A-Za-z][A-Za-z0-9-]*)\s*:\s*(.*?);\s*(\/\/.*)?$/;
const MIXIN_DEF_RE = /^(\s*)(\.[A-Za-z][A-Za-z0-9_-]*)\s*\(([^)]*)\)\s*(when\s*\(.*\))?\s*\{/;
const MIXIN_CALL_RE = /^(\s*)(\.[A-Za-z][A-Za-z0-9_-]*)\s*(\(([^;{]*)\))?\s*(!important)?\s*;/;

// Two variable sites are block-scoped (not file-top-level) and must NOT be
// hoisted to a :root-style "layer declares this variable globally" bucket:
//   - src/core/less/core/nav.less:117       @breakpoint:
//   - vanilla core/drawerItem.less:9        @total-margin:
// Both are inside a mixin/rule body, re-declared per use, not a layer-wide
// contract variable. scanLessStructure records indent depth (leading
// whitespace length) precisely so a caller can apply this exclusion by
// checking `indent > 0`, rather than hardcoding the two file:line pairs,
// which would silently stop working the moment either file is edited.
function scanLessStructure(fileList) {
  const variables = []; // { name, file, line, value, indent }
  const mixinDefs = []; // { name, file, line, params, guarded, indent }
  const mixinCalls = []; // { name, file, line, args, indent }
  for (const f of fileList) {
    const text = fs.readFileSync(f, 'utf8');
    const lines = text.split('\n');
    for (let i = 0; i < lines.length; i++) {
      const raw = lines[i];
      let m = raw.match(VAR_DECL_RE);
      if (m) {
        variables.push({ name: m[2], file: rel(f), line: i + 1, value: m[3].trim(), indent: m[1].length });
        continue;
      }
      m = raw.match(MIXIN_DEF_RE);
      if (m) {
        mixinDefs.push({ name: m[2], file: rel(f), line: i + 1, params: m[3].trim(), guarded: !!m[4], indent: m[1].length });
        continue;
      }
      m = raw.match(MIXIN_CALL_RE);
      if (m) {
        mixinCalls.push({ name: m[2], file: rel(f), line: i + 1, args: (m[4] || '').trim(), indent: m[1].length });
      }
    }
  }
  return { variables, mixinDefs, mixinCalls };
}

// Resolve each variable NAME to its declaring site(s), separating top-level
// (indent === 0, a real layer-wide contract variable) from block-scoped
// (indent > 0, re-declared per use, excluded from the contract) sites.
function resolveVariableSites(variables) {
  const byName = new Map(); // name -> { topLevel: [...sites], blockScoped: [...sites] }
  for (const v of variables) {
    if (!byName.has(v.name)) byName.set(v.name, { topLevel: [], blockScoped: [] });
    const entry = byName.get(v.name);
    if (v.indent === 0) entry.topLevel.push(v);
    else entry.blockScoped.push(v);
  }
  return byName;
}

// Index mixin definitions by name - a mixin can have more than one guarded
// definition (dispatch by `when`), so this is name -> [sites], not a single site.
function indexMixinDefinitions(mixinDefs) {
  const byName = new Map();
  for (const d of mixinDefs) {
    if (!byName.has(d.name)) byName.set(d.name, []);
    byName.get(d.name).push(d);
  }
  return byName;
}

// Resolve each mixin CALL site to its definition(s) by name. A call whose
// name has no entry in defsByName is reported with defs: [] (unresolved) -
// flagged, never silently dropped, same discipline as L3's classifySelector.
function resolveMixinCalls(mixinCalls, defsByName) {
  return mixinCalls.map((call) => ({
    ...call,
    defs: defsByName.get(call.name) || []
  }));
}

// ---------------------------------------------------------------------------
// 10. property-name set -> --ad-lX-<property> custom-property token names.
// Token NAMES are the real compiled CSS property names (from propertyNamesOf
// on the real layer's own JSON), never invented. `layer` is the lX prefix
// ('l2'|'l3'|'l4'|'l5'). Returns [{ property, token }], sorted for stable output.
// ---------------------------------------------------------------------------
function tokeniseBody(layer, propertyNames) {
  return [...propertyNames].sort().map((property) => ({
    property,
    token: `--ad-${layer}-${property}`
  }));
}

module.exports = {
  ROOT,
  rel,
  parseArgs,
  readJsonOrFatal,
  resolveTheme,
  compareFilePaths,
  walkLessFiles,
  loadScreenSizeDefaults,
  screenSizeToLessVars,
  runLessc,
  splitCssRules,
  stripComments,
  splitTopLevelCommas,
  scanDeclaredSelectors,
  scanDeclaredSelectorsGuardAware,
  classTokens,
  tokensEqual,
  tokensSubset,
  selectorsRelated,
  buildL1LineIndex,
  propertyNamesOf,
  combinedBody,
  scanLessStructure,
  resolveVariableSites,
  indexMixinDefinitions,
  resolveMixinCalls,
  tokeniseBody,
  VAR_DECL_RE,
  MIXIN_DEF_RE,
  MIXIN_CALL_RE
};
