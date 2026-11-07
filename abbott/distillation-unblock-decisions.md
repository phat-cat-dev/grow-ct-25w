# Unblocking `pathway-distillation`: nine decisions

Unlanded proposal. Sits beside `pathway-proliferation-proposal.md`,
`trial-build-presenting-crs.md` and `trial-build-presenting-sdef-05.md` in
this same `abbott/` folder, outside `wkspc2614-adapt3`'s git tree, until
Abbott rules on it. **No gate ran to produce this document; nothing under
`courses/`, `design-kb/`, `schemas/` or `tools/` was edited.** `git status
--short` from the adapt3 repo root, both before and after this pass, shows
only the three pre-existing untracked sibling files above — none of the
three presenting manifests moved.

## What distillation is meant to do

`pathway-distillation` is the profile (`design-kb/design-kb.gate-profiles.json`,
third profile block, confirmed exactly three profiles exist across
`schemas/course-design.schema.json:45-49` and
`schemas/design-kb.gates.schema.json:136-140`) for building all three tiers
of one pathway together, grounded in the pathway's own 9 capabilities / 18
evidence statements (`catalogue/context/pathway*/`) rather than a free
thematic scope invented per course. Its own steps replace `crs-02` (scope)
and `crs-03` (free course outcomes) with `crs-06_pathway-statements` (surface
the 18 statements), `crs-07_tiered-outcomes` (4-6 flat LOs per tier, book-
first two-layer method) and `crs-08_progression` (cross-tier signposts), then
rejoins the universal flow at `crs-04_lesson-map` and continues through
`les-01`/`wra-01..04` unchanged in name but, in two of the four `wra-*`
gates, not in behaviour.

**The three-profile correction.** `pathway-proliferation` is not a fourth
profile. `docs/authoring/pathway-proliferation-gating-lookups.md:1-8` titles
itself "Pathway-proliferation gating" and then states plainly: "the user's
shorthand 'multiplies the old one by three' refers to (`pathway-distillation`:
all three tiers built together...)". It is informal shorthand for
`pathway-distillation`, nothing more. Both schemas enumerate exactly three
profile ids; there is no fourth to reconcile.

**Which three courses.** `presenting-introductory`, `presenting-intermediate`
and `presenting-advanced` — three independent, already-built, single-tier
manifests (not the multi-tier triplet `pathway-distillation` was designed to
scaffold together; see D1). Confirmed via `grep -n '"profile"'` against all
three: no manifest carries a `profile` field at all, so every validator run
below resolves them as `built-course-shape` (the schema's stated default,
`schemas/course-design.schema.json:50`: "Absent means built-course-shape").

## The measured baseline

Captured fresh, this pass, against all three tiers. Read-only commands; no
retries, no edits in between.

```
$ python3 tools/validate-design-schemas.py --course-design courses/presenting-introductory/course-design_presenting-introductory.json ; echo "EXIT: $?"
...
NSK-1: 9 closed lesson-map/after-outcomes record(s) found, crs-03_course-outcomes record present: True, required by profile 'built-course-shape': True
...
PASS
EXIT: 0
```
Identical PASS / `EXIT: 0` for `presenting-intermediate` and
`presenting-advanced`, same NSK-1 line, same profile resolution.

```
$ node tools/manifest-completeness.js --course=presenting-introductory ; echo "EXIT: $?"
...
Clause                                            | Items | Result
1. Gate coverage (les-01 per lesson-map lesson)   | 4     | FAIL  — missing: presenting-introductory-L04-les-01
2. Instantiations                                 | 18    | PASS
3. Context packs imply cxp-04 record              | 2     | FAIL  — psychology, school-of-sport: no per-pack cxp-04 record
4. Scaffold outputs                               | 5     | PASS
5. Duplicate _id                                  | 185   | PASS
6. slotKey resolution                             | 37    | FAIL  — L01-L04 "concept-intro" not in archetype
7. Lesson-key numbering                           | 4     | PASS

Lesson check (LCR-1): OC-1 PASS, CO-1 PASS, AL-3b FAIL ("course outcome(s)
with fewer than two summative items: co4 (0)"), AL-4 PASS, BKS-1 PASS,
CK-1 PASS, AL-3a PASS, PSR-1 PASS, LPG-1 PASS, RP-1 PASS, CP-1h PASS,
CP-1i PASS, PLR-1 PASS, MK-1 FAIL (L01-L03 activity-1..4: no built component)

manifest-completeness: FAILED (one or more clauses failed)
EXIT: 1
```
Byte-identical clause/result pattern for `presenting-intermediate` and
`presenting-advanced` (verified: same five failing checks — clauses 1, 3, 6,
AL-3b, MK-1 — same `co4 (0)` message, same missing-record name pattern,
`EXIT: 1` all three).

```
$ node tools/verify-course.js --course=presenting-introductory ; echo "EXIT: $?"
...
Check                      | Result
voice-lint                 | PASS
validate-design-schemas    | PASS
conformance-lint           | PASS
manifest-completeness      | FAIL

verify-course: FAILED (one or more checks failed)
EXIT: 1
```
Same for `presenting-intermediate` and `presenting-advanced`: `EXIT: 1`, same
three PASS + one FAIL pattern.

**The baseline is already red, before any profile switch, before any
distillation gate runs.** The profile switch this document leads toward
changes exactly one informational line in this output — NSK-1's
`required by profile '...'` value — and fixes none of the five standing
failures above.

---

## Tier 1 — wiring

### D1. How `profile` gets set on an existing manifest

**Gap.** `pathway-distillation` only exists as a manifest-level `profile`
field. There is currently no supported way to set that field on any of the
three presenting manifests, because the only tool that ever writes it writes
it in a mode these manifests didn't use, and no tool can amend it after the
fact.

**Evidence.**
- `tools/new-course.js:178-181` (inside `createMultiTierManifests`, the
  `pitch === "all"` multi-tier path): `slug: tierSlug, status:
  'in-development', profile: 'pathway-distillation', facetSet: facetSet,` —
  `profile` is written here and only here.
