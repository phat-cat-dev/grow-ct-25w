# adapt-grow-timeline

A chronological sequence of 2-12 events, with optional highlighting and a
configurable display direction. Ported from congen11's `grow-timeline` component.

## Source mapping

| This plugin | congen11 source |
|---|---|
| Schema | `schemas/components/grow-timeline.schema.json` (authoritative) |
| BEM classes | `renderers/elesson/components/grow-timeline.njk` |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `title` | plain string | No | Rendered as `h2`. ~10 words or fewer. |
| `_direction` | enum: `ascending\|descending` | No (default `ascending`) | See authoring contract below. |
| `_items` | array, 2-12 items | Yes | Each item: `dateLabel` (free text, required), `title` (required), `body` (HTML), `_highlight` (boolean, default false). |

### Authoring contract

**Always author `_items` in ascending chronological order**, regardless of the
`_direction` setting. `TimelineView` reverses the display order at render time
when `_direction` is `descending` - this matches congen11's documented
authoring rule ("the renderer handles display order"), which its own `.njk`
renderer never actually implemented.

`dateLabel` is a free string, not a parsed date - `"1998"`, `"March 2010"`,
`"1980s"`, `"Present"` are all valid.

Use `_highlight` sparingly - source guidance recommends at most 1-2
highlighted events per grow-timeline.

## Deviations from source

- congen11's renderer iterated `component.events` and read `event.date` /
  `event.description` - none of which match the schema's `items` /
  `date_label` / `body` field names. This port follows the schema.
- `_direction` and `_highlight` were declared in the schema but never
  implemented by the source renderer (no reversal logic, no highlight
  modifier class). Both are implemented here: reversal in
  `TimelineView.preRender()`, highlighting via the `grow-timeline__event--highlight`
  class.
- No SCSS existed for this component; `grow-timeline__marker` (the track dot) was
  emitted by the source renderer but entirely unstyled. The LESS here designs
  a working vertical track from the shared `$cm-*` palette.

## Adapt v5 (AMD) equivalent

```javascript
define([
  'core/js/adapt',
  'core/js/views/componentView',
  'core/js/models/componentModel'
], function(Adapt, ComponentView, ComponentModel) {

  var TimelineView = ComponentView.extend({

    preRender: function() {
      ComponentView.prototype.preRender.apply(this, arguments);

      var items = this.model.get('_items') || [];
      var direction = this.model.get('_direction') || 'ascending';
      var displayItems = direction === 'descending' ? items.slice().reverse() : items;

      this.model.set('_displayItems', displayItems);
    }

  });

  Adapt.register('grow-timeline', {
    view: TimelineView,
    model: ComponentModel
  });

  return TimelineView;

});
```
