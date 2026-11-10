/**
 * adapt-grow-expanding-links
 *
 * A formative learning-sequence stepper whose step buttons are expanding
 * icon-links. Each step button shows an icon at rest and expands its short
 * label on hover, keyboard focus and for the current step (aria-current="step").
 * Only the current step's activity is shown after mount; Back and Next navigate.
 *
 * Matured from the self-contained study at
 * abbott/assets/components/expanding-links/ (expanding-links.css,
 * learning-sequence.css, learning-sequence.js, learning.template.html).
 *
 * Extends ComponentModel, NOT QuestionModel, so it stays entirely outside the
 * scoring machinery. Completion, when enabled, is an explicit learner action,
 * never a score and never a cmi.interactions write.
 */

import components from 'core/js/components';
import ExpandingLinksView from './ExpandingLinksView';
import ExpandingLinksModel from './ExpandingLinksModel';

export default components.register('growExpandingLinks', {
  view: ExpandingLinksView,
  model: ExpandingLinksModel
});
