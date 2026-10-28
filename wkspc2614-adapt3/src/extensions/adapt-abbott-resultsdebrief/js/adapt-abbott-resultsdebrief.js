/**
 * adapt-abbott-resultsdebrief
 *
 * Consolidated post-assessment debrief. After assessment completion,
 * renders:
 * - a full, ordered results list covering every question in the
 *   assessment, each marked correct or incorrect (SVP-1, 21 Sep 2026:
 *   the debrief previously filtered to `_isCorrect === false` only, so a
 *   learner never saw which questions they got right);
 * - a study plan showing which lessons to revisit, built from the
 *   incorrect questions only and deduplicated by lesson (each lesson
 *   appears once with its topics gathered).
 *
 * Correctness marks follow SEL-1's convention: a tick for correct and a
 * cross for incorrect, each carrying its own screen-reader text, so
 * nothing depends on seeing a shape or a colour.
 *
 * - During attempt: no debrief shown
 * - After submission (pass or fail): results list always shown; study
 *   plan shown additionally if any answers wrong
 * - On pass additionally: passRevealNote shown (ties to adapt-abbott-passreveal)
 *
 * Configuration (course.json):
 *   "_resultsDebrief": {
 *     "_isEnabled": true,
 *     "_assessmentId": "SUMM-a-01",
 *     "_studyPlanHeading": "Where to focus next",
 *     "_passRevealNote": "You can now view the correct answers on the questions above.",
 *     "_items": [
 *       { "_questionId": "SUMM-c-10", "topic": "identifying the steer", "lessonTitle": "Understanding the task" },
 *       ...
 *     ]
 *   }
 *
 * Events listened:
 *   - assessments:complete: fired when an assessment attempt completes
 *   - assessment:restored: fired when assessment state is restored from SCORM
 *   - componentView:postRender: fired when a component view finishes rendering
 *
 * @author Abbott
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';

const LOG_PREFIX = '[resultsdebrief]';
const DEBRIEF_CLASS = 'resultsdebrief';
const DEBRIEF_SELECTOR = `.${DEBRIEF_CLASS}`;

/**
 * Store completed assessment debrief HTML.
 * Keyed by assessment ID. Entries persist for re-renders.
 */
const completedAssessments = new Map();

/**
 * Get the results-debrief configuration from course.json.
 * Returns null if the extension is disabled or not configured.
 */
function getConfig() {
  const course = Adapt.course;
  if (!course) return null;

  const config = course.get('_resultsDebrief');
  if (!config) return null;
  if (!config._isEnabled) return null;

  return config;
}

/**
 * Check if the given assessment ID matches the configured target.
 */
function isAssessmentTargeted(config, assessmentId) {
  if (!config._assessmentId) return false;
  return config._assessmentId === assessmentId;
}

/**
 * Build the question-to-mapping lookup from config._items.
 * Returns a Map keyed by question ID.
 */
function buildQuestionMap(config) {
  const map = new Map();
  if (!config._items || !Array.isArray(config._items)) return map;

  config._items.forEach(item => {
    if (item._questionId) {
      map.set(item._questionId, {
        topic: item.topic || '',
        lessonTitle: item.lessonTitle || ''
      });
    }
  });

  return map;
}

/**
 * Group incorrect questions by lesson, deduplicating.
 * Returns an array of { lessonTitle, topics: [] }.
 */
function groupByLesson(incorrectQuestions, questionMap) {
  const lessonMap = new Map();

  incorrectQuestions.forEach(qId => {
    const mapping = questionMap.get(qId);
    if (!mapping || !mapping.lessonTitle) return;

    const { lessonTitle, topic } = mapping;

    if (!lessonMap.has(lessonTitle)) {
      lessonMap.set(lessonTitle, { lessonTitle, topics: [] });
    }

    if (topic && !lessonMap.get(lessonTitle).topics.includes(topic)) {
      lessonMap.get(lessonTitle).topics.push(topic);
    }
  });

  // Return as array, sorted by lesson title for consistency
  return Array.from(lessonMap.values()).sort((a, b) =>
    a.lessonTitle.localeCompare(b.lessonTitle)
  );
}

