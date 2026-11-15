# Mapping the Book to Adapt — Ground-Up Workflow

*Project reference. The agreed method for turning the teaching in* Excelling at University *into Adapt-native interactive learning. This is a design exercise: it decides how content should work before any Adapt JSON is written.*

---

## The goal

Turn the pedagogy of the book into Adapt-native interactive learning that is (a) consistent across every pathway, (b) faithful to the voice specification, and (c) designed deliberately rather than improvised component-by-component. The exercise produces one reusable design — the mapping artefact — that all later authoring follows.

---

## Principles (why the workflow is shaped this way)

- **Design before build.** Decide the teaching first, encode it in Adapt second. The technical build is the last mile, not the starting point.
- **Need before tool.** Work out what the content needs to *do* before surveying what Adapt *offers*, so components end up serving the teaching rather than the teaching being bent to fit whatever component is nearest to hand.
- **Three authoritative inputs, in order.** The book (what to teach), the voice specification (how it should sound), and the linguistic audit (the structural flow). Nothing else feeds the design.
- **Generalise carefully.** Build one practice-agnostic core mapping. Where a specific practice needs something unusual, record it as a known gap rather than inventing a general rule from a single case.
- **Constructed content may expand on the book, never just repeat it.** Where the book doesn't give a lesson's concept a natural worked example, contrast, or other content need, construct new material rather than forcing the design to fit only what's literally on the page. Constructed content must expand on the book's material or offer a genuinely different version of it — never restate what's already there in different words. Flag constructed (non-book) content explicitly in that lesson's Step 5 output, same as any other design deviation.
- **Reference-worthiness is filtered, not automatic.** A book source earns a reference in the final references list only where it offers additional or more extensive discussion beyond what the lesson itself already provides, not wherever content happened to be drawn from. Track candidate sourcing as each lesson is authored (a working sourcing log, separate from the final references data, which requires a real link the author supplies, never a fabricated one).
- **The prior specimen is archived reference only.** An earlier, non-Adapt pathway build exists (see the closing note). It is deliberately *not* an input, to avoid anchoring the fresh design on choices that predate the current voice specification.

---

## The three-layer copy model

Copy generation holds **three** distinct layers:

1. **Shell** — the teaching prose and structure shared across contexts (the six-part section flow, core explanations, practical guidance). Shell content is pathway-specific but context-neutral.

2. **Context slots** — the context-specific fills (character name, discipline, worked-example details) supplied by a context pack. These swap by discipline/overlay without touching the shell.

3. **Wrapper** — the connective framing that makes lessons feel like one coherent programme within a pathway-tier: how a lesson opens and orients, signposts where it sits in the sequence and what's coming, and closes or hands off to the next lesson.

The wrapper is **scoped to the pathway-tier** (e.g. "Academic Writing — Introductory" has one wrapper around its lesson set; "Academic Writing — Intermediate" has its own). It is **not fixed boilerplate** — it flexes deliberately by pathway, tier, lesson-type (orientation vs skill lesson), and context. When generating lesson copy, the wrapper is a conscious design decision, not a pasted-in constant.

Note: The six-part section flow (orientation → concept → worked example → analysis → practical guidance → reflective prompt) operates *within* a lesson. The wrapper operates *around* lessons, at the pathway-tier level.

---

## What we are actually producing

The output is **the mapping artefact**: a specification that, for each teaching move, names the Adapt component that carries it, the voice rule it must follow, whether it is assessed, and how it shifts by tier. It should be detailed enough that generating the Adapt JSON later becomes a mechanical translation.

The artefact takes roughly this shape (one row per teaching move):

| Teaching move | When to use it | Adapt component(s) | Voice rule (spec ref) | Assessed? | Tier adjustment | Accessibility note |
|---|---|---|---|---|---|---|
| Worked example | Model a skill in action | narrative | §15.2 (third person, weaker example first) | No | More complex scenario at higher tiers | Alt text on any images; logical reading order |