- `tools/new-course.js:274-296` (the single-tier path, the one these three
  manifests actually went through): the manifest object literal —
  `schemaVersion`, `courseId`, `slug`, `status`, `facetSet`, `kbVersions`,
  `gates`, `phases`, `instantiations` — has no `profile` key at all.
- `tools/new-course.js:240-246`: `main()` hard-refuses outright if
  `courseDir` already exists with a manifest inside it — `"This tool creates
  a course's FIRST manifest only; do not overwrite."` `new-course.js` cannot
  be rerun against these three.
- `tools/reopen.js` writes only two things to a manifest:
  `entry.records.push(result.newRecord)` and
  `courseDesign.sweepEvents.push(result.sweepEvent)`
  (`tools/reopen.js:258-261`, `applyReopen`). Neither path touches a
  top-level field; `reopen.js` cannot reach `profile` either.
- `schemas/course-design.schema.json:44-50` confirms `profile` is a real,
  validated top-level field (enum of exactly three values) — so this is a
  tooling gap, not a schema gap.

**Options.**
1. A new `tools/set-profile.js` — a small, single-purpose tool that opens a
   manifest, asserts the current `profile` value (or its absence) before
   writing, sets the new one, and writes nothing else. Matches this repo's
   "string-asserted edits" discipline (`CLAUDE.md`) and needs no change to
   any other tool.
2. Extend `tools/reopen.js` to also accept a `--set-profile` flag. Reuses an
   existing entry point but conflates two unrelated operations (profile
   change is not a gate reopen) and risks pulling an already-working tool
   into new failure modes.
3. A sanctioned one-off hand edit to the three manifests, with a dated note
   recording who/when/why (the model this repo already uses for
   unlanded decisions — see the sibling trial docs). Fastest, but leaves no
   reusable tool for the next course that needs this, and "one-off" hand
   edits to append-only manifests are exactly the kind of untooled write
   this repo's gate model exists to avoid.

**Recommended ruling.** Option 1, a new `tools/set-profile.js`. Every other
manifest mutation in this repo goes through a purpose-built tool with its own
assertions (`new-course.js`, `reopen.js`); `profile` should not be the one
field that only ever gets set by a hand edit. It is also small enough to
write and test in isolation before anything downstream depends on it.

**Implies.** A new file, `tools/set-profile.js` (not written this pass):
takes `--course=<slug> --profile=<id>`, asserts the manifest's current
`profile` value (including "absent") before writing, validates the new value
against `schemas/course-design.schema.json`'s enum, writes the single field,
and prints a diff-style before/after line ending in `EXIT: $?`.

---

### D2. Which gates `pathway-distillation` actually runs

**Gap.** `design-kb/design-kb.gate-profiles.json` and
`design-kb/design-kb.gates.json` disagree about whether `crs-06`, `crs-07`
and `crs-08` are part of `pathway-distillation`. The store that the live
validator actually reads (`gate-profiles.json`) omits them; the gates'
own self-declared `profiles` field claims them.

**Evidence.**
- `design-kb/design-kb.gate-profiles.json:172-179`, the `"pathway-statements"`
  step: `"id": "pathway-statements", "label": "The 18 pathway statements",
  "planned": true,` — no `"gates"` array.
- `design-kb/design-kb.gate-profiles.json:180-191`, the `"tiered-outcomes"`
  step: same pattern, `"planned": true`, no `"gates"` array.
- `design-kb/design-kb.gate-profiles.json:205-216`, the
  `"progression-signposting"` step: same pattern again.
- Contrast `design-kb/design-kb.gate-profiles.json:192-195`, the `"lessons"`
  step, which *does* carry `"gates": ["crs-04_lesson-map"]`.
- Meanwhile `design-kb/design-kb.gates.json:1103-1105` (`crs-06`),
  `:1191-1193` (`crs-07`) and `:1316-1318` (`crs-08`) each independently
  declare `"profiles": ["pathway-distillation"]`.
- The disagreement is not cosmetic — it is load-bearing in the one place a
  resolver already exists. `tools/validate-design-schemas.py:459-480`,
  `_profile_gate_ids()`: `ids = set(prof.get("continuesWith", []) or [])` then
  `for step in prof.get("steps", []) or []: ids.update(step.get("gates", [])
  or [])`. A step with `"planned": true` and no `"gates"` key contributes
  nothing to this set. For `pathway-distillation`, that means `crs-06`,
  `crs-07` and `crs-08` are **not** in the set this resolver returns, despite
  each gate's own `profiles` field naming the profile.
- `schemas/design-kb.gates.schema.json:143` documents what that resolved set
  is for: "gate.md step 1 RECON resolves it the same way to treat an
  out-of-profile dependsOn edge as not-applicable rather than a STOP." A gate
  the resolver thinks is out-of-profile has its dependents' edges on it
  silently waved through as not-applicable — the opposite of what
  `crs-07`'s own `"profiles"` field intends for, e.g., `wra-03`'s dependency
  on it (`design-kb/design-kb.gates.json:1830-1834`).

**Options.**
1. Add `"gates": ["crs-06_pathway-statements"]` /
   `["crs-07_tiered-outcomes"]` / `["crs-08_progression"]` to the three
   `"planned": true` steps and drop the `"planned"` flag (or keep it
   alongside `gates`, if "planned" is meant to survive as a separate
   "not yet exercised end-to-end" marker). Makes `_profile_gate_ids()` agree
   with `design-kb.gates.json`'s own claims with a four-line diff.
2. Treat each gate's own `"profiles"` field as the single source of truth and
   strip the `"profiles"` claims from `crs-06`/`crs-07`/`crs-08` in
   `gates.json` instead, leaving `gate-profiles.json`'s step list to decide
   scope on its own. Inverts which file wins, but means the `profiles` field
   on an individual gate stops being meaningful for any future profile-scoped
   gate, which is a larger behaviour change than this pass's remit.

