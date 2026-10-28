import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import less from 'less';
import { FLUID_CORE_CSS } from '../public/site/fluid-core.js';
import { DEFAULT_SPACING, SPACING_PROFILES, validateSpacing, spacingCss } from '../public/site/spacing-system.js';
import { emitCss } from './emit-css.js';

test('the persistent engine is compiled from all three supplied LESS sources without changing calc arithmetic', async () => {
  const files = ['abbott-core-default.less', 'abbott-core-fluid.less', 'abbott-core-legacy.less'];
  const sources = await Promise.all(files.map(file => readFile(new URL('../public/site/fragments/04_spacing/' + file, import.meta.url), 'utf8')));
  const result = await less.render(sources.join('\n'), { math: 'parens-division' });
  assert.equal(FLUID_CORE_CSS, result.css);
  for (const scale of ['text', 'space', 'layout']) {
    assert.ok(result.css.includes(`--ab-fluid-${scale}: clamp(`));
    assert.ok(result.css.includes(`var(--ab-fluid-${scale}-vp-max, var(--ab-fluid-vp-max))`));
  }
  assert.ok(result.css.includes(':where([data-ab-profile])'));
  assert.equal((result.css.match(/--ab-core-[\w-]+:/g) || []).length, 14);
});

test('spacing defaults, profiles and partial records retain the supplied bounds', () => {
  assert.deepEqual(validateSpacing(), DEFAULT_SPACING);
  assert.deepEqual(validateSpacing({ spaceMax: 2 }), { ...DEFAULT_SPACING, spaceMax: 2 });
  assert.equal(SPACING_PROFILES.compact.textMax, DEFAULT_SPACING.textMax);
  assert.equal(SPACING_PROFILES.roomy.viewportMax, 80);
  for (const profile of Object.values(SPACING_PROFILES)) {
    assert.deepEqual(validateSpacing(profile), profile);
  }
});

test('invalid, nonfinite and reversed settings fail explicitly', () => {
  for (const value of [null, [], 'compact', { spaceMax: NaN }, { layoutMin: Infinity },
    { textMin: '1' }, { viewportMin: 45 }, { viewportMin: 46 }, { textMin: 2 },
    { spaceMin: -1 }, { layoutMax: 4 }, { viewportMax: 121 }]) {
    assert.throws(() => validateSpacing(value));
  }
  assert.doesNotThrow(() => validateSpacing({ textMin: 1, textMax: 1 }));
});

test('fluid settings and scoped profiles travel through builds while legacy builds stay unchanged', () => {
  const css = spacingCss({ ...DEFAULT_SPACING, spaceMax: 2 });
  assert.ok(css.includes('--ab-fluid-space-max: 2;'));
  for (const name of Object.keys(SPACING_PROFILES)) assert.ok(css.includes(`[data-ab-profile="${name}"]`));
  const baseline = emitCss({}, '/* template */');
  assert.ok(!baseline.includes('--ab-fluid-'));
  const built = emitCss({}, '/* template */', '/* custom last */', undefined, undefined, undefined, { spaceMax: 2 });
  assert.ok(built.includes(css));
  assert.ok(built.endsWith('/* custom last */\n'));
});

test('icon size has independent fluid bounds, legacy defaults and portable CSS', () => {
  const legacy = { ...DEFAULT_SPACING };
  delete legacy.iconMin;
  delete legacy.iconMax;
  assert.equal(validateSpacing(legacy).iconMin, 1.5);
  assert.equal(validateSpacing(legacy).iconMax, 2.5);
  const state = validateSpacing({ iconMin: 2, iconMax: 4 });
  assert.equal(state.textMax, DEFAULT_SPACING.textMax);
  assert.equal(state.spaceMax, DEFAULT_SPACING.spaceMax);
  const css = spacingCss(JSON.parse(JSON.stringify(state)));
  assert.ok(css.includes('--ab-fluid-icon-min: 2;'));
  assert.ok(css.includes('--ab-fluid-icon-max: 4;'));
  assert.ok(css.includes('--ab-icon-size: var(--ab-fluid-icon)'));
  assert.ok(css.includes('inline-size: var(--ab-icon-size)'));
  for (const invalid of [{ iconMin: 3, iconMax: 2 }, { iconMax: 7 }, { iconMin: NaN }, { iconMax: '4' }]) {
    assert.throws(() => validateSpacing(invalid));
  }
  assert.ok(emitCss({}, '', '', undefined, undefined, undefined, state).includes(css));
});
