(function () {
  var api = window.ABSpacing;
  var state = api.validateSpacing();
  var style = document.createElement('style');
  document.head.appendChild(style);
  var panel = document.querySelector('[data-spacing-controls]');
  var status = document.getElementById('spacing-demo-spacing-status');
  var controls = panel.querySelectorAll('[data-spacing-setting]');
  function measure() {
    document.querySelectorAll('[data-spacing-readout]').forEach(function (output) {
      var specimen = output.closest('[data-ab-profile]');
      if (!specimen.getClientRects().length) return;
      var card = getComputedStyle(specimen.querySelector('.fluid-card'));
      var text = getComputedStyle(specimen.querySelector('.fluid-copy'));
      var icon = specimen.querySelector('.fluid-icon');
      output.textContent = 'Text ' + parseFloat(text.fontSize).toFixed(1) + 'px / padding ' +
        parseFloat(card.paddingTop).toFixed(1) + 'px' + (icon ? ' / icon ' + parseFloat(getComputedStyle(icon).width).toFixed(1) + 'px' : '') + ' / viewport ' + window.innerWidth + 'px';
    });
  }
  function render(changedInput) {
    style.textContent = api.spacingCss(state);
    controls.forEach(function (input) {
      var key = input.dataset.spacingSetting;
      var minimum = key.endsWith('Min');
      var scale = key.slice(0, -3);
      var gap = scale === 'viewport' ? 1 : 0;
      if (minimum) input.max = state[scale + 'Max'] - gap;
      else input.min = state[scale + 'Min'] + gap;
      if (input !== changedInput) input.value = state[input.dataset.spacingSetting];
      input.setAttribute('aria-valuetext', state[key] + ' rem');
      panel.querySelector('[data-spacing-value="' + key + '"]').textContent = state[key] + ' rem';
    });
    panel.querySelector('select').value = Object.keys(api.SPACING_PROFILES).find(function (name) {
      return Object.keys(state).every(function (key) { return state[key] === api.SPACING_PROFILES[name][key]; });
    }) || 'custom';
    document.getElementById('spacing-demo-spacing-css').textContent = api.spacingCss(state);
    status.textContent = 'Fluid tokens are live. Text, spacing, layout and icon size have independent ranges. Icon padding still follows the space scale. Existing typography controls are unchanged.';
    status.classList.remove('error');
    measure();
    requestAnimationFrame(measure);
  }
  controls.forEach(function (input) {
    input.addEventListener('input', function () {
      try {
        state = api.validateSpacing(Object.assign({}, state, { [input.dataset.spacingSetting]: input.valueAsNumber }));
        render(input);
      } catch (error) {
        status.textContent = error.message + '. The last valid settings remain active.';
        status.classList.add('error');
      }
    });
    input.addEventListener('change', function () { input.value = state[input.dataset.spacingSetting]; });
  });
  panel.querySelector('select').addEventListener('change', function () {
    state = api.validateSpacing(api.SPACING_PROFILES[this.value]);
    render();
  });
  panel.querySelector('button').addEventListener('click', function () {
    state = api.validateSpacing();
    panel.querySelector('select').value = 'default';
    render();
  });
  window.addEventListener('resize', measure);
  new ResizeObserver(measure).observe(document.getElementById('spacing-content'));
  window.ABSpacingTheme = {
    get: function () { return Object.assign({}, state); },
    css: function () { return api.spacingCss(state); },
    load: function (config) { state = api.validateSpacing(config.spacing); render(); },
  };
  render();
})();
