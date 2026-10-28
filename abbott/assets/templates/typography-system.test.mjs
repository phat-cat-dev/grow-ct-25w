import test from 'node:test';
import assert from 'node:assert/strict';
import { DEFAULT_TYPOGRAPHY, TYPOGRAPHY_BULLETS, TYPOGRAPHY_RATIOS, HEADING_HARMONIES, headingSizes, ACADEMIC_BULLETS, validateTypography, typographyCss } from '../public/site/typography-system.js';
import { readFile } from 'node:fs/promises';
import { emitCss } from './emit-css.js';

test('modular heading formulas preserve their measured ratios, fluid bounds and JSON/CSS exports', () => {
  for (const [size, ratio] of Object.entries(TYPOGRAPHY_RATIOS)) {
    const sizes = headingSizes(size);
    assert.equal(sizes.length, 6);
    assert.equal(sizes[5], .875);
    for (let i = 0; i < 5; i++) assert.ok(Math.abs(sizes[i] / sizes[i + 1] - ratio) < 1e-12);
    for (const scale of [.8, 1, 1.8]) {
      const state = validateTypography({ size, scale, applied: true });
      const css = typographyCss(state);
      const rules = [...css.matchAll(/font-size: clamp\(([\d.]+)rem, calc\([^)]+\), ([\d.]+)rem\)/g)];
      assert.equal(rules.length, 7);
      for (let i = 0; i < 6; i++) {
        assert.ok(Math.abs(+rules[i][1] - sizes[i] * scale * .85) < .000051);
        assert.ok(Math.abs(+rules[i][2] - sizes[i] * scale) < .000051);
      }
      assert.equal(typographyCss(JSON.parse(JSON.stringify(state))), css);
      assert.ok(emitCss({}, '', '', undefined, undefined, state).includes(css));
      assert.deepEqual(typographyCss({ ...state, reverse: true }).match(/font-size:[^;]+;/g), css.match(/font-size:[^;]+;/g));
    }
  }
  assert.deepEqual(headingSizes('graded'), [2, 1.5, 1.18, 1, .875, .75]);
  assert.deepEqual(headingSizes('uniform'), Array(6).fill(1.15));
  assert.throws(() => headingSizes('missing'), /Invalid heading/);
  assert.throws(() => validateTypography({ size: 'missing' }), /Invalid typography/);
});

