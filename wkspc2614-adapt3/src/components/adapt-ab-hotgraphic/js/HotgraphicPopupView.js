import Adapt from 'core/js/adapt';
import React from 'react';
import ReactDOM from 'react-dom';
import { templates } from 'core/js/reactHelpers';

/**
 * HotgraphicPopupView
 *
 * Deliberately NOT an AdaptView - mirrors adapt-contrib-hotgraphic's popup
 * shape (a plain Backbone.View that hand-renders its own React template via
 * ReactDOM.render, triggered off `notify:opened`). Shows only the item that
 * was just activated - no pagination through the other hotspots - so it
 * never needs `_globals._components._hotgraphic` (the back/next pagination
 * labels the stock popup reads: that key belongs to adapt-contrib-hotgraphic
 * and would be undefined here).
 */
class HotgraphicPopupView extends Backbone.View {

  className() {
    return 'ab-hotgraphic-popup';
  }

  initialize() {
    this.onCloseClick = this.onCloseClick.bind(this);
    this.listenToOnce(Adapt, 'notify:opened', this.render.bind(this));
  }

  onCloseClick() {
    Adapt.trigger('notify:close');
  }

  render() {
    const activeItem = this.model.getActiveItem();
    ReactDOM.render(
      <templates.abHotgraphicPopup
        item={activeItem ? activeItem.toJSON() : null}
        onCloseClick={this.onCloseClick}
      />,
      this.el
    );
    return this;
  }

}

export default HotgraphicPopupView;
