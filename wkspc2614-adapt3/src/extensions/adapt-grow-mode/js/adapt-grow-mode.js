import Adapt from 'core/js/adapt';

/**
 * GROW Display Mode
 * --------------------------------------------------------------------------
 * Injects a "mode" button into the top-left of Adapt's nav bar. It opens a
 * small panel: Light / Dark / Contrast (sets data-theme on <html>), an
 * Animations toggle (data-motion="off") and a Backgrounds toggle
 * (data-bg="off"). The grow tokens (_grow-tokens.less) already respond to
 * data-theme; grow-mode.less handles data-motion, the bg-notebook page
 * textures and data-bg. Choices persist in localStorage and re-apply on load.
 *
 * bg-notebook: one grayscale notebook texture is painted on the PAGE GROUND
 * (body) so it sits behind every page template (menu, WRA-O, CONF, LESSON,
 * SUMMATIVE, WRA-C). Each page gets a weighted-random style (favouring lined;
 * grids read as analytical), stable per page for the session, UNLESS the page's
 * data object names one (`_growBg`, or an `nb-*` token in `_classes`).
 * Backgrounds are suppressed in high-contrast and when the toggle is off.
 */
const KEY_THEME = 'grow-mode-theme';
const KEY_MOTION = 'grow-mode-motion';
const KEY_BG = 'grow-mode-bg';
const MODES = [
  { id: 'light', label: 'Light', icon: 'light_mode' },
  { id: 'dark', label: 'Dark', icon: 'dark_mode' },
  { id: 'contrast', label: 'Contrast', icon: 'contrast' }
];
// weighted so lined turns up most; grids (quad/microgrid) suit analytical work
const NB_WEIGHTS = [['nb-lined', 3], ['nb-handwriting', 2], ['nb-legalpad', 2], ['nb-quad', 1.5], ['nb-hairlines', 1], ['nb-microgrid', 1]];
const NB_ALL = NB_WEIGHTS.map(w => w[0]);

class GrowMode {

  constructor() {
    this.mount = this.mount.bind(this);
    this._lastModel = null;
    this.restore();
    Adapt.on('menuView:ready pageView:ready', this.mount);
    // set the page-ground background on every page/menu as it readies
    Adapt.on('pageView:ready menuView:ready', (view) => {
      this._lastModel = (view && view.model) || null;
      this.setPageBg(this._lastModel);
    });
  }

  restore() {
    try {
      const t = localStorage.getItem(KEY_THEME);
      if (t) document.documentElement.setAttribute('data-theme', t);
      if (localStorage.getItem(KEY_MOTION) === 'off') document.documentElement.setAttribute('data-motion', 'off');
      if (localStorage.getItem(KEY_BG) === 'off') document.documentElement.setAttribute('data-bg', 'off');
    } catch (e) { /* storage unavailable */ }
  }

  mount() {
    const nav = document.querySelector('.nav__inner');
    if (!nav || nav.querySelector('.grow-mode')) return;

    const wrap = document.createElement('div');
    wrap.className = 'grow-mode';
    // data-order places this in the core nav's sort (sortNavigationButtons in
    // navigationView.js): negative = left-aligned, positive = right-aligned.
    // 95 sits just right of adapt-contrib-pageLevelProgress's completion icon
    // (default _navOrder 90) and just left of the drawer button (default 100).
    wrap.setAttribute('data-order', '95');
    wrap.innerHTML = `
      <button type="button" class="btn-icon nav__btn grow-mode__toggle" aria-haspopup="true" aria-expanded="false" aria-label="Display mode" title="Mode">
        <span class="grow-mode__icon" aria-hidden="true">contrast</span>
      </button>
      <div class="grow-mode__panel" role="menu" hidden>
        ${MODES.map(m => `<button type="button" class="grow-mode__opt" role="menuitemradio" data-mode="${m.id}"><span class="grow-mode__icon" aria-hidden="true">${m.icon}</span><span>${m.label}</span></button>`).join('')}
        <button type="button" class="grow-mode__opt grow-mode__motion" role="menuitemcheckbox"><span class="grow-mode__icon" aria-hidden="true">animation</span><span>Animations</span></button>
        <button type="button" class="grow-mode__opt grow-mode__bg" role="menuitemcheckbox"><span class="grow-mode__icon" aria-hidden="true">wallpaper</span><span>Backgrounds</span></button>
      </div>`;
    nav.appendChild(wrap);

    const toggle = wrap.querySelector('.grow-mode__toggle');
    const panel = wrap.querySelector('.grow-mode__panel');
    const setOpen = (open) => { panel.toggleAttribute('hidden', !open); toggle.setAttribute('aria-expanded', String(open)); };
    toggle.addEventListener('click', () => setOpen(panel.hasAttribute('hidden')));
    wrap.querySelectorAll('.grow-mode__opt[data-mode]').forEach(btn => btn.addEventListener('click', () => this.setTheme(btn.dataset.mode)));
    wrap.querySelector('.grow-mode__motion').addEventListener('click', () => this.toggleMotion());
    wrap.querySelector('.grow-mode__bg').addEventListener('click', () => this.toggleBg());
    document.addEventListener('click', (e) => { if (!wrap.contains(e.target)) setOpen(false); });
    this.reflect();
  }

