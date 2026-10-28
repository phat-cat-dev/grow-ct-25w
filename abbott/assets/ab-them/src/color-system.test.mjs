import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { defaultColorSystem, randomizeColorSystem, semanticHue, SEMANTIC_BANDS, SEMANTIC_PRESETS, SEMANTIC_APPEARANCES, colorSystemCss, mainColor, COLOR_HARMONIES, validateColorSystem, harmonyPalette, remixBrand, paletteLightness, COLOR_STOPS, semanticSettings } from '../public/site/color-system.js';
import { buildTokens } from './tokens.js';
import { emitCss } from './emit-css.js';

test('custom pasted colours retain exact lightness through save and CSS export', () => {
  const state = defaultColorSystem();
  state.main = 'brand';
  state.mainShade = { family: 'brand', step: 'custom', h: 210, s: 65.3846, l: 40.7843 };
  const restored = validateColorSystem(JSON.parse(JSON.stringify(state)));
  assert.equal(mainColor(restored).l, 40.7843);
  assert.equal(mainColor(restored).h, 210);
  assert.ok(colorSystemCss(restored).includes('40.7843%'));
  assert.ok(emitCss(buildTokens({ colorSystem: restored }), '', '', undefined, restored).includes(colorSystemCss(restored)));
  state.mainShade.step = 'unknown';
  assert.throws(() => validateColorSystem(state), /Invalid selected main shade/);
});

test('harmony card preview precedes its modifiers without duplication', async () => {
  const source = await readFile(new URL('../public/site/01_color.md', import.meta.url), 'utf8');
  assert.equal((source.match(/class="harmony-demo-panel"/g) || []).length, 1);
  assert.ok(source.indexOf('class="harmony-demo-panel"') < source.indexOf('class="harmony-preset-panel"'));
});

test('random themes replace exact selections without mutating inputs and survive JSON and CSS export', () => {
  for (const random of [() => 0, () => 0.5, () => 1 - Number.EPSILON]) {
    const state = defaultColorSystem();
    state.main = 'hsl';
    state.included = ['hsl'];
    state.mainShade = { family: 'brand', step: 500, h: 22, s: 50, l: 48 };
    state.semanticAdjustments.s = 10;
    const before = JSON.stringify(state);
    const next = randomizeColorSystem(state, random);
    assert.equal(JSON.stringify(state), before);
    assert.notEqual(mainColor(next).h, mainColor(state).h);
    assert.equal(next.main, 'brand');
    assert.equal(next.mainShade, undefined);
    assert.deepEqual(next.included, ['hsl', 'brand']);
    assert.deepEqual(next.semanticAdjustments, defaultColorSystem().semanticAdjustments);
    assert.ok(next.harmonyCount >= 3 && next.harmonyCount <= 10);
    assert.ok(Object.hasOwn(COLOR_HARMONIES, next.harmony));
    const restored = validateColorSystem(JSON.parse(JSON.stringify(next)));
    assert.ok(emitCss(buildTokens({ colorSystem: restored }), '', '', undefined, restored).includes(colorSystemCss(next)));
    assert.notEqual(mainColor(randomizeColorSystem(next, random)).h, mainColor(next).h);
  }
});

test('selecting a semantic shade does not compound its preset or relative adjustments', () => {
  for (const semanticPreset of Object.keys(SEMANTIC_PRESETS)) {
    const state = { ...defaultColorSystem(), main: 'semantics', semanticPreset };
    state.semanticAdjustments.s = 8;
    const settings = semanticSettings(state);
    state.mainShade = { family: 'positive', step: 'strong', h: 145, s: settings.s, l: settings.light.strong };
    assert.deepEqual(semanticSettings(state), settings);
    assert.equal(mainColor(state).s, settings.s);
    assert.equal(mainColor(state).l, settings.light.strong);
  }
});