/**
 * Build a per-question results list, in assessment order (SVP-1).
 * Unlike groupByLesson, every question is included, not just the
 * incorrect ones, so a screen-reader user gets a complete, ordered
 * account of the whole attempt rather than only the wrong answers.
 * Returns an array of { id, isCorrect, topic, lessonTitle }.
 */
function buildQuestionResults(questions, questionMap) {
  return questions.map((q, index) => {
    const mapping = questionMap.get(q._id) || {};
    return {
      id: q._id,
      index,
      isCorrect: q._isCorrect === true,
      topic: mapping.topic || '',
      lessonTitle: mapping.lessonTitle || ''
    };
  });
}

/**
 * Generate the results-list HTML: every question, in order, each marked
 * correct or incorrect with SEL-1's tick/cross convention. The icon is
 * aria-hidden and paired with visually-hidden text, so correctness is
 * never conveyed by shape or colour alone.
 */
function generateResultsListHtml(questionResults) {
  if (questionResults.length === 0) return '';

  const parts = [];
  parts.push(`<section class="${DEBRIEF_CLASS}__results" role="region" aria-label="Your answers" tabindex="-1">`);
  parts.push(`<h3 class="${DEBRIEF_CLASS}__results-heading">Your answers</h3>`);
  parts.push(`<ol class="${DEBRIEF_CLASS}__results-list">`);

  questionResults.forEach(result => {
    const stateClass = result.isCorrect ? 'is-correct' : 'is-incorrect';
    const stateText = result.isCorrect ? 'Correct' : 'Incorrect';
    const label = (result.topic || result.lessonTitle)
      ? [result.topic, result.lessonTitle].filter(Boolean).join(' — ')
      : `Question ${result.index + 1}`;

    parts.push(`<li class="${DEBRIEF_CLASS}__results-item ${stateClass}">`);
    parts.push(`<span class="${DEBRIEF_CLASS}__results-icon ${DEBRIEF_CLASS}__results-icon--correct" aria-hidden="true"><span class="icon"></span></span>`);
    parts.push(`<span class="${DEBRIEF_CLASS}__results-icon ${DEBRIEF_CLASS}__results-icon--incorrect" aria-hidden="true"><span class="icon"></span></span>`);
    parts.push(`<span class="visually-hidden">${stateText}. </span>`);
    parts.push(`<span class="${DEBRIEF_CLASS}__results-text">${label}</span>`);
    parts.push('</li>');
  });

  parts.push('</ol>');
  parts.push('</section>');

  return parts.join('');
}

/**
 * Generate the debrief HTML.
 */
function generateDebriefHtml(config, lessonGroups, isPass, questionResults) {
  const parts = [];

  // Results list (SVP-1): every question, in order, shown regardless of
  // correctness.
  parts.push(generateResultsListHtml(questionResults));

  // Study plan section (shown if any lessons to revisit)
  if (lessonGroups.length > 0) {
    const heading = config._studyPlanHeading || 'Where to focus next';
    parts.push(`<section class="${DEBRIEF_CLASS}" role="region" aria-label="${heading}" tabindex="-1">`);
    parts.push(`<h3 class="${DEBRIEF_CLASS}__heading">${heading}</h3>`);
    parts.push(`<ul class="${DEBRIEF_CLASS}__list">`);

    lessonGroups.forEach(group => {
      const topicsText = group.topics.length > 0
        ? `: ${group.topics.join(', ')}`
        : '';
      parts.push(`<li class="${DEBRIEF_CLASS}__item"><strong>${group.lessonTitle}</strong>${topicsText}</li>`);
    });

    parts.push('</ul>');
    parts.push('</section>');
  }

  // Pass reveal note (shown only on pass, regardless of whether study plan shown)
  if (isPass && config._passRevealNote) {
    parts.push(`<p class="${DEBRIEF_CLASS}__pass-note">${config._passRevealNote}</p>`);
  }

  return parts.join('');
}

/**
 * Inject the debrief HTML into the DOM after the assessmentResults body.
 * Idempotent: removes any existing debrief within the target component before injecting.
 */
