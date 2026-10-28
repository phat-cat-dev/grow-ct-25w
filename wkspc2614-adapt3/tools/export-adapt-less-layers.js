#!/usr/bin/env node
/**
 * export-adapt-less-layers.js
 *
 * Exports the Adapt core LESS layer and the adapt-contrib-vanilla theme LESS
 * layer as readable, labelled concatenations, plus a "combined" comparison
 * document that lines core and theme up module-by-module.
 *
 * For each selected layer this script produces:
 *   1. a plain concatenation  (headers only, original LESS untouched)
 *   2. a "tokenised" concatenation, where every real CSS declaration's
 *      VALUE is replaced with a generated custom-property style token:
 *
 *        <property>: --ad-<selector>-<property>-<core|vanilla>-<nnnnnn>;
 *        // <property>: <original value>;
 *
 *      <nnnnnn> is a 6-digit, zero-padded counter starting at 000001 for
 *      the first declaration in the document and incrementing once per
 *      declaration for the rest of that document (it is NOT reset
 *      between files/layers within the same output document).
 *
 * Usage, from the repo root:
 *   node tools/export-adapt-less-layers.js [--layers=core,vanilla,combined] [--no-tokens]
 *
 * Paths resolve from __dirname, not the pwd, so the repo root is found
 * whatever directory you invoke it from.
 *
 * Output (relative to the repo root):
 *   undlaf-intro_<yy><mm><dd>-<hh><mm><ss>/adapt-less-compiles/
 */

'use strict';

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..');
const CORE_LESS = path.join(REPO_ROOT, 'src/core/less');
const THEME_LESS = path.join(REPO_ROOT, 'src/theme/adapt-contrib-vanilla/less');

// ---------------------------------------------------------------------------
// File order - mirrors the order grunt/tasks/less.js feeds files to the LESS
// compiler: core/less/**/*.less (mandatory) first, then theme/**/*.less (src).
// ---------------------------------------------------------------------------

const CORE_ORDER = [
  '_browser/normalize.less',
  '_defaults/_variables.less',
  '_defaults/base.less',
  '_defaults/easing.less',
  '_defaults/icons.less',
  '_defaults/layout.less',
  '_defaults/utility.less',
  'core/accessibility.less',
  'core/article.less',
  'core/block.less',
  'core/button.less',
  'core/component.less',
  'core/drawer.less',
  'core/drawerItem.less',
  'core/global.less',
  'core/loading.less',
  'core/nav.less',
  'core/notify.less',
  'core/notifyPush.less',
  'core/page.less',
  'core/scrolling.less',
  'core/shadow.less',
  'core/tooltip.less',
  'core/transform.less',
  'core/transitions.less'
];

