# Architecture - the component map

Where everything lives and what reads or writes what. Companion to
`docs/PIPELINE.md` (the conceptual flow) and `docs/RUNBOOK.md` (the commands).

## The three kinds of thing

1. **Stores** - the shared, versioned knowledge the pipeline reasons from.
2. **The manifest** - one per course; the append-only record of its decisions.
3. **Tools and skills** - the code and the conversation grammar that read the
   stores, write the manifest, and build the course.

---

## 1. Stores (shared, read-only during a build)

| Store | Holds |
|---|---|
| `design-kb/design-kb.gates.json` | **The 24 gates.** Each gate's id, phase, kind, hardness, sequence, dependencies, generation/response blocks, and the shape of its answer. The spine of Stage A. |
| `design-kb/design-kb.skeletons.json` | **The 6 page archetypes** and their fixed/variable slots. What the manifest maps onto. |
| `design-kb/design-kb.palette.json` | **The component palette** - every Adapt component a variable slot can be filled with (incl. the custom `adapt-abbott-*` set). |
| `design-kb/design-kb.activity-patterns.json` | **The pedagogy layer** - activity patterns, each with the slot-types it fits, the components that realise it, tier calibration and the content shapes it serves. Drives LES slot choices. |
| `design-kb/design-kb.content-shapes.json`, `.content-conventions.json`, `.tier-bands.json` | Supporting vocabularies: content shapes, authoring conventions, tier-band calibration. |
| `schemas/*.json` | JSON Schemas that validate the stores and the manifest. `course-design.schema.json` governs the manifest; `design-kb.gates.schema.json` governs the gate store. |
| `catalogue/pathways.json` + `catalogue/pathways/*.json` | The pathway **registry** - the 13 pathways (the theme axis), 3 tiers each, with pointers to the mapping doc. |
| `design-kb/design-kb.pathways.json` | **Layer-1 grounding (consolidated).** One resolved record per pathway: chapters in scope, the per-tier focus + voice band, and the book-map chunk ids tagged to the pathway (`primary` = sole tag, `shared` = co-tagged). Read at the generic content gates (crs-02/03/04, les-01, wra-*). Resolves the catalogue + mapping-doc + book-map hops into one lookup. |
| `source-kb/source-maps/book-excelling-at-university-2026.json` | The book **source-map** - the teachable content chunked and tagged by pathway with evidence quotes and locators. Source of truth for chunk text; the Layer-1 store references its chunk ids. |
| `reference/excelling-at-university.md` | The source book (primary grounding for agent gates). |
| `reference/excelling-voice-specification.md` | The authoritative voice contract. Apply its section 18 register check before any copy is done. |
| `tools/subject/`, `integrations/mapper/` | Subject vocabularies (CAH/HECOS) and the mapper profiles linking subjects, HESA codes and pathways. Used by CXS/CXP subject work. |

The gate store is the brain; the skeletons/palette/patterns are the building
blocks; the schemas keep everything honest.

---

## 2. The manifest (one per course, append-only)

`courses/<slug>/course-design_<slug>.json`, governed by
`schemas/course-design.schema.json`. Three top-level sections:

| Key | Holds | Written by |
|---|---|---|
| `gates[]` | `{gateId, records[]}`. Each record = `decidedValue` (the decision, any JSON) + provenance + grounding + state. **Append-only.** | every gate's `/land` |
| `phases[]` | `{phaseId, closedAt, bulkBlessing}` | phase close |
| `instantiations[]` | `{pageKey, pageType, archetype, slotChoices[]}` - which component filled each archetype slot on each page, with its context-coupling | `/scaffold` + the LES/WRA gates |

Rule: the manifest is **append-only**. The only exception is `/new-course`,
which creates it. `/reopen` adds a sweep event; it never rewrites history.

---

## 3. Tools (the code)

### Stage A - consult & specify
| Tool | Role |
|---|---|
| `tools/new-course.js` | Cold-start: writes a new manifest from the four closed ONB answers. |
| `tools/gate-order.js` | Computes gate order and the closure set for a phase. |
| `tools/phase-confirm.js` | Validates a just-written record against the schema, then renders the read-back. |
| `tools/render-course-spec.js` | Renders the readable course spec (`adp-course-design-specification_<slug>.md`) from the gate store + manifest. |

