# adapt-gow-keyTerm

A glossary-style key term display: term, part of speech, pronunciation,
definition, extended definition, example and related terms. Ported from
congen11's `key-term` component.

## Source mapping

| This plugin | congen11 source |
|---|---|
| Schema | `schemas/components/key-term.schema.json` (authoritative) |
| Base BEM classes (`key-term`, `key-term__title`, `key-term__definition`) | `renderers/elesson/components/key-term.njk` |
| Remaining BEM classes | New in this port (see Deviations) |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `term` | plain string | Yes | ~6 words or fewer. |
| `_partOfSpeech` | enum: `noun\|verb\|adjective\|adverb\|phrase` | No | |
| `pronunciation` | plain string | No | Plain-English phonetic, not IPA. |
| `definition` | plain string | Yes | ~40 words or fewer. |
| `extendedDefinition` | HTML string | No | Longer explanation. |
| `example` | plain string | No | Single example sentence (schema calls this singular, not a list). |
| `_relatedTerms` | array of strings, max 5 | No | |

## Deviations from source

The congen11 `.njk` renderer only ever output `term`, `definition` (incorrectly
piped through the `richText` filter, even though `definition` is a plain string
in the schema) and a looped `component.examples` array - but the schema declares
`example` as a **singular string**, not an array, so that loop would never have
matched real data. `part_of_speech`, `pronunciation`, `extended_definition` and
`related_terms` were declared in the schema but **never rendered at all**.

This port renders every schema field, keeping the original `key-term`,
`key-term__title` (term heading) and `key-term__definition` class names, and
introducing new classes for the previously-unrendered fields:
`key-term__part-of-speech`, `key-term__pronunciation`,
`key-term__extended-definition`, `key-term__example(-title)`,
`key-term__related-terms(-title|-list)`.

No SCSS existed for this component in congen11, so the LESS here is designed
from the shared card idiom and `$cm-*` palette used elsewhere in the theme.

## Adapt v5 (AMD) equivalent

```javascript
define([
  'core/js/adapt',
  'core/js/views/componentView',
  'core/js/models/componentModel'
], function(Adapt, ComponentView, ComponentModel) {

  var KeyTermView = ComponentView.extend({});

  Adapt.register('keyTerm', {
    view: KeyTermView,
    model: ComponentModel
  });

  return KeyTermView;

});
```
