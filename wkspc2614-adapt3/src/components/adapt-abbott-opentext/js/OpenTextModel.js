/**
 * OpenTextModel
 *
 * Model for the open-text component. Extends ComponentModel (NOT QuestionModel)
 * to stay outside the scoring machinery.
 *
 * Stores learner text in _text (not _userAnswer — that's QuestionModel vocabulary).
 * Persists via offlineStorage custom keys into cmi.suspend_data.
 *
 * Stage 2: persistence to offlineStorage, restore at adapt:start, fail-closed verification.
 * Stage 4: completion — model owns rule (canComplete), view owns affordance.
 */

import Adapt from 'core/js/adapt';
import ComponentModel from 'core/js/models/componentModel';
import offlineStorage from 'core/js/offlineStorage';
import logging from 'core/js/logging';

const LOG_PREFIX = '[opentext]';
const KEY_PREFIX = 'ot:';
const VALID_VARIANTS = ['reflection', 'notes'];

export default class OpenTextModel extends ComponentModel {

  /**
   * Default values. Variant resolution lives here (spec §2) so the model
   * owns storage tagging and completion rules consistently.
   */
  defaults() {
    return {
      ...super.defaults(),
      _variant: 'reflection',
      _rows: 8,
      _maxRows: 20,
      _maxCharacters: 4000,
      _minCharacters: 0,
      _maxWords: 0,
      _minWords: 0,
      _isCompletionBearing: false,
      _text: ''
    };
  }

  /**
   * Initialize: validate variant, listen for adapt:start to restore text.
   * Model is created during loadManifestFiles(), before adapt:start fires,
   * so the listener attaches in time. Restore happens after spoor's
   * restoreSessionState() (triggered at app:dataReady, before adapt:start).
   */
  init() {
    super.init();
    this._validateVariant();
    this._validateCompletionBearing();
    this.listenToOnce(Adapt, 'adapt:start', this.restoreText);
  }

  /**
   * Validate _variant is in the allowed enum. If not, warn and fall back to default.
   * @private
   */
  _validateVariant() {
    const variant = this.get('_variant');
    if (variant && !VALID_VARIANTS.includes(variant)) {
      const componentId = this.get('_id');
      logging.warn(`${LOG_PREFIX} ${componentId}: Invalid _variant "${variant}" — expected one of [${VALID_VARIANTS.join(', ')}]. Falling back to "reflection".`);
      this.set('_variant', 'reflection');
    }
  }

  /**
   * Validate _isCompletionBearing against variant.
   * Notes variant ignores completion — log a warning so authors know (spec §3).
   * @private
   */
  _validateCompletionBearing() {
    const variant = this.get('_variant');
    const isCompletionBearing = this.get('_isCompletionBearing');

    if (variant === 'notes' && isCompletionBearing) {
      const componentId = this.get('_id');
      logging.warn(`${LOG_PREFIX} ${componentId}: _isCompletionBearing has no effect when _variant is "notes". Notes are never completion-bearing.`);
    }
  }

  /**
   * Whether the completion button should be shown.
   * True only for reflection variant with _isCompletionBearing: true.
   */
  shouldShowCompletionButton() {
    const variant = this.get('_variant');
    const isCompletionBearing = this.get('_isCompletionBearing');
    return variant === 'reflection' && isCompletionBearing === true;
  }

  /**
   * Check if text meets minimum character requirement.
   */
  meetsMinimum() {
    const metChars = this.getCharacterCount() >= this.get('_minCharacters');
    const metWords = !this.isWordMode() || this.getWordCount() >= (this.get('_minWords') || 0);
    return metChars && metWords;
  }

  /**
   * Mark the component as complete.
   * Completion is sticky — once set, never reverted by editing.
   */
  markComplete() {
    this.setCompletionStatus();
  }

  /**
   * Override reset to protect completion (spec §5, §7).
   * Completion is sticky — _isResetOnRevisit must not clear it.
   * AdaptModel.reset() with type='hard' sets _isComplete: false;
   * we preserve it by restoring after super.reset().
   */
  reset(type = 'hard', canReset = this.get('_canReset')) {
    const wasComplete = this.get('_isComplete');
    const didReset = super.reset(type, canReset);
    if (didReset && wasComplete) {
      // Restore sticky completion
      this.set('_isComplete', true);
    }
    return didReset;
  }

  /**
   * Storage key for this component's text.
   */
  getStorageKey() {
    return KEY_PREFIX + this.get('_id');
  }

  /**
   * Resolved placeholder text, defaulted per variant if author didn't specify.
   * View should call this rather than computing placeholder itself.
   */
  getPlaceholder() {
    const placeholder = this.get('placeholder');
    if (placeholder) return placeholder;

    const variant = this.get('_variant');
    return variant === 'notes'
      ? 'Make your notes here…'
      : 'Write your reflection here…';
  }

  /**
   * Get current text value.
   */
  getText() {
    return this.get('_text') || '';
  }

  /**
   * Set text value (updates model, does NOT persist — call saveText() for that).
   */
  setText(text) {
    this.set('_text', text);
  }

  /**
   * Current character count.
   */
  getCharacterCount() {
    return this.getText().length;
  }

  /**
   * Whether a word limit is configured. When _maxWords > 0 the component
   * counts and gates on WORDS (the pedagogy-facing unit); _maxCharacters stays
   * a silent suspend_data backstop. Keep _maxWords well below _maxCharacters.
   */
  isWordMode() {
    return this.get('_maxWords') > 0;
  }

  /**
   * Current word count (whitespace-delimited runs; empty text = 0).
   */
  getWordCount() {
    const text = this.getText().trim();
    return text ? text.split(/\s+/).length : 0;
  }

