---
title: Gate system (ONB -> CXP)
source: design-kb/design-kb.gates.json
kbVersion: 0.10.1
gates: 24
phases: [ONB, CXS, CRS, LES, WRA, CXP]
note: Generated from design-kb.gates.json by scratchpad/gate-to-md.js — do not hand-edit; regenerate.
---

# Gate system (ONB -> CXP)

**Phase flow:** ONB → CXS → CRS → LES → WRA → CXP

## Pipeline — where the gates point (decisions -> files)

The gates do not build anything directly; each writes a decision, and the decisions
drive three artifacts in turn.

1. **ONB** (onb-01..onb-04) answered, then `/new-course` writes the **manifest**
   `courses/<slug>/course-design_<slug>.json` (`facetSet{pathway,tier}` + first records).
2. **CXS** (reserved) — auto-passes; writes nothing live except `cxs-04` referencing
   (the token source CXP inherits).
3. **CRS** (crs-01..crs-05) — more manifest records (sources, thematic scope + strands,
   course outcomes + banks, lesson map, course-spec rollup).
4. **SCAFFOLD** — `tools/generate-course-shell.js` reads the manifest -> the **shell**
   `courses/<slug>/config.json` + `en/*.json` (pages / articles / blocks / components).
5. **LES** (les-01, per lesson) — interior + activities + per-slot coupling, authored into
   the shell's lesson slots.
6. **WRA** (wra-01..wra-04; wra-03/04 run post-scaffold) — wrapper content, SUMM items, and
   the C-PRE / C-POST confidence components, authored into the shell.
7. **CXP** (cxp-01..cxp-04, per subject) — the **context pack**
   `content/context-packs/<subject>/<slug>/<page>.json` (`generatedProse` / `generatedItems`).
8. **MERGE** — `merge-context.js --context=<subject> --tier=<slug>` overlays the pack into
   the shell -> the **variant** `courses/_generated/<slug>-<subject>/`.
9. **BUILD** — `grunt build` -> `build/` -> `package-scorm.js` -> `scorm-packages/`.

Within the gates, "**Feeds**" below is the forward edge: which later gates consume this
gate's decision.

## ONB — Onboarding

### Theme preset  `onb-01_theme-preset`

```yaml
id: onb-01_theme-preset
name: Theme preset
phase: ONB
sequence: 0
decider: human
hardness: hard-stop
prompt: Use a theme-preset? (e.g. academic-practice-pathways, or none)
produces: preset
dependsOn: []
feeds:   # where this gate's decision points
  - onb-02_course-theme
```

A7-round: optional. A preset bundle (academic-practice-pathways first) scopes onb-02's themes and pre-loads crs-01_sources (assumed-approved, amendable). 'none' = fully custom path.

### Course theme  `onb-02_course-theme`

```yaml
id: onb-02_course-theme
name: Course theme
phase: ONB
sequence: 1
decider: agent+human
hardness: hard-stop
prompt: "Select the course theme (preset: a defined pathway; no preset: give a one-sentence topic area for the agent to shape)."
produces: decidedValue.theme
dependsOn:
  - onb-01_theme-preset (constitutive)
feeds:   # where this gate's decision points
  - onb-03_pitch
  - onb-04_naming
  - crs-01_sources
```

Preset chosen -> dropdown of that preset's themes (academic-practice-pathways: the 13, soon 14, pathways). No preset -> user gives a one-sentence topic area, agent turns it into the theme, user confirms.

### Pitch  `onb-03_pitch`

```yaml
id: onb-03_pitch
name: Pitch
phase: ONB
sequence: 2
decider: agent+human
hardness: hard-stop
prompt: Choose the tier (pitch), grounded in what that tier means for this pathway against the book.
produces: decidedValue.pitch
dependsOn:
  - onb-02_course-theme (constitutive)
feeds:   # where this gate's decision points
  - onb-04_naming
```