test('random themes respect a fixed base without consuming randomness', () => {
  const state = defaultColorSystem();
  state.baseColor = { h: 202, s: 72, l: 48, gs: 12 };
  const before = JSON.stringify(state);
  assert.equal(randomizeColorSystem(state, () => { throw new Error('Should not randomise'); }), state);
  assert.equal(JSON.stringify(state), before);
  assert.throws(() => randomizeColorSystem({}), /Invalid/);
});

test('semantic presets transform the foundation before offsets without changing meaning hues or a locked base', () => {
  const original = defaultColorSystem();
  const baseline = semanticSettings(original);
  for (const semanticPreset of Object.keys(SEMANTIC_PRESETS)) {
    for (const s of [0, 50, 100]) {
      const state = { ...original, semanticPreset, baseColor: { h: 310, s, l: 48, gs: 12 } };
      const settings = semanticSettings(state);
      assert.deepEqual(mainColor(state), state.baseColor);
      for (const mode of ['light', 'dark']) {
        for (const value of [settings.s, settings.weakS, settings[mode].strong, settings[mode].weak]) {
          assert.ok(Number.isFinite(value) && value >= 0 && value <= 100);
        }
      }
      const css = colorSystemCss(state);
      for (const role of Object.keys(SEMANTIC_BANDS)) assert.ok(css.includes(`--${role}-h: ${semanticHue(role)};`));
      assert.ok(css.includes('--accent: hsl(310'));
    }
    const state = { ...original, semanticPreset };
    const settings = semanticSettings(state);
    state.semanticAdjustments = { ...original.semanticAdjustments, s: -5 };
    assert.equal(semanticSettings(state).s, Math.max(0, settings.base.s - 5));
  }
  assert.ok(semanticSettings({ ...original, semanticPreset: 'muted' }).s < baseline.s);
  assert.ok(semanticSettings({ ...original, semanticPreset: 'vivid' }).s > baseline.s);
  assert.ok(semanticSettings({ ...original, semanticPreset: 'pastel' }).light.strong > baseline.light.strong);
  assert.ok(semanticSettings({ ...original, semanticPreset: 'high-contrast' }).light.strong < baseline.light.strong);
});

test('semantic modifiers persist, export only with their layer, and support legacy themes', () => {
  for (const semanticPreset of Object.keys(SEMANTIC_PRESETS)) {
    for (const semanticAppearance of SEMANTIC_APPEARANCES) {
      const state = { ...defaultColorSystem(), semanticPreset, semanticAppearance };
      const restored = validateColorSystem(JSON.parse(JSON.stringify(state)));
      const css = colorSystemCss(restored);
      assert.equal(css, colorSystemCss(state));
      assert.ok(emitCss(buildTokens({ colorSystem: restored }), '', '', undefined, restored).includes(css));
      assert.ok(css.includes('--positive-foreground:'));
      assert.ok(!css.includes('undefined'));
      if (semanticAppearance !== 'default') {
        assert.ok(css.includes('border: 1px solid var(--semantic-colour);'));
        assert.ok(css.includes('forced-colors: active'));
        assert.ok(css.includes(':not(.outline):not(.soft):not(.link)'));
      }
      state.included = ['brand'];
      assert.ok(!colorSystemCss(state).includes('--semantic-colour:'));
    }
  }
  const state = defaultColorSystem();
  const css = colorSystemCss(state);
  delete state.semanticPreset;
  delete state.semanticAppearance;
  assert.equal(colorSystemCss(validateColorSystem(state)), css);
  delete state.semanticAdjustments;
  const legacy = semanticSettings(state);
  assert.equal(legacy.s, state.semanticS);
  state.semanticPreset = 'muted';
  assert.equal(semanticSettings(state).s, Math.round(legacy.s * .55 * 10) / 10);
  for (const patch of [{ semanticPreset: 'bad' }, { semanticPreset: null }, { semanticAppearance: 'bad' }, { semanticAppearance: null }]) {
    assert.throws(() => validateColorSystem({ ...state, ...patch }), /Invalid semantic/);
  }
});

