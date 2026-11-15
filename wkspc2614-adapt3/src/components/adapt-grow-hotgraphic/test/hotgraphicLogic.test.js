/**
 * Unit tests for hotgraphicLogic - pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/hotgraphicLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  buildSelectorCandidates,
  resolveHotspotSelector,
  prefixId,
  rewriteIdReference,
  slugFromSrc,
  isAllRequiredVisited,
  composeHotspotLabel
} from '../js/hotgraphicLogic.js';

/**
 * A minimal querySelectorAll-only stand-in for an SVG root, so the resolver
 * can be unit-tested without a DOM implementation. `nodesBySelector` maps a
 * selector string to the array of "nodes" it should return.
 */
function makeFakeRoot(nodesBySelector) {
  return {
    querySelectorAll(selector) {
      return nodesBySelector[selector] || [];
    }
  };
}

describe('buildSelectorCandidates', () => {
  it('prefers an explicit _selector first', () => {
    deepStrictEqual(
      buildSelectorCandidates({ _selector: '.custom', _id: 'learning' }),
      ['.custom', '[data-ab-hotspot="learning"]', '#learning']
    );
  });

  it('falls back to data-attribute then id when no _selector authored', () => {
    deepStrictEqual(
      buildSelectorCandidates({ _id: 'learning' }),
      ['[data-ab-hotspot="learning"]', '#learning']
    );
  });

  it('returns an empty list when neither _selector nor _id is authored', () => {
    deepStrictEqual(buildSelectorCandidates({}), []);
  });
});

describe('resolveHotspotSelector', () => {
  it('resolves via the first selector that matches exactly one node', () => {
    const node = { id: 'w-learning' };
    const root = makeFakeRoot({ '[data-ab-hotspot="learning"]': [node] });
    const result = resolveHotspotSelector(root, { _id: 'learning' });
    strictEqual(result.node, node);
    strictEqual(result.matchedSelector, '[data-ab-hotspot="learning"]');
    strictEqual(result.error, null);
  });

  it('falls through to the next candidate when one selector matches nothing', () => {
    const node = { id: 'w-learning' };
    const root = makeFakeRoot({
      '[data-ab-hotspot="learning"]': [],
      '#learning': [node]
    });
    const result = resolveHotspotSelector(root, { _id: 'learning' });
    strictEqual(result.node, node);
    strictEqual(result.matchedSelector, '#learning');
  });

  it('errors when a selector matches more than one node', () => {
    const root = makeFakeRoot({
      '[data-ab-hotspot="learning"]': [{}, {}]
    });
    const result = resolveHotspotSelector(root, { _id: 'learning' });
    strictEqual(result.node, null);
    strictEqual(typeof result.error, 'string');
    strictEqual(result.error.includes('matched 2 nodes'), true);
  });

  it('errors when no candidate selector matches anything', () => {
    const root = makeFakeRoot({});
    const result = resolveHotspotSelector(root, { _id: 'missing' });
    strictEqual(result.node, null);
    strictEqual(result.error, 'no selector matched any node');
  });

  it('errors when the hotspot has no _id or _selector to try', () => {
    const root = makeFakeRoot({});
    const result = resolveHotspotSelector(root, {});
    strictEqual(result.node, null);
    strictEqual(result.triedSelectors.length, 0);
    strictEqual(result.error, 'no _id or _selector authored');
  });
});

describe('prefixId', () => {
  it('joins the prefix and id with a hyphen', () => {
    strictEqual(prefixId('arrowhead-learning', 'co-1'), 'co-1-arrowhead-learning');
  });
});

describe('rewriteIdReference', () => {
  it('rewrites a CSS url(#id) function reference', () => {
    strictEqual(rewriteIdReference('url(#arrowhead-learning)', 'co-1'), 'url(#co-1-arrowhead-learning)');
  });

  it('rewrites a bare hash reference', () => {
    strictEqual(rewriteIdReference('#diagram-title', 'co-1'), '#co-1-diagram-title');
  });

  it('leaves values with no fragment reference unchanged', () => {
    strictEqual(rewriteIdReference('currentColor', 'co-1'), 'currentColor');
    strictEqual(rewriteIdReference('none', 'co-1'), 'none');
  });

  it('passes through non-string values unchanged', () => {
    strictEqual(rewriteIdReference(null, 'co-1'), null);
    strictEqual(rewriteIdReference(undefined, 'co-1'), undefined);
  });
});

describe('slugFromSrc', () => {
  it('derives a slug from the filename, stripping the extension', () => {
    strictEqual(slugFromSrc('course/en/images/ulaf-cycle.svg'), 'ulaf-cycle');
  });

  it('is case-insensitive about the extension', () => {
    strictEqual(slugFromSrc('course/en/images/ulaf-cycle.SVG'), 'ulaf-cycle');
  });

  it('returns an empty string for an empty src', () => {
    strictEqual(slugFromSrc(''), '');
    strictEqual(slugFromSrc(undefined), '');
  });
});

describe('isAllRequiredVisited', () => {
  it('is true only when every required hotspot has been visited', () => {
    strictEqual(isAllRequiredVisited([
      { _isVisited: true, _hotspot: { _action: 'popup' } },
      { _isVisited: true, _hotspot: { _action: 'popup' } }
    ]), true);
    strictEqual(isAllRequiredVisited([
      { _isVisited: true, _hotspot: { _action: 'popup' } },
      { _isVisited: false, _hotspot: { _action: 'popup' } }
    ]), false);
  });

  it('excludes decorative (_action: none) items from the denominator', () => {
    strictEqual(isAllRequiredVisited([
      { _isVisited: true, _hotspot: { _action: 'popup' } },
      { _isVisited: false, _hotspot: { _action: 'none' } }
    ]), true);
  });

  it('is vacuously true when there are no required hotspots', () => {
    strictEqual(isAllRequiredVisited([]), true);
    strictEqual(isAllRequiredVisited([
      { _isVisited: false, _hotspot: { _action: 'none' } }
    ]), true);
  });
});

describe('composeHotspotLabel', () => {
  it('returns just the title when not visited', () => {
    strictEqual(composeHotspotLabel('Learning', false, 'Visited'), 'Learning');
  });

  it('prepends the visited word when visited, without stacking on repeat calls', () => {
    const first = composeHotspotLabel('Learning', true, 'Visited');
    strictEqual(first, 'Visited. Learning');
    // Simulate a second render with the SAME inputs - must not grow.
    const second = composeHotspotLabel('Learning', true, 'Visited');
    strictEqual(second, 'Visited. Learning');
  });

  it('omits the visited word entirely when none is supplied', () => {
    strictEqual(composeHotspotLabel('Learning', true, ''), 'Learning');
  });
});
