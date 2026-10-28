# tools/subject/

ADAPT's subject-classification tooling on HESA's own data (HMD-1, 30 September 2026), under the `tools/<module>/` layout (TLS-1).

## Two parts

| Part | Folder | What it holds |
|---|---|---|
| Generic HESA tooling | `core/` | HESA's CSVs as pinned source data (`data/`), the vocabulary stores built from them (`vocab/`, formerly `vocab-kb/`), and the build tool (`tools/`) |
| ADAPT's side | `adapt/` | Empty for now; will hold the context gate's rules when they are written |

`adapt/` may read `core/`. `core/` never reads or names `adapt/`, ADAPT or any other consuming project.

## What is built

- `core/vocab/cah.json` and `core/vocab/hecos.json`: the CAH and HECoS vocabulary stores.
- `core/tools/build-hesa-vocab.py`: the deterministic builder that produces them from HESA's CSVs, refusing to run if any CSV's SHA-256 does not match the hash it holds.
- `core/tools/resolve-subject-context.js`: a HECoS code, a CAH code (CAH1, CAH2 or CAH3) or a subject name in, its level/code/label out plus the CAH chain above it; `"universal"` returns an unscoped context rather than either store being read (adp-0223, RJ-0099).

## What is not built

- HMP-1's HESA maps (tagging each benchmark statement from HECoS up through CAH3, CAH2 and CAH1): ruled, not built.
- The context gate's rules for `adapt/`.

## The CSVs

`core/data/` holds HESA's own CSVs, pinned as source data, each recorded in `core/data/SOURCES.md` with its name, size, SHA-256 and (where known) HESA's version and date. As of 30 September 2026 (adp-0204) none of the five is committed: none was found anywhere in the workspace, and `SOURCES.md` records the search. Abbott must supply them.
