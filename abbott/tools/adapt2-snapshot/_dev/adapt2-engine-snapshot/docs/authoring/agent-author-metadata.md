# Agent-author metadata

Status: **partially landed (10 Oct 2026).** The unified `agentAuthor` shape below
is live in the skeletons schema (`design-kb.skeletons.json`, kbVersion 0.1.32),
**consumed** by `tools/resolve-agent-author.js`, which the `/gate` (5b) and
`/land` (step 4) skills now call before proposing or authoring a slot. It is
populated on **all 21 authored slots** across every page type — every teaching,
framing, outcome, concept, worked-example, practical-guidance, check, reflective,
summary, assessment and references slot. The only slots without it are the seven
`role: furniture` blocks (signpost, course-instructions, course-conventions,
confidence-pre/post, summative introduction and results), which are
generator-written and carry no authored prose. Teaching slots carry a live
`byTier` steer (framing by stage, concept depth, Bloom level, example complexity,
reflection depth…); the two reference slots carry a baseline with no `byTier`
(references do not vary by tier). Every populated slot carries the empty
`byQualifier`/`bySubject`/`byInstitution` placeholders. Still pending: CXP pack
slots and the manifest-level block; populating the reserved steers as CXS / cxp-02
/ institutions land; and the migration of `standingContextPrompt` / pack `_prompts`
into it (see Migration). This defines a scheme for instruction metadata that steers an AI
authoring agent as it fills a slot; changes go through the `kbVersion` + validator
route (see Governance).

Field names are camelCase, to match the existing store keys (`standingContextPrompt`,
`slotType`, `contextCoupling`).

## Why

The page flow already carries one agent-instruction string per coupled slot:
`standingContextPrompt`. It is useful but narrow:

- a single flat string, with no place for pitfalls or best practice;
- aimed only at the context-pack agent filling a coupled slot;
- present only on coupled slots;
- silent on how a slot relates to the slots around it.

The manifest flow carries no authoring instruction at all. The result is that
hard-won lessons (for example: *keep MCQ distractors parallel in length to the
key, or length alone flags the answer*) have nowhere structured to live, so they
are re-learned per course.

This scheme generalises `standingContextPrompt` into a layered block that can
sit at slot level and at manifest level, and that distinguishes the **mode** the
agent is working in.

## The three fields

A layered block. `agentAuthor` is the mode-agnostic baseline and always applies.
The one mode field matching the agent's current mode is layered on top of it.

| Field | Applies to | Holds |
|---|---|---|
| `agentAuthor` | every mode (baseline) | What content the slot/field requires and *why*; its relation to the surrounding slots (what it follows, must cohere with, must not duplicate); common issues / warnings; best practice. |
| `agentAuthorWritten` | agents generating written course copy (this project) | Nuances specific to written authoring, layered on the baseline. |
| `agentAuthorDialogue` | agents in live chat dialogue with a human learner | Nuances specific to conversational delivery, layered on the baseline. |

### Shape

Each field is a small structured object, so its parts are individually
addressable and lintable rather than buried in one string:

```jsonc
"agentAuthor": {
  "content":      "What this slot must contain, and the reason it exists in the flow.",
  "relation":     "How it sits against the slots around it (follows X, feeds Y, do not repeat Z).",
  "warnings":     ["Common mistakes / failure modes to avoid."],
  "bestPractice": ["Positive directives."],
  "context": {                         // the agent's TARGETING LAYER: named steers
    "all":    "Base: how the course context (CXP subject/pack) shapes this slot.",
    "byTier": {                        // per-tier steer, selected first
      // each entry is a string prompt-formula, OR an object when the tier needs
      // structural control (applies:false omits the block; displayTitle /
      // sideways / forwardBack / an override of a baseline field)
      "introductory": "...", "intermediate": "...", "advanced": "..."
    }
    "byQualifier":   {},  // RESERVED, present empty & ready: per cxp-02 / CSP qualifier
    "bySubject":     {},  // RESERVED: per highest CAH grouping (CXS)
    "byInstitution": {}   // RESERVED: institutional framing + link-up
    //   fill any of these with { "<key>": "<string prompt-formula | structural object>" }
  }
},
"agentAuthorWritten":  { "notes": ["Written-mode nuances, layered on the baseline."] },
"agentAuthorDialogue": { "notes": ["Dialogue-mode nuances, layered on the baseline."] }
```

