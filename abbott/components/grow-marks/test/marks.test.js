/**
 * Unit tests for the grow-marks catalogue + pure logic (no DOM).
 * Run with: node --test test/marks.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, ok, deepStrictEqual, match } from 'node:assert';
import {
  MARKS, COLOR_ROLES, getMark, hasMark, listMarks, categories, makeBadge
} from '../src/marksCatalogue.js';
import {
  colorClass, clampSpeed, elementClass, elementMarkup, buildSvg, placeClass, markFromDataset
} from '../src/marksLogic.js';

const KINDS = ['wrap', 'inline', 'highlight'];

describe('catalogue integrity', () => {
  it('every mark has a valid kind and colour role', () => {
    for (const [id, def] of Object.entries(MARKS)) {
      ok(KINDS.includes(def.kind), `${id} has unknown kind ${def.kind}`);
      ok(COLOR_ROLES.includes(def.color), `${id} has unknown colour ${def.color}`);
    }
  });

  it('drawable marks have a viewBox and at least one element', () => {
    for (const [id, def] of Object.entries(MARKS)) {
      if (def.kind === 'highlight') continue;
      ok(typeof def.viewBox === 'string' && def.viewBox.length, `${id} missing viewBox`);
      ok(Array.isArray(def.els) && def.els.length, `${id} missing els`);
    }
  });

  it('wrap marks declare a placement', () => {
    for (const [id, def] of Object.entries(MARKS)) {
      if (def.kind === 'wrap') ok(def.place, `${id} missing place`);
    }
  });

  it('covers both source galleries (marks + bullets)', () => {
    ['underline', 'oval', 'strike', 'highlight', 'tick', 'cross'].forEach(id => ok(hasMark(id), `missing ${id}`));
    ['dot', 'disc', 'ring', 'diamond', 'toggle', 'bookmark'].forEach(id => ok(hasMark(id), `missing ${id}`));
    ok(categories().includes('emphasis'));
    ok(categories().includes('bullet'));
    ok(categories().includes('state'));
  });

  it('listMarks filters by category', () => {
    ok(listMarks('bullet').length >= 10);
    ok(listMarks('emphasis').includes('underline'));
    ok(!listMarks('emphasis').includes('dot'));
  });

  it('getMark / hasMark behave for unknown ids', () => {
    strictEqual(getMark('nope'), null);
    strictEqual(hasMark('nope'), false);
  });
});

describe('colorClass', () => {
  it('maps each role', () => {
    deepStrictEqual(
      ['accent', 'positive', 'negative', 'neutral', 'comment', 'soft'].map(colorClass),
      ['gm-accent', 'gm-ok', 'gm-no', 'gm-warn', 'gm-vio', 'gm-soft']
    );
  });
  it('falls back to accent for unknown/empty', () => {
    strictEqual(colorClass('weird'), 'gm-accent');
    strictEqual(colorClass(undefined), 'gm-accent');
  });
});

describe('clampSpeed', () => {
  it('passes a normal value', () => strictEqual(clampSpeed('1.5'), 1.5));
  it('clamps high and low', () => {
    strictEqual(clampSpeed(5), 2.5);
    strictEqual(clampSpeed(0.1), 0.4);
  });
  it('defaults non-numbers and non-positives to 1', () => {
    strictEqual(clampSpeed('x'), 1);
    strictEqual(clampSpeed(0), 1);
    strictEqual(clampSpeed(-3), 1);
  });
});

describe('elementClass', () => {
  it('maps animation kinds', () => {
    strictEqual(elementClass({ type: 'path', anim: 'ink' }), 'gm-ink');
    strictEqual(elementClass({ type: 'circle', anim: 'pop' }), 'gm-fill gm-pop');
    strictEqual(elementClass({ type: 'circle', anim: 'knob' }), 'gm-fill gm-knob');
    strictEqual(elementClass({ type: 'path', anim: 'static' }), 'gm-dash');
    strictEqual(elementClass({ type: 'text' }), 'gm-num gm-pop');
  });
});

describe('elementMarkup', () => {
  it('gives ink paths pathLength and width', () => {
    const out = elementMarkup({ type: 'path', anim: 'ink', width: 3, d: 'M0 0 L1 1' });
    match(out, /class="gm-ink"/);
    match(out, /pathLength="1"/);
    match(out, /stroke-width:3/);
  });
  it('adds a delay custom property when present, omits it at 0', () => {
    match(elementMarkup({ type: 'path', anim: 'ink', delay: 0.18, d: 'M0 0' }), /--gm-d:0\.18s/);
    const noDelay = elementMarkup({ type: 'path', anim: 'ink', d: 'M0 0' });
    strictEqual(/--gm-d/.test(noDelay), false);
  });
  it('pop elements are fill, with no pathLength', () => {
    const out = elementMarkup({ type: 'circle', anim: 'pop', cx: 20, cy: 20, r: 7 });
    match(out, /class="gm-fill gm-pop"/);
    strictEqual(/pathLength/.test(out), false);
  });
  it('applies a per-element colour override', () => {
    match(elementMarkup({ type: 'path', anim: 'ink', color: 'positive', d: 'M0 0' }), /class="gm-ink gm-ok"/);
  });
  it('renders text badges with content and font size', () => {
    const out = elementMarkup({ type: 'text', anim: 'pop', x: 20, y: 20, content: '3', fontSize: 16 });
    match(out, /<text class="gm-num gm-pop"/);
    match(out, /font-size:16px/);
    match(out, />3<\/text>/);
  });
});

describe('buildSvg', () => {
  it('wraps the elements with the resolved colour class', () => {
    const svg = buildSvg(getMark('tick'), { colorClass: 'gm-ok' });
    match(svg, /^<svg class="gm-svg gm-ok" viewBox="0 0 48 48"/);
    match(svg, /d="M9 26 L21 38 L40 11"/);
  });
  it('uses the mark default colour when none is passed', () => {
    match(buildSvg(getMark('cross')), /class="gm-svg gm-no"/); // cross default = negative
  });
  it('emits preserveAspectRatio for wrap marks', () => {
    match(buildSvg(getMark('underline')), /preserveAspectRatio="none"/);
  });
  it('builds a badge from makeBadge', () => {
    const svg = buildSvg(makeBadge('12'));
    match(svg, /<circle class="gm-fill gm-pop"/);
    match(svg, /<text class="gm-num gm-pop"[^>]*>12<\/text>/);
    match(svg, /font-size:13px/); // two chars -> 13px
  });
});

describe('placeClass', () => {
  it('prefixes the placement', () => {
    strictEqual(placeClass('around'), 'gm-place-around');
    strictEqual(placeClass(), 'gm-place-under');
  });
});

describe('markFromDataset', () => {
  it('reads the data-gm-* options', () => {
    deepStrictEqual(
      markFromDataset({ gmMark: 'oval', gmColor: 'positive', gmSpeed: '1.5', gmHold: 'false', gmVariant: 'tall' }),
      { mark: 'oval', color: 'positive', variant: 'tall', speed: 1.5, hold: false }
    );
  });
  it('omits absent options and defaults hold when the attr is present', () => {
    deepStrictEqual(markFromDataset({ gmMark: 'tick' }), { mark: 'tick' });
    deepStrictEqual(markFromDataset({ gmMark: 'tick', gmHold: 'true' }), { mark: 'tick', hold: true });
  });
});
