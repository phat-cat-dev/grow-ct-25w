/**
 * adapt-abbott-reflective-store
 *
 * Stores and restores reflective textInput answers in SCORM suspend_data via
 * offlineStorage custom keys. Solves RTR-1: cross-session SCORM resume now
 * preserves full-length reflective text.
 *
 * The original cmi.interactions approach was disproven (30 July 2026): spoor
 * truncates learner_response to 250 chars (SCORM 2004 SPM). This extension
 * stores text in cmi.suspend_data instead, which has a 64,000-char budget
 * (measured practical ceiling ~52,000 on Cardiff Met Moodle).
 *
 * Keys: one per component, 'rtr:<componentId>' (e.g. 'rtr:L02-c-40').
 * Allowlist: textinput component type only, single-item only.
 * Dependency: requires Phase 1 patch (adapt-contrib-textInput+reflective-answer-restore.patch)
 *             which creates _userAnswerText in storeUserAnswer() and reads it in restoreUserAnswers().
 *
 * @author Abbott
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import offlineStorage from 'core/js/offlineStorage';
import logging from 'core/js/logging';

const LOG_PREFIX = '[reflective-store]';
const KEY_PREFIX = 'rtr:';

// Explicit allowlist of component types to store/restore
const ALLOWED_COMPONENT_TYPES = ['textinput'];

/**
 * Check if the last SCORM operation succeeded by reading the error code.
 * Returns { success: boolean, errorCode: number|string }
 *
 * FAIL CLOSED: If the error code cannot be read, returns failure with
 * errorCode: 'UNREADABLE' — never assume success on an unreadable path.
 *
 * NOTE: The error code reflects the most recent SCORM API call. When used
 * immediately after a specific operation (set or commit), it reliably
 * indicates that operation's result.
 */
function checkScormResult(scorm) {
  try {
    // Access the pipwerks SCORM API's debug interface
    // Path: Adapt.spoor.scorm (wrapper) → .scorm (pipwerks.SCORM) → .debug → .getCode()
    const debugInterface = scorm.scorm?.debug;
    if (!debugInterface || typeof debugInterface.getCode !== 'function') {
      logging.warn(`${LOG_PREFIX} SCORM debug interface not available — cannot verify write`);
      return { success: false, errorCode: 'UNREADABLE' };
    }

    const errorCode = debugInterface.getCode();
    if (typeof errorCode !== 'number') {
      logging.warn(`${LOG_PREFIX} SCORM debug.getCode() returned non-number: ${typeof errorCode}`);
      return { success: false, errorCode: 'UNREADABLE' };
    }

    return {
      success: errorCode === 0,
      errorCode
    };
  } catch (e) {
    // If we can't read the error code, FAIL CLOSED — don't assume success
    logging.warn(`${LOG_PREFIX} Error reading SCORM error code: ${e.message}`);
    return { success: false, errorCode: 'UNREADABLE' };
  }
}

/**
 * Force an explicit commit to persist suspend_data immediately.
 * Uses Adapt.spoor.scorm.commit() directly — the suspend_data was just
 * updated by offlineStorage.set(), so we only need to commit.
 *
 * FAIL CLOSED: If the commit result cannot be verified, reports failure.
 * Returns { success: boolean, errorCode: number|string }
 *
 * NOTE: scorm.commit() returns void. We verify success by checking the
 * SCORM error code immediately after the call. Since commit() is synchronous
 * and we call it directly (not via offlineStorage.save()), the error code
 * unambiguously reflects the commit operation.
 */
function forceCommit(scorm, componentId) {
  logging.info(`${LOG_PREFIX} ${componentId}: forcing explicit commit...`);

  try {
    // Call commit() directly on the wrapper.
    // We don't use offlineStorage.save() because:
    // 1. It calls saveSessionState() first, which is redundant (we just did a set())
    // 2. It makes the error code ambiguous (could be from set or commit)
    scorm.commit();
  } catch (e) {
    logging.error(`${LOG_PREFIX} ${componentId}: commit threw: ${e.message}`);
    return { success: false, errorCode: `EXCEPTION: ${e.message}` };
  }

  // Verify the commit succeeded using the same fail-closed pattern.
  // The error code now unambiguously reflects the commit operation.
  const commitResult = checkScormResult(scorm);

  if (commitResult.success) {
    logging.info(`${LOG_PREFIX} ${componentId}: commit succeeded — data persisted to LMS`);
  } else {
    logging.error(`${LOG_PREFIX} ${componentId}: COMMIT FAILED — SCORM error code: ${commitResult.errorCode}`);
    logging.error(`${LOG_PREFIX} The reflective text was written to suspend_data but NOT committed to the LMS.`);
    logging.error(`${LOG_PREFIX} The data may be lost if the session ends without a subsequent successful commit.`);
  }

  return commitResult;
}

/**
 * Restore reflective text from offlineStorage custom keys.
 * Called on adapt:start (before adapt:initialize / restoreUserAnswers).
 */
