# Component Candidates Register

*A durable backlog of Adapt components/plugins worth considering for the programme, with evaluation status. Purpose: capture ideas so they're not lost, and record outcomes as each is assessed — so a decision made once isn't re-litigated later.*

**Governing principle:** need before tool. Nothing here is a shopping list. A candidate is only built/installed when a lesson's design actually calls for it. Every candidate must pass, in order: (1) Adapt framework 5.56.2 compatibility, (2) schema-check, (3) pedagogical fit — before adoption. This is the discipline that caught the narrative image requirement and rejected the dead 2017 sorting plugin.

**Status values:** `idea` (noted, not yet needed) · `evaluating` · `adopted` · `built-own` · `rejected` (with reason) · `deferred`.

---

## Adopted / built

| Component | For | Status | Notes |
|---|---|---|---|
| **Sorting / sequencing** | Ordering tasks (writing-cycle stages; recurs in research stages, reflective models, revision) | **built-own** → `adapt-abbott-sortable` | No v5-compatible community plugin existed (the only candidate was an unmaintained 2017 plugin — see rejected). Built our own, fully accessible (drag + keyboard + ARIA). First use: lesson 1 writing-cycle stages, replacing the matching workaround. |
| **Flip cards** | Paired reveal cards (term→definition, prompt→explanation, image→description); self-paced concept exploration | **built-own** → `adapt-abbott-flipcard` | No community plugin with v5 compatibility and the needed visitation-completion model. Built our own (31 July 2026): each card is a native `<button>` with `aria-expanded`, keyboard Enter/Space toggles, both faces in DOM with `aria-hidden` swap, CSS 3D flip with prefers-reduced-motion fallback. Completion by visitation (all cards flipped at least once). Two flip behaviours: `independent` (default, multiple cards open) and `single` (one at a time, auto-closes others). 24 unit tests via Node built-in runner. Authoring spec: `component-specs/flipcard.md`. |
| **Timeline** | Vertical ordered-process display for Signpost process overviews and temporal content | **built-own** → `adapt-abbott-timeline` | No community plugin with v5 compatibility and the needed ordinal (non-scalar) model. Built our own (31 July 2026): `<ol>/<li>` structure with sequence semantics, each stage marker is a native `<button>` with `aria-expanded` and `aria-controls`, vertical axis as CSS pseudo-element, prefers-reduced-motion fallback. Completion by visitation (all stages expanded at least once). Two expand behaviours: `single` (default, one at a time) and `independent`. 25 unit tests via Node built-in runner. Authoring spec: `component-specs/timeline.md`. |
| **Branching** | Self-contained decision-scenario for "what would you do?" interactions; 2–4 choices revealing consequences | **built-own** → `adapt-abbott-branching` | No existing component for in-place decision-consequence reveal (adapt-contrib-branching is a page-flow extension). Built our own (1 August 2026): choices as native `<button>`s in `role="group"`, `aria-pressed` for selection state, `aria-disabled` (not `disabled`) on commit-locked unchosen buttons to keep them in tab order, consequence region with `aria-live="polite"`. Completion by visitation on FIRST selection (any-true override). Two selection behaviours: `commit` (default, one choice locked) and `explore` (try multiple). 30 unit tests via Node built-in runner. Authoring spec: `component-specs/branching.md`. |
| **Tabs** | Tabbed-panes component for organising parallel content into selectable panels | **built-own** → `adapt-abbott-tabs` | cgkineo/adapt-tabs was archived and missing Home/End keys. Built our own (1 August 2026): full WAI-ARIA tabs pattern with `role="tablist"`/`role="tab"`/`role="tabpanel"`, roving tabindex, automatic activation, Left/Right/Home/End keyboard navigation with wraparound. Completion by visitation (all tabs visited). 28 unit tests via Node built-in runner. Authoring spec: `component-specs/tabs.md`. |
| **Annotated** | Annotated-passage component for exemplar analysis with inline phrase-level commentary | **built-own** → `adapt-abbott-annotated` | No existing component for inline text annotation with accessible markers. Accessibility recon found `aria-details` has unverified AT support and WAI-ARIA Annotations roles are still 1.3 draft — used proven footnote/disclosure pattern instead. Built our own (2 August 2026): passage renders as continuous prose with underlined annotated segments; marker buttons with `aria-expanded`/`aria-controls`; single shared note region with `aria-live="polite"`; focus management (to region on expand, back to marker on close). Completion by visitation (all notes opened). 23 unit tests via Node built-in runner. Authoring spec: `component-specs/annotated.md`. Note: this component was never a register candidate — it originates from the 2 August 2026 design session as a direct build, not evaluation of an existing candidate. |
| **Glossary** | Glossary-passage component for inline term definitions within teaching prose | **built-own** → `adapt-abbott-glossary` | No existing component for inline-term marking with disclosure definitions. Built our own (2 August 2026): teaching prose with dotted-underline term markers; marker buttons with `aria-expanded`/`aria-controls`; single shared definition region with `aria-live="polite"`; focus management (to region on expand, back to marker on close); accessible name "Definition of: [term]". Completion by visitation (all terms opened). JSON Schema draft-04 minItems:2 on passage; 2–8 term bound runtime-warned (cannot be schema-enforced). 30 unit tests via Node built-in runner. Authoring spec: `component-specs/glossary.md`. Three-way routing rule documented in `design-kb/design-kb.palette.json`'s `palette/glossary` config notes (moved from the now-superseded component-mapping-artefact.md, MA-1). Note: this component was never a register candidate — it originates from the 2 August 2026 design session as a direct build, not evaluation of an existing candidate. |
| **Checklist** | Working-aid checklist component for concrete tickable actions (pre-submission, rehearsal, revision-readiness) | **built-own** → `adapt-abbott-checklist` | No existing component for a reusable working-aid checklist with ephemeral tick state. Built our own (2 August 2026): native `<input type="checkbox">` with `<label htmlFor>` for each item; `<fieldset>/<legend>` grouping; IDs derived from component `_id` for cross-instance safety; progress count with `aria-live="polite"`. Key contract: tick state resets on revisit (CL-2), completion persists once all items ticked (CL-3/4). 4–8 items schema-enforced. 31 unit tests via Node built-in runner. Authoring spec: `component-specs/checklist.md`. Routing boundary vs confidence documented in `design-kb/design-kb.activity-patterns.json`'s `action-checklist` recognition text (moved from the now-superseded component-mapping-artefact.md, MA-1). Note: this component was never a register candidate — it originates from the 2 August 2026 design session as a direct build, not evaluation of an existing candidate. |
| **Open Text** | Free-text reflection or note-taking; no correct answer, no marking — "Mark as complete" only; freely editable; sticky completion | **built-own** → `adapt-abbott-opentext` | Built on probe/scorm-2004 branch (30–31 July 2026), merged to master 13 August 2026. Two variants: `reflection` (default, may be completion-bearing) and `notes` (general note-taking, never completion-bearing). Persists learner text via `adapt-abbott-reflective-store` extension using SCORM 2004 suspend_data custom keys (RTR-1 fix). Authoring spec: `component-specs/opentext.md`. Note: diverges from the original candidate idea (model answer revealed on submit) — that capability is a separate planned component (model-answer reveal), design-complete, unblocked by this merge. |
| **Hotspot** | Graded image-region-selection question: learner selects one or more labelled rectangular regions on an authored image | **built-own** → `adapt-abbott-hotspot` | No existing component for graded region-selection on an image with native-input accessibility. Built our own (20 September 2026): 2–8 rect regions positioned by percentage, real radio/checkbox inputs inside `fieldset`/`legend`, regions invisible until hover/keyboard-focus/after-submission, list-mode fallback below a 44×44px rendered-region threshold. Built on `ItemsQuestionModel`/`QuestionView` with zero overrides to attempts, marking, model-answer, or SCORM "choice" interaction recording — same base as mcq/gmcq. Logic module (`hotspotLogic.js`) unit-tested (27 tests) as an independent mirror of the inherited marking path, not a second live code path — see `component-specs/hotspot.md` §7 for this and the region-validation-not-wired-in gap. Authoring spec: `component-specs/hotspot.md`. Note: diverges from the original candidate idea below, which named video as well as image; only the image half was built — video-region support is not addressed by this component. |
| **ab-hotgraphic** | Reusable inline-SVG hotspot diagram: interactive labelled diagram rebuilt so the SVG is parsed and injected into the DOM rather than shown via `<img>`, so hover/focus and the `--ab-*` theme cascade apply to individual hotspot regions | **built-own** → `adapt-ab-hotgraphic` | Replaces the stock `hotgraphic` component (row below) for diagrams needing live interactive paint. Interface layer: `_diagram.src` (inlined SVG) plus a per-item `_hotspot` binding (`{_id\|_selector, _action}`) resolved against `data-ab-hotspot`/id/explicit-selector in the SVG, so a new diagram costs a theme-level token block (`src/extensions/adapt-ab-theme/less/ab-hotgraphic.less`) rather than new component code. SVG id-namespacing, childless-mount-point React strategy, and `setReadyStatus()`-in-`finally` load are documented in `component-specs/ab-hotgraphic.md` §7. First use: the ULAF learning/assessment/feedback cycle diagram (`ulaf-cycle.svg`) in the Understanding Learning, Assessment and Feedback course's W-OPEN signpost, replacing the stock `hotgraphic` instance there. Authoring spec: `component-specs/ab-hotgraphic.md`. |
| **hotgraphic** (core) | Interactive labelled diagram | adopted | Writing-cycle diagram (lesson 1). Note: requires a per-pin image (use `hide-popup-image` for text-only pins). |
| **accordion** (core) | Stepped reveal without images | adopted | Lesson 2 worked example. The clean text-only stepped option (narrative requires images). |
| matching, mcq, textInput (core) | Standard question types | adopted | In use across the pilot lessons. |

