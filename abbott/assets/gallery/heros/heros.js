(function () {
  'use strict';
  const dotsHeroes = document.querySelectorAll('.asset-hero--dots');
  if (dotsHeroes.length) {
    let idleTimer;
    const onInteraction = () => {
      dotsHeroes.forEach(hero => {
        hero.dataset.heroInteracting = 'true';
      });
      clearTimeout(idleTimer);
      idleTimer = setTimeout(() => {
        dotsHeroes.forEach(hero => {
          delete hero.dataset.heroInteracting;
        });
      }, 3000);
    };
    ['pointermove', 'pointerdown', 'keydown', 'wheel', 'scroll', 'input'].forEach(event => {
      document.addEventListener(event, onInteraction, { passive: true, capture: true });
    });
  }
  document.querySelectorAll('[data-hero-motion]').forEach(button => {
    const hero = button.closest('.asset-hero');
    button.addEventListener('click', () => {
      const playing = hero.dataset.heroPlaying !== 'true';
      hero.dataset.heroPlaying = String(playing);
      button.setAttribute('aria-pressed', String(playing));
      button.textContent = playing ? 'Pause motion' : 'Play motion';
    });
  });
})();
