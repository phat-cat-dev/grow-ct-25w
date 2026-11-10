/*
 * adapt-grow-timeline
 * Static display component - ported from congen11's `grow-timeline` component schema.
 *
 * congen11's authoring contract requires `_items` to always be authored in
 * ascending chronological order, regardless of `_direction` - the renderer is
 * responsible for reversing display order for 'descending'. The source
 * `.njk` renderer never implemented this at all (no reversal logic). This
 * view implements it by computing `_displayItems` before render.
 *
 * See ../README.md for the v5 (AMD) equivalent.
 */
import components from 'core/js/components';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class TimelineView extends ComponentView {

  events() {
    return {
      'click .js-grow-timeline-toggle': 'onToggle'
    };
  }

  // When _reveal is set, each event's description is collapsed until its
  // title button is clicked (independent toggles).
  onToggle(event) {
    const button = event.currentTarget;
    const expanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!expanded));
    const eventEl = button.closest('.grow-timeline__event');
    if (!eventEl) return;
    const description = eventEl.querySelector('.grow-timeline__description');
    if (description) description.setAttribute('aria-hidden', String(expanded));
    eventEl.classList.toggle('is-revealed', !expanded);
  }

  preRender() {
    super.preRender();

    const items = this.model.get('_items') || [];
    const direction = this.model.get('_direction') || 'ascending';
    const displayItems = direction === 'descending' ? [...items].reverse() : items;

    this.model.set('_displayItems', displayItems);
  }

  // ComponentView.postRender() is a no-op, so this static component must
  // signal ready/completion itself or the page never fires
  // contentObjectView:ready and the loading screen never lifts.
  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__inner');
  }

}

TimelineView.template = 'growTimeline.jsx';

export default components.register('growTimeline', {
  view: TimelineView,
  model: ComponentModel
});
