/**
 * flipcardLogic.js
 *
 * Pure functions for flipcard state transitions.
 * Extracted for testability without Backbone/DOM dependencies.
 *
 * Design ref: FB-5 (unit tests)
 */

/**
 * Compute the next flipped-state map after toggling an item.
 *
 * @param {Object<number, boolean>} currentFlippedMap - Map of itemIndex -> isFlipped
 * @param {number} itemIndex - Index of the item being toggled
 * @param {string} behaviour - 'independent' or 'single'
 * @returns {Object<number, boolean>} - New flipped-state map
 */
export function computeNextFlippedState(currentFlippedMap, itemIndex, behaviour) {
  const isCurrentlyFlipped = !!currentFlippedMap[itemIndex];
  const newFlippedState = !isCurrentlyFlipped;

  // Start with a copy
  const nextMap = { ...currentFlippedMap };

  if (behaviour === 'single' && newFlippedState) {
    // In single mode, unflip all others when flipping this one
    for (const key of Object.keys(nextMap)) {
      const idx = Number(key);
      if (idx !== itemIndex) {
        nextMap[idx] = false;
      }
    }
  }

  // Toggle this item
  nextMap[itemIndex] = newFlippedState;

  return nextMap;
}

/**
 * Compute the next visitation array after a flip action.
 * Visitation is set on first flip to back (newFlippedState = true), idempotent thereafter.
 *
 * @param {boolean[]} currentVisited - Array of visited states per item
 * @param {number} itemIndex - Index of the item being flipped
 * @param {boolean} newFlippedState - The new flipped state of the item
 * @returns {boolean[]} - New visitation array
 */
export function computeNextVisitation(currentVisited, itemIndex, newFlippedState) {
  const nextVisited = [...currentVisited];

  // Mark as visited on first flip to back, idempotent
  if (newFlippedState && !nextVisited[itemIndex]) {
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
 * items component. Used to verify no transient state (_isFlipped) leaks.
 *
 * This returns the expected inherited fields from ItemsComponentModel.
 * _isFlipped should NOT be in this list.
 *
 * @returns {string[]} - Array of expected trackable field names
 */
export function getExpectedTrackableFields() {
  // These are the standard fields from ItemsComponentModel that get persisted
  // via _userAnswer for visitation tracking. _isFlipped is NOT included.
  return [
    '_isComplete',
    '_isInteractionComplete',
    '_isVisible',
    '_isLocked',
    '_isVisited'
  ];
}
