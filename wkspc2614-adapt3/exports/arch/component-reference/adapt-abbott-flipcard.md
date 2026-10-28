# Flip Card  (`flipcard`)

- plugin: `adapt-abbott-flipcard` (component)
- targetAttribute: `_flipcard`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Flip cards. Select each card to reveal  |   |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" | Instruction Instruction text displayed below the component body. |
| `_flipBehaviour` | string enum: independent, single |  | "independent" | Flip Behaviour 'independent': cards flip and stay flipped individually. 'single': flipping one card closes any other open card. |
| `_items` | array | yes |  | Cards Each card has a front face and a back face. Front must have at least one of: title, body, or graphic. Back must have at least one of: title or body. |
| `_id` | string |  | "" | Item ID Stable identifier for this card. If blank, index is used. Useful for analytics. |
| `front` | object | yes |  | Front Face The initially visible face of the card. Must have at least one of: title, body, or graphic. |
| `title` | string |  | "" | Front Title Title displayed on the front face. Also used as the card's accessible name. |
| `body` | string |  | "" | Front Body Body text displayed on the front face. |
| `_graphic` | object |  |  | Front Graphic  |
| `src` | string |  | "" | Source Image displayed on the front face. |
| `alt` | string |  | "" | Alternative Text Describes the image for screen readers. Leave blank if the image is decorative and the front title provides sufficient context. |
| `back` | object | yes |  | Back Face The revealed face of the card. Must have at least one of: title or body. |
| `title` | string |  | "" | Back Title Title displayed on the back face. |
| `body` | string |  | "" | Back Body Body text displayed on the back face. |

## JSX template(s)

**flipcard.jsx**

```jsx
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
```

## Live example (from this course)

```json
{
  "_id": "L01-c-25",
  "_parentId": "L01-b-25",
  "_type": "component",
  "_component": "flipcard",
  "_classes": "",
  "_layout": "full",
  "title": "Explore the concept",
  "displayTitle": "The discourse community",
  "body": "Four steps in how you join your subject’s community. Turn each card, in order, to see how you move from the edge towards the centre.",
  "instruction": "Select each card to turn it over. Work through all four.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  },
  "_flipBehaviour": "independent",
  "_items": [
    {
      "front": {
        "title": "Disciplinary community"
      },
      "back": {
        "body": "The people who make, teach and debate knowledge in your subject: researchers, tutors and students. Each subject is its own discourse community, and learning here means finding your place within it. Because knowledge is built between people rather than alone, taking part in that shared work is itself how you learn."
      }
    },
    {
      "front": {
        "title": "Discourse"
      },
      "back": {
        "body": "Knowledge is not static, it develops and accepted understanding evolves. Academic communities propose, test and make new knowledge. A discourse community does this by the questions it asks, what it accepts as good evidence, and how it argues towards agreement. To learn your subject is to learn not only its current understanding of the field but also its debate, discussion and discourse."
      }
    },
    {
      "front": {
        "title": "Knowledge"
      },
      "back": {
        "body": "Knowledge is not a fixed set of facts to memorise it is not static. Rather it is the interpretations the community itself debates and refines through the process of discourse. Currently accepted understanding is the knowledge that emerges from ongoing debate, and so it can be added to, it can and does change."
      }
    },
    {
      "front": {
        "title": "You"
      },
      "back": {
        "body": "At first you work with ideas your community has already agreed or is still debating. As you progress, you begin to apply, support and contest those ideas and practices yourself, moving from the edge of your subject towards its centre, and with practice, becoming a contributor to its discourse through your own interpretations and the knowledge you generate."
      }
    }
  ]
}
```

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
