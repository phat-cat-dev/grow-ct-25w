/**
 * adapt-grow-callouts
 *
 * A presentational callout (admonition) component, rendering one or more
 * callouts via the theme's .ab.callout system (ab-base-callout.less / the
 * brand grow-callouts.less, on --ab-callout-* tokens; no Bootstrap dependency).
 * More than one callout, or _isGroup, renders as a responsive group.
 *
 * Presentational only: no marking, no response semantics. Completion is by
 * inview (the component becoming visible counts toward page completion).
 *
 * See: docs/adapt-ab-components-sketch.md
 */

import components from 'core/js/components';
import CalloutsView from './CalloutsView';
import CalloutsModel from './CalloutsModel';

export default components.register('growCallouts', {
  view: CalloutsView,
  model: CalloutsModel
});
