import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import notify from 'core/js/notify';
import ComponentView from 'core/js/views/componentView';
import HotgraphicPopupView from './HotgraphicPopupView';
import {
  resolveHotspotSelector,
  rewriteIdReference,
  prefixId,
  composeHotspotLabel
} from './hotgraphicLogic';

/**
 * HotgraphicView
 *
 * Fetches and inlines the authored SVG, resolves each item's `_hotspot` to a
 * node in it, applies the generated class vocabulary, and dispatches
 * activation through the authored `_action`. See hotgraphic.jsx for why
 * `.ab-hotgraphic__canvas` must stay childless, and hotgraphicLogic.js for
 * the pure resolve/rewrite/compose functions used below.
 */

// Attribute values that may carry an intra-document `#id` fragment reference
// and so need rewriting when the SVG's ids are namespaced - see
// hotgraphicLogic.rewriteIdReference.
const ID_REF_ATTRIBUTES = [
  'fill', 'stroke', 'marker-start', 'marker-mid', 'marker-end',
  'clip-path', 'mask', 'filter', 'href', 'xlink:href',
  'aria-labelledby', 'aria-describedby', 'for'
];

class HotgraphicView extends ComponentView {

  initialize(...args) {
    super.initialize(...args);
    this._svgEl = null;
    this._isPopupOpen = false;
  }

  events() {
    return {
      'click .js-ab-hotgraphic-hotspot': 'onHotspotClick',
      'keydown .js-ab-hotgraphic-hotspot': 'onHotspotKeydown',
      'click .js-ab-hotgraphic-reveal-close': 'onRevealClose',
      'click .js-ab-hotgraphic-list-item': 'onListItemClick'
    };
  }

  preRender() {
    this.listenTo(this.model.getChildren(), {
      'change:_isVisited': this.onItemVisitedChange,
      'change:_isActive': this.onItemActiveChange
    });
    this.listenTo(this.model, 'change:_revealedIndex', this.onRevealedIndexChange);
  }

  async postRender() {
    if (this.model.get('_setCompletionOn') === 'inview') {
      this.setupInviewCompletion('.component__widget');
    }
    try {
      this._svgEl = await this.loadDiagram();
      this.mountDiagram();
      this.decorate();
      this.applyInitialState();
      this.model.set('_isDiagramReady', true);
    } catch (err) {
      logging.error(`[ab-hotgraphic ${this.model.get('_id')}] ${err.message}`);
      this.$el.addClass('is-diagram-error');
    } finally {
      // Load-bearing: omitting this on a load/decorate failure hangs page-ready.
      this.setReadyStatus();
    }
  }

  changed(...args) {
    super.changed(...args);
    this.mountDiagram();
  }

  // ---- load ----

  async loadDiagram() {
    const diagram = this.model.get('_diagram') || {};
    const src = diagram.src;
    if (!src || typeof src !== 'string' || !/^course\//.test(src)) {
      throw new Error(`_diagram.src must be a relative path under "course/", got "${src}"`);
    }
    const text = await new Promise((resolve, reject) => {
      $.get(src, null, null, 'text')
        .done(resolve)
        .fail(() => reject(new Error(`unable to load "${src}"`)));
    });
    const doc = new DOMParser().parseFromString(text, 'image/svg+xml');
    if (doc.querySelector('parsererror')) {
      throw new Error(`malformed SVG at "${src}"`);
    }
    const svg = document.importNode(doc.documentElement, true);
    this.sanitiseSvg(svg);
    return svg;
  }

  /**
   * Hygiene pass for design-tool accidents, not a security boundary - the SVG
   * is project-authored build input, same trust tier as components.json.
   */
  sanitiseSvg(svg) {
    svg.querySelectorAll('script, foreignObject').forEach(node => node.remove());
    svg.querySelectorAll('*').forEach(node => {
      [...node.attributes].forEach(attr => {
        if (/^on/i.test(attr.name)) node.removeAttribute(attr.name);
      });
      ['href', 'xlink:href'].forEach(hrefAttr => {
        const value = node.getAttribute(hrefAttr);
        if (value && !value.startsWith('#')) node.removeAttribute(hrefAttr);
      });
    });
  }

