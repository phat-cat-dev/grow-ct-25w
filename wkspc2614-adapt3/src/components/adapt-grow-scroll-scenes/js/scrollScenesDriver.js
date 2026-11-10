/**
 * scrollScenesDriver.js
 *
 * The scroll-linked engine, ported from the original `scroll-scenes.patched.js`
 * study to an ES module. It is framework-agnostic: give it a host element that
 * contains [data-scroll-viewport] and [data-scroll-scene] blocks and it drives
 * the animation on scroll. The Adapt view mounts it in postRender and destroys
 * it in preRemove.
 *
 * What changed from the study:
 *  - IIFE / window.ScrollScenes global  ->  named export mountScrollScenes().
 *  - The per-scene maths now comes from scrollScenesLogic.js (unit-tested).
 *  - The two-line transition patch (STYLE-STRUCTURE.md s5.4) is folded in:
 *    --scene-offset / --scene-distance are written every frame, so the CSS
 *    transition models (rise, drift, tilt, wipe, stagger) work with no bridge.
 *
 * Still deliberately a JavaScript scroll-linked driver rather than requiring
 * CSS scroll-timeline support. No external libraries, fonts or network access.
 */

import {
  EFFECTS,
  sceneOffset,
  nearestIndex,
  scrollProgress,
  computeSceneStyles
} from './scrollScenesLogic';

const instances = new WeakMap();

/**
 * Mount the engine on a host element.
 *
 * @param {HTMLElement} host - the .scroll-scenes element
 * @param {{effect?:string, snap?:boolean}} [options]
 * @returns {{go:Function, set:Function, get:Function, destroy:Function}}
 */
export function mountScrollScenes(host, options = {}) {
  if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted scroll-scenes element.');
  const viewport = host.querySelector('[data-scroll-viewport]');
  const scenes = [...host.querySelectorAll('[data-scroll-scene]')];
  if (!viewport || !scenes.length) throw new Error('Scroll scenes require a viewport and at least one scene.');
  const contents = scenes.map(scene => scene.querySelector('[data-scene-content]'));
  if (contents.some(content => !content)) throw new Error('Each scene needs data-scene-content.');
  const savedStyles = contents.map(content => content.getAttribute('style'));
  const originalSnap = viewport.style.scrollSnapType;
  const controller = new AbortController();
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let effect = 'zoom';
  let snap = true;
  let frame = null;
  let destroyed = false;
  let active = -1;

  function reduced() {
    return motion.matches || !!host.closest('.no-motion, [data-tm-no-motion="true"]');
  }

  function render() {
    frame = null;
    const bounds = viewport.getBoundingClientRect();
    const center = bounds.top + viewport.clientTop + viewport.clientHeight / 2;
    const noMotion = reduced();
    const offsets = scenes.map(scene => {
      const rect = scene.getBoundingClientRect();
      return sceneOffset(rect.top + rect.height / 2, center, viewport.clientHeight);
    });
    const nearest = nearestIndex(offsets);
    scenes.forEach((scene, index) => {
      const content = contents[index];
      const styles = computeSceneStyles(offsets[index], effect, noMotion);
      content.style.setProperty('--scene-offset', styles['--scene-offset']);
      content.style.setProperty('--scene-distance', styles['--scene-distance']);
      content.style.opacity = styles.opacity;
      content.style.translate = styles.translate;
      content.style.scale = styles.scale;
      content.style.filter = styles.filter;
    });
    host.querySelectorAll('[data-scroll-to]').forEach(button => {
      if (Number(button.dataset.scrollTo) === nearest) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    const progress = host.querySelector('[data-scroll-progress]');
    if (progress) progress.value = scrollProgress(viewport.scrollTop, viewport.scrollHeight, viewport.clientHeight);
    if (active !== nearest) {
      active = nearest;
      const status = host.querySelector('[data-scroll-status]');
      if (status) status.textContent = `Scene ${active + 1} of ${scenes.length}`;
      host.dispatchEvent(new CustomEvent('scroll-scenes:change', { bubbles: true, detail: { index: active } }));
    }
  }

  function schedule() {
    if (!destroyed && frame === null) frame = requestAnimationFrame(render);
  }

  function set(value = {}) {
    if (destroyed) throw new Error('Scroll scenes have been destroyed.');
    const nextEffect = value.effect ?? effect;
    const nextSnap = value.snap ?? snap;
    if (!EFFECTS.includes(nextEffect)) throw new RangeError('Unknown scroll effect.');
    if (typeof nextSnap !== 'boolean') throw new TypeError('snap must be true or false.');
    effect = nextEffect;
    snap = nextSnap;
    viewport.style.scrollSnapType = snap ? 'y proximity' : 'none';
    schedule();
  }

  function go(index) {
    if (destroyed) throw new Error('Scroll scenes have been destroyed.');
    if (!Number.isInteger(index) || index < 0 || index >= scenes.length) throw new RangeError('Choose a valid zero-based scene index.');
    const bounds = viewport.getBoundingClientRect();
    const rect = scenes[index].getBoundingClientRect();
    viewport.scrollTo({
      top: viewport.scrollTop + rect.top - bounds.top - viewport.clientTop,
      behavior: reduced() ? 'instant' : 'smooth'
    });
  }

  set(options);
  viewport.addEventListener('scroll', schedule, { passive: true, signal: controller.signal });
  motion.addEventListener('change', schedule, { signal: controller.signal });
  host.addEventListener('click', event => {
    const button = event.target.closest('[data-scroll-to]');
    if (button && host.contains(button)) go(Number(button.dataset.scrollTo));
  }, { signal: controller.signal });
  viewport.addEventListener('focusin', event => {
    const index = scenes.findIndex(scene => scene.contains(event.target));
    if (index >= 0) {
      const bounds = viewport.getBoundingClientRect();
      viewport.scrollTop += scenes[index].getBoundingClientRect().top - bounds.top - viewport.clientTop;
      render();
    }
  }, { signal: controller.signal });
  const resize = new ResizeObserver(schedule);
  resize.observe(viewport);
  scenes.forEach(scene => resize.observe(scene));
  const preferences = new MutationObserver(schedule);
  for (let element = host; element; element = element.parentElement) {
    preferences.observe(element, { attributes: true, attributeFilter: ['class', 'data-tm-no-motion'] });
  }

  const api = {
    go,
    set,
    get: () => ({ index: active, effect, snap, count: scenes.length }),
    destroy() {
      destroyed = true;
      controller.abort();
      resize.disconnect();
      preferences.disconnect();
      if (frame !== null) cancelAnimationFrame(frame);
      contents.forEach((content, index) => {
        if (savedStyles[index] === null) content.removeAttribute('style');
        else content.setAttribute('style', savedStyles[index]);
      });
      viewport.style.scrollSnapType = originalSnap;
      instances.delete(host);
    }
  };
  instances.set(host, api);
  return api;
}
