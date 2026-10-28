(function (global) {
  'use strict';
  const instances = new WeakMap();
  function mount(host, options = {}) {
    if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted fade-in section.');
    if (!host.querySelector('[data-fade-item]')) throw new Error('The fade-in section needs data-fade-item elements.');
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    const controller = new AbortController();
    let animations = [], observer = null, destroyed = false, generation = 0;
    let settings = validate(options);
    function validate(value) {
      const next = { duration: 650, stagger: 160, distance: 18, effect: 'rise', cardGap: null, ...value };
      for (const [key, min, max] of [['duration', 100, 2000], ['stagger', 0, 1000], ['distance', 0, 60]]) {
        if (!Number.isFinite(next[key]) || next[key] < min || next[key] > max) {
          throw new RangeError(`${key} must be a number from ${min} to ${max}.`);
        }
      }
      if (!['fade', 'rise', 'left', 'right', 'zoom'].includes(next.effect)) throw new RangeError('Unknown transition effect.');
      if (next.cardGap !== null && (!Number.isFinite(next.cardGap) || next.cardGap < 0 || next.cardGap > 10000)) {
        throw new RangeError('cardGap must be null or a number from 0 to 10000.');
      }
      return next;
    }
    function reduced() {
      return motion.matches || !!host.closest('.no-motion, [data-tm-no-motion="true"]');
    }
    function show() {
      generation++;
      observer?.disconnect();
      animations.forEach(animation => animation.cancel());
      animations = [];
    }
    async function play() {
      if (destroyed) throw new Error('This fade-in section has been destroyed.');
      show();
      const current = generation;
      if (!reduced() && typeof host.animate === 'function') {
        const items = [...host.querySelectorAll('[data-fade-item]')];
        let cardIndex = 0;
        const firstCard = items.findIndex(item => item.matches('.fade-grid > li'));
        const introCount = firstCard < 0 ? items.length : firstCard;
        const start = { opacity: 0 };
        const end = { opacity: 1 };
        if (settings.effect === 'rise') { start.translate = `0 ${settings.distance}px`; end.translate = '0 0'; }
        if (settings.effect === 'left') { start.translate = `-${settings.distance}px 0`; end.translate = '0 0'; }
        if (settings.effect === 'right') { start.translate = `${settings.distance}px 0`; end.translate = '0 0'; }
        if (settings.effect === 'zoom') { start.scale = .94; end.scale = 1; }
        animations = items.map((item, index) => {
          let delay = index * settings.stagger;
          if (settings.cardGap !== null && item.matches('.fade-grid > li')) {
            const introEnd = introCount ? (introCount - 1) * settings.stagger + settings.duration : 0;
            delay = introEnd + cardIndex++ * (settings.duration + settings.cardGap);
          }
          return item.animate([start, end], {
            duration: settings.duration, delay,
            easing: 'cubic-bezier(.2,.65,.3,1)', fill: 'backwards',
          });
        });
        try { await Promise.all(animations.map(animation => animation.finished)); }
        catch (error) { if (error.name !== 'AbortError') throw error; }
      }
      if (destroyed || generation !== current) return;
      show();
      host.dispatchEvent(new CustomEvent('fade-in:complete', { bubbles: true }));
    }
    function start() {
      play().catch(error => {
        show();
        host.dispatchEvent(new CustomEvent('fade-in:error', { bubbles: true, detail: error }));
        console.error('Fade-in playback failed:', error);
      });
    }
    motion.addEventListener('change', () => { if (reduced()) show(); }, { signal: controller.signal });
    host.addEventListener('focusin', show, { signal: controller.signal });
    const preferenceObserver = new MutationObserver(() => { if (reduced()) show(); });
    for (let parent = host; parent; parent = parent.parentElement) {
      preferenceObserver.observe(parent, { attributes: true, attributeFilter: ['class', 'data-tm-no-motion'] });
    }
    const api = {
      play,
      show,
      set(value) { settings = validate({ ...settings, ...value }); },
      destroy() {
        show(); destroyed = true; observer?.disconnect(); preferenceObserver.disconnect();
        controller.abort(); instances.delete(host);
      },
    };
    instances.set(host, api);
    if (options.trigger !== 'manual') {
      if (typeof IntersectionObserver === 'function') {
        observer = new IntersectionObserver(entries => {
          if (entries.some(entry => entry.isIntersecting)) { observer.disconnect(); start(); }
        }, { threshold: 0.1 });
        observer.observe(host);
      } else start();
    }
    return api;
  }
  global.FadeInCards = { mount };
})(window);
