# Modal launcher  (`modal`)

- plugin: `adapt-abbott-modal` (component)
- targetAttribute: `_modal`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "both" |   |
| `body` | string |  | "" |  Optional teaser shown on the page, above the trigger button. |
| `_completion` | string enum: trigger, view, none |  | "trigger" | Completion When this component completes: 'trigger' (the learner opens the popup, default), 'view' (scrolls into view) or 'none'. |
| `_trigger` | object | yes |  | Trigger button  |
| `text` | string | yes | "Open" | Button text  |
| `ariaLabel` | string |  | "" | Button aria-label Accessible label for the trigger. Falls back to the button text. |
| `_icon` | string |  | "" | Trigger icon Optional cm icon name (e.g. 'learning', 'assessment') shown on the button. |
| `_popup` | object | yes |  | Popup content  |
| `title` | string |  | "" | Popup title  |
| `body` | string | yes | "" | Popup body The foregrounded content (HTML allowed): the activity, worked example, definition or panel. |
| `_classes` | string |  | "" | Popup classes Extra CSS classes on the popup (cm-notify cm-modal are always applied). |
| `_isCancellable` | boolean |  | true | Cancellable Whether the learner can dismiss the popup with the close control / Esc. |

## JSX template(s)

**modal.jsx**

```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Modal launcher template.
 * Header + optional teaser body + a .cm.btn trigger. The trigger opens the
 * authored _popup content in the Adapt notify popup (themed by cm-notify.less).
 */
export default function Modal(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    body,
    _trigger
  } = props;

  const triggerText = _trigger?.text || 'Open';
  const triggerAria = _trigger?.ariaLabel || triggerText;
  const triggerIcon = _trigger?._icon || '';   // optional cm icon name, e.g. "learning"

  return (
    <div className="component__inner modal__inner">

      <templates.header {...props} />

      {body && (
        <div
          className="component__body modal__body"
          dangerouslySetInnerHTML={{ __html: compile(body) }}
        />
      )}

      <div className="btn__container modal__btn-container">
        <button
          type="button"
          className={classes([
            'cm btn primary js-modal-trigger',
            _isComplete && 'is-complete'
          ])}
          disabled={_isEnabled === false}
          aria-label={triggerAria}
        >
          {triggerIcon && (
            <span className={`cm icon-${triggerIcon}-svg modal__trigger-icon`} aria-hidden="true" />
          )}
          <span className="modal__trigger-label">{triggerText}</span>
        </button>
      </div>

    </div>
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