test('exact ramp shades persist through JSON and theme builds without changing the upstream palettes', () => {
  for (const main of ['hsl', 'brand']) {
    for (const family of ['brand', 'grey', 'gray']) {
      const state = defaultColorSystem();
      const original = JSON.stringify([state.source, state.brand]);
      state.main = main;
      state.mainShade = { family, step: 900, h: 316, s: family === 'gray' ? 0 : 33, l: 19.8 };
      const restored = validateColorSystem(JSON.parse(JSON.stringify(state)));
      assert.equal(mainColor(restored).l, 19.8);
      assert.equal(mainColor(restored).s, state.mainShade.s);
      assert.equal(JSON.stringify([state.source, state.brand]), original);
      const css = colorSystemCss(restored);
      assert.ok(css.includes(`--accent: hsl(316 ${state.mainShade.s}% 19.8%);`));
      assert.ok(css.includes('--on-accent: #fff;'));
      assert.ok(css.includes(':root[data-theme]'));
      assert.ok(css.includes(':root .ab.btn.primary'));
      const built = emitCss(buildTokens({ colorSystem: restored }), '/* template */', '', undefined, restored);
      assert.ok(built.includes(css));
      delete restored.mainShade;
      assert.ok(!colorSystemCss(restored).includes('Exact selected shade'));
    }
  }
});

test('exact semantic selections retain meaning hues and choose a contrasting primary foreground', () => {
  const state = defaultColorSystem();
  state.main = 'semantics';
  state.mainShade = { family: 'positive', step: 'weak', h: 145, s: 72, l: 92 };
  state.semanticRole = 'positive';
  assert.equal(mainColor(state).h, 145);
  assert.equal(mainColor(state).gs, state.brand.gs);
  assert.equal(semanticSettings(state).base.light.strong, 42);
  const css = colorSystemCss(state);
  assert.ok(css.includes('--accent: hsl(145 72% 92%);'));
  assert.ok(css.includes('--on-accent: #000;'));
  for (const role of Object.keys(SEMANTIC_BANDS)) assert.ok(css.includes(`--${role}-h: ${semanticHue(role)};`));
});

test('automatic semantic main uses its actual adjusted colour in each mode', () => {
  const state = defaultColorSystem();
  state.main = 'semantics';
  state.semanticRole = 'negative';
  state.semanticAdjustments.light.strong = 25;
  const css = colorSystemCss(state);
  assert.ok(css.includes('--accent: var(--negative);'));
  assert.ok(css.includes('--acc-l: var(--sem-l);'));
  assert.ok(css.includes('--on-accent: #000;'));
  assert.ok(css.includes('--sem-l: 67%;'));
});

test('malformed exact shades and incompatible harmony selections fail explicitly', () => {
  const state = defaultColorSystem();
  const shade = { family: 'brand', step: 500, h: 202, s: 72, l: 48 };
  for (const invalid of [null, { ...shade, l: NaN }, { ...shade, l: 101 },
    { ...shade, step: 999 }, { ...shade, family: 'missing' }, { ...shade, s: '72' }]) {
    assert.throws(() => validateColorSystem({ ...state, mainShade: invalid }), /Invalid selected/);
  }
  assert.throws(() => validateColorSystem({ ...state, main: 'harmony', mainShade: shade }), /Invalid selected/);
});