---

## The steps

### Step 1 — Inventory the teaching moves (the demand)

**In plain terms:** work out the small set of things good teaching in this book actually *does* — explaining an idea, showing a worked example, contrasting two approaches, checking understanding, prompting reflection — and the order they usually come in.

**Why it comes first:** you cannot sensibly choose tools until you know the jobs. Starting here keeps the whole design driven by teaching intent rather than by whichever component looks appealing.

**Inputs:** the book, plus the audit's six-part section flow (orientation → concept → worked example → analysis → practical guidance → reflective prompt) and its content types.

**Output:** a short, named list of teaching moves and the typical sequence they follow.

---

### Step 2 — Audit Adapt's components (the supply)

**In plain terms:** go through the interactive building blocks Adapt actually gives you — text, graphic, accordion, narrative, multiple-choice, matching, text input, slider, and the rest — and describe, in teaching language, what each one is good and bad at.

**Why:** you need an honest picture of the toolkit before you can match jobs to tools. Crucially, this is done from the *real components installed in the project*, read from their schemas, not from memory or assumption.

**Inputs:** the actual component schemas in the repository.

**Output:** a plain-language capability list — for example, "accordion = reference material you reveal on demand; narrative = a step-through worked example; matching = pairing concepts for a low-stakes check."

---

### Step 3 — Map the flow to Adapt's structure

**In plain terms:** decide how one whole lesson lays out inside Adapt's nesting. A topic becomes a page; the stages of the teaching flow become its sections and rows; and you decide where progression gates and any assessment sit.

**Why:** Adapt organises everything as page → section → row → component. Getting this skeleton right first means every smaller piece has somewhere to live, and it settles how *trickle* (which locks later content until earlier content is done) and scoring will work.

**Inputs:** steps 1–2, plus the project plan's packaging rule (one SCORM package per practice-tier).

**Output:** a structural template for a topic — the standard skeleton every topic will be built on.

**Note:** Formative vs summative, scoring, and pass/fail are a per-tier design decision — see `docs/curriculum/scoring-and-summative-model.md`.

---

### Step 4 — Map the moves to components (the artefact)

**In plain terms:** the main event. Pair each teaching move from step 1 with the Adapt component from step 2 that best carries it; attach the voice rule it must follow; mark whether it is scored; and note how it changes as the tier rises.

**Why:** this is the reusable design that makes every pathway feel like one programme and keeps every piece voice-compliant. It is the thing the later authoring actually follows.

**Inputs:** steps 1–3, plus the voice specification.

**Output:** the mapping artefact (the table described above), practice-agnostic, with any practice-specific exceptions flagged.

---

### Step 5 — Pressure-test on one real topic

**In plain terms:** take one genuine topic from the book — Chapter 9 (Writing for Assessment) is the natural first choice — and build it out on paper using the mapping, with no code yet, to see whether the design survives contact with real content. Where the source material doesn't fully serve the lesson's concept, construct new content per the Principles section above, rather than forcing the design into an awkward shape to avoid it.

**Why:** a mapping that looks tidy in the abstract can fall apart on a real lesson. Testing on paper catches the gaps cheaply and may send you back to revise steps 3–4. Expect at least one loop; that is the step working, not failing.

**Inputs:** a Chapter 9 topic and the draft artefact.

