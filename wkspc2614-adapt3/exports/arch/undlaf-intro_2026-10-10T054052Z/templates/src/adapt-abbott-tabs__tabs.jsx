import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Tabs component template.
 *
 * Accessibility model (TC-4):
 * - Tablist container with role="tablist", aria-orientation
 * - Each tab button with role="tab", aria-selected, aria-controls
 * - Roving tabindex: active tab has tabindex="0", others have tabindex="-1"
 * - Tab panels with role="tabpanel", aria-labelledby
 * - Only active panel visible; inactive panels hidden with aria-hidden
 *
 * Design refs: TC-4 (ARIA tabs), TC-5 (responsive orientation)
 */
export default function Tabs(props) {
  const {
    _id,
    _isEnabled,
    _items,
    _activeIndex = 0
  } = props;

  const items = _items || [];
  const activeIndex = _activeIndex;

  return (
    <div className="component__inner tabs__inner">

      <templates.header {...props} />

      <div className="component__widget tabs__widget">

        {/* Tab list - aria-orientation set dynamically by View (TA-5) */}
        <div
          className="tabs__tablist"
          role="tablist"
        >
          {items.map((item, index) => (
            <TabButton
              key={index}
              item={item}
              index={index}
              componentId={_id}
              isActive={index === activeIndex}
              isEnabled={_isEnabled}
            />
          ))}
        </div>

        {/* Tab panels */}
        <div className="tabs__panels">
          {items.map((item, index) => (
            <TabPanel
              key={index}
              item={item}
              index={index}
              componentId={_id}
              isActive={index === activeIndex}
            />
          ))}
        </div>

      </div>

    </div>
  );
}

/**
 * Individual tab button component.
 */
function TabButton({ item, index, componentId, isActive, isEnabled }) {
  const tabTitle = item.tabTitle || `Tab ${index + 1}`;
  const isVisited = !!item._isVisited;

  const tabId = `${componentId}-tab-${index}`;
  const panelId = `${componentId}-panel-${index}`;

  return (
    <button
      type="button"
      id={tabId}
      className={classes([
        'tabs__tab',
        isActive && 'is-active',
        isVisited && 'is-visited'
      ])}
      role="tab"
      aria-selected={isActive.toString()}
      aria-controls={panelId}
      tabIndex={isActive ? 0 : -1}
      data-index={index}
      disabled={!isEnabled}
    >
      {tabTitle}
    </button>
  );
}

/**
 * Individual tab panel component.
 */
function TabPanel({ item, index, componentId, isActive }) {
  const title = item.title || '';
  const body = item.body || '';
  const graphic = item._graphic || {};

  const tabId = `${componentId}-tab-${index}`;
  const panelId = `${componentId}-panel-${index}`;

  const hasTitle = !!title;
  const hasBody = !!body;
  const hasGraphic = !!(graphic.src);

  return (
    <div
      id={panelId}
      className={classes([
        'tabs__panel',
        isActive && 'is-active'
      ])}
      role="tabpanel"
      aria-labelledby={tabId}
      aria-hidden={(!isActive).toString()}
      tabIndex={isActive ? 0 : -1}
    >
      <div className="tabs__panel-content">
        {hasGraphic && (
          <div className="tabs__graphic">
            <img
              src={graphic.src}
              alt={graphic.alt || ''}
              className="tabs__image"
            />
          </div>
        )}
        {hasTitle && (
          <div className="tabs__panel-title">
            {title}
          </div>
        )}
        {hasBody && (
          <div
            className="tabs__panel-body"
            dangerouslySetInnerHTML={{ __html: compile(body) }}
          />
        )}
      </div>
    </div>
  );
}
