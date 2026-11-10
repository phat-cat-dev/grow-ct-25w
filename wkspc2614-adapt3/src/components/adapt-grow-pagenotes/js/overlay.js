/**
 * overlay.js — the transparent page-notes overlay (DOM, no React; the scenario
 * mountPlayer pattern). It builds a position:fixed layer matched to a target
 * region's box, draws authored notes on at x%/y% positions, and cleans up on
 * close. The layer is transparent and pointer-events:none except on the notes
 * and the controls, so the underlying content stays visible AND usable — this is
 * an overlay, not a modal (aria-modal="false", role="group", no focus trap).
 *
 * Two note vocabularies, both reusing the existing draw-on engines:
 *   - ink marks  → engine.instanceMarkup (the adapt-grow-animations catalogue)
 *   - chalk      → ChalkLabels.render     (the chalk-patterns diagram library)
 */
import growLayer from 'extensions/adapt-grow-layer/js/adapt-grow-layer';
import { instanceMarkup, baseCss, INK_FILTER_SVG } from './libs/engine';
import ChalkLabels from './libs/chalk-labels';
import chalkCss from './libs/chalk-css';

// A note's colour role → the GROW theme token the chalk strokes should follow.
// (Ink marks take the role directly through the engine's own --am-c-* tokens.)
const ROLE_VAR = {
  accent: '--accent', positive: '--c-positive', negative: '--c-negative',
  neutral: '--c-neutral', comment: '--c-comment', pen: '--pen', ink: '--ink'
};

const clampPct = value => Math.max(0, Math.min(100, Number(value) || 0));

function prefersReducedMotion() {
  try {
    if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return true;
  } catch (e) { /* ignore */ }
  return document.documentElement.classList.contains('no-motion') ||
    document.documentElement.hasAttribute('data-tm-no-motion');
}

// The marks stylesheet (am-* classes/tokens) and the hand-drawn ink filter are
// global and shared; add each once per page.
function injectAssetsOnce() {
  if (typeof document === 'undefined') return;
  if (!document.getElementById('grow-pagenotes-marks-css')) {
    const style = document.createElement('style');
    style.id = 'grow-pagenotes-marks-css';
    style.textContent = baseCss();
    document.head.appendChild(style);
  }
  if (!document.getElementById('grow-pagenotes-chalk-css')) {
    const style = document.createElement('style');
    style.id = 'grow-pagenotes-chalk-css';
    style.textContent = chalkCss;
    document.head.appendChild(style);
  }
  if (!document.getElementById('am-ink')) {
    document.body.insertAdjacentHTML('beforeend', INK_FILTER_SVG);
  }
}

function buildNote(note) {
  const el = document.createElement('div');
  el.className = `grow-pagenotes__note grow-pagenotes__note--${note._type || 'mark'}`;
  el.style.left = `${clampPct(note.x)}%`;
  el.style.top = `${clampPct(note.y)}%`;
  if (note._color && ROLE_VAR[note._color]) {
    el.style.setProperty('--chalk-color', `var(${ROLE_VAR[note._color]})`);
    el.style.color = `var(${ROLE_VAR[note._color]})`;
  }
  try {
    if (note._type === 'chalk') {
      const host = document.createElement('div');
      host.className = 'grow-pagenotes__chalk';
      el.appendChild(host);
      el._chalkSvg = ChalkLabels.render(host, {
        pattern: note._pattern,
        mode: 'svg',
        data: note.data || {}
      });
    } else {
      el.innerHTML = instanceMarkup(note._markId, {
        text: note.text,
        over: note.over,
        color: note._color,
        speed: note._speed,
        scale: note._scale,
        rotation: note._rotation,
        repeats: note._repeats,
        jitter: note._jitter,
        play: true
      });
    }
  } catch (e) {
    return null; // unknown mark id / pattern — skip rather than break the overlay
  }
  return el;
}

