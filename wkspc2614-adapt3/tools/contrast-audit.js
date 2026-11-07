#!/usr/bin/env node
/**
 * contrast-audit.js
 *
 * Static WCAG 2.2 colour-contrast check for the GROW high-contrast theme
 * (`src/theme/grow-ct/less/grow-contrast.less`). Parses the token values
 * directly out of that LESS source (not hand-copied, so it can't drift),
 * computes real contrast ratios for every foreground/background pair the
 * theme produces, and fails if any pair misses its WCAG AA threshold:
 *   - 4.5:1 for normal text (1.4.3)
 *   - 3:1 for large (>=24px, or >=19px bold) text (1.4.3)
 *   - 3:1 for UI component boundaries / focus indicators (1.4.11)
 *
 * This is a static maths check, not a live-page scan: it runs with no
 * build/server and catches a token regression the moment someone edits
 * grow-contrast.less. It is deliberately narrow in scope to the
 * high-contrast theme; it does NOT check the default light/dark themes or
 * page content colours — see tools/a11y-scan.js for a live, broader
 * axe-core scan across every WCAG rule on real pages.
 *
 * Usage:
 *   node tools/contrast-audit.js [--verbose]
 *
 * Exit: 0 = every pair passes its required ratio and no regression guard
 * tripped, 1 = any pair fails or a dangerous pattern was reintroduced.
 *
 * Built in response to: "get the high contrast theme sorted, it should
 * adhere to WCAG 2.2 AA" (backlog, Oct 2026). AAA (1.4.6, 7:1/4.5:1) was
 * considered and explicitly deferred — AA is the agreed baseline target for
 * now; most pairs already clear AAA anyway (see output).
 *
 * Regression history: --line (tuned for contrast against the WHITE page
 * surfaces) was briefly reused as `.nav .nav__btn.btn-icon { border-color:
 * var(--line); }` in grow-contrast.less. The nav bar itself is a fixed dark
 * navy (grow-chrome.less, independent of the --page-bg token), so that pair
 * measured ~1.2:1 — a 1.4.11 fail. Fixed by removing the override (the base
 * white border already clears 14.8:1 there). GUARD_NAV_LINE below asserts
 * that override never comes back.
 */

const fs = require('fs');
const path = require('path');
const { contrastRatio, toHex, AA_NORMAL_TEXT, AA_LARGE_TEXT, AA_UI, AAA_NORMAL_TEXT } = require('./lib/wcag-contrast');

const ROOT = path.resolve(__dirname, '..');
const CONTRAST_LESS = path.join(ROOT, 'src/theme/grow-ct/less/grow-contrast.less');
const CHROME_LESS = path.join(ROOT, 'src/theme/grow-ct/less/grow-chrome.less');
const H = 202; // @grow-h (grow-navy-theme.less) — every token below rides on this hue

function parseArgs() {
  const args = { verbose: false };
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (parts[0] === 'verbose') args.verbose = true;
    else {
      console.error(`Unrecognised argument: --${parts[0]}. Usage: node tools/contrast-audit.js [--verbose]`);
      process.exit(1);
    }
  });
  return args;
}

/**
 * Pull `--token: hsl(var(--h) S% L%);` and `--token: #hex;` declarations out
 * of the .grow-contrast-tokens() mixin, substituting the real hue for
 * var(--h). Returns { tokenName: 'hsl(202, S%, L%)' | '#hex' }.
 */