function injectDebrief(assessmentId, html) {
  // Find the assessmentResults component targeting this assessment
  const resultsComponent = Adapt.components.findWhere({
    _component: 'assessmentResults',
    _assessmentId: assessmentId
  });

  if (!resultsComponent) {
    logging.warn(`${LOG_PREFIX} Could not find assessmentResults component for '${assessmentId}'`);
    return false;
  }

  const componentId = resultsComponent.get('_id');
  const $component = $(`.${componentId}`);

  if ($component.length === 0) {
    logging.debug(`${LOG_PREFIX} assessmentResults component not in DOM yet for '${assessmentId}'`);
    return false;
  }

  // Find the body-inner element to inject after
  const $bodyInner = $component.find('.component__body-inner');
  if ($bodyInner.length === 0) {
    logging.warn(`${LOG_PREFIX} Could not find .component__body-inner in assessmentResults`);
    return false;
  }

  // Remove any existing debrief within this component (idempotent)
  $component.find(DEBRIEF_SELECTOR).remove();

  // Inject the new debrief after the body-inner
  if (html) {
    $bodyInner.after(html);
    logging.info(`${LOG_PREFIX} Debrief injected for assessment '${assessmentId}'`);

    // Announce to screen readers
    const $debrief = $component.find(DEBRIEF_SELECTOR);
    if ($debrief.length > 0) {
      // Small delay to ensure DOM is ready, then focus for announcement
      setTimeout(() => {
        $debrief.first().trigger('focus');
      }, 100);
    }
  }

  return true;
}

/**
 * Handle assessment completion or restoration.
 * Stores debrief HTML and attempts immediate injection.
 */
function handleAssessmentState(state) {
  // Guard 1: Extension enabled
  const config = getConfig();
  if (!config) return;

  // Guard 2: Assessment ID match
  const assessmentId = state.id;
  if (!isAssessmentTargeted(config, assessmentId)) {
    logging.debug(`${LOG_PREFIX} Assessment '${assessmentId}' not targeted, skipping`);
    return;
  }

  // Guard 3: Assessment must be complete (not in progress)
  if (!state.isComplete) {
    logging.debug(`${LOG_PREFIX} Assessment '${assessmentId}' not complete, skipping debrief`);
    return;
  }

  // Get per-question results
  const questions = state.questions || [];
  const incorrectQuestions = questions
    .filter(q => q._isCorrect === false)
    .map(q => q._id);

  logging.debug(`${LOG_PREFIX} Assessment '${assessmentId}': ${incorrectQuestions.length} incorrect questions`);

  // Build lesson groups (study plan: incorrect only) and the full
  // per-question results list (SVP-1: every question, in order)
  const questionMap = buildQuestionMap(config);
  const lessonGroups = groupByLesson(incorrectQuestions, questionMap);
  const questionResults = buildQuestionResults(questions, questionMap);

  // Generate HTML
  const html = generateDebriefHtml(config, lessonGroups, state.isPass, questionResults);

  // Store in completedAssessments (persists for re-renders)
  completedAssessments.set(assessmentId, html);

  // Try immediate injection (may succeed if component already rendered)
  injectDebrief(assessmentId, html);
}

/**
 * Handle componentView:postRender to inject debrief when assessmentResults renders.
 * Re-injects unconditionally on every render if assessment is completed.
 */
function onComponentPostRender(view) {
  if (!view || !view.model) return;

  const component = view.model.get('_component');
  if (component !== 'assessmentResults') return;

  const assessmentId = view.model.get('_assessmentId');
  if (!assessmentId) return;

  // Check if we have debrief HTML for this assessment
  const html = completedAssessments.get(assessmentId);
  if (!html) {
    logging.debug(`${LOG_PREFIX} No completed assessment data for '${assessmentId}'`);
    return;
  }

  logging.debug(`${LOG_PREFIX} assessmentResults postRender for '${assessmentId}', injecting debrief`);

  // Small delay to ensure DOM is fully ready
  setTimeout(() => {
    injectDebrief(assessmentId, html);
  }, 50);
}

/**
 * Handler for assessments:complete event.
 */
function onAssessmentsComplete(state) {
  handleAssessmentState(state);
}

/**
 * Handler for assessment:restored event.
 */
function onAssessmentRestored(state) {
  handleAssessmentState(state);
}

// Register event listeners
Adapt.on('assessments:complete', onAssessmentsComplete);
Adapt.on('assessment:restored', onAssessmentRestored);
Adapt.on('componentView:postRender', onComponentPostRender);

logging.debug(`${LOG_PREFIX} Extension loaded`);
