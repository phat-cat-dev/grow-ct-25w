import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Timeline component template.
 *
 * Accessibility model (TL-6):
 * - <ol> with <li> per stage — sequence semantics in the list structure
 * - Each stage marker is a native <button>
 * - aria-expanded reflects expand state
 * - Button accessible name = label + title (static, never swapping)
 * - Detail region in flow after button, aria-hidden when collapsed
 * - ariaRegion introduces interaction at component level
 * - Focus doesn't move on expand; native button semantics only
 */
export default function Timeline(props) {
  const {
    _id,
    _isEnabled,
    _items
  } = props;

  const items = _items || [];

  return (
    <div className="component__inner timeline__inner">

      <templates.header {...props} />

      <div className="component__widget timeline__widget">

        <ol className="timeline__stages">
          {items.map((item, index) => (
            <TimelineStage
              key={index}
              item={item}
              index={index}
              componentId={_id}
              isEnabled={_isEnabled}
            />
          ))}
        </ol>

      </div>

    </div>
  );
}

/**
 * Individual timeline stage component.
 */
function TimelineStage({ item, index, componentId, isEnabled }) {
  const label = item.label || '';
  const title = item.title || '';
  const body = item.body || '';
  const graphic = item._graphic || {};
  const isExpanded = !!item._isExpanded;
  const isVisited = !!item._isVisited;

  // Accessible name: label + title
  const accessibleName = `${label}${label && title ? ': ' : ''}${title}`;

  // Has detail content?
  const hasBody = !!body;
  const hasGraphic = !!(graphic.src);
  const hasDetail = hasBody || hasGraphic;

  // Unique ID for the detail region (for aria-controls)
  const detailId = `${componentId}-stage-${index}-detail`;

  return (
    <li
      className={classes([
        'timeline__stage',
        isExpanded && 'is-expanded',
        isVisited && 'is-visited'
      ])}
    >
      {/* Marker button */}
      <button
        type="button"
        className="timeline__marker"
        data-index={index}
        aria-expanded={isExpanded.toString()}
        aria-controls={detailId}
        aria-label={accessibleName}
        disabled={!isEnabled}
      >
        <span className="timeline__marker-dot" aria-hidden="true">
          {label}
        </span>
        <span className="timeline__marker-title">
          {title}
        </span>
      </button>

      {/* Detail region - always in DOM, hidden when collapsed */}
      <div
        id={detailId}
        className={classes([
          'timeline__detail',
          isExpanded && 'is-expanded'
        ])}
        aria-hidden={(!isExpanded).toString()}
      >
        {hasDetail ? (
          <div className="timeline__detail-content">
            {hasGraphic && (
              <div className="timeline__graphic">
                <img
                  src={graphic.src}
                  alt={graphic.alt || ''}
                  className="timeline__image"
                />
              </div>
            )}
            {hasBody && (
              <div
                className="timeline__body"
                dangerouslySetInnerHTML={{ __html: compile(body) }}
              />
            )}
          </div>
        ) : (
          <div className="timeline__detail-content timeline__detail-content--empty">
            {/* No detail content - stage is marker + title only */}
          </div>
        )}
      </div>
    </li>
  );
}
