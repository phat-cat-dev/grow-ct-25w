# The pipeline

This is the one authoritative description of how a course is made, start to
finish. Read it first. Everything else in `docs/` is detail that hangs off the
stages described here.

The pipeline turns a **pathway + pitch** (a topic and a level) into a **SCORM
package** ready for Moodle, in three stages:

```
  STAGE A  consult & specify        STAGE B  build                 STAGE C  test & package
  ──────────────────────────        ───────────────────────        ────────────────────────
  ONB  onboarding            ┐      scaffold (shell skeleton)       verify + lint
  CXS  context shell         ├─►    LES   lesson content       ─►   grunt build  ─►  SCORM zip
  CRS  course                ┘      WRA   wrapper/assessment        server-scorm + a11y
                                    CXP   context pack (subject)    (Moodle upload = manual)
       produces the MANIFEST        fills the shell, compiles       produces the PACKAGE
```

- **Stage A** is a guided conversation (the "gates"). Its output is the
  **manifest**: `courses/<slug>/course-design_<slug>.json`, an append-only
  record of every decision. Nothing is built yet.
- **Stage B** turns the manifest into Adapt content. `/scaffold` builds the
  empty page skeleton from the manifest; the LES/WRA gates author the lessons
  and wrappers into it; the CXP gates generate a subject-specific context pack
  that fills the reserved context slots; then `grunt build` compiles it.
- **Stage C** verifies, packages the build as a SCORM zip, and hands it off.
  Uploading to Moodle is manual (the pipeline has no Moodle access).

The manifest is the hinge. Stage A writes it; Stage B reads it. It is the
single source of truth for what a course is.

---

## The six phases (Stage A and the first half of Stage B)

Work is organised into six **phases**, run in order. Each phase holds one or
more **gates**. A gate is one decision. The authoritative definitions live in
`design-kb/design-kb.gates.json` (24 gates, kbVersion 0.10.0); this table is the
readable summary.

A gate has a **kind**:
- **human** - the agent asks, the person answers.
- **agent+human** - the agent generates a proposal, the person confirms, amends,
  chooses between options, or asks for a regenerate.
- **auto** - a reserved placeholder that auto-passes with a default. Present in
  the flow so the slot exists to be wired later; it takes no input now.

And a **hardness**: `hard-stop` (never closes without an answer), `soft` (a
proposal stands unless changed), `advisory` (informational, auto-stands).

### ONB - Onboarding  (Stage A)
Sets the course's identity and creates its files.

| gate | kind | does |
|---|---|---|
| `onb-01_theme-preset` | human | pick the theme preset |
| `onb-02_course-theme` | agent+human | set the theme (one of the 13 pathways) |
| `onb-03_pitch` | human | set the pitch (introductory / intermediate / advanced) |
| `onb-04_naming` | agent+human | derive course name + slug; **the folder and manifest are created here** |

`/new-course` runs once at the end of ONB: it writes the four answers into a new
`courses/<slug>/course-design_<slug>.json` and auto-states the reserved CXS
gates. This is the one place the manifest's append-only rule is waived, because
the file must be born before anything can append to it.

### CXS - Context Shell  (Stage A)
The angle-setting layer. For the current build, **all six gates auto-pass** with
a default of "none" (except `cxs-04`, which carries the `Harvard (Cite Them
Right)` referencing default). They are reserved placeholders for later wiring:
institutional context, subject context, qualifiers, referencing style, external
standards, resources. CXS sits before the course body so that angle is available
to the agent as it builds, even while reserved.

### CRS - Course  (Stage A)
Produces the generic course: its scope, outcomes and lesson map.

| gate | kind | does |
|---|---|---|
| `crs-01_sources` | human | confirm the source material in scope |
| `crs-02_thematic-scope` | agent+human | agent reads the book, proposes chapters/sections in scope, tier-band window, prior-experience anchor, and 5-10 **thematic strands** (candidate lesson topics); person confirms |
| `crs-03_course-outcomes` | agent+human | agent proposes 3-5 course outcomes (+ a confidence statement and the MCQ questions measuring each); person confirms |
| `crs-04_lesson-map` | agent+human | agent proposes the lesson list from the strands + outcomes; person confirms |
| `crs-05_course-spec` | agent+human (advisory) | auto-assembles the course spec: a rollup of everything confirmed in ONB + CXS + CRS. No new decisions. |

When ONB and CRS have closed, run **`/scaffold`** (Stage A to Stage B hinge). It
fuses the manifest with the page archetypes and writes the empty Adapt content
model (`config.json` + `en/*.json`) with one page per lesson in the lesson map.
Interior/activity slots are emitted as **deferred blocks** (empty `_id`s) for the
LES/WRA gates to fill. A scaffolded shell does not build on its own, by design
(see RUNBOOK).

