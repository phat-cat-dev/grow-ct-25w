# Course Creation Workflow

*The procedure for creating a new course, start to finish, through the
gate conversation model. This is P7 (project-backlog.md), started
22 July 2026. REWRITTEN 27 August 2026 (away-week Session 3) against
the S3-D1–D9 decision set; the prior step-numbered form (22 July) is
superseded in full — its structural content is absorbed at the gate
loci recorded in S3-D9, and the away-week log's Session 3 entries hold
the mapping. Supersession visible per records policy.*

**Terminology, fixed by open-decisions.md #29 (DM-1a):** a **course** is
one pathway-tier. A **lesson** is one teaching unit within a course
(e.g. what Academic Writing Introductory calls "Planning"). A **shell** is
the context-neutral prose within one lesson. Don't use "course" to mean
a single lesson, or "lesson" to mean a whole pathway-tier; this
document and everything it points to depends on the distinction
staying clean.

## §0 Preamble

**What this document is.** The course-creation procedure as a sequence
of gated conversations. It has two consumers, per the standing working
model as ruled 8 Sep 2026 (venue/cadence/provenance ruling, part 1):
**either claude.ai or Claude Code may conduct the design
conversation** (every gate in this document is a conversational
moment, wherever it runs; a Claude Code session runs its own gate
conversation via `/gate`, read-only, in plan mode) and **Claude Code
executes** the resulting build and records tasks on node01 — via
self-contained prompts where the claude.ai relay conducted the
conversation (companion document: `course-creation-prompts.md`, one
prompt per phase/write moment, mirroring this document's section
order), or via `/land` where a Claude Code session conducted it
directly. Every gate record's `sessionRef` names which venue actually
closed it. Abbott relays between claude.ai and Claude Code when the
claude.ai venue is in use for a session. Neither consumer follows this
document alone: the conversation produces decisions; the prompts (or
`/land`) record them.

**Authorities this document points to, never duplicates:**

- **Gate definitions** — `design-kb/design-kb.gates.json` (machine
  authority: hardness, default types, clusters, dependency edges).
  This document says what happens *at* each gate; the kb says what
  each gate *is*.
- **Gate behaviour** — `docs/design/gate-conversation-model-draft-v1.md`
  (proposal/confirmation mechanics, provenance vocabulary, sweep
  machinery §5). This document choreographs; the model governs.
- **Decision provenance** — the away-week log and open-decisions.md
  (S1-D1–D12, S2-D1–D9, S3-D1–D9 and their ancestors).

**The manifest is authoritative (S1-D5).** Every course conversation
produces `course-design_<slug>.json`: the per-course manifest of
decisions and declarations — facet set, archetype instantiations, slot
choices, gate outcomes with provenance and grounding. It is never
content or structure bodies. It is checkable four ways: design-kb
refs, source-kb grounding, the built course via the 5.13 lint (the
manifest is the build contract), and the conversation via provenance.
When this document and a manifest disagree about a particular course,
the manifest wins; when a manifest and the built course disagree, the
lint says so.

**Writes happen at phase close (§7).** Gates close in conversation;
records land when a phase closes, in one write moment — with one
deliberate exception (reopen sweeps, §5). Nothing in this document
licenses silent mid-phase record edits.

**Template-conformance BY CONSTRUCTION (named principle, S3-D9.5).**
This workflow and the template-v2 pass converge on one artefact:
courses produced through these gates are template-conformant because
the gates' authorities (skeletons, palette, component specs) are the
same artefacts the templates are generated from — conformance is not
a separate checking step performed twice. The 5.13 lint checks the
result; v2 never happens twice.

## §1 Phase A: identity & context

One session (gate model §4). Three conversational movements per the
gate model §3's confirmed Phase A structure; hard-stops individually
addressed (shared message, separate asks, never a composite yes),
soft gates weave into flow feeding the tally, advisories stated at
the moment they apply.

**Gate index (identity only — hardness, default types, dependency
edges live in `design-kb/design-kb.gates.json`; consult it, don't
trust this table for anything but order):**

| Movement | Gates |
|---|---|
| 1 Identity | CTX → A1 → A2 → EXM |
| 2 Architecture | A3, A4, A5 |
| 3 Furniture | A6, A7 |

