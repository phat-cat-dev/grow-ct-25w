# Timeline  (`timeline`)

- plugin: `adapt-abbott-timeline` (component)
- targetAttribute: `_timeline`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Timeline. Select each stage to reveal i |   |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" | Instruction Instruction text displayed below the component body. |
| `_expandBehaviour` | string enum: single, independent |  | "single" | Expand Behaviour 'single' (default): expanding one stage collapses others, keeping the overview scannable. 'independent': stages expand and stay open individually. |
| `_items` | array | yes |  | Stages Each stage has a label (axis marker), title, optional body, and optional graphic. Label and title are required. |
| `label` | string | yes | "" | Label Axis marker text (e.g. 'Stage 1', 'Week 3', '1'). Displayed on the timeline axis. |
| `title` | string | yes | "" | Title Stage title displayed next to the marker. Combined with label for the accessible name. |
| `body` | string |  | "" | Body Detail content revealed when the stage is expanded. |
| `_graphic` | object |  |  | Graphic  |
| `src` | string |  | "" | Source Image displayed in the expanded detail area. |
| `alt` | string |  | "" | Alternative Text Describes the image for screen readers. Leave blank if decorative. |

## JSX template(s)

**timeline.jsx**

```jsx
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
```

## Live example (from this course)

_No instance of this component in the sampled course._

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
