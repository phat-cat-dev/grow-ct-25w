#!/usr/bin/env node
/**
 * l4-adapt-vanilla-less-generator.js — compile adapt-contrib-vanilla's less
 * (core/less-mirroring files + _defaults + plugins + project) standalone,
 * mapped onto the same L1 structural spine L2 used, with L2's own hooks
 * cited alongside so the three layers read as one column: L1 spine -> L2
 * core hook -> L4 vanilla hook -> relation (new / redeclare / additive).
 *
 * This is the real Stage 2d of grunt's LESS compile (grunt/tasks/less.js:
 * 68-82, the LAST entry in options.src) — compiled here with core's less in
 * the bundle too, because vanilla's own core/*.less calls mixins
 * (.l-container-padding, .l-container-responsive, .transform, .transition)
 * that only exist in src/core/less/_defaults/layout.less and
 * src/core/less/core/{transform,transitions}.less. Confirmed empirically:
 * compiling src/theme/adapt-contrib-vanilla/less alone fails
 * (".l-container-responsive is undefined") - vanilla is NOT self-sufficient,
 * the opposite of core (see l2-adapt-core-less/_index.md's correction).
 * Stage 2a/2b/2c (components/extensions/menu) are deliberately omitted here -
 * this generator is a direct two-layer (core vs vanilla) comparison, not a
 * full build. See tools/theme-mapping/layers/l4-adapt-vanilla-less/_index.md.
 *
 * Reads (never writes):
 *   src/core/less/**\/*.less                   — compile CONTEXT only (mixin
 *                                                resolution); never scanned/
 *                                                attributed in this layer -
 *                                                that is L2's job.
 *   src/theme/adapt-contrib-vanilla/less/**\/*.less — compiled + scanned/attributed
 *   src/core/schema/config.schema.json         — screenSize defaults (same as L2)
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.json
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less (line numbers)
 *   tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less.json (L2's own hooks, for citation)
 *
 * Writes:
 *   tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less.less
 *   tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less.json
 *
 * Usage:
 *   node tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less-generator.js
 *   node tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less-generator.js --json-only
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const CORE_LESS_DIR = path.join(ROOT, 'src', 'core', 'less');
const VANILLA_LESS_DIR = path.join(ROOT, 'src', 'theme', 'adapt-contrib-vanilla', 'less');
const CONFIG_SCHEMA = path.join(ROOT, 'src', 'core', 'schema', 'config.schema.json');
const L1_DIR = path.join(ROOT, 'tools', 'theme-mapping', 'layers', 'l1-adapt-templates');
const L1_JSON_PATH = path.join(L1_DIR, 'adapt-template-classes.json');
const L1_LESS_PATH = path.join(L1_DIR, 'adapt-template-classes.less');
const L2_JSON_PATH = path.join(ROOT, 'tools', 'theme-mapping', 'layers', 'l2-adapt-core-less', 'l2-adapt-core-less.json');
const OUT_DIR = __dirname;

function rel(p) { return path.relative(ROOT, p).replace(/\\/g, '/'); }

function parseArgs(argv) {
  const out = { jsonOnly: false };
  for (const a of argv) {
    if (a === '--json-only') out.jsonOnly = true;
  }
  return out;
}

// ---- 1. file order: same faithful copy of grunt/config/less.js's sortLESSFilePaths as L2 ----
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

// ---- 2. Stage-0 device variables (identical to L2 - same framework defaults) ----
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

// ---- 3. compile via lessc ----
function runLessc(bundleText, label) {
  const tmpFile = path.join(require('os').tmpdir(), `l4-vanilla-${label}-${process.pid}-${Math.random().toString(36).slice(2)}.less`);
  fs.writeFileSync(tmpFile, bundleText);
  const r = spawnSync('npx', ['lessc', tmpFile], { encoding: 'utf8', shell: true, cwd: ROOT });
  fs.unlinkSync(tmpFile);
  return r;
}
// Whole-bundle: core (mandatory) then vanilla (theme, Stage 2d) - sanity check
// and line-count stat only, same caveat as L2 (shared bare selectors across
// files make this unusable for per-hook attribution).
function compileWholeBundle(coreFiles, vanillaFiles, screenSizeVars) {
  let bundle = screenSizeVars + '\n';
  for (const f of coreFiles) bundle += `\n/* ===== ${rel(f)} ===== */\n` + fs.readFileSync(f, 'utf8');
  for (const f of vanillaFiles) bundle += `\n/* ===== ${rel(f)} ===== */\n` + fs.readFileSync(f, 'utf8');
  const r = runLessc(bundle, 'whole');
  if (r.status !== 0) {
    console.error('FATAL: lessc failed to compile core+vanilla together.');
    console.error(r.stderr || r.stdout);
    process.exit(1);
  }
  return r.stdout;
}
// Per-file isolated compile: screenSize vars + ALL core/less files (mixin
// context only, never scanned) + every OTHER vanilla file + a unique marker
// + exactly this one vanilla file's own text. Only CSS after the marker is
// kept, so bare selectors vanilla shares across its own files (e.g. .page in
// both core/page.less and, hypothetically, a plugin) are attributed only to
// the file being isolated - same technique as L2, context list is larger.
function compilePerFile(coreContextFiles, vanillaFiles, screenSizeVars) {
  const perFileCompiled = new Map();
  const marker = '/* L4-ISOLATE-MARKER */';
  const coreText = coreContextFiles.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
  for (const target of vanillaFiles) {
    const others = vanillaFiles.filter((f) => f !== target);
    const othersText = others.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
    const bundle = screenSizeVars + '\n' + coreText + '\n' + othersText + '\n' + marker + '\n' + fs.readFileSync(target, 'utf8');
    const r = runLessc(bundle, 'file');
    if (r.status !== 0) {
      console.error(`WARNING: isolated compile failed for ${rel(target)} - hooks from this file will show no compiled body.`);
      perFileCompiled.set(rel(target), new Map());
      continue;
    }
    const markerIdx = r.stdout.indexOf(marker);
    const ownCss = markerIdx >= 0 ? r.stdout.slice(markerIdx + marker.length) : r.stdout;
    const rules = splitCssRules(ownCss);
    const map = new Map();
    for (const rule of rules) {
      if (!map.has(rule.selector)) map.set(rule.selector, rule.body);
      else map.set(rule.selector, map.get(rule.selector) + '; ' + rule.body);
    }
    perFileCompiled.set(rel(target), map);
  }
  return perFileCompiled;
}

// ---- 4. split compiled CSS into top-level rule blocks (identical to L2) ----
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

// ---- 5. resolve every selector vanilla's own files declare (identical algorithm to L2) ----
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
  const found = [];
  const stack = [];
  let depth = 0;
  let buf = '';
  let line = 1;
  let bufLine = 1;
  for (let i = 0; i < clean.length; i++) {
    const ch = clean[i];
    if (ch === '\n') line++;
    if (ch === '{') {
      const rawParts = splitTopLevelCommas(buf.trim());
      const parentAlts = depth === 0 ? [''] : (stack[depth - 1]?.alts || ['']);
      let alts = [];
      let isTransparent = false;
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

// ---- 6. token-set matching (identical to L2) ----
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

// ---- 7. L1 line index (identical to L2) ----
function buildL1LineIndex(l1LessText, spine) {
  const lines = l1LessText.split('\n');
  const index = {};
  for (const rung of spine) {
    let found = null;
    for (let i = 0; i < lines.length; i++) {
      const escaped = rung.selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      if (new RegExp(`^${escaped}\\s*\\{\\}`).test(lines[i].trim())) { found = i + 1; break; }
      if (lines[i].includes(`/* ${rung.selector}`)) found = i + 1;
    }
    index[rung.selector] = found;
  }
  return index;
}

// ---- 8. L2-vs-L4 relation: compare the set of CSS property names each layer
// actually declares on this spine selector, from real compiled text, never guessed.
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
function relationToL2(l2Hooks, l4Hooks) {
  const l2Props = propertyNamesOf(combinedBody(l2Hooks));
  const l4Props = propertyNamesOf(combinedBody(l4Hooks));
  if (!l4Props.size) return null; // L4 has no own declared body here (container-only) - nothing to relate
  if (!l2Props.size) return { kind: 'new', shared: [] };
  const shared = [...l4Props].filter((p) => l2Props.has(p));
  if (!shared.length) return { kind: 'additive', shared: [] };
  return { kind: 'redeclare', shared };
}

function writeLess(data) {
  const lines = [];
  lines.push('/* =====================================================================');
  lines.push(' * l4-adapt-vanilla-less.less');
  lines.push(' * Generated by tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less-generator.js');
  lines.push(' * Do not hand-edit - re-run the generator.');
  lines.push(' *');
  lines.push(' * src/theme/adapt-contrib-vanilla/less compiled together with src/core/less');
  lines.push(' * (vanilla needs core\'s mixins - it does not compile standalone, confirmed');
  lines.push(' * empirically; see _index.md), mapped onto the same L1 structural spine L2');
  lines.push(' * used. Each spine block below shows, in order: the L1 rung, what L2 (core)');
  lines.push(' * already declared there (cited from l2-adapt-core-less.json - not re-derived),');
  lines.push(' * what L4 (vanilla) additionally declares there, and the relation between');
  lines.push(' * the two layers\' real compiled property sets: new (L2 had nothing here),');
  lines.push(' * additive (no shared property names), or redeclare (L4 sets a property');
  lines.push(' * name L2 also set - named explicitly, cascade order means L4 wins).');
  lines.push(' * ===================================================================== */');
  lines.push('');
  lines.push('/* ---- STRUCTURAL SPINE x CORE (L2) x VANILLA (L4) ---- */');
  for (const rung of data.spine) {
    const l1Line = data.l1LineIndex[rung.selector];
    const l1Ref = l1Line ? `adapt-template-classes.less:${l1Line}` : 'adapt-template-classes.less (not found)';
    lines.push(`/* L1 SPINE: ${rung.selector}  <->  ${l1Ref}   (L1 source: ${rung.source}) */`);

    lines.push(`/* L2 CORE (see l2-adapt-core-less.less):`);
    if (!rung.l2Hooks.length) {
      lines.push(`   no core rule for this selector. */`);
    } else {
      lines.push('   (cited, not re-compiled here) */');
      for (const hook of rung.l2Hooks) {
        lines.push(`/* L2 HOOK [${hook.relation}]: ${hook.file}:${hook.line}  declares  ${hook.selector} */`);
        if (hook.compiled) {
          lines.push(`${hook.selector} {`);
          for (const decl of hook.compiled.split(';').map((d) => d.trim()).filter(Boolean)) lines.push(`  ${decl};`);
          lines.push('}');
        } else {
          lines.push(`/*   (container only - declarations are on a descendant, see L2) */`);
        }
      }
    }

    lines.push(`/* L4 VANILLA (this layer): */`);
    if (!rung.l4Hooks.length) {
      lines.push(`/* VANILLA: no rule in adapt-contrib-vanilla's less for this selector. */`);
      lines.push('');
      continue;
    }
    for (const hook of rung.l4Hooks) {
      const relNote = hook.relation === 'subset' ? ` (${hook.selector} is a strict subset of ${rung.selector} - every element matching the spine selector also matches this rule)` : '';
      lines.push(`/* L4 HOOK [${hook.relation}]: ${hook.file}:${hook.line}  declares  ${hook.selector}${relNote} */`);
      if (hook.compiled) {
        lines.push(`${hook.selector} {`);
        for (const decl of hook.compiled.split(';').map((d) => d.trim()).filter(Boolean)) lines.push(`  ${decl};`);
        lines.push('}');
      } else {
        lines.push(`/*   (container only - declarations are on a descendant, see below) */`);
      }
    }
    if (rung.relation) {
      if (rung.relation.kind === 'new') {
        lines.push(`/* L4 RELATION TO L2: NEW - L2 had no direct declared body on ${rung.selector}; this is vanilla's first real rule here. */`);
      } else if (rung.relation.kind === 'additive') {
        lines.push(`/* L4 RELATION TO L2: ADDITIVE - no property name L4 sets here is also set by L2; the two compose, nothing is overridden. */`);
      } else {
        lines.push(`/* L4 RELATION TO L2: REDECLARES propert${rung.relation.shared.length > 1 ? 'ies' : 'y'} also set by L2 core: ${rung.relation.shared.join(', ')} - cascade order (core mandatory, vanilla last) means L4's value wins for ${rung.relation.shared.length > 1 ? 'these' : 'this'}. */`);
      }
    }
    lines.push('');
  }

  lines.push('/* ---- PER-COMPONENT VANILLA RULES (deferred - see _index.md Layer boundaries) ---- */');
  lines.push(`/* This pass is scoped to the spine only, matching L2's own scope exactly.`);
  lines.push(`   adapt-contrib-vanilla/less/plugins/*.less (${data.pluginFileCount} files) is where the`);
  lines.push(`   32 L1 components would get mapped; _index.md records the real naming/`);
  lines.push(`   install-filter findings (only some plugin dirs match an installed`);
  lines.push(`   component) as a forward reference for a future layer, not built here. */`);
  lines.push('');

  lines.push('/* ---- OTHER VANILLA RULES (outside the L1 spine) ---- */');
  lines.push('/* Everything adapt-contrib-vanilla/less declares that has no class-token');
  lines.push('   overlap with any L1 spine selector - nav, drawer, notify, button, loading,');
  lines.push('   shadow, attribution, every plugins/* and project/* file. Listed by source');
  lines.push('   file, selectors only (no bodies - not part of the L1 spine this layer is');
  lines.push('   cross-referencing). */');
  for (const f of data.otherFiles) {
    lines.push(`/* ${f.file}  (${f.selectors.length} selector(s)): ${f.selectors.slice(0, 12).join(', ')}${f.selectors.length > 12 ? ', ...' : ''} */`);
  }
  lines.push('');

  fs.writeFileSync(path.join(OUT_DIR, 'l4-adapt-vanilla-less.less'), lines.join('\n') + '\n');
}

