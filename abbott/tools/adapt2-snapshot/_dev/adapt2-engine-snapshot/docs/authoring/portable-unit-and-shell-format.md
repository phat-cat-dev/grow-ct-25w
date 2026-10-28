# Portable Unit & Shell Format

*Design decision. Defines what a **lesson shell** is on disk, the `_id` namespacing
convention that keeps lessons collision-free, and the extract/assemble path that
lets one authored lesson be lifted into any delivery course. This is the design
record; the assembly tooling that acts on it is built later (see "Status" below).*

**Status:** Convention is authoritative and binds all lessons from now on. The
pilot lessons (co-400, co-500) are renumbered to fit it. The extract/assemble
*tooling* remains deferred until after Moodle integration is proven — this doc
specifies the convention that tooling will implement, so it can be built later
without a content rewrite.

Intended home: `docs/authoring/portable-unit-and-shell-format.md`.

---

## Why this exists

The programme's authoring model is **portable-unit**: a lesson is a self-contained
teaching unit that can live in a tier course *or* be pulled into a bespoke
Moodle-assembled suite. That premise only holds if a lesson carries no dependency
on *where it was authored* — no id that collides when the lesson lands in a new
course, no reference pointing at another lesson's objects, no asset filename that
clashes with a neighbour's.

The pilot investigation confirmed the two real lessons are already **cleanly
liftable**: their `_parentId` chains terminate at `course`, and nothing in either
lesson references an id outside itself. What they lack is a *convention* that
guarantees this stays true as the matrix scales to thirteen pathways. Right now
the lessons avoid collision by luck (co-400 happens to use 400-series ids, co-500
the 500-series); two lessons authored independently would both reach for the same
low-numbered ids and clash on assembly. This doc replaces luck with a rule.

---

## What a shell IS

A **lesson shell** is a self-contained directory holding one lesson's built Adapt
JSON, its assets, and a manifest of what it depends on. Concretely:

```
content/shells/<pathway>/<tier>/<lesson-key>/
├── manifest.json          # lesson key, title, dependencies, required globals
├── contentObject.json     # the page object (one)
├── articles.json          # article object(s) for this lesson
├── blocks.json            # block objects for this lesson
├── components.json        # component objects for this lesson
└── assets/
    └── <lesson-key>-*.png # lesson-owned assets, namespaced by key
```

Three things it is deliberately **not**:

- **Not a full Adapt sub-course.** Adapt cannot build a lone fragment; a shell is
  raw material for assembly, not a runnable course on its own.
- **Not a pre-JSON authored source re-encoded per course.** The encoding work is
  done once and voice-checked once; re-encoding per delivery course would throw
  that away and reopen voice drift. The shell holds the *built* JSON — it is the
  canonical form of the lesson.
- **Not tied to its authoring location.** Filing a shell under
  `academic-writing/introductory/` is filing, not binding. Adapt resolves everything
  by `_id`/`_parentId`, never by filesystem path, so a shell lifts out of its
  folder without anything breaking. (The folder tells a human where it came from;
  it tells Adapt nothing.)

The shell is the canonical lesson. **Delivery courses are assembled from shells** —
author once, assemble many.

---

## The `_id` namespacing convention

### The rule

Every object id carries a **lesson key** as an opaque prefix:

```
<lesson-key>-<type>-<local-number>
```

- **Lesson key** — a short, opaque, permanently-unique token: `L01`, `L02`, `L03`…
  Assigned once from a registry, never reused, never re-derived from the title.
- **type** — `co` (page), `a` (article), `b` (block), `c` (component).
- **local-number** — restarts within each lesson, gapped in 5s: `05`, `10`, `15`…

Examples: `L01-co-01`, `L01-a-01`, `L01-b-05`, `L01-c-05`.

### Why opaque, not semantic

The pilot investigation recommended a semantic prefix (`wc-` for "writing cycle").
Rejected — the prefix, kept; the semantics, dropped. Reasons:

- **Semantic slugs rot.** Retitle the lesson and the prefix lies.
- **They don't guarantee uniqueness** across a 13-pathway matrix — two pathways
  could both plausibly claim `wc`.
