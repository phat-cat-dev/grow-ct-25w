# adapt-grow-annotate

A passage the learner **marks up with hand-drawn ink** — circle the key idea,
underline evidence, flag what they're unsure of. Reflective, not graded. Built
on the shared [grow-marks](../grow-marks/) engine.

The author chooses which words are annotatable and offers a small palette of
annotation "tools"; the learner picks a tool and clicks words to mark them, and
each mark draws on. This is the self-contained version of the idea — the
companion **adapt-grow-marks extension** handles marking across other
components (author-tagged spans + question right/wrong).

## How authoring works

The passage is plain text with annotatable words wrapped in double brackets:

```
"A landscape needs a [[foreground]], a [[middle ground]] and a [[backdrop|bd]]."
```

`[[word]]` becomes a clickable target; add a stable key with a pipe
(`[[word|bd]]`) if you reuse a word or want a fixed id. Surrounding text may
contain inline HTML.

Tools are the palette (`_tools`): each is a label + an ink mark + a colour.

```json
"_tools": [
  { "_id": "idea",     "label": "Main idea", "_mark": "oval",      "_color": "accent" },
  { "_id": "evidence", "label": "Evidence",  "_mark": "underline", "_color": "positive" },
  { "_id": "doubt",    "label": "Not sure",  "_mark": "question",  "_color": "neutral" }
]
```

With a single tool the component is a simple circle-the-word toggle (and if you
provide none, a default "Circle" tool is used). `example.json` is a complete
component block.

Other settings: `_minAnnotations` (how many marks before it counts complete; 0
= complete on view), `_showLabels` (a label chip floating above each marked
word, on top of the ink mark), `_allowReset` (a clear button).

Question mode (`_isQuestion` + `_answers`, or `_targets` in free-select) adds a
Submit button that marks each target right/wrong and shows feedback. A wrong
answer does **not** lock the activity: the learner's marks and the feedback stay
in place, the targets in red stay editable, and the button becomes **Check
again** — so corrections are made with the feedback in front of them, without
starting over. Only an all-correct submit locks it.

Marks available to `_mark`: the word-wrappers `oval`, `box`, `bracket`,
`underline`, `double`, `wavy`, `strike`, `scribble`, `highlight`, and the
beside-the-word glyphs `tick`, `cross`, `star`, `caret`, `checkbox`,
`question`, `exclaim`.

Colours (`_color`) come in two families:
- **Semantic ink** — `accent`, `positive`, `negative`, `neutral`, `comment`,
  `soft`, mapped to the theme tokens.
- **Fluoro marker pens** — `fluro-pink`, `fluro-yellow`, `fluro-green`,
  `fluro-blue`, `fluro-purple`: fixed bright colours. Pair with `highlight` for a
  highlighter pen, or with `box`/`oval` for a bright rectangle/circle. Together
  the `highlight`/`box`/`oval` marks × five fluoro colours give the full
  marker-pen range.

## Activity types (one component, many shapes)

The same component covers a spectrum, set by three independent switches:

| Switch | Off | On |
| --- | --- | --- |
| `_freeSelect` | author picks the words (`[[word]]`) | learner drags across any text |
| `_isQuestion` | reflective, no right/wrong | Submit + marked right/wrong + feedback |
| who sets the colour | **learner** chooses the pen (omit `_answers`/`_targets`) | **author/AI** fixes it (give `_answers` or `_targets`) |

So, for example: free-hand reflective highlighting (all off); "find and colour
the claim/evidence/hedge" (free-select + question + `_targets`); or author-pinned
"label each `[[word]]`" (targets + question + `_answers`). `example.json` ships five
worked instances: a reflective free-hand marker (Variant A); two graded
free-select exercises on the identical shell but two unrelated subject
vocabularies — rhetorical moves (claim / evidence / assertive / tentative,
Variant B) and critical vocabulary (application / analysis / evaluation /
synthesis, Variant E); an author-pinned graded exercise (Variant C); and a
reflective free-select shapes exercise (Variant D).

## Data object: shell vs context (baseline / L2 / L3)

The data object splits cleanly into a **stable shell** and a **swappable content
slot**, so one activity design can be filled by an AI agent or a human at any
pitch:

- **Shell (fixed per activity design):** `_tools` (the pen palette + what each
  means), `_freeSelect`, `_isQuestion`, `_showLabels`, `_minAnnotations`,
  `instruction`, `_feedback`. These are the analytical vocabulary and are reused
  across subjects.
- **Content slot (filled per use):** `passage` and the answer key (`_answers` for
  targets mode, `_targets` for free-select) — and, in targets mode, which words
  are bracketed. Fill it from a **baseline** generic passage, or from
  **context-specific** material at proficiency **Level 2 or Level 3**; the shell
  does not change. Keep tool ids stable so the same `_answers`/`_targets` grammar
  carries across fills.

**One data object, not two.** The split above is the whole answer to "do we
need a separate data shape per activity type?" — no. `_tools[]` already takes
an arbitrary palette and `js/annotateLogic.js` is tool-id-agnostic throughout
(its own test fixture uses `'hedge'` as a bare string), so a new teaching
vocabulary is new *content*, not a new *component shape*. Variant B
(rhetorical moves: claim / evidence / assertive / tentative) and Variant E
(critical vocabulary: application / analysis / evaluation / synthesis) are the
proof: two worked examples from unrelated subject domains, filled into the
identical shell, with no `_mode` switch anywhere. Adding one would hard-code a
specific rhetorical or Bloom's vocabulary into component code — exactly the
coupling a generic, cross-subject component needs to avoid.