**Recommended ruling.** Option 1. `design-kb.gates.json`'s `profiles` field
is the field `_profile_gate_ids()`-adjacent machinery
(`schemas/design-kb.gates.schema.json:143`) treats as authoritative
everywhere else in the store (it is how `crs-02`/`crs-03` are correctly
excluded from `pathway-distillation` today — see the Preamble). Making
`gate-profiles.json`'s steps agree with it is the smaller, more consistent
edit, and it is the one that does not ask every other profile-scoped gate's
semantics to change.

**Implies.** An edit to `design-kb/design-kb.gate-profiles.json`'s three
`"planned": true` steps (lines 172-179, 180-191, 205-216) in the
`pathway-distillation` profile block: add each step's own `"gates"` array
naming its one gate (`crs-06_pathway-statements`,
`crs-07_tiered-outcomes`, `crs-08_progression` respectively), leaving
`"planned": true` in place as a separate signal unless Abbott rules it should
go. No other file changes.

---

## Tier 2 — data shape

### D3. What crs-06's required `text` field reads from

**Gap.** `crs-06`'s `decidedValueShape` requires every statement to carry a
`text` field. Its own authoring instruction says to copy that text verbatim
from `catalogue/context/pathway-evidence/<pathway>.json`. That file's items
have no `text` field.

**Evidence.**
- `design-kb/design-kb.gates.json:1153-1155`: `"text": { "type": "string" }`,
  inside `statements[]`'s `required: ["capabilityId", "tier", "kind",
  "text"]` (`:1129-1134`).
- `design-kb/design-kb.gates.json:1169`: "Read
  catalogue/context/pathway-evidence/<pathway>.json in full and copy its 18
  statements into decidedValue.statements unchanged. Do not paraphrase, trim,
  or invent a 19th."
- `catalogue/context/pathway-evidence/presenting.json:13-17`, one full item:
  `"kind": "conceptual", "title": "Presentation brief mapped to learning
  outcomes", "example": "...", "artefact": "...", "grounding": [...]`. No
  `"text"` key anywhere in the file (confirmed: every item in the file
  carries exactly `kind`/`title`/`example`/`artefact`/`grounding`).
- The same file also carries a `"genericOutcomes"` array
  (`catalogue/context/pathway-evidence/presenting.json:27` onward) whose
  items carry a `"learningOutcome"` field
  (e.g. line 32: `"learningOutcome": "The student can explain how a
  presentation brief defines its intended audience..."`) — a full prose
  string, unused by any gate in the store (confirmed: no `gate.id` or field
  description anywhere in `design-kb.gates.json` names `genericOutcomes` or
  `learningOutcome`).

**Options.**
1. Map `text` to `title` — short, already present, matches the evidence
   item's own headline, but loses the fuller `example` prose crs-07 might
   need for grounding.
2. Map `text` to `example` — the fullest prose field, closest in spirit to
   "a statement", but it is written as a worked scenario, not a flat
   assertion, so it reads oddly as a "pathway statement".
3. Compose `text` from `title` + `example` (or `title` + `artefact`) at
   authoring time. Richer, but turns a stated "copy unchanged" instruction
   into a derived-field instruction, contradicting crs-06's own
   `authoringReview` text.
4. Rename the field the gate actually requires (`text` → `title`, or
   `text` → `statement`) so the schema matches the source file instead of
   asking the source file to grow a field. Simpler schema-side fix, but a
   gate-shape rename after records may already be referencing it elsewhere
   needs its own check for other readers of `statements[].text`.

**Recommended ruling.** Option 1, map `text` to `title`. `title` is the one
field in the evidence-file item that is already a single, self-contained
statement (not a worked scenario like `example`, not a derived composite);
it matches "copy ... unchanged" literally, and it leaves the schema's field
name stable for any other reader. The unused `genericOutcomes`/
`learningOutcome` pair should be flagged to Abbott separately — it may be the
field crs-06 was actually meant to read, in which case this ruling changes
to "map `text` to `genericOutcomes[].learningOutcome`" instead, but that is a
different source array entirely (9 items vs. 18) and needs its own
confirmation before being folded into this ruling.

**Implies.** An edit to `crs-06`'s `authoringReview.instruction`
(`design-kb/design-kb.gates.json:1169`) clarifying that `text` is sourced
from the evidence item's `title` field, not a literal 1:1 field-name copy.
No schema-shape edit needed, since `text` as a string field already accepts
`title`'s string value unchanged.

---

### D4. The `capabilityId` form, and the two nulls

**Gap.** `crs-06` requires `capabilityId` as a string on every statement.
`catalogue/context/pathway/presenting.json` carries `capabilityId: null` for
two of its nine capability rows, and the convention for a non-null
`capabilityId` is not settled — three different forms are in live use across
two files.

**Evidence.**
- `design-kb/design-kb.gates.json:1136-1138`: `"capabilityId": { "type":
  "string", "description": "The i1-i3/d1-d3/e1-e3 capability id this
  statement evidences." }`.
- `catalogue/context/pathway/presenting.json:42-43`: `"rowId": "i1",
  "capabilityId": null,`.
- `catalogue/context/pathway/presenting.json:152-153`: `"rowId": "i3",
  "capabilityId": null,`.
- The other seven rows in the same file use a slash form: `"capabilityId":
  "presenting/c1"` (line 74), `"presenting/01"` (line 180), `"presenting/03"`
  (line 260), `"presenting/02"` (line 336), `"presenting/c3"` (line 410),
  `"presenting/04"` (line 488), `"presenting/c2"` (line 565).
- `catalogue/context/pathway-evidence/presenting.json` uses a third,
  different form for the same two rows: line 7, `"capability":
  "presenting#i1"`, and line 103, `"capability": "presenting#i3"` — a `#`
  form, not the `/` form the other file uses for its other seven rows (same
  file, lines 55, 151, 199, 247, 295, 343, 392: `"presenting/c1"`,
  `"presenting/01"`, `"presenting/03"`, `"presenting/02"`, `"presenting/c3"`,
  `"presenting/04"`, `"presenting/c2"` — the identical slash set, for the
  identical seven rows, as the other file).
