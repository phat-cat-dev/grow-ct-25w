/**
 * ReflectionModuleModel
 *
 * Model for the GROW reflection module — a composed reflection activity: a lined
 * "sketchbook" journal where the learner develops a thought, paired with a
 * "change the lens" panel of reframing prompts.
 *
 * The writing half behaves exactly like adapt-grow-journal: it extends
 * ComponentModel (NOT QuestionModel), has no correct answer, and persists via
 * offlineStorage custom keys into cmi.suspend_data (not cmi.interactions, which
 * would truncate prose at 250 chars and mark it incorrect). The lens prompts are
 * static authored content and hold no state.
 */

import Adapt from 'core/js/adapt';
import ComponentModel from 'core/js/models/componentModel';
import offlineStorage from 'core/js/offlineStorage';
import logging from 'core/js/logging';

const LOG_PREFIX = '[grow-reflection-module]';
const KEY_PREFIX = 'grm:';
const VALID_VARIANTS = ['reflection', 'notes'];

export default class ReflectionModuleModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _variant: 'reflection',
      _rows: 4,
      _maxRows: 20,
      _maxCharacters: 4000,
      _minCharacters: 0,
      _maxWords: 0,
      _minWords: 0,
      _isCompletionBearing: false,
      _text: ''
    };
  }

  init() {
    super.init();
    this._validateVariant();
    this._validateCompletionBearing();
    this.listenToOnce(Adapt, 'adapt:start', this.restoreText);
  }

  _validateVariant() {
    const variant = this.get('_variant');
    if (variant && !VALID_VARIANTS.includes(variant)) {
      const componentId = this.get('_id');
      logging.warn(`${LOG_PREFIX} ${componentId}: Invalid _variant "${variant}" — expected one of [${VALID_VARIANTS.join(', ')}]. Falling back to "reflection".`);
      this.set('_variant', 'reflection');
    }
  }

  _validateCompletionBearing() {
    const variant = this.get('_variant');
    const isCompletionBearing = this.get('_isCompletionBearing');
    if (variant === 'notes' && isCompletionBearing) {
      const componentId = this.get('_id');
      logging.warn(`${LOG_PREFIX} ${componentId}: _isCompletionBearing has no effect when _variant is "notes". Notes are never completion-bearing.`);
    }
  }

  shouldShowCompletionButton() {
    const variant = this.get('_variant');
    const isCompletionBearing = this.get('_isCompletionBearing');
    return variant === 'reflection' && isCompletionBearing === true;
  }

  meetsMinimum() {
    const metChars = this.getCharacterCount() >= this.get('_minCharacters');
    const metWords = !this.isWordMode() || this.getWordCount() >= (this.get('_minWords') || 0);
    return metChars && metWords;
  }

  markComplete() {
    this.setCompletionStatus();
  }

  /**
   * Completion is sticky — _isResetOnRevisit must not clear it.
   */
  reset(type = 'hard', canReset = this.get('_canReset')) {
    const wasComplete = this.get('_isComplete');
    const didReset = super.reset(type, canReset);
    if (didReset && wasComplete) this.set('_isComplete', true);
    return didReset;
  }

  getStorageKey() {
    return KEY_PREFIX + this.get('_id');
  }

  getPlaceholder() {
    const placeholder = this.get('placeholder');
    if (placeholder) return placeholder;
    const variant = this.get('_variant');
    return variant === 'notes'
      ? 'Make your notes here…'
      : 'Capture a thought, question or next step…';
  }

  getText() {
    return this.get('_text') || '';
  }

  setText(text) {
    this.set('_text', text);
  }

  getCharacterCount() {
    return this.getText().length;
  }

  isWordMode() {
    return this.get('_maxWords') > 0;
  }

  getWordCount() {
    const text = this.getText().trim();
    return text ? text.split(/\s+/).length : 0;
  }

  isWithinLimit() {
    return this.getCharacterCount() <= this.get('_maxCharacters');
  }

  isApproachingLimit() {
    const count = this.getCharacterCount();
    const max = this.get('_maxCharacters');
    return count > (max - 750) && count <= max;
  }

  isOverLimit() {
    const charsOver = this.getCharacterCount() > this.get('_maxCharacters');
    const wordsOver = this.isWordMode() && this.getWordCount() > this.get('_maxWords');
    return charsOver || wordsOver;
  }

  getOverLimitCount() {
    if (this.isWordMode()) {
      const overWords = this.getWordCount() - this.get('_maxWords');
      if (overWords > 0) return overWords;
    }
    const over = this.getCharacterCount() - this.get('_maxCharacters');
    return over > 0 ? over : 0;
  }

  restoreText() {
    const componentId = this.get('_id');
    const key = this.getStorageKey();

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

    let text;
    if (typeof stored === 'object' && stored.t !== undefined) {
      text = stored.t;
      logging.debug(`${LOG_PREFIX} ${componentId}: Restored from object shape (variant: ${stored.v})`);
    } else if (typeof stored === 'string') {
      text = stored;
      logging.debug(`${LOG_PREFIX} ${componentId}: Restored from bare string (legacy)`);
    } else {
      logging.warn(`${LOG_PREFIX} ${componentId}: Unexpected stored shape: ${typeof stored}`);
      return;
    }

    this.set('_text', text);
    const preview = text.length > 50 ? text.substring(0, 50) + '...' : text;
    logging.info(`${LOG_PREFIX} ${componentId}: Restored "${preview}" (${text.length} chars)`);
  }

  /**
   * FAIL CLOSED: if write verification fails, report failure.
   */
  saveText() {
    const componentId = this.get('_id');
    const key = this.getStorageKey();
    const text = this.getText();
    const variant = this.get('_variant');

    const scorm = Adapt.spoor?.scorm;
    if (!scorm) {
      logging.debug(`${LOG_PREFIX} ${componentId}: spoor not available, skipping save`);
      return { success: false, errorCode: 'NO_SPOOR' };
    }
    if (!scorm.lmsConnected) {
      logging.debug(`${LOG_PREFIX} ${componentId}: LMS not connected, skipping save`);
      return { success: false, errorCode: 'NO_LMS' };
    }

    const payload = { v: variant, t: text };
    logging.debug(`${LOG_PREFIX} ${componentId}: Saving ${text.length} chars...`);

    try {
      offlineStorage.set(key, payload);
    } catch (e) {
      logging.error(`${LOG_PREFIX} ${componentId}: offlineStorage.set() threw: ${e.message}`);
      return { success: false, errorCode: `EXCEPTION: ${e.message}` };
    }

    const writeResult = this._checkScormResult(scorm);
    if (writeResult.success) {
      logging.debug(`${LOG_PREFIX} ${componentId}: Saved successfully`);
    } else {
      logging.error(`${LOG_PREFIX} ${componentId}: WRITE FAILED — SCORM error code: ${writeResult.errorCode}`);
    }
    return writeResult;
  }

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