test('exact harmony shades replace role mapping and survive JSON and CSS builds for every preset and count', () => {
  for (const harmony of Object.keys(COLOR_HARMONIES)) {
    for (let count = 3; count <= 10; count++) {
      const state = { ...defaultColorSystem(), main: 'harmony', harmony, harmonyCount: count };
      harmonyPalette(state).forEach((entry, i) => {
        state.harmonyHue = i + 1;
        state.mainShade = {
          family: 'harmony', step: i + 1, h: (state.brand.h + entry.offset) % 360,
          s: state.brand.s, l: Math.max(10, Math.min(90, 42 + entry.lightness)),
        };
        const restored = validateColorSystem(JSON.parse(JSON.stringify(state)));
        const css = colorSystemCss(restored);
        assert.equal(mainColor(restored).l, state.mainShade.l);
        assert.ok(css.includes(`--accent: hsl(${state.mainShade.h} 72% ${state.mainShade.l}%);`));
        assert.ok(!css.includes('Harmony role mapping'));
        assert.ok(!css.includes(`--acc-l: ${state.mainShade.l}%;`));
        assert.ok(emitCss(buildTokens({ colorSystem: restored }), '', '', undefined, restored).includes(css));
        assert.throws(() => validateColorSystem({ ...restored, mainShade: { ...restored.mainShade, step: count + 1 } }), /Invalid selected/);
      });
      delete state.mainShade;
      assert.ok(colorSystemCss(state).includes('Harmony role mapping'));
    }
  }
});

test('semantic hues remain in their identity bands across the entire brand circle', () => {
  for (let hue = 0; hue <= 360; hue += 0.5) {
    for (const [role, [min, max]] of Object.entries(SEMANTIC_BANDS)) {
      let result = semanticHue(role, hue);
      if (role === 'negative' && result > 180) result -= 360;
      assert.ok(result >= min - 1e-10 && result <= max + 1e-10, `${role} at ${hue}`);
    }
  }
  assert.equal(semanticHue('negative', 0), 0);
  assert.equal(semanticHue('negative', 360), 0);
});

test('main sources and all harmony patterns use the correct upstream palette', () => {
  const state = defaultColorSystem();
  state.source.h = 40;
  state.brand.h = 250;
  state.main = 'hsl';
  assert.equal(mainColor(state).h, 40);
  state.main = 'brand';
  assert.equal(mainColor(state).h, 250);
  state.main = 'harmony';
  for (const [name, offsets] of Object.entries(COLOR_HARMONIES)) {
    state.harmony = name;
    for (let n = 2; n <= 4; n++) {
      state.harmonyHue = n;
      assert.equal(mainColor(state).h, (250 + offsets[n - 2]) % 360);
    }
  }
  state.main = 'semantics';
  state.semanticRole = 'negative';
  assert.equal(mainColor(state).h, semanticHue('negative', 250));
});

test('only included layers are added to exports, with selected main protected', () => {
  const state = defaultColorSystem();
  state.included = ['brand'];
  const css = colorSystemCss(state);
  assert.ok(css.includes('--theme-brand-500:'));
  assert.ok(css.includes('--theme-brand-grey-500:'));
  assert.ok(css.includes('--theme-brand-gray-500:'));
  for (const omitted of ['--theme-hsl-', '--theme-harmony-', '--negative-h:', '--sem-l:']) assert.ok(!css.includes(omitted));
  const tokens = buildTokens({ colorSystem: state, semanticS: 75, harmony: 'triadic' });
  assert.deepEqual(Object.keys(tokens).sort(), ['--brand-h', '--brand-s', '--grey-s']);
  state.main = 'semantics';
  assert.throws(() => validateColorSystem(state), /Invalid/);
});

test('legacy semantic brightness is retained with fixed hues and independent modes', () => {
  const state = defaultColorSystem();
  delete state.semanticAdjustments;
  state.brand.h = 300;
  state.light.strong = 45;
  state.dark.strong = 70;
  const css = colorSystemCss(state);
  assert.ok(css.includes('--negative-h: 0'));
  assert.ok(css.includes('--negative: hsl(0 var(--sem-s) var(--sem-l))'));
  assert.ok(css.includes('--sem-l: 45%'));
  assert.ok(css.includes('--sem-l: 70%'));
  assert.ok(css.includes(':root[data-theme="dark"]'));
  const output = emitCss(buildTokens({ colorSystem: state }), '/* base */', '.custom {}', undefined, state);
  assert.ok(output.includes(css));
  assert.ok(output.endsWith('.custom {}\n'));
});

