/**
 * AnnotatedModel
 *
 * Model for the annotated exemplar component. Extends ItemsComponentModel
 * with a custom setUpItems() that derives the items collection from _passage.
 *
 * NOT a question component — no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _expandedIndex tracks which note is currently expanded (single-open).
 * This is transient — NOT persisted to _userAnswer or SCORM.
 *
 * Design refs: AE-1 (schema), AE-6 (completion), AB-2 (derivation)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import ItemModel from 'core/js/models/itemModel';
import {
  deriveNotesFromPassage,
  computeNextNoteState,
  computeNextVisitation,
  isAllVisited
} from './annotatedLogic';

export default class AnnotatedModel extends ItemsComponentModel {

  /**
   * Default values.
   */
  defaults() {
    return {
      ...super.defaults(),
      _expandedIndex: null
    };
  }

  /**
   * Override setUpItems to derive items from _passage.
   *
   * The base class reads directly from _items; we read from _passage,
   * extract only segments carrying _note, and assign contiguous 0-based
   * _index values in note order. This matches the MatchingModel pattern.
   *
   * The _passage array remains intact as the render source.
   * The children collection contains only the notes for visitation tracking.
   */
  setUpItems() {
    const passage = this.get('_passage') || [];
    const notes = deriveNotesFromPassage(passage);

    // Convert notes to item format expected by base class
    const items = notes.map(note => ({
      _index: note.noteIndex,
      _sourceIndex: note.sourceIndex,
      text: note.text,
      title: note.title,
      body: note.body
    }));

    // Store for model access
    this.set('_notes', notes);

    // Register items as children using setChildren()
    // This ensures proper framework integration
    this.setChildren(new Backbone.Collection(items, { model: ItemModel }));
  }

  /**
   * Toggle a note's expansion state.
   *
   * Single-open: opening one note closes another.
   * Re-selecting the open note closes it.
   * Marks the note as visited on first expansion.
   *
   * @param {number} index - The note index to toggle
   */
  toggleNote(index) {
    const currentExpanded = this.get('_expandedIndex');
    const nextExpanded = computeNextNoteState(currentExpanded, index);

    // Update expansion state
    this.set('_expandedIndex', nextExpanded);

    // Mark as visited on expansion (not closure)
    if (nextExpanded !== null) {
      const item = this.getItem(index);
      if (item && !item.get('_isVisited')) {
        item.set('_isVisited', true);
      }
    }
  }

  /**
   * Get the currently expanded note index.
   * @returns {number|null}
   */
  getExpandedIndex() {
    return this.get('_expandedIndex');
  }

  /**
   * Check if a note at given index is expanded.
   * @param {number} index
   * @returns {boolean}
   */
  isNoteExpanded(index) {
    return this.getExpandedIndex() === index;
  }

  /**
   * Close any open note.
   */
  closeNote() {
    this.set('_expandedIndex', null);
  }

  /**
   * Get the derived notes array.
   * @returns {Array}
   */
  getNotes() {
    return this.get('_notes') || [];
  }

  /**
   * Get note count.
   * @returns {number}
   */
  getNoteCount() {
    return this.getChildren().length;
  }

  /**
   * Check if any notes exist.
   * @returns {boolean}
   */
  hasNotes() {
    return this.getNoteCount() > 0;
  }

}
