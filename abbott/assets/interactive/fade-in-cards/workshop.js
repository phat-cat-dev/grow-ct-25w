(function () {
  'use strict';
  const host = document.querySelector('.fade-cards');
  const status = document.querySelector('[data-status]');
  const player = FadeInCards.mount(host, { cardGap: 500 });
  const grid = host.querySelector('.fade-grid');
  const cards = [...grid.children];
  const cardTemplate = document.createElement('template');
  cardTemplate.innerHTML = '<li data-fade-item><article class="fade-card"><p class="fade-eyebrow"></p><h3></h3><p data-card-summary></p><div class="fade-card-back" hidden><h3>Take it further.</h3><p>Replace this with additional guidance, an example or a reflection prompt.</p></div></article></li>';
  for (const key of ['duration', 'stagger', 'distance', 'gap']) {
    const input = document.querySelector(`[data-${key}]`);
    input.addEventListener('input', () => {
      document.querySelector(`[data-${key}-value]`).textContent = `${input.value} ${key === 'distance' ? 'px' : 'ms'}`;
    });
  }
  document.querySelector('[data-count]').addEventListener('change', event => {
    const input = event.target;
    if (!input.checkValidity() || !Number.isInteger(input.valueAsNumber)) {
      input.setAttribute('aria-invalid', 'true');
      status.textContent = 'Enter a whole number of cards from 1 to 12.';
      return;
    }
    input.removeAttribute('aria-invalid');
    player.show();
    const count = input.valueAsNumber;
    while (cards.length < count) {
      const item = cardTemplate.content.firstElementChild.cloneNode(true);
      const number = cards.length + 1;
      item.querySelector('.fade-eyebrow').textContent = `${String(number).padStart(2, '0')} / Next step`;
      item.querySelector('h3').textContent = `Your next step ${number}.`;
      item.querySelector('[data-card-summary]').textContent = 'Replace this example with your own prompt, explanation or action.';
      cards.push(item);
    }
    grid.replaceChildren(...cards.slice(0, count));
    FadeFlipCards.enhance(grid);
    status.textContent = `${count} cards ready. Press Replay to reveal them in order.`;
  });
  document.querySelector('select[data-layout]').addEventListener('change', event => {
    player.show();
    host.dataset.layout = event.target.value;
    status.textContent = 'Layout updated. Press Replay to start the sequence.';
  });
  host.addEventListener('fade-in:complete', () => { status.textContent = 'All content revealed.'; });
  host.addEventListener('fade-in:error', event => { status.textContent = `Animation error: ${event.detail.message}`; });
  document.querySelector('[data-replay]').addEventListener('click', async () => {
    try {
      player.set(Object.fromEntries(['duration', 'stagger', 'distance'].map(key =>
        [key, document.querySelector(`[data-${key}]`).valueAsNumber])));
      player.set({
        effect: document.querySelector('[data-effect]').value,
        cardGap: document.querySelector('[data-gap]').valueAsNumber,
      });
      status.textContent = 'Replaying the fade-in sequence.';
      await player.play();
    } catch (error) { player.show(); status.textContent = `Animation error: ${error.message}`; }
  });
  document.querySelector('[data-show]').addEventListener('click', () => {
    player.show(); status.textContent = 'All content shown immediately.';
  });
})();
