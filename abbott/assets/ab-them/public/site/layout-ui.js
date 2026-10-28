(function () {
  var state = window.ABLayout.validateLayout();
  var style = document.createElement('style');
  document.head.appendChild(style);
  var input = document.getElementById('layout-demo-corner-radius');
  function render() {
    input.value = state.radius;
    input.setAttribute('aria-valuetext', state.radius + ' pixels');
    document.getElementById('layout-demo-corner-radius-value').textContent = state.radius + ' px';
    style.textContent = window.ABLayout.layoutCss(state);
  }
  input.addEventListener('input', function () {
    state = window.ABLayout.validateLayout({ radius: +input.value });
    render();
  });
  document.getElementById('layout-demo-radius-reset').addEventListener('click', function () {
    state = window.ABLayout.validateLayout();
    render();
  });
  window.ABLayoutTheme = {
    get: function () { return { ...state }; },
    css: function () { return window.ABLayout.layoutCss(state); },
    load: function (config) { state = window.ABLayout.validateLayout(config.layout); render(); },
  };
  render();
})();
