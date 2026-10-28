import test from 'node:test';
import assert from 'node:assert/strict';
import { validateLayout, layoutCss } from '../public/site/layout-system.js';
import { emitCss } from './emit-css.js';

test('corner radius supports square through rounded, reset and JSON persistence', () => {
  assert.equal(validateLayout().radius, 16);
  for (const radius of [0, 16, 48]) {
    const state = validateLayout({ radius });
    assert.deepEqual(validateLayout(JSON.parse(JSON.stringify(state))), state);
    const css = layoutCss(state);
    assert.ok(css.includes(`--radius: ${radius}px`));
    assert.ok(css.includes(`--radius-sm: ${radius / 2}px`));
    assert.ok(css.includes('#base-colour-lock'));
    assert.ok(css.includes('.active-source-chip'));
    assert.ok(css.includes('.hovmodes label'));
    assert.ok(css.includes('code, kbd'));
    assert.ok(emitCss({}, '', '', undefined, undefined, undefined, undefined, state).includes(css));
  }
  for (const radius of [-1, 49, NaN, '16', null]) {
    assert.throws(() => validateLayout({ radius }), /Invalid layout/);
  }
  assert.ok(!emitCss({}, '').includes('Layout corner radius'));
});