const THEME_ORDER = [
  '_defaults/_animations.less',
  '_defaults/_btn-mixins.less',
  '_defaults/_btn-style.less',
  '_defaults/_buttonMixins/_btn.less',
  '_defaults/_buttonMixins/_drawerItem.less',
  '_defaults/_buttonMixins/_drawerUI.less',
  '_defaults/_buttonMixins/_item.less',
  '_defaults/_buttonMixins/_itemUI.less',
  '_defaults/_buttonMixins/_menuItem.less',
  '_defaults/_buttonMixins/_navUI.less',
  '_defaults/_buttonMixins/_notifyBtn.less',
  '_defaults/_buttonMixins/_notifyUI.less',
  '_defaults/_colors.less',
  '_defaults/_font-config.less',
  '_defaults/_font-mixins.less',
  '_defaults/_spacing-config.less',
  '_defaults/_spacing-containers.less',
  '_defaults/blend.less',
  '_defaults/filter.less',
  'core/article.less',
  'core/attribution.less',
  'core/block.less',
  'core/button.less',
  'core/buttonQuestion.less',
  'core/component.less',
  'core/drawer.less',
  'core/drawerItem.less',
  'core/global.less',
  'core/loading.less',
  'core/nav.less',
  'core/notify.less',
  'core/notifyPush.less',
  'core/page.less',
  'core/shadow.less',
  'plugins/adapt-contrib-accordion/accordion.less',
  'plugins/adapt-contrib-assessmentResults/assessmentResults.less',
  'plugins/adapt-contrib-boxmenu/boxMenu.less',
  'plugins/adapt-contrib-boxmenu/boxMenuGroup.less',
  'plugins/adapt-contrib-boxmenu/boxMenuItem.less',
  'plugins/adapt-contrib-confidenceSlider/confidenceSlider.less',
  'plugins/adapt-contrib-glossary/glossary.less',
  'plugins/adapt-contrib-glossary/glossaryItem.less',
  'plugins/adapt-contrib-gmcq/gmcq.less',
  'plugins/adapt-contrib-graphic/graphic.less',
  'plugins/adapt-contrib-hotgraphic/hotgraphic.less',
  'plugins/adapt-contrib-hotgraphic/hotgraphicPopup.less',
  'plugins/adapt-contrib-languagePicker/languagePicker.less',
  'plugins/adapt-contrib-matching/dropdown.less',
  'plugins/adapt-contrib-matching/matching.less',
  'plugins/adapt-contrib-mcq/mcq.less',
  'plugins/adapt-contrib-media/media.less',
  'plugins/adapt-contrib-media/mep-legacy.less',
  'plugins/adapt-contrib-media/mep.less',
  'plugins/adapt-contrib-narrative/narrative.less',
  'plugins/adapt-contrib-pageLevelProgress/pageLevelProgressIndicator.less',
  'plugins/adapt-contrib-resources/resources.less',
  'plugins/adapt-contrib-slider/slider.less',
  'plugins/adapt-contrib-textInput/textinput.less',
  'plugins/adapt-contrib-trickle/trickle.less',
  'plugins/adapt-contrib-tutor/tutor.less',
  'project/columns.less',
  'project/theme-blocks.less',
  'project/theme-common.less',
  'project/theme-components.less',
  'project/theme-contentObjects.less'
];

// Groupings used only by the "combined" comparison document.
const FOUNDATION = [
  '_browser/normalize.less',
  '_defaults/_variables.less',
  '_defaults/base.less',
  '_defaults/easing.less',
  '_defaults/icons.less',
  '_defaults/layout.less',
  '_defaults/utility.less'
];
const PAIRS = ['article', 'block', 'button', 'component', 'drawer', 'drawerItem',
  'global', 'loading', 'nav', 'notify', 'notifyPush', 'page', 'shadow'];
const CORE_ONLY = ['accessibility', 'scrolling', 'tooltip', 'transform', 'transitions'];
const THEME_NEW_CORE = ['attribution', 'buttonQuestion'];
const THEME_DEFAULTS = THEME_ORDER.filter(f => f.startsWith('_defaults/'));
const THEME_PLUGINS = THEME_ORDER.filter(f => f.startsWith('plugins/'));
const THEME_PROJECT = THEME_ORDER.filter(f => f.startsWith('project/'));

// ---------------------------------------------------------------------------
// Tokeniser
//
// Walks LESS/CSS source char-by-char (quote-aware, comment-aware,
// paren-depth-aware) so that embedded ';' inside url()/strings/mixin-call
// arguments can't be mistaken for a declaration terminator. Only genuine
// `property: value;` declarations inside a rule body are tokenised; LESS
// variable assignments (@foo: bar;), mixin calls (.foo();), extends
// (&:extend(...);) and selectors/at-rules are left exactly as written.
// ---------------------------------------------------------------------------

function sanitizeToken(str) {
  const cleaned = String(str)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  return cleaned || 'x';
}

