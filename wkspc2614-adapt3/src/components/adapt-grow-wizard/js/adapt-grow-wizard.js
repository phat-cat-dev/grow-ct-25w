/**
 * adapt-grow-wizard
 *
 * Step wizard: a guided multi-step flow with a progress bar. An ordered array of
 * authorable steps, each with a short label and a panel body (HTML). The progress
 * width and the active label are computed from the current step; Back and Next
 * move through the steps, clamped at the ends.
 *
 * Formative only. Extends ComponentModel (NOT QuestionModel) so it stays outside
 * the scoring machinery entirely: no interactions, no marking, no score. It
 * optionally completes when the learner reaches the final step (the opentext-style
 * _isCompletionBearing flag); otherwise it is presentational and completes on view.
 *
 * Matured from the "Step wizard" gallery pattern (abbott/assets/gallery/patterns-3.html).
 */

import components from 'core/js/components';
import WizardView from './WizardView';
import WizardModel from './WizardModel';

export default components.register('growWizard', {
  view: WizardView,
  model: WizardModel
});
