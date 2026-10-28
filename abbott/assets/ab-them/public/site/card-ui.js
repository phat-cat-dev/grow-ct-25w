(function () {
  var api = window.ABCards;
  var state = api.validateCards();
  var style = document.createElement('style');
  document.head.appendChild(style);
  function byId(id) { return document.getElementById('objects-demo-card-' + id); }
  function render() {
    Object.keys(api.DEFAULT_CARDS).forEach(function (key) {
      var input = byId(key);
      input.value = state[key];
      if (input.type === 'range') {
        var unit = key === 'tint' ? '%' : ' px';
        byId(key + '-value').textContent = state[key] + unit;
        input.setAttribute('aria-valuetext', state[key] + (key === 'tint' ? ' percent' : ' pixels'));
      }
    });
    style.textContent = api.cardsCss(state);
    byId('css').textContent = style.textContent;
  }
  Object.keys(api.DEFAULT_CARDS).forEach(function (key) {
    var input = byId(key);
    input.addEventListener(input.type === 'range' ? 'input' : 'change', function () {
      state = api.validateCards({ ...state, [key]: input.type === 'range' ? +input.value : input.value });
      render();
      byId('status').textContent = 'Card settings applied throughout the project.';
    });
  });
  byId('reset').addEventListener('click', function () {
    state = api.validateCards();
    render();
    byId('status').textContent = 'Card settings reset. Project colours and Layout corners are unchanged.';
  });
  window.ABCardTheme = {
    get: function () { return { ...state }; },
    css: function () { return api.cardsCss(state); },
    load: function (config) { state = api.validateCards(config.cards); render(); },
  };
  render();
})();
