/**
 * adapt-grow-card
 *
 * A presentational card component (Bootstrap-5-shaped), rendering one or more
 * cards via the theme's .ab.card system (ab-cards.less, on --ab-card-* tokens;
 * no Bootstrap dependency). More than one card renders as a .card-group.
 *
 * Presentational only: no marking, no response semantics. Completion is by
 * inview (the component becoming visible counts toward page completion).
 *
 * See: docs/adapt-ab-components-sketch.md
 */

import components from 'core/js/components';
import CardView from './CardView';
import CardModel from './CardModel';

export default components.register('growCard', {
  view: CardView,
  model: CardModel
});