export function mountOverlay(targetEl, notes, opts = {}) {
  const { reveal = 'stepped', scrim = 'none', ariaLabel = 'Page notes', returnFocusTo = null } = opts;
  injectAssetsOnce();
  const reduced = prefersReducedMotion();

  const root = document.createElement('div');
  root.className = 'grow-pagenotes__overlay';
  root.setAttribute('role', 'group');
  root.setAttribute('aria-label', ariaLabel);
  root.setAttribute('aria-modal', 'false');
  root.dataset.scrim = scrim;
  root.tabIndex = -1;
  // Mount into the shared GROW overlay stage (one stacking context for every GROW
  // overlay) rather than straight onto <body>. `root` stays position:fixed and the
  // stage carries no transform, so the getBoundingClientRect math below is unchanged.
  growLayer.overlay().appendChild(root);

  // Keep the fixed layer matched to the (scrolling, resizing) target region.
  let frame = 0;
  const position = () => {
    const r = (targetEl || document.body).getBoundingClientRect();
    root.style.left = `${r.left}px`;
    root.style.top = `${r.top}px`;
    root.style.width = `${r.width}px`;
    root.style.height = `${r.height}px`;
  };
  const schedulePosition = () => {
    if (frame) return;
    frame = requestAnimationFrame(() => { frame = 0; position(); });
  };
  position();

  // Build the note elements, grouped by step for sequential reveal.
  const els = notes.map(buildNote).map((el, i) => ({ el, step: Number(notes[i].step) || 0 })).filter(n => n.el);
  const steps = [...new Set(els.map(n => n.step))].sort((a, b) => a - b);

  const show = group => group.forEach(({ el }) => {
    root.appendChild(el);
    if (el._chalkSvg && !reduced) ChalkLabels.play(el._chalkSvg);
  });

  // Controls (pointer-events re-enabled; the rest of the layer stays click-through).
  const controls = document.createElement('div');
  controls.className = 'grow-pagenotes__controls';
  const nextBtn = document.createElement('button');
  nextBtn.type = 'button';
  nextBtn.className = 'grow-pagenotes__btn grow-pagenotes__btn--next';
  nextBtn.textContent = 'Next';
  const closeBtn = document.createElement('button');
  closeBtn.type = 'button';
  closeBtn.className = 'grow-pagenotes__btn grow-pagenotes__btn--close';
  closeBtn.textContent = 'Close';
  closeBtn.setAttribute('aria-label', 'Close the notes');

  const stepped = reveal === 'stepped' && !reduced && steps.length > 1;
  let cursor = 0;
  const revealStep = () => show(els.filter(n => n.step === steps[cursor]));
  const advance = () => {
    cursor += 1;
    if (cursor >= steps.length) return;
    revealStep();
    if (cursor >= steps.length - 1) nextBtn.remove();
  };

  if (stepped) {
    nextBtn.addEventListener('click', advance);
    controls.append(nextBtn, closeBtn);
    revealStep(); // first group visible on open
  } else {
    // "all" or reduced motion: show everything at once.
    show(els);
    controls.append(closeBtn);
  }
  root.appendChild(controls);

  // a11y lifecycle: focus a control on open, Escape closes, focus returns on close.
  const onKey = e => { if (e.key === 'Escape') { e.preventDefault(); destroy(); } };
  function destroy() {
    if (!root.isConnected) return;
    cancelAnimationFrame(frame);
    window.removeEventListener('resize', schedulePosition, true);
    window.removeEventListener('scroll', schedulePosition, true);
    document.removeEventListener('keydown', onKey, true);
    observer?.disconnect();
    root.remove();
    returnFocusTo?.focus?.();
  }
  closeBtn.addEventListener('click', destroy);
  document.addEventListener('keydown', onKey, true);
  window.addEventListener('resize', schedulePosition, true);
  window.addEventListener('scroll', schedulePosition, true);
  let observer = null;
  if (typeof ResizeObserver !== 'undefined' && targetEl) {
    observer = new ResizeObserver(schedulePosition);
    observer.observe(targetEl);
  }
  (stepped ? nextBtn : closeBtn).focus({ preventScroll: true });

  return { destroy, focus: () => closeBtn.focus({ preventScroll: true }) };
}
