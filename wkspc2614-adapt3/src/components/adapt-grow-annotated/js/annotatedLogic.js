/**
 * Pure logic functions for the annotated exemplar component.
 *
 * These functions have no Adapt/Backbone dependencies and can be
 * unit-tested in isolation with Node's built-in test runner.
 *
 * Design refs: AE-2/AE-3 (structured segments), AB-3 (pure logic)
 */

/**
 * Derive the notes array from a passage.
 *
 * Extracts only segments that carry a _note, assigning contiguous
 * 0-based noteIndex values. The sourceIndex tracks position in the
 * original passage for rendering purposes.
 *
 * @param {Array} passage - The _passage array from authored JSON
 * @returns {Array} Array of note objects: { noteIndex, sourceIndex, text, title, body }
 */
export function deriveNotesFromPassage(passage) {
  if (!Array.isArray(passage)) return [];

  const notes = [];
  let noteIndex = 0;

  passage.forEach((segment, sourceIndex) => {
    if (segment && segment._note) {
      notes.push({
        noteIndex,
        sourceIndex,
        text: segment.text || '',
        title: segment._note.title || '',
        body: segment._note.body || ''
      });
      noteIndex++;
    }
  });

  return notes;
}

/**
 * Compute the next expansion state (single-open, re-select closes).
 *
 * @param {number|null} currentExpanded - Currently expanded note index, or null if none
 * @param {number} toggledIndex - The note index being toggled
 * @returns {number|null} The new expanded index, or null if closing
 */
export function computeNextNoteState(currentExpanded, toggledIndex) {
  // Re-selecting the open note closes it
  if (currentExpanded === toggledIndex) {
    return null;
  }
  // Opening a new note (closes any other)
  return toggledIndex;
}

/**
 * Compute next visitation state.
 *
 * Marks a note as visited on first expansion. Already-visited notes
 * remain visited (idempotent).
 *
 * @param {Array<boolean>} visited - Current visitation state array
 * @param {number} index - Note index being expanded
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
 * Check if all notes have been visited.
 *
 * @param {Array<boolean>} visited - Visitation state array
 * @returns {boolean} True if all entries are true
 */
export function isAllVisited(visited) {
  if (!Array.isArray(visited) || visited.length === 0) return false;
  return visited.every(v => v === true);
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
