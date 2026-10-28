(function (global) {
  'use strict';
  const instances = new WeakMap();
  function mount(host, options = {}) {
    if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted starfield element.');
    let settings = validate(options);
    function validate(value) {
      const next = { density: 180, speed: 1, paused: false, ...value };
      if (!Number.isInteger(next.density) || next.density < 20 || next.density > 500) throw new RangeError('density must be a whole number from 20 to 500.');
      if (!Number.isFinite(next.speed) || next.speed < .1 || next.speed > 3) throw new RangeError('speed must be between 0.1 and 3.');
      if (typeof next.paused !== 'boolean') throw new TypeError('paused must be true or false.');
      return next;
    }
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    const canvas = document.createElement('canvas');
    canvas.className = 'starfield-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    host.prepend(canvas);
    const context = canvas.getContext('2d');
    if (!context) { canvas.remove(); throw new Error('A 2D canvas is required for this starfield.'); }
    const abort = new AbortController();
    let width = 1, height = 1, frame = null, last = null, destroyed = false, visible = true;
    let stars = [];
    function generate() {
      stars = Array.from({ length: settings.density }, () => ({
        x: Math.random(), y: Math.random(), depth: Math.floor(Math.random() * 3),
      }));
    }
    function reduced() { return motion.matches || !!host.closest('.no-motion, [data-tm-no-motion="true"]'); }
    function moving() { return !settings.paused && !reduced() && !document.hidden && visible; }
    function draw(delta = 0) {
      context.clearRect(0, 0, width, height);
      context.fillStyle = getComputedStyle(host).getPropertyValue('--star-colour').trim() || '#f4f8ff';
      for (const star of stars) {
        if (delta) star.y = (star.y - delta * settings.speed * (star.depth + 1) * .012 + 1) % 1;
        context.globalAlpha = .35 + star.depth * .28;
        context.beginPath();
        context.arc(star.x * width, star.y * height, .65 + star.depth * .55, 0, Math.PI * 2);
        context.fill();
      }
      context.globalAlpha = 1;
    }
    function tick(time) {
      frame = null;
      if (destroyed) return;
      const delta = last === null ? 0 : Math.min((time - last) / 1000, .05);
      last = time;
      draw(moving() ? delta : 0);
      if (moving()) frame = requestAnimationFrame(tick);
      else last = null;
    }
    function sync() {
      if (frame !== null) cancelAnimationFrame(frame);
      frame = null; last = null;
      draw();
      if (!destroyed && moving()) frame = requestAnimationFrame(tick);
    }
    function resize() {
      width = Math.max(1, host.clientWidth); height = Math.max(1, host.clientHeight);
      const ratio = Math.min(devicePixelRatio || 1, 2);
      canvas.width = Math.round(width * ratio); canvas.height = Math.round(height * ratio);
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
      sync();
    }
    const resizeObserver = new ResizeObserver(resize);
    const preferences = new MutationObserver(sync);
    const visibility = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); });
    generate(); resize();
    resizeObserver.observe(host); visibility.observe(host);
    for (let element = host; element; element = element.parentElement) {
      preferences.observe(element, { attributes: true, attributeFilter: ['class', 'style', 'data-tm-no-motion'] });
    }
    motion.addEventListener('change', sync, { signal: abort.signal });
    document.addEventListener('visibilitychange', sync, { signal: abort.signal });
    const api = {
      get: () => ({ ...settings }),
      set(value) {
        if (destroyed) throw new Error('This starfield has been destroyed.');
        const next = validate({ ...settings, ...value });
        const changed = next.density !== settings.density;
        settings = next;
        if (changed) generate();
        sync();
      },
      shuffle() {
        if (destroyed) throw new Error('This starfield has been destroyed.');
        generate(); sync();
      },
      destroy() {
        destroyed = true;
        if (frame !== null) cancelAnimationFrame(frame);
        abort.abort(); resizeObserver.disconnect(); preferences.disconnect(); visibility.disconnect();
        canvas.remove(); instances.delete(host);
      },
    };
    instances.set(host, api);
    return api;
  }
  global.Starfield = { mount };
})(window);
