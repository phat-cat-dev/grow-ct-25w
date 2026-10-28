(function () {
  var connectorApi = window.ABConnectors;
  var connectorConfig = Object.assign({}, connectorApi.DEFAULT_CONNECTORS);
  var connectorStyle = document.createElement('style');
  document.head.appendChild(connectorStyle);
  var connectorLinks = {};
  var selectedSymbol = 'home';
  var root = document.documentElement;
  var editor = document.getElementById('scheme-css');
  var nameInput = document.getElementById('scheme-name');
  var list = document.getElementById('scheme-list');
  var status = document.getElementById('scheme-status');
  var downloads = document.getElementById('scheme-downloads');
  var loaded = { brandH: 202, brandS: 72, greyS: 12, harmony: 'complementary', semanticS: 55, overrides: {} };
  var localMode = location.protocol === 'file:';
  var storageKey = 'ab-theme-studio-schemes';
  function localSchemes() {
    var records = JSON.parse(localStorage.getItem(storageKey) || '{}');
    if (!records || typeof records !== 'object' || Array.isArray(records)) throw new Error('Saved local themes are invalid. Import a theme JSON backup to recover.');
    return records;
  }
  var injection = document.createElement('style');
  injection.id = 'scheme-injection';
  document.head.appendChild(injection);

  function report(message, error) {
    status.textContent = message;
    status.classList.toggle('error', !!error);
  }
  var motionPreference = matchMedia('(prefers-reduced-motion: reduce)');
  var motionButtons = document.querySelectorAll('[data-motion-toggle]');
  var transitionDemo = document.getElementById('motion-demo-transition-demo');
  var transitionDuration = document.getElementById('motion-demo-transition-duration');
  transitionDuration.addEventListener('input', function () {
    transitionDemo.style.setProperty('--transition-duration', this.value + 'ms');
    document.getElementById('motion-demo-transition-duration-value').textContent = this.value + ' ms';
    this.setAttribute('aria-valuetext', this.value + ' milliseconds');
  });
  document.querySelectorAll('[data-transition-toggle]').forEach(function (button) {
    button.addEventListener('click', function () {
      var active = button.getAttribute('aria-pressed') !== 'true';
      button.setAttribute('aria-pressed', String(active));
      button.querySelector('.motion-state').textContent = active ? 'Changed state - click to reverse' : 'Original state';
    });
  });
  function pauseMotion() {
    motionButtons.forEach(function (button) {
      button.closest('.motion-sample').classList.remove('is-playing');
      button.setAttribute('aria-pressed', 'false');
      button.querySelector('.motion-state').textContent = motionPreference.matches ? 'Reduced motion' : 'Click to play';
      button.disabled = motionPreference.matches;
    });
    document.getElementById('motion-demo-motion-status').textContent = motionPreference.matches
      ? 'Reduced motion is enabled. All previews remain still.'
      : 'Motion previews are paused.';
  }
  motionButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      if (motionPreference.matches) return;
      var sample = button.closest('.motion-sample');
      var playing = sample.classList.toggle('is-playing');
      button.setAttribute('aria-pressed', String(playing));
      button.querySelector('.motion-state').textContent = playing ? 'Playing · click to pause' : 'Click to play';
      document.getElementById('motion-demo-motion-status').textContent = sample.querySelector('.motion-title').textContent + (playing ? ' playing. Click its tile again to pause.' : ' paused.');
    });
  });
  motionPreference.addEventListener('change', pauseMotion);
  document.addEventListener('visibilitychange', function () { if (document.hidden) pauseMotion(); });
  pauseMotion();
  function scheme() {
    var name = nameInput.value.trim();
    if (!/^[a-z0-9_-]+$/i.test(name)) throw new Error('Use letters, numbers, underscores or hyphens for the scheme name.');
    var colors = window.ABColorTheme.get();
    var main = window.ABColor.mainColor(colors);
    return Object.assign({}, loaded, {
      name: name, customCss: editor.value, connectors: connectorConfig, colorSystem: colors, typography: window.ABTypographyTheme.get(), spacing: window.ABSpacingTheme.get(), layout: window.ABLayoutTheme.get(), cards: window.ABCardTheme.get(), themeMode: root.dataset.theme || 'system',
      brandH: main.h, brandS: main.s, greyS: main.gs, harmony: colors.harmony, semanticS: colors.semanticS
    });
  }
  async function request(url, options) {
    var response = await fetch(url, options);
    var data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Request failed (' + response.status + ')');
    return data;
  }
  async function refresh() {
    var names = localMode ? Object.keys(localSchemes()).sort() : await request('/api/themes');
    list.replaceChildren(new Option('Choose a scheme', ''));
    names.forEach(function (name) { list.add(new Option(name, name)); });
  }
  async function save(config) {
    if (localMode) {
      var records = localSchemes();
      Object.defineProperty(records, config.name, { value: config, enumerable: true, writable: true, configurable: true });
      localStorage.setItem(storageKey, JSON.stringify(records));
    } else {
      await request('/api/themes/' + encodeURIComponent(config.name), {
        method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(config)
      });
    }
    loaded = config;
    await refresh();
    list.value = config.name;
  }
  function action(id, callback) {
    document.getElementById(id).addEventListener('click', async function () {
      downloads.replaceChildren();
      try { await callback(); }
      catch (error) { report(error.message, true); }
    });
  }
  function download(text, filename, type) {
    var url = URL.createObjectURL(new Blob([text], { type: type }));
    var link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    report('Exported ' + filename);
  }
  function exportedCss() {
    var assets = connectorApi.connectorAssets(connectorConfig);
    return connectorApi.connectorImports(assets.urls) + '\n' + window.ABThemeTemplate + '\n' + assets.css + '\n\n' + window.ABColorTheme.css() + '\n' + window.ABTypographyTheme.css() + '\n' + window.ABSpacingTheme.css() + '\n' + window.ABLayoutTheme.css() + '\n' + window.ABCardTheme.css() + '\n' + editor.value;
  }
  function connectorStatus(id, message, error) {
    var element = document.getElementById(id);
    element.textContent = message;
    element.classList.toggle('error', !!error);
  }
  function loadStylesheet(key, url, statusId, font, sample) {
    if (connectorLinks[key] && connectorLinks[key].href === url) return;
    if (connectorLinks[key]) connectorLinks[key].remove();
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = url;
    connectorLinks[key] = link;
    connectorStatus(statusId, 'Connecting to Google...');
    link.onload = async function () {
      try {
        var faces = await document.fonts.load(font, sample);
        if (connectorLinks[key] !== link) return;
        if (!faces.length) throw new Error('Font did not load');
        connectorStatus(statusId, 'Connected to Google. Preview and exports are ready.');
      } catch (error) {
        if (connectorLinks[key] === link) connectorStatus(statusId, 'Font download failed. Check your connection; local fallbacks remain available.', true);
      }
    };
    link.onerror = function () {
      if (connectorLinks[key] === link) connectorStatus(statusId, 'Google could not be reached. Check your connection; exports still include the connector.', true);
    };
    document.head.appendChild(link);
  }
  function applyConnectors() {
    var assets = connectorApi.connectorAssets(connectorConfig);
    connectorStyle.textContent = assets.css;
    document.getElementById('icons-demo-symbol-gallery').style.setProperty('--symbol-size', connectorConfig.symbolSize + 'px');
    loadStylesheet('fonts', assets.urls[0], 'typography-demo-fonts-status', '400 16px "' + connectorConfig.bodyFont + '"', 'Typography');
    loadStylesheet('symbols', assets.urls[1], 'icons-demo-symbols-status', '400 32px "Material Symbols ' + connectorConfig.symbolStyle + '"', 'home');
    document.getElementById('typography-demo-font-heading').value = connectorConfig.headingFont;
    document.getElementById('typography-demo-font-body').value = connectorConfig.bodyFont;
    document.getElementById('icons-demo-symbol-style').value = connectorConfig.symbolStyle;
    document.getElementById('icons-demo-symbol-weight').value = connectorConfig.symbolWeight;
    document.getElementById('icons-demo-symbol-size').value = connectorConfig.symbolSize;
    document.getElementById('icons-demo-symbol-size-value').textContent = connectorConfig.symbolSize + ' px';
    document.getElementById('icons-demo-symbol-fill').checked = !!connectorConfig.symbolFill;
  }
  ['typography-demo-font-heading', 'typography-demo-font-body'].forEach(function (id) {
    var select = document.getElementById(id);
    connectorApi.FONT_FAMILIES.forEach(function (font) { select.add(new Option(font, font)); });
  });
  document.getElementById('typography-demo-fonts-apply').addEventListener('click', function () {
    connectorConfig.headingFont = document.getElementById('typography-demo-font-heading').value;
    connectorConfig.bodyFont = document.getElementById('typography-demo-font-body').value;
    applyConnectors();
  });
  ['style', 'weight', 'size', 'fill'].forEach(function (property) {
    var input = document.getElementById('icons-demo-symbol-' + property);
    input.addEventListener(property === 'size' ? 'input' : 'change', function () {
      connectorConfig.symbolStyle = document.getElementById('icons-demo-symbol-style').value;
      connectorConfig.symbolWeight = +document.getElementById('icons-demo-symbol-weight').value;
      connectorConfig.symbolSize = +document.getElementById('icons-demo-symbol-size').value;
      connectorConfig.symbolFill = +document.getElementById('icons-demo-symbol-fill').checked;
      applyConnectors();
    });
  });
  var symbols = ['home', 'search', 'favorite', 'check_circle', 'close', 'add', 'settings', 'palette', 'text_fields', 'school', 'menu_book', 'lightbulb', 'download', 'upload', 'content_copy', 'arrow_forward', 'person', 'groups', 'calendar_month', 'notifications', 'edit', 'delete', 'info', 'warning'];
  function symbolMarkup() {
    return '<span class="material-symbol" aria-hidden="true">' + selectedSymbol + '</span>';
  }
  function renderSymbols() {
    var gallery = document.getElementById('icons-demo-symbol-gallery');
    var query = document.getElementById('icons-demo-symbol-search').value.trim().toLowerCase().replaceAll(' ', '_');
    gallery.replaceChildren();
    symbols.filter(function (name) { return name.includes(query); }).forEach(function (name) {
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'symbol-choice';
      button.setAttribute('aria-label', name.replaceAll('_', ' '));
      button.title = name.replaceAll('_', ' ');
      button.setAttribute('aria-pressed', String(name === selectedSymbol));
      var glyph = document.createElement('span');
      glyph.className = 'material-symbol';
      glyph.setAttribute('aria-hidden', 'true');
      glyph.textContent = name;
      button.appendChild(glyph);
      button.addEventListener('click', function () {
        selectedSymbol = name;
        document.getElementById('icons-demo-symbol-markup').textContent = symbolMarkup();
        renderSymbols();
        Array.from(gallery.children).find(function (choice) { return choice.getAttribute('aria-pressed') === 'true'; }).focus({ preventScroll: true });
      });
      gallery.appendChild(button);
    });
    if (!gallery.children.length) {
      var empty = document.createElement('p');
      empty.textContent = 'No matching preview symbols. Browse the full Google library using the link below.';
      gallery.appendChild(empty);
    }
  }
  document.getElementById('icons-demo-symbol-search').addEventListener('input', renderSymbols);
  document.getElementById('icons-demo-symbol-copy').addEventListener('click', async function () {
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable. Select the markup above to copy it.');
      await navigator.clipboard.writeText(symbolMarkup());
      connectorStatus('icons-demo-symbols-status', 'Symbol markup copied. Export your scheme CSS to include its font and styling.');
    } catch (error) { connectorStatus('icons-demo-symbols-status', error.message, true); }
  });
  renderSymbols();
  applyConnectors();
  var svgPacks = document.getElementById('icons-demo-iconPacks');
  var svgSize = document.getElementById('icons-demo-svg-icon-size');
  var svgCircle = document.getElementById('icons-demo-svg-icon-circle');
  function updateSvgFrames() {
    svgPacks.style.setProperty('--svg-icon-size', svgSize.value + 'px');
    svgPacks.style.setProperty('--svg-frame-radius', svgCircle.checked ? '50%' : '0');
    document.getElementById('icons-demo-svg-icon-size-value').textContent = svgSize.value + ' px';
  }
  svgSize.addEventListener('input', updateSvgFrames);
  svgCircle.addEventListener('change', updateSvgFrames);
  svgPacks.querySelectorAll('.iconcell').forEach(function (cell) {
    var name = cell.querySelector('use').getAttribute('href').replace('#ic-', '').replaceAll('-', ' ');
    cell.setAttribute('aria-label', 'Copy ' + name + ' icon markup');
    cell.title = name + ' - click to copy markup';
    cell.querySelector('svg').setAttribute('aria-hidden', 'true');
  });
  updateSvgFrames();

  document.getElementById('scheme-open').addEventListener('click', function () {
    var panel = document.getElementById('scheme-tools');
    panel.hidden = !panel.hidden;
    this.setAttribute('aria-expanded', String(!panel.hidden));
  });
  document.querySelectorAll('[data-theme-set]').forEach(function (button) {
    button.addEventListener('click', function () {
      var mode = button.dataset.themeSet;
      if (mode === 'system') root.removeAttribute('data-theme');
      else root.dataset.theme = mode;
      document.querySelectorAll('[data-theme-set]').forEach(function (item) {
        item.setAttribute('aria-pressed', String(item === button));
      });
    });
  });
  document.querySelectorAll('.area-trigger').forEach(function (button) {
    var content = document.getElementById(button.getAttribute('aria-controls'));
    content.hidden = true;
    button.setAttribute('aria-expanded', 'false');
    button.addEventListener('click', function () {
      content.hidden = !content.hidden;
      button.setAttribute('aria-expanded', String(!content.hidden));
    });
  });
  document.querySelectorAll('h3.outline-title').forEach(function (heading) {
    var content = document.createElement('div');
    content.id = heading.id + '-content';
    content.className = 'outline-content';
    while (heading.nextSibling) content.appendChild(heading.nextSibling);
    heading.after(content);
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'outline-trigger';
    button.setAttribute('aria-expanded', 'true');
    button.setAttribute('aria-controls', content.id);
    while (heading.firstChild) button.appendChild(heading.firstChild);
    var chevron = document.createElement('span');
    chevron.className = 'area-chevron';
    chevron.setAttribute('aria-hidden', 'true');
    button.appendChild(chevron);
    heading.appendChild(button);
    button.addEventListener('click', function () {
      content.hidden = !content.hidden;
      button.setAttribute('aria-expanded', String(!content.hidden));
    });
  });
  function openLinkedArea() {
    var target = document.getElementById(location.hash.slice(1));
    var area = target && target.closest('.site-area');
    if (!area) return;
    var button = area.querySelector('.area-trigger');
    document.getElementById(button.getAttribute('aria-controls')).hidden = false;
    button.setAttribute('aria-expanded', 'true');
    for (var section = target; section && section !== area; section = section.parentElement) {
      if (!section.classList.contains('outline-section')) continue;
      var trigger = section.querySelector(':scope > h3.outline-title > .outline-trigger');
      if (!trigger) continue;
      document.getElementById(trigger.getAttribute('aria-controls')).hidden = false;
      trigger.setAttribute('aria-expanded', 'true');
    }
    target.scrollIntoView();
  }
  window.addEventListener('hashchange', openLinkedArea);
  document.querySelector('.page-nav').addEventListener('click', function (event) {
    var link = event.target.closest('a');
    if (link && link.hash === location.hash) openLinkedArea();
  });
  openLinkedArea();
  document.querySelectorAll('.ab.accordion .accordion-button').forEach(function (button, index) {
    var panel = button.closest('.accordion-header').nextElementSibling;
    button.id = 'accordion-trigger-' + (index + 1);
    panel.id = 'accordion-panel-' + (index + 1);
    button.setAttribute('aria-controls', panel.id);
    panel.setAttribute('role', 'region');
    panel.setAttribute('aria-labelledby', button.id);
    function setOpen(open) {
      button.classList.toggle('collapsed', !open);
      button.setAttribute('aria-expanded', String(open));
      panel.hidden = !open;
    }
    setOpen(!button.classList.contains('collapsed'));
    button.addEventListener('click', function () { setOpen(button.getAttribute('aria-expanded') !== 'true'); });
  });
  document.querySelectorAll('#site-content input, #site-content select, #site-content button:not(.area-trigger)').forEach(function (control) {
    if (control.closest('[data-connector], [data-motion-demo], [data-layout-live], [data-card-live], [data-lesson], [data-horizontal-accordion], [data-edu-library]') || control.matches('.accordion-button, .outline-trigger') || control.hasAttribute('data-color-live') || control.hasAttribute('data-typography-live') || control.hasAttribute('data-spacing-live')) return;
    control.disabled = true;
    control.title = 'Structure preview - wiring comes in the next stage.';
  });
  document.querySelectorAll('#site-content [role="button"]').forEach(function (control) {
    if (control.classList.contains('iconcell')) {
      async function copySvg() {
        try {
          var href = control.querySelector('use').getAttribute('href');
          if (!navigator.clipboard) throw new Error('Clipboard unavailable. SVG reference: ' + href);
          await navigator.clipboard.writeText('<span class="ab-icon"><svg aria-hidden="true"><use href="' + href + '"></use></svg></span>');
          control.classList.add('ok');
          connectorStatus('icons-demo-symbols-status', 'SVG icon markup copied: ' + href);
          setTimeout(function () { control.classList.remove('ok'); }, 1400);
        } catch (error) { connectorStatus('icons-demo-symbols-status', error.message, true); }
      }
      control.addEventListener('click', copySvg);
      control.addEventListener('keydown', function (event) {
        if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); copySvg(); }
      });
      return;
    }
    control.setAttribute('aria-disabled', 'true');
    control.setAttribute('tabindex', '-1');
    control.title = 'Structure preview - wiring comes in the next stage.';
  });
  document.querySelectorAll('#site-content input[type="range"]').forEach(function (input) {
    var label = document.getElementById(input.id + '-val');
    if (label) {
      var suffix = label.textContent.includes('°') ? '°' : label.textContent.includes('%') ? '%' : label.textContent.includes('×') ? '×' : '';
      label.textContent = input.value + suffix;
    }
  });
  action('scheme-inject', function () {
    injection.textContent = editor.value;
    report('Custom CSS injected on top of your live colour, font and symbol settings.');
  });
  action('scheme-reset', function () {
    injection.textContent = '';
    report('Injected CSS removed.');
  });
  action('scheme-copy', async function () {
    if (!navigator.clipboard) throw new Error('Clipboard unavailable. Use Export CSS instead.');
    await navigator.clipboard.writeText(exportedCss());
    report('CSS copied.');
  });
  action('scheme-export', function () { download(exportedCss(), scheme().name + '.css', 'text/css'); });
  document.querySelectorAll('[data-theme-export]').forEach(function (button) {
    button.addEventListener('click', function () { document.getElementById('scheme-export').click(); });
  });
  document.querySelectorAll('[data-theme-tools]').forEach(function (button) {
    button.addEventListener('click', function () {
      if (document.getElementById('scheme-tools').hidden) document.getElementById('scheme-open').click();
      nameInput.focus();
      document.getElementById('scheme-tools').scrollIntoView({ block: 'start' });
    });
  });
  action('scheme-json', function () { var config = scheme(); download(JSON.stringify(config, null, 2) + '\n', config.name + '.json', 'application/json'); });
  function loadScheme(config) {
    if (!config || typeof config !== 'object' || !/^[a-z0-9_-]+$/i.test(config.name || '')) throw new Error('Theme JSON needs a valid theme name.');
    if (config.customCss !== undefined && typeof config.customCss !== 'string') throw new Error('Theme CSS must be text.');
    if (config.themeMode !== undefined && !['light', 'dark', 'system'].includes(config.themeMode)) throw new Error('Invalid theme mode.');
    var assets = connectorApi.connectorAssets(config.connectors || connectorApi.DEFAULT_CONNECTORS);
    window.ABColor.validateColorSystem(config.colorSystem || window.ABColor.defaultColorSystem(config));
    window.ABTypography.validateTypography(config.typography);
    window.ABSpacing.validateSpacing(config.spacing);
    window.ABLayout.validateLayout(config.layout);
    window.ABCards.validateCards(config.cards);
    window.ABColorTheme.load(config);
    window.ABTypographyTheme.load(config);
    window.ABSpacingTheme.load(config);
    window.ABLayoutTheme.load(config);
    window.ABCardTheme.load(config);
    loaded = config;
    connectorConfig = assets.config;
    applyConnectors();
    nameInput.value = config.name;
    editor.value = config.customCss || '';
    if (config.themeMode) document.querySelector('[data-theme-set="' + config.themeMode + '"]').click();
    injection.textContent = editor.value;
    report('Loaded complete theme ' + config.name + ', including custom CSS.');
  }
  action('scheme-save', async function () {
    var config = scheme();
    await save(config);
    report('Saved complete theme ' + config.name + (localMode ? ' in this browser. Export scheme JSON for a portable backup.' : '.'));
  });
  action('scheme-load', async function () {
    if (!list.value) throw new Error('Choose a saved scheme first.');
    var config = localMode ? localSchemes()[list.value] : await request('/api/themes/' + encodeURIComponent(list.value));
    loadScheme(config);
  });
  document.getElementById('scheme-import').addEventListener('change', async function () {
    try {
      var file = this.files[0];
      if (!file) return;
      var record = JSON.parse(await file.text());
      loadScheme(record.config || record);
    } catch (error) { report('Theme import failed: ' + error.message, true); }
    finally { this.value = ''; }
  });
  action('scheme-build', async function () {
    var config = scheme();
    report('Saving and building ' + config.name + '...');
    await save(config);
    await request('/api/build/' + encodeURIComponent(config.name), { method: 'POST' });
    ['theme.css', 'tokens.json'].forEach(function (file) {
      var link = document.createElement('a');
      link.href = '/dist/' + encodeURIComponent(config.name) + '/' + file;
      link.textContent = file;
      link.download = file;
      downloads.appendChild(link);
    });
    report('Built ' + config.name + '. Download the full CSS and scheme JSON below.');
  });
  if (localMode) {
    document.getElementById('scheme-build').disabled = true;
    report('Save and Load store complete themes in this browser. Export/import JSON for portable backups. Run npm start for full CSS builds.');
  }
  refresh().catch(function (error) { report('Could not read saved themes: ' + error.message, true); });
})();
