# Open Text  (`opentext`)

- plugin: `adapt-abbott-opentext` (component)
- targetAttribute: `_opentext`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Open text input. Write your response in |   |
| `counterText` | string | yes | "{{count}} of {{max}} characters" |  Character counter format. Placeholders: {{count}}, {{max}}. |
| `statusNormal` | string | yes | "Your writing saves automatically." |  Status line shown during normal operation. |
| `statusFailed` | string | yes | "Your writing could not be saved. Please |  Status line shown when a save fails. |
| `overLimitText` | string | yes | "You're {{over}} characters over the lim |  Warning shown when character limit exceeded. Placeholder: {{over}}. |
| `remainingAnnouncement` | string | yes | "{{remaining}} characters remaining." |  Screen reader announcement when approaching limit. Placeholder: {{remaining}}. |
| `completionButton` | string | yes | "Mark as complete" |  Label for the completion button (reflection variant only). |
| `completedState` | string | yes | "Completed" |  Static text shown after marking complete. |
| `belowMinimumMessage` | string | yes | "Please write a little more before marki |  Message announced when pressing complete with insufficient text. |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" | Instruction Optional guidance text displayed above the text area. |
| `_variant` | string enum: reflection, notes |  | "reflection" | Variant Purpose of this component. 'reflection' for reflective prompts (may be completion-bearing); 'notes' for general note-taking (never completion-bearing). |
| `placeholder` | string |  | "" | Placeholder text Empty-state text shown when the learner has not typed anything. If blank, uses variant default: 'Write your reflection here...' or 'Make your notes here...' |
| `_maxCharacters` | number |  | 4000 | Maximum characters Soft character limit. Learner can type beyond this but cannot mark complete until under. Do not raise without checking suspend_data budget. |
| `_minCharacters` | number |  | 0 | Minimum characters Minimum characters required before the learner can mark as complete. Only applies when _isCompletionBearing is true. |
| `_isCompletionBearing` | boolean |  | false | Is completion bearing Reflection variant only. Has no effect when _variant is 'notes'. When true, displays a 'Mark as complete' button and contributes to lesson completion. |
| `_rows` | number |  | 8 | Initial rows Initial height of the text area in rows. The area auto-grows as the learner types. |
| `_maxRows` | number |  | 20 | Maximum rows Maximum height before scrolling. The text area stops growing and scrolls internally beyond this. |

## JSX template(s)

**opentext.jsx**

