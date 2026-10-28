# adapt-gow-statBlock

A titled collection of 2-6 highlighted statistics, each with a value, label,
optional context and source. Ported from congen11's `stat-block` component.

## Source mapping

| This plugin | congen11 source |
|---|---|
| Schema | `schemas/components/stat-block.schema.json` (authoritative) |
| `stat-block__value` / `__label` / `__context` classes | `renderers/elesson/components/stat-block.njk` (nesting rebuilt - see Deviations) |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `title` | plain string | No | Rendered as `h2`. ~10 words or fewer. |
| `_items` | array, 2-6 items | Yes | Each item: `value` (string, required), `label` (string, required), `context` (string), `source` (string). |

A single stat should use `adapt-gow-callout` instead - this component is
specifically a *collection*.

`value` is deliberately a **string**, not a number, so authors can write
`"74%"`, `"3 in 5"`, `"Over 80%"`.

`source` is not schema-required, but congen11's authoring guidance treats it as
mandatory by convention ("Always provide a source. If the source is not known,
do not include this stat.") - enforce that editorially if you want it strict.

## Deviations from source

congen11's `.njk` renderer for this component was **structurally incompatible**
with its own schema: it modelled a single stat read from the component root
(`component.value`, `component.label`) plus a `trend` field
(`trend.direction`/`trend.value`) that doesn't exist anywhere in the schema, and
had no loop and no `title` output at all.

This port is rebuilt directly from the schema's titled-collection shape
(`title` + `_items[]`). The `stat-block__value`, `__label` and `__context`
class names are kept from the source renderer, now nested inside new
`stat-block__items` (wrapper) and `stat-block__item` (per-stat) classes, with a
new `stat-block__title` and `stat-block__source` added. The non-schema `trend`
field is dropped entirely.

No SCSS existed for this component in congen11, so the LESS here is designed
from the shared card idiom and `$cm-*` palette, laid out as a responsive grid.

## Adapt v5 (AMD) equivalent

```javascript
define([
  'core/js/adapt',
  'core/js/views/componentView',
  'core/js/models/componentModel'
], function(Adapt, ComponentView, ComponentModel) {

  var StatBlockView = ComponentView.extend({});

  Adapt.register('statBlock', {
    view: StatBlockView,
    model: ComponentModel
  });

  return StatBlockView;

});
```
