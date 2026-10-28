/**
 * hotgraphicLogic
 *
 * Pure functions for the ab-hotgraphic interface layer: resolving an authored
 * hotspot to a node in an inlined SVG, namespacing ids so two diagrams on one
 * page never collide, and the all-required-visited completion rule. No
 * Backbone, no jQuery, no module-level DOM access - see hotgraphicLogic.test.js.
 */

/**
 * Build the ordered list of CSS selectors to try when resolving a hotspot to
 * a node in the inlined SVG. First match wins (see resolveHotspotSelector).
 *
 * @param {object} hotspot - an item's `_hotspot` config
 * @param {string} [hotspot._selector] - an explicit author-supplied selector
 * @param {string} [hotspot._id] - the hotspot's conventional identifier
 * @returns {string[]}
 */
export function buildSelectorCandidates(hotspot) {
  const candidates = [];
  if (hotspot?._selector) candidates.push(hotspot._selector);
  if (hotspot?._id) {
    candidates.push(`[data-ab-hotspot="${hotspot._id}"]`);
    candidates.push(`#${hotspot._id}`);
  }
  return candidates;
}

/**
 * Resolve a hotspot to exactly one node in an inlined SVG, trying each
 * candidate selector in turn. Zero or multiple matches on a selector is not
 * an automatic failure - the next candidate is tried - but zero or multiple
 * matches across ALL candidates is a hard authoring error.
 *
 * @param {{ querySelectorAll: function(string): ArrayLike }} root - the
 *   inlined SVG root (or any object exposing querySelectorAll, which is all
 *   this function needs - kept duck-typed so it is unit-testable without a
 *   DOM implementation)
 * @param {object} hotspot - an item's `_hotspot` config
 * @returns {{ node: object|null, matchedSelector: string|null, triedSelectors: string[], error: string|null }}
 */
export function resolveHotspotSelector(root, hotspot) {
  const triedSelectors = buildSelectorCandidates(hotspot);
  if (!triedSelectors.length) {
    return { node: null, matchedSelector: null, triedSelectors, error: 'no _id or _selector authored' };
  }
  for (const selector of triedSelectors) {
    const matches = Array.from(root.querySelectorAll(selector));
    if (matches.length === 1) {
      return { node: matches[0], matchedSelector: selector, triedSelectors, error: null };
    }
    if (matches.length > 1) {
      return { node: null, matchedSelector: null, triedSelectors, error: `selector "${selector}" matched ${matches.length} nodes, expected 1` };
    }
  }
  return { node: null, matchedSelector: null, triedSelectors, error: 'no selector matched any node' };
}

/**
 * Namespace an id with the component's own id, so two instances of the same
 * (or different) diagram on one page never collide.
 *
 * @param {string} id
 * @param {string} prefix - the component's `_id`
 * @returns {string}
 */
export function prefixId(id, prefix) {
  return `${prefix}-${id}`;
}

/**
 * Rewrite a single attribute VALUE that may contain an intra-document
 * fragment reference, prefixing the referenced id. Handles both forms used
 * across SVG: the CSS function form (`url(#foo)`, used by fill, stroke,
 * marker-start/mid/end, clip-path, mask and filter) and the bare-hash form
 * (`#foo`, used by href, xlink:href, aria-labelledby, aria-describedby, for).
 *
 * Values with no fragment reference are returned unchanged.
 *
 * @param {string} value
 * @param {string} prefix
 * @returns {string}
 */
export function rewriteIdReference(value, prefix) {
  if (typeof value !== 'string') return value;
  const urlMatch = value.match(/^url\(#([^)]+)\)$/);
  if (urlMatch) return `url(#${prefixId(urlMatch[1], prefix)})`;
  // A bare "#..." on a paint attribute (fill/stroke) is a COLOUR, not a fragment
  // reference — never prefix a hex colour. Without this guard, fills like
  // "#ADB5BD" became the invalid "#<componentId>-ADB5BD". Genuine id refs
  // (href / xlink:href / aria-*) still get prefixed below.
  if (/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(value)) return value;
  if (value.startsWith('#')) return `#${prefixId(value.slice(1), prefix)}`;
  return value;
}

/**
 * Derive a diagram slug from its asset path, e.g.
 * "course/en/images/ulaf-cycle.svg" -> "ulaf-cycle".
 *
 * @param {string} src
 * @returns {string}
 */
export function slugFromSrc(src) {
  if (!src) return '';
  const filename = src.split('/').pop() || '';
  return filename.replace(/\.svg$/i, '');
}

/**
 * Completion rule: every hotspot whose `_action` is not "none" must be
 * visited. Decorative hotspots (`_action: "none"`) are excluded from the
 * denominator so they can never block completion. A diagram with no required
 * hotspots at all is vacuously complete.
 *
 * @param {Array<{ _isVisited: boolean, _hotspot?: { _action?: string } }>} items
 * @returns {boolean}
 */
export function isAllRequiredVisited(items) {
  const required = (items || []).filter(item => item?._hotspot?._action !== 'none');
  if (!required.length) return true;
  return required.every(item => item._isVisited);
}

/**
 * Compose a hotspot's accessible label from scratch on every call - never
 * append to a previous render's output, which would stack repeat
 * announcements (the bug this deliberately avoids is in
 * adapt-contrib-hotgraphic's hotgraphicView.js, which prepends into
 * el.innerHTML on every change).
 *
 * @param {string} title
 * @param {boolean} isVisited
 * @param {string} visitedWord - e.g. the `_globals._accessibility._ariaLabels.visited` string
 * @returns {string}
 */
export function composeHotspotLabel(title, isVisited, visitedWord) {
  return [isVisited && visitedWord, title].filter(Boolean).join('. ');
}