### Stage A to B hinge
| Tool | Role |
|---|---|
| `tools/generate-course-shell.js` | **The scaffold.** Fuses manifest + archetypes into the Adapt content model (`config.json` + `en/*.json`), one page per lesson, deferred blocks for interior slots. |

### Stage B - build
| Tool | Role |
|---|---|
| `merge-context.js` (root) | The CXP merge step: slots context-pack prose into components marked for coupling. |
| `tools/build-course-pack.js`, `tools/build-all-packages.js` | Materialise a shell + context pack pair and drive the SCORM build. |
| `package-scorm.js` (root) | Zip `build/` into a traceable SCORM package. |
| `grunt` (`Gruntfile.js`, `grunt/`) | The Adapt build itself: `grunt build` compiles `src/course` into `build/`. |

### Quality gates (run throughout, especially Stage C)
| Tool | Checks |
|---|---|
| `tools/verify-course.js`, `tools/verify-all-courses.js` | Referential integrity of a course's content model. |
| `tools/manifest-completeness.js` | Whether the manifest is complete enough to build (reports; does not gate). |
| `tools/validate-design-schemas.py` | Validates stores and manifests against the schemas. |
| `voice-lint.js` (root) | Checks copy against the voice spec's pattern rules. |
| `tools/conformance-lint.js` | Adapt content-model conformance. |
| `test-browser-checklist.mjs`, `test-accessibility-scan.mjs`, `test-focus-sequence-scan.mjs` | Playwright walkthrough, axe-core WCAG scan, focus-order scan against a local server. |

---

## 4. Skills (the conversation grammar)

In `.claude/commands/`. These drive Stage A and the authoring half of Stage B.

| Skill | Mode | Does |
|---|---|---|
| `/gate` | read-only (plan) | opens one gate: shows the proposal and the draft record |
| `/land` | execute | writes one confirmed gate record and, for content gates, its Adapt content |
| `/new-course` | execute | creates a course's manifest (once, after ONB) |
| `/scaffold` | execute | builds the shell from the manifest (once, after CRS) |
| `/new-context` | execute | authors a context pack for an existing closed course (CXP) |
| `/cxp-open` | execute | opens the CXP phase for a course |
| `/ledger` | read-only | shows the standing ledger for a course from its manifest |
| `/phase-draft` | read-only (plan) | drafts a whole phase's soft/advisory gates in one sitting |
| `/reopen` | execute | reopens a closed gate and sweeps its dependents |

The `reviewer` agent (`.claude/agents/reviewer.md`) is a read-only second reader,
invoked after a `/land` or `/new-context` write and before staging. It checks
claims against files and never edits.

---

## 5. The Adapt build harness

| Path | What |
|---|---|
| `src/components/adapt-abbott-*` | 12 custom components (confidence, sortable, hotspot, glossary, timeline, tabs, flipcard, branching, annotated, opentext, references, checklist). |
| `src/extensions/adapt-abbott-*` | 3 custom extensions (pass-reveal, reflective-store, resultsdebrief). |
| `adapt.json` | The contrib-plugin manifest: what `adapt install` pulls in. |
| `patches/` + `scripts/apply-vendor-patches.js` | Local vendor bug-fixes, reapplied after every install. |
| `grunt/`, `Gruntfile.js` | The build. |

Core, menu, theme and all `adapt-contrib-*` plugins are **installed**, not
vendored: run `npm run adapt-install` (never raw `adapt install`, which wipes the
patches). See RUNBOOK.

---

## Data flow, end to end

```
 stores (gates, skeletons, palette, patterns; pathways store + book map = Layer-1 grounding)
        │  read by
        ▼
 /gate + /land ──► MANIFEST (course-design_<slug>.json)      [Stage A]
        │                       │
        │  ONB/CRS closed       │ read by
        ▼                       ▼
 /scaffold ──────────────► config.json + en/*.json (shell)   [Stage B]
                                │  deferred slots filled by
                                ▼
                         /land (LES, WRA)  +  merge-context.js (CXP)
                                │  compiled by
                                ▼
                         grunt build ──► build/               [Stage B]
                                │  verified + zipped by
                                ▼
          verify/lint + package-scorm.js ──► scorm-packages/  [Stage C]
                                │  uploaded by
                                ▼
                             Moodle (manual)
```
