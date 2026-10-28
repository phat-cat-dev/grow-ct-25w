(function () {
  'use strict';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('.motion-card').forEach(card => {
    const svg = card.querySelector('svg');
    const play = card.querySelector('[data-play]');
    const status = card.querySelector('[data-status]');
    function setPlaying(playing) {
      const active = playing && !reduced.matches;
      svg.toggleAttribute('data-paused', !active);
      play.setAttribute('aria-pressed', String(active));
      play.textContent = active ? 'Pause' : 'Play';
      status.textContent = reduced.matches ? 'Static preview: reduced motion is enabled.' : active ? 'Playing' : 'Paused';
    }
    play.addEventListener('click', () => setPlaying(play.getAttribute('aria-pressed') !== 'true'));
    card.querySelector('[data-replay]').addEventListener('click', () => {
      svg.getAnimations({ subtree: true }).forEach(animation => { animation.currentTime = 0; });
      setPlaying(true);
    });
    for (const kind of ['speed', 'size', 'angle']) {
      const input = card.querySelector(`[data-${kind}]`);
      input.addEventListener('input', () => {
        const value = Number(input.value);
        if (kind === 'speed') svg.style.setProperty('--motion-speed', String(value));
        else svg.style.setProperty(`--preview-${kind}`, `${value}${kind === 'angle' ? 'deg' : ''}`);
        input.nextElementSibling.value = `${value}${kind === 'angle' ? ' degrees' : 'x'}`;
        input.setAttribute('aria-valuetext', input.nextElementSibling.value);
      });
    }
    reduced.addEventListener('change', () => setPlaying(false));
    setPlaying(false);
  });
})();
