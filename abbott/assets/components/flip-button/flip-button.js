(function () {
  'use strict';
  document.addEventListener('click', event => {
    const button = event.target.closest('button.flip-button[data-flip-toggle]');
    if (!button || button.disabled) return;
    const flipped = button.dataset.flipped !== 'true';
    button.dataset.flipped = String(flipped);
    button.setAttribute('aria-pressed', String(flipped));
    button.dispatchEvent(new CustomEvent('flip-button:change', { bubbles: true, detail: { flipped } }));
  });
})();