- **They fight portability.** A structured key like `AWB-01` (Academic Writing /
  Introductory) reads nicely *until* the lesson is pulled into a bespoke suite that
  isn't academic-writing-introductory — then the prefix actively misleads. Portability
  means a lesson belongs to no fixed course, so its key must encode no course.

An opaque key belongs to the lesson, not to any course it currently sits in. The
cost is that `L07` tells you nothing on sight — paid for by a **registry** (below).

### Why gapped local numbers

The current content already uses 5-step spacing (`b-400`, `b-405`, `b-410`).
Keeping gaps means a block can be slotted between two others later without
renumbering neighbours or leaving an out-of-order tail. Sequential (`01, 02, 03`)
would be tidier on day one and more painful on every later edit.

### The lesson registry

A single registry file is the source of truth for key assignment:

`content/shells/lesson-registry.json`

```json
{
  "_latestKey": 2,
  "lessons": {
    "L01": { "title": "The writing cycle",       "pathway": "academic-writing", "tier": "introductory" },
    "L02": { "title": "Understanding the task",   "pathway": "academic-writing", "tier": "introductory" }
  }
}
```

The registry is the *only* place the human-readable mapping lives, so the ids
themselves can stay opaque and stable. Allocating a new lesson = increment
`_latestKey`, add an entry. Keys are never reused, even if a lesson is retired.

### Non-lesson page keys: `W-OPEN`, `W-CLOSE`, `SUMM`

Wrapper and summative pages use a different kind of key from the
lesson-key pattern above. `W-OPEN`, `W-CLOSE`, and `SUMM` are fixed,
non-sequential tokens — not allocated from the registry, not tracked by
`_latestKey`, and not entries in the `lessons` object. They recur
identically once per pathway-tier package (every tier has exactly one
`W-OPEN`, one `W-CLOSE`, one `SUMM`), rather than being globally unique
the way lesson keys are.

This is deliberate, not an oversight: per the "one SCORM package per
pathway-tier" packaging rule and the three-layer model (shell / context
slots / wrapper), a wrapper page is authored per pathway-tier and never
shared across tiers within one compiled package, so `W-OPEN` in one tier's
package and `W-OPEN` in another's never collide, unlike lessons, which are
deliberately built to be portable across bespoke course assemblies (see
"Why opaque, not semantic" above). If that portability assumption ever
changes for wrapper content specifically, this convention would need
revisiting — flagged as a watch-point, not assumed permanent.

Object ids within these pages still follow the
`<key>-<type>-<local-number>` pattern (e.g. `W-OPEN-b-05`), just with a
fixed key instead of a registry-allocated one.

---

## What travels with a lesson

A shell is only portable if everything it depends on travels with it or is
declared. Four categories:

1. **Its own objects** — the page/article/blocks/components JSON. Self-contained
   by the id convention; concatenation into a new course can't collide.
2. **Its assets** — namespaced by lesson key (`L01-writing-cycle.png`, not
   `writing-cycle-placeholder.png`) so two lessons' assets never clash in a
   shared `images/` folder. Assets live in the shell's `assets/` dir and are
   copied into the delivery course on assembly.
3. **Custom components** — e.g. `adapt-abbott-sortable`. The *plugin* is handled
   by the repo's component-tracking convention (committed under
   `src/components/adapt-abbott-*`); the shell's `manifest.json` **declares** the
   dependency so assembly can verify the plugin is present.
4. **Required globals** — e.g. the `_globals._components._sortable` aria labels in
   `course.json`. Declared in the shell manifest and merged into the delivery
   course's `course.json` on assembly.

### `manifest.json` shape

```json
{
  "lessonKey": "L01",
  "title": "The writing cycle",
  "pathway": "academic-writing",
  "tier": "introductory",
  "requiresComponents": ["adapt-abbott-sortable"],
  "requiresGlobals": ["_components._sortable"],
  "assets": ["L01-writing-cycle.png"]
}
```

---

## Extract / assemble path (specification, tooling deferred)

The tooling isn't built yet. This is what it will do, specified now so the
convention above is provably sufficient for it.

**Extract** (sandbox → shell): filter the sandbox course's five JSON files by
lesson-key prefix, writing the matching objects into a shell directory; copy the
lesson's assets in, renamed to the namespaced form; write the manifest.
Mechanical once ids are prefixed — that is the entire payoff of the convention.

