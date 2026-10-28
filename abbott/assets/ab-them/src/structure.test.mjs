import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const read = path => readFile(new URL(path, import.meta.url), 'utf8');

test('Adapt structure is registered and generated with prefixed navigation targets', async () => {
  const [builder, source, html] = await Promise.all([
    read('../build-site.mjs'), read('../public/site/08_structure.md'), read('../public/site/index.html'),
  ]);
  assert.ok(builder.includes("['08_structure.md', 'structure', 'Adapt structure']"));
  assert.ok(html.includes('id="structure-content"'));
  assert.ok(html.includes('href="#structure"'));
  for (const id of ['course-menu', 'learning-page', 'layout-block', 'reflection-article']) {
    assert.ok(source.includes(`id="${id}"`));
    assert.equal((html.match(new RegExp(`id="structure-demo-${id}"`, 'g')) || []).length, 1);
    assert.ok(html.includes(`href="#structure-demo-${id}"`));
  }
  assert.ok(source.includes('component__container'));
  assert.ok(source.includes('component__inner text__inner'));
  assert.ok(source.includes('component text is-full'));
  assert.ok(source.includes('not an embedded Adapt runtime'));
  assert.ok(source.includes('not a new export format yet'));
});

test('rail buttons share geometry and Adapt layout selectors stay scoped', async () => {
  const css = await read('../public/site/site.css');
  assert.ok(css.includes('.rail :is(.theme-toggle button, #scheme-open)'));
  assert.ok(css.includes('#scheme-open[aria-expanded="true"]'));
  assert.ok(css.includes('.adapt-specimen .component__container { display: flex; flex-wrap: wrap;'));
  assert.ok(css.includes('.adapt-specimen .component.is-full { flex-basis: 100%; }'));
  assert.ok(!/^\.component__container\s*\{/m.test(css));
});

test('standalone learning template has unique targets and local stylesheets', async () => {
  const path = '../public/site/section/page-template.html';
  const html = await read(path);
  assert.match(html, /^<!doctype html>/i);
  assert.match(html, /<html lang="en">/);
  assert.equal((html.match(/<h1\b/g) || []).length, 1);
  for (const attribute of ['id', 'data-adapt-id']) {
    const values = [...html.matchAll(new RegExp(`\\s${attribute}="([^"]+)"`, 'g'))].map(match => match[1]);
    assert.ok(values.length > 0);
    assert.equal(new Set(values).size, values.length, `Duplicate ${attribute}`);
  }
  const ids = new Set([...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]));
  for (const [, target] of html.matchAll(/href="#([^"]+)"/g)) {
    assert.ok(ids.has(target), `Missing anchor target: ${target}`);
  }
  const stylesheets = [...html.matchAll(/<link rel="stylesheet" href="([^"]+)"/g)];
  assert.equal(stylesheets.length, 2);
  for (const [, href] of stylesheets) {
    assert.ok((await readFile(new URL(href, new URL(path, import.meta.url)), 'utf8')).length > 0);
  }
  assert.ok(html.includes('component text is-left'));
  assert.ok(html.includes('component graphic is-right'));
  assert.ok(html.includes('component text is-full is-raised'));
  assert.ok(!html.includes('is-complete'));
  assert.ok(!html.includes('<script'));
});
