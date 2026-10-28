/**
 * adapt-abbott-pass-reveal
 *
 * Enables model answer display on assessment questions only after the learner
 * passes. Until pass, _canShowModelAnswer stays false on all question
 * components in the targeted assessment(s); on pass, it's set to true.
 *
 * This prevents learners from revealing correct answers before demonstrating
 * competence, while still allowing model-answer review after passing for
 * reflection and consolidation.
 *
 * Configuration (course.json):
 *   "_passReveal": {
 *     "_isEnabled": true,
 *     "_assessmentIds": ["SUMM-a-01"]  // optional; if absent, applies to all
 *   }
 *
 * Events listened:
 *   - assessments:complete: fired when an assessment attempt completes
 *   - assessment:restored: fired when assessment state is restored from SCORM
 *
 * Guard order (per user specification):
 *   1. Extension enabled check (disabled/absent = no-op)
 *   2. Assessment ID match
 *   3. isPass true
 *   4. Set _canShowModelAnswer on question models
 *
 * @author Abbott
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';

const LOG_PREFIX = '[pass-reveal]';

/**
 * Get the pass-reveal configuration from course.json.
 * Returns null if the extension is disabled or not configured.
 */
function getConfig() {
  const course = Adapt.course;
  if (!course) return null;

  const config = course.get('_passReveal');
  if (!config) return null;
  if (!config._isEnabled) return null;

  return config;
}

/**
 * Check if the given assessment ID is targeted by this extension.
 * If no _assessmentIds array is configured, all assessments are targeted.
 */
function isAssessmentTargeted(config, assessmentId) {
  if (!config._assessmentIds || config._assessmentIds.length === 0) {
    return true; // No filter = all assessments
  }
  return config._assessmentIds.includes(assessmentId);
}

/**
 * Get question components for a given assessment.
 * Uses the assessment model's internal method to find descendant questions.
 */
function getAssessmentQuestions(assessmentId) {
  if (!Adapt.assessment) return [];

  const assessmentModel = Adapt.assessment.get(assessmentId);
  if (!assessmentModel) return [];

  // Use the assessment's method to get all question components
  if (typeof assessmentModel._getAllQuestionComponents === 'function') {
    return assessmentModel._getAllQuestionComponents();
  }

  // Fallback: find questions manually via the model's descendants
  if (typeof assessmentModel.findDescendantModels === 'function') {
    return assessmentModel.findDescendantModels('question');
  }

  return [];
}

/**
 * Enable model answers on all questions in the given assessment.
 */
function enableModelAnswers(assessmentId) {
  const questions = getAssessmentQuestions(assessmentId);

  if (questions.length === 0) {
    logging.warn(`${LOG_PREFIX} No questions found for assessment '${assessmentId}'`);
    return;
  }

  let enabledCount = 0;
  questions.forEach(question => {
    const currentValue = question.get('_canShowModelAnswer');
    if (currentValue !== true) {
      question.set('_canShowModelAnswer', true);
      enabledCount++;
      logging.debug(`${LOG_PREFIX} Enabled model answer on ${question.get('_id')}`);
    }
  });

  logging.info(`${LOG_PREFIX} Enabled model answers on ${enabledCount}/${questions.length} questions for assessment '${assessmentId}'`);
}

/**
 * Handle assessment completion or restoration.
 * Applies the guard chain and enables model answers if all guards pass.
 */
function handleAssessmentState(state) {
  // Guard 1: Extension enabled (must be first per specification)
  const config = getConfig();
  if (!config) {
    // Extension disabled or not configured - silent no-op
    return;
  }

  // Guard 2: Assessment ID match
  const assessmentId = state.id;
  if (!isAssessmentTargeted(config, assessmentId)) {
    logging.debug(`${LOG_PREFIX} Assessment '${assessmentId}' not targeted, skipping`);
    return;
  }

  // Guard 3: isPass true
  if (!state.isPass) {
    logging.debug(`${LOG_PREFIX} Assessment '${assessmentId}' not passed (isPass=${state.isPass}), model answers remain hidden`);
    return;
  }

  // All guards passed - enable model answers
  logging.info(`${LOG_PREFIX} Assessment '${assessmentId}' passed, enabling model answers`);
  enableModelAnswers(assessmentId);
}

/**
 * Handler for assessments:complete event.
 * Fired when an assessment attempt completes (pass or fail).
 */
function onAssessmentsComplete(state) {
  handleAssessmentState(state);
}

/**
 * Handler for assessment:restored event.
 * Fired when assessment state is restored from SCORM on revisit.
 */
function onAssessmentRestored(state) {
  handleAssessmentState(state);
}

// Register event listeners
Adapt.on('assessments:complete', onAssessmentsComplete);
Adapt.on('assessment:restored', onAssessmentRestored);

logging.debug(`${LOG_PREFIX} Extension loaded`);