---

## Candidates worth evaluating (when a lesson calls for one)

Ranked by likelihood of genuine need in this programme.

| Component | What it does | Likely pathways | Status | Priority |
|---|---|---|---|---|
| ~~**Open Text Input**~~ | ~~Free-text reflection/notes (original idea included model-answer reveal; built version diverges — see Adopted section)~~ | ~~Reflection-heavy pathways~~ | **built-own** | Moved to Adopted/built section (13 August 2026). |
| ~~Timeline~~ | ~~Chronological / sequential process display~~ | ~~Researching (9), Reflective Practice (10), and process content generally~~ | **built-own** | Moved to Adopted/built section (31 July 2026). |
| ~~Branching~~ | ~~Decision-scenario for "what would you do?" interactions~~ | ~~Presenting (7), Reflective Practice (10), Work-Based Learning (11)~~ | **built-own** | Moved to Adopted/built section (1 August 2026). |
| ~~Tabs (enhanced)~~ | ~~Tabbed content panels~~ | ~~Any content-dense lesson~~ | **built-own** | Moved to Adopted/built section (1 August 2026). |
| ~~Flip cards~~ | ~~Two-sided reveal cards~~ | ~~Revising & Exams (8) — term/definition recall~~ | **built-own** | Moved to Adopted/built section (31 July 2026). |
| **Confidence slider** | Learner rates confidence alongside an answer | Any formative/self-assessment beat | `idea` | Low — nice-to-have, not core. |
| ~~**Interactive video / hotspot**~~ | ~~Clickable regions on video/image~~ | ~~Media-rich lessons~~ | **built-own** | Moved to Adopted/built section (20 September 2026), image half only — see that row's note on the video-support divergence. |