  // ---- mount ----

  /**
   * Move the live SVG into the childless canvas. Only touches the DOM when
   * the SVG isn't already mounted, so a React re-render never disturbs it.
   */
  mountDiagram() {
    const mount = this.$('.ab-hotgraphic__canvas')[0];
    if (!this._svgEl || !mount || mount.firstElementChild === this._svgEl) return;
    mount.replaceChildren(this._svgEl);
  }

  // ---- decorate (one-time, on the freshly-mounted SVG) ----

  decorate() {
    if (!this._svgEl) return;
    const prefix = this.model.get('_id');
    const slug = this.model.getDiagramSlug();
    this.namespaceIds(this._svgEl, prefix);
    this.$el.addClass(`ab-hotgraphic--${slug}`);
    this._svgEl.classList.add('ab-hotgraphic__svg', `ab-hotgraphic__svg--${slug}`);
    this.decorateRoot();
    this.decorateHotspots();
  }

  /**
   * Prefix every id in the SVG and rewrite every reference to it, so two
   * instances of the same (or different) diagram on one page never collide.
   */
  namespaceIds(svg, prefix) {
    svg.querySelectorAll('[id]').forEach(node => {
      node.setAttribute('id', prefixId(node.getAttribute('id'), prefix));
    });
    svg.querySelectorAll('*').forEach(node => {
      ID_REF_ATTRIBUTES.forEach(attr => {
        const value = node.getAttribute(attr);
        if (value == null) return;
        const rewritten = rewriteIdReference(value, prefix);
        if (rewritten !== value) node.setAttribute(attr, rewritten);
      });
    });
  }

  /**
   * role="img" would prune every descendant (including the hotspot controls)
   * from the accessibility tree - role="group" plus labelledby/describedby
   * pointing at the SVG's own title/desc keeps them reachable.
   */
  decorateRoot() {
    const svg = this._svgEl;
    const titleEl = svg.querySelector('title');
    const descEl = svg.querySelector('desc');
    svg.setAttribute('role', 'group');
    svg.setAttribute('focusable', 'false');
    if (titleEl) svg.setAttribute('aria-labelledby', titleEl.id);
    if (descEl) svg.setAttribute('aria-describedby', descEl.id);
    svg.removeAttribute('aria-label');
  }

  decorateHotspots() {
    const componentId = this.model.get('_id');
    const visitedWord = this.model.get('_globals')?._accessibility?._ariaLabels?.visited || '';
    const items = this.model.getChildren().toJSON();

    items.forEach((item, index) => {
      const hotspot = item._hotspot || {};
      const { node: region, error, triedSelectors } = resolveHotspotSelector(this._svgEl, hotspot);
      if (!region) {
        logging.error(`[ab-hotgraphic ${componentId}] hotspot "${hotspot._id || index}": ${error} (tried: ${triedSelectors.join(', ') || 'none'})`);
        return;
      }

      region.classList.add('ab-hotgraphic__hotspot', `is-hotspot-${hotspot._id || index}`);
      region.setAttribute('data-ab-hotspot-index', index);
      region.setAttribute('data-ab-hotspot-id', hotspot._id || '');
      region.classList.toggle('is-visited', Boolean(item._isVisited));

      // Decorative hotspots (_action: "none") are painted but never made
      // into focusable controls.
      if (hotspot._action === 'none') return;

      const control = region.closest('a') || region;
      control.removeAttribute('href');
      control.removeAttribute('xlink:href');
      control.setAttribute('role', 'button');
      control.setAttribute('tabindex', '0');
      control.classList.add('ab-hotgraphic__control', 'js-ab-hotgraphic-hotspot');
      control.setAttribute('data-ab-hotgraphic-index', index);
      control.setAttribute('aria-label', composeHotspotLabel(item.title, Boolean(item._isVisited), visitedWord));
    });

    this.checkDocumentOrder(componentId);
  }

