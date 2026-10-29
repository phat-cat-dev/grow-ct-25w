import Adapt from 'core/js/adapt';

/**
 * GROW Display Mode
 * --------------------------------------------------------------------------
 * Injects a "mode" button into the top-left of Adapt's nav bar. It opens a
 * small panel: Light / Dark / Contrast (sets data-theme on <html>) and an
 * Animations toggle (sets data-motion="off"). The grow tokens
 * (_grow-tokens.less) already respond to data-theme; grow-mode.less handles
 * data-motion. Choices persist in localStorage and are re-applied on load.
 */
const KEY_THEME = 'grow-mode-theme';
const KEY_MOTION = 'grow-mode-motion';
const MODES = [
  { id: 'light', label: 'Light', icon: 'light_mode' },
  { id: 'dark', label: 'Dark', icon: 'dark_mode' },
  { id: 'contrast', label: 'Contrast', icon: 'contrast' }
];

class GrowMode {

  constructor() {
    this.mount = this.mount.bind(this);
    this.restore();
    Adapt.on('menuView:ready pageView:ready', this.mount);
  }

  restore() {
    try {
      const t = localStorage.getItem(KEY_THEME);
      if (t) document.documentElement.setAttribute('data-theme', t);
      if (localStorage.getItem(KEY_MOTION) === 'off') document.documentElement.setAttribute('data-motion', 'off');
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
    // Without this the button defaulted to order 0 and was force-inserted at
    // nav.firstChild, landing beside/under the skip-navigation button
    // (_navOrder -100, position:absolute left:0 on focus — see nav.less).
    wrap.setAttribute('data-order', '95');
    wrap.innerHTML = `
      <button type="button" class="btn-icon nav__btn grow-mode__toggle" aria-haspopup="true" aria-expanded="false" aria-label="Display mode" title="Mode">
        <span class="grow-mode__icon" aria-hidden="true">contrast</span>
      </button>
      <div class="grow-mode__panel" role="menu" hidden>
        ${MODES.map(m => `<button type="button" class="grow-mode__opt" role="menuitemradio" data-mode="${m.id}"><span class="grow-mode__icon" aria-hidden="true">${m.icon}</span><span>${m.label}</span></button>`).join('')}
        <button type="button" class="grow-mode__opt grow-mode__motion" role="menuitemcheckbox"><span class="grow-mode__icon" aria-hidden="true">animation</span><span>Animations</span></button>
      </div>`;
    nav.appendChild(wrap);

    const toggle = wrap.querySelector('.grow-mode__toggle');
    const panel = wrap.querySelector('.grow-mode__panel');
    const setOpen = (open) => { panel.toggleAttribute('hidden', !open); toggle.setAttribute('aria-expanded', String(open)); };
    toggle.addEventListener('click', () => setOpen(panel.hasAttribute('hidden')));
    wrap.querySelectorAll('.grow-mode__opt[data-mode]').forEach(btn => btn.addEventListener('click', () => this.setTheme(btn.dataset.mode)));
    wrap.querySelector('.grow-mode__motion').addEventListener('click', () => this.toggleMotion());
    document.addEventListener('click', (e) => { if (!wrap.contains(e.target)) setOpen(false); });
    this.reflect();
  }

  setTheme(id) {
    document.documentElement.setAttribute('data-theme', id);
    try { localStorage.setItem(KEY_THEME, id); } catch (e) {}
    this.reflect();
  }

  toggleMotion() {
    const off = document.documentElement.getAttribute('data-motion') === 'off';
    if (off) document.documentElement.removeAttribute('data-motion');
    else document.documentElement.setAttribute('data-motion', 'off');
    try { localStorage.setItem(KEY_MOTION, off ? 'on' : 'off'); } catch (e) {}
    this.reflect();
  }

  reflect() {
    const theme = document.documentElement.getAttribute('data-theme') || 'light';
    const motionOff = document.documentElement.getAttribute('data-motion') === 'off';
    document.querySelectorAll('.grow-mode').forEach(wrap => {
      wrap.querySelectorAll('.grow-mode__opt[data-mode]').forEach(b => b.setAttribute('aria-checked', String(b.dataset.mode === theme)));
      const mb = wrap.querySelector('.grow-mode__motion');
      if (mb) { mb.setAttribute('aria-checked', String(!motionOff)); mb.classList.toggle('is-off', motionOff); }
    });
  }

}

export default new GrowMode();
