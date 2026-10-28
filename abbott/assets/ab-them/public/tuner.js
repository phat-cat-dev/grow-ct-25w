(function () {
  var root = document.documentElement;
  var hEl = document.getElementById('h'),
      sEl = document.getElementById('s'),
      gsEl = document.getElementById('gs');
  var loadedConfig = {};
  var harmonySelect = document.getElementById('harm');

  // Lightness ladders. Brand tapers saturation at the extremes a touch via L spread;
  // grey keeps the same stops so the two scales line up visually.
  var STOPS = [
    ['50', 97], ['100', 92], ['200', 84], ['300', 73], ['400', 60],
    ['500', 48], ['600', 40], ['700', 32], ['800', 24], ['900', 17], ['950', 12]
  ];

  function textOn(l) { return l > 55 ? 'hsl(var(--h) 45% 14%)' : 'hsl(var(--h) 30% 96%)'; }

  function buildScale(elId, satExpr, satLabel) {
    var el = document.getElementById(elId);
    el.innerHTML = '';
    STOPS.forEach(function (st) {
      var step = st[0], L = st[1];
      var b = document.createElement('button');
      b.className = 'sw';
      b.style.background = 'hsl(var(--h) ' + satExpr + ' ' + L + '%)';
      b.style.color = textOn(L);
      b.innerHTML = '<span class="step">' + step + '</span><span class="lval">L ' + L + '%</span>';
      b.title = 'Click to copy';
      b.addEventListener('click', function () {
        var h = hEl.value, s = (elId === 'gray-scale' ? '0' : elId === 'grey-scale' ? gsEl.value : sEl.value);
        copy('hsl(' + h + ', ' + s + '%, ' + L + '%)');
      });
      el.appendChild(b);
    });
  }

  function render() {
    var h = hEl.value, s = sEl.value, gs = gsEl.value;
    root.style.setProperty('--h', h);
    root.style.setProperty('--s', s + '%');
    root.style.setProperty('--gs', gs + '%');
    document.getElementById('h-val').textContent = h + '°';
    document.getElementById('s-val').textContent = s + '%';
    document.getElementById('gs-val').textContent = gs + '%';
    buildScale('brand-scale', 'var(--s)');
    buildScale('grey-scale', 'var(--gs)');
    buildScale('gray-scale', '0%');
    updateHarmHues();
    writeExport(h, s, gs);
    syncSemanticState();
    var ingredientPreview = document.getElementById('ingredient-preview');
    if (ingredientPreview) ingredientPreview.textContent = ':root { --brand-h: ' + h + '; --brand-s: ' + s + '%; --grey-s: ' + gs + '%; }';
  }

  function syncSemanticState() {
    [['semS', '--sem-s', '%'], ['semWS', '--sem-weak-s', '%']].forEach(function (cfg) {
      var el = document.getElementById(cfg[0]);
      if (!el) return;
      var value = el.value + cfg[2];
      document.documentElement.style.setProperty(cfg[1], value);
      var label = document.getElementById(cfg[0] + '-val');
      if (label) label.textContent = value;
    });
    var styles = getComputedStyle(root);
    [['semL', '--sem-l'], ['semWL', '--sem-weak-l']].forEach(function (cfg) {
      var value = styles.getPropertyValue(cfg[1]).trim();
      document.getElementById(cfg[0]).value = parseFloat(value);
      document.getElementById(cfg[0] + '-val').textContent = value;
    });
  }

  function currentThemeConfig() {
    return Object.assign({}, loadedConfig, {
      brandH: +hEl.value,
      brandS: +sEl.value,
      greyS: +gsEl.value,
      harmony: harmSel(),
      semanticS: +document.getElementById('semS').value,
      overrides: loadedConfig.overrides || {}
    });
  }

  /* ---- colour harmony ---- */
  var HARM = {
    monochrome:    [0, 0, 0],
    complementary: [180, 180, 180],
    analogous:     [30, -30, 60],
    triadic:       [120, 240, 120],
    split:         [150, 210, 180],
    tetradic:      [60, 180, 240],
    square:        [90, 180, 270]
  };
  function harmSel() {
    if (harmonySelect) return harmonySelect.value;
    var r = document.querySelector('#harmPreset input[name=harm]:checked');
    return r ? r.value : 'complementary';
  }
  function wrapHue(x) { x %= 360; return x < 0 ? x + 360 : x; }
  function updateHarmHues() {
    var offs = HARM[harmSel()] || HARM.complementary, h = +hEl.value;
    var b1 = document.querySelector('.hsw b[data-hue="1"]'); if (b1) b1.textContent = h + '°';
    [2, 3, 4].forEach(function (n, i) {
      var b = document.querySelector('.hsw b[data-hue="' + n + '"]');
      if (b) b.textContent = wrapHue(h + offs[i]) + '°';
    });
  }
  function applyHarmony() { root.setAttribute('data-harmony', harmSel()); updateHarmHues(); }

  function writeExport(h, s, gs) {
    var lines = [];
    lines.push(':root {');
    lines.push('  /* --- ingredients: change --brand-h to re-theme the site --- */');
    lines.push('  --brand-h: ' + h + ';');
    lines.push('  --brand-s: ' + s + '%;   /* colourful blues */');
    lines.push('  --grey-s:  ' + gs + '%;   /* blue-grey neutrals */');
    lines.push('');
    lines.push('  /* --- brand scale --- */');
    STOPS.forEach(function (st) {
      lines.push('  --blue-' + pad(st[0]) + 'hsl(var(--brand-h) var(--brand-s) ' + st[1] + '%);');
    });
    lines.push('');
    lines.push('  /* --- blue-grey scale (same hue) --- */');
    STOPS.forEach(function (st) {
      lines.push('  --grey-' + pad(st[0]) + 'hsl(var(--brand-h) var(--grey-s) ' + st[1] + '%);');
    });
    lines.push('');
    lines.push('  /* --- pure grey scale (true neutral, 0% saturation) --- */');
    STOPS.forEach(function (st) {
      lines.push('  --gray-' + pad(st[0]) + 'hsl(0 0% ' + st[1] + '%);');
    });
    lines.push('');
    lines.push('  /* --- depth: tint shadows with the hue, never pure black --- */');
    lines.push('  --shadow-1: 0 1px 2px hsl(var(--brand-h) 40% 20% / .10),');
    lines.push('              0 4px 10px -4px hsl(var(--brand-h) 40% 20% / .16);');
    lines.push('  --shadow-2: 0 2px 4px hsl(var(--brand-h) 40% 20% / .12),');
    lines.push('              0 12px 26px -8px hsl(var(--brand-h) 45% 20% / .26);');
    lines.push('');
    lines.push('  /* --- headings: saturation + lightness ramp --- */');
    lines.push('  --h1-color: hsl(var(--brand-h) var(--brand-s) 40%);');
    lines.push('  --h2-color: hsl(var(--brand-h) 45% 24%);');
    lines.push('  --h3-color: hsl(var(--brand-h) 28% 36%);');
    lines.push('  --h4-color: hsl(var(--brand-h) var(--grey-s) 46%);');
    lines.push('');
    var offs = HARM[harmSel()] || HARM.complementary;
    lines.push('  /* --- colour harmony: "' + harmSel() + '" — siblings spawned from the hue --- */');
    lines.push('  --hue-2: calc(var(--brand-h) + ' + offs[0] + ');');
    lines.push('  --hue-3: calc(var(--brand-h) + ' + offs[1] + ');');
    lines.push('  --hue-4: calc(var(--brand-h) + ' + offs[2] + ');');
    lines.push('  --accent-2: hsl(var(--hue-2) var(--brand-s) 40%);');
    lines.push('  --accent-3: hsl(var(--hue-3) var(--brand-s) 40%);');
    lines.push('  --accent-4: hsl(var(--hue-4) var(--brand-s) 40%);');
    lines.push('}');
    document.getElementById('export').textContent = lines.join('\n');
  }
  function pad(step) { var s = step + ':'; while (s.length < 5) s += ' '; return s; }

  var toastT;
  function showToast(msg) {
    var t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove('show'); }, 1400);
  }
  function copy(text) {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { showToast('Copied  ' + (text.length > 30 ? ':root CSS' : text)); },
          function () { fallbackCopy(text); });
      } else { fallbackCopy(text); }
    } catch (e) { fallbackCopy(text); }
  }
  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { showToast(document.execCommand('copy') ? 'Copied' : 'Copy failed. Select the text and press Ctrl+C.'); }
    catch (e) { showToast('Copy failed. Select the text and press Ctrl+C.'); }
    document.body.removeChild(ta);
  }

  document.getElementById('copy').addEventListener('click', function () {
    copy(document.getElementById('export').textContent);
  });

  function sanitizeThemeName(name) {
    return String(name || '').trim().toLowerCase().replace(/[^a-z0-9_-]+/g, '-').replace(/^-+|-+$/g, '') || 'untitled';
  }

  function setBuildStatus(message, isError) {
    var box = document.getElementById('theme-build-output');
    if (!box) return;
    box.classList.toggle('error', !!isError);
    box.textContent = message || '';
  }

  async function refreshThemeList() {
    var list = document.getElementById('theme-list');
    var current = list.value || document.getElementById('theme-name').value || '';
    var res = await fetch('/api/themes');
    if (!res.ok) throw new Error('Unable to load saved themes');
    var themes = await res.json();
    list.innerHTML = '';
    var placeholder = document.createElement('option');
    placeholder.value = '';
    placeholder.textContent = 'Choose a saved theme…';
    list.appendChild(placeholder);
    themes.forEach(function (name) {
      var option = document.createElement('option');
      option.value = name;
      option.textContent = name;
      list.appendChild(option);
    });
    if (current && themes.includes(current)) list.value = current;
    else if (current && !themes.includes(current)) document.getElementById('theme-name').value = current;
  }

  async function loadTheme(name) {
    var safeName = sanitizeThemeName(name);
    if (!safeName || safeName === 'untitled') throw new Error('Choose a saved theme to load');
    var res = await fetch('/api/themes/' + safeName);
    if (!res.ok) throw new Error('Theme not found');
    var cfg = await res.json();
    if (cfg.colorSystem) throw new Error('This is a layered colour theme. Open /site/ to edit its source, refinement and selected systems.');
    if (!HARM[cfg.harmony || 'complementary']) throw new Error('Unknown harmony preset');
    loadedConfig = cfg;
    document.getElementById('theme-name').value = cfg.name || safeName;
    hEl.value = cfg.brandH ?? hEl.value;
    sEl.value = cfg.brandS ?? sEl.value;
    gsEl.value = cfg.greyS ?? gsEl.value;
    var target = document.querySelector('#harmPreset input[name=harm][value="' + (cfg.harmony || harmSel()) + '"]');
    if (target) target.checked = true;
    if (harmonySelect) harmonySelect.value = cfg.harmony || 'complementary';
    var semS = document.getElementById('semS');
    if (semS) semS.value = cfg.semanticS ?? semS.value;
    var semWS = document.getElementById('semWS');
    if (semWS) semWS.value = cfg.semanticWeakS ?? cfg.semanticS ?? semWS.value;
    root.style.removeProperty('--sem-l');
    root.style.removeProperty('--sem-weak-l');
    applyHarmony();
    render();
    document.getElementById('theme-list').value = safeName;
    showToast('Loaded ' + safeName);
  }

  async function saveTheme() {
    var name = sanitizeThemeName(document.getElementById('theme-name').value);
    if (!name || name === 'untitled') {
      showToast('Enter a valid theme name');
      return;
    }
    var cfg = currentThemeConfig();
    cfg.name = name;
    var res = await fetch('/api/themes/' + name, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(cfg)
    });
    var data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Unable to save theme');
    await refreshThemeList();
    document.getElementById('theme-name').value = name;
    document.getElementById('theme-list').value = name;
    showToast('Saved ' + name);
  }

  async function buildTheme() {
    var name = sanitizeThemeName(document.getElementById('theme-name').value || document.getElementById('theme-list').value);
    if (!name || name === 'untitled') {
      setBuildStatus('Choose a theme name before building.', true);
      return;
    }
    setBuildStatus('Building…', false);
    var res = await fetch('/api/build/' + name, { method: 'POST' });
    var data = await res.json();
    if (!res.ok) {
      setBuildStatus(data.error || 'Build failed', true);
      return;
    }
    setBuildStatus('Built: ', false);
    var output = document.getElementById('theme-build-output');
    ['theme.css', 'tokens.json'].forEach(function (file, i) {
      if (i) output.appendChild(document.createTextNode(' / '));
      var link = document.createElement('a');
      link.href = '/dist/' + encodeURIComponent(name) + '/' + file;
      link.textContent = 'dist/' + name + '/' + file;
      link.target = '_blank';
      link.rel = 'noreferrer';
      output.appendChild(link);
    });
    document.getElementById('theme-list').value = name;
  }

  document.getElementById('theme-save').addEventListener('click', function () {
    saveTheme().catch(function (err) { showToast(err.message || 'Save failed'); });
  });
  document.getElementById('theme-load').addEventListener('click', function () {
    var name = document.getElementById('theme-list').value || document.getElementById('theme-name').value;
    if (!name) { showToast('Choose a saved theme to load'); return; }
    loadTheme(name).catch(function (err) { showToast(err.message || 'Load failed'); });
  });
  document.getElementById('theme-list').addEventListener('change', function () {
    var name = this.value;
    if (!name) return;
    document.getElementById('theme-name').value = name;
    loadTheme(name).catch(function (err) { showToast(err.message || 'Load failed'); });
  });
  document.getElementById('theme-build').addEventListener('click', function () {
    buildTheme().catch(function (err) { setBuildStatus(err.message || 'Build failed', true); });
  });

  // theme toggle
  var btns = document.querySelectorAll('.theme-toggle button');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var mode = b.getAttribute('data-theme-set');
      btns.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      if (mode === 'system') root.removeAttribute('data-theme');
      else root.setAttribute('data-theme', mode);
      syncSemanticState();
    });
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', syncSemanticState);
  });

  // ---- parse any of: #hex, rgb(), hsl(), or a bare "10, 42, 61" triple ----
  function clamp(n, lo, hi) { return Math.min(hi, Math.max(lo, n)); }

  function rgbToHsl(r, g, b) {
    r /= 255; g /= 255; b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b), d = max - min;
    var h = 0, s = 0, l = (max + min) / 2;
    if (d !== 0) {
      s = d / (1 - Math.abs(2 * l - 1));
      switch (max) {
        case r: h = ((g - b) / d) % 6; break;
        case g: h = (b - r) / d + 2; break;
        default: h = (r - g) / d + 4;
      }
      h *= 60; if (h < 0) h += 360;
    }
    return { h: Math.round(h), s: Math.round(s * 100), l: Math.round(l * 100) };
  }

  function parseColor(raw) {
    var str = (raw || '').trim().toLowerCase();
    if (!str) return null;
    var m;
    // #rgb / #rrggbb
    if ((m = str.match(/^#?([0-9a-f]{3}|[0-9a-f]{6})$/))) {
      var hex = m[1];
      if (hex.length === 3) hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
      return rgbToHsl(parseInt(hex.slice(0,2),16), parseInt(hex.slice(2,4),16), parseInt(hex.slice(4,6),16));
    }
    // hsl(h s% l%) or hsl(h, s%, l%)
    if ((m = str.match(/^hsla?\(\s*([\d.]+)\s*[, ]\s*([\d.]+)%?\s*[, ]\s*([\d.]+)%?/))) {
      return { h: Math.round(+m[1]) % 360, s: clamp(Math.round(+m[2]), 0, 100), l: clamp(Math.round(+m[3]), 0, 100) };
    }
    // rgb(r g b), rgb(r,g,b), or bare "r,g,b" / "r g b"
    m = str.replace(/^rgba?\(/, '').match(/(\d{1,3})\s*[, ]\s*(\d{1,3})\s*[, ]\s*(\d{1,3})/);
    if (m) {
      return rgbToHsl(clamp(+m[1],0,255), clamp(+m[2],0,255), clamp(+m[3],0,255));
    }
    return null;
  }

  var seedIn = document.getElementById('seed-in');
  function applySeed() {
    var c = parseColor(seedIn.value);
    if (!c) { seedIn.classList.add('bad'); return; }
    seedIn.classList.remove('bad');
    hEl.value = c.h;
    sEl.value = c.s;               // seed the brand saturation from the colour
    // seed the grey saturation to ~1/6 of it, floored so greys stay tinted
    gsEl.value = clamp(Math.round(c.s / 6), 6, 40);
    root.style.setProperty('--seed-color', 'hsl(' + c.h + ' ' + c.s + '% ' + c.l + '%)');
    document.getElementById('seed-read').textContent = 'hsl(' + c.h + ' ' + c.s + '% ' + c.l + '%)';
    render();
  }
  document.getElementById('seed-apply').addEventListener('click', applySeed);
  seedIn.addEventListener('keydown', function (e) { if (e.key === 'Enter') applySeed(); });
  seedIn.addEventListener('input', function () { seedIn.classList.remove('bad'); });

  // hover-mode radio switches → swap the wrapper class
  var themeWrap = document.getElementById('themeWrap');
  document.getElementById('hovmodes').addEventListener('change', function (e) {
    if (e.target.name !== 'hovmode') return;
    themeWrap.className = 'hv-' + e.target.value;
  });

  // modifiers demo: family + hover-mode radios drive one wrapper
  var modWrap = document.getElementById('modWrap');
  var modState = { fam: 'brand', hov: 'flip' };
  function applyMod() { modWrap.className = 'fm-' + modState.fam + ' hv-' + modState.hov; }
  document.getElementById('modFam').addEventListener('change', function (e) {
    if (e.target.name === 'modfam') { modState.fam = e.target.value; applyMod(); }
  });
  document.getElementById('modHov').addEventListener('change', function (e) {
    if (e.target.name === 'modhov') { modState.hov = e.target.value; applyMod(); }
  });

  // icons demo: its own family + hover-mode radios
  var iconWrap = document.getElementById('iconWrap');
  var icState = { fam: 'brand', hov: 'flip' };
  function applyIcon() { iconWrap.className = 'fm-' + icState.fam + ' hv-' + icState.hov; }
  document.getElementById('icFam').addEventListener('change', function (e) {
    if (e.target.name === 'icfam') { icState.fam = e.target.value; applyIcon(); }
  });
  document.getElementById('icHov').addEventListener('change', function (e) {
    if (e.target.name === 'ichov') { icState.hov = e.target.value; applyIcon(); }
  });

  // card modifiers: family + fill-style radios
  var cardWrap = document.getElementById('cardWrap');
  var cardState = { fam: 'brand', style: 'tinted' };
  function applyCard() { cardWrap.className = 'cardgrid cfm-' + cardState.fam + ' cst-' + cardState.style; }
  document.getElementById('cFam').addEventListener('change', function (e) {
    if (e.target.name === 'cfam') { cardState.fam = e.target.value; applyCard(); }
  });
  document.getElementById('cStyle').addEventListener('change', function (e) {
    if (e.target.name === 'cstyle') { cardState.style = e.target.value; applyCard(); }
  });

  // depth: invert (reverse the elevation direction)
  var depthBox = document.getElementById('depthBox');
  document.getElementById('depthInvert').addEventListener('change', function (e) {
    depthBox.classList.toggle('invert', e.target.checked);
  });
  document.getElementById('depthFam').addEventListener('change', function (e) {
    if (e.target.name !== 'dfam') return;
    depthBox.classList.remove('dfm-grey', 'dfm-brand', 'dfm-gray');
    depthBox.classList.add('dfm-' + e.target.value);
  });

  // heading colour scheme: family + reverse + underline + bullet, with set-downstream
  var headWrap = document.getElementById('headWrap');
  var headState = { scheme: 'diagonal', dec: 'none', rev: false, bul: 'none', size: 'graded' };
  function schemeMods() {
    return 'hsc-' + headState.scheme +
      ' hdec-' + headState.dec +
      (headState.rev ? ' hrev' : '') +
      ' hbul-' + headState.bul +
      ' hsz-' + headState.size;
  }
  function applyHead() { headWrap.className = 'panel headings scheme ' + schemeMods(); }
  document.getElementById('headScheme').addEventListener('change', function (e) { if (e.target.name === 'hsc') { headState.scheme = e.target.value; applyHead(); } });
  document.getElementById('headDec').addEventListener('change', function (e) { if (e.target.name === 'hdec') { headState.dec = e.target.value; applyHead(); } });
  document.getElementById('headBul').addEventListener('change', function (e) { if (e.target.name === 'hbul') { headState.bul = e.target.value; applyHead(); } });
  document.getElementById('headSize').addEventListener('change', function (e) { if (e.target.name === 'hsz') { headState.size = e.target.value; applyHead(); } });
  document.getElementById('headRev').addEventListener('change', function (e) { headState.rev = e.target.checked; applyHead(); });
  var hScale = document.getElementById('headScale');
  hScale.addEventListener('input', function () {
    document.body.style.setProperty('--hscale', hScale.value);
    document.getElementById('headScale-val').textContent = (+hScale.value).toFixed(2) + '×';
  });
  // semantic formula sliders → set the shared knobs on :root
  [['semS', '--sem-s', '%'], ['semL', '--sem-l', '%'], ['semWS', '--sem-weak-s', '%'], ['semWL', '--sem-weak-l', '%']].forEach(function (cfg) {
    var el = document.getElementById(cfg[0]);
    el.addEventListener('input', function () {
      document.documentElement.style.setProperty(cfg[1], el.value + cfg[2]);
      document.getElementById(cfg[0] + '-val').textContent = el.value + cfg[2];
    });
  });

  // callout family + fill-style radios
  var calloutWrap = document.getElementById('calloutWrap');
  var coState = { fam: 'brand', style: 'tinted' };
  function applyCallout() { calloutWrap.className = 'cofm-' + coState.fam + ' cost-' + coState.style; }
  document.getElementById('coFam').addEventListener('change', function (e) { if (e.target.name === 'cofam') { coState.fam = e.target.value; applyCallout(); } });
  document.getElementById('coStyle').addEventListener('change', function (e) { if (e.target.name === 'costyle') { coState.style = e.target.value; applyCallout(); } });

  // accordion: toggle the .collapsed class (CSS handles show/hide + chevron)
  document.querySelectorAll('.ab.accordion .accordion-button').forEach(function (btn) {
    btn.addEventListener('click', function () { btn.classList.toggle('collapsed'); });
  });

  var pageWrap = document.querySelector('.wrap');
  document.getElementById('setDownstream').addEventListener('click', function () {
    pageWrap.className = 'wrap scheme ' + schemeMods();   // stamp the scheme onto the whole page
    var ds = document.getElementById('downstream');
    ds.classList.add('downstream-flash');
    setTimeout(function () { ds.classList.remove('downstream-flash'); }, 500);
  });

  hEl.addEventListener('input', render);
  sEl.addEventListener('input', render);
  gsEl.addEventListener('input', render);
  document.querySelectorAll('#harmPreset input[name=harm]').forEach(function (r) {
    r.addEventListener('change', function () { applyHarmony(); render(); });
  });
  if (harmonySelect) harmonySelect.addEventListener('change', function () { applyHarmony(); render(); });
  if (location.protocol === 'file:') {
    ['theme-save', 'theme-load', 'theme-build', 'theme-list'].forEach(function (id) {
      document.getElementById(id).disabled = true;
    });
    setBuildStatus('Live demos work here. Open this page through the Node studio server to Save, Load or Build.', false);
  } else {
    refreshThemeList().catch(function (err) { setBuildStatus(err.message, true); });
  }
  applyHarmony();   // sync data-harmony with the checked preset
  applySeed();      // boot from the seed field so hue/sat/grey all agree
  render();
})();