  /**
   * Asset discipline, not enforcement - a mismatch only warns, since fixing
   * it requires re-authoring the SVG, not this component.
   */
  checkDocumentOrder(componentId) {
    const controls = [...this._svgEl.querySelectorAll('.js-ab-hotgraphic-hotspot')];
    const indices = controls.map(el => Number(el.getAttribute('data-ab-hotgraphic-index')));
    const isAscending = indices.every((value, i) => i === 0 || value >= indices[i - 1]);
    if (isAscending) return;
    logging.warn(`[ab-hotgraphic ${componentId}] SVG document order does not match _items order - tab order will not match reading order`);
  }

  applyInitialState() {
    this.updateAllVisitedClass();
  }

  updateAllVisitedClass() {
    this.$el.toggleClass('is-all-visited', this.model.areAllItemsCompleted());
  }

  // ---- item state -> imperative SVG classes (React never reaches these) ----

  getRegionForItem(index) {
    return this._svgEl?.querySelector(`[data-ab-hotspot-index="${index}"]`) || null;
  }

  getControlForItem(index) {
    return this._svgEl?.querySelector(`[data-ab-hotgraphic-index="${index}"]`) || null;
  }

  onItemVisitedChange(itemModel) {
    const index = itemModel.get('_index');
    const isVisited = Boolean(itemModel.get('_isVisited'));
    const region = this.getRegionForItem(index);
    const control = this.getControlForItem(index);
    if (region) region.classList.toggle('is-visited', isVisited);
    if (control) {
      const visitedWord = this.model.get('_globals')?._accessibility?._ariaLabels?.visited || '';
      control.setAttribute('aria-label', composeHotspotLabel(itemModel.get('title'), isVisited, visitedWord));
    }
    this.updateAllVisitedClass();
  }

  onItemActiveChange(itemModel) {
    const region = this.getRegionForItem(itemModel.get('_index'));
    if (region) region.classList.toggle('is-active', Boolean(itemModel.get('_isActive')));
  }

  onRevealedIndexChange() {
    const revealedIndex = this.model.get('_revealedIndex');
    this.model.getChildren().each(itemModel => {
      const region = this.getRegionForItem(itemModel.get('_index'));
      if (region) region.classList.toggle('is-active', itemModel.get('_index') === revealedIndex);
    });
  }

  // ---- activation ----

  activateItem(index) {
    const item = this.model.getItem(index);
    if (!item) return;
    const hotspot = item.get('_hotspot') || {};
    item.toggleVisited(true);
    switch (hotspot._action) {
      case 'popup':
        item.toggleActive(true);
        this.openPopup();
        break;
      case 'inlineReveal':
        this.model.revealItem(index);
        break;
    }
  }

  onHotspotClick(event) {
    event.preventDefault();
    const index = this.$(event.currentTarget).data('ab-hotgraphic-index');
    this.activateItem(Number(index));
  }

  onHotspotKeydown(event) {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    // Stops Space from scrolling the page - this control has no native activation.
    event.preventDefault();
    const index = this.$(event.currentTarget).data('ab-hotgraphic-index');
    this.activateItem(Number(index));
  }

  onListItemClick(event) {
    const index = this.$(event.currentTarget).data('ab-hotgraphic-index');
    this.activateItem(Number(index));
  }

  onRevealClose() {
    this.model.revealItem(null);
  }

  openPopup() {
    if (this._isPopupOpen) return;
    this._isPopupOpen = true;

    this.popupView = new HotgraphicPopupView({
      model: this.model
    });

    notify.popup({
      _attributes: { 'data-adapt-id': this.model.get('_id') },
      _view: this.popupView,
      _isCancellable: true,
      _showCloseButton: false,
      _classes: `ab-hotgraphic is-component is-ab-hotgraphic ${this.model.get('_classes') || ''}`
    });

    this.listenToOnce(Adapt, {
      'popup:closed': this.onPopupClosed
    });
  }

  onPopupClosed() {
    this.model.getActiveItem()?.toggleActive();
    this._isPopupOpen = false;
  }

  remove() {
    if (this._isPopupOpen) Adapt.trigger('notify:close');
    this._svgEl = null;
    super.remove();
  }

}

HotgraphicView.template = 'ab-hotgraphic.jsx';

export default HotgraphicView;