**Output:** a worked topic outline, a list of any fixes the mapping needs, and a sourcing-log entry per book passage used. When a lesson includes genuinely context-coupled content (per CP-1b's variation types), the paper draft also documents that content's slot shape — following the pattern established in `content/drafts/pilot/overlay-tokens-lesson2.md` and the L03-L07 retrofit (see open-decisions.md #28, CP-1d): state which type applies (1: token substitution; 2: structured fields; or 3: whole prose per context) and the field shape or replacement scope, so Step 6 encoding can tag the slot correctly without a separate retrofit pass later. Sourcing-log entries are assessed against the reference-worthiness filter (Principles section). **Additionally (per RF-4):** any book material used that goes beyond what the lesson itself already covers (i.e. genuinely reference-worthy) should be logged in `book-sourcing-log.md` (chapter, page, brief note) as the paper outline is drafted — not left to be reconstructed later.

---

### Step 6 — Encode as Adapt JSON

**In plain terms:** only now translate the validated design into the actual Adapt content files. This is the point where Claude Code does the heavy lifting.

**Why:** with the design settled and tested, generating correct JSON is mechanical, and it plays to Claude Code's strengths — especially the fiddly, error-prone wiring of `_id` and `_parentId` references that Adapt depends on.

**Inputs:** the validated artefact and one topic outline.

**Output:** the pilot slice, built and building in Adapt. Any reference-log entries with a confirmed link are encoded into the references component at this stage; entries still awaiting a link stay logged, not fabricated. **Additionally (per PLR-1):** cross-check the lesson against `book-sourcing-log.md` and draft the corresponding lesson-level reference block (citation only — chapter + page — no live URL yet); the URL is sourced later in the dedicated Reference Consolidation pass (see `course-creation-workflow.md` Step 2.9).

---

### Portable-unit authoring discipline

Each lesson is authored as a **portable unit** from the start, so it can either:

- **(a) Live as a page** inside a pathway-tier Adapt course (the standard case: wrapper = the tier course's menu + shared framing; one SCORM package per tier), **or**
- **(b) Be pulled into a bespoke suite** (a custom set drawn from across pathways, assembled at the Moodle level) without being re-authored or duplicated.

**Mechanics:**

- **Standard pathway-tier:** one Adapt course, menu-as-wrapper, lessons as pages, gated by trickle where appropriate, one SCORM package. Wrapping is native Adapt structure, NOT hyperlinks.
- **Bespoke suite:** assembly at the Moodle level across self-contained units; cross-package sequencing/completion is Moodle's job.

**Portability discipline when authoring:**

- Each lesson uses its own content objects/articles/blocks/components with clean, non-colliding ids (e.g. lesson 1 = co-400/a-400/b-400–b-430/c-400–c-435; lesson 2 = co-500 series).
- Self-contained tracking: each lesson's trackingIds are contiguous and independent.
- No hard dependencies on sibling lessons' ids inside a lesson's own content — a lesson can be dropped into a tier course as a page or built standalone.
- Context slots (context overlays) are marked by CSS class, not by cross-lesson references.

This is the same "cut the seam early" discipline as the context slots: cheap now, painful to retrofit.

---

## How we know the mapping is good (definition of done)

The artefact is ready to build from when all of the following hold:

- every teaching move has a component home;
- every component carries its voice rule, referenced to the specification;
- assessable moves are marked, with their tier thresholds set;
- the pressure-test topic builds out without forcing the content into an awkward shape; and
- practice-specific gaps are listed openly, not hidden.

If the pressure-test forces content into a shape that fights the teaching, the mapping is not done — revise and retest.

---

## Where this sits in the wider project

Steps 1–4 produce the artefact. Step 5 validates it. Step 6 begins the pilot vertical slice — one practice built across the core tiers — which is the first real content and the proof of the whole voice-to-Adapt-to-Moodle workflow. Everything in this document is design; the build follows from it.

---

## Note on the prior pathway specimen

An earlier, non-Adapt pathway build exists (a custom HTML format, with academic writing worked out across two tiers). It holds valuable design thinking, but its content predates the current voice specification and its format does not map directly to Adapt. It is therefore kept as **archived reference only** and is not an input to this exercise, to avoid anchoring the fresh design on out-of-date choices. Its one legitimate later use is as a **final sanity check**: once the artefact exists, a single pass to ask "did we miss any obvious teaching move they thought of?" — never as something that shapes the design up front.

---

*End of workflow document.*