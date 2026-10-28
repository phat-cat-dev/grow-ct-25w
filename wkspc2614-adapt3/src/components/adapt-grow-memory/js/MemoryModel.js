/**
 * MemoryModel
 *
 * Model for the memory match component. Extends ComponentModel (NOT
 * QuestionModel) so it never touches the scoring machinery — no marking, no
 * _userAnswer, no cmi.interactions.
 *
 * Responsibilities:
 *  - Build the shuffled deck once, on init, from the authored pairs.
 *    Two tiles per pair, sharing a pair key, shuffled with Fisher-Yates.
 *    Held as a plain property (getDeck) so it never leaks into suspend_data.
 *  - Expose the pair count and the completion-bearing decision.
 *
 * The deck reshuffles on every page load (the game resets each visit). The
 * view owns the interactive game state and the completion call.
 */

import ComponentModel from 'core/js/models/componentModel';

export default class MemoryModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _isCompletionBearing: true,
      _columns: 0
    };
  }

  init() {
    super.init();
    this.buildDeck();
  }

  /**
   * Build a shuffled deck of tiles from the authored pairs.
   * Each pair yields two tiles that share a `_pair` key; the accessible
   * `label` falls back alt -> text -> icon so an icon-only tile still reads.
   * @private
   */
  buildDeck() {
    const items = this.get('_items') || [];
    const tiles = [];

    items.forEach((item, pairIndex) => {
      const label = item.alt || item.text || item.icon || '';
      for (let copy = 0; copy < 2; copy++) {
        tiles.push({
          _pair: pairIndex,
          icon: item.icon || '',
          text: item.text || '',
          label
        });
      }
    });

    this._deck = this._shuffle(tiles).map((tile, index) => ({
      ...tile,
      _index: index,
      _number: index + 1
    }));
  }

  /**
   * Fisher-Yates shuffle on a copy of the array.
   * @private
   */
  _shuffle(array) {
    const result = array.slice();
    for (let i = result.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  /**
   * The shuffled deck (array of tile descriptors). Stable for this instance.
   */
  getDeck() {
    return this._deck || [];
  }

  /**
   * Number of pairs to find (one per authored item).
   */
  getPairCount() {
    return (this.get('_items') || []).length;
  }

  /**
   * Whether finding all pairs should mark the component complete.
   * Defaults to true; authors opt out for a purely formative game.
   */
  isCompletionBearing() {
    return this.get('_isCompletionBearing') !== false;
  }

}
