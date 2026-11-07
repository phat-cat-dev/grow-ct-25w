/**
 * adapt-abbott-pagefeedback
 *
 * An end-of-page self-report component: a two-choice useful/not-useful
 * response plus an optional note.
 *
 * Extends ComponentModel/ComponentView, NOT QuestionModel/ItemsComponentModel
 * — there is no array of items and no correct answer. Persists via
 * offlineStorage custom keys into cmi.suspend_data, not cmi.interactions
 * (avoids the 250-char truncation and false result:incorrect).
 *
 * See: docs/authoring/component-specs/pagefeedback.md
 */

import components from 'core/js/components';
import PagefeedbackView from './PagefeedbackView';
import PagefeedbackModel from './PagefeedbackModel';

export default components.register('pagefeedback', {
  view: PagefeedbackView,
  model: PagefeedbackModel
});