EXM applies only where CTX closed the `school` facet specifically —
see `gates/EXM.reachabilityFacet` in `design-kb/design-kb.gates.json`.
Institutional is a superset (institution, faculty, school, module): an
institution- or faculty-only declaration does not reach EXM, nor does
a baseline or discipline-scoped course.

### Movement 1: Identity

**CTX — Context facet set (hard-stop, S1-D4; interior per S3-D2).**
One gate closes the whole facet set. The adaptive interior is a
parse-and-derive pipeline, never a question tree:

1. **Parse** Abbott's opening declaration; classify every facet
   (S1-D3 model: core pathway/tier; contextual subject/level;
   institutional institution/faculty/school/module; floating
   activity) as *declared*, *derivable*, or *silent*.
2. **Questions — two types only.** Core-completion (pathway or tier
   missing — they are mandatory) and signal-disambiguation (the
   declaration contains a signal the AI cannot classify). Everything
   else is derivation or silence; absence is silent by design.
3. **Derive, from kb records only.** Module = deepest derivation
   (institutional-kb → institution, faculty, school, level
   singleton, subject tags — each citing its kb entry). Subject-only
   = CAH classification at the most specific justified tier (S1-D9
   walk-up). Faculty/school = only what the kb record carries.
   Activity homed by module-tie. **The AI never derives from world
   knowledge and never guesses; it may suggest, visibly labelled as
   suggestion, checked before close.**

   > **Note, 18 September 2026 (DL-1, `docs/project/open-decisions.md`).** Superseded: CTX does not close a subject facet, and the subject-only CAH-classification derivation named here is not implemented anywhere in the repo. Discipline variation is authored into the context pack and merged by `merge-context.js` instead. S1-D9's CAH scheme is held as a deferred intention. Prose left unedited above as the historical record.
   >
   > **Correction, 18 September 2026 (DL-1 AMENDMENT, `docs/project/open-decisions.md`).** The note above is wrong on its main point. CTX DOES record the subject facet; S1-D9's CAH scheme is live, not deferred. The subject-only CAH-classification derivation named above still cannot run — no CAH1 group vocabulary exists anywhere in the repo, so the facet's recorded shape is unresolved and no course may record one until it is settled — but that is a gap in the shape, not a reason CTX withholds the facet. See DL-1's amendment for the full reasoning. Prose above left unedited as the historical record.
   >
   > [Note, 29 September 2026 (adp-0192): the gap this correction names is closed. DL-1 SHAPE
   > RESOLUTION (`docs/project/open-decisions.md`, 18 September 2026) settles the subject facet's
   > recorded shape, and the vocabulary is landed, not retyped: `vocab-kb/cah.json` (commit
   > `3c30255`) carries HESA's CAH data. HSV-1 (`docs/project/open-decisions.md`, 26 September
   > 2026, Prompt adp-0184) rebuilds that store complete for all three CAH levels, superseding
   > the scope-limited CAH3 note DL-1 SHAPE RESOLUTION originally carried. The correction's prose
   > above stays as the historical record; this note does not amend it in place.]
4. **No-source-match (S3-D3 seam).** A resolved lookup is read, not
   merely cited: consulting a source means opening the cited section,
   and the gate's grounding names what was read, not only that a
   record existed. A failed lookup is declared in
   the discovering turn — store, lookup, what a hit would have
   grounded — and recorded as a `groundingGaps` entry (amendment A5)
   on the gate record. Declarations stand without kb corroboration;
   derivations fail empty; direct declaration is offered inside the
   gap statement. The gate still closes; gaps feed the sourcing list
   at phase close.
5. **Close: one restatement + one set-level confirm.** Every value
   marked declared / derived-with-citation / defaulted, carrying the
   CONSEQUENCE LINE — the S1-D2 facet→store mapping read out, so a
   forgotten facet is visible by absence. Confirm is conditional on
   full visibility of every derived value. Baseline and happy-path
   module declarations each take one AI turn.

Record: decidedValue = the facet set; derivation trail in grounding;
the restatement in originalProposal. A mid-course facet change is the
paradigm upstream reopen — §5.

**A1 — Vocabulary & naming (hard-stop).** Confirm before anything is
built on the names: pathway name against
`docs/curriculum/pathway-tier-mapping.md` (the authority, not memory
or conversation); tier naming per the confirmed convention
`<Pathway>: <Tier> Stage`; the slug stated explicitly with its
slugification rule, never left to emerge from the first filename.
(Academic Writing Beginner's "Beginner" naming remains the recorded
one-off exception pending its retrofit.)

