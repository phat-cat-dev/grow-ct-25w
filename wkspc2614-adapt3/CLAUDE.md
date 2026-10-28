# CLAUDE.md - Academic Practice eLearning (adapt2)

Working rules for an agent operating this repo. For how the pipeline works, read
`docs/PIPELINE.md` first, then `docs/ARCHITECTURE.md` and `docs/RUNBOOK.md`.

## Before any command

Work from the repo root (confirm `pwd`). Writing files or running git from the
wrong directory creates stray files outside version control.

## What this project is

An academic-skills e-learning programme built with the Adapt Framework, packaged
as SCORM and delivered through Moodle. Content is a matrix of academic-practice
pathways at tiered pitches, sourced from *Excelling at University* (Dennis &
Abbott, 2026) and new material authored to the same voice. The taxonomy (13
pathways x 3 pitches) is settled; see `docs/curriculum/pathway-tier-mapping.md`.

## Golden rules (voice and content)

**Scope: these govern student-facing Adapt course content only** - the copy that
ships inside a course (components, blocks, wrappers, assessment items). They do
**not** apply to repo docs, skills, commit messages, code, or build notes. Do not
voice-check or em-dash-check anything that is not course output.

- All student-facing copy follows `reference/excelling-voice-specification.md`. It
  is the single source of truth for voice. Apply its section 18 register check
  before treating any copy as done.
- Explain the *why*, not just the what or how: every significant piece of advice
  carries its reason.
- British English. Harvard (Cite Them Right) referencing by default (overridable
  per subject: APA, OSCOLA). No em dashes. Address the student as "you".
- Structure each topic on the six-part flow: orientation, concept (example
  first), worked example, analysis, practical guidance, reflective prompt.
- You draft; a human subject-matter expert approves academic accuracy. Never
  present invented facts, statistics or citations as real. Mark fictional
  references as fictional in build notes, never in student-facing copy.

## Installing / updating Adapt extensions (critical)

Always run `npm run adapt-install`, never raw `adapt install`.

Raw `adapt install` silently wipes the locally patched vendor fixes in `src/`.
The npm script runs `adapt install` then reapplies the patches from `patches/`
via `scripts/apply-vendor-patches.js`. (Origin: `adapt-contrib-assessment` had a
`_banks` optional-chaining bug fixed only by a local patch; the patch must be
reapplied after every install until upstream ships the fix.)

## Adapt content model

Course > Content Object (page/menu) > Article > Block > Component. Authored as
JSON under `courses/<slug>/en/`: config.json, course.json, contentObjects.json,
articles.json, blocks.json, components.json. Every element needs a unique `_id`
and a correct `_parentId`. Keep referential integrity intact; the build and
`tools/verify-course.js` validate it.

## Component mapping (voice-aware)

- Teaching prose -> text component (mid-register, why-before-how)
- Worked example -> narrative component (third person, weaker example first)
- Reflective prompt -> opentext (1-3 genuine questions, "no right answers")
- Self-test -> question component + assessment (feedback confirms and gives the
  reason; never a bare "Correct" / "Wrong"). When authoring MCQ items (les-01
  check, wra-03 summative), follow `docs/authoring/mcq-authoring-guidance.md`:
  balance the options so the correct answer is not the longest/most qualified
  (no give-away length or specificity cue).
- Glossary/definitions -> accordion + tooltips (self-contained first sentence)
- Learning outcomes -> formal, Bloom verbs appropriate to the pitch

The authoritative routing is in `design-kb/design-kb.activity-patterns.json` and
`design-kb/design-kb.palette.json`, read by `/gate` at each gate.

## Build & package

See `docs/RUNBOOK.md`. In brief: `grunt build` compiles `src/course` (a symlink
to a `courses/<slug>/`) into `build/`; `package-scorm.js` zips it. Package the
contents of `build/` so `imsmanifest.xml` sits at the top level of the zip.

## Working conventions

- Commit to git before each build. One commit per file touched in a write
  session. Nothing is pushed without an explicit instruction.
- Portable-unit authoring: each lesson is a self-contained unit (clean,
  non-colliding ids, self-contained tracking, no hard dependency on sibling
  lessons). Wrapper framing is per-pathway-tier. See
  `docs/authoring/portable-unit-and-shell-format.md` and
  `docs/authoring/wrapper-and-portability.md`.
- One SCORM package per pitch; keep pathways modular.

## Guardrails

- **Pathway scope check.** The component-to-pedagogy routing was derived mainly
  from the writing- and critical-thinking-heavy chapters. Before authoring a
  pathway outside that group (exams, work-based learning, presentations),
  pressure-test the six-part flow against that pathway's own chapter first and
  flag gaps before generating JSON.
- **Tracking-behaviour check.** Any claim about SCORM/completion behaviour (e.g.
  a reflective opentext being optional and never blocking completion) must be
  verified empirically with `grunt server-scorm`, not assumed.

## Verification discipline (the short version)

- **Prove, don't claim.** A claim that something was built or fixed is shown in
  the same response: the file content or diff, plus one real run with real
  output. A description is not proof.
- **Use the canonical tool.** If a task names a tool (`voice-lint.js`,
  `validate-design-schemas.py`, `conformance-lint.js`, `verify-course.js`), run
  that tool. If it fails for environment reasons, say so; do not quietly
  substitute something else and present it as equivalent.
- **Verify before "done".** A fix that looks right in code, or passes the local
  server, may still fail in Moodle. Keep "fix applied" and "verified" distinct.
- **String-asserted edits.** Edit existing files by asserting the exact current
  string before replacing it, so drift surfaces as a failed assertion rather than
  a silent wrong-target write. Never target by line number.
- **End verification commands with a visible exit code** (`; echo "EXIT: $?"`).
  Silence is not a pass.