## Reflective or analytical?

Marking up a passage looks reflective — the learner is doing something with
the text in front of them — but most annotate exercises are analytical: the
learner is naming the structure of *someone else's* writing, not examining
their own practice. Three conditions have to hold together before an instance
counts as reflective, not analytical:

1. **`_isQuestion` is false (or omitted).** A right answer to mark means the
   exercise is testing recognition of a category, not inviting a response.
2. **No `_targets` or `_answers`.** An answer key is itself evidence the
   activity is graded against one fixed reading, whatever `_isQuestion` says.
3. **Tool labels invite a response, not name a category.** "I agree", "I have
   a question", "Important to me" ask what the learner thinks. "Claim",
   "Evidence", "Hedge" ask the learner to identify a category, whether or not
   that identification is marked right or wrong.

The third condition is the one authors get wrong. Strip the grading out of
Variant B or Variant E (drop `_isQuestion` and `_targets`, keep the pens) and
the result is still analytical, merely unmarked — the pens still name
rhetorical or cognitive categories, not responses. Only Variant A (the
free-hand marker, with pens like "I agree" and "I have a question") meets all
three conditions.

Per CLAUDE.md's component-mapping table, a reflective prompt routes to
`opentext` (1-3 genuine questions, "no right answers"), and that routing does
not change here. Annotate's reflective mode *complements* opentext, it does
not replace it: it lets the learner mark up *someone else's* text — a
passage, a source, a piece of feedback — and never asks them to compose their
own writing. Candidate placements: critical/close reading, source evaluation,
rhetorical analysis, feedback literacy (marking up a tutor's comments), and —
as a pre-writing step, never the destination — a reflective-writing pathway
that has the learner mark a passage before an `opentext` prompt asks them to
write about it.

That pre-writing placement is also the direct answer to "what makes a piece of
writing reflective rather than descriptive": not the first person, and not
naming a feeling, but four moves — what you did, what close comparison shows,
whether it worked, and what you would combine or change next time — turned on
your own practice instead of someone else's. That is exactly what mode 2
(`c-annotate-vocab`, the Gibbs'-cycle passage) has the learner find in
somebody else's reflective paragraph, as rehearsal before writing their own.

## How it works

- `js/annotateLogic.js` — pure: parses the passage into segments, holds the
  `targetKey -> toolId` state (apply/toggle), completion predicate, and
  (de)serialisation. **19 unit tests, all passing.**
- `js/AnnotateModel.js` — `ComponentModel` subclass; parses the passage in
  `init`, records annotations, completes at `_minAnnotations`.
- `js/AnnotateView.js` — renders the JSX shell once, then wires the palette and
  targets **imperatively** and drives grow-marks. There is no React re-render
  after mount, so the appended mark SVGs are never discarded (same discipline
  as scroll-scenes).
- `templates/annotate.jsx` — the static shell (palette + passage + footer).
- `less/annotate.less` + `less/grow-marks.less` — component styles plus the
  vendored mark styles.
- `js/libs/` — the vendored grow-marks core (`growMarks.js`, `marksLogic.js`,
  `marksCatalogue.js`).

### Accessibility
Each target is a real `<button>` with `aria-pressed`; the palette is a
`role="toolbar"`; changes are announced through a polite live region; marks
respect reduced motion (shown complete, no animation). Native scrolling/reading
is unaffected.

Author-pinned targets (`[[word]]`) no longer underline on hover. A hover
underline reads as a hyperlink affordance, so brushing the cursor across the
passage silently revealed the whole answer set before anyone read a word. The
underline carried no other function — focus state and the `.is-annotated`
weight change are untouched — so it was removed outright rather than dimmed.

That fixes the visual leak, not the whole leak, by design. Pinned targets are
real `<button>` elements so they are reachable and operable by keyboard and by
screen reader, which is the correct accessible control — and that same
correctness means the full set of answerable words is still discoverable by
tabbing through the passage before engaging with it. Breaking button
semantics to hide that would trade accessibility for a cosmetic fix, which is
not a trade worth making. Free-select mode has no pinned target set to leak:
there is nothing to tab to until the learner selects something themselves.

## Vendored library

`js/libs/` and `less/grow-marks.less` are copied from
`abbott/components/grow-marks` so this plugin is self-contained (Adapt plugins
can't import across plugin folders). If the library changes, re-copy:

```bash
cp ../grow-marks/src/*.js            js/libs/
cp ../grow-marks/grow-marks.css      less/grow-marks.less
```

## Known limitation (v1)

Completion persists through Adapt's normal state (it's a trackable). The
**annotations themselves** are written to `_userAnswer` and restored on
re-render, but persisting them into LMS suspend data across a full reload needs
them wired into the model's serialised state / `offlineStorage` — a small
follow-up. The interaction, marks, labels, completion and reset all work now.

## Developing

```bash
node --test test/annotateLogic.test.js
```

The view/engine are exercised visually once built. To preview the look of the
marks without a build, open the grow-marks demo (`../grow-marks/demo/`).

## Installing into the GROW build

Copy the folder to `wkspc2614-adapt3/src/components/adapt-grow-annotate/`, add a
component block (see `example.json`) to a block's `components.json`, then
`npx grunt build`. Component type `annotate`, attribute `_annotate`.
