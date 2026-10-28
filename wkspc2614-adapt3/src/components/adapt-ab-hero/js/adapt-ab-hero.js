/**
 * adapt-ab-hero
 *
 * A presentational hero banner component, rendering a single .ab.hero object
 * (eyebrow / title / subtitle / actions, with optional icon or media) via the
 * theme's .ab.hero system (ab-base-hero.less / the brand ab-hero.less, on
 * --ab-hero-* tokens; no Bootstrap dependency).
 *
 * Presentational only: no marking, no response semantics. Completion is by
 * inview (the component becoming visible counts toward page completion).
 *
 * See: docs/adapt-ab-components-sketch.md
 */

import components from 'core/js/components';
import HeroView from './HeroView';
import HeroModel from './HeroModel';

export default components.register('ab-hero', {
  view: HeroView,
  model: HeroModel
});