function restoreReflectiveText() {
  logging.debug(`${LOG_PREFIX} Restore phase starting...`);

  // Check if spoor is available
  const scorm = Adapt.spoor?.scorm;
  if (!scorm) {
    logging.debug(`${LOG_PREFIX} spoor.scorm not available, skipping restore`);
    return;
  }

  // Check LMS connection
  if (!scorm.lmsConnected) {
    logging.debug(`${LOG_PREFIX} LMS not connected, skipping restore`);
    return;
  }

  // Trigger offlineStorage restore (ensures suspendDataRestored is true)
  try {
    offlineStorage.get();
  } catch (e) {
    logging.warn(`${LOG_PREFIX} Error reading offlineStorage: ${e.message}`);
    return;
  }

  let restoredCount = 0;

  // Iterate all components to find textInput ones with stored text
  Adapt.components.forEach(model => {
    const componentType = model.get('_component');
    const componentId = model.get('_id');

    // Check allowlist
    if (!ALLOWED_COMPONENT_TYPES.includes(componentType)) {
      return;
    }

    // Check for multi-item components (only restore single-item)
    const items = model.get('_items');
    if (items && items.length > 1) {
      logging.debug(`${LOG_PREFIX} Skipping multi-item ${componentId} (${items.length} items)`);
      return;
    }

    // Check if _userAnswerText already has content (don't overwrite)
    const existingText = model.get('_userAnswerText');
    if (existingText && existingText[0] && existingText[0].length > 0) {
      logging.debug(`${LOG_PREFIX} ${componentId} already has _userAnswerText, not overwriting`);
      return;
    }

    // Read from offlineStorage
    const key = KEY_PREFIX + componentId;
    let storedText;
    try {
      storedText = offlineStorage.get(key);
    } catch (e) {
      logging.warn(`${LOG_PREFIX} Error reading key '${key}': ${e.message}`);
      return;
    }

    // Skip if no stored text
    if (storedText === undefined || storedText === null || storedText === '') {
      return;
    }

    // Set _userAnswerText on the model
    // textInput's restoreUserAnswers() will read this and render it
    model.set('_userAnswerText', [storedText]);

    const preview = storedText.length > 50 ? storedText.substring(0, 50) + '...' : storedText;
    logging.info(`${LOG_PREFIX} Restored ${componentId}: "${preview}" (${storedText.length} chars)`);
    restoredCount++;
  });

  if (restoredCount > 0) {
    logging.info(`${LOG_PREFIX} Restore complete: ${restoredCount} component(s) restored from suspend_data`);
  } else {
    logging.debug(`${LOG_PREFIX} Restore complete: no reflective text found to restore`);
  }
}

/**
 * Store reflective text to offlineStorage on submit.
 * Called on questionView:submitted (after storeUserAnswer populates _userAnswerText).
 */
function storeReflectiveText(view) {
  const model = view.model;
  const componentType = model.get('_component');
  const componentId = model.get('_id');

  // Check allowlist
  if (!ALLOWED_COMPONENT_TYPES.includes(componentType)) {
    return;
  }

  // Check for multi-item components (only store single-item)
  const items = model.get('_items');
  if (items && items.length > 1) {
    logging.warn(`${LOG_PREFIX} Skipping multi-item ${componentId} (${items.length} items) — not yet supported`);
    return;
  }

  // Get the text from _userAnswerText (set by storeUserAnswer via Phase 1 patch)
  const userAnswerText = model.get('_userAnswerText');
  if (!userAnswerText || !userAnswerText[0] || userAnswerText[0].length === 0) {
    logging.debug(`${LOG_PREFIX} ${componentId}: no text to store`);
    return;
  }

  const text = userAnswerText[0];
  const key = KEY_PREFIX + componentId;

  logging.info(`${LOG_PREFIX} Storing ${componentId}: ${text.length} chars`);

  try {
    offlineStorage.set(key, text);
  } catch (e) {
    logging.error(`${LOG_PREFIX} ${componentId}: offlineStorage.set() threw: ${e.message}`);
    return;
  }

  // Check if the write actually succeeded by reading the SCORM error code
  const scorm = Adapt.spoor?.scorm;
  if (!scorm) {
    // No spoor — can't verify, but the write was attempted
    logging.debug(`${LOG_PREFIX} ${componentId}: spoor not available, cannot verify write`);
    return;
  }

  const writeResult = checkScormResult(scorm);

  if (writeResult.success) {
    logging.info(`${LOG_PREFIX} ${componentId}: stored successfully`);

    // Force explicit commit to persist immediately — reflective text is high-value
    // learner-authored data and shouldn't wait on a general commit mechanism.
    // Cost: ~6 commits per course run (one per reflective textInput).
    forceCommit(scorm, componentId);
  } else {
    // CRITICAL: The write failed. The entire suspend_data blob was rejected.
    // The learner may see a browser error dialog.
    logging.error(`${LOG_PREFIX} ${componentId}: WRITE FAILED — SCORM error code: ${writeResult.errorCode}`);
    logging.error(`${LOG_PREFIX} The LMS rejected the suspend_data write. The learner's reflective text was NOT saved.`);
    logging.error(`${LOG_PREFIX} Likely cause: suspend_data exceeded LMS size limit. Text length: ${text.length} chars.`);
  }
}

// Hook into adapt:start (fires before adapt:initialize / restoreUserAnswers)
Adapt.on('adapt:start', restoreReflectiveText);

// Hook into questionView:submitted (fires after storeUserAnswer)
Adapt.on('questionView:submitted', storeReflectiveText);
