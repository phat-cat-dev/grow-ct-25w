(function () {
  var api = window.ABColor;
  var state = api.defaultColorSystem();
  var candidateBase;
  var cancellingColourEdit = false;
  var previewStyle = document.createElement('style');
  document.head.appendChild(previewStyle);
  var root = document.documentElement;
  var byId = function (id) { return document.getElementById(id); };
  var sourceInputs = ['color-demo-h', 'color-demo-s', 'color-demo-gs'];
  var harmonyRadios = document.querySelectorAll('#color-demo-harmPreset input[type="radio"]');
  function isDark() {
    return root.dataset.theme === 'dark' || (!root.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
  }
  function setInput(id, value, suffix) {
    var input = byId(id);
    input.value = value;
    var label = byId(id + '-val') || byId(id + '-value');
    if (label) label.textContent = value + suffix;
  }
  function fillRamp(container, palette, saturation, stacked, system, family) {
    container.replaceChildren();
    api.COLOR_STOPS.forEach(function (stop) {
      var button = document.createElement('button');
      var light = api.paletteLightness(palette, stop[1]);
      var color = 'hsl(' + palette.h + ' ' + saturation + '% ' + light + '%)';
      button.type = 'button';
      button.className = stacked ? 'ramp-step' : 'sw';
      button.dataset.colorLive = '';
      button.dataset.rampSystem = system;
      button.dataset.rampFamily = family;
      button.dataset.rampStep = stop[0];
      button.style.background = color;
      button.style.color = light > 55 ? '#171717' : '#ffffff';
      button.textContent = stop[0] + ' · ' + light + '%';
      var active = state.main === system && state.mainShade && state.mainShade.family === family && state.mainShade.step === stop[0];
      button.setAttribute('aria-pressed', String(!!active));
      button.title = 'Use ' + color + ' as the main accent';
      button.setAttribute('aria-label', system + ' ' + family + ' ' + stop[0] + ': use ' + color + ' as main accent');
      button.addEventListener('click', function () {
        state.main = system;
        state.mainShade = { family: family, step: stop[0], h: palette.h, s: saturation, l: light };
        if (!state.included.includes(system)) state.included.push(system);
        render();
        document.querySelector('[data-ramp-system="' + system + '"][data-ramp-family="' + family + '"][data-ramp-step="' + stop[0] + '"]').focus({ preventScroll: true });
      });
      container.appendChild(button);
    });
  }
  function render() {
    api.validateColorSystem(state);
    // Preview every stage; the exported CSS only contains the selected layers.
    previewStyle.textContent = api.colorSystemCss(Object.assign({}, state, { included: api.COLOR_SYSTEMS.slice() }));
    sourceInputs.forEach(function (id, i) { setInput(id, state.source[['h', 's', 'gs'][i]], i ? '%' : '°'); });
    byId('color-brand-remix-status').textContent = 'Hue ' + state.brand.h + '° · Saturation ' + state.brand.s + '% · Color-grey ' + state.brand.gs + '% · Tone ' + (state.brand.tone ?? 0);
    ['brand', 'grey', 'gray'].forEach(function (family, i) {
      fillRamp(byId('color-demo-' + family + '-scale'), state.source, [state.source.s, state.source.gs, 0][i], false, 'hsl', family);
    });
    var scaleRow = byId('color-demo-scaleRow');
    scaleRow.replaceChildren();
    ['Brand', 'Color-grey', 'Pure grey'].forEach(function (name, i) {
      var column = document.createElement('div');
      column.className = 'refined-ramp';
      var label = document.createElement('strong');
      label.textContent = name;
      var ramp = document.createElement('div');
      fillRamp(ramp, state.brand, [state.brand.s, state.brand.gs, 0][i], true, 'brand', ['brand', 'grey', 'gray'][i]);
      column.append(label, ramp);
      scaleRow.appendChild(column);
    });
    harmonyRadios.forEach(function (radio) { radio.checked = radio.value === state.harmony; });
    var theory = byId('color-3-0-color-theory');
    var swatches = byId('color-demo-harmSwatches');
    var demos = theory.querySelector('.harm-demo');
    var mainHue = byId('color-main-hue');
    swatches.replaceChildren();
    demos.replaceChildren();
    mainHue.replaceChildren();
    byId('color-demo-harmony-count').value = state.harmonyCount ?? 4;
    var foundation = state.baseColor || state.brand;
    api.harmonyPalette(state).forEach(function (entry, i) {
      var offset = entry.offset;
      var swatch = document.createElement('button');
      swatch.type = 'button';
      swatch.dataset.colorLive = '';
      swatch.className = 'hsw';
      swatch.style.setProperty('--swatch-color', 'var(--theme-harmony-' + (i + 1) + ')');
      swatch.setAttribute('aria-pressed', String(state.main === 'harmony' && !!state.mainShade && state.harmonyHue === i + 1));
      swatch.addEventListener('click', function () {
        var baseLightness = parseFloat(getComputedStyle(root).getPropertyValue('--acc-l'));
        if (!Number.isFinite(baseLightness)) {
          byId('color-selection-status').textContent = 'Cannot select this harmony colour: the active accent lightness is invalid.';
          return;
        }
        state.mainShade = {
          family: 'harmony', step: i + 1,
          h: (foundation.h + offset + 360) % 360, s: Math.round(foundation.s * (entry.saturation ?? 1) * 10) / 10,
          l: entry.absoluteLightness ?? Math.max(10, Math.min(90, baseLightness + entry.lightness)),
        };
        state.harmonyHue = i + 1;
        state.main = 'harmony';
        if (!state.included.includes('harmony')) state.included.push('harmony');
        render();
        byId('color-demo-harmSwatches').children[i].focus({ preventScroll: true });
      });
      var label = document.createElement('span');
      label.textContent = i ? 'Colour ' + (i + 1) : 'Base';
      var hue = document.createElement('b');
      hue.dataset.hue = i + 1;
      hue.textContent = ((foundation.h + offset + 360) % 360) + '°';
      if (entry.absoluteLightness !== undefined) {
        hue.textContent += ' · S ' + (Math.round(foundation.s * entry.saturation * 10) / 10) + '% · L ' + entry.absoluteLightness + '%';
        swatch.style.setProperty('--swatch-foreground', entry.absoluteLightness > 55 ? '#171717' : '#ffffff');
      }
      swatch.setAttribute('aria-label', label.textContent + ': ' + hue.textContent + '. Use as main accent');
      swatch.title = swatch.getAttribute('aria-label');
      var glyph = document.createElement('span');
      glyph.className = 'material-symbol';
      glyph.setAttribute('aria-hidden', 'true');
      glyph.textContent = ['filter_vintage', 'local_florist', 'ac_unit', 'diamond', 'auto_awesome', 'brightness_7', 'filter_tilt_shift', 'flare', 'blur_on', 'radio_button_checked'][i];
      swatch.appendChild(glyph);
      swatches.appendChild(swatch);
      var card = document.createElement('div');
      card.className = 'hue-' + (i + 1) + ' harm-card';
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'demobtn';
      button.dataset.colorLive = '';
      button.textContent = label.textContent;
      var text = document.createElement('div');
      text.append('Rethemed subtree — ');
      var link = document.createElement('a');
      link.href = '#color-3-0-color-theory';
      link.textContent = 'a link';
      text.append(link, ' & accents.');
      card.append(button, text);
      demos.appendChild(card);
      var option = document.createElement('option');
      option.value = i + 1;
      option.textContent = 'Colour ' + (i + 1);
      mainHue.appendChild(option);
    });
    var semantics = api.semanticSettings(state);
    document.querySelectorAll('[data-semantic-preset]').forEach(function (radio) { radio.checked = radio.value === (state.semanticPreset ?? 'default'); });
    document.querySelectorAll('[data-semantic-appearance]').forEach(function (radio) { radio.checked = radio.value === (state.semanticAppearance ?? 'default'); });
    setInput('color-demo-semS', semantics.s, '%');
    setInput('color-demo-semWS', semantics.weakS, '%');
    var mode = isDark() ? 'dark' : 'light';
    var semanticSection = byId('color-4-0-semantic-tuning');
    semanticSection.querySelectorAll('[data-semantic-role]').forEach(function (button) {
      var active = state.main === 'semantics' && state.mainShade && state.mainShade.family === button.dataset.semanticRole && state.mainShade.step === button.dataset.semanticStrength;
      button.setAttribute('aria-pressed', String(!!active));
      button.title = 'Use this exact semantic colour as the main accent';
      button.style.setProperty('--_fg', 'var(--' + button.dataset.semanticRole + (button.dataset.semanticStrength === 'weak' ? '-weak' : '') + '-foreground)');
    });
    setInput('color-demo-semL', semantics[mode].strong, '%');
    setInput('color-demo-semWL', semantics[mode].weak, '%');
    byId('color-semantic-mode').textContent = 'Following ' + (state.main === 'semantics' ? 'section 2 remix (Semantics is main)' : state.main) + '. Editing ' + mode + '-mode brightness; adjustments stay relative to the main palette.';
    byId('color-semantic-values').textContent = Object.keys(api.SEMANTIC_BANDS).map(function (role) {
      return role + ': ' + api.semanticHue(role) + '° (locked)';
    }).join(' · ');
    byId('color-main').value = state.main;
    document.querySelectorAll('[data-color-main]').forEach(function (button) {
      var active = button.dataset.colorMain === state.main;
      button.setAttribute('aria-pressed', String(active));
      button.textContent = 'Set as base theme';
      button.title = 'Set this selection as the fixed foundation. Other colour controls remain editable.';
    });
    byId('color-main-hue').value = state.harmonyHue;
    byId('color-main-hue').disabled = state.main !== 'harmony';
    byId('color-main-role').value = state.semanticRole;
    byId('color-main-role').disabled = state.main !== 'semantics';
    document.querySelectorAll('[data-color-include]').forEach(function (input) {
      input.checked = state.included.includes(input.dataset.colorInclude);
      input.disabled = input.dataset.colorInclude === state.main;
    });
    byId('color-theme-preview').textContent = api.colorSystemCss(state);
    var ingredient = byId('color-2-0-brand-tuner').querySelector('pre');
    ingredient.textContent = ':root { --brand-h: ' + state.brand.h + '; --brand-s: ' + state.brand.s + '%; --grey-s: ' + state.brand.gs + '%; }';
    var main = api.mainColor(Object.assign({}, state, { baseColor: undefined }));
    if (state.main === 'harmony' && !state.mainShade && state.baseColor) {
      var candidateEntry = api.harmonyPalette(state)[state.harmonyHue - 1];
      main.h = (foundation.h + candidateEntry.offset + 360) % 360;
      main.s = Math.round(foundation.s * (candidateEntry.saturation ?? 1) * 10) / 10;
    }
    var lightness = main.l;
    if (lightness === undefined) {
      lightness = parseFloat(getComputedStyle(root).getPropertyValue('--acc-l'));
      if (state.main === 'semantics') lightness = semantics[mode].strong;
      if (state.main === 'harmony') {
        var selectedEntry = api.harmonyPalette(state)[state.harmonyHue - 1];
        lightness = selectedEntry.absoluteLightness ?? Math.max(10, Math.min(90, lightness + selectedEntry.lightness));
      }
    }
    if (!Number.isFinite(lightness)) throw new Error('Cannot display the active source: invalid accent lightness.');
    candidateBase = { h: main.h, s: main.s, l: lightness, gs: main.gs };
    if (state.baseColor) {
      main = state.baseColor;
      lightness = main.l;
    }
    var sourceColour = 'hsl(' + main.h + ' ' + main.s + '% ' + lightness + '%)';
    var sourceCanvas = document.createElement('canvas');
    sourceCanvas.width = sourceCanvas.height = 1;
    var sourceContext = sourceCanvas.getContext('2d');
    if (!sourceContext) throw new Error('Active source colour display requires browser canvas support.');
    sourceContext.fillStyle = sourceColour;
    sourceContext.fillRect(0, 0, 1, 1);
    var sourceRgb = Array.from(sourceContext.getImageData(0, 0, 1, 1).data).slice(0, 3);
    var sourceHex = '#' + sourceRgb.map(function (channel) { return ('0' + channel.toString(16)).slice(-2); }).join('');
    var hslReadout = byId('active-source-hsltext');
    if (hslReadout) hslReadout.textContent = sourceColour;
    var rgbReadout = byId('active-source-rgb');
    if (rgbReadout) rgbReadout.textContent = 'rgb(' + sourceRgb.join(' ') + ')';
    byId('active-source-chip').style.backgroundColor = sourceColour;
    var luminance = sourceRgb.map(function (channel) {
      var value = channel / 255;
      return value <= .04045 ? value / 12.92 : Math.pow((value + .055) / 1.055, 2.4);
    }).reduce(function (sum, value, index) { return sum + value * [.2126, .7152, .0722][index]; }, 0);
    byId('active-source-chip').style.color = (luminance + .05) / .05 >= 1.05 / (luminance + .05) ? '#000' : '#fff';
    byId('color-brand-remix').style.setProperty('--remix-colour', sourceColour);
    byId('color-brand-remix').style.setProperty('--remix-foreground', byId('active-source-chip').style.color);
    if (document.activeElement !== byId('active-source-hsl')) {
      byId('active-source-hsl').value = sourceHex.toUpperCase();
      byId('active-source-hsl').removeAttribute('aria-invalid');
    }
    byId('active-source-hsl').disabled = !!state.baseColor;
    byId('active-source-chip').title = state.baseColor ? 'Unlock the base colour to paste a new colour' : 'Paste a CSS colour; press Enter or leave the field to apply';
    var lockButton = byId('base-colour-lock');
    lockButton.setAttribute('aria-pressed', String(!!state.baseColor));
    lockButton.setAttribute('aria-label', state.baseColor ? 'Unlock base colour - colour selections will update the live theme' : 'Lock current colour as base theme');
    lockButton.title = lockButton.getAttribute('aria-label');
    lockButton.querySelector('.material-symbol').textContent = state.baseColor ? 'lock' : 'lock_open';
    byId('colour-random').disabled = !!state.baseColor;
    byId('colour-random').title = state.baseColor ? 'Unlock the base colour to randomise the theme' : 'Randomise colour theme';
    document.querySelectorAll('#color-content input, #color-content select, #color-content button').forEach(function (control) {
      if (control.matches('.outline-trigger, [data-theme-export], [data-theme-tools]')) return;
      if (control.hasAttribute('data-color-main')) {
        control.disabled = false;
      } else if (control.id === 'color-main-hue') {
        control.disabled = state.main !== 'harmony';
      } else if (control.id === 'color-main-role') {
        control.disabled = state.main !== 'semantics';
      } else if (control.hasAttribute('data-color-include')) {
        control.disabled = control.dataset.colorInclude === state.main;
      } else {
        control.disabled = false;
      }
    });
    byId('color-selection-status').textContent = 'Main: ' + state.main + (state.mainShade ? ' / ' + state.mainShade.family + ' ' + state.mainShade.step : '') + ' · hsl(' + main.h.toFixed(1) + ' ' + main.s + '%' + (main.l !== undefined ? ' ' + main.l + '%' : '') + ') · Included: ' + state.included.join(', ');
  }
  function regenerate() {
    delete state.mainShade;
    state.source = { h: +byId(sourceInputs[0]).value, s: +byId(sourceInputs[1]).value, gs: +byId(sourceInputs[2]).value };
    state.brand = Object.assign({}, state.source);
    render();
  }
  byId('base-colour-lock').addEventListener('click', function () {
    if (state.baseColor) delete state.baseColor;
    else state.baseColor = Object.assign({}, candidateBase);
    delete state.locked;
    byId('active-source-status').textContent = state.baseColor ? 'Colour locked. Unlock to edit or paste a new colour.' : 'Colour unlocked. Paste a colour and press Enter to apply.';
    render();
  });
  byId('colour-random').addEventListener('click', function () {
    if (state.baseColor) return;
    state = api.randomizeColorSystem(state);
    render();
    byId('color-selection-status').textContent = 'Random colour theme generated. ' + byId('color-selection-status').textContent;
  });
  sourceInputs.forEach(function (id) { byId(id).addEventListener('input', regenerate); });
  byId('color-brand-remix').addEventListener('click', function () {
    delete state.mainShade;
    state.brand = api.remixBrand(state.source, state.brand);
    render();
  });
  function parseColour(input, status) {
    var raw = input.value.trim();
    var valid = /^#?(?:[\da-f]{3}|[\da-f]{6})$/i.test(raw);
    var text = valid ? '#' + raw.replace(/^#/, '') : raw;
    if (/^\d{1,3}\s*[, ]\s*\d{1,3}\s*[, ]\s*\d{1,3}$/.test(raw)) text = 'rgb(' + raw + ')';
    if (!text || /^(?:currentcolor|inherit|initial|unset|revert(?:-layer)?)$|var\(|env\(|light-dark\(/i.test(text) || !CSS.supports('color', text)) {
      input.setAttribute('aria-invalid', 'true');
      status.textContent = 'Enter a valid hex, rgb(), hsl() or other absolute CSS colour.';
      return null;
    }
    var canvas = document.createElement('canvas');
    var context = canvas.getContext('2d');
    if (!context) throw new Error('Colour parsing requires browser canvas support.');
    context.fillStyle = text;
    context.fillRect(0, 0, 1, 1);
    var rgb = context.getImageData(0, 0, 1, 1).data;
    if (rgb[3] !== 255) {
      input.setAttribute('aria-invalid', 'true');
      status.textContent = 'Use an opaque colour, without transparency.';
      return null;
    }
    var r = rgb[0] / 255, g = rgb[1] / 255, b = rgb[2] / 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b), delta = max - min;
    var light = (max + min) / 2, hue = 0, sat = 0;
    if (delta) {
      sat = delta / (1 - Math.abs(2 * light - 1));
      hue = max === r ? ((g - b) / delta) % 6 : max === g ? (b - r) / delta + 2 : (r - g) / delta + 4;
    }
    input.removeAttribute('aria-invalid');
    return { h: +((hue * 60 + 360) % 360).toFixed(4), s: +(sat * 100).toFixed(4), l: +(light * 100).toFixed(4), gs: Math.max(6, Math.min(40, Math.round(sat * 100 / 6))), css: text };
  }
  function sourceColourToHex(css) {
    var hx = document.createElement('canvas');
    hx.width = hx.height = 1;
    var hc = hx.getContext('2d');
    if (!hc) return css;
    hc.fillStyle = css;
    hc.fillRect(0, 0, 1, 1);
    var px = hc.getImageData(0, 0, 1, 1).data;
    return ('#' + [px[0], px[1], px[2]].map(function (channel) { return ('0' + channel.toString(16)).slice(-2); }).join('')).toUpperCase();
  }
  function applyActiveColour() {
    if (cancellingColourEdit) return;
    var input = byId('active-source-hsl');
    var status = byId('active-source-status');
    if (state.baseColor) {
      status.textContent = 'Colour locked. Unlock before applying a new colour.';
      return;
    }
    var colour = parseColour(input, status);
    if (!colour) return;
    state.source = { h: colour.h, s: colour.s, gs: colour.gs };
    state.brand = Object.assign({}, state.source);
    state.main = 'brand';
    state.mainShade = { family: 'brand', step: 'custom', h: colour.h, s: colour.s, l: colour.l };
    if (!state.included.includes('brand')) state.included.push('brand');
    render();
    input.value = sourceColourToHex('hsl(' + colour.h + ' ' + colour.s + '% ' + colour.l + '%)');
    status.textContent = 'Applied ' + colour.css + ' as the main colour. Lock it to keep it fixed.';
  }
  byId('active-source-hsl').addEventListener('change', applyActiveColour);
  byId('active-source-hsl').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      applyActiveColour();
    } else if (event.key === 'Escape') {
      cancellingColourEdit = true;
      this.blur();
      cancellingColourEdit = false;
      this.removeAttribute('aria-invalid');
      render();
      byId('active-source-status').textContent = 'Colour edit cancelled.';
    }
  });
  function applySeed() {
    var input = byId('color-demo-seed-in');
    var colour = parseColour(input, byId('color-demo-seed-read'));
    if (!colour) return;
    state.source = { h: Math.round(colour.h), s: Math.round(colour.s), gs: colour.gs };
    delete state.mainShade;
    state.brand = Object.assign({}, state.source);
    input.removeAttribute('aria-invalid');
    byId('color-demo-seed-read').textContent = 'hsl(' + state.source.h + ' ' + state.source.s + '% ' + Math.round(colour.l) + '%)';
    byId('color-demo-seed-chip').style.setProperty('--seed-color', colour.css);
    render();
  }
  byId('color-demo-seed-apply').addEventListener('click', applySeed);
  byId('color-seed-set-base').addEventListener('click', function () {
    regenerate();
    var color = 'hsl(' + state.source.h + ' ' + state.source.s + '% 50%)';
    var input = byId('color-demo-seed-in');
    input.value = color;
    input.removeAttribute('aria-invalid');
    byId('color-demo-seed-read').textContent = color;
    byId('color-demo-seed-chip').style.setProperty('--seed-color', color);
    byId('color-selection-status').textContent = 'New base set from the current sliders. Stage 2 now matches stage 1.';
  });
  byId('color-demo-seed-in').addEventListener('keydown', function (event) { if (event.key === 'Enter') applySeed(); });
  harmonyRadios.forEach(function (radio) { radio.addEventListener('change', function () { if (this.checked) { if (state.main === 'harmony') delete state.mainShade; state.harmony = this.value; render(); } }); });
  byId('color-demo-harmony-count').addEventListener('change', function () {
    if (state.main === 'harmony') delete state.mainShade;
    state.harmonyCount = +this.value;
    state.harmonyHue = Math.min(state.harmonyHue, state.harmonyCount);
    render();
  });
  [['semS', 'semanticS'], ['semWS', 'semanticWeakS'], ['semL', 'strong'], ['semWL', 'weak']].forEach(function (pair) {
    byId('color-demo-' + pair[0]).addEventListener('input', function () {
      var settings = api.semanticSettings(state);
      if (!state.semanticAdjustments) {
        state.semanticAdjustments = {
          s: settings.s - settings.base.s, weakS: settings.weakS - settings.base.weakS,
          light: { strong: settings.light.strong - settings.base.light.strong, weak: settings.light.weak - settings.base.light.weak },
          dark: { strong: settings.dark.strong - settings.base.dark.strong, weak: settings.dark.weak - settings.base.dark.weak },
        };
      }
      if (pair[1] === 'strong' || pair[1] === 'weak') {
        var mode = isDark() ? 'dark' : 'light';
        state.semanticAdjustments[mode][pair[1]] = +this.value - settings.base[mode][pair[1]];
      } else {
        var key = pair[1] === 'semanticS' ? 's' : 'weakS';
        state.semanticAdjustments[key] = +this.value - settings.base[key];
      }
      render();
    });
    document.querySelectorAll('[data-semantic-preset]').forEach(function (radio) {
      radio.addEventListener('change', function () {
        if (!this.checked) return;
        if (state.main === 'semantics') delete state.mainShade;
        state.semanticPreset = this.value;
        state.semanticAdjustments = { s: 0, weakS: 0, light: { strong: 0, weak: 0 }, dark: { strong: 0, weak: 0 } };
        render();
        byId('color-selection-status').textContent = 'Semantic preset applied: ' + this.value + '. Slider adjustments reset; base lock preserved.';
      });
    });
    document.querySelectorAll('[data-semantic-appearance]').forEach(function (radio) {
      radio.addEventListener('change', function () {
        if (!this.checked) return;
        state.semanticAppearance = this.value;
        render();
        byId('color-selection-status').textContent = 'Semantic button and badge appearance: ' + this.value + '.';
      });
    });
  });
  byId('color-main').addEventListener('change', function () {
    delete state.mainShade;
    state.main = this.value;
    if (!state.included.includes(state.main)) state.included.push(state.main);
    render();
  });
  byId('color-main-hue').addEventListener('change', function () { byId('color-demo-harmSwatches').children[+this.value - 1].click(); });
  byId('color-main-role').addEventListener('change', function () { delete state.mainShade; state.semanticRole = this.value; render(); });
  document.querySelectorAll('[data-semantic-role]').forEach(function (button) {
    button.addEventListener('click', function () {
      var settings = api.semanticSettings(state);
      var strength = this.dataset.semanticStrength;
      var role = this.dataset.semanticRole;
      state.mainShade = { family: role, step: strength, h: api.semanticHue(role), s: strength === 'weak' ? settings.weakS : settings.s, l: settings[isDark() ? 'dark' : 'light'][strength] };
      state.main = 'semantics';
      state.semanticRole = role;
      if (!state.included.includes('semantics')) state.included.push('semantics');
      render();
    });
  });
  document.querySelectorAll('[data-color-include]').forEach(function (input) {
    input.addEventListener('change', function () {
      var name = this.dataset.colorInclude;
      if (this.checked && !state.included.includes(name)) state.included.push(name);
      else if (!this.checked && name !== state.main) state.included = state.included.filter(function (system) { return system !== name; });
      render();
    });
  });
  document.querySelectorAll('[data-color-main]').forEach(function (button) {
    button.addEventListener('click', function () {
      if (state.main !== this.dataset.colorMain) delete state.mainShade;
      state.main = this.dataset.colorMain;
      if (!state.included.includes(state.main)) state.included.push(state.main);
      render();
      state.baseColor = Object.assign({}, candidateBase);
      delete state.locked;
      render();
    });
  });
  new MutationObserver(render).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', render);
  document.querySelectorAll('#color-content input, #color-content select, #color-content button').forEach(function (control) { control.dataset.colorLive = ''; });
  window.ABColorTheme = {
    get: function () { return JSON.parse(JSON.stringify(state)); },
    css: function () { return api.colorSystemCss(state); },
    load: function (config) { state = JSON.parse(JSON.stringify(api.validateColorSystem(config.colorSystem || api.defaultColorSystem(config)))); render(); },
  };
  render();
})();
