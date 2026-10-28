(function (global) {
  'use strict';
  function mount(host) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-process-mounted')) throw new Error('Use an unmounted process asset.');
    const controller = new AbortController();
    const options = { signal: controller.signal };
    const counter = host.querySelector('[data-process-count]');
    const pause = host.querySelector('[data-process-pause]');
    const status = host.querySelector('[data-process-status]');
    host.setAttribute('data-process-mounted', '');
    function play() {
      host.classList.remove('is-playing', 'is-paused');
      if (counter) counter.textContent = '1';
      pause.setAttribute('aria-pressed', 'false');
      void host.offsetWidth;
      host.classList.add('is-playing');
      status.textContent = 'Playing. Reduced motion keeps the example still.';
    }
    host.querySelector('[data-process-play]').addEventListener('click', play, options);
    pause.addEventListener('click', () => {
      const paused = host.classList.toggle('is-paused');
      pause.setAttribute('aria-pressed', String(paused));
      status.textContent = paused ? 'Motion paused.' : 'Motion resumed.';
    }, options);
    host.querySelector('[data-process-rate]').addEventListener('change', event => {
      host.style.setProperty('--flow-rate', event.target.value);
      play();
    }, options);
    if (counter) {
      const token = host.querySelector('.ltoken');
      token.addEventListener('animationiteration', () => {
        counter.textContent = String(Math.min(3, Number(counter.textContent) + 1));
      }, options);
      token.addEventListener('animationend', () => {
        counter.textContent = '3';
        status.textContent = 'Three iterations complete.';
      }, options);
    }
    return {
      play,
      destroy() {
        controller.abort();
        host.classList.remove('is-playing', 'is-paused');
        host.removeAttribute('data-process-mounted');
      },
    };
  }
  global.ProcessAssets = { mount };
  document.querySelectorAll('[data-process-asset]:not([data-process-mounted])').forEach(mount);
})(window);