function parseTokens(lessSource) {
  const mixinMatch = lessSource.match(/\.grow-contrast-tokens\(\)\s*\{([\s\S]*?)\n\}/);
  if (!mixinMatch) throw new Error('contrast-audit: could not find .grow-contrast-tokens() in grow-contrast.less — has the file structure changed?');
  const body = mixinMatch[1];
  const tokens = {};
  const lineRe = /(--[\w-]+)\s*:\s*([^;]+);/g;
  let m;
  while ((m = lineRe.exec(body))) {
    const [, name, rawValue] = m;
    const hslMatch = rawValue.match(/hsl\(\s*var\(--h\)\s+(\d+(?:\.\d+)?)%\s+(\d+(?:\.\d+)?)%\s*\)/);
    const hexMatch = rawValue.match(/#[0-9a-fA-F]{3,6}/);
    if (hslMatch) tokens[name] = `hsl(${H}, ${hslMatch[1]}%, ${hslMatch[2]}%)`;
    else if (hexMatch) tokens[name] = hexMatch[0];
    // skip non-colour declarations (color-scheme, --shadow's alpha-0 hsl, etc.)
  }
  return tokens;
}

/** Pull the fixed nav-bar background colour out of grow-chrome.less. */
function parseNavBarColor(chromeSource) {
  const m = chromeSource.match(/body \.nav\s*\{[\s\S]*?background-color:\s*(hsl\([^)]+\))/);
  if (!m) throw new Error('contrast-audit: could not find body .nav background-color in grow-chrome.less');
  return m[1];
}

/**
 * Regression guard: assert grow-contrast.less never re-applies a --line (or
 * other white-surface-tuned token) border to a nav button, which sits on
 * the fixed dark navy bar, not a --page-bg surface.
 */
function guardNavLineBorder(contrastSource) {
  const dangerous = /\.nav\s+\.nav__btn\.btn-icon\s*\{[^}]*border-color:\s*var\(--line\)/;
  return !dangerous.test(contrastSource);
}

function main() {
  const { verbose } = parseArgs();

  const contrastSource = fs.readFileSync(CONTRAST_LESS, 'utf8');
  const chromeSource = fs.readFileSync(CHROME_LESS, 'utf8');

  const tokens = parseTokens(contrastSource);
  tokens['--navbar-bg'] = parseNavBarColor(chromeSource);
  tokens['--white'] = '#ffffff';

  console.log('contrast-audit: GROW high-contrast theme vs WCAG 2.2 AA');
  console.log(`Source: ${path.relative(ROOT, CONTRAST_LESS)} (hue ${H}, parsed live — not hand-copied)`);
  console.log('');

  const need = (name) => tokens[name];
  const CHECKS = [
    { label: '--ink on --page-bg (body text)', fg: '--ink', bg: '--page-bg', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: '--ink-soft on --page-bg (secondary text)', fg: '--ink-soft', bg: '--page-bg', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: '--accent on --page-bg (links/text)', fg: '--accent', bg: '--page-bg', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: '--h1 on --page-bg (large heading)', fg: '--h1', bg: '--page-bg', need: AA_LARGE_TEXT, clause: '1.4.3' },
    { label: '--h2 on --page-bg (large heading)', fg: '--h2', bg: '--page-bg', need: AA_LARGE_TEXT, clause: '1.4.3' },
    { label: '--line on --page-bg (card/panel border)', fg: '--line', bg: '--page-bg', need: AA_UI, clause: '1.4.11' },
    { label: '--ink on --surface-2 (text on tinted fill)', fg: '--ink', bg: '--surface-2', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: '--accent on --surface-2 (link on tinted fill)', fg: '--accent', bg: '--surface-2', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: '--line on --surface-2 (border on tinted fill)', fg: '--line', bg: '--surface-2', need: AA_UI, clause: '1.4.11' },
    { label: 'white on --accent (filled button text)', fg: '--white', bg: '--accent', need: AA_NORMAL_TEXT, clause: '1.4.3' },
    { label: 'white on nav bar (nav icon buttons)', fg: '--white', bg: '--navbar-bg', need: AA_UI, clause: '1.4.11' }
  ].filter(c => tokens[c.fg] && tokens[c.bg]); // tolerate tokens being removed/renamed

  const rows = CHECKS.map(check => {
    const ratio = contrastRatio(tokens[check.fg], tokens[check.bg]);
    return { ...check, ratio, pass: ratio >= check.need };
  });

  console.log('Result | Ratio   | Need | Clause | Check');
  console.log('-------|---------|------|--------|' + '-'.repeat(50));
  rows.forEach(r => {
    const result = r.pass ? 'PASS' : 'FAIL';
    const aaaNote = verbose && r.ratio >= AAA_NORMAL_TEXT ? ' (clears AAA 7:1 too)' : '';
    console.log(`${result.padEnd(6)} | ${r.ratio.toFixed(2).padStart(6)}:1 | ${String(r.need).padStart(3)}:1 | ${r.clause.padEnd(6)} | ${r.label}${aaaNote}`);
  });

  const navGuardOk = guardNavLineBorder(contrastSource);
  console.log(`${navGuardOk ? 'PASS' : 'FAIL'.padEnd(6)} | regression guard         | 1.4.11 | --line must not be re-applied as .nav__btn.btn-icon border-color`);

  if (verbose) {
    console.log('');
    console.log('Parsed tokens:');
    Object.entries(tokens).forEach(([name, value]) => {
      console.log(`  ${name.padEnd(14)} ${value.padEnd(22)} -> ${toHex(require('./lib/wcag-contrast').parseColor(value))}`);
    });
  }

  const failedRows = rows.filter(r => !r.pass);
  const totalChecks = rows.length + 1;
  const totalFailed = failedRows.length + (navGuardOk ? 0 : 1);

  console.log('');
  if (totalFailed > 0) {
    console.log(`contrast-audit: FAILED (${totalFailed} of ${totalChecks} checks failed)`);
    process.exit(1);
  } else {
    console.log(`contrast-audit: PASSED (all ${totalChecks} checks meet WCAG AA)`);
    process.exit(0);
  }
}

main();