**Assemble** (shells → delivery course): concatenate the selected shells' object
arrays into the delivery course's `contentObjects.json` / `articles.json` /
`blocks.json` / `components.json`; copy assets into the course's `images/`; then
two fix-up passes:

- **Reassign `_trackingId`.** These are course-global integers
  (`course.json._latestTrackingId`). Renumber sequentially from 1 across the
  assembled course. **Safe only under the condition below.**
- **Merge required globals** into the delivery course's `course.json`, de-duped.

Because ids are lesson-prefixed, the concatenation step **cannot collide** — no
coordination between independently-authored lessons is needed.

### `_trackingId` safety condition (write it down so it can't surprise us)

Renumbering `_trackingId` on assembly is free **only because** nothing in a lesson
*references* a tracking id from elsewhere — no `_assessmentId`, no quiz bank, no
spoor/tracking extension pointing at specific ids. The pilot satisfies this. **If
a future lesson adds an assessment or any feature that references tracking ids by
value, this assumption breaks** and reassignment must become reference-aware.
Any lesson introducing such a feature must flag it in its manifest.

---

## Definition of done for a shell

A lesson shell is portable-ready when:

- every object id carries the lesson key prefix (no bare `b-05`, no legacy
  `b-400`);
- local numbers restart per lesson and are gapped in 5s;
- no object references an id outside the lesson (the `_parentId` chain terminates
  at `course`, and no component points elsewhere);
- assets are namespaced by lesson key and listed in the manifest;
- custom-component and required-globals dependencies are declared in the manifest;
- the lesson has a registry entry.

If a lesson can't meet the "no outward references" line — because it genuinely
needs a cross-lesson assessment, say — that's a real exception to record openly,
not to paper over: it means the lesson is not independently portable and must be
assembled as part of a fixed group.

---

## Relationship to existing decisions

- **Three-layer model (shell / context slots / wrapper).** This doc defines the
  *shell* layer's on-disk form. Context slots are filled by context packs
  (`content/context-packs/`); the wrapper is authored per pathway-tier
  (`content/wrappers/`). A shell is context-neutral — the same shell is
  contextualised for criminology or sports journalism by applying a context pack,
  not by editing the shell.
- **One SCORM package per pathway-tier.** A delivery course assembled from shells
  is packaged as one SCORM zip per pathway-tier, per the packaging rule.
- **Each context delivered as a separate course.** A context pack applied to a set
  of shells produces one context-specific delivery course; different contexts are
  different courses assembled from the same shells.

---

## Wrapper structure (Wrapper Open / Wrapper Close)

*Added 16 July 2026, wrapper redesign session (open-decisions.md #24,
WR-1). Fleshes out the wrapper concept named above. The six-part flow
(above) operates *within* a lesson; the wrapper operates *around* lessons
at the pathway-tier level — distinct authoring layers, not to be
conflated at build time. This section is the structural detail; that
conceptual distinction was previously recorded only in
component-mapping-artefact.md's "Note on wrapper vs section flow," carried
here in substance so the reference does not dangle once that document
retires (MA-1, `docs/project/open-decisions.md`, 20 September 2026).*

The wrapper's two halves, **Wrapper Open** and **Wrapper Close** (internal/
authoring terms; learner-facing titles are a separate authoring choice),
bracket a pathway-tier's sub-lessons:

**Wrapper Open**, in order: (1) Overview & justification, why this
practice matters, academic-progression framing, voiced per §15.10; (2)
Signpost, pathway, tier, what's ahead, kept as its own block; (3)
Tier-level learning outcomes; (4) Confidence PRE.

**Wrapper Close**, following the tier's sub-lessons and its Summative
page, in order: (1) Confidence POST, referencing the fact that the
summative has just happened, not forward-pointing to it; (2) Tier summary,
referencing the tier's learning outcomes and suggesting further practice;
(3) References/resources section.

ID convention: `W-OPEN` / `W-CLOSE`, sitting outside the L-series
lesson-key registry (`content/shells/lesson-registry.json`).

Mandatory for a "pedagogically complete" tier — applies retroactively to
already-built tiers, not just new ones (open-decisions.md #24, WR-1e).

Full rationale and the confidence-mechanics detail: open-decisions.md
#24–25 (WR-1 through WR-2).

---

*End of design decision.*