### LES - Lesson  (Stage B)
`les-01_lesson-proposal` (agent+human, soft, **repeats once per lesson**). For
each lesson, the agent proposes the content for the variable slots, led by
pedagogy: it selects activity-patterns whose slot-types, tier calibration and
content shapes fit, and realises each via the pattern's Adapt component. The
person confirms or amends. `/land` writes the confirmed content into
`components.json` / `blocks.json` and records an `instantiation` in the manifest.

### WRA - Wrapper  (Stage B)
Four agent+human gates that author the course-level pages:

| gate | page |
|---|---|
| `wra-01_wrapper-open` | the opening page (overview, outcomes, signpost) |
| `wra-02_wrapper-close` | the closing page (summary, where-next) |
| `wra-03_summative` | the summative assessment page |
| `wra-04_confidence` | the confidence pre/post pages (course-level) |

### CXP - Context Pack  (Stage B, standalone, last)
Generates subject-specific content that fills the shell's reserved context
slots. Standalone by design: a pack can be generated for any subject against the
same finished shell, so one shell serves many contexts.

| gate | kind | does |
|---|---|---|
| `cxp-01_subject` | human | name the subject/context |
| `cxp-02_qualifiers` | human | set qualifiers for this pack |
| `cxp-03_exemplar-programmes` | auto | reserved |
| `cxp-04_context-generation` | agent+human | generate the pack content; `merge-context.js` slots it into the shell's context-coupled components |

---

## The page archetypes (what the manifest maps onto)

The scaffold builds every page from one of six **archetypes**, defined in
`design-kb/design-kb.skeletons.json`. Each archetype is a sequence of **fixed**
slots (the generator always fills these) and **variable** slots (a gate decides
whether the slot appears and which component fills it).

| archetype | purpose |
|---|---|
| `wrapper-open` | course opening page |
| `c-pre` | confidence pre-check |
| `lesson` | a standard lesson page |
| `summative` | the summative assessment |
| `c-post` | confidence post-check |
| `wrapper-close` | course closing page |

The `lesson` archetype is the workhorse. Its slots, in order:

```
orientation (f) · learning-outcomes (f) · concept-intro (v) · worked-example (v)
· practical-guidance (v) · check (v) · reflective-prompt (v) · summary (f)
· lesson-references (v)
```

Variable slots carry a `selectionModel` that says how the component is chosen
(pattern-derived, single-realisation, or furniture) and a `contextCoupling` that
says how a context pack fills it (shell-coupled, token-substitution,
structured-fields, whole-prose). The store is authoritative; read it rather than
relying on this summary when encoding.

---

## The two grounding layers

The agent generates from two separate grounding layers, and never mixes them:

- **Layer 1 - pathway grounding (generic).** `design-kb/design-kb.pathways.json`,
  one resolved record per pathway: the chapters in scope, the per-tier focus and
  voice band, and the book-map chunk ids tagged to the pathway (primary = sole
  tag; shared = co-tagged). Read at the generic content gates (crs-02, crs-03,
  crs-04, les-01, wra-*). It is subject-agnostic - the same whatever subject the
  course is later contextualised for. Chunk *text* is read from the book map it
  points at (`source-kb/source-maps/book-excelling-at-university-2026.json`), the
  single source of truth for text.
- **Layer 2 - insitutional context.** Not currently active
- **Layer 3 - subject grounding.** The QAA benchmarks and the ingested
  vector-DB corpus, keyed by subject (CAH/HECOS). Read only at CXP (cxp-04), to
  fill the coupled slots with subject-specific content. Deferred in v1 to the
  search/index step; left out of the repo until then.
- **Layer 4 - cross-cutting qualifiers.** Not currently active


One shell is authored once from Layer 1; many context versions are generated
from Layer 2 against that finished shell. That split is what the next section is
about.

## How content gets its subject angle (the coupling idea)

A shell is authored **once**, generically. Subject-specific content arrives later
through the context pack (CXP), which fills the slots marked for coupling. This
is why the referencing style, for example, is a token in the shell rather than a
baked-in value: the token resolves per subject at pack time, so Law (OSCOLA) and
Psychology (APA) reuse the same shell without it being rebuilt. The coupling
layer is what lets one generic shell serve many contexts.

---

## Where each stage's output lives

| Stage | Output | Path |
|---|---|---|
| A | the manifest (every decision) | `courses/<slug>/course-design_<slug>.json` |
| A | the readable course spec | `courses/<slug>/adp-course-design-specification_<slug>.md` |
| B | the Adapt content model (shell) | `courses/<slug>/config.json`, `courses/<slug>/en/*.json` |
| B | context packs | `content/context-packs/<subject>/<slug>/` |
| B | compiled course | `build/` (gitignored) |
| C | SCORM package | `scorm-packages/` (gitignored) |

See `docs/ARCHITECTURE.md` for the full component map (which tool reads/writes
what) and `docs/RUNBOOK.md` for the exact commands.
