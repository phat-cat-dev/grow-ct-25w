import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { LESSON_EXPERIMENTS, lessonExperiment, horizontalPanels } from './lesson-experiments.mjs';

test('six distinct lessons preserve Adapt hierarchy and progressive disclosure defaults', () => {
  assert.equal(LESSON_EXPERIMENTS.length, 6);
  assert.equal(new Set(LESSON_EXPERIMENTS.map(item => item.layout)).size, 6);
  for (const { id } of LESSON_EXPERIMENTS) {
    const html = lessonExperiment(id);
    assert.equal((html.match(/data-lesson-step=/g) || []).length, 3);
    assert.equal((html.match(/data-lesson-complete>/g) || []).length, 3);
    assert.equal((html.match(/data-lesson-step="\d" hidden/g) || []).length, 2);
    assert.ok(html.includes('data-lesson-step="0" open'));
    assert.ok(html.includes('class="lesson-frontmatter" open'));
    for (const layer of ['d2', 'd3', 'd4', 'd5']) assert.ok(html.includes(`data-layer="${layer}"`));
    for (const hook of ['page__inner', 'article__container', 'article__inner', 'block__container', 'block__inner', 'component__container', 'component__inner text__inner']) assert.ok(html.includes(hook));
    assert.ok(html.includes('ab card'));
    assert.ok(html.includes('data-lesson-reset'));
    assert.ok(!html.includes('<h1'));
    assert.ok(html.includes('<h4') && html.includes('<h5') && html.includes('<h6'));
    assert.ok(html.includes('role="heading" aria-level="7"'));
    assert.ok(!html.includes('<h2') && !html.includes('<h3'));
  }
  assert.throws(() => lessonExperiment('bad'), /Unknown lesson/);
});

test('lessons have distinct composition signatures and stage-specific content', () => {
  const signatures = {
    guided: ['lesson-editorial', 'lesson-marginalia', 'Write your field note'],
    workshop: ['lesson-bench-model', 'lesson-workspace', 'Reference approach'],
    story: ['lesson-cinematic', 'lesson-story-decision', 'lesson-story-ending'],
    casebook: ['lesson-case-file', 'lesson-evidence-board', 'lesson-verdict'],
    journey: ['lesson-route-map', 'lesson-checkpoint-banner', 'lesson-arrival'],
    studio: ['lesson-inspiration-wall', 'lesson-sketchbook', 'lesson-gallery'],
  };
  for (const [id, markers] of Object.entries(signatures)) {
    const html = lessonExperiment(id);
    for (const marker of markers) assert.ok(html.includes(marker), `${id}: ${marker}`);
    const otherIds = Object.keys(signatures).filter(other => other !== id);
    for (const other of otherIds) assert.ok(!lessonExperiment(other).includes(markers[0]));
  }
});

test('all lesson buttons use shared schema with varied action treatments', () => {
  const firstActions = new Set();
  for (const { id } of LESSON_EXPERIMENTS) {
    const html = lessonExperiment(id);
    const buttons = [...html.matchAll(/<button\b([^>]*)>/g)];
    assert.equal(buttons.length, 4);
    for (const [, attributes] of buttons) assert.match(attributes, /class="ab btn /);
    const first = buttons.find(([, attributes]) => attributes.includes('data-lesson-complete'));
    firstActions.add(first[1].match(/class="([^"]+)"/)[1]);
  }
  assert.equal(firstActions.size, 6);
});

test('horizontal workspaces have exclusive accessible panels and multiple components', () => {
  const html = horizontalPanels();
  assert.equal((html.match(/class="ab btn primary/g) || []).length, 4);
  assert.equal((html.match(/aria-expanded="true"/g) || []).length, 1);
  assert.equal((html.match(/role="region"/g) || []).length, 4);
  assert.equal((html.match(/ inert/g) || []).length, 3);
  assert.equal((html.match(/ hidden/g) || []).length, 3);
  assert.ok((html.match(/class="component text"/g) || []).length >= 7);
});

test('lesson source, runtime and generated page are wired with reduced-motion and reset support', async () => {
  const read = path => readFile(new URL(path, import.meta.url), 'utf8');
  const [html, css, runtime, site] = await Promise.all([
    read('../public/site/index.html'), read('../public/site/site.css'),
    read('../public/site/lesson-ui.js'), read('../public/site/site.js'),
  ]);
  assert.ok(html.includes('id="lessons-content"'));
  assert.ok(html.includes('<script src="lesson-ui.js" defer>'));
  for (let i = 0; i < 4; i++) {
    assert.ok(html.includes(`aria-controls="lessons-demo-sideways-panel-${i}"`));
    assert.ok(html.includes(`aria-labelledby="lessons-demo-sideways-trigger-${i}"`));
  }
  for (const { id } of LESSON_EXPERIMENTS) {
    assert.equal((html.match(new RegExp(`data-lesson="${id}"`, 'g')) || []).length, 1);
    assert.ok(html.includes(`id="lessons-demo-lesson-${id}-article"`));
    assert.ok(html.includes(`href="#lessons-demo-lesson-${id}-article"`));
  }
  assert.ok(runtime.includes('next.hidden = false'));
  assert.ok(runtime.includes('next.open = true'));
  assert.ok(runtime.includes('completed.clear()'));
  assert.ok(css.includes('prefers-reduced-motion: reduce) { .lesson-experiment .lesson-revealed { animation: none;'));
  assert.match(css, /\.lesson-experiment \.lesson-depth \{ position: absolute; inset-inline-end:/);
  assert.match(css, /\.lesson-experiment :is\(\.page__header, \.article__header, \.lesson-block > summary, \.card-body\) \{ position: relative;/);
  assert.ok(site.includes('[data-lesson]'));
});
