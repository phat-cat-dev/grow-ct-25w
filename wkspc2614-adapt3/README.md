# Academic Practice eLearning (adapt2)

An academic-skills e-learning programme built with the
[Adapt Framework](https://www.adaptlearning.org/), packaged as SCORM and
delivered through Moodle. Content is a matrix of academic-practice **pathways**
at tiered **pitches**, sourced from *Excelling at University* (Dennis & Abbott,
2026) and new material authored to the same voice.

This is a clean rebuild of the earlier project: the working pipeline, stores,
tools and skills, carried over without the accumulated session logs, audit
trails and superseded working-docs.

## What it does

It turns a **pathway + pitch** (a topic and a level) into a **SCORM package**, in
three stages:

| Stage | What | Output |
|---|---|---|
| **A - consult & specify** | a guided gate conversation (6 phases: ONB, CXS, CRS ...) | the **manifest** (`courses/<slug>/course-design_<slug>.json`) |
| **B - build** | scaffold the shell from the manifest, author lessons/wrappers, generate a subject context pack, compile | the compiled course (`build/`) |
| **C - test & package** | verify, lint, package, hand off | the **SCORM package** (`scorm-packages/`) |

Read **`docs/PIPELINE.md`** first - it is the one authoritative description of
the whole flow. Then:
- **`docs/ARCHITECTURE.md`** - where everything lives; which tool reads/writes what.
- **`docs/RUNBOOK.md`** - the exact commands to build a course end to end.
- **`CLAUDE.md`** - the working rules for an agent operating this repo.

## Taxonomy

13 pathways x 3 pitches (introductory / intermediate / advanced). The pathways
are in `catalogue/pathways.json`; the pathway/tier mapping is in
`docs/curriculum/pathway-tier-mapping.md`. The taxonomy is settled.

## Golden rules (the short version)

- All student-facing copy follows `reference/excelling-voice-specification.md`.
- British English. Harvard (Cite Them Right) referencing by default. No em dashes.
  Address the student as "you".
- Explain the *why*, not just the what.
- You draft; a human subject-matter expert approves academic accuracy. Never
  present invented facts, statistics or citations as real.

Full rules in `CLAUDE.md`.

## Setup

```
npm ci
npm run adapt-install     # NEVER raw `adapt install` - it wipes the patches/
```

Build commands are in `docs/RUNBOOK.md`.

## Layout

```
design-kb/     the gate store, page archetypes, component palette, activity patterns
schemas/       JSON Schemas for the stores and the manifest
catalogue/     the 13 pathways
reference/     the source book, voice spec, linguistic audit
tools/         pipeline + quality tooling and tests
.claude/       the gate skills and the reviewer agent
src/           custom Adapt components + extensions (contrib plugins install on demand)
grunt/         the Adapt build
courses/       one directory per course (manifest + Adapt content model)
content/       context packs and shared assets
docs/          PIPELINE, ARCHITECTURE, RUNBOOK + authoring/curriculum/testing references
```
