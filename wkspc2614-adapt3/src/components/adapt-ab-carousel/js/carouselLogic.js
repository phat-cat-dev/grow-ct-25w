/**
 * carouselLogic
 *
 * Pure functions for slide index resolution and visitation, extracted for
 * testability (no Backbone, no DOM). See carouselLogic.test.js.
 */

/**
 * Resolve a requested slide index against the slide count.
 * - canCycle true: wraps around (… -> last when going back from 0, etc.).
 * - canCycle false: clamps to [0, length - 1].
 *
 * @param {number} requested - the raw target index (may be out of range)
 * @param {number} length - number of slides
 * @param {boolean} canCycle
 * @returns {number} a valid index, or 0 when there are no slides
 */
export function resolveIndex(requested, length, canCycle) {
  if (length <= 0) return 0;
  if (canCycle) return ((requested % length) + length) % length;
  return Math.max(0, Math.min(length - 1, requested));
}

/**
 * Mark a slide visited (visitation never un-sets).
 *
 * @param {boolean[]} visited - current visitation flags by index
 * @param {number} index
 * @returns {boolean[]} next visitation flags
 */
export function computeNextVisitation(visited, index) {
  const next = [...visited];
  if (index >= 0 && index < next.length) next[index] = true;
  return next;
}

/**
 * @param {boolean[]} visited
 * @returns {boolean} whether every slide has been visited
 */
export function isAllVisited(visited) {
  return visited.length > 0 && visited.every(Boolean);
}
