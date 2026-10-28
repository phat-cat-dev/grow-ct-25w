/**
 * accordionLogic
 *
 * Pure functions for the accordion's open/close decisions, extracted for
 * testability (no Backbone, no DOM). See accordionLogic.test.js.
 */

/**
 * Compute the next open-state map after toggling one item.
 *
 * @param {Object<number,boolean>} current - index -> isOpen
 * @param {number} index - the item being toggled
 * @param {boolean} isMultiSelect - allow multiple panels open at once
 * @param {boolean} [forceOpen] - if boolean, set that state instead of toggling
 * @returns {Object<number,boolean>} the next open-state map
 */
export function computeNextOpenState(current, index, isMultiSelect, forceOpen) {
  const next = { ...current };
  const open = (typeof forceOpen === 'boolean') ? forceOpen : !current[index];

  if (!isMultiSelect && open) {
    // single-open: close every other panel
    Object.keys(next).forEach(k => { next[k] = false; });
  }
  next[index] = open;
  return next;
}

/**
 * Mark an item visited when it is opened (visitation never un-sets).
 *
 * @param {boolean[]} visited - current visitation flags by index
 * @param {number} index
 * @param {boolean} isNowOpen
 * @returns {boolean[]} next visitation flags
 */
export function computeNextVisitation(visited, index, isNowOpen) {
  const next = [...visited];
  if (isNowOpen) next[index] = true;
  return next;
}
