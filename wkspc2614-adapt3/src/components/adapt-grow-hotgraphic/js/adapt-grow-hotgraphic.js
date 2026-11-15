/**
 * adapt-grow-hotgraphic
 *
 * A reusable inline-SVG hotspot component. Fetches and inlines an authored
 * SVG diagram, resolves each item's `_hotspot` to a node in it, and exposes a
 * generated class vocabulary so every future diagram can be painted by the
 * theme without new component code - see js/HotgraphicView.js and
 * js/hotgraphicLogic.js for the interface layer this depends on.
 *
 * Extends ItemsComponentModel for per-hotspot visitation and completion.
 */

import components from 'core/js/components';
import HotgraphicView from './HotgraphicView';
import HotgraphicModel from './HotgraphicModel';

export default components.register('growHotgraphic', {
  view: HotgraphicView,
  model: HotgraphicModel
});