**Manifest creation — `/new-course` (once per course, between A1 and
A2).** CTX and A1 are answered before any file exists: nothing in
`courses/` names this course yet, so there is nothing for `/gate` to
read against nor for `/land` to append to. Once both are closed,
`/new-course <slug>` writes `courses/<slug>/course-design_<slug>.json`
for the first time from exactly those two closed records — the one
exception to `/land`'s append-only, string-asserted-edit invariant,
kept on its own command surface rather than folded into `/land` so
that invariant stays literally true everywhere else (PR-S-51). It
projects CTX's `decidedValue` onto the schema's `facetSet` shape
(`schemas/common.schema.json`) rather than copying it verbatim —
`decidedValue` legitimately carries keys `facetSet` does not allow
(`additionalProperties: false`) — and never invents a facetSet value
of its own. A2 is the first gate opened against the manifest this
step writes.

**A2 — Curriculum scope & source (hard-stop).** Scope from
`pathway-tier-mapping.md`; tier boundary per the tier model
(complexity and prior experience, not credit level). Source type:
book-derived (eleven of thirteen pathways — identify chapters) or
authored (AI & Technology, Creativity — institutional/sector sources,
recorded per Track B provenance). Source consultation obligations
from the CTX facet set (S1-D2) attach here and run through every
downstream gate.

**EXM — Exemplar programme set (hard-stop; reached only where CTX
closed the `school` facet — see `gates/EXM.reachabilityFacet`).**
Which three programmes from the declared school stand as the
exemplars for every context slot in
this course. Read against `docs/contexts/cmet/cardiff_met_courses.csv`
(filtered by the school facet CTX closed) and the decode table at
`docs/contexts/cmet/cardiff_met_schools.json`, both as a picklist,
never cited as a source. Ruled 17 Sep 2026 (Abbott): its own gate,
not a refinement of A5 — a wrong set cannot be amended afterwards,
since every context slot is written against it. How a pack spends
the set is deliberately left open (PR-S-17, PR-S-23).

### Movement 2: Architecture

**A3 — Lesson breakdown (hard-stop).** The course's teaching units,
proposed against the source scope confirmed at A2. The first
lesson's `pageKey` is `L01`; lesson keys run consecutively from
there with no gaps (LN-1, `docs/project/open-decisions.md`,
19 September 2026).

**A3 also records each lesson's book sections (BKS-1,
`docs/project/open-decisions.md`, 20 September 2026).** For each
lesson, one or more book sections: the chapter number, the chapter
title, the section heading quoted exactly as in the book, and the
page range. This is SF-1's passage source until a book map exists;
when one exists, A3 picks from its chunks and the record keeps this
shape. The lesson's Lesson Sources book citation (PLR-1 AMENDMENT)
is drawn from it. Record shape:

```json
{"lesson": "L01", "bookSections": [{"chapter": 10, "chapterTitle": "...", "heading": "...", "pages": "pp. 00-00"}]}
```

**A4 — Visual overview (soft; VO-1-as-gate).** The old workflow's
VO-1 palette step is this gate: choose the pathway's visual-overview
treatment from the VO-1 palette (open-decisions #32 — hotgraphic,
narrative, timeline, flipcard, text-only), once per pathway. A slot
decision, so the S3-D4 grammar applies: pattern → realisation →
coupling, three citations, S3-D6 pre-flight against the component
spec before the proposal is uttered.

**A5 — Context-coupling plan (soft).** Where and how deeply this
course couples to the declared context facets; per-slot activity-floor
overrides (S1-D3) available downstream. Stays soft per GI-1e.

### Movement 3: Furniture

**A6 — Confidence item set (soft).** The tier's confidence
statements (cap 10, WR-2a; five-pattern feedback per WR-2d), AND the
per-course ruling on the optional C-POST reflective bridge — off by
default programme-wide, enabled here per CC-1c (obvious candidates:
reflection-heavy pathways). The old workflow's optional-bridge step
is this gate.

**A7 — Resources drawer (advisory).** Stated when it applies (RF-1:
consolidated references at W-CLOSE only; sourcing log feeds it).

### Phase close