test('semantics follow the main palette with persistent offsets, fixed hues and no circular source', () => {
  const state = defaultColorSystem();
  state.source = { h: 40, s: 85, gs: 10 };
  state.brand = { h: 180, s: 30, gs: 24, tone: 8 };
  state.semanticAdjustments.s = -10;
  state.semanticAdjustments.light.strong = 5;
  state.main = 'hsl';
  assert.equal(semanticSettings(state).s, 75);
  assert.equal(semanticSettings(state).light.strong, 47);
  state.main = 'brand';
  assert.equal(semanticSettings(state).s, 20);
  assert.equal(semanticSettings(state).light.strong, paletteLightness(state.brand, 42) + 5);
  state.main = 'harmony';
  state.harmony = 'monochrome';
  state.harmonyHue = 2;
  assert.equal(semanticSettings(state).light.strong, paletteLightness(state.brand, 42) + 20);
  state.main = 'semantics';
  state.semanticRole = 'negative';
  assert.equal(mainColor(state).s, 20);
  assert.equal(mainColor(state).h, 0);
  assert.equal(semanticSettings(state).light.strong, paletteLightness(state.brand, 42) + 5);
  state.semanticAdjustments.s = 100;
  state.semanticAdjustments.dark.strong = -100;
  assert.equal(semanticSettings(state).s, 100);
  assert.equal(semanticSettings(state).dark.strong, 0);
  assert.equal(colorSystemCss(JSON.parse(JSON.stringify(state))), colorSystemCss(state));
  assert.throws(() => validateColorSystem({ ...state, semanticAdjustments: { s: NaN } }), /Invalid/);
});

test('malformed saved colour states are rejected explicitly', () => {
  for (const patch of [{ main: 'invalid' }, { brand: { h: NaN, s: 50, gs: 12 } }, { harmony: 'missing' }, { harmonyHue: 2.5 }, { semanticS: 101 }, { dark: { strong: 100, weak: 10 } }]) {
    assert.throws(() => validateColorSystem({ ...defaultColorSystem(), ...patch }), /Invalid/);
  }
});

test('all presets export exactly the requested 3–10 harmony colours and classes', () => {
  assert.equal(Object.keys(COLOR_HARMONIES).length, 23);
  for (const harmony of Object.keys(COLOR_HARMONIES)) {
    for (let count = 3; count <= 10; count++) {
      const state = { ...defaultColorSystem(), harmony, harmonyCount: count, main: 'harmony', harmonyHue: count };
      const palette = harmonyPalette(state);
      assert.equal(palette.length, count);
      assert.equal(new Set(palette.map(p => `${p.offset}:${p.lightness}:${p.absoluteLightness}:${p.saturation}`)).size, count);
      const css = colorSystemCss(state);
      assert.equal((css.match(/--theme-harmony-\d+:/g) || []).length, count);
      assert.ok(css.includes(`.hue-${count} {`));
      assert.ok(css.includes(`.ab.card.fam-h${count} {`));
      assert.ok(!css.includes(`--hue-${count + 1}:`));
      assert.ok(!/undefined|NaN/.test(css));
      validateColorSystem(JSON.parse(JSON.stringify(state)));
      assert.equal(mainColor(state).h, (state.brand.h + palette[count - 1].offset + 360) % 360);
      assert.equal(JSON.parse(JSON.stringify(state)).harmonyCount, count);
    }
  }
});

