(function () {
  'use strict';
  document.querySelectorAll('[data-stack]').forEach(host => {
    const layers = [...host.querySelectorAll('details.layer')];
    const step = host.querySelector('[data-step]');
    const status = host.querySelector('[data-stack-status]');
    const progress = host.querySelector('progress');
    let visited = 0;
    let walking = false;
    progress.max = layers.length;
    function render() {
      layers.forEach((layer, index) => {
        layer.hidden = walking && index >= visited;
        layer.toggleAttribute('data-current', walking && index === visited - 1);
      });
      host.querySelectorAll('.arrow, .plus').forEach(item => { item.hidden = walking; });
      progress.value = visited;
      step.textContent = !walking ? 'Walk through layers' : visited === layers.length ? 'Restart walkthrough' : 'Next layer';
      status.textContent = walking
        ? `${visited} of ${layers.length} layers visited. ${layers[visited - 1].querySelector('summary').textContent}`
        : 'All layers visible. Select a layer heading to open or close its explanation.';
    }
    step.addEventListener('click', () => {
      if (!walking || visited === layers.length) visited = 0;
      walking = true;
      layers.forEach(layer => { layer.open = false; });
      layers[visited].open = true;
      visited += 1;
      render();
      layers[visited - 1].querySelector('summary').focus();
    });
    host.querySelector('[data-show-all]').addEventListener('click', () => {
      walking = false;
      visited = 0;
      layers.forEach(layer => { layer.open = true; });
      render();
    });
    host.querySelector('[data-collapse]').addEventListener('click', () => {
      layers.forEach(layer => { layer.open = false; });
      status.textContent = 'Explanations closed. Select any visible layer heading to reopen it.';
    });
    host.querySelector('[data-profile]').addEventListener('change', event => {
      host.dataset.profile = event.target.value;
      status.textContent = `${event.target.selectedOptions[0].textContent} visual profile applied. Structure and layer order are unchanged.`;
    });
    const form = host.querySelector('form');
    const answer = form.elements.namedItem('owner');
    const feedback = form.querySelector('[data-check-status]');
    function clearAnswer() {
      feedback.textContent = '';
      answer.removeAttribute('aria-invalid');
    }
    answer.addEventListener('change', clearAnswer);
    form.addEventListener('submit', event => {
      event.preventDefault();
      const correct = answer.value === (host.dataset.stack === 'adapt-core-base' ? 'adapt' : 'grow');
      answer.setAttribute('aria-invalid', String(!correct));
      feedback.textContent = correct
        ? 'Correct. Both stacks share the style tier; mechanical structure ownership is the difference.'
        : 'Not quite. Read the mechanical layers above. A customer profile changes styles, not structure ownership.';
    });
    host.querySelector('[data-check-reset]').addEventListener('click', () => {
      form.reset();
      clearAnswer();
      answer.focus();
    });
    render();
  });
})();
