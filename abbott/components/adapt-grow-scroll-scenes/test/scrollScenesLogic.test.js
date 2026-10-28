/**
 * Unit tests for scrollScenesLogic — the engine maths and the presentation
 * resolver, tested without Backbone or the DOM.
 * Run with: node --test test/scrollScenesLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  PRESETS,
  resolvePresentation,
  sceneOffset,
  clampDistance,
  nearestIndex,
  scrollProgress,
  computeSceneStyles,
  isValidEffect
} from '../js/scrollScenesLogic.js';

describe('resolvePresentation', () => {
  it('expands a known preset into its four values', () => {
    const p = resolvePresentation({ _preset: 'technical' });
    strictEqual(p.scheme, 'default');
    strictEqual(p.background, 'grid');
    strictEqual(p.transition, 'drift');
    strictEqual(p.effect, 'fade');
  });

  it('defaults to the original preset when none is given', () => {
    deepStrictEqual(
      resolvePresentation({}),
      { ...PRESETS.original, snap: true }
    );
  });

  it('falls back to the original preset for an unknown preset id', () => {
    const p = resolvePresentation({ _preset: 'does-not-exist' });
    strictEqual(p.background, PRESETS.original.background);
  });

  it('lets a valid override beat the preset', () => {
    const p = resolvePresentation({ _preset: 'calm', _background: 'aurora', _effect: 'blur' });
    strictEqual(p.background, 'aurora');
    strictEqual(p.effect, 'blur');
    // untouched dials still come from the preset
    strictEqual(p.transition, PRESETS.calm.transition);
  });

  it('treats an empty-string override as "inherit the preset"', () => {
    const p = resolvePresentation({ _preset: 'editorial', _scheme: '', _effect: '' });
    strictEqual(p.scheme, PRESETS.editorial.scheme);
    strictEqual(p.effect, PRESETS.editorial.effect);
  });

  it('ignores an invalid override and keeps the preset value', () => {
    const p = resolvePresentation({ _preset: 'atlas', _transition: 'not-a-model' });
    strictEqual(p.transition, PRESETS.atlas.transition);
  });

  it('defaults snap to true and respects an explicit false', () => {
    strictEqual(resolvePresentation({}).snap, true);
    strictEqual(resolvePresentation({ _snap: false }).snap, false);
  });
});

describe('sceneOffset', () => {
  it('is 0 when the scene centre is the viewport centre', () => {
    strictEqual(sceneOffset(500, 500, 800), 0);
  });

  it('is positive when the scene is below the centre', () => {
    strictEqual(sceneOffset(1300, 500, 800), 1);
  });

  it('is negative when the scene is above the centre', () => {
    strictEqual(sceneOffset(-300, 500, 800), -1);
  });

  it('guards against a zero viewport height', () => {
    strictEqual(sceneOffset(10, 0, 0), 10);
  });
});

describe('clampDistance', () => {
  it('is the absolute offset up to 1', () => {
    strictEqual(clampDistance(0.4), 0.4);
    strictEqual(clampDistance(-0.4), 0.4);
  });

  it('clamps beyond one viewport height to 1', () => {
    strictEqual(clampDistance(2.5), 1);
    strictEqual(clampDistance(-9), 1);
  });
});

describe('nearestIndex', () => {
  it('finds the scene closest to the centre', () => {
    strictEqual(nearestIndex([-1.2, -0.3, 0.6, 1.5]), 1);
  });

  it('keeps the first scene on a tie (matches the original)', () => {
    strictEqual(nearestIndex([0.5, -0.5]), 0);
  });

  it('handles a single scene', () => {
    strictEqual(nearestIndex([0.9]), 0);
  });
});

describe('scrollProgress', () => {
  it('is the scrolled fraction of the scrollable range', () => {
    strictEqual(scrollProgress(250, 1000, 500), 0.5);
  });

  it('is 1 when there is nothing to scroll', () => {
    strictEqual(scrollProgress(0, 500, 500), 1);
    strictEqual(scrollProgress(0, 400, 500), 1);
  });
});

describe('computeSceneStyles', () => {
  it('is fully visible and still at the centre with zoom', () => {
    const s = computeSceneStyles(0, 'zoom', false);
    strictEqual(s.opacity, '1');
    strictEqual(s.scale, '1');
    strictEqual(s.filter, 'none');
    strictEqual(s.translate, 'none');
  });

  it('fades and shrinks with distance under zoom, never below 0.35 opacity', () => {
    const s = computeSceneStyles(1, 'zoom', false);
    strictEqual(s.opacity, String(1 - 0.65));
    strictEqual(s.scale, String(1 - 0.12));
  });

  it('adds blur only for the blur effect', () => {
    strictEqual(computeSceneStyles(1, 'blur', false).filter, 'blur(7px)');
    strictEqual(computeSceneStyles(1, 'zoom', false).filter, 'none');
  });

  it('slides on x only for the slide effect, carrying the sign', () => {
    strictEqual(computeSceneStyles(0.5, 'slide', false).translate, '22.5px 0');
    strictEqual(computeSceneStyles(-0.5, 'slide', false).translate, '-22.5px 0');
    strictEqual(computeSceneStyles(0.5, 'fade', false).translate, 'none');
  });

  it('holds everything still for the none effect', () => {
    const s = computeSceneStyles(1, 'none', false);
    strictEqual(s.opacity, '1');
    strictEqual(s.scale, 'none');
    strictEqual(s.filter, 'none');
    strictEqual(s.translate, 'none');
  });

  it('holds everything still under reduced motion, whatever the effect', () => {
    const s = computeSceneStyles(1, 'blur', true);
    strictEqual(s.opacity, '1');
    strictEqual(s.scale, 'none');
    strictEqual(s.filter, 'none');
    strictEqual(s.translate, 'none');
  });

  it('always publishes the two custom properties for the CSS transition models', () => {
    const s = computeSceneStyles(-0.5493, 'fade', false);
    strictEqual(s['--scene-offset'], '-0.5493');
    strictEqual(s['--scene-distance'], '0.5493');
  });
});

describe('isValidEffect', () => {
  it('accepts the five known effects', () => {
    ['none', 'fade', 'slide', 'zoom', 'blur'].forEach(e => strictEqual(isValidEffect(e), true));
  });

  it('rejects anything else', () => {
    strictEqual(isValidEffect('spin'), false);
    strictEqual(isValidEffect(''), false);
  });
});
