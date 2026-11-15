/**
 * TabsView
 *
 * View for the tabs component. Extends ComponentView.
 *
 * Accessibility model (TC-4):
 * - Tablist container with role="tablist"
 * - Each tab button with role="tab", aria-selected, aria-controls
 * - Roving tabindex: active tab has tabindex="0", others have tabindex="-1"
 * - Tab panels with role="tabpanel", aria-labelledby
 * - Automatic activation: focus moves to tab and activates it immediately
 * - Keyboard: Left/Right/Home/End navigate between tabs with wraparound
 * - aria-orientation switches horizontal/vertical at breakpoint (TA-5)
 *
 * Design refs: TC-4 (view/template), TC-5 (responsive), TC-6 (keyboard)
 */

import ComponentView from 'core/js/views/componentView';

// Breakpoint for vertical layout (must match @device-width-medium in LESS)
const VERTICAL_BREAKPOINT = '60rem';

class TabsView extends ComponentView {

  events() {
    return {
      'click .grow-tabs__tab': 'onTabClick',
      'keydown .grow-tabs__tab': 'onTabKeydown'
    };
  }

  preRender() {
    // Listen for active index changes to re-render
    this.listenTo(this.model, 'change:_activeIndex', this.onActiveIndexChange);

    // Bind the orientation handler so we can add/remove it
    this._onOrientationChange = this._onOrientationChange.bind(this);
  }

  postRender() {
    // Wait for panel images to load before marking ready
    if (this.model.hasAnyGraphics()) {
      this.$('.grow-tabs__panels').imageready(this.setReadyStatus.bind(this));
    } else {
      // No images — ready immediately
      this.setReadyStatus();
    }

    // Set up inview completion (component visible = counts toward page completion)
    this.setupInviewCompletion('.component__widget');

    // Set up aria-orientation listener (TA-5)
    this._setupOrientationListener();
  }

  /**
   * Set up matchMedia listener for aria-orientation switching.
   * Updates aria-orientation="vertical" when viewport is narrow.
   */
  _setupOrientationListener() {
    // Create media query matching the LESS breakpoint
    this._orientationQuery = window.matchMedia(`(max-width: ${VERTICAL_BREAKPOINT})`);

    // Set initial orientation
    this._updateOrientation(this._orientationQuery.matches);

    // Listen for changes
    this._orientationQuery.addEventListener('change', this._onOrientationChange);
  }

  /**
   * Handle orientation media query change.
   * @param {MediaQueryListEvent} event
   */
  _onOrientationChange(event) {
    this._updateOrientation(event.matches);
  }

  /**
   * Update aria-orientation on the tablist element.
   * @param {boolean} isVertical - true if narrow viewport (vertical layout)
   */
  _updateOrientation(isVertical) {
    const $tablist = this.$('.grow-tabs__tablist');
    if ($tablist.length) {
      $tablist.attr('aria-orientation', isVertical ? 'vertical' : 'horizontal');
    }
  }

  /**
   * Clean up on remove.
   */
  remove() {
    // Remove orientation listener
    if (this._orientationQuery) {
      this._orientationQuery.removeEventListener('change', this._onOrientationChange);
      this._orientationQuery = null;
    }
    return super.remove();
  }

  /**
   * Handle tab click — select tab via model.
   * @param {Event} event
   */
  onTabClick(event) {
    const $tab = this.$(event.currentTarget);
    const index = parseInt($tab.data('index'), 10);

    if (isNaN(index)) return;
    if (!this.model.get('_isEnabled')) return;

    this.model.selectTab(index);
  }

  /**
   * Handle keyboard navigation on tabs.
   * @param {Event} event
   */
  onTabKeydown(event) {
    if (!this.model.get('_isEnabled')) return;

    const newIndex = this.model.handleKeyNavigation(event.key);

    if (newIndex !== null) {
      event.preventDefault();
      // Focus the newly active tab
      this.focusTab(newIndex);
    }
  }

  /**
   * Focus a tab button by index.
   * @param {number} index
   */
  focusTab(index) {
    const $tabs = this.$('.grow-tabs__tab');
    const $tab = $tabs.eq(index);
    if ($tab.length) {
      $tab.focus();
    }
  }

  /**
   * Re-render when active index changes.
   */
  onActiveIndexChange() {
    this.changed();
    // Re-apply orientation after re-render (template doesn't set it)
    if (this._orientationQuery) {
      this._updateOrientation(this._orientationQuery.matches);
    }
  }

}

TabsView.template = 'growTabs.jsx';

export default TabsView;