test('new harmony formulas have precise angular intervals for every count', () => {
  const fixed = {
    'analogous-tight': [0, 15, -15, 30], 'analogous-wide': [0, 60, -60, 120],
    'split-wide': [0, 135, 225, 180], rectangle: [0, 45, 180, 225],
    pentadic: [0, 72, 144, 216, 288], hexadic: [0, 60, 120, 180, 240, 300],
  };
  for (let count = 3; count <= 10; count++) {
    for (const [harmony, anchors] of Object.entries(fixed)) {
      const palette = harmonyPalette({ ...defaultColorSystem(), harmony, harmonyCount: count });
      palette.forEach((entry, i) => {
        assert.equal(entry.offset, anchors[i % anchors.length]);
        assert.equal(entry.lightness, [0, 15, -15][Math.floor(i / anchors.length)]);
      });
    }
    for (const harmony of ['spectrum', 'golden-angle']) {
      const state = { ...defaultColorSystem(), harmony, harmonyCount: count };
      const palette = harmonyPalette(state);
      assert.equal(new Set(palette.map(p => p.offset)).size, count);
      palette.forEach((entry, i) => {
        const expected = harmony === 'spectrum' ? i * 360 / count : (i * 180 * (3 - Math.sqrt(5))) % 360;
        assert.ok(Math.abs(entry.offset - expected) <= .000501);
        assert.equal(entry.lightness, 0);
      });
    }
  }
});

test('monochrome variations preserve hue with measurable saturation and lightness differences', () => {
  for (const harmony of ['mono-tints', 'mono-shades', 'mono-muted', 'mono-pastel', 'mono-contrast', 'mono-ink-wash']) {
    for (let count = 3; count <= 10; count++) {
      const state = { ...defaultColorSystem(), harmony, harmonyCount: count, main: 'harmony', harmonyHue: count };
      const palette = harmonyPalette(state);
      const first = palette[0], last = palette.at(-1);
      assert.ok(palette.every(p => p.offset === 0 && p.absoluteLightness >= 10 && p.absoluteLightness <= 90 && p.saturation > 0 && p.saturation <= 1));
      if (harmony === 'mono-tints' || harmony === 'mono-pastel') assert.ok(palette.every((p, i) => !i || p.absoluteLightness > palette[i - 1].absoluteLightness));
      if (harmony === 'mono-shades') assert.ok(palette.every((p, i) => !i || p.absoluteLightness < palette[i - 1].absoluteLightness));
      if (harmony === 'mono-muted') {
        assert.ok(first.saturation > last.saturation);
        assert.ok(palette.every(p => p.absoluteLightness === 48));
      }
      if (harmony === 'mono-contrast') assert.ok(palette.every((p, i) => !i || Math.abs(p.absoluteLightness - palette[i - 1].absoluteLightness) >= 45));
      if (harmony === 'mono-ink-wash') assert.ok(first.absoluteLightness === 20 && palette.slice(1).every(p => p.absoluteLightness > 75));
      assert.equal(mainColor(state).s, Math.round(state.brand.s * last.saturation * 10) / 10);
      assert.equal(semanticSettings(state).light.strong, last.absoluteLightness);
      const css = colorSystemCss(state);
      assert.ok(css.includes(`--theme-harmony-s-${count}: ${mainColor(state).s}%;`));
      assert.ok(css.includes(`--theme-harmony-l-${count}: ${last.absoluteLightness}%;`));
      assert.equal(colorSystemCss(JSON.parse(JSON.stringify(state))), css);
    }
  }
});

