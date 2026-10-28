(function () {
  'use strict';
  let ids = 0;
  function enhance(root) {
    root.querySelectorAll('.fade-card:has(.fade-card-back):not([data-flip-ready])').forEach(card => {
      const back = card.querySelector('.fade-card-back');
      const title = card.querySelector('h3').textContent;
      const front = document.createElement('div');
      front.className = 'fade-card-front';
      for (const node of [...card.childNodes]) if (node !== back) front.append(node);
      const rotor = document.createElement('div');
      rotor.className = 'fade-card-rotor';
      rotor.append(front, back);
      const button = document.createElement('button');
      button.type = 'button'; button.className = 'fade-card-toggle';
      back.id = `fade-card-info-${++ids}`;
      back.hidden = false;
      button.setAttribute('aria-controls', back.id);
      card.replaceChildren(rotor, button);
      card.dataset.flipReady = '';
      const set = flipped => {
        card.dataset.flipped = String(flipped);
        button.setAttribute('aria-expanded', String(flipped));
        button.setAttribute('aria-label', `${flipped ? 'Show front' : 'More information'}: ${title}`);
        front.setAttribute('aria-hidden', String(flipped));
        back.setAttribute('aria-hidden', String(!flipped));
        front.inert = flipped; back.inert = !flipped;
      };
      set(false);
      card.addEventListener('pointerenter', event => {
        if (event.pointerType === 'mouse' && matchMedia('(hover: hover)').matches) set(true);
      });
      card.addEventListener('pointerleave', event => { if (event.pointerType === 'mouse') set(false); });
      button.addEventListener('click', () => set(card.dataset.flipped !== 'true'));
      button.addEventListener('keydown', event => {
        if (event.key === 'Escape') { set(false); event.preventDefault(); }
      });
      card.addEventListener('focusout', event => { if (!card.contains(event.relatedTarget)) set(false); });
    });
  }
  globalThis.FadeFlipCards = { enhance };
  enhance(document);
})();
