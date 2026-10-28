/**
 * timelineLogic.js
 *
 * Pure functions for timeline state transitions.
 * Extracted for testability without Backbone/DOM dependencies.
 *
 * Note: This is a separate copy from flipcardLogic.js, not a shared module.
 * Self-contained plugin folders outweigh five lines of near-duplication (TB-3).
 *
 * Design ref: TB-3 (pure logic + tests)
 */

/**
 * Compute the next expanded-state map after toggling an item.
 *
 * @param {Object<number, boolean>} currentExpandedMap - Map of itemIndex -> isExpanded
 * @param {number} itemIndex - Index of the item being toggled
 * @param {string} behaviour - 'single' (default) or 'independent'
 * @returns {Object<number, boolean>} - New expanded-state map
 */
export function computeNextExpandedState(currentExpandedMap, itemIndex, behaviour) {
  const isCurrentlyExpanded = !!currentExpandedMap[itemIndex];
  const newExpandedState = !isCurrentlyExpanded;

  // Start with a copy
  const nextMap = { ...currentExpandedMap };

  if (behaviour === 'single' && newExpandedState) {
    // In single mode, collapse all others when expanding this one
    for (const key of Object.keys(nextMap)) {
      const idx = Number(key);
      if (idx !== itemIndex) {
        nextMap[idx] = false;
      }
    }
  }

  // Toggle this item
  nextMap[itemIndex] = newExpandedState;

  return nextMap;
}

/**
 * Compute the next visitation array after an expand action.
 * Visitation is set on first expand (newExpandedState = true), idempotent thereafter.
 *
 * @param {boolean[]} currentVisited - Array of visited states per item
 * @param {number} itemIndex - Index of the item being expanded
 * @param {boolean} newExpandedState - The new expanded state of the item
 * @returns {boolean[]} - New visitation array
 */
export function computeNextVisitation(currentVisited, itemIndex, newExpandedState) {
  const nextVisited = [...currentVisited];

  // Mark as visited on first expand, idempotent
  if (newExpandedState && !nextVisited[itemIndex]) {
    nextVisited[itemIndex] = true;
  }

  return nextVisited;
}

/**
 * Check if all items have been visited (completion predicate).
 *
 * @param {boolean[]} visited - Array of visited states per item
 * @returns {boolean} - True if all items visited
 */
export function isAllVisited(visited) {
  if (!visited || visited.length === 0) {
    return false;
  }
  return visited.every(v => v === true);
}

/**
 * Get the list of fields that should be in trackable() for a presentational
 * items component. Used to verify no transient state (_isExpanded) leaks.
 *
 * This returns the expected inherited fields from ItemsComponentModel.
 * _isExpanded should NOT be in this list.
 *
 * @returns {string[]} - Array of expected trackable field names
 */
export function getExpectedTrackableFields() {
  // These are the standard fields from ItemsComponentModel that get persisted
  // via _userAnswer for visitation tracking. _isExpanded is NOT included.
  return [
    '_isComplete',
    '_isInteractionComplete',
    '_isVisible',
    '_isLocked',
    '_isVisited'
  ];
}