- `catalogue/context/subject/benchmarks/universal-reference.json:9151` also
  contains the string `"presenting#i1"`, confirming that form
  is attested in a second file for `i1` specifically — but no
  `"presenting#i3"` form appears there, so `i3`'s `#` form is attested only
  once, in `pathway-evidence/presenting.json` alone.

**Options.**
1. Standardise on the bare `rowId` (`"i1"`, `"i3"`) — shortest, needs no
   cross-file lookup, but discards the pathway-prefix disambiguation the
   other two forms carry (relevant once multiple pathways' capability ids
   are compared side by side, e.g. at `crs-08`'s cross-tier step).
2. Standardise on the `#` form (`"presenting#i1"`) — already used by both
   `pathway-evidence/presenting.json` and (for `i1` only)
   `universal-reference.json`; extending it to `i3` and to the other seven
   rows (which currently use `/`, not `#`) means rewriting eight of the nine
   rows in `pathway/presenting.json`, not just filling two nulls.
3. Standardise on the `/` form already used for seven of the nine rows in
   `pathway/presenting.json` (and mirrored in `pathway-evidence/
   presenting.json`'s own seven) — fills the two nulls by extension of the
   file's own dominant pattern (`presenting/i1`, `presenting/i3`), at the
   cost of diverging from the `#` form already live in
   `universal-reference.json` for `i1`.

**Recommended ruling.** Option 3, the `/` form, extended to the two null
rows as `"presenting/i1"` and `"presenting/i3"`. Seven of nine rows in the
file that actually requires the fix (`pathway/presenting.json`) already use
`/`; fixing the two nulls to match their eight siblings touches only those
two rows. The `#` form's one precedent in `universal-reference.json`
(`i1` only) is a smaller footprint to reconcile afterward (one value, one
file) than rewriting eight rows across two files to adopt `#` everywhere.

**Implies.** An edit to `catalogue/context/pathway/presenting.json:43` and
`:153`: `"capabilityId": null` → `"capabilityId": "presenting/i1"` and
`"presenting/i3"` respectively. A follow-up note (not this pass) that
`universal-reference.json`'s one `"presenting#i1"` occurrence should be
reconciled to the `/` form once this ruling lands, so the two files stop
disagreeing for that one id.

---

## Tier 3 — semantics

### D5. What crs-04 points at under distillation (absorbing D9's trigger, formerly B9)

**Gap.** `crs-04_lesson-map`'s shape, dependency notes and validation checks
are all written against `crs-03`'s course outcomes. Under
`pathway-distillation`, `crs-03` does not run (it is scoped to
`["built-course-shape", "single-course"]` only), and no replacement wiring —
pointing lessons at `crs-07`'s flat LOs instead — is written down anywhere.

**Evidence.**
- `design-kb/design-kb.gates.json:863-874` (`crs-04`'s `dependsOn`): both
  edges, on `crs-03_course-outcomes` and `crs-02_thematic-scope`, are
  `"dependencyClass": "constitutive"` — the strongest class — and neither
  edge carries any profile qualifier.
- `design-kb/design-kb.gates.json:901-903` and `:983`:
  `lessons[].mainCourseOutcome` is not in `required: ["key"]`, and the
  `lessons[]` item object is `"additionalProperties": false` — so
  `mainCourseOutcome` is optional, present-or-absent, never itself pointing
  anywhere else.
- `design-kb/design-kb.gates.json:1004-1017`: `AL-1`
  (`lessons[].outcomes[].serves` against
  `crs-03_course-outcomes.courseOutcomes[].id`), `AL-2` (scope check against
  `crs-02_thematic-scope`), `MCO-1` (`lessons[].mainCourseOutcome` against
  the same `crs-03` ids) — all three of `crs-04`'s own validation checks
  resolve against `crs-03`, with no profile-conditional branch (contrast
  `wra-03`'s explicit branch, see D6's evidence).
- `design-kb/design-kb.gate-profiles.json:203`, the `pathway-distillation`
  "lessons" step's own `"open"` note (its embedded line-number pointers to
  `design-kb.gates.json:748-755` and `:1361-1366` do not resolve to the
  content they claim — themselves drifted, not usable as citations — but the
  note's own text, at this location, stands): "crs-04's dependency note and
  every lesson's serves field assume a course-outcome id ... crs-03
  _course-outcomes itself needs removing or repurposing before this touches
  live gates."
- `tools/validate-design-schemas.py:786-796`: `course_outcome_ids` is "built
  from crs-03_course-outcomes' decidedValue.courseOutcomes"; the `OC-1`/`CO-1`
  cross-check (`:796` onward) "Only enforced when at least one course outcome
  was found" — i.e., it is silent whenever `crs-03` carries no record, which
  is exactly `pathway-distillation`'s normal state.
- The B9 consequence, concretely: in the three presenting manifests today,
  `crs-03` **does** carry a closed record (because they currently resolve as
  `built-course-shape`, Preamble). `courses/presenting-introductory/
  course-design_presenting-introductory.json:369,373,377,381` show four
  outcome ids, `co1`-`co4`. If `crs-04`'s `serves`/`mainCourseOutcome` were
  repointed at `crs-07` ids while this stale `crs-03` record stayed in place,
  `course_outcome_ids` would stay populated from the old `co1`-`co4` set and
  `OC-1`/`CO-1` would fail every `serves` value that now names a `crs-07`
  outcome id instead.

**Options.**
1. Add a `pathway-distillation`-conditional branch to `crs-04`'s
   `dependsOn`, `AL-1`, `AL-2` and `MCO-1` — mirroring the pattern `wra-03`
   already uses (D6's evidence) — naming `crs-07_tiered-outcomes` as the
   constitutive source and its `outcomes[].id` as what `serves`/
   `mainCourseOutcome` must resolve against, under this profile only.
2. Leave `crs-04` universal/unconditional and instead give `crs-07` outcome
   ids the exact same shape and id-space as `crs-03` outcome ids, so no
   gate downstream needs to know which profile produced them. Simpler for
   every downstream reader, but hides the fact that `pathway-distillation`
   has no course-outcome tier at all (the gate's own `consequenceNote`,
   `design-kb.gates.json:1211`, is explicit that this is intentional:
   "no distillation to 3, no expansion to 9").

**Recommended ruling.** Option 1. It is the smaller, more honest edit: it
makes `crs-04` match the branching pattern `wra-03` already demonstrates
works (D6), rather than asking `crs-07`'s id space to impersonate `crs-03`'s.
It also directly answers D9's trigger: once `crs-04`'s validation explicitly
branches on profile, a stale out-of-profile `crs-03` record is visibly
irrelevant to `crs-04`'s checks rather than silently interfering with them —
which is the condition D9 needs settled before it can rule on what happens
to that stale record.

**Implies.** An edit to `design-kb/design-kb.gates.json`'s `crs-04` entry:
add a third `dependsOn` edge on `crs-07_tiered-outcomes` (constitutive,
`pathway-distillation` only, mirroring `wra-03`'s edge note style at
`:1830-1834`), and extend `AL-1`/`AL-2`/`MCO-1`'s `rule`/`appliesTo` text with
the `crs-07`-sourced id-space for that profile — without removing the
existing `crs-03`-sourced branch, which stays correct for
`built-course-shape`/`single-course`. A paired edit to
`tools/validate-design-schemas.py`'s `NSK-1` is **not** required — it is
already profile-aware (`:539-559`, "only ever relaxes" confirmed by its own
fallback: `co_required_by_profile` is `True` whenever profile resolution
fails or the profile's own step list names `crs-03`, and only ever `False`
when it demonstrably does not).

---

### D6. Where wrapper and confidence content comes from

**Gap.** All four `wra-*` gates sit in `pathway-distillation`'s
`continuesWith` list, so all four are in-profile. But only one of the two
content-bearing wrappers — `wra-03_summative` — has a written branch for
what to do without `crs-03`. `wra-04_confidence` has none: its only upstream
edge is the now-absent `crs-03`, and `crs-07`'s shape has no field to supply
confidence-statement text from instead.

**Evidence.**
- `design-kb/design-kb.gate-profiles.json:259`: `"continuesWith":
  ["les-01_lesson-proposal", "wra-01_wrapper-open", "wra-02_wrapper-close",
  "wra-03_summative", "wra-04_confidence"]` — all four `wra-*` gates listed,
  `pathway-distillation` profile block.
- `wra-03` **is** distillation-aware. `design-kb/design-kb.gates.json:1830
  -1834`, its third `dependsOn` edge: `"gate": "crs-07_tiered-outcomes",
  "dependencyClass": "constitutive", "note": "pathway-distillation only
  (crs-07 carries no record, and this edge is not-applicable, under any
  profile that does not name crs-07_tiered-outcomes in its step list): under
  this profile, with no course-outcome tier, SUMM items are authored one per
  flat LO (AL-3 becomes one-per-LO, not two-per-course-outcome) from crs-07's
  tiered outcomes directly."` Its `generation.parameters` even carries both
  branches side by side (`:1851-1852`): `"perOutcome": "...built-course-shape
  / single-course"`, `"perLO": "...pathway-distillation..."`.
- `wra-04` has no equivalent branch anywhere. Its entire `dependsOn` is one
  edge (`design-kb/design-kb.gates.json:1920-1926`): `{"gate":
  "crs-03_course-outcomes", "dependencyClass": "constitutive", "note":
  "Places crs-03's per-outcome confidence statements into C-PRE/C-POST."}` —
  no second edge, no profile-conditional note, unlike its sibling `wra-03`
  three gates earlier in the same file.
- `wra-04`'s `consequenceNote` (`:1942`) and `decidedValueShape`
  (`:1943-1966`) both describe `statements[].rates` as "the course outcome
  id (from crs-03) this statement rates" (`:1957`) — `crs-03` is hard-coded
  into the field's own description, not merely its generation source.
- `crs-07`'s `decidedValueShape` (`design-kb/design-kb.gates.json:1212-1268`)
  has no `confidenceStatement` field, nor anything resembling one, anywhere
  in its `outcomes[]` item shape (`id`, `text`, `layer`, `source` only,
  confirmed exhaustively against `:1223-1264`).
- No formal check object named `AL-5` exists anywhere in
  `design-kb.gates.json` (confirmed by grep: `AL-5` appears only inside prose
  — `crs-04`'s `scopeNote` at `:1019` and `crs-05`'s `scopeNote` at `:1084` —
  never as a check with its own `"id": "AL-5"` entry), so there is no
  existing formal rule to extend even if a source field existed.

**Options.**
1. Add a `confidenceStatement` field to `crs-07`'s `outcomes[]` item shape —
   mirrors `crs-03`'s `courseOutcomeBanks[].confidenceStatement` structurally,
   lets `wra-04` branch exactly the way `wra-03` already does. Requires
   authoring new confidence-statement text at `crs-07` time, one per flat LO,
   that does not exist in the pathway's evidence/book sources today.
2. Add a `pathway-distillation` clause to `wra-04`'s existing (prose-only,
   not a formal check object) `AL-4` parameter, deriving confidence-statement
   text from `crs-06`'s evidence statements instead of a new `crs-07` field —
   reuses already-authored prose (the 18 evidence statements) rather than
   demanding new authoring, but stretches `AL-4`'s stated meaning ("every
   course outcome carries at least one" — there is no course outcome under
   this profile) to cover a different id space without being reworded.
3. A new gate, distinct from `wra-04`, scoped to `pathway-distillation` only,
   producing confidence statements against `crs-07` ids directly — cleanest
   separation of concerns, but the heaviest option: a new gate id, new shape,
   new sequence slot, and `wra-04` would need its own `dependsOn`/`profiles`
   edit anyway to stay out of this profile's way.

**Recommended ruling.** Option 1, add `confidenceStatement` to `crs-07`'s
outcome shape. It is the option that makes `wra-04` able to copy `wra-03`'s
already-proven branching pattern verbatim (same `dependsOn`-edge-plus-note
shape, same `perOutcome`/`perLO`-style parameter split), rather than
inventing a new reuse-vs-reword tradeoff (option 2) or a new gate (option 3)
for a problem `wra-03` already solved once in this exact profile.

**Implies.** Two paired edits to `design-kb/design-kb.gates.json`: (a) add
`confidenceStatement: {type: "string"}` to `crs-07`'s `outcomes[]` item
properties (near `:1229-1264`), with an `authoringReview` note describing
when it is authored (same pass as the outcome's `text`, book-grounded, no
separate source); (b) give `wra-04` a second `dependsOn` edge on
`crs-07_tiered-outcomes` (constitutive, `pathway-distillation` only) mirroring
`wra-03`'s note at `:1830-1834`, and extend `wra-04`'s `generation.parameters`
and `decidedValueShape.statements[].rates` description with the `crs-07`-id
branch, exactly paralleling `wra-03`'s `perOutcome`/`perLO` split.

---

### D7. The lesson-count floor

**Gap.** A "minimum 5 lessons per tier" ruling, dated 2 Nov 2026, is recorded
in multiple places governing the `pathway-distillation` lesson map. The gate
that actually produces the flat LOs lessons are built one-to-one from —
`crs-07`'s own schema — sets a floor of 4, not 5. One of the two is wrong,
and today's three presenting-course manifests sit exactly on the fault line:
each carries 4 lessons.

**Evidence.**
- `design-kb/design-kb.gate-profiles.json:194`: `"label": "5-6 lessons per
  tier (hard floor 5, ceiling 6), one LO each"`.
- `design-kb/design-kb.gate-profiles.json:200`: `"produces": "5-6 lessons per
  tier, one LO each (minimum 5 enforced 2 Nov 2026; ceiling remains 6)"`.
- `design-kb/design-kb.gates.json:1019` (`crs-04`'s `scopeNote`): "The
  lesson-count floor (minimum 5 per tier, 2 Nov 2026 ruling) ... NOT YET
  schema-enforced on decidedValueShape."
- `docs/authoring/pathway-proliferation-gating-lookups.md:158` (table row):
  "5-6 lessons per tier (hard floor 5, ceiling 6), one LO each".
- Against all of that: `design-kb/design-kb.gates.json:1220-1221`, `crs-07`'s
  own `decidedValueShape.outcomes`: `"minItems": 4, "maxItems": 6` — the gate
  that is the one-to-one source for lesson count
  (`design-kb.gate-profiles.json:196`: "The tier's flat LOs (5-6, set by
  tiered-outcomes' ... method) map one-to-one onto 5-6 lessons") is itself
  schema-enforced at a floor of 4, not 5.
- All three presenting manifests currently carry exactly 4 lessons each
  (confirmed: `crs-04_lesson-map.decidedValue.lessons` arrays, all three
  tiers, length 4 — matching `manifest-completeness.js`'s own "Lesson map: 4
  lessons" line in every run captured in the Preamble).

**Options.**
1. Rule the floor is 5, as every prose source states, and fix `crs-07`'s
   `minItems` from 4 to 5 to match — the schema-enforced number was simply
   never updated when the floor was raised. Under this ruling, all three
   presenting tiers are already non-conformant at 4 lessons.
2. Rule the floor is 4, matching `crs-07`'s schema, and treat every "hard
   floor 5" prose statement as the thing that drifted — the floor was
   provisionally 5 and was quietly relaxed to 4 (consistent with these three
   courses actually shipping at 4), but the prose was never updated to say
   so.

**Recommended ruling.** Option 1, the floor is 5 and `crs-07`'s `minItems`
is the drift. Four independent prose sources (`gate-profiles.json` twice,
`gates.json`'s own `crs-04` scope note, and the external docs file) all
state "5" and all cite the same dated ruling (2 Nov 2026); `crs-07`'s
`minItems: 4` is the single outlier, and nothing in the record documents a
deliberate relaxation from 5 to 4 — only `crs-04`'s own scope note
describing the floor as "not yet schema-enforced," which reads as an
oversight rather than a decision. This ruling does mean the three presenting
tiers are already non-conformant and the four L04-related gaps recorded
below are not the only outstanding lesson-count question once distillation
runs on them.

**Implies.** An edit to `design-kb/design-kb.gates.json:1220`: `"minItems":
4` → `"minItems": 5` on `crs-07_tiered-outcomes.decidedValueShape.outcomes`.
No other file changes; this does not by itself change the three presenting
manifests (out of scope, Explicitly out of scope section below).

---

## Tier 4 — the tool fix

### D8. Two defects in `tools/reopen.js`

**Gap.** `reopen.js`'s dependent-sweep preview has two defects that would
surface the moment it is run against any of these three courses under a
profile switch: it cannot tell an in-profile dependent from an out-of-profile
one, and it cannot recognise a per-lesson gate record by its stored id.

**Evidence — (a) no profile awareness.**
- `tools/reopen.js:15-17` (header comment, stating the design intent): "The
  preview: tools/gate-order.js's own getDependents(store, gateId) ... the
  reverse-edge scan over the store's static dependsOn edges -- never a
  hardcoded list."
- `tools/gate-order.js:138-150`, `getDependents` in full: it iterates every
  gate's `dependsOn` array and collects every edge whose `edge.gate ===
  gateId`, with no parameter for, or reference to, the manifest's `profile`
  or any `profiles` field. It would return `crs-04`'s dependents on `crs-03`
  and `crs-02` exactly the same way whether or not the manifest is
  `pathway-distillation`, where (per D5) those two should be out-of-profile.
- `tools/reopen.js:141-153`, `buildReopenPreview`, calls `gateOrder
  .getDependents(store, gateId)` directly (`:146`) with no post-filter by
  profile anywhere in the function.
- Concretely: reopening `crs-02` or `crs-03` under `pathway-distillation`
  today would sweep every dependent `getDependents` finds via the raw
  `dependsOn` edges — including `crs-04`, `wra-03`, `wra-04` — as
  `constitutive → invalidate` (the default verdict per `reopen.js:19-22`),
  even though D5/D6 would make those edges not-applicable under this profile.

**Evidence — (b) `hasRecord`'s exact-match lookup.**
- `tools/reopen.js:200-203`: `const hasRecord = dep => { const e =
  (courseDesign.gates || []).find(g => g.gateId === dep.gate); return !!(e
  && e.records && e.records.length > 0); };` — an exact string match between
  the bare gate id from a `dependsOn` edge (e.g. `"les-01_lesson-proposal"`)
  and the manifest's stored `gateId`.
- The three presenting manifests store per-lesson `les-01` records under a
  slug-and-lesson-prefixed id, not the bare one:
  `courses/presenting-introductory/course-design_presenting-introductory.json
  :783,938,1093`: `"gateId": "presenting-introductory-L01-les-01"`,
  `"...-L02-les-01"`, `"...-L03-les-01"`.
- `"les-01_lesson-proposal" === "presenting-introductory-L01-les-01"` is
  false for every one of these three real ids, so `hasRecord` returns
  `false` for a gate that in fact has three closed records. Per
  `tools/reopen.js:204`: `const authoredFresh = preview.dependents
  .filter(dep => !hasRecord(dep)).map(dep => dep.gate);` — these three
  closed, human-confirmed records would be silently classified as
  `authoredFresh` ("neither require nor receive a sweep entry," per the
  comment at `:197-199`) and dropped from the sweep entirely, rather than
  being reported to Abbott for disposition.

**Options.**
1. Fix (a) by having `buildReopenPreview` filter `getDependents`'s result
   against the manifest's own resolved profile-gate-id set (the same
   resolver D2 fixes, `_profile_gate_ids`-equivalent logic ported into
   `gate-order.js` or called from it), dropping any dependent whose edge is
   not-applicable under the active profile before the sweep is built. Fix
   (b) by normalising `dep.gate` against the manifest's actual stored ids —
   for `repeatsPer: lesson` gates, expand the bare id to every
   `<slug>-L<NN>-<bareId>` the manifest actually carries, the same way
   `manifest-completeness.js`'s own per-lesson logic already does (it
   correctly finds and reports the three `les-01` records in every baseline
   run above).
2. Fix only (b), leave (a) for whenever D5/D2 land, since (a) only matters
   once a profile-scoped reopen is actually attempted and D1-D2 are
   prerequisites for that happening at all. Smaller immediate patch, but
   ships a tool that is still wrong for the exact scenario this whole
   unblocking effort is for.
3. Fix neither now; document both as known defects and block any `/reopen`
   call on these three courses until both are fixed. No code risk this pass,
   but defers the one piece of this whole document that is an actual,
   unambiguous bug (not a judgement call) with no decision left to make.

**Recommended ruling.** Option 1, fix both together. Both are confirmed,
unambiguous defects (not judgement calls — `hasRecord`'s mismatch is a plain
string-equality bug against data already in the repo; `getDependents`'s lack
of profile awareness is a plain gap against a schema field,
`design-kb.gates.schema.json:143`, that already documents the intended
behaviour). Shipping (b) alone leaves a tool that will misreport the very
courses this pass is about the first time anyone reopens `crs-02`/`crs-03`
on them under distillation.

**Implies.** Edits to `tools/reopen.js`: `buildReopenPreview`
(`:141-153`) gains a profile-filter step after `getDependents` is called,
using whatever resolver D2's ruling produces; `hasRecord` (`:200-203`) gains
id-expansion logic for `repeatsPer: lesson` gates before the equality check,
reading the gate's own `repeatsPer` flag off the store
(`design-kb.gates.schema.json:131`, the field already documenting the
`<slug>-<lessonKey>-les-01` keying convention) rather than hardcoding the
pattern. The test that proves it: a reopen preview run against
`presenting-introductory`'s `crs-04` (once D1 sets its profile) correctly
lists the three `les-01` records as sweep-eligible dependents, not
`authoredFresh`.

---

## Tier 5 — the consequence question

### D9. What happens to the inert closed crs-02/crs-03 records

**Gap.** Once D1 sets a `profile` and D2 fixes which gates run, `crs-02` and
`crs-03` are out of profile for all three presenting courses. But their
closed, human-confirmed records already exist in all three manifests, were
written under `built-course-shape`, and — per D5 — actively break the
`OC-1`/`CO-1` cross-check the moment `crs-04`'s `serves` values are
repointed at `crs-07` ids. Append-only means they cannot simply be deleted;
what happens to them is undecided.

**Evidence.**
- All three manifests currently carry closed `crs-02_thematic-scope` and
  `crs-03_course-outcomes` records (confirmed in every `validate-design
  -schemas.py` run in the Preamble: `SHP-1 PASS: crs-02_thematic-scope seq 1`
  / `SHP-1 PASS: crs-03_course-outcomes seq 1`, all three tiers).
- `tools/validate-design-schemas.py:786-796`: `course_outcome_ids` is built
  from `crs-03`'s `decidedValue.courseOutcomes`; the cross-check "Only
  enforced when at least one course outcome was found" (`:794-795`) — i.e.,
  as long as the stale `crs-03` record exists with its `co1`-`co4` ids
  populated, this check stays live and will fire against whatever `crs-04`'s
  `serves` values actually say, regardless of profile.
- `schemas/course-design.schema.json:634-642`: the `changeKind` enum
  includes `"re-deferred"` alongside `"amended"`, `"replaced"`,
  `"facet-added"`, `"facet-removed"`, `"facet-swapped"` — a real, already
  schema-defined option for exactly this kind of "no longer in scope, not
  wrong, not superseded by new content" state change.
- `tools/validate-design-schemas.py:539-559`'s NSK-1 profile-awareness
  (D2/D5's own evidence) is, in its own comment's words, the only
  profile-aware check in the file, and "only ever relaxes" — it lifts a
  requirement, it never adds a new pass/fail condition based on profile. It
  has no mechanism today to say "this closed record is out-of-profile,
  ignore its contribution to `OC-1`/`CO-1`."

**Options.**
1. Leave the records in place and make `OC-1`/`CO-1` (and any other
   cross-check that reads `course_outcome_ids`) profile-aware the same way
   `NSK-1` already is: skip building `course_outcome_ids` from `crs-03` when
   the manifest's profile does not name it. Pairs directly with D5's ruling
   and reuses the exact resolver D2 introduces. Keeps the append-only record
   untouched, which is the safest option for a human-confirmed decision.
2. `/reopen` both gates with `changeKind: "re-deferred"`, appending a new
   record state rather than leaving the old one load-bearing. Uses the
   schema's own vocabulary for this situation and leaves an explicit, dated
   trail of the profile switch — but needs D8 fixed first (reopening
   `crs-02` would otherwise mis-sweep `crs-04` per D8(a)), and needs a
   decision on what a `re-deferred` record's own `decidedValue` should
   contain (empty? a pointer to `crs-06`/`crs-07`?).
3. A new disposition verdict, distinct from `re-deferred`, specifically for
   "superseded by a profile change, not by new authoring" — most precise,
   but the heaviest option: a schema change to the `changeKind` enum and a
   new code path in `reopen.js` for a situation that may only ever apply to
   exactly these three courses.

**Recommended ruling.** Option 1, make the cross-checks profile-aware rather
than touching the records. It needs no schema change, no new disposition
verdict, and directly extends a pattern (`NSK-1`'s profile resolution) this
same store already uses correctly elsewhere. It also correctly reflects what
actually happened to these records: nothing about them is wrong or
superseded by new authoring — they are simply the product of a profile the
course no longer runs under, which is a reading question for the validator,
not a writing question for the manifest. Needs Abbott's word regardless,
since it is the one ruling in this document that decides the fate of
existing human-confirmed, append-only records rather than future tooling.

**Implies.** An edit to `tools/validate-design-schemas.py`'s `OC-1`/`CO-1`
cross-check (`:786` onward): gate the `course_outcome_ids`-building step on
the same `co_required_by_profile` resolution `NSK-1` already computes
(`:555-559`), so a `crs-03` record present under an out-of-profile condition
does not populate `course_outcome_ids` at all. No edit to any manifest.

---

## Also recorded, not as decisions

**The four missing L04 `les-01` gate records are not an unauthored gap.**
All three tiers have 4 lesson-map entries, 4 page `instantiations`, and L04
carries the same authored volume as L01-L03 — confirmed against
`presenting-introductory`'s own `manifest-completeness.js` run in the
Preamble: `L04 BKS-1 - 6 sourceSections resolved` (more than L01-L03's 2
each) and an identical `OC-1`/`CO-1` pass for L04's three outcomes
(`L04-o1..3 serves co4`). Only L04's *gate* record is absent; L04's content
is not behind L01-L03 in any other clause. (This matches
`manifest-completeness.js`'s own observation at
clause 1: "Missing gate records (1): presenting-introductory-L04-les-01" —
one record, not four pages of missing authoring.)

**The crs-03 outcome-count inconsistency.** All three manifests' closed
`crs-03_course-outcomes` records carry four outcomes, `co1`-`co4`
(`courses/presenting-introductory/course-design_presenting-introductory.json
:369,373,377,381`), while the same record's own
`courseOutcomeCountReason` field (line 385) states: "Three, matching the
three introductory sub-themes ... No integrative fourth outcome at
introductory." The record's count field and its own stated reason for that
count disagree inside the same closed, human-confirmed record. This is
exactly the condition `AL-3b` fails against in every baseline run above
(`"course outcome(s) with fewer than two summative items: co4 (0)"` — `co4`
has no summative coverage, consistent with a fourth outcome the record's own
prose says should not exist).

**The baseline is already red, independent of anything in this document.**
Per-tier, `validate-design-schemas.py --course-design` exits 0 (`PASS`);
`manifest-completeness.js` and `verify-course.js` both exit 1 (`FAIL`),
identically across all three tiers, with five pre-existing failures: clause
1 (missing L04 `les-01` record), clause 3 (missing per-subject `cxp-04`
records for psychology and school-of-sport), clause 6 (`concept-intro`
slotKey not in archetype, L01-L04), `AL-3b` (`co4`'s zero summative items),
and `MK-1` (L01-L03's `activity-1..4` skeleton keys have no built
component). The profile-switch work this document leads toward changes one
informational `NSK-1` line in `validate-design-schemas.py`'s output and
fixes none of these five.

**`pathway-proliferation` is not a profile.** Per the Preamble's
three-profile correction: it is `pathway-distillation`'s own informal
shorthand, per `docs/authoring/pathway-proliferation-gating-lookups.md:1-8`,
and both schemas enumerate exactly three profile ids. There is no fourth
profile anywhere in this store to reconcile against.

**`crs-04` needs no `profiles` array of its own.**
`schemas/design-kb.gates.schema.json:143`: "Absent means universal (applies
under every profile — the default for all pre-existing gates)." `crs-04`
already has no `profiles` field (confirmed: no such key anywhere in its
entry, `design-kb/design-kb.gates.json:857-1023`), which is correct as-is —
D5's ruling adds a third `dependsOn` edge and extends its checks, it does
not add a `profiles` array, since narrowing `crs-04` to named profiles would
be a regression from its current, correct, universal scope.
