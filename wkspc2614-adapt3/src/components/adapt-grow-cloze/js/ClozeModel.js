/**
 * ClozeModel
 *
 * Model for the fill-the-blanks component. Extends ComponentModel (NOT
 * QuestionModel) to stay outside the scoring machinery entirely: no score, no
 * cmi.interactions, no result status.
 *
 * Parses the author's `text` (plain text with [[1]], [[2]], ... placeholders)
 * into an ordered list of segments the template can render: literal text runs
 * interleaved with blank descriptors. Correct answers stay in the model and are
 * compared by blank index in the view; they are never written into the DOM.
 */
import ComponentModel from 'core/js/models/componentModel';
import logging from 'core/js/logging';

const LOG_PREFIX = '[growCloze]';
const PLACEHOLDER = /\[\[(\d+)\]\]/g;

export default class ClozeModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      text: '',
      _blanks: [],
      _isCompletionBearing: false
    };
  }

  init() {
    super.init();
    this._buildSegments();
  }

  /**
   * Split `text` on [[n]] placeholders into an ordered segment list. Each matched
   * placeholder becomes a blank segment carrying its options; everything else is a
   * text segment. A placeholder with no matching _blanks entry is left as literal
   * text and warned about, so an authoring slip degrades gracefully.
   * @private
   */
  _buildSegments() {
    const id = this.get('_id');
    const text = this.get('text') || '';
    const blanks = this.get('_blanks') || [];
    const segments = [];

    let lastIndex = 0;
    let match;
    let used = 0;
    PLACEHOLDER.lastIndex = 0;

    while ((match = PLACEHOLDER.exec(text)) !== null) {
      if (match.index > lastIndex) {
        segments.push({ _type: 'text', _value: text.slice(lastIndex, match.index) });
      }
      const number = parseInt(match[1], 10);
      const blankIndex = number - 1;
      const blank = blanks[blankIndex];

      if (blank) {
        segments.push({
          _type: 'blank',
          _index: blankIndex,
          _number: number,
          _options: Array.isArray(blank._options) ? blank._options : []
        });
        used++;
      } else {
        logging.warn(`${LOG_PREFIX} ${id}: placeholder [[${number}]] has no matching _blanks entry; left as literal text.`);
        segments.push({ _type: 'text', _value: match[0] });
      }
      lastIndex = PLACEHOLDER.lastIndex;
    }

    if (lastIndex < text.length) {
      segments.push({ _type: 'text', _value: text.slice(lastIndex) });
    }

    if (used === 0 && blanks.length > 0) {
      logging.warn(`${LOG_PREFIX} ${id}: no [[n]] placeholders found in text; no blanks will render inline.`);
    }

    this._segments = segments;
    this._blankCount = used;
  }

  /**
   * Ordered segment list for the template (text runs and blank descriptors).
   */
  getSegments() {
    return this._segments || [];
  }

  /**
   * Number of blanks actually placed in the sentence.
   */
  getBlankCount() {
    return this._blankCount || 0;
  }

  /**
   * Correct answer string for a blank, by 0-based index. Kept in the model (not
   * the DOM) so the view compares against it at Check time.
   */
  getAnswer(index) {
    const blank = (this.get('_blanks') || [])[index];
    return blank ? blank._answer : undefined;
  }

  /**
   * Whether this component completes on the first Check (informational only).
   */
  isCompletionBearing() {
    return this.get('_isCompletionBearing') === true;
  }

}
