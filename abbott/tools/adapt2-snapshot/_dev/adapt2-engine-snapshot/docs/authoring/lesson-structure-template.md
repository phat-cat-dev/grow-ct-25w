# Lesson page structure (v2)

The content-lesson page model. This is the readable guide; the authoritative
structure is `design-kb/design-kb.skeletons.json` (SKS-1). v2 (8 October 2026)
rewrites the earlier draft to the model agreed while authoring the first course,
and adds the generic/context coupling split, the standing per-slot context
prompts, and the token system.

## Block order

```
Orientation -> Learning outcomes -> Concept (definition + context) ->
  Interior / activity -> Worked example -> Practical guidance ->
  Check (general + context) -> Reflective prompt -> Summary -> Lesson Sources
```

Orientation renders before learning outcomes (LS-2, 2 September 2026; see
`design-kb/design-kb.skeletons.json`'s lesson-archetype notes). The authoritative
structure is the skeletons store; where this guide and the store disagree, the
store wins (SKS-1).

## The coupling model

A shell is authored once, generically. Subject/context content is filled later by
a context pack (CXP), which resolves tokens and fills coupled slots. Every slot is
one of:

- **shell** - generic, authored in the shell, same for every context.
- **token-substitution** - generic text carrying tokens the pack resolves
  (the `{{context}}` label; character tokens).
- **whole-prose** - a coupled component the pack fills with free prose that reads
  as a natural follow-on from the generic part above it.
- **structured-fields** - the shell authors a generic frame with named fields; the
  pack fills the fields with subject-specific content.

Every coupled slot carries a **standing context prompt** - a fixed instruction
tied to the page layout (not the lesson topic), which the context-pack agent
applies to whatever generic content sits in the slot. These prompts live as slot
metadata in the skeletons store, so every lesson inherits them.

### Tokens

- **`{{context}}`** - the context definition (the subject / discipline / school /
  faculty grouping label), set at `cxp-01`/`cxp-02`. Usable in any generic slot to
  name the context without full coupling.
- **character tokens** (e.g. `{{learner-a}}`, `{{learner-b}}`) - the cast used in
  worked examples. Context-specific: the names are generated and confirmed at CXP
  (`cxp-05_characters`, a diverse set), stored in the context pack, and reused
  consistently for that context across all pathways and tiers. In the shell they
  are only token slugs.

## The slots

The `slotType` column gives the key the skeletons store and the slot markers use
(`slot__<page>__<slotType>`); the interactive activity block keeps the slotType
`concept-intro`, and the worked example keeps `worked-example` (block key
`interior`), unchanged from v1 — v2 adds the `concept-context` and `summary`
coupled slots rather than renaming the existing ones.

| Slot | slotType | Role | Coupling | Standing context prompt |
|---|---|---|---|---|
| Orientation | orientation | fixed | shell + optional `{{context}}` | (optional) name the context where it aids framing |
| Learning outcomes | learning-outcomes | fixed | shell | — |
| Concept - definition | concept-definition | definition | shell | — |
| Concept - context | concept-context | definition (applied) | whole-prose | "What does this look like in practice within the given context?" |
| Interior / activity | concept-intro | activity | generic (shell) | — |
| Worked example | worked-example | example | structured-fields + character tokens | "Give a subject-specific worked example of this lesson's concept: a weaker version first, then a stronger one reached by better practice. Use the cast." |
| Practical guidance | practical-guidance | guidance | shell + token-substitution (`{{context}}`) | — (label only) |
| Check - general | check (position 1) | check | shell | — |
| Check - context | check (rest) | check | coupled | the subject's own version of the lesson's check question |
| Reflective prompt | reflective-prompt | reflect | shell | — |
| Summary | summary | fixed | structured-fields | "Recap what the learner can now do, in terms of their own subject/context." |
| Lesson Sources | lesson-references | refs | shell | — |

### Concept (two blocks)

The concept introduction is **two blocks**:

1. **concept-definition** (shell). A generic definition of the lesson topic,
   why-before-how. It **frames** the lesson and says why it matters; it does **not**
   summarise or spoil what the activity will reveal. Standing (generic) instruction:
   "author a generic definition of the lesson topic."
2. **concept-context** (whole-prose coupled, marker `slot__<page>__concept-context`).
   Empty in the shell. The pack fills it from the standing prompt above, as a
   natural follow-on from the definition.

### Interior / activity (generic)

The interactive presentation of the concept (slotType `concept-intro`), authored
generically (same for every context). The component is chosen from **three activity proposals**: three
alternative components that could present this content, proposed on (a) the
**shape** of the content and (b) **component fit**, from which the human selects
one. An asset-needing component (e.g. hotgraphic) is a valid proposal; its asset is
a `visualAssets` placeholder supplied if chosen (never a pre-flight failure). The
checklist (practical guidance) and the MCQ (check) are defaults, not among the
three proposals.

**Activity-mode question components** (8 October 2026). The activity may be a
manipulation question component rather than a presentational reveal: `matching`,
`sortable`, `hotspot` or `slider` (learn by doing). In the activity slot such a
component runs in *activity mode*, not as a check: `_attempts: -1` (unlimited
tries), `_incorrect.notFinal` that explains and points the way (no `final`), and
a `correct` that reiterates and explains the concept just completed; never graded
(`_isPartOfAssessment: false`). This is distinct from the check slot (limited
attempts, `notFinal` + `final`, a formative test). `mcq`/`gmcq` (pure selection)
stay check-only.

### Worked example (structured-fields + cast)

A distinct block after the activity. The shell authors the generic frame (the
weaker-then-stronger contrast and the field structure for this lesson's concept);
the pack fills subject-specific fields and the cast names via character tokens.
Weaker or less-developed version first. The standing prompt is layout-level: it
says "a weaker version first, then a stronger one", never a topic (surface/deep,
etc.) — the topic is the lesson's own, set in the shell frame, not in the prompt.

## Trickle

Default-on, override by exception. Gate at: concept -> interior/activity ("now see
it"), practical guidance -> check ("now prove it"). No gating across the opening
reads (outcomes/orientation/concept) or the end wind-down (reflective/summary/
sources). Interior gating depends on the chosen activity component's own pacing.

## Fixed blocks (role unchanged)

- **Learning outcomes** - `text`; "By the end of this topic, you will be able to:"
  + the lesson's outcomes (from `crs-04_lesson-map`), Bloom verbs for the tier.
- **Orientation** - `text`; situates the learner; may use `{{context}}`.
- **Reflective prompt** - `opentext` (`_isOptional: true`, never completion-bearing);
  1-3 genuine questions, "no right answers".
- **Lesson Sources** - `references`; footnote-style pointer (chapter + pages), from
  the lesson's bound source sections; every source also appears in W-CLOSE's Course
  Sources.

## Block ID convention

`{lessonKey}-b-{nn}`, increment by 5. Ids generated per ID-1; coupled components
carry `_classes: "slot__{page}__{slotType}"` (or `__{part}` per MP-1); generic
components carry `_classes: ""`.