`context` is the **targeting layer**: a set of **named steers**, each a little
prompt-formula that narrows the agent's output. `all` is the base; `byTier` is the
first steer (per-tier, selected before the baseline→mode overlay). Three further
steers are **reserved and present as empty `{}` placeholders** on the live slots —
available to fill now (an empty steer validates), populated when their phase lands:
`byQualifier` (per CXP cxp-02 / CSP qualifier), `bySubject` (per highest CAH
grouping, from CXS — subject-grouping framing that shapes how the agent discusses
the content) and `byInstitution` (per institution — local framing, referencing
overrides and link-up to institutional modules/resources). A steer object may be
empty; fill it with `{ "<key>": "<string | structural object>" }` entries. A
`byTier`/`byQualifier` entry is a plain string, or an object when it also needs
structural control — `applies:false` omits the block at that tier (as advanced
`where-next` does), or it sets `displayTitle` / `sideways` / `forwardBack` / an
override of a baseline field. `context` written as a bare string is shorthand for
`{ "all": <string> }`.

A bare string is accepted as shorthand for `{ "content": "<string>" }`, so a
simple slot need not spell out the full object.

## Where it attaches

The same block shape is valid at two levels:

1. **Skeleton slot** — in `design-kb.skeletons.json`, on a slot object. Generic,
   tied to the page layout, and therefore inherited by that `slotType` in every
   course. This is the natural successor to `standingContextPrompt`; see
   Migration.
2. **Manifest** — in `course-design_<slug>.json`, either course-level (a default
   for the whole course) or on a specific `instantiation` (per realised
   page/component), for course-specific steering.

## Resolution order

For a slot authored in mode *M* (`written` or `dialogue`), the agent composes the
effective instruction most-specific-wins:

```
skeleton.agentAuthor
  -> skeleton.agentAuthor{M}
    -> manifest.agentAuthor
      -> manifest.agentAuthor{M}
```

Within that chain:

- **`warnings` accumulate** — the union of every level's warnings, de-duplicated.
- **Directive fields** (`content`, `relation`, and each `notes` entry's intent)
  **override** — a more specific level replaces, not appends, where they conflict.
- The baseline is always included; the mode field is included only for the
  active mode.

## Worked example — the `check` (mcq) slot

This is where today's distractor fix belongs:

```jsonc
"agentAuthor": {
  "content": "A question testing one lesson outcome, with teaching feedback - never a bare right/wrong.",
  "relation": "Tests the concept defined earlier in the page; do not introduce new ideas here.",
  "warnings": [
    "Keep distractors parallel in length and structure to the correct answer. If the key is a longer, two-clause definitional sentence and the distractors are short one-liners, length alone flags the answer - match their shape and rough length so only the content distinguishes the right option."
  ],
  "bestPractice": [
    "Every distractor defensibly wrong, and the feedback says why (teach, do not bark)."
  ]
},
"agentAuthorWritten":  { "notes": ["Apply the Voice Spec section 18 register check before treating copy as done."] },
"agentAuthorDialogue": { "notes": ["Pose the question conversationally; probe the learner's reasoning before revealing the key."] }
```

## Worked example — the `where-next` slot (series cross-links)

The close-wrapper `where-next` block ("Where this goes next") is the motivating
case for this scheme. Its content is not fixed prose: it depends on which other
courses exist in the series, and on this course's tier. The instruction belongs
with the slot, not re-decided per course:

```jsonc
"agentAuthor": {
  "content": "Point the learner to where this course leads next in the programme: an outline of the topics the other courses cover, so they can see the shape of the series.",
  "relation": "Terminal block of the close wrapper; follows the practice-connection block. Do not restate this course's own content - look outward to the series.",
  "warnings": [
    "Do not hard-code course names or links that may not exist yet. Reference sibling/next courses through series link tokens, so an unbuilt course resolves to a safe placeholder rather than a dead link.",
    "Keep it tier-appropriate: an introductory course points forward only; an intermediate or advanced course points forward AND back to the course it follows, giving that prior context."
  ],
  "bestPractice": [
    "Give a short outline of each linked course's topics, not just a title, so the learner can judge where to go."
  ]
},
"agentAuthorWritten":  { "notes": ["Resolve series link tokens to the courses that exist at build time; outline their topics in prose."] },
"agentAuthorDialogue": { "notes": ["Offer the next steps as a short menu and ask which direction interests the learner, rather than listing every course."] }
```

This surfaces a **new token family** beyond the existing `{{context}}` and
character tokens: *series link tokens* (e.g. `{{next-course}}`, `{{prior-course}}`,
`{{series-outline}}`) that resolve, at build/merge time, against the set of
courses that actually exist in the programme. That token work is a prerequisite
for the `where-next` slot to be fully agent-authored, and is tracked as an open
question below rather than specified here.

## How the agent consumes it

**The activation rule — the agent does not read every steer.** A context steer
applies ONLY where its key matches a facet that is *active* for this course. The
agent never walks all of `byQualifier` / `bySubject` / `byInstitution`; it reads
the entry whose flag is actually set, and ignores the rest (an empty steer, or one
with no entry for an active facet, contributes nothing — it is a ready
placeholder, not an instruction):

- `byTier[tier]` applies to **every** course (every course carries a tier), so the
  tier steer is **live now** — nothing else need exist for it to take effect.
- `bySubject[grouping]` applies only once **CXS** sets the highest-CAH-grouping facet.
- `byQualifier[q]` applies only for each qualifier the **CXP / CSP** set.
- `byInstitution[inst]` applies only when an **institution** facet is set.

So an author targeting an introductory psychology course reads `byTier.introductory`
(and, when they exist, the psychology `bySubject` and any set `byQualifier`), and
simply does not consult the steers whose facets are not in play.

1. Determine mode: `written` for course-copy generation, `dialogue` for a
   conversational delivery agent.
2. Gather the course's active facets (tier from the manifest `facetSet`; subject /
   qualifiers / institution when their phases have set them).
3. Resolve the effective block for the target slot using the activation rule and
   the order above — or call the canonical resolver, which does exactly this:
   `node tools/resolve-agent-author.js --archetype=skeletons/<type> --slot=<key>
   --tier=<tier> --mode=written` (or `--manifest=courses/<slug>/course-design_<slug>.json`
   to read the tier from the course). It returns `{ omit, content, context,
   relation, sideways, forwardBack, warnings[], bestPractice[], modeNotes[],
   applied[] }`; `omit:true` (a tier with `applies:false`) means do not author the
   block at all. `applied[]` names exactly which steers fired.
4. Treat `content` + `relation` as the brief, `warnings` as hard do-nots to
   self-check against before emitting, and `bestPractice` as positive guidance.
5. For written mode, the Voice Spec remains the single source of truth for voice;
   `agentAuthorWritten.notes` points at the relevant checks, it does not restate
   them.

## Pathway relationships and the tier overlay

The `where-next` slot has two sub-blocks, and each needs a different relationship
model to drive it. Both should be data-driven, not re-decided per course.

### Horizontal — "Put it into practice" (pathway to pathway)

Links to *other pathways* in the programme (e.g. Academic Writing, Criticality,
Reflective Practice). The data home already exists: `design-kb.pathways.json`
carries `pathways[].routes` (`feeds` / `drawsOn`, currently null). Proposal:

- Each pathway's entry declares a **weighted relationship to every other
  pathway** - a relationship table across the 13 pathways. Strength varies
  (strong / moderate / weak), and relationships may be directional.
- The "Put it into practice" block's `agentAuthor` selects the strongest-related
  pathways for this pathway and outlines how what was learned here applies there.
- Future: turn the outline into actual interlinks between courses.

Open design points: symmetric or directional relationships; how strength is
represented (enum vs score); whether the table is authored once centrally or
each pathway declares its own row (and the two are cross-checked for agreement).

### Vertical — "Go deeper on this topic" (tier to tier)

Links to *higher/lower tiers of the same pathway*, using the `tiers` dimension.
This block is **tier-dependent**, and the applicability differs by tier:

| Tier | Go deeper (up) | Look back (down) | Net effect on the block |
|---|---|---|---|
| Introductory | yes | - (nothing below) | forward only |
| Intermediate | yes | yes (prior-tier context) | forward and back |
| Advanced | - (nothing above) | minimal / omitted | mostly "Put it into practice" |

So at advanced, "Go deeper on this topic" largely does not apply, and the block
collapses towards the horizontal (other-pathway) links.

### The tier axis

The two sub-blocks above mean the scheme needs a **tier axis** alongside the mode
axis (`written` / `dialogue`). The `agentAuthor*` prompt the agent uses is
selected by `(tier, mode)`: a tier-keyed set of prompts, or a tier-applicability
flag per prompt, so that - for example - the advanced `where-next` prompt simply
omits the "go deeper" instruction rather than the agent having to infer it.
Resolution order (slot -> manifest, baseline -> mode) gains tier selection as a
prior step: pick the tier variant, then apply the baseline-then-mode overlay.

## Migration from `standingContextPrompt`

`standingContextPrompt` is the context-pack agent's filling instruction for a
coupled slot. It maps onto `agentAuthor.relation` (how the coupled follow-on
should relate to the generic part above it). Proposed path:

- Phase 1: add `agentAuthor*` alongside the existing `standingContextPrompt`;
  both present, no behaviour change for the context-pack agent.
- Phase 2: once consumers read `agentAuthor`, fold each `standingContextPrompt`
  into its slot's `agentAuthor.relation` and retire the old key.

## Governance

- `design-kb.skeletons.json` carries a `kbVersion`; adding the fields is a
  `kbVersion` bump plus a rule in the schema validator
  (`tools/validate-design-schemas.py`) so the new shape is checked, not just
  tolerated.
- The manifest carries a `schemaVersion` and is written through the
  `/gate` -> `/land` process; the manifest-level fields likely belong in a gate
  record rather than a hand-edit, and `tools/manifest-completeness.js` would gain
  a clause if the fields are to be required.
- Until both validators understand the fields, the scheme stays a proposal.

## Open questions

1. Should `agentAuthorDialogue` be in scope now, or reserved until a
   conversational delivery agent actually exists?
2. Do manifest-level fields belong on `instantiations`, or on a new per-course
   block, or both?
3. Is a third mode (context-pack filling) worth naming explicitly, or does
   `agentAuthorWritten` cover it with the migration above?
4. Series link tokens (`{{next-course}}`, `{{prior-course}}`,
   `{{series-outline}}`) for the `where-next` slot: what resolves them, when
   (build vs merge), and how does an unbuilt course resolve safely? This is a
   prerequisite for the `where-next` worked example above.
5. Horizontal pathway relationships: symmetric or directional? Strength as an
   enum or a score? Authored centrally as one table, or per-pathway rows that
   are cross-checked? (Extends `design-kb.pathways.json` `routes`.)
6. Tier axis mechanics: are `agentAuthor*` prompts tier-keyed variants, or one
   prompt with per-tier applicability flags? How does tier selection compose
   with the baseline-then-mode overlay (tier selected first, then mode)?
