/**
 * Pure logic functions for the glossary passage component.
 *
 * These functions have no Adapt/Backbone dependencies and can be
 * unit-tested in isolation with Node's built-in test runner.
 *
 * Design refs: GL-3 (passage shape), GB-3 (pure logic)
 */

/**
 * Derive the terms array from a passage.
 *
 * Extracts only segments that carry a _term, assigning contiguous
 * 0-based termIndex values. The sourceIndex tracks position in the
 * original passage for rendering purposes.
 *
 * @param {Array} passage - The _passage array from authored JSON
 * @returns {Array} Array of term objects: { termIndex, sourceIndex, text, term, definition }
 */
export function deriveTermsFromPassage(passage) {
  if (!Array.isArray(passage)) return [];

  const terms = [];
  let termIndex = 0;

  passage.forEach((segment, sourceIndex) => {
    if (segment && segment._term) {
      terms.push({
        termIndex,
        sourceIndex,
        text: segment.text || '',
        term: segment._term.term || '',
        definition: segment._term.definition || ''
      });
      termIndex++;
    }
  });

  return terms;
}

/**
 * Compute the next expansion state (single-open, re-select closes).
 *
 * @param {number|null} currentExpanded - Currently expanded term index, or null if none
 * @param {number} toggledIndex - The term index being toggled
 * @returns {number|null} The new expanded index, or null if closing
 */
export function computeNextTermState(currentExpanded, toggledIndex) {
  // Re-selecting the open term closes it
  if (currentExpanded === toggledIndex) {
    return null;
  }
  // Opening a new term (closes any other)
  return toggledIndex;
}

/**
 * Compute next visitation state.
 *
 * Marks a term as visited on first expansion. Already-visited terms
 * remain visited (idempotent).
 *
 * @param {Array<boolean>} visited - Current visitation state array
 * @param {number} index - Term index being expanded
 * @returns {Array<boolean>} New visitation state array
 */
export function computeNextVisitation(visited, index) {
  if (!Array.isArray(visited)) return [];
  if (index < 0 || index >= visited.length) return visited;

  // Already visited - no change
  if (visited[index]) return visited;

  // Mark as visited (immutable update)
  const newVisited = [...visited];
  newVisited[index] = true;
  return newVisited;
}

/**
 * Check if all terms have been visited.
 *
 * @param {Array<boolean>} visited - Visitation state array
 * @returns {boolean} True if all entries are true
 */
export function isAllVisited(visited) {
  if (!Array.isArray(visited) || visited.length === 0) return false;
  return visited.every(v => v === true);
}

/**
 * Validate term count is within allowed bounds (2–8).
 *
 * GL-8 specifies 2–8 terms per passage. Draft-04 JSON Schema cannot
 * constrain a filtered subset of an array, so this is enforced at runtime.
 *
 * @param {number} count - Number of terms derived from passage
 * @returns {boolean} True if count is valid (2–8 inclusive)
 */
export function isTermCountValid(count) {
  return Number.isInteger(count) && count >= 2 && count <= 8;
}

/**
 * Get the expected trackable fields for this component.
 *
 * Used by tests to assert that expansion state is NOT persisted.
 * Only visitation (_userAnswer) is tracked; _expandedIndex is transient.
 *
 * @returns {Object} Expected trackable field assertions
 */
export function getExpectedTrackableFields() {
  return {
    persisted: ['_userAnswer'],
    transient: ['_expandedIndex']
  };
}
