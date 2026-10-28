import test from 'node:test';
import assert from 'node:assert/strict';
import { emitCss } from './emit-css.js';
import { connectorAssets, DEFAULT_CONNECTORS } from '../public/site/connectors.js';

test('existing schemes keep their output when no connectors are configured', () => {
  const css = emitCss({ '--brand-h': '202' }, '/* template */', '.example { color: red; }');
  assert.equal(css, emitCss({ '--brand-h': '202' }, '/* template */', '.example { color: red; }', undefined));
  assert.ok(css.startsWith('/* template */'));
  assert.ok(css.endsWith('.example { color: red; }\n'));
});

test('Google imports precede the template and custom rules remain last', () => {
  const config = { ...DEFAULT_CONNECTORS, headingFont: 'Playfair Display', bodyFont: 'Source Sans 3', symbolStyle: 'Rounded', symbolFill: 1, symbolWeight: 600, symbolSize: 44 };
  const assets = connectorAssets(config);
  const css = emitCss({ '--brand-h': '202' }, '/* template */', '.example { color: red; }', config);
  assert.ok(css.startsWith('@import url("https://fonts.googleapis.com/css2?'));
  assert.equal((css.match(/@import/g) || []).length, 2);
  assert.ok(css.indexOf(assets.urls[1]) < css.indexOf('/* template */'));
  assert.ok(css.includes('--font-heading: "Playfair Display", serif'));
  assert.ok(css.includes('--font-body: "Source Sans 3", sans-serif'));
  assert.ok(css.includes("'FILL' 1, 'wght' 600, 'GRAD' 0, 'opsz' 44"));
  assert.ok(css.endsWith('.example { color: red; }\n'));
});

test('identical font families are requested only once', () => {
  const assets = connectorAssets(DEFAULT_CONNECTORS);
  assert.equal((assets.urls[0].match(/family=/g) || []).length, 1);
});

test('all three Material Symbols styles have variable-axis requests', () => {
  for (const symbolStyle of ['Outlined', 'Rounded', 'Sharp']) {
    const assets = connectorAssets({ ...DEFAULT_CONNECTORS, symbolStyle });
    assert.ok(assets.urls[1].includes('Material+Symbols+' + symbolStyle));
    assert.ok(assets.urls[1].includes('opsz,wght,FILL,GRAD@20..48,100..700,0..1,0'));
  }
});

test('invalid connector settings and non-text custom CSS are rejected', () => {
  for (const invalid of [{ headingFont: 'Unknown font' }, { symbolStyle: 'Unknown' }, { symbolWeight: 999 }, { symbolFill: 2 }, { symbolSize: 49 }]) {
    assert.throws(() => connectorAssets({ ...DEFAULT_CONNECTORS, ...invalid }), /Invalid/);
  }
  assert.throws(() => emitCss({}, '', {}), /must be a string/);
});
