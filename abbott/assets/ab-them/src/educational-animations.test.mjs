import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { cyclePieces, lineBoxSvg, LINE_PATHS, BOX_PATHS, DRAW_CSS, educationalAnimations } from './educational-animations.mjs';

test('line and box variants combine independently into two ordered normalized strokes', () => {
  for (const line of Object.keys(LINE_PATHS)) {
    for (const box of Object.keys(BOX_PATHS)) {
      const svg = lineBoxSvg(line, box);
      assert.equal((svg.match(/pathLength="1"/g) || []).length, 2);
      assert.ok(svg.indexOf(LINE_PATHS[line]) < svg.indexOf(BOX_PATHS[box]));
    }
  }
  assert.throws(() => lineBoxSvg('invalid', 'rectangle'));
});

test('cycles comprise exactly 1 through 4 consecutive parts and separate arrowheads', () => {
  for (const shape of ['circle', 'triangle']) {
    for (const count of [1, 2, 3, 4]) {
      const pieces = cyclePieces(shape, count);
      assert.equal(pieces.length, count);
      pieces.forEach(piece => {
        assert.ok(piece.d.startsWith('M'));
        assert.match(piece.arrow, /^M.+ L.+ L/);
        assert.ok(!piece.d.includes('NaN') && !piece.arrow.includes('NaN'));
      });
      const endpoints = pieces.map(piece => {
        const start = piece.d.match(/^M([-\d.e+]+) ([-\d.e+]+)/i).slice(1).map(Number);
        const numbers = piece.d.match(/[-+]?\d*\.?\d+(?:e[-+]?\d+)?/gi).map(Number);
        return { start, end: numbers.slice(-2) };
      });
      endpoints.forEach((piece, i) => {
        const next = endpoints[(i + 1) % count].start;
        assert.ok(Math.hypot(piece.end[0] - next[0], piece.end[1] - next[1]) < 1e-8);
      });
    }
  }
  assert.throws(() => cyclePieces('circle', 5));
});

test('master clock, reduced motion and all 18 reusable demos are wired', async () => {
  const html = educationalAnimations();
  assert.equal((html.match(/data-edu-demo/g) || []).length, 18);
  assert.ok(DRAW_CSS.includes('var(--edu-speed,1) / var(--edu-local-speed,1)'));
  assert.ok(DRAW_CSS.includes('prefers-reduced-motion:reduce'));
  assert.ok(DRAW_CSS.includes('@keyframes edu-draw-8-7'));
  const page = await readFile(new URL('../public/site/index.html', import.meta.url), 'utf8');
  assert.ok(page.includes('id="educational-content"'));
  assert.ok(page.includes('src="educational-ui.js"'));
  assert.ok(!page.includes('EDUCATIONAL_ANIMATIONS'));
});