test('fixed foundation survives candidate changes and drives harmony and semantics', () => {
  const baseColor = { h: 310, s: 65, l: 35, gs: 12 };
  const state = { ...defaultColorSystem(), baseColor };
  for (const main of ['brand', 'hsl', 'harmony', 'semantics']) {
    const candidate = { ...state, main, harmonyCount: 10 };
    assert.deepEqual(mainColor(candidate), baseColor);
    const css = colorSystemCss(candidate);
    assert.ok(css.includes('--theme-harmony-h: 310;'));
    assert.ok(css.includes('--theme-harmony-s: 65%;'));
    assert.ok(css.includes('--accent: hsl(310 65% 35%);'));
    assert.equal(semanticSettings(candidate).base.light.strong, 35);
    assert.equal(semanticSettings(candidate).base.s, 65);
    assert.deepEqual(validateColorSystem(JSON.parse(JSON.stringify(candidate))).baseColor, baseColor);
  }
  const changed = { ...state, brand: { h: 50, s: 20, gs: 0, tone: 12 } };
  assert.deepEqual(mainColor(changed), baseColor);
  assert.equal(semanticSettings(changed).base.s, 65);
  for (const bad of [null, { ...baseColor, l: 101 }, { ...baseColor, h: NaN }]) {
    assert.throws(() => validateColorSystem({ ...state, baseColor: bad }), /Invalid fixed base/);
  }
});

test('legacy colour edit lock is accepted without changing exported colours', () => {
  const state = defaultColorSystem();
  const locked = { ...state, locked: true };
  assert.equal(validateColorSystem(JSON.parse(JSON.stringify(locked))).locked, true);
  assert.equal(colorSystemCss(locked), colorSystemCss(state));
  assert.equal(validateColorSystem({ ...state, locked: false }).locked, false);
  assert.throws(() => validateColorSystem({ ...state, locked: 'yes' }), /Invalid/);
});

test('legacy themes default to four harmony colours; invalid counts and selections fail', () => {
  const state = defaultColorSystem();
  delete state.harmonyCount;
  assert.equal(harmonyPalette(validateColorSystem(state)).length, 4);
  for (const harmonyCount of [2, 11, 3.5, '5']) {
    assert.throws(() => validateColorSystem({ ...state, harmonyCount }), /Invalid/);
  }
  assert.throws(() => validateColorSystem({ ...state, harmonyCount: 3, harmonyHue: 4 }), /Invalid/);
});

test('remixes preserve source hue, vary consecutive results and persist ordered tonal ramps', () => {
  for (const source of [{ h: 180, s: 30, gs: 24 }, { h: 0, s: 0, gs: 0 }, { h: 360, s: 100, gs: 40 }]) {
    const original = { ...source };
    let previous = source;
    for (let i = 0; i < 20; i++) {
      const brand = remixBrand(source, previous, () => (i % 5) / 5);
      assert.equal(brand.h, source.h);
      assert.notDeepEqual(brand, previous);
      const state = { ...defaultColorSystem(), source, brand };
      validateColorSystem(state);
      const lights = COLOR_STOPS.map(([, light]) => paletteLightness(brand, light));
      assert.ok(lights.every((light, n) => light > 0 && light < 100 && (!n || light < lights[n - 1])));
      const restored = JSON.parse(JSON.stringify(state));
      assert.equal(colorSystemCss(restored), colorSystemCss(state));
      assert.ok(colorSystemCss(state).includes(`--blue-500: hsl(var(--brand-h) var(--brand-s) ${paletteLightness(brand, 48)}%);`));
      previous = brand;
    }
    assert.deepEqual(source, original);
  }
  assert.throws(() => validateColorSystem({ ...defaultColorSystem(), brand: { h: 180, s: 30, gs: 24, tone: 99 } }), /Invalid/);
});

test('harmony main distributes the palette by role and removes role rules for other mains', () => {
  for (let count = 3; count <= 10; count++) {
    const state = { ...defaultColorSystem(), main: 'harmony', harmonyCount: count };
    const css = colorSystemCss(state);
    assert.ok(css.includes('--accent: var(--theme-harmony-3)'));
    assert.ok(css.includes(`--line: var(--theme-harmony-${Math.min(count, 4)})`));
    assert.ok(css.includes('--theme-heading-h-1: var(--hue-2)'));
    if (count > 4) assert.ok(css.includes('--theme-heading-h-2: var(--hue-5)'));
    state.main = 'brand';
    assert.ok(!colorSystemCss(state).includes('Harmony role mapping'));
  }
});
