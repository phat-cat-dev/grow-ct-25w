/**
 * ab-theme-switcher — a removable, dev/preview overlay for trying the colour
 * theme packs and light/dark live, without rebuilding.
 *
 * WHAT IT DOES
 *   Floating panel (bottom-right) that switches:
 *     - the colour theme PACK  (base / dark-blue / dark-grey / dark-blue-grey)
 *       by swapping the cm-theme-<name> class on <html>; and
 *     - the LIGHT/DARK version  by setting data-theme on <html> (which overrides
 *       ab-force-light and the OS preference, so it previews either version of
 *       any pack regardless of the course's committed _htmlClasses).
 *   The choice is remembered in localStorage so it survives reloads.
 *
 * HOW TO TURN IT ON (it is OFF by default, so students never see it):
 *   - add the class `cm-theme-switch` to the course config.json `_htmlClasses`, OR
 *   - append `?cm-theme-switch` (or `#cm-theme-switch`) to the preview URL.
 *
 * HOW TO REMOVE IT ENTIRELY
 *   Delete the one import line in adapt-ab-theme.js (and this file). It adds
 *   nothing to a build where the flag is absent, and nothing at all once the
 *   import is gone. It is pure dev furniture — not part of the course.
 */

const PACKS = [
  { id: '', label: 'Base' },
  { id: 'dark-blue', label: 'Dark blue' },
  { id: 'dark-grey', label: 'Dark grey' },
  { id: 'dark-blue-grey', label: 'Blue + grey' }
];
const PACK_CLASSES = PACKS.filter(p => p.id).map(p => `cm-theme-${p.id}`);
const LS_KEY = 'cmThemeSwitch';

function enabled() {
  try {
    const q = window.location.search + ' ' + window.location.hash;
    if (/cm-theme-switch/.test(q)) return true;
  } catch (e) { /* ignore */ }
  return document.documentElement.classList.contains('cm-theme-switch');
}

function currentPack() {
  for (const c of PACK_CLASSES) {
    if (document.documentElement.classList.contains(c)) return c.replace('cm-theme-', '');
  }
  return '';
}

function applyPack(id) {
  const root = document.documentElement;
  PACK_CLASSES.forEach(c => root.classList.remove(c));
  if (id) root.classList.add(`cm-theme-${id}`);
}

function applyMode(mode) {
  // explicit data-theme wins over ab-force-light and the OS setting, so either
  // version previews on demand.
  document.documentElement.setAttribute('data-theme', mode);
}

function save(pack, mode) {
  try { localStorage.setItem(LS_KEY, JSON.stringify({ pack, mode })); } catch (e) { /* ignore */ }
}
function load() {
  try { return JSON.parse(localStorage.getItem(LS_KEY) || 'null'); } catch (e) { return null; }
}

function build() {
  if (document.getElementById('ab-theme-switcher')) return; // once
  // restore a saved choice, else read what the page already has
  const saved = load();
  let pack = saved ? saved.pack : currentPack();
  let mode = saved
    ? saved.mode
    : (document.documentElement.getAttribute('data-theme') ||
       (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches &&
           !document.documentElement.classList.contains('ab-force-light')
         ? 'dark'
         : 'light'));
  applyPack(pack); applyMode(mode); save(pack, mode);

  const style = document.createElement('style');
  style.textContent = `
    #ab-theme-switcher{position:fixed;right:16px;bottom:16px;z-index:99999;
      font:13px/1.3 system-ui,sans-serif;background:#fff;color:#1a1a1a;
      border:1px solid #ccc;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.22);
      padding:10px 12px;max-width:220px;user-select:none}
    #ab-theme-switcher.cmts-min{padding:0}
    #ab-theme-switcher .cmts-h{display:flex;align-items:center;justify-content:space-between;
      gap:8px;font-weight:600;margin-bottom:8px;cursor:pointer}
    #ab-theme-switcher.cmts-min .cmts-h{margin:0;padding:8px 10px}
    #ab-theme-switcher.cmts-min .cmts-body{display:none}
    #ab-theme-switcher .cmts-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
    #ab-theme-switcher button.cmts-opt{flex:1 1 auto;min-width:64px;padding:6px 8px;
      border:1px solid #ccc;border-radius:7px;background:#f3f3f3;color:#1a1a1a;cursor:pointer}
    #ab-theme-switcher button.cmts-opt[aria-pressed="true"]{background:#0a2a3d;color:#fff;border-color:#0a2a3d}
    #ab-theme-switcher .cmts-lbl{font-size:11px;text-transform:uppercase;letter-spacing:.04em;
      opacity:.6;margin:2px 0 4px}
    #ab-theme-switcher .cmts-x{border:0;background:none;font-size:16px;line-height:1;cursor:pointer;color:inherit}
  `;
  document.head.appendChild(style);

  const el = document.createElement('div');
  el.id = 'ab-theme-switcher';
  el.setAttribute('role', 'region');
  el.setAttribute('aria-label', 'Theme preview switcher');
  el.innerHTML = `
    <div class="cmts-h"><span>Theme preview</span><button class="cmts-x" title="collapse" aria-label="collapse">–</button></div>
    <div class="cmts-body">
      <div class="cmts-lbl">Colour pack</div>
      <div class="cmts-row cmts-packs">${PACKS.map(p =>
    `<button class="cmts-opt" data-pack="${p.id}">${p.label}</button>`).join('')}</div>
      <div class="cmts-lbl">Mode</div>
      <div class="cmts-row cmts-modes">
        <button class="cmts-opt" data-mode="light">Light</button>
        <button class="cmts-opt" data-mode="dark">Dark</button>
      </div>
    </div>`;
  document.body.appendChild(el);

  const paint = () => {
    el.querySelectorAll('[data-pack]').forEach(b =>
      b.setAttribute('aria-pressed', String(b.dataset.pack === pack)));
    el.querySelectorAll('[data-mode]').forEach(b =>
      b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
  };
  paint();

  el.querySelector('.cmts-packs').addEventListener('click', e => {
    const b = e.target.closest('[data-pack]'); if (!b) return;
    pack = b.dataset.pack; applyPack(pack); save(pack, mode); paint();
  });
  el.querySelector('.cmts-modes').addEventListener('click', e => {
    const b = e.target.closest('[data-mode]'); if (!b) return;
    mode = b.dataset.mode; applyMode(mode); save(pack, mode); paint();
  });
  el.querySelector('.cmts-h').addEventListener('click', e => {
    if (e.target.closest('[data-pack],[data-mode]')) return;
    el.classList.toggle('cmts-min');
  });
}

export default function initThemeSwitcher() {
  if (!enabled()) return;
  if (document.body) build();
  else document.addEventListener('DOMContentLoaded', build, { once: true });
}