test('typography validates every heading option and emits fluid, main-colour-linked rules', () => {
  for (const scheme of ['diagonal', 'grey', 'gray', 'mono', 'twotone', 'accent', 'muted', ...Object.keys(HEADING_HARMONIES)]) {
    for (const decoration of ['none', 'underline', 'dashed', 'dotted', 'leftborder']) {
      for (const [bullet, symbol] of Object.entries(TYPOGRAPHY_BULLETS)) {
        const state = { ...DEFAULT_TYPOGRAPHY, scheme, decoration, bullet, applied: true };
        const css = typographyCss(state);
        assert.equal((css.match(/font-size: clamp\(/g) || []).length, 7);
        assert.ok(css.includes('var(--brand-h, var(--h, 202))'));
        assert.ok(css.includes('prefers-color-scheme: dark'));
        assert.ok(css.includes(':root[data-theme="dark"]'));
        assert.ok(!css.includes('undefined'));
        assert.ok(css.includes(`content: "${symbol}"`));
        assert.equal(validateTypography(JSON.parse(JSON.stringify(state))).bullet, bullet);
      }
    }
  }
});

test('heading harmony schemes emit explicit per-level hue formulas and reverse colour order only', async () => {
  const source = await readFile(new URL('../public/site/02_typography.md', import.meta.url), 'utf8');
  for (const [scheme, offsets] of Object.entries(HEADING_HARMONIES)) {
    assert.ok(source.includes(`name="hsc" value="${scheme}"`));
    for (const reverse of [false, true]) {
      const state = validateTypography({ scheme, reverse, applied: true, size: 'major-third' });
      const css = typographyCss(state);
      for (let i = 0; i < 6; i++) {
        const rule = css.match(new RegExp(`:root h${i + 1}[^\\{]+\\{([^}]+)\\}`))[1];
        assert.ok(rule.includes(`color: hsl(calc(var(--brand-h, var(--h, 202)) + ${offsets[reverse ? 5 - i : i]})`));
        assert.ok(!rule.includes('--theme-heading-h-'));
      }
      assert.equal(typographyCss(JSON.parse(JSON.stringify(state))), css);
      assert.ok(emitCss({}, '', '', undefined, undefined, state).includes(css));
      assert.deepEqual(css.match(/font-size:[^;]+;/g), typographyCss({ ...state, reverse: !reverse }).match(/font-size:[^;]+;/g));
      assert.ok(typographyCss(state, '#preview').includes('#preview h6'));
    }
  }
  const muted = typographyCss({ scheme: 'muted', applied: true });
  assert.equal((muted.match(/calc\(var\(--brand-s, var\(--s, 72%\)\) \* .45\)/g) || []).length, 6);
});

test('preview, reverse, uniform, reset and optional export preserve existing behaviour', () => {
  assert.ok(!typographyCss().includes(':root h1'));
  assert.ok(typographyCss(DEFAULT_TYPOGRAPHY, '#preview').includes('#preview h1'));
  const state = { ...DEFAULT_TYPOGRAPHY, applied: true, reverse: true, size: 'uniform', scale: 1.4 };
  assert.ok(typographyCss(state).includes('--type-l-1: 68%'));
  assert.deepEqual(validateTypography(), DEFAULT_TYPOGRAPHY);
  const css = emitCss({}, '/* base */', '.custom {}', undefined, undefined, state);
  assert.ok(css.includes(typographyCss(state)));
  assert.ok(css.endsWith('.custom {}\n'));
  assert.ok(!emitCss({}, '/* base */').includes('Typography follows'));
  assert.deepEqual(validateTypography(JSON.parse(JSON.stringify(state))), state);
});

test('invalid typography values fail explicitly', () => {
  for (const patch of [{ scheme: 'bad' }, { decoration: 'bad' }, { bullet: 'bad' }, { bodySize: 30 }, { scale: NaN }, { readingWidth: 10 }, { lineHeight: 0 }, { applied: 'yes' }, { underlineWidth: 0 }, { borderWidth: .6 }]) {
    assert.throws(() => validateTypography({ ...DEFAULT_TYPOGRAPHY, ...patch }), /Invalid typography/);
  }
});

test('decoration widths are independent, relative and backwards compatible', () => {
  const state = { ...DEFAULT_TYPOGRAPHY, applied: true, decoration: 'leftborder', underlineWidth: .12, borderWidth: .3 };
  const css = typographyCss(state);
  assert.ok(css.includes('text-decoration-thickness: 0.12em'));
  assert.ok(css.includes('border-left: 0.3rem solid currentColor'));
  assert.equal((css.match(/padding-left: .5rem;/g) || []).length, 6);
  assert.equal((css.match(/margin-inline: 0;/g) || []).length, 6);
  assert.equal((css.match(/text-align: left;/g) || []).length, 6);
  assert.ok(typographyCss({ ...state, decoration: 'dotted' }).includes('border-left: 0;'));
  const legacy = { ...state };
  delete legacy.underlineWidth;
  delete legacy.borderWidth;
  assert.equal(validateTypography(legacy).underlineWidth, .06);
  assert.equal(validateTypography(legacy).borderWidth, .18);
  assert.equal(typographyCss(JSON.parse(JSON.stringify(state))), css);
});

test('academic bullets use existing practice icons and export standalone masks', async () => {
  const reference = await readFile(new URL('../public/cheatsheet copy.html', import.meta.url), 'utf8');
  for (const [bullet, icon] of Object.entries(ACADEMIC_BULLETS)) {
    const symbol = reference.match(new RegExp(`<symbol id="ic-${bullet.replace('academic-', '')}"[^>]*>([\\s\\S]*?)</symbol>`));
    assert.ok(symbol?.[1].includes(icon.path), `Original icon matches ${bullet}`);
    const state = { ...DEFAULT_TYPOGRAPHY, applied: true, bullet };
    const css = typographyCss(state);
    assert.ok(css.includes('data:image/svg+xml,'));
    assert.ok(css.includes('width: 0.72em; height: 0.72em; background: currentColor'));
    assert.ok(!css.includes('undefined'));
    assert.equal(validateTypography(JSON.parse(JSON.stringify(state))).bullet, bullet);
  }
});

test('heading icon size is independent, validated and retained in exports and legacy themes', () => {
  const state = { ...DEFAULT_TYPOGRAPHY, applied: true, bullet: 'academic-writing', iconSize: 1.5 };
  const css = typographyCss(state);
  assert.ok(css.includes('width: 1.5em; height: 1.5em'));
  assert.ok(css.includes('display: flex;\n  align-items: center;'));
  assert.ok(css.includes('flex: none; margin-right: .4em'));
  const original = typographyCss({ ...state, iconSize: .72 });
  assert.deepEqual(css.match(/font-size: [^;]+;/g), original.match(/font-size: [^;]+;/g));
  assert.equal(validateTypography({}).iconSize, .72);
  assert.deepEqual(validateTypography(JSON.parse(JSON.stringify(state))), state);
  assert.ok(emitCss({}, '/* base */', '', undefined, undefined, state).includes(css));
  for (const iconSize of [.29, 2.01, NaN, '1']) {
    assert.throws(() => validateTypography({ iconSize }), /Invalid typography/);
  }
  for (const iconSize of [.3, 2]) assert.equal(validateTypography({ iconSize }).iconSize, iconSize);
});

test('CAPS can be independently overridden at every heading level and persisted', () => {
  assert.deepEqual(validateTypography({}).caps, [false, false, false, false, false, true]);
  const independent = validateTypography();
  independent.caps[0] = true;
  assert.equal(DEFAULT_TYPOGRAPHY.caps[0], false);
  for (let index = 0; index < 6; index++) {
    const caps = Array(6).fill(false);
    caps[index] = true;
    const state = validateTypography({ caps, applied: true });
    const css = typographyCss(state);
    for (let level = 0; level < 6; level++) {
      const rule = css.match(new RegExp(`:root h${level + 1}[^\\{]+\\{([^}]+)\\}`))[1];
      assert.ok(rule.includes(`text-transform: ${level === index ? 'uppercase' : 'none'};`));
    }
    assert.deepEqual(validateTypography(JSON.parse(JSON.stringify(state))), state);
    assert.ok(emitCss({}, '/* base */', '', undefined, undefined, state).includes(css));
  }
  for (const caps of [null, true, [], Array(6), [false, false, false, false, false, 'yes']]) {
    assert.throws(() => validateTypography({ caps }), /Invalid typography/);
  }
});
