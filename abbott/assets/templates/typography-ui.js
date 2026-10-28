(function () {
  var api = window.ABTypography;
  var state = api.validateTypography();
  var style = document.createElement('style');
  document.head.appendChild(style);
  var byId = function (id) { return document.getElementById('typography-demo-' + id); };
  var groups = { headScheme: 'scheme', headDec: 'decoration', headBul: 'bullet', academicBul: 'bullet', headSize: 'size' };
  function render() {
    api.validateTypography(state);
    Object.keys(groups).forEach(function (id) {
      byId(id).querySelectorAll('input[type="radio"]').forEach(function (input) { input.checked = input.value === state[groups[id]]; });
    });
    byId('headRev').checked = state.reverse;
    byId('headCaps').querySelectorAll('input').forEach(function (input, index) {
      input.checked = state.caps[index];
    });
    byId('headScale').value = state.scale;
    byId('headScale-val').textContent = state.scale.toFixed(2) + '×';
    var ratio = api.TYPOGRAPHY_RATIOS[state.size];
    byId('heading-size-formula').textContent = (ratio ? 'Formula: 0.875rem × ' + ratio.toFixed(4) + '^(6 − heading level) × scale. ' : state.size === 'uniform' ? 'Uniform maximum: 1.15rem × scale. ' : 'Original graded sizes. ') +
      'H1–H6 maxima: ' + api.headingSizes(state.size).map(function (size) { return (size * state.scale).toFixed(3) + 'rem'; }).join(' · ');
    ['underlineWidth', 'borderWidth', 'iconSize'].forEach(function (key) {
      var unit = key === 'borderWidth' ? ' rem' : ' em';
      byId(key).value = state[key];
      byId(key + '-val').textContent = state[key].toFixed(2) + unit;
      byId(key).setAttribute('aria-valuetext', state[key].toFixed(2) + unit);
    });
    ['bodySize', 'lineHeight', 'readingWidth'].forEach(function (key) {
      byId(key).value = state[key];
      byId(key + '-val').textContent = state[key] + (key === 'bodySize' ? ' px' : key === 'readingWidth' ? ' ch' : '');
    });
    byId('headWrap').className = 'panel headings';
    style.textContent = api.typographyCss(state) + api.typographyCss(state, '#typography-demo-headWrap');
    byId('setDownstream').setAttribute('aria-pressed', String(state.applied));
    byId('setDownstream').textContent = state.applied ? 'Heading scheme active across page' : 'Set downstream - apply to whole page';
    byId('type-status').textContent = state.applied ? 'Heading scheme is live across the page and follows your main colour. Changes apply immediately.' : 'Previewing headings here. Set downstream to apply them across the page. Body settings are live.';
    byId('type-css').textContent = api.typographyCss(state);
  }
  Object.keys(groups).forEach(function (id) {
    byId(id).querySelectorAll('input[type="radio"]').forEach(function (input) {
      input.addEventListener('change', function () { if (this.checked) { state[groups[id]] = this.value; render(); } });
    });
  });
  byId('headRev').addEventListener('change', function () { state.reverse = this.checked; render(); });
  byId('headCaps').querySelectorAll('input').forEach(function (input, index) {
    input.addEventListener('change', function () { state.caps[index] = this.checked; render(); });
  });
  [['headScale', 'scale'], ['bodySize', 'bodySize'], ['lineHeight', 'lineHeight'], ['readingWidth', 'readingWidth'], ['underlineWidth', 'underlineWidth'], ['borderWidth', 'borderWidth'], ['iconSize', 'iconSize']].forEach(function (pair) {
    byId(pair[0]).addEventListener('input', function () { state[pair[1]] = +this.value; render(); });
  });
  byId('setDownstream').addEventListener('click', function () { state.applied = true; render(); });
  byId('type-reset').addEventListener('click', function () { state = api.validateTypography(); render(); });
  document.querySelectorAll('#typography-content input, #typography-content button').forEach(function (control) { control.dataset.typographyLive = ''; });
  window.ABTypographyTheme = {
    get: function () { return JSON.parse(JSON.stringify(state)); },
    css: function () { return api.typographyCss(state); },
    load: function (config) { state = api.validateTypography(config.typography); render(); },
  };
  render();
})();
