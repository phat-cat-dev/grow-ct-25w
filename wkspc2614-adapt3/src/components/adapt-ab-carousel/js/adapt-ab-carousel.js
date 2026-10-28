/**
 * adapt-ab-carousel
 *
 * A Bootstrap-carousel-shaped component: a single-slide viewport with
 * previous/next controls and indicator dots. Auto-rotate is OFF by default
 * (accessibility + reliable completion); _shouldAutoScroll opts in.
 *
 * Extends ItemsComponentModel for per-slide visitation; completion is reached
 * when every slide has been viewed.
 *
 * See: docs/adapt-ab-components-sketch.md
 */

import components from 'core/js/components';
import CarouselView from './CarouselView';
import CarouselModel from './CarouselModel';

export default components.register('ab-carousel', {
  view: CarouselView,
  model: CarouselModel
});
