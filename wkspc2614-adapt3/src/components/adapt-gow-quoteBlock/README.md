# adapt-gow-quoteBlock

An attributed quotation block. Ported from congen11's `quote-block` component.

## Source mapping

| This plugin | congen11 source |
|---|---|
| Schema | `schemas/components/quote-block.schema.json` (authoritative) |
| BEM classes | Invented in this port - the `.njk` renderer used a triple-mismatched, non-functional field/class set (see Deviations below) and there was **no SCSS at all** for this component |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `quote` | plain string | Yes | No quotation marks - the template adds them. Source authoring guidance capped this at ~60 words. |
| `_attribution` | object `{name (required), role, source}` | Yes | |
| `context` | plain string | No | Short framing sentence, ~25 words or fewer. |

## Deviations from source

The congen11 `.njk` renderer for this component was a stale prototype that never
matched its own schema:
- It read `component.quote_text` (schema field is `quote`).
- It piped that through the `richText` filter even though `quote` is a plain string
  in the schema (would have rendered an "Invalid rich text" comment).
- It printed `component.attribution` directly as a scalar even though `attribution`
  is an object in the schema (would have rendered `[object Object]`).
- It never rendered `context` at all.

None of that renderer's behaviour was ported. This plugin implements the schema
faithfully instead: `quote` as plain text wrapped in curly quotes, `_attribution`
rendered as name/role/source, and `context` rendered above the quote (new
`quote-block__context` class).

Because no SCSS existed for this component, the LESS here is designed from the
shared card idiom and `$cm-*` palette used elsewhere in congen11's theme, not
ported line-for-line from an existing stylesheet.

## Adapt v5 (AMD) equivalent

```javascript
define([
  'core/js/adapt',
  'core/js/views/componentView',
  'core/js/models/componentModel'
], function(Adapt, ComponentView, ComponentModel) {

  var QuoteBlockView = ComponentView.extend({});

  Adapt.register('quoteBlock', {
    view: QuoteBlockView,
    model: ComponentModel
  });

  return QuoteBlockView;

});
```
