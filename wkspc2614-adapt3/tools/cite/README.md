# tools/cite/

CITE, ADAPT's referencing tooling, under the `tools/<module>/` layout (TLS-1).

## Two parts

| Part | Folder | What it holds |
|---|---|---|
| Generic CITE tooling | `core/` | Empty for now; will hold CITE's generic tooling and data once CITE-6 lands |
| ADAPT's side | `adapt/records/` | Empty for now; will hold ADAPT's own CITE records |

`adapt/` may read `core/`. `core/` never reads or names `adapt/`, ADAPT or any other consuming project.

## What is ruled so far

- **CITE-1**: CITE pins three CSL styles: Cite Them Right Harvard (the default), APA 7th edition (psychology) and OSCOLA (law).
- **CITE-2**: Reference data lives in `source-kb/source-kb.json`, one entry per format of a source, each with its own `csl` field (CSL-JSON) and `cslVerified`.
- **CITE-3**: CITE vendors two CSL locales: `en-GB` (default) and `cy-GB`.
- **CITE-4**: Entries that are formats of one work share a `workId`.
- **CITE-5**: CITE's definition document belongs in META as global tooling, vendored by name (title, date, drafting thread) rather than landed in this repo.
- **CITE-6** (the folder layout under `tools/cite/`, naming the two parts above) is ruled by TLS-1's own text but has not itself landed as a numbered ruling.

## What is not built

Nothing. This module holds only the folder scaffolding above; no tool, schema or data file has been written for CITE yet.
