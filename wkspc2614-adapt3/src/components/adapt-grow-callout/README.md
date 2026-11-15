# adapt-grow-callout

A static, categorised message box (info / warning / tip / example / note / definition).
Ported from congen11's `callout` component.

## Source mapping

| This plugin | congen11 source |
|---|---|
| Schema | `schemas/components/callout.schema.json` (authoritative - the `.njk` renderer reads different, stale field names and was **not** used as a source) |
| BEM classes | `renderers/elesson/components/callout.njk` |
| Colours (`--info/--warning/--tip/--example`) | `themes/cardiff-met/scss/_components.scss` |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `title` | string | No | Optional heading. No terminal punctuation. |
| `body` | HTML string | Yes | Rendered with triple-stash `{{{body}}}` - author plain HTML, not a rich-text block array. |
| `_calloutType` | enum: `info\|warning\|tip\|example\|note\|definition` | Yes | Source schema made this required with **no default**; this port defaults to `info`. |

## Deviations from source

- congen11's enum includes `note` and `definition`, but its SCSS only styled
  `info`/`warning`/`tip`/`example`. This port adds `--note` (purple) and
  `--definition` (grey) LESS variants so every enum value has a visual treatment.
- congen11's `body` field is a rich-text block array
  (`[{type:"paragraph",text:"..."}]`). This port uses a plain HTML string instead,
  per Adapt convention - see the top-level README's "Rich text → HTML" note for how
  to convert source content.

## Adapt v5 (AMD) equivalent

If your target framework is Adapt v5.x rather than v6+, replace
`js/adapt-grow-callout.js` with:

```javascript
define([
  'core/js/adapt',
  'core/js/views/componentView',
  'core/js/models/componentModel'
], function(Adapt, ComponentView, ComponentModel) {

  var CalloutView = ComponentView.extend({});

  Adapt.register('growCallout', {
    view: CalloutView,
    model: ComponentModel
  });

  return CalloutView;

});
```