```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * OpenText component template.
 *
 * Stage 3: auto-grow, counter, status line.
 * Stage 4: completion button and state.
 * - Textarea defaultValue set from model (restored at adapt:start)
 * - Counter visible when approaching/over limit (view controls visibility)
 * - Over-limit message shown when exceeded (view controls visibility)
 * - Status line updated by view on save success/failure
 * - Completion button shown for reflection variant when _isCompletionBearing
 * - All learner-facing strings from schema globals (spec §10)
 *
 * Accessibility (spec §9):
 * - Body rendered with ID, referenced by aria-labelledby on textarea
 * - Counter is aria-hidden (not announced on keystrokes)
 * - Status line referenced by aria-describedby
 * - Live regions: polite for thresholds, alert for failures
 * - Completion announced via live region
 */
export default function OpenText(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _variant,
    _rows,
    _globals,
    _shouldShowCompletionButton,
    displayTitle,
    body,
    instruction,
    _resolvedPlaceholder,
    _initialText
  } = props;

  // Get strings from globals (single source of truth, no fallback)
  const statusNormal = _globals?.statusNormal;
  const completionButtonText = _globals?.completionButton;
  const completedStateText = _globals?.completedState;
  const ariaRegion = _globals?.ariaRegion;

  // Variant and rows come from model defaults (spec §2)
  const variant = _variant || 'reflection';
  const rows = _rows || 8;

  // Label configuration (spec §9.1): fallback chain for accessible name
  // body → instruction → displayTitle → ariaRegion
  // All use aria-labelledby pointing to a rendered element with ID
  const hasBody = Boolean(body);
  const labelId = hasBody ? `${_id}-body` : `${_id}-label`;

  // Strip HTML tags from fallback content — instruction/displayTitle may contain
  // block-level HTML which could cause screen readers to run text together
  const stripTags = (html) => {
    if (!html) return '';
    return html
      .replace(/<\/(p|div|li|h[1-6])>/gi, ' ')  // Space after block closers
      .replace(/<[^>]*>/g, '')                   // Strip all tags
      .replace(/\s+/g, ' ')                      // Normalize whitespace
      .trim();
  };
  const fallbackLabelText = stripTags(instruction) || stripTags(displayTitle) || ariaRegion || '';

  // Render header without body — body renders separately for aria-labelledby
  const headerProps = { ...props, body: null };

  return (
    <div className="component__inner opentext__inner">

      {/* Header renders displayTitle and instruction; body excluded */}
      <templates.header {...headerProps} />

      {/* Body rendered separately with ID for aria-labelledby (spec §9.1) */}
      {body &&
        <div className="opentext__body">
          <div
            id={`${_id}-body`}
            className="opentext__body-inner"
            dangerouslySetInnerHTML={{ __html: compile(body, props) }}
          />
        </div>
      }

      {/* Fallback label when no body — visually hidden, provides accessible name (spec §9.1) */}
      {/* Chain: instruction → displayTitle → ariaRegion (tags stripped for clean SR output) */}
      {!body &&
        <div
          id={`${_id}-label`}
          className="opentext__label--hidden"
        >
          {fallbackLabelText}
        </div>
      }

      <div
        className={classes([
          'component__widget opentext__widget',
          !_isEnabled && 'is-disabled',
          _isComplete && 'is-complete',
          `is-variant-${variant}`
        ])}
      >

        {/* Textarea with auto-grow (view handles resizing) */}
        <div className="opentext__textarea-container">
          <textarea
            id={`${_id}-textarea`}
            className="opentext__textarea"
            rows={rows}
            placeholder={_resolvedPlaceholder}
            disabled={!_isEnabled}
            defaultValue={_initialText || ''}
            aria-labelledby={labelId}
            aria-describedby={`${_id}-status`}
          />
        </div>

        {/* Character counter — hidden until approaching limit (spec §8) */}
        {/* aria-hidden: must not be announced on every keystroke (spec §9.1) */}
        <div
          className="opentext__counter u-display-none"
          aria-hidden="true"
        >
          {/* Content and visibility controlled by view */}
        </div>

        {/* Over-limit warning — hidden until limit exceeded (spec §8, §10) */}
        <div className="opentext__over-limit u-display-none">
          {/* Content and visibility controlled by view */}
        </div>

        {/* Completion UI — only for reflection variant with _isCompletionBearing (spec §7) */}
        {_shouldShowCompletionButton &&
          <div className="opentext__completion">
            {/* Button — hidden when complete, shown otherwise */}
            <button
              type="button"
              className={classes([
                'btn-text opentext__complete-btn',
                _isComplete && 'u-display-none'
              ])}
            >
              {completionButtonText}
            </button>
            {/* Completed state — hidden until complete, receives focus (spec §9.5) */}
            <div
              className={classes([
                'opentext__completed-state',
                !_isComplete && 'u-display-none'
              ])}
              tabIndex="-1"
            >
              {completedStateText}
            </div>
          </div>
        }

        {/* Status line — updated by view on save success/failure (spec §9.3) */}
        {/* Default text from schema globals (spec §10) */}
        <div
          id={`${_id}-status`}
          className="opentext__status"
        >
          {statusNormal}
        </div>

        {/* Live region for routine announcements: thresholds, completion (spec §9.2) */}
        <div
          className="opentext__live-region"
          aria-live="polite"
          aria-atomic="true"
        >
          {/* Announcements injected by view */}
        </div>

        {/* Alert region for write failures — assertive (spec §9.3) */}
        <div
          className="opentext__alert"
          role="alert"
          aria-atomic="true"
        >
          {/* Failure message injected by view when write fails */}
        </div>

      </div>

    </div>
  );
}
```

## Live example (from this course)

```json
{
  "_id": "L01-c-45",
  "_parentId": "L01-b-45",
  "_type": "component",
  "_component": "opentext",
  "_classes": "",
  "_layout": "full",
  "title": "Reflective prompt",
  "displayTitle": "",
  "body": "<p>Where do you sit in your subject's discourse community right now, and what would moving toward its centre look like for you?</p>",
  "instruction": "Write a few sentences for yourself. This is not marked, and the questions have no right answers.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  },
  "_variant": "reflection",
  "_isOptional": true
}
```

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
