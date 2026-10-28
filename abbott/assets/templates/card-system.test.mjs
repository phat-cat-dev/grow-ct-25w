import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { DEFAULT_CARDS, validateCards, cardsCss } from '../public/site/card-system.js';
import { emitCss } from './emit-css.js';
import { colorSystemCss, defaultColorSystem } from '../public/site/color-system.js';

test('card defaults are cloned and partial configurations retain their other defaults', () => {
  assert.deepEqual(validateCards(), DEFAULT_CARDS);
  const state = validateCards({ padding: 32 });
  assert.equal(state.padding, 32);
  assert.equal(state.fill, 'tinted');
  state.padding = 8;
  assert.equal(DEFAULT_CARDS.padding, 16);
  assert.deepEqual(validateCards(JSON.parse(JSON.stringify(DEFAULT_CARDS))), DEFAULT_CARDS);
});

test('card controls enforce their full numeric and enum limits', () => {
  for (const [key, min, max] of [['padding', 8, 40], ['border', 0, 6], ['tint', 0, 30], ['iconSize', 16, 56], ['gap', 8, 32]]) {
    assert.equal(validateCards({ [key]: min })[key], min);
    assert.equal(validateCards({ [key]: max })[key], max);
    for (const invalid of [min - 1, max + 1, NaN, Infinity, String(min), null]) {
      assert.throws(() => validateCards({ [key]: invalid }), /Invalid card settings/);
    }
  }
  for (const invalid of [null, [], 'cards', { family: 'red' }, { fill: 'unknown' }, { elevation: 'floating' }]) {
    assert.throws(() => validateCards(invalid), /Invalid card settings/);
  }
});

test('each family, fill and elevation exports live tokens rather than a disconnected palette', () => {
  for (const family of ['brand', 'grey', 'gray']) {
    for (const fill of ['tinted', 'soft', 'invert']) {
      for (const elevation of ['flat', 'soft', 'raised']) {
        const css = cardsCss({ family, fill, elevation, padding: 30, border: 4, tint: 23, iconSize: 42, gap: 24 });
        for (const token of ['--ab-card-spacer-x: 30px', '--ab-card-border-width: 4px', '--ab-card-tint: 23%', '--ab-card-icon-size: 42px', '--ab-card-group-gap: 24px']) {
          assert.ok(css.includes(token), token);
        }
        assert.match(css, /--ab-card-accent: var\(--neutral\)/);
        assert.match(css, /--ab-card-accent: var\(--positive\)/);
        assert.match(css, /border-radius: var\(--radius\)/);
        assert.match(css, /prefers-reduced-motion/);
        assert.match(css, /forced-colors/);
        assert.doesNotMatch(css, /scale\(1\.02\)|undefined|NaN/);
      }
    }
  }
});

test('card CSS participates in portable exports after layout and before custom overrides', () => {
  const settings = { ...DEFAULT_CARDS, padding: 24, fill: 'soft' };
  const css = emitCss({}, '/* base */', '/* custom */', undefined, undefined, undefined, undefined, { radius: 24 }, settings);
  assert.ok(css.includes(cardsCss(settings)));
  assert.ok(css.indexOf('Layout corner radius') < css.indexOf('Theme-linked cards'));
  assert.ok(css.endsWith('/* custom */\n'));
  assert.equal(emitCss({}, ''), emitCss({}, '', '', undefined, undefined, undefined, undefined, undefined, undefined));
  assert.throws(() => emitCss({}, '', '', undefined, undefined, undefined, undefined, undefined, { border: -1 }), /Invalid/);
});

test('Harmony per-card accents remain more specific than default card styling', () => {
  const css = colorSystemCss({ ...defaultColorSystem(), included: ['hsl', 'brand', 'harmony'], harmonyCount: 10 });
  assert.match(css, /:root \.ab\.card\.fam-h10 \{ --ab-card-accent: var\(--theme-harmony-10\)/);
});

test('maintained card fragment puts themed examples before semantic examples and includes live controls', async () => {
  const fragment = await readFile(new URL('../public/site/fragments/cards.html', import.meta.url), 'utf8');
  assert.ok(fragment.indexOf('1.1 Themed cards') < fragment.indexOf('1.2 Semantic cards'));
  assert.match(fragment, /class="ab card warning soft with-icon"/);
  assert.match(fragment, /class="ab card-group"/);
  assert.match(fragment, /Layer 3/);
  assert.match(fragment, /data-card-live/);
  for (const key of Object.keys(DEFAULT_CARDS)) assert.ok(fragment.includes(`id="card-${key}"`), key);
  const ids = Array.from(fragment.matchAll(/\bid="([^"]+)"/g), match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
});