  /**
   * Check if character count is within allowed limit.
   */
  isWithinLimit() {
    return this.getCharacterCount() <= this.get('_maxCharacters');
  }

  /**
   * Check if character count is approaching limit (within 750 chars).
   */
  isApproachingLimit() {
    const count = this.getCharacterCount();
    const max = this.get('_maxCharacters');
    return count > (max - 750) && count <= max;
  }

  /**
   * Check if character count exceeds limit.
   */
  isOverLimit() {
    const charsOver = this.getCharacterCount() > this.get('_maxCharacters');
    const wordsOver = this.isWordMode() && this.getWordCount() > this.get('_maxWords');
    return charsOver || wordsOver;
  }

  /**
   * Count over the active limit (words in word mode, else characters; 0 if under).
   */
  getOverLimitCount() {
    if (this.isWordMode()) {
      const overWords = this.getWordCount() - this.get('_maxWords');
      if (overWords > 0) return overWords;
    }
    const over = this.getCharacterCount() - this.get('_maxCharacters');
    return over > 0 ? over : 0;
  }

  /**
   * Restore text from offlineStorage.
   * Called on init. Parses defensively — accepts object shape or bare string.
   */
  restoreText() {
    const componentId = this.get('_id');
    const key = this.getStorageKey();

    // Check if spoor/LMS is available
    const scorm = Adapt.spoor?.scorm;
    if (!scorm || !scorm.lmsConnected) {
      logging.debug(`${LOG_PREFIX} ${componentId}: LMS not connected, skipping restore`);
      return;
    }

    let stored;
    try {
      stored = offlineStorage.get(key);
    } catch (e) {
      logging.warn(`${LOG_PREFIX} ${componentId}: Error reading offlineStorage: ${e.message}`);
      return;
    }

    if (stored === undefined || stored === null || stored === '') {
      logging.debug(`${LOG_PREFIX} ${componentId}: No stored text found`);
      return;
    }

    // Parse defensively (spec §6)
    let text;
    if (typeof stored === 'object' && stored.t !== undefined) {
      // Expected shape: { v: "reflection"|"notes", t: "the text" }
      text = stored.t;
      logging.debug(`${LOG_PREFIX} ${componentId}: Restored from object shape (variant: ${stored.v})`);
    } else if (typeof stored === 'string') {
      // Legacy/fallback: bare string (treat as reflection)
      text = stored;
      logging.debug(`${LOG_PREFIX} ${componentId}: Restored from bare string (legacy)`);
    } else {
      // Unexpected shape — don't crash, just log and skip
      logging.warn(`${LOG_PREFIX} ${componentId}: Unexpected stored shape: ${typeof stored}`);
      return;
    }

    this.set('_text', text);

    const preview = text.length > 50 ? text.substring(0, 50) + '...' : text;
    logging.info(`${LOG_PREFIX} ${componentId}: Restored "${preview}" (${text.length} chars)`);
  }

  /**
   * Save text to offlineStorage.
   * Returns { success: boolean, errorCode: number|string }
   *
   * FAIL CLOSED: If write verification fails, reports failure.
   */
  saveText() {
    const componentId = this.get('_id');
    const key = this.getStorageKey();
    const text = this.getText();
    const variant = this.get('_variant');

    // Check if spoor/LMS is available
    const scorm = Adapt.spoor?.scorm;
    if (!scorm) {
      logging.debug(`${LOG_PREFIX} ${componentId}: spoor not available, skipping save`);
      return { success: false, errorCode: 'NO_SPOOR' };
    }

    if (!scorm.lmsConnected) {
      logging.debug(`${LOG_PREFIX} ${componentId}: LMS not connected, skipping save`);
      return { success: false, errorCode: 'NO_LMS' };
    }

    // Store with variant tag (spec §6)
    const payload = { v: variant, t: text };

    logging.debug(`${LOG_PREFIX} ${componentId}: Saving ${text.length} chars...`);

    try {
      offlineStorage.set(key, payload);
    } catch (e) {
      logging.error(`${LOG_PREFIX} ${componentId}: offlineStorage.set() threw: ${e.message}`);
      return { success: false, errorCode: `EXCEPTION: ${e.message}` };
    }

    // Verify the write using fail-closed pattern
    const writeResult = this._checkScormResult(scorm);

    if (writeResult.success) {
      logging.debug(`${LOG_PREFIX} ${componentId}: Saved successfully`);
      // No explicit commit — _commitOnAnyChange commits within ~100ms (spec §6)
    } else {
      logging.error(`${LOG_PREFIX} ${componentId}: WRITE FAILED — SCORM error code: ${writeResult.errorCode}`);
    }

    return writeResult;
  }

  /**
   * Check if the last SCORM operation succeeded.
   * FAIL CLOSED: If error code can't be read, returns failure.
   * @private
   */
  _checkScormResult(scorm) {
    try {
      const debugInterface = scorm.scorm?.debug;
      if (!debugInterface || typeof debugInterface.getCode !== 'function') {
        logging.warn(`${LOG_PREFIX} SCORM debug interface not available`);
        return { success: false, errorCode: 'UNREADABLE' };
      }

      const errorCode = debugInterface.getCode();
      if (typeof errorCode !== 'number') {
        logging.warn(`${LOG_PREFIX} SCORM debug.getCode() returned non-number: ${typeof errorCode}`);
        return { success: false, errorCode: 'UNREADABLE' };
      }

      return { success: errorCode === 0, errorCode };
    } catch (e) {
      logging.warn(`${LOG_PREFIX} Error reading SCORM error code: ${e.message}`);
      return { success: false, errorCode: 'UNREADABLE' };
    }
  }

}
