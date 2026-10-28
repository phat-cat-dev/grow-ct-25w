import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Flipcard component template.
 *
 * Accessibility model (FB-3):
 * - Each card is a native <button> containing both faces
 * - Both faces always in DOM; non-current face has aria-hidden="true"
 * - aria-expanded reflects flip state
 * - Button accessible name = front title (stable, doesn't swap on flip)
 * - ariaRegion introduces interaction at component level
 * - Focus doesn't move on flip; native button semantics only
 */
export default function Flipcard(props) {
  const {
    _id,
    _isEnabled,
    _items
  } = props;

  const items = _items || [];

  return (
    <div className="component__inner flipcard__inner">

      <templates.header {...props} />

      <div className="component__widget flipcard__widget">

        <div className="flipcard__cards" role="list">
          {items.map((item, index) => (
            <FlipcardCard
              key={item._id || index}
              item={item}
              index={index}
              componentId={_id}
              isEnabled={_isEnabled}
            />
          ))}
        </div>

      </div>

    </div>
  );
}

/**
 * Individual flipcard card component.
 */
function FlipcardCard({ item, index, componentId, isEnabled }) {
  const front = item.front || {};
  const back = item.back || {};
  const isFlipped = !!item._isFlipped;
  const isVisited = !!item._isVisited;
  const variant = item._variant || 'neutral';

  // Accessible name: front title, falling back to "Card N"
  const accessibleName = front.title || `Card ${index + 1}`;

  // Front has content?
  const hasFrontTitle = !!front.title;
  const hasFrontBody = !!front.body;
  const hasFrontGraphic = !!(front._graphic && front._graphic.src);
  const hasFrontContent = hasFrontTitle || hasFrontBody || hasFrontGraphic;

  // Back has content?
  const hasBackTitle = !!back.title;
  const hasBackBody = !!back.body;
  const hasBackContent = hasBackTitle || hasBackBody;

  return (
    <div
      className={classes([
        'flipcard__card-container',
        `flipcard__card-container--${variant}`,
        isFlipped && 'is-flipped',
        isVisited && 'is-visited'
      ])}
      role="listitem"
    >
      <button
        type="button"
        className="flipcard__card"
        data-index={index}
        aria-expanded={isFlipped.toString()}
        aria-label={accessibleName}
        disabled={!isEnabled}
      >
        {/* Inner wrapper for 3D transform */}
        <div className="flipcard__card-inner">

          {/* Front face */}
          <div
            className="flipcard__face flipcard__face--front"
            aria-hidden={isFlipped.toString()}
          >
            {hasFrontContent ? (
              <>
                {hasFrontGraphic && (
                  <div className="flipcard__graphic">
                    <img
                      src={front._graphic.src}
                      alt={front._graphic.alt || ''}
                      className="flipcard__image"
                    />
                  </div>
                )}
                {hasFrontTitle && (
                  <div className="flipcard__title flipcard__title--front">
                    {front.title}
                  </div>
                )}
                {hasFrontBody && (
                  <div
                    className="flipcard__body flipcard__body--front"
                    dangerouslySetInnerHTML={{ __html: compile(front.body) }}
                  />
                )}
              </>
            ) : (
              <div className="flipcard__title flipcard__title--front">
                Card {index + 1}
              </div>
            )}
          </div>

          {/* Back face */}
          <div
            className="flipcard__face flipcard__face--back"
            aria-hidden={(!isFlipped).toString()}
          >
            {hasBackContent ? (
              <>
                {hasBackTitle && (
                  <div className="flipcard__title flipcard__title--back">
                    {back.title}
                  </div>
                )}
                {hasBackBody && (
                  <div
                    className="flipcard__body flipcard__body--back"
                    dangerouslySetInnerHTML={{ __html: compile(back.body) }}
                  />
                )}
              </>
            ) : (
              <div className="flipcard__body flipcard__body--back">
                (No back content)
              </div>
            )}
          </div>

        </div>
      </button>
    </div>
  );
}
