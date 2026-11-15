/**
 * Pure logic functions for the checklist component.
 *
 * These functions have no Adapt/Backbone dependencies and can be
 * unit-tested in isolation with Node's built-in test runner.
 *
 * Design refs: CL-4 (untick does not unvisit), CB-3 (pure logic)
 */

/**
 * Compute the next checked state after toggling an item.
 *
 * Independent toggle: ticking one item never affects another.
 *
 * @param {Object} currentMap - Current checked state map { index: boolean }
 * @param {number} index - The item index to toggle
 * @returns {Object} New checked state map
 */
export function computeNextCheckedState(currentMap, index) {
  if (currentMap === null || typeof currentMap !== 'object') {
    return {};
  }

  // Toggle the specified index
  return {
    ...currentMap,
    [index]: !currentMap[index]
  };
}

/**
 * Compute next visitation state.
 *
 * Visitation is ONE-WAY: first tick marks the item visited permanently.
 * Already-visited items remain visited (idempotent). Unticking does NOT
 * unvisit (CL-4).
 *
 * @param {Array<boolean>} visited - Current visitation state array
 * @param {number} index - Item index being ticked
 * @returns {Array<boolean>} New visitation state array
 */
export function computeNextVisitation(visited, index) {
  if (!Array.isArray(visited)) return [];
  if (index < 0 || index >= visited.length) return visited;

  // Already visited - no change (one-way, idempotent)
  if (visited[index]) return visited;

  // Mark as visited (immutable update)
  const newVisited = [...visited];
  newVisited[index] = true;
  return newVisited;
}

/**
 * Check if all items have been visited.
 *
 * @param {Array<boolean>} visited - Visitation state array
 * @returns {boolean} True if all entries are true
 */
export function isAllVisited(visited) {
  if (!Array.isArray(visited) || visited.length === 0) return false;
  return visited.every(v => v === true);
}

/**
 * Count the number of checked items.
 *
 * @param {Object} checkedMap - Checked state map { index: boolean }
 * @returns {number} Number of items currently checked
 */
export function countChecked(checkedMap) {
  if (checkedMap === null || typeof checkedMap !== 'object') return 0;

  return Object.values(checkedMap).filter(v => v === true).length;
}

/**
 * Get the expected trackable fields for this component.
 *
 * Used by tests to assert that checked state is NOT persisted.
 * Only visitation (_userAnswer) is tracked; _isChecked is transient.
 *
 * CRITICAL: _isChecked must NOT appear in persisted fields. This is
 * the tracking-behaviour check specified in the guardrails.
 *
 * @returns {Object} Expected trackable field assertions
 */
export function getExpectedTrackableFields() {
  return {
    persisted: ['_userAnswer'],
    transient: ['_isChecked', '_checkedMap']
  };
}
