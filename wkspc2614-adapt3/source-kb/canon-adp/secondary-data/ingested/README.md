# ingested: the documents made from these sources

Each ingest profile owns one folder, named for the profile exactly as the
catalogue and the manifests name it. A document's file name carries its profile,
so the folders are a convenience and the names are the truth.

| Folder | Holds | Shape |
|---|---|---|
| `theory/` | theory runs, `ingest-theory-<slug>.md` | one file |
| `academic-source/` | source précis, `src-<author>-<year>-<title>-<type>.md` | one file |
| `standards/` | standards runs, `ingest-std-<slug>/` | a folder with `run-src/` |
| `reference/` | reference-layer maps, `ingest-reference-<slug>/` | a folder with `run-src/` |
| `pathway/` | pathway runs, `ingest-path-<slug>.md` | one file (written in ADAPT today) |
| `_definitions/` | the ingest golden files: the document structure and template, the run prompts and run frame, the profiles, the project spec, charter and instructions, the queue and the gates | |
| `_indexes/` | what reads across profiles: the code map, the placement and skeleton maps, the terminology register, the process register | |

The two folders beginning with an underscore are not profiles. They sort first,
which is the point: a reader meets the definitions before the documents.

## Where these came from

`theory/`, `academic-source/`, `reference/`, `_definitions/` and `_indexes/`
moved here from UNI `mta/claude/mta-relay/designs/ingest/` on 4 October 2026
(Abbott, 01:03; META nts N-1215), 155 files, each hashed before and after.
`standards/` moved from UNI on 3 October (Abbott, 20:56; std N-0119).

The library is the single home for documents (Abbott, 4 October 2026, 00:03).
UNI keeps a read-only published copy, written by the library's `publish`.
