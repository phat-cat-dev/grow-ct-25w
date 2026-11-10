/**
 * GlossaryModel
 *
 * Model for the glossary passage component. Extends ItemsComponentModel
 * with a custom setUpItems() that derives the items collection from _passage.
 *
 * NOT a question component — no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _expandedIndex tracks which term is currently expanded (single-open).
 * This is transient — NOT persisted to _userAnswer or SCORM.
 *
 * Design refs: GL-1 (schema), GL-7 (completion), GB-2 (derivation)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import ItemModel from 'core/js/models/itemModel';
import {
  deriveTermsFromPassage,
  computeNextTermState,
  computeNextVisitation,
  isAllVisited,
  isTermCountValid
} from './glossaryLogic';

export default class GlossaryModel extends ItemsComponentModel {

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
   * extract only segments carrying _term, and assign contiguous 0-based
   * _index values in term order. This matches the AnnotatedModel pattern.
   *
   * The _passage array remains intact as the render source.
   * The children collection contains only the terms for visitation tracking.
   */
  setUpItems() {
    const passage = this.get('_passage') || [];
    const terms = deriveTermsFromPassage(passage);

    // Convert terms to item format expected by base class
    const items = terms.map(term => ({
      _index: term.termIndex,
      _sourceIndex: term.sourceIndex,
      text: term.text,
      term: term.term,
      definition: term.definition
    }));

    // Store for model access
    this.set('_terms', terms);

    // GL-8: Validate term count (2–8). Draft-04 cannot constrain filtered
    // subsets, so we warn at runtime. Not an error — component still renders.
    if (!isTermCountValid(terms.length)) {
      console.warn(
        `[adapt-grow-glossary] Component "${this.get('_id')}" has ${terms.length} marked term(s). ` +
        `Expected 2–8. Check _passage for correct _term markup.`
      );
    }

    // Register items as children using setChildren()
    // This ensures proper framework integration
    this.setChildren(new Backbone.Collection(items, { model: ItemModel }));
  }

  /**
   * Toggle a term's expansion state.
   *
   * Single-open: opening one term closes another.
   * Re-selecting the open term closes it.
   * Marks the term as visited on first expansion.
   *
   * @param {number} index - The term index to toggle
   */
  toggleTerm(index) {
    const currentExpanded = this.get('_expandedIndex');
    const nextExpanded = computeNextTermState(currentExpanded, index);

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
   * Get the currently expanded term index.
   * @returns {number|null}
   */
  getExpandedIndex() {
    return this.get('_expandedIndex');
  }

  /**
   * Check if a term at given index is expanded.
   * @param {number} index
   * @returns {boolean}
   */
  isTermExpanded(index) {
    return this.getExpandedIndex() === index;
  }

  /**
   * Close any open term.
   */
  closeTerm() {
    this.set('_expandedIndex', null);
  }

  /**
   * Get the derived terms array.
   * @returns {Array}
   */
  getTerms() {
    return this.get('_terms') || [];
  }

  /**
   * Get term count.
   * @returns {number}
   */
  getTermCount() {
    return this.getChildren().length;
  }

  /**
   * Check if any terms exist.
   * @returns {boolean}
   */
  hasTerms() {
    return this.getTermCount() > 0;
  }

}