function transformDeclarations(text, layerLabel, counterRef) {
  const n = text.length;
  let i = 0;
  let pendingStart = 0;
  let parenDepth = 0;
  const out = [];
  // stack entries: { resolved, isAtRule, raw }
  const stack = [];

  const nearestSelector = () => {
    for (let k = stack.length - 1; k >= 0; k--) {
      if (!stack[k].isAtRule) return stack[k].resolved;
    }
    for (let k = stack.length - 1; k >= 0; k--) {
      if (stack[k].isAtRule) return stack[k].raw;
    }
    return 'root';
  };
  const nearestNonAtParentResolved = () => {
    for (let k = stack.length - 1; k >= 0; k--) {
      if (!stack[k].isAtRule) return stack[k].resolved;
    }
    return '';
  };

  const flushCopy = (end) => {
    if (end > pendingStart) out.push(text.slice(pendingStart, end));
    pendingStart = end;
  };

  while (i < n) {
    const c = text[i];

    if (c === '"' || c === "'") {
      const quote = c;
      i++;
      while (i < n && text[i] !== quote) {
        if (text[i] === '\\') i++;
        i++;
      }
      i++;
      continue;
    }

    if (c === '/' && text[i + 1] === '*') {
      // Flush up to and including the comment so pendingStart always sits
      // right after it. Without this, a comment between two declarations
      // (e.g. `font-size: 100%; /* 1 */\n  line-height: 1.15;`) stays glued
      // to the front of the NEXT declaration's captured text, the "starts
      // with a property name" regex below fails, and that declaration is
      // silently left untokenised.
      flushCopy(i);
      i += 2;
      while (i < n && !(text[i] === '*' && text[i + 1] === '/')) i++;
      i += 2;
      flushCopy(i);
      pendingStart = i;
      continue;
    }

    if (c === '/' && text[i + 1] === '/') {
      flushCopy(i);
      i += 2;
      while (i < n && text[i] !== '\n') i++;
      flushCopy(i);
      pendingStart = i;
      continue;
    }

    if (c === '(') { parenDepth++; i++; continue; }
    if (c === ')') { parenDepth--; i++; continue; }
    if (parenDepth > 0) { i++; continue; }

    if (c === '{') {
      const rawSelText = text.slice(pendingStart, i).trim();
      flushCopy(i + 1);
      // Strip comments, then strip any parenthesised groups (repeatedly, to
      // also catch nested parens) before using this text as a selector name.
      // Comments would otherwise leak into the token (e.g. the normalize.css
      // comment above `h1 { ... }` producing a token built from "Correct the
      // font size and margin on..." instead of "h1"). Parens would otherwise
      // drag an entire mixin parameter list into every declaration inside it
      // (e.g. `.img-zoom(@scale: 1.1; @duration: .75s; ...)` producing a
      // token built from "img-zoom-scale-1-1-duration-75s-..." instead of
      // just "img-zoom") - pseudo-class arguments like `:not(...)` are
      // stripped the same way, which is fine, the token only needs enough of
      // the selector to identify it, not reproduce it.
      let selText = rawSelText
        .replace(/\/\*[\s\S]*?\*\//g, '')
        .replace(/\/\/[^\n]*/g, '')
        .trim();
      let prevSelText;
      do {
        prevSelText = selText;
        selText = selText.replace(/\([^()]*\)/g, '');
      } while (selText !== prevSelText);
      selText = selText.replace(/\s+/g, ' ').trim();
      const isAtRule = selText.startsWith('@');
      let resolved = selText;
      if (!isAtRule && selText.includes('&')) {
        resolved = selText.split('&').join(nearestNonAtParentResolved());
      }
      stack.push({ resolved, isAtRule, raw: selText });
      pendingStart = i + 1;
      i++;
      continue;
    }

    if (c === '}') {
      flushCopy(i + 1);
      stack.pop();
      pendingStart = i + 1;
      i++;
      continue;
    }

    if (c === ';') {
      const stmt = text.slice(pendingStart, i);
      const trimmed = stmt.trim();
      const match = trimmed.match(/^(-{0,2}[A-Za-z][A-Za-z0-9-]*)\s*:\s*([\s\S]*)$/);

      if (match && stack.length > 0) {
        const property = match[1];
        const value = match[2].trim();
        const leadingWs = (stmt.match(/^\s*/) || [''])[0];
        const selTok = sanitizeToken(nearestSelector());
        const propTok = sanitizeToken(property);
        const num = String(counterRef.value++).padStart(6, '0');
        const token = `--ad-${selTok}-${propTok}-${layerLabel}-${num}`;
        out.push(`${leadingWs}${property}: ${token}; // ${property}: ${value};`);
      } else {
        out.push(stmt);
        out.push(';');
      }
      pendingStart = i + 1;
      i++;
      continue;
    }

    i++;
  }
  flushCopy(n);
  return out.join('');
}

// ---------------------------------------------------------------------------
// Builders
// ---------------------------------------------------------------------------

function readFile(base, rel) {
  return fs.readFileSync(path.join(base, rel), 'utf8');
}

function headerLine(label) {
  return `/* ===== ${label} ===== */\n`;
}
function noteLine(text) {
  return `/* ----- ${text} ----- */\n`;
}

function docPreamble(title, lines) {
  const body = lines.map(l => `   ${l}`).join('\n');
  return `/* =====================================================\n   ${title}\n   =====================================================\n\n${body}\n   ===================================================== */\n\n`;
}

function buildPlainConcat(base, fileList, title, preambleLines) {
  let out = docPreamble(title, preambleLines);
  for (const rel of fileList) {
    out += headerLine(rel);
    out += readFile(base, rel);
    out += '\n';
  }
  return out;
}

function buildTokenConcat(base, fileList, layerLabel, title, preambleLines) {
  let out = docPreamble(title, preambleLines);
  const counter = { value: 1 };
  for (const rel of fileList) {
    out += headerLine(rel);
    out += transformDeclarations(readFile(base, rel), layerLabel, counter);
    out += '\n';
  }
  return out;
}

function buildCombined(tokenised) {
  const counter = { value: 1 };
  const emit = (base, rel, layerLabel) => {
    const raw = readFile(base, rel);
    return headerLine(rel) + (tokenised ? transformDeclarations(raw, layerLabel, counter) : raw) + '\n';
  };

  let out = docPreamble('CORE vs VANILLA THEME - COMBINED COMPARISON VIEW', [
    'PURPOSE: pair up core/less and theme/adapt-contrib-vanilla/less files',
    'that share the same module name, so you can see exactly where the',
    'vanilla theme re-declares (and therefore overrides, via normal CSS',
    'cascade - same selector, later rule wins) a core module, versus where',
    'core has no theme equivalent at all and so runs completely unmodified.',
    '',
    'IMPORTANT - this is a COMPARISON AID, not the literal build order.',
    'The real Adapt build compiles ALL of src/core/less first (mandatory',
    'block), THEN ALL of src/theme/<theme>/less afterwards (src block).',
    'For the literal build-order output, read adapt-core-less-concat.less',
    'followed by adapt-vanilla-theme-less-concat.less.',
    '',
    tokenised
      ? 'TOKENISED VARIANT: every declaration value below has been replaced'
      : 'PLAIN VARIANT: declaration values below are exactly as authored.',
    tokenised
      ? 'with --ad-<selector>-<property>-<core|vanilla>-<nnnnnn>; the real'
      : '',
    tokenised
      ? 'value is preserved in the trailing // comment. Grep for "-core-"'
      : '',
    tokenised
      ? 'or "-vanilla-" to isolate which layer a given rule came from.'
      : '',
    '',
    'Sections: A core foundation (no theme equiv) | B core/theme pairs |',
    'C core-only modules | D theme-only new core/ files | E theme-only',
    'defaults | F theme-only plugin styling | G theme-only project layer'
  ]);

  out += docPreamble('SECTION A - CORE FOUNDATION (no same-named theme file)', []);
  for (const rel of FOUNDATION) {
    out += emit(CORE_LESS, rel, 'core');
  }

  out += docPreamble('SECTION B - CORE vs THEME PAIRS (same module name)', []);
  for (const name of PAIRS) {
    out += `/* ========== PAIR: ${name}.less ========== */\n`;
    out += noteLine('CORE VERSION - loaded first; stands unless the theme version below repeats the same selector');
    out += emit(CORE_LESS, `core/${name}.less`, 'core');
    out += noteLine('VANILLA THEME VERSION - loaded after core; overrides matching selectors, extends new ones, leaves the rest of core alone');
    out += emit(THEME_LESS, `core/${name}.less`, 'vanilla');
  }

  out += docPreamble('SECTION C - CORE ONLY (no matching theme file at all)', []);
  for (const name of CORE_ONLY) {
    out += emit(CORE_LESS, `core/${name}.less`, 'core');
  }

  out += docPreamble('SECTION D - THEME ONLY, NEW core/ FOLDER FILES', []);
  for (const name of THEME_NEW_CORE) {
    out += emit(THEME_LESS, `core/${name}.less`, 'vanilla');
  }

  out += docPreamble('SECTION E - THEME ONLY DEFAULTS (variables/mixins, no core equivalent)', []);
  for (const rel of THEME_DEFAULTS) {
    out += emit(THEME_LESS, rel, 'vanilla');
  }

  out += docPreamble('SECTION F - THEME ONLY PLUGIN STYLING (new components, no core equivalent)', []);
  for (const rel of THEME_PLUGINS) {
    out += emit(THEME_LESS, rel, 'vanilla');
  }

  out += docPreamble('SECTION G - THEME ONLY PROJECT LAYER (final override pass)', []);
  for (const rel of THEME_PROJECT) {
    out += emit(THEME_LESS, rel, 'vanilla');
  }

  return out;
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

function parseArgs(argv) {
  const opts = { layers: ['core', 'vanilla', 'combined'], tokens: true };
  for (const arg of argv) {
    if (arg.startsWith('--layers=')) {
      opts.layers = arg.slice('--layers='.length).split(',').map(s => s.trim()).filter(Boolean);
    } else if (arg === '--no-tokens') {
      opts.tokens = false;
    }
  }
  return opts;
}

function timestampFolderName() {
  const d = new Date();
  const pad = n => String(n).padStart(2, '0');
  const yy = pad(d.getFullYear() % 100);
  const mm = pad(d.getMonth() + 1);
  const dd = pad(d.getDate());
  const hh = pad(d.getHours());
  const mi = pad(d.getMinutes());
  const ss = pad(d.getSeconds());
  return `undlaf-intro_${yy}${mm}${dd}-${hh}${mi}${ss}`;
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  const outDir = path.join(REPO_ROOT, timestampFolderName(), 'adapt-less-compiles');
  fs.mkdirSync(outDir, { recursive: true });

  const written = [];
  const write = (name, content) => {
    const p = path.join(outDir, name);
    fs.writeFileSync(p, content, 'utf8');
    written.push(p);
  };

  if (opts.layers.includes('core')) {
    write('adapt-core-less-concat.less',
      buildPlainConcat(CORE_LESS, CORE_ORDER, 'ADAPT CORE LESS - FULL CONCATENATION',
        ['Build order: src/core/less/**/*.less (mandatory block)',
          'Source: grunt/config/less.js -> grunt/tasks/less.js']));
    if (opts.tokens) {
      write('adapt-core-less-concat.tokens.less',
        buildTokenConcat(CORE_LESS, CORE_ORDER, 'core', 'ADAPT CORE LESS - TOKENISED CONCATENATION',
          ['Every declaration value replaced with --ad-<selector>-<property>-core-<nnnnnn>;',
            'original value preserved in the trailing // comment.']));
    }
  }

  if (opts.layers.includes('vanilla')) {
    write('adapt-vanilla-theme-less-concat.less',
      buildPlainConcat(THEME_LESS, THEME_ORDER, 'ADAPT VANILLA THEME LESS - FULL CONCATENATION',
        ['Build order: src/theme/adapt-contrib-vanilla/**/*.less (src block, after core)',
          'Source: grunt/config/less.js -> grunt/tasks/less.js']));
    if (opts.tokens) {
      write('adapt-vanilla-theme-less-concat.tokens.less',
        buildTokenConcat(THEME_LESS, THEME_ORDER, 'vanilla', 'ADAPT VANILLA THEME LESS - TOKENISED CONCATENATION',
          ['Every declaration value replaced with --ad-<selector>-<property>-vanilla-<nnnnnn>;',
            'original value preserved in the trailing // comment.']));
    }
  }

  if (opts.layers.includes('combined')) {
    write('adapt-core-vs-vanilla-combined.less', buildCombined(false));
    if (opts.tokens) {
      write('adapt-core-vs-vanilla-combined.tokens.less', buildCombined(true));
    }
  }

  console.log(`Output folder: ${path.relative(REPO_ROOT, outDir)}`);
  for (const p of written) {
    const lines = fs.readFileSync(p, 'utf8').split('\n').length;
    console.log(`  ${path.relative(outDir, p)} (${lines} lines)`);
  }
}

main();