The tier band, now a grounded choice (tier-bands + the pathway reference's tierStatements/capabilities + the book window from bookGrounding) rather than a blind enum. Flows into manifest.facetSet.tier, which keys the Layer-1 pathway grounding every downstream content gate reads. Indicative FHEQ levels per design-kb.tier-bands.json (indicativeLevels are not a progression). no-tier tooling not yet wired. Future per-level targeting lives in cxs-01 (institutional).

### Naming  `onb-04_naming`

```yaml
id: onb-04_naming
name: Naming
phase: ONB
sequence: 3
decider: agent+human
hardness: hard-stop
prompt: Confirm (or amend) the proposed course name and slug.
produces: decidedValue.slug + display name
dependsOn:
  - onb-02_course-theme (constitutive)
  - onb-03_pitch (constitutive)
feeds: []   # terminal / consumed at scaffold or build
```

Agent derives course name + slug from theme + pitch; on confirm, tooling creates the folder and answer-sheet file. No files can be created until answered. (Carries old crs-03_vocabulary shape.)

## CXS — Context setup (reserved)

### Institutional context  `cxs-01_institutional-context`

```yaml
id: cxs-01_institutional-context
name: Institutional context
phase: CXS
sequence: 4
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Reserved: future institutional/module process (the plug point for a module's own framing, and future per-level targeting). Auto-passes 'none'.

### Subject context  `cxs-02_subject-context`

```yaml
id: cxs-02_subject-context
name: Subject context
phase: CXS
sequence: 5
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Reserved: future human CAH 1-3 grouping select, which parameterises the agent source sweep. Auto-passes 'none'.

### Qualifiers  `cxs-03_qualifiers`

```yaml
id: cxs-03_qualifiers
name: Qualifiers
phase: CXS
sequence: 6
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Reserved: future human select (<=3 from docs/authoring/qualifier-list-2026-10-04.md). Auto-passes 'none'.

### Referencing style  `cxs-04_referencing-style`

```yaml
id: cxs-04_referencing-style
name: Referencing style
phase: CXS
sequence: 7
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Referencing is ALWAYS set here. Auto-passes the default 'Harvard (Cite Them Right)'; this is the token source CXP inherits (referencing = token-substitution coupling). The one CXS gate with a live default, not 'none'.

### External standards  `cxs-05_external-standards`

```yaml
id: cxs-05_external-standards
name: External standards
phase: CXS
sequence: 8
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Reserved: future human select; fed by the standing benchmark/standards corpus. Auto-passes 'none'.

### Resources drawer  `cxs-06_resources`

```yaml
id: cxs-06_resources
name: Resources drawer
phase: CXS
sequence: 9
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Reserved: the course's resources drawer (course.json _resources). The old A7 resources gate has no live counterpart in the six-phase model; kept here as a reserved placeholder for a future process, auto-passes 'none'. Added 8 October 2026 (Abbott: keep a reserved gate for the resources drawer, in CXS). While reserved it writes nothing; the shell ships the adapt-contrib-resources extension at its own default until a live process fills this gate.

## CRS — Course structure

### Sources  `crs-01_sources`

```yaml
id: crs-01_sources
name: Sources
phase: CRS
sequence: 10
decider: human
hardness: hard-stop
prompt: Name the themed source set the agent searches (book default; add/remove).
produces: sources
dependsOn:
  - onb-02_course-theme (constitutive)
feeds:   # where this gate's decision points
  - crs-02_thematic-scope
```

After theme+pitch. Points the agent at the theme's pathway doc-set (core + source-map + adapt-integration) and the book (default). Preset pre-loads assumed-approved (amend/remove); no preset -> user supplies, or agent suggests if theme matches the library. Feeds every agent search (CRS, LES, CXP). Standing benchmark corpus is always-on in addition.

### Thematic scope  `crs-02_thematic-scope`

```yaml
id: crs-02_thematic-scope
name: Thematic scope
phase: CRS
sequence: 11
decider: agent+human
hardness: hard-stop
prompt: Confirm/amend the thematic scope and the 5-10 thematic strands (regenerate with steer available).
produces: decidedValue (scope + subThemes)
dependsOn:
  - crs-01_sources (constitutive)
feeds:   # where this gate's decision points
  - crs-03_course-outcomes
  - crs-04_lesson-map
  - les-01_lesson-proposal
sourceConsultation:
  triggeringFacets: [level]
  authorityLevels: [sector]
```

Chapters/sections in scope, tier-band window, prior-experience anchor, + 5-10 thematic strands (candidate lesson topics). Most consequential upstream gate. Strands: human approve/amend/remove/regenerate.

### Course outcomes  `crs-03_course-outcomes`

```yaml
id: crs-03_course-outcomes
name: Course outcomes
phase: CRS
sequence: 12
decider: agent+human
hardness: hard-stop
prompt: Confirm/amend the 3-5 course outcomes and their confidence statements + measuring MCQs.
produces: decidedValue (courseOutcomes + courseOutcomeBanks)
dependsOn:
  - crs-02_thematic-scope (constitutive)
feeds:   # where this gate's decision points
  - crs-04_lesson-map
  - wra-01_wrapper-open
  - wra-02_wrapper-close
  - wra-03_summative
  - wra-04_confidence
```

3-5 course outcomes (3 default; reason if 4-5). Also produces, per outcome at CRS, a confidence statement + 3 general MCQ sets (courseOutcomeBanks) used on the SUMM page (OBK-1). Lesson-outcome banks are produced later at les-01.

### Lesson map  `crs-04_lesson-map`

```yaml
id: crs-04_lesson-map
name: Lesson map
phase: CRS
sequence: 13
decider: agent+human
hardness: hard-stop
prompt: Agree the lesson map; per lesson approve/amend/reject+regenerate; add/remove lessons.
produces: decidedValue (lessons + progression)
dependsOn:
  - crs-03_course-outcomes (constitutive)
  - crs-02_thematic-scope (constitutive)
feeds:   # where this gate's decision points
  - crs-05_course-spec
  - les-01_lesson-proposal
  - wra-01_wrapper-open
  - wra-02_wrapper-close
  - wra-03_summative
```

Per lesson: key, title, topic, brief description, lesson outcomes, source section(s); + cross-lesson progression. Last CRS step before the course spec. Feeds the course pack. (Carries old gates/A3 shape; lesson outcomes folded in from old B1.)

### Course spec  `crs-05_course-spec`

```yaml
id: crs-05_course-spec
name: Course spec
phase: CRS
sequence: 14
decider: agent+human
hardness: advisory
prompt: ""
produces: the course spec / user-facing course pack (render-doc)
dependsOn:
  - crs-04_lesson-map (constitutive)
feeds: []   # terminal / consumed at scaffold or build
```

Auto-stands rollup of ONB+CRS -> user-facing course pack (tools/doc-templates/course-pack.template.json). Order: Identity -> Context shell -> Thematic scope -> Thematic strands -> Course outcomes -> per-outcome -> Lesson map. No new decisions.

## LES — Lessons (per lesson)

### Lesson proposal  `les-01_lesson-proposal`

```yaml
id: les-01_lesson-proposal
name: Lesson proposal
phase: LES
sequence: 15
decider: agent+human
hardness: soft
repeatsPer: lesson
prompt: "Confirm/amend the lesson's interior design and activities (regenerate+steer available)."
produces: "the lesson's interior design + activities"
dependsOn:
  - crs-04_lesson-map (constitutive)
  - crs-02_thematic-scope (substantive)
feeds:   # where this gate's decision points
  - cxp-04_context-generation
procedureFlags: [varietyView, candidates]
sourceConsultation:
  triggeringFacets: [activity]
  authorityLevels: [institutional]
```

One consolidated per-lesson gate (A6.2): interior design (knowledge/interactivity, worked example, pacing, visuals) + activities (formative check, reflective prompt, 3 interactivity proposals) + per-slot coupling marking. NO confidence (course-level, C-PRE/C-POST fed by crs-03). Outcomes are set at crs-04, not here. Merges old B2-B7 and crs-06 lessonOutcomeBanks.

## WRA — Wrap

### Wrapper open  `wra-01_wrapper-open`

```yaml
id: wra-01_wrapper-open
name: Wrapper open
phase: WRA
sequence: 16
decider: agent+human
hardness: soft
prompt: Confirm/amend wrapper-open content.
produces: wrapper-open content
dependsOn:
  - crs-03_course-outcomes (constitutive)
  - crs-04_lesson-map (constitutive)
feeds:   # where this gate's decision points
  - cxp-04_context-generation
procedureFlags: [candidates]
```

Overview, learning-outcomes, practice-connection (academic/professional framing; human sets the academic<->professional extent; academic + professional sections each optionally removable), signpost component (old les-02 visual-overview), course-instructions, course-conventions. Wrapper-page coupling degree set here (A6.3).

### Wrapper close  `wra-02_wrapper-close`

```yaml
id: wra-02_wrapper-close
name: Wrapper close
phase: WRA
sequence: 17
decider: agent+human
hardness: soft
prompt: Confirm/amend wrapper-close content.
produces: wrapper-close content
dependsOn:
  - crs-03_course-outcomes (constitutive)
  - crs-04_lesson-map (substantive)
feeds:   # where this gate's decision points
  - cxp-04_context-generation
procedureFlags: [candidates]
```

Summary, practice-connection, where-next (vertical = tier ladder; horizontal = related pathways/themes/subjects; agent proposes + confirm), course-references. Wrapper-page coupling degree set here (A6.3).

### Summative assessment  `wra-03_summative`

```yaml
id: wra-03_summative
name: Summative assessment
phase: WRA
sequence: 18
decider: agent+human
hardness: soft
prompt: "Confirm/amend the summative question stems drafted from crs-03's MCQ-set specs."
produces: SUMM assessment-items (real MCQ/sortable question stems)
dependsOn:
  - crs-03_course-outcomes (constitutive)
  - crs-04_lesson-map (substantive)
feeds:   # where this gate's decision points
  - cxp-04_context-generation
procedureFlags: [candidates]
```

Post-scaffold authoring of SUMM's assessment-items: crs-03's 3 mcqSet specs per outcome become real question stems (palette/mcq or palette/sortable, SM-2 split). AL-3: each course outcome tested by exactly two summative questions; AL-6 tests. A set whose crs-03 coupling is not shell-coupled is left as a marked slot for cxp-04 to fill per subject. Added 8 October 2026 (Abbott: post-scaffold summative/confidence authoring, two gates in WRA).

### Confidence statements  `wra-04_confidence`

```yaml
id: wra-04_confidence
name: Confidence statements
phase: WRA
sequence: 19
decider: agent+human
hardness: soft
prompt: Confirm/amend the confidence statements placed into the C-PRE and C-POST pages.
produces: C-PRE confidence-pre + C-POST confidence-post components
dependsOn:
  - crs-03_course-outcomes (constitutive)
feeds: []   # terminal / consumed at scaffold or build
```

Post-scaffold placement of crs-03's per-outcome confidence statements into the C-PRE confidence-pre and C-POST confidence-post components (palette/confidence). AL-4: each statement rates its course outcome; every course outcome carries at least one. The same statement set brackets the course (C-PRE before lessons, C-POST at close). Added 8 October 2026 (Abbott: two gates in WRA).

## CXP — Context pack (per context)

### Subject  `cxp-01_subject`

```yaml
id: cxp-01_subject
name: Subject
phase: CXP
sequence: 20
decider: human
hardness: hard-stop
repeatsPer: context-pack
prompt: Set the subject for this context pack (CAH/HECOS).
produces: subject
dependsOn: []
feeds:   # where this gate's decision points
  - cxp-04_context-generation
```

Per-pack subject. PRIMARY agent lookup = that subject's interpreted benchmark statements (standing corpus), never the copyrighted originals. BASELINE OPTION: 'baseline' is a valid selection; it routes the cxp-04 lookup to the universal reference (the generic shared-core standards in catalogue/context/subject/benchmarks/universal-reference.json) instead of a single subject's benchmark. Record it as subject {scheme:'baseline', code:'baseline', label:'baseline'}, with the resolved benchmark id (universal-reference) in the record's grounding. resolve-subject-benchmark.js returns this for inputs baseline/universal/generic/none.

### Qualifiers  `cxp-02_qualifiers`

```yaml
id: cxp-02_qualifiers
name: Qualifiers
phase: CXP
sequence: 21
decider: human
hardness: hard-stop
repeatsPer: context-pack
prompt: Set up to three qualifiers for this pack (default none).
produces: qualifiers
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

Per-pack qualifiers (<=3 across categories, default none) from docs/authoring/qualifier-list-2026-10-04.md.

### Exemplar programmes  `cxp-03_exemplar-programmes`

```yaml
id: cxp-03_exemplar-programmes
name: Exemplar programmes
phase: CXP
sequence: 22
decider: auto
hardness: advisory
reserved: true
prompt: Reserved — auto-passes; not opened interactively.
produces: programmes
dependsOn: []
feeds: []   # terminal / consumed at scaffold or build
```

RESERVED / auto-none, come back to (A8). Optional, special-circumstances, likely one exemplar (not the old mandatory three). Demoted from the old hard-stop gates/EXM; carries its shape for when defined. SHAPE NOTE (8 Oct 2026): `programmes` is no longer `required`, so the reserved auto-pass record ({value:"none", reserved:true}, written by cxp-open.js) validates. The `programmes` array still carries minItems/maxItems 3 from the old mandatory-three model, which CONTRADICTS this gate's own "likely one exemplar, not the old mandatory three": that range is left untouched here (it only bites once cxp-03 is un-reserved and actually defined) and is flagged for that future ruling.

### Context generation  `cxp-04_context-generation`

```yaml
id: cxp-04_context-generation
name: Context generation
phase: CXP
sequence: 23
decider: agent+human
hardness: soft
repeatsPer: context-pack
prompt: Confirm/amend the generated context-slot content.
produces: "all coupled-slot content (lessons + wrappers) at each slot's variationType"
dependsOn:
  - cxp-01_subject (constitutive)
  - les-01_lesson-proposal (constitutive)
  - wra-01_wrapper-open (constitutive)
  - wra-02_wrapper-close (constitutive)
  - wra-03_summative (constitutive)
feeds: []   # terminal / consumed at scaffold or build
sourceConsultation:
  triggeringFacets: [level, institution, faculty, activity]
  authorityLevels: [sector, institutional]
```

Old D1. Generates all coupled-slot content per subject: lesson context-specific checks, coupled worked examples, wrapper practice-connection prose. Referencing inherited from cxs-04 (not a gate here). Widest sourceConsultation set. BASELINE BRANCH: when cxp-01's subject is baseline, the generation reads the universal reference (generic, average student-facing standards from universal-reference.json) in place of a subject benchmark corpus; see generation.parameters.baseline.