  setTheme(id) {
    document.documentElement.setAttribute('data-theme', id);
    try { localStorage.setItem(KEY_THEME, id); } catch (e) {}
    this.setPageBg(this._lastModel); // contrast ⇒ no texture, others ⇒ restore it
    this.reflect();
  }

  toggleMotion() {
    const off = document.documentElement.getAttribute('data-motion') === 'off';
    if (off) document.documentElement.removeAttribute('data-motion');
    else document.documentElement.setAttribute('data-motion', 'off');
    try { localStorage.setItem(KEY_MOTION, off ? 'on' : 'off'); } catch (e) {}
    this.reflect();
  }

  toggleBg() {
    const html = document.documentElement;
    const off = html.getAttribute('data-bg') === 'off';
    if (off) html.removeAttribute('data-bg');
    else html.setAttribute('data-bg', 'off');
    try { localStorage.setItem(KEY_BG, off ? 'on' : 'off'); } catch (e) {}
    this.setPageBg(this._lastModel);
    this.reflect();
  }

  // ── bg-notebook ───────────────────────────────────────────────────────────
  pickNb() {
    const tot = NB_WEIGHTS.reduce((a, [, w]) => a + w, 0);
    let r = Math.random() * tot;
    for (const [k, w] of NB_WEIGHTS) { if ((r -= w) < 0) return k; }
    return NB_ALL[0];
  }

  // designer override first, else a stable weighted-random choice per page id
  nbFor(model) {
    if (model) {
      const pref = model.get('_growBg');
      if (NB_ALL.includes(pref)) return pref;
      const inClasses = (model.get('_classes') || '').split(/\s+/).find(c => NB_ALL.includes(c));
      if (inClasses) return inClasses;
    }
    const id = (model && model.get('_id')) || 'page';
    try {
      const map = JSON.parse(sessionStorage.getItem('grow-nb-map') || '{}');
      if (!map[id]) { map[id] = this.pickNb(); sessionStorage.setItem('grow-nb-map', JSON.stringify(map)); }
      return map[id];
    } catch (e) { return this.pickNb(); }
  }

  setPageBg(model) {
    const html = document.documentElement;
    NB_ALL.forEach(c => html.classList.remove(c));
    const off = html.getAttribute('data-bg') === 'off' || html.getAttribute('data-theme') === 'contrast';
    if (off) return;
    html.classList.add(this.nbFor(model));
  }

  reflect() {
    const theme = document.documentElement.getAttribute('data-theme') || 'light';
    const motionOff = document.documentElement.getAttribute('data-motion') === 'off';
    const bgOff = document.documentElement.getAttribute('data-bg') === 'off';
    document.querySelectorAll('.grow-mode').forEach(wrap => {
      wrap.querySelectorAll('.grow-mode__opt[data-mode]').forEach(b => b.setAttribute('aria-checked', String(b.dataset.mode === theme)));
      const mb = wrap.querySelector('.grow-mode__motion');
      if (mb) { mb.setAttribute('aria-checked', String(!motionOff)); mb.classList.toggle('is-off', motionOff); }
      const bb = wrap.querySelector('.grow-mode__bg');
      if (bb) { bb.setAttribute('aria-checked', String(!bgOff)); bb.classList.toggle('is-off', bgOff); }
    });
  }

}

export default new GrowMode();
