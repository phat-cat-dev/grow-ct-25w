/**
 * wcag-contrast.js
 *
 * Shared WCAG colour-contrast maths (relative luminance + contrast ratio,
 * per https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Accepts hex or
 * HSL input so callers can mirror the LESS tokens they're checking without
 * hand-converting colours first.
 *
 * Used by tools/contrast-audit.js (static theme-token check) and
 * tools/a11y-scan.js (live-page axe-core scan) so both tools agree on the
 * same thresholds and maths.
 */

const AA_NORMAL_TEXT = 4.5;
const AA_LARGE_TEXT = 3; // >=24px, or >=19px bold
const AA_UI = 3; // WCAG 1.4.11 non-text contrast (borders, icons, focus rings)
const AAA_NORMAL_TEXT = 7;
const AAA_LARGE_TEXT = 4.5;

function hexToRgb(hex) {
  const clean = hex.replace('#', '');
  const full = clean.length === 3
    ? clean.split('').map(c => c + c).join('')
    : clean;
  return [0, 2, 4].map(i => parseInt(full.substr(i, 2), 16) / 255);
}

function hslToRgb(h, s, l) {
  s /= 100; l /= 100;
  const c = (1 - Math.abs(2 * l - 1)) * s;
  const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
  const m = l - c / 2;
  let r, g, b;
  if (h < 60) [r, g, b] = [c, x, 0];
  else if (h < 120) [r, g, b] = [x, c, 0];
  else if (h < 180) [r, g, b] = [0, c, x];
  else if (h < 240) [r, g, b] = [0, x, c];
  else if (h < 300) [r, g, b] = [x, 0, c];
  else [r, g, b] = [c, 0, x];
  return [r + m, g + m, b + m];
}

/**
 * Parse a colour string: "#rrggbb", "#rgb", or "hsl(h, s%, l%)".
 * Returns [r, g, b] each in 0-1.
 */
function parseColor(input) {
  const s = String(input).trim();
  if (s.startsWith('#')) return hexToRgb(s);
  const m = s.match(/^hsla?\(\s*([\d.]+)\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%/i);
  if (m) return hslToRgb(parseFloat(m[1]), parseFloat(m[2]), parseFloat(m[3]));
  throw new Error(`parseColor: unrecognised colour format "${input}" (expected #hex or hsl(h, s%, l%))`);
}

function relativeLuminance([r, g, b]) {
  const f = (c) => (c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
}

/**
 * Contrast ratio between two colours (either as strings or pre-parsed [r,g,b]
 * 0-1 arrays). Returns a number >= 1.
 */
function contrastRatio(a, b) {
  const rgbA = Array.isArray(a) ? a : parseColor(a);
  const rgbB = Array.isArray(b) ? b : parseColor(b);
  const la = relativeLuminance(rgbA);
  const lb = relativeLuminance(rgbB);
  const lighter = Math.max(la, lb);
  const darker = Math.min(la, lb);
  return (lighter + 0.05) / (darker + 0.05);
}

function toHex([r, g, b]) {
  return '#' + [r, g, b].map(c => Math.round(c * 255).toString(16).padStart(2, '0')).join('');
}

module.exports = {
  AA_NORMAL_TEXT,
  AA_LARGE_TEXT,
  AA_UI,
  AAA_NORMAL_TEXT,
  AAA_LARGE_TEXT,
  parseColor,
  relativeLuminance,
  contrastRatio,
  toHex
};
