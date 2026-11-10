/**
 * adapt-grow-tabs
 *
 * Entry point for the tabs component.
 * Registers the component with Adapt's component factory.
 */

import components from 'core/js/components';
import TabsModel from './TabsModel';
import TabsView from './TabsView';

export default components.register('growTabs', {
  model: TabsModel,
  view: TabsView
});
