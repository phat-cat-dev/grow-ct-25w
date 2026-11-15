/**
 * PagefeedbackModel
 *
 * Model for the end-of-page feedback component. Extends ComponentModel (NOT
 * QuestionModel/ItemsComponentModel) — there is no array of items and no
 * correct answer, just a flat two-choice self-report plus an optional note.
 *
 * Stores the response in _response (not _userAnswer — that's QuestionModel
 * vocabulary) and the note in _note. Persists via offlineStorage custom keys
 * into cmi.suspend_data, not cmi.interactions, mirroring adapt-grow-opentext.
 *
 * See: docs/authoring/component-specs/pagefeedback.md
 */

import Adapt from 'core/js/adapt';
import ComponentModel from 'core/js/models/componentModel';
import offlineStorage from 'core/js/offlineStorage';
import logging from 'core/js/logging';
import { VALID_VARIANTS, isValidResponse, resolveChoiceLabels, resolveStatusKey, buildPayload, parsePayload } from './pagefeedbackLogic';

const LOG_PREFIX = '[pagefeedback]';
const KEY_PREFIX = 'pf:';

export default class PagefeedbackModel extends ComponentModel {

  defaults () {
    return {
      ...super.defaults(),
      _variant: 'conversation',
      _choicePositiveLabel: '',
      _choiceNegativeLabel: '',
      _isCompletionBearing: false,
      _response: null,
      _note: '',
      _isSubmitted: false,
      // Transient outcome of the last save action, never persisted — drives
      // which globals string the status line shows. See resolveStatusKey().
      _saveStatus: 'idle'
    };
  }

  /**
   * Initialize: validate variant, listen for adapt:start to restore a
   * previously-saved response. Model is created during loadManifestFiles(),
   * before adapt:start fires, so the listener attaches in time.
   */
  init () {
    super.init();
    this._validateVariant();
    this.listenToOnce(Adapt, 'adapt:start', this.restoreResponse);
  }

  /**
   * Validate _variant is in the allowed enum. If not, warn and fall back to
   * the default. Variant only affects illustration/labels, never behaviour.
   * @private
   */
  _validateVariant () {
    const variant = this.get('_variant');
    if (variant && !VALID_VARIANTS.includes(variant)) {
      const componentId = this.get('_id');
      logging.warn(`${LOG_PREFIX} ${componentId}: Invalid _variant "${variant}" — expected one of [${VALID_VARIANTS.join(', ')}]. Falling back to "conversation".`);
      this.set('_variant', 'conversation');
    }
  }

  /**
   * Resolve the labels to show for the two choice buttons — author
   * overrides win, otherwise the variant default (spec).
   */
  getChoiceLabels () {
    return resolveChoiceLabels(
      this.get('_variant'),
      this.get('_choicePositiveLabel'),
      this.get('_choiceNegativeLabel')
    );
  }

  /**
   * Globals key for the current status line, given the last save outcome
   * and whether a response is currently chosen.
   */
  getStatusKey () {
    return resolveStatusKey(this.get('_saveStatus'), isValidResponse(this.get('_response')));
  }

  /**
   * Mark the component as complete.
   * Completion is sticky — once set, never reverted by a later clear.
   */
  markComplete () {
    this.setCompletionStatus();
  }

  /**
   * Override reset to protect completion, mirroring adapt-grow-opentext.
   * AdaptModel.reset() with type='hard' sets _isComplete: false; restore it
   * after super.reset() if it was already true.
   */
  reset (type = 'hard', canReset = this.get('_canReset')) {
    const wasComplete = this.get('_isComplete');
    const didReset = super.reset(type, canReset);
    if (didReset && wasComplete) {
      this.set('_isComplete', true);
    }
    return didReset;
  }

  /**
   * Storage key for this component's response.
   */
  getStorageKey () {
    return KEY_PREFIX + this.get('_id');
  }

  /**
   * Record a response choice. Does NOT persist — call submitResponse() for
   * that, matching the original demo's "choose, then explicitly save" flow.
   */
  setResponse (value) {
    if (!isValidResponse(value)) return;
    this.set({ _response: value, _saveStatus: 'idle' });
  }

  /**
   * Update the note text. Does NOT persist — saved on submit/clear only, so
   * typing never triggers a write (unlike opentext, which autosaves on a
   * debounce — a note here is secondary content with no size pressure).
   */
  setNote (text) {
    this.set('_note', text || '');
  }

  /**
   * Submit the current response: persists it, and — when this instance is
   * completion-bearing — marks the component complete. Requires a response
   * to already be set; the view is responsible for guarding/announcing when
   * it isn't.
   */
  submitResponse () {
    if (!isValidResponse(this.get('_response'))) {
      this.set('_saveStatus', 'no-response');
      return { success: false, errorCode: 'NO_RESPONSE' };
    }
    this.set('_isSubmitted', true);
    const result = this.saveResponse();
    this.set('_saveStatus', result.success ? 'saved' : 'failed');
    if (result.success && this.get('_isCompletionBearing')) {
      this.markComplete();
    }
    return result;
  }

  /**
   * Clear the response and note, and persist the cleared state immediately
   * so a reload does not resurrect data the learner asked to remove.
   * Deliberately NOT named reset() — that name belongs to AdaptModel's own
   * revisit-reset lifecycle method (see reset() above), and reusing it here
   * would silently shadow it.
   */
  clearResponse () {
    this.set({ _response: null, _note: '', _isSubmitted: false });
    const result = this.saveResponse();
    this.set('_saveStatus', result.success ? 'cleared' : 'failed');
    return result;
  }

  /**
   * Restore a previously-saved response from offlineStorage.
   * Called on init. Parses defensively — unrecognised shapes are skipped,
   * not crashed on.
   */
  restoreResponse () {
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
      logging.debug(`${LOG_PREFIX} ${componentId}: No stored response found`);
      return;
    }

    const parsed = parsePayload(stored);
    if (!parsed) {
      logging.warn(`${LOG_PREFIX} ${componentId}: Unexpected stored shape: ${typeof stored}`);
      return;
    }

    this.set({
      _response: parsed.response,
      _note: parsed.note,
      _isSubmitted: Boolean(parsed.response),
      // Restoring a response means it genuinely was saved previously.
      _saveStatus: parsed.response ? 'saved' : 'idle'
    });

    logging.info(`${LOG_PREFIX} ${componentId}: Restored response "${parsed.response}"`);
  }

  /**
   * Save the current response/note to offlineStorage.
   * Returns { success: boolean, errorCode: number|string }
   *
   * FAIL CLOSED: if write verification fails, reports failure.
   */
  saveResponse () {
    const componentId = this.get('_id');
    const key = this.getStorageKey();
    const payload = buildPayload(this.get('_variant'), this.get('_response'), this.get('_note'));

    const scorm = Adapt.spoor?.scorm;
    if (!scorm) {
      logging.debug(`${LOG_PREFIX} ${componentId}: spoor not available, skipping save`);
      return { success: false, errorCode: 'NO_SPOOR' };
    }

    if (!scorm.lmsConnected) {
      logging.debug(`${LOG_PREFIX} ${componentId}: LMS not connected, skipping save`);
      return { success: false, errorCode: 'NO_LMS' };
    }

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

  /**
   * Check if the last SCORM operation succeeded.
   * FAIL CLOSED: if the error code can't be read, returns failure.
   * @private
   */
  _checkScormResult (scorm) {
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