Full ledger + assumptions tally presented for blessing (gate model
§4); the sweep is the write moment (§7). Any groundingGaps recorded
this phase are read out with the sourcing-list feed named.

Once every hard-stop gate here is `closed` or `skipped`, run
`/scaffold <course-slug>` (SG-1, `docs/project/open-decisions.md`,
18 September 2026) to generate the course's structural shell before
Phase B (§3) opens.

## §2 Course shape

**Standing course shape (S3-D9.1, sourced CC-1/WC-1).** Every course
is the fixed structural sequence around a content-driven lesson
count:

    W-OPEN → C-PRE → lessons → SUMM → C-POST → W-CLOSE

Five structural pages, one instance each per tier, unnumbered in the
menu (28 July decision); lesson count decided at A3, content-driven
(source structure tested against the six-part flow; 4–8 typical).
The pilot instantiates this at six lessons — eleven pages total, the
shape's first proof. Sequencing constraint WR-2c stands: SUMM
renders before C-POST; the POST never reads another component's
score. The bridge, where A6 enabled it, rides C-POST per CC-1c.

**Archetypes and skeletons.** The structural pages and the lesson
shape are ARCHETYPES, defined once in `design-kb.skeletons` (S1-D7:
skeletons are simultaneously the 5.13 lint's conformance manifests —
one artefact, two consumers). A course's manifest carries archetype
INSTANTIATIONS — pointers plus per-course values — never structure
bodies (S1-D5). Skeleton population is return-week work; until it
lands, the authoring templates remain the working reference with
their recorded caveats (F7 on summative-template.md: SUMM furniture
is specified from the backlog 14 Aug records, §4, never from that
template). Deviations from an archetype are recorded in the
instantiation's `notes` — the lint consumes them (§6) so an honest
deviation is never a surprise.

**Folder discipline (carried forward, 22 July).** Every course gets
its permanently-named folder from day one, `courses/<course-slug>/`
— possible because A1 confirmed the final slug before any content
existed. The folder changes status as the course matures, never
name.

