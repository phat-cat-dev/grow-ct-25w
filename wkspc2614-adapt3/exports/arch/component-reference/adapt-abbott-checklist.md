# Checklist  (`checklist`)

- plugin: `adapt-abbott-checklist` (component)
- targetAttribute: `_checklist`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Checklist. Work through each item and t |   |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" |  Instruction text for the checklist. |
| `_items` | array | yes |  | Checklist items The checklist items. Each item is a concrete action the learner can tick off. Items should be answerable yes/no without judgement. Provide 4-8 items. |
| `text` | string | yes | "" | Item text A concrete action phrased as a yes/no check. Example: 'Have I checked every in-text citation appears in my reference list?' |

## JSX template(s)

**checklist.jsx**

```jsx
import React from 'react';
import { templates, classes } from 'core/js/reactHelpers';

/**
 * Checklist Template
 *
 * Renders a set of native checkboxes with properly associated labels.
 * Uses fieldset/legend for programmatic grouping.
 *
 * Accessibility: native <input type="checkbox"> with <label> via for/id.
 * IDs derived from component _id for multi-instance safety.
 *
 * Design refs: CL-A (accessibility model), CB-4 (view/template)
 */
export default function Checklist(props) {
  const {
    _id,
    _items,
    instruction,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._checklist?.ariaRegion ||
    'Checklist. Work through each item and tick it when done.';

  const itemCount = (_items || []).length;

  return (
    <div className="component__inner checklist__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget',
          'checklist__widget'
        ])}
        role="region"
        aria-label={ariaRegion}
      >

        {/* Fieldset groups the checkboxes with a programmatic label */}
        <fieldset className="checklist__fieldset">
          {instruction && (
            <legend className="checklist__legend aria-label">
              {instruction}
            </legend>
          )}

          <div className="checklist__items">
            {(_items || []).map((item, index) => {
              // Derive unique IDs from component _id for multi-instance safety
              const inputId = `${_id}-item-${index}`;

              return (
                <div
                  key={index}
                  className={classes([
                    'checklist__item'
                  ])}
                >
                  <input
                    type="checkbox"
                    id={inputId}
                    className="checklist__input js-checklist-input"
                    data-index={index}
                  />
                  <label
                    htmlFor={inputId}
                    className="checklist__label"
                  >
                    <span className="checklist__indicator" aria-hidden="true"></span>
                    <span className="checklist__text">{item.text}</span>
                  </label>
                </div>
              );
            })}
          </div>

        </fieldset>

        {/* Neutral progress count (CL-6: no evaluative copy) */}
        <div
          className="checklist__progress"
          aria-live="polite"
          aria-atomic="true"
        >
          <span className="checklist__progress-text js-checklist-progress">
            0 of {itemCount} checked
          </span>
        </div>

      </div>

    </div>
  );
}
```

## Live example (from this course)

```json
{
  "_id": "L05-c-35",
  "_parentId": "L05-b-35",
  "_type": "component",
  "_component": "checklist",
  "_classes": "",
  "_layout": "full",
  "title": "Working with the cycle",
  "displayTitle": "How to do it",
  "body": "Use these to keep the cycle turning in your own studies, rather than treating each module as a fresh start.",
  "instruction": "Tick each item when you have done it.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  },
  "_items": [
    {
      "text": "When a module begins, have I looked back at feedback from a related one?"
    },
    {
      "text": "Am I clear what each assessment is actually asking me to show?"
    },
    {
      "text": "When feedback arrives, have I read all of it, not just the mark?"
    },
    {
      "text": "Have I turned that feedback into one or two things to carry into my next piece of work?"
    },
    {
      "text": "Do I treat each piece of work as the start of the next round, rather than the end of this one?"
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