function writeJson(data) {
  fs.writeFileSync(
    path.join(OUT_DIR, 'l4-adapt-vanilla-less.json'),
    JSON.stringify(data, null, 2) + '\n'
  );
}

function printInventory(data) {
  console.log('\nL4 spine x vanilla-less inventory (L2 hooks cited, not re-derived):');
  console.log('selector'.padEnd(32) + 'l1 line'.padEnd(10) + 'l2 hooks'.padEnd(10) + 'l3 hooks'.padEnd(10) + 'relation'.padEnd(12) + 'notes');
  for (const rung of data.spine) {
    const l1Line = data.l1LineIndex[rung.selector] || '-';
    const relKind = rung.relation ? rung.relation.kind : (rung.l4Hooks.length ? '-' : 'no-rule');
    console.log(
      rung.selector.padEnd(32) +
      String(l1Line).padEnd(10) +
      String(rung.l2Hooks.length).padEnd(10) +
      String(rung.l4Hooks.length).padEnd(10) +
      String(relKind).padEnd(12) +
      (rung.l4Hooks.length ? rung.l4Hooks.map((h) => `${h.file}:${h.line}`).join('; ') : 'no vanilla rule')
    );
  }
  console.log(`\nOther (non-spine) vanilla files: ${data.otherFiles.length}`);
  console.log(`Total vanilla .less files compiled: ${data.fileCount} (+ ${data.coreContextFileCount} core files as mixin context, not scanned)`);
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!fs.existsSync(L1_JSON_PATH)) {
    console.error(`FATAL: L1 output not found at ${rel(L1_JSON_PATH)}. Run the L1 generator first.`);
    process.exit(1);
  }
  if (!fs.existsSync(L2_JSON_PATH)) {
    console.error(`FATAL: L2 output not found at ${rel(L2_JSON_PATH)}. Run the L2 generator first.`);
    process.exit(1);
  }
  const l1 = JSON.parse(fs.readFileSync(L1_JSON_PATH, 'utf8'));
  const l1LessText = fs.readFileSync(L1_LESS_PATH, 'utf8');
  const l1LineIndex = buildL1LineIndex(l1LessText, l1.spine);
  const l2 = JSON.parse(fs.readFileSync(L2_JSON_PATH, 'utf8'));
  const l2BySelector = new Map(l2.spine.map((s) => [s.selector, s.coreHooks]));

  const coreFiles = walkLessFiles(CORE_LESS_DIR).sort(compareFilePaths);
  const vanillaFiles = walkLessFiles(VANILLA_LESS_DIR).sort(compareFilePaths);
  const pluginFileCount = vanillaFiles.filter((f) => rel(f).includes('/less/plugins/')).length;
  console.log(`Compiling ${vanillaFiles.length} adapt-contrib-vanilla less file(s), with ${coreFiles.length} core file(s) as mixin context ...`);

  const screenSize = loadScreenSizeDefaults();
  const screenSizeVars = screenSizeToLessVars(screenSize);
  const wholeCss = compileWholeBundle(coreFiles, vanillaFiles, screenSizeVars);
  console.log(`  lessc OK (whole bundle, core+vanilla) - ${wholeCss.split('\n').length} line(s) of compiled CSS.`);
  console.log(`  Compiling ${vanillaFiles.length} vanilla file(s) in isolation for correct per-file attribution ...`);
  const perFileCompiled = compilePerFile(coreFiles, vanillaFiles, screenSizeVars);

  const declared = [];
  for (const f of vanillaFiles) {
    const text = fs.readFileSync(f, 'utf8');
    for (const d of scanDeclaredSelectors(text, rel(f))) declared.push(d);
  }

  const spineOut = [];
  const matchedDeclaredIndexes = new Set();
  for (const rung of l1.spine) {
    const rungTokens = classTokens(rung.selector);
    const l4Hooks = [];
    declared.forEach((d, idx) => {
      const dTokens = classTokens(d.selector);
      if (!dTokens.length) return;
      if (selectorsRelated(dTokens, rungTokens)) {
        matchedDeclaredIndexes.add(idx);
        const fileMap = perFileCompiled.get(d.file);
        const compiledBody = fileMap ? fileMap.get(d.selector) : null;
        l4Hooks.push({
          selector: d.selector,
          file: d.file,
          line: d.line,
          relation: tokensEqual(dTokens, rungTokens) ? 'exact' : 'subset',
          compiled: compiledBody || null
        });
      }
    });
    const l2Hooks = l2BySelector.get(rung.selector) || [];
    spineOut.push({
      selector: rung.selector,
      source: rung.source,
      l2Hooks,
      l4Hooks,
      relation: relationToL2(l2Hooks, l4Hooks)
    });
  }

  const otherByFile = new Map();
  declared.forEach((d, idx) => {
    if (matchedDeclaredIndexes.has(idx)) return;
    if (!classTokens(d.selector).length) return;
    if (!otherByFile.has(d.file)) otherByFile.set(d.file, new Set());
    otherByFile.get(d.file).add(d.selector);
  });
  const otherFiles = [...otherByFile.entries()].map(([file, set]) => ({ file, selectors: [...set] }));

  const data = {
    generatedBy: 'tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less-generator.js',
    l1Source: rel(L1_JSON_PATH),
    l2Source: rel(L2_JSON_PATH),
    screenSizeDefaults: screenSize,
    fileCount: vanillaFiles.length,
    coreContextFileCount: coreFiles.length,
    pluginFileCount,
    l1LineIndex,
    spine: spineOut,
    otherFiles
  };

  if (!args.jsonOnly) writeLess(data);
  writeJson(data);
  printInventory(data);
  console.log(`\nWritten: ${rel(path.join(OUT_DIR, 'l4-adapt-vanilla-less.json'))}`);
  if (!args.jsonOnly) console.log(`Written: ${rel(path.join(OUT_DIR, 'l4-adapt-vanilla-less.less'))}`);
}

main();