**Registry as generated view (S3-D9.9 / S1-D6).** Authority for page
lists and course status is the MANIFEST. `lesson-registry.json` is a
generated view, regenerated from manifests, never hand-edited;
`latestTrackingId` moves to a tooling-owned build-state file.
Regeneration tooling is return-week, VERIFY-ON-RETURN; until it
lands, registry entries are written by the build task mechanically
from the manifest — same authority direction, manual mechanism —
and are still never hand-edited outside a build task. The
sourcing-list (S3-D3's groundingGaps feed) follows the same
generated-view direction, its tooling riding the same return-week
item.

## §3 Phase B: lesson design

One session per lesson (gate model §4, matches per-lesson design
rhythm and context-exhaustion discipline). Two movements per GI-1c,
confirmed unamended by the L03 walk-through (S3-D8):

| Movement | Gates | Concern |
|---|---|---|
| Substance | B1, B2, B3 | outcomes and lesson frame (LF-1), knowledge structure, worked example |
| Interaction | B4, B5, B6, B7 | check, reflective prompt, pacing, visual assets |

The split never implies movement isolation: B4-on-B2 is a real,
machined constitutive dependency edge (GI-1d/gate-model §5.3) — a
substance change can invalidate an interaction decision, handled by
the sweep (§5), not by pretending the movements don't touch.

**Clarification recorded with the split (S3-D8):** page block ORDER
is B2 territory (knowledge structure decides sequence); B6 owns
revelation PACING over that sequence (trickle/gating timing). A
lesson's known order-deviation is a B2-class fact, not a B6 one —
record it there.

**B2 absorbs interactivity-design (S3-D9.2).** There is no separate
interactivity step. Choosing the interior pattern (the realisation
is drawn from the matched activity-pattern's own `realisations` list
in `design-kb.activity-patterns.json`, per the proposal grammar
below — never a free-picked list here; before proposing a new custom
component), selecting it with course-wide variety in view rather
than per-lesson isolation, and recording the reasoning (not just the
choice, so a future lesson can avoid copying this one's shape by
default) are all part of closing B2.

**B2+B3 batch in one shared message with separate asks** (gate
model §3's shared-message-separate-asks discipline): each still
needs its own explicit response.

### The proposal grammar (S3-D4/D5/D6) — the standard for every
### activity/interaction gate (B2, B4, B5, S1 furniture; "activity gate"
### = any gate deciding a slot realisation)

**0. Shape reading (SF-1).** Before naming any pattern, name the
content shape or shapes for this slot from
`design-kb/design-kb.content-shapes.json`, quoting the book passage
that shows each shape (until a book map exists, drawn from the book
section recorded for this lesson at A3). Candidate patterns in step 1
below are restricted to those whose `servesShapes` includes the named
shape; the existing filters on slot type, tier and intent then apply.
The shape id and the quoted passage land in grounding beside the
pattern.

**1. Pattern-led triple (S3-D4).** One utterance, three fixed
layers, pattern always leading:

- **Pattern** — an `activity-patterns` entry, intent (formative or
  summative — same grammar, no second form) and tier calibration
  cited from the entry.
- **Realisation** — a palette component drawn FROM the pattern's own
  realisations list, never free-picked.
- **Coupling** — a variation type from the entry's contextAffinity
  plus the kb entry the content draws on; baseline still cites
  variation type "generic" so every record has the same shape.

All three citations land in grounding; decidedValue is the triple;
ONE gate record per proposal — amending any layer makes the whole
record human-amended. A proposal that cannot name its pattern is
MALFORMED, not weak; the same for a realisation outside the
pattern's list or an unsupported coupling.

**2. Recommendation + alternatives (S3-D5/S1-D11 AMENDMENT), asymmetric.**
The lead is the full triple above. One to three ALTERNATIVES accompany
it as pattern-level sketches with a one-line why-not — never full
triples. Alternatives are drawn MECHANICALLY, in shape order: first,
other patterns serving the same shape named at step 0; then, only if
the content shows a second shape, a pattern serving that second
shape. Each candidate, whichever shape it serves, is still subject to
the same slot type, tier and intent filters as the lead, ranked by
contextAffinity against the declared facets, top 1–3. Zero survivors is stated honestly, not
papered over — and a repeated zero-state is logged as pattern-store
population evidence (a conversational note plus a records line, no
machinery). Why-nots are FIELD-GROUNDED: a comparative line citing
an actual entry-field difference, or left unsaid rather than
invented. Picking an alternative promotes it to a fresh full triple;
the old lead is preserved in originalProposal (human-amended).

**The ask is always the standard gate ask** — never a menu, never
"which would you like?" A menu-of-equals would force a choice at
every activity gate and destroy the silence-passes path (S3-D2
reaffirmed, S1-D11b stands). The human's low-effort path is
unchanged: silence passes soft gates (ai-default-stood, tallied,
bulk-blessed at phase close); one word — "confirm" — passes
hard-stops.

**3. Constraint-aware pre-flight (S3-D6) — runs BEFORE the proposal
is spoken, not after.** Verify the specific proposed shape against
the component spec the palette points to — caps, interaction/
feedback structures, required children — never the palette's
register notes alone, never AI memory. A failing shape is never
uttered: adjust within the pattern, or take the next listed
realisation. The consulted spec joins grounding as a prose citation
(`{doc, ref}`, F9 stable-anchor form — no line numbers). A missing
spec reuses the F1 policy by name: propose the next realisation with
a reachable spec, or state the blockage plainly; the record cites
the nearest real authority plus the backlog. This is deliberately
NOT a groundingGaps entry (those are scoped to sourced external
stores, S3-D3) — a missing spec is the project's own documentation
debt, and its home is the backlog, not the manifest's gap ledger.

### Per-lesson session discipline

One lesson, start to finish, per session (matches the per-lesson
design rhythm above). Recovery from a dead session is bounded by the
last written manifest plus the ledger — "show me the ledger" is a
standing command, answerable at any point without re-deriving state.

## §4 Summative & wrappers

### SUMM furniture (S3-D9.6)

**Never source SUMM specifics from `summative-template.md` (F7):**
that document predates the 14 August changes and is actively
misleading about marking, feedback, and furniture. The authoritative
SUMM record is `project-backlog.md`'s 14 August APPEND LOG entries;
where no resultsdebrief spec exists, cite `passreveal.md` plus the
backlog entry in its place (F1's policy, reused here by name — the
same substitution S3-D6 formalised for a missing component spec).

**Standard furniture, every SUMM, both directions:**

- **`adapt-abbott-resultsdebrief`** — post-submission "Where to focus
  next" section, grouping incorrect answers by lesson (deduplicated),
  with a pass-reveal note on pass. Fires on `assessments:complete` +
  `assessment:restored` + `componentView:postRender`, gated by a
  three-link guard chain (enabled flag → assessment ID match →
  completion state).
- **`adapt-abbott-pass-reveal`** — model answers revealed on the
  assessment's questions once passed, gated by its own three-link
  guard chain (enabled flag → assessment ID match → `isPass`).

**Marking and feedback, per the 14 August fix:** `_suppressMarking:
true` (marking withheld until every item is answered);
`_canShowFeedback`/`_canShowMarking: true` on the article and every
component; every `_incorrect.notFinal` string carries a remediation
pointer naming a specific lesson — remediation-first, never an
answer-reveal, which is what makes the retry policy below acceptable.

**Item-to-lesson mapping is authored per course**, not templated:
each SUMM item maps to the lesson(s) it draws on (the pilot's
8-item, 3-lesson mapping is the worked example, not a fixed
shape) — record the mapping in the gate record's grounding so
resultsdebrief's configuration and the manifest agree.

**Coverage is a standing watch, not a gate failure:** a SUMM that
doesn't cover every lesson is not itself a fault (the pilot omits
three lessons deliberately) — but log it as a watch item feeding the
backlog, per the pilot's own precedent.

### Retry policy (S3-D9.7)

> **Superseded (SVP-1, `open-decisions.md`, 20 September 2026).** The
> capped-attempt-count lever named below as a future decision has now
> been taken: three attempts at the whole test, reshuffled on each
> attempt, unlimited tries within a single attempt
> (`assessmentDefaults.attempts`, `design-kb.skeletons.json`; written
> by `tools/generate-course-shell.js` into the SUMM article's
> `_attempts`/`_randomisation`). The grinding risk the paragraph below
> names is mitigated by both the pre-existing remediation-first
> feedback and this new cap. Prose below left unedited as the
> historical record, per this document's own convention of visible
> supersession rather than silent correction.

**Unlimited SUMM retries stands, as-is, for now.** Grinding — visible
marking plus unlimited attempts permitting memorisation of correct
answers rather than genuine remediation — is an acknowledged risk,
mitigated for now by remediation-first feedback (lesson names, never
answers). It is a **logged watch item (5.14)**, not a gate condition:
nothing in this workflow blocks a course on the grinding question.
The stated lever, if analytics ever show grinding: switch to a
capped attempt count plus a review-first message in the lowest
score band. That switch is a future decision, not a default to
pre-empt here.

### W1 — Wrapper content

Wrapper architecture is fixed (WR-1 cluster): W-OPEN / W-CLOSE
naming, ID convention `W-OPEN-b-NN` / `W-CLOSE-b-NN`, both
unnumbered in the menu. **W-OPEN's block order is overview, then
course learning outcomes, then practice connection, then signpost,
then the fixed course-instructions block, then course conventions
(WOS-1, `open-decisions.md`, 20 September 2026, superseding the
14 August reorder that put learning outcomes first — that order is
in turn retained in `open-decisions.md` as a visible supersession,
never silently corrected).** The course-instructions block is new
under WOS-1: fixed, generator-written shell text (a `{{passMark}}`
substitution included), sitting between signpost and course
conventions. The Signpost block's visual-overview component is
decided at gate A4 (§1), not here — W1 states the content, A4
decided the treatment.

W-CLOSE carries four blocks in render order: course summary,
practice connection, where-this-goes-next, course sources (RF-1
references, sourced from the sourcing log built during authoring,
§7; displayed title "Course Sources" per SVP-1, `open-decisions.md`,
20 September 2026 — "further reading" above was this document's own
working name for the block, not its displayed title). Confidence
PRE/POST no longer live on the wrappers — they are C-PRE/C-POST,
decided at gate A6 (§1); a course's W1 record should not re-litigate
that placement.

Gate W1 closes the CONTENT of course summary prose and what's-next
framing; it does not reopen the architecture, which is closed by
design, not by this gate. Practice-connection content is not among
them: DR-1 (20 September 2026) rules it is written at D1, not W1.

## §5 Revision & sweeps

**This section is the CONVERSATION over settled mechanics — it
never restates them.** The machinery (dependency representation,
verdict vocabulary, assignment, change-kind recording, choreography,
history shape) is fixed in `gate-conversation-model-draft-v1.md` §5
(S2-D1–D7, all hard-stops, human-confirmed). Consult it directly for
mechanism; this section only choreographs what the human sees and
says.

### The two-beat grammar (S3-D7)

**Reopens are always NAMED before anything runs.** No silent
re-entry into a gate.

**Beat one — scope preview.** A compact preview drawn from the
STATIC dependency edges alone (`design-kb.gates.json`'s `dependsOn`,
the sweep net's safety floor per §5.2 of the gate model) — no
record-reading at this beat. Per-gate detail available on request.
The ask is proceed or withdraw.

**Re-close.** Each swept gate re-closes through its own normal
interior, under its own hardness — CTX re-enters the S3-D2 pipeline
in full (§1), an activity gate re-enters the S3-D4/5/6 proposal
grammar (§3). changeKind is captured per the gate model's §5.5
(amended/replaced/re-deferred; recorded, never mechanised).

**Beat two — disposition, ONE message, grouped by verdict grade,
fixed order:**

1. **Invalidates first** — individually named (edge, one-line why,
   the record evidence that argued against the default, stated as
   grounding — the relocated middle tier from the gate model's §5.3).
   Each needs the human's explicit word; these behave like
   hard-stops regardless of the swept gate's own native hardness.
2. **Flags second** — a labelled bulk-confirmable set, named
   exceptions callable out individually.
3. **Warnings last** — silence stands, same as any soft gate.

The §3 shared-message-separate-asks discipline holds throughout: one
message, but every ask keeps its own explicit response where the
grade requires it.

**Write moment — narrated, not silent (deliberate exception to
write-at-phase-close, §7).** State the event summary (sweep id,
trigger, dispositions, any open obligations) and write immediately;
the gate model's mid-phase exception is stated aloud, not assumed.

**Aftermath is agenda, not silence.** Confirmed invalidates re-enter
as open gates in the stated order. Flag obligations ride the
standing ledger — "show me the ledger" surfaces them alongside
everything else.

### Cascade rule (S3-D7, new substance)

A swept-invalidated gate that re-closes with a **changed** value
triggers its own preview-plus-sweep — recursion through this same
two-beat grammar, one sweep event per actual movement. Recursion
terminates the moment a re-close reinstates the SAME value: no
movement, no further sweep. This is deliberately not a
transitive-closure sweep run upfront (no speculative dispositions on
ground that hasn't actually moved) and not a per-record dialogue (a
grade-grouped beat two is what makes an 8-record sweep one exchange
instead of eight).

### Named cases

The gate model's bracketing cases stand: a **CTX facet change** is
the paradigm upstream reopen (the facet set grounds the entire
conversation, S1-D4) and propagates via `propagationScope: universal`
— no enumerated edges, deliberately, since CTX single-homes every
downstream gate. A **core-facet change (pathway/tier)** is not a
revision at all — it is a different course, out of this section's
scope entirely (S2-D5).

## §6 Verification & build-readiness

### Evidence standard (S3-D9.8)

**No model writes during evidence runs.** Every claim of working
behaviour is proven through real UI events — clicks, real form
input, real navigation — never through direct `model.set()` or
equivalent state injection. A prior session's own test state was
corrupted this way (SUMM evidence runs, 14 August); the rule exists
because of that specific failure, not as abstract caution.

**Evidence is concrete DOM values, never pass marks.** A green
checkmark or a "PASS" label proves nothing on its own. Acceptable
evidence names the actual attribute, value, or count observed —
`.resultsdebrief` count === 1, `_canShowModelAnswer: true` on all 8
questions, a specific score percentage achieved through real
answers. Playwright evidence follows this standard throughout: every
verification claim in a gate record's grounding should be traceable
to a concrete observed value, not a summary of one.

**Verification precedes the claim, not the reverse.** A session that
first reports a summary and only supplies verbatim evidence when
challenged has already broken the standard once (S3 thread 1's own
honesty item, A5 landing) — recon, full diff, and concrete
before/after values are given unprompted, not on request.

### 5.13 lint — three clauses (S3-D9.10)

The conformance lint has three distinct obligations, all required,
none optional:

1. **Consumes instantiation `notes`.** A recorded deviation from an
   archetype (§2) is read before flagging — an honest, notes-carrying
   deviation is never treated as a surprise. Without this clause the
   lint false-positives on any deliberately-recorded departure.
2. **Refuses on unresolved sweep events.** Build-readiness is
   derived, never stored: any `sweepEvents` entry left with an
   unconfirmed invalidate or flag blocks the build outright (§5's
   choreography assumes this is where its teeth are).
3. **Reports groundingGaps informationally — never refuses on them**
   (S3-D3). A gap is an honest closed state (the gate closed, the
   source didn't), categorically different from an unresolved sweep
   event. The lint surfaces gaps for the sourcing list (§7); it does
   not hold the build hostage to sourcing, which is weeks-scale work
   by design.

The manifest is the build contract (S1-D5): the lint's job is
checking the built course against the manifest's decisions, on all
three of the above axes, not against this document or any template
directly.

## §7 Records discipline

**Writes happen at gate-group close, with one deliberate exception —
this supersedes the original one-write-per-phase rule (8 Sep 2026
venue/cadence/provenance ruling, part 2).** Gates close in
conversation; the write is a separate, later act — the ritual (gate
model §4): the full ledger (every gate, state, provenance) plus the
assumptions tally presented for final blessing, swept by the human,
THAT sweep is the write moment. Cadence is one commit per gate group:
one Phase A movement (Identity, Architecture, or Furniture; §1), one
lesson's Phase B (§3), or one of S1, W1, D1 (§4, §8) — matching
practice already in place since R37 (7 Sep 2026); the ruling records
the practice rather than changing it. Nothing in this document
licenses a write outside a gate-group boundary.

**The sweep exception (§5).** A reopen sweep's write is its own
moment, narrated at the point it happens, not deferred to the next
phase close. This is the one place mid-phase writing is correct
behaviour, and it is stated aloud each time so it never reads as a
slip from the phase-close discipline.

**groundingGaps feed the sourcing list.** Every gap recorded via
amendment A5 (S3-D3: a no-source-match, declared in the discovering
turn, store + lookup + what a hit would have grounded) is read out
at the phase close that contains it, and feeds Abbott's sourcing
list — the manifest stays authoritative; the list is a generated
view (S1-D6's direction, same as the registry, §2). Gap arrival at
sourcing time is recorded as ordinary supersession when the source
lands, never mechanised into an automatic re-sweep (S2-D5's
record-not-mechanise pattern: sourcing is evidence arriving, not a
decision moving — no dependency edge fires on it).

**Delegation-regrade path (S3-D1).** There is no delegation mode:
every hard-stop requires the human's explicit word, at every
instance, with no bulk-delegable escape. The one relief valve is
structural, not procedural: if a hard-stop repeatedly feels
delegable in practice, that is evidence for a hardness REGRADE,
raised and settled through an ordinary records entry (the GI-1e
precedent — A5's soft-grading ruling is the worked example). Grading
questions go through records, on their own gate, at their own pace;
this document does not build a bypass mechanism to route around a
hard-stop that feels burdensome in the moment.

**Provenance vocabulary is closed, to eight values (GI-2,
`docs/project/open-decisions.md`, 27 Aug 2026; `schemas/common.schema.json`'s
`provenance` enum description states the enum directly).** Every
closed record's provenance is one of the standing values
(human-confirmed, human-specified, human-amended, ai-default-stood,
ai-proposal-stood, advisory-stated, fixed-default, deferred) — never
a new value invented to describe an edge case (the S1-D12/S2-D3
protective logic, reaffirmed at S3-D1: a delegated hard-stop cannot
be marked honestly within the existing vocabulary, which is exactly
why delegation isn't built). Where a reconstructed record's basis is
`inferred` rather than `documented` (S1-D12), provenance is omitted
rather than guessed.

**"Show me the ledger" is a standing command**, answerable at any
point without re-deriving state, per the gate model §4. This
document's own recovery discipline rests on that command working
correctly at every session boundary.

## §8 WF-B: existing course, new context

A second workflow, distinct from §1–§7's course build: authoring a
new context pack for an EXISTING, already-closed course. The
manifest is read ONLY — no shell edits. The new pack's shape is
copied from the baseline pack (the course's existing context
instantiation), never invented fresh. One D1 record per context
authored. Run via `/new-context`. If the work turns out to need a
shell edit — a structural change, not a context substitution — that
is a REOPEN, not a WF-B task: it returns to §5's sweep grammar rather
than proceeding as a context pack.