---

## Rejected

| Component | For | Reason |
|---|---|---|
| **adapt-sortable** (danielstorey, 2017) | Ordering | 8 years old, no v5 update; Adapt v5's breaking changes (BEM/SMACSS, rem units) require updates it never received. Failed the compatibility gate. Led to building `adapt-abbott-sortable` instead. |

---

## Structure / tracking extensions (course-wide, not teaching components)

| Extension | Does | Status |
|---|---|---|
| **PageLevelProgress** (core) | Per-page/component progress indicators | in use (note: interacts fussily with custom components — see the sortable per-item-indicator fix) |
| trickle (core) | Gates content sequence | in use (available; optional per lesson) |
| spoor (core) | SCORM tracking | in use (the delivery mechanism) |
| Bookmarking | Returns learner to last position | `idea` — quality-of-life; consider before wider rollout |
| **Assessment** (core, `adapt-contrib-assessment`) | Article-level assessment container; scoring; attempts | in use — wraps question components for summative/formative assessment; enables SCORM score reporting (moved here from `component-mapping-artefact.md`'s retiring "Installed Extensions" table, MA-1) |
| **Tutor** (core, `adapt-contrib-tutor`) | Feedback popup handler | in use — displays question feedback in an overlay so it is noticed (moved here from `component-mapping-artefact.md`'s retiring "Installed Extensions" table, MA-1) |
| **adapt-abbott-pass-reveal** | Enables model-answer display on assessment questions only after pass | **built-own** — prevents answer-grinding before demonstrating competence. Config: `_passReveal._isEnabled`, `_assessmentIds[]`. Listens `assessments:complete` + `assessment:restored`; guard chain (enabled→ID match→isPass). First use: SUMM-a-01 in Academic Writing: Introductory Stage. Authoring spec: `extension-specs/passreveal.md`. |
| **adapt-abbott-resultsdebrief** | Post-assessment study-plan debrief; groups incorrect answers by lesson | **built-own** — renders "Where to focus next" section after assessment completion, grouping incorrect answers by lesson (deduplicated) with remediation pointers, plus pass-reveal note on pass. Config: `_resultsDebrief._isEnabled`, `_assessmentId`, `_items[]` (question-to-lesson mappings). Listens `assessments:complete` + `assessment:restored` + `componentView:postRender`. First use: SUMM-a-01 in Academic Writing: Introductory Stage (8 question mappings). Authoring spec: `extension-specs/resultsdebrief.md`. |

---

## Known gaps (no component, no plan)

Real gaps this register has no answer for yet — recorded so a retiring source document
doesn't take the finding with it (MA-1).

| Gap | Description | Notes |
|---|---|---|
| **Peer assessment** | No native Adapt component for a structured peer-assessment task; the only current workaround is `textInput`/`opentext`, which has no peer-review or cross-learner mechanism at all. | Stated twice in `component-mapping-artefact.md` before its retirement (its Part 1 "Known Gaps" and end-section "Gaps" table both name the same finding). No candidate component has been identified and no plan exists to build or adopt one — this is a "not built, no plan" entry, not an `idea` awaiting evaluation. |
| **Long-form word-count guidance** | No component or convention gives a learner a live word-count target for long-form reflective writing. `opentext`'s `_maxCharacters` is a hard cap enforced at the character level, not word-count guidance. | Stated in `component-mapping-artefact.md`'s end-section "Gaps" table before its retirement; Prompt 129's disposition pass found no evidence it has been resolved. Carried here as a still-real, unaddressed gap, not independently re-verified this sitting. |

---

## How to use this register

1. When a lesson's paper design calls for an interaction the core set can't do, check here first — it may already be evaluated (adopted, built, or rejected-with-reason).
2. If it's an `idea`, move it to `evaluating`: compatibility-check (5.56.2) → schema-check → pedagogical fit. Record the outcome here (`adopted` / `built-own` / `rejected` + reason).
3. Never install speculatively. Each plugin is compiled into every build and adds schema surface; on the AVX-less box, a lean plugin set keeps `grunt build` clean.
4. Prefer core components, then a compatible community plugin, then build-own only when nothing fits and the need recurs (the sorting decision followed exactly this ladder).
