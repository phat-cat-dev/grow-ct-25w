# Source mapping rules (v1.2)

Drafted by the project's prompt thread **[ADAPT]** on 29 September 2026 at Abbott's request; landed by adp-0193 under STD-1.

**v1.1 (1 October 2026, adp-0206):** step 1 checks only the text's hash against the index, which is the only hash the index holds, and records the chunks file's hash in the map; section 6 follows MDV-1, so the Markdown view is made on demand and never committed.

**v1.1.1 (1 October 2026, adp-0209):** step 4 states that a pathway summary rests only on that pathway's own statements, and `validate-map.js` rejects a map that breaks it (SRB-1).

**Note added 2 October 2026 (adp-0214, RJ-0054):** title and prose reworded to name no consuming project (PCP-1); passages specific to one project marked **[ADAPT]**, the same way the existing marked parts are. Not rules v1.2; version unchanged.

**Note added 2 October 2026 (adp-0215, RJ-0057):** the context-consultation process paragraph's second sentence, naming `agent-review-map-process-adapt.md`, marked **[ADAPT]** (PCP-1); missed by RJ-0054's pass. Not rules v1.2; version unchanged.

**v1.2 (3 October 2026, adp-0221, RJ-0091):** step 1 stops unless the index marks its chunking as `ok`, not only on `failed`, now that `ingestion-rules.md` v1.4 gives `chunking` a fourth value, `not cut` (a ruled exception, not a tool failure), which this step must also treat as not yet eligible for mapping.

**Where it lives (PTH-1, RJ-0048).** This document is the pathways model's own (`tools/pathways/core/`, TLS-1); moved here, and renamed from a project-qualified filename under TLS-1's naming convention, by RJ-0048 (D-0041, D-0044, adp-0213). It reads the standards module's generic side, `tools/standards/core/`, which will be spun out into the STANDARDS-DB project and never reads or names anything here. Chunking is done there (`tools/standards/core/rules/ingestion-rules.md`); this document starts from finished chunks.

It is the first of two parts of the **context-consultation process**. Part 1, this document, tells a **mapping agent** how to map one QAA subject benchmark statement against the pathways. Part 2 **[ADAPT]**, `agent-review-map-process-adapt.md`, tells a **consulting agent** how to use the finished map.

The process is meant to become a META process that any project can call. Everything specific to the first project to use it is marked **[ADAPT]**. For another project, you replace those parts: its topic list, its tag prefix and its output location.

---

## 1. Objective

Produce one map for each benchmark statement. The map collects every place where QAA itself describes a relationship between the subject and one of the pathway topics, **grouped by pathway**. A consulting agent can then find what QAA says about, for example, psychology and referencing, without reading the whole statement.

The map records **what the benchmark says**. It does not record what the mapper thinks the subject ought to need. A pathway with no QAA statement is recorded as empty, and that empty entry is a finding.

## 2. Inputs

| Input | Where | Use |
|---|---|---|
| The benchmark's chunks | `tools/standards/core/qaa/benchmarks/<slug>.chunks.json` | The unit every statement is taken from |
| The benchmark's text | `tools/standards/core/qaa/benchmarks/<slug>.txt` | Full text, read where a chunk needs checking |
| The sources index | `tools/standards/core/qaa/benchmarks/index.json` | Title, year, origin and SHA-256; the map records the hashes it was made from |
| The pathway list **[ADAPT]** | `catalogue/pathways.json` | The 13 pathway ids; never remapped |
| The term list for each pathway **[ADAPT]** | `tools/pathways/core/rules/pathway-term-lists.json` | The word test for strength |
| Block types | BM-1's closed list of 15 | One block type per chunk |

The mapper never reads the PDF, except to settle what none of these can.

## 3. Vocabulary

- **Chunk.** One of QAA's numbered paragraphs, or a run of them, as the generic ingestion step cut it. Identified by its `chunkId`, `qaa/<slug>/<paragraphs>` (for example `qaa/psychology-2023/3.16`), which is the join key. Chunks excluded at ingestion are not mapped.
- **Statement.** A chunk (or one sentence within it) that says something about one pathway. A chunk can yield statements for several pathways.
- **Pathway tag.** `adapt-<pathway-id>`, for example `adapt-referencing` or `adapt-finding-using-sources` **[ADAPT prefix]**. The part after the prefix is always a `catalogue/pathways.json` id.
- **Strength.**
  - `direct`: the passage names the pathway's topic in the pathway's own terms (the term list's word test).
  - `indirect`: the passage describes the activity without those terms.
- **Evidence extract.** The shortest verbatim run of whole words that shows the link: 4 to 25 words, never paraphrased and never more than two sentences.
- **Orientation.** `academic`, `professional` or `both`, with its own evidence extract.
- **Block type.** One of BM-1's 15 values.
- **Agent instruction.** A short note from the mapper to the consulting agent. It says what the statement is good for and what it must not be used to claim.
- **Coverage.** For each pathway: the number of direct statements and the number of indirect statements, or `none`.

## 4. The tagging tests (QV-TAG-2, parts a to m, frozen 24 September 2026)

QV-TAG-2 was ruled in the QAAVector project, now retired (STD-1). Its text is quoted below verbatim from its source, with the path and commit it was read from.

**Source:** `config/manualTags/README.md`, QAAVector, commit `a9a2f1061c62366d939b209f3a9732a8f51c4292` (unchanged at QAAVector's repo HEAD `366bcb99a01118f2c4c3ebfa2a8337596bddc455`, confirmed by `git diff` between the two commits on this file, no output).

## QV-TAG-2 (2026-09-22)

Abbott ruled: "yes agreed no tag for sentences about education providers
(rather than the students or learners) yes agreed to all". The rule has
three parts, landed in the sections above:

- (a) Referencing: `referencing` means students or learners acknowledging
  sources and acting with academic integrity themselves, not providers
  keeping assessment secure or maintaining academic integrity (for example
  against AI); such a passage may still carry `ai-technology` if it meets
  part (b).
- (b) Students, not providers: a tag needs a passage about what students or
  learners do, learn or are assessed on. A passage about what education
  providers, course teams, degree-awarding bodies or external examiners
  design, review, monitor or must do gets no tag.
- (c) Evidence: an evidence quote is whole words, never starting or ending
  inside a word; at least four words and at most 25; one quote may support
  more than one pathway only where the quoted sentence names each of them.
- (d) Provider processes: a passage whose subject is how a provider runs,
  reviews, monitors or quality-assures a course gets no tag, even where
  students take part in that process.
- (e) Strength: a tag is `direct` when its evidence quote contains one of
  that pathway's strength terms (`STRENGTH_TERMS` in
  `config/pathwayTerms.js`), and `indirect` when it does not. Strength
  follows from the quote; choosing or rewriting a quote to change the
  strength is not allowed.
- (f) A term in a different sense does not name the practice. A chunk
  carries at most one tag per pathway. Continuing professional development
  counts as `reflective-practice` only where the passage also names
  reflection.
- (g) The passage must be about what students or learners do, learn, or
  are assessed on. It counts however it is phrased, including where the
  sentence's subject is the course, the curriculum, a degree, an
  assessment method, or a list of skills or outcomes, and including where
  students appear as a possessive or as the object of assessment. What
  fails is a passage about something else: a provider's own process under
  part (d), what staff or course teams do, a heading, title or bare list
  label with no statement attached, or a topic the discipline studies
  under the discipline-subject carve-out.
- (h) Directive phrasing does not by itself make a passage a provider
  process. A passage counts where its content is something students do,
  learn or are assessed on, even where the sentence tells a provider to
  arrange, design, offer or deliver it. Part (d) removes a passage whose
  content is the provider's own machinery: access and equity
  arrangements, resourcing, and who is responsible for choosing what.
- (i) A list item counts where its own words name something students do,
  make or learn, whatever sentence introduces the list. It makes no
  difference whether the list is introduced as assessment, learning
  activities, teaching methods or scheduled activities. A list item fails
  where it is a bare content-area label with no statement attached, or
  where the list names what staff do.
- (j) The discipline-subject carve-out covers a passage about the world:
  what the field is, what the sector does, what a term means. It does not
  cover a passage about what the course covers, even where the course
  content is named rather than the student. A passage that says what is
  taught counts.
- (k) A passage about what staff, course teams or the institution do
  fails under part (b). This does not remove a passage about feedback,
  marking criteria or assessment information given to students, because
  those are themselves pathways and QAA writes about them addressed to
  the people who provide them.
- (l) A passage stating an administrative fact about the qualification
  fails: accreditation and eligibility, credit calculation, qualification
  structure, resourcing, facilities, and what providers make available.
- (m) A passage about career outcomes, the employment market,
  institutional reputation, or what industry or employers gain fails.

## 5. Steps

1. **Check the source.** Find the benchmark in the index. Stop unless the index marks its chunking as `ok`. Compute the SHA-256 of its text file by the index's own method (trailing newlines stripped, `ingestion-rules.md` section 2) and compare it with the index's `sha256`; stop on a mismatch. Compute the SHA-256 of its chunks file over the file's bytes as they stand, nothing stripped. Record the source id, the year, the text's hash in `source.text.sha256` and the chunks file's hash in `source.chunksFile.sha256`. The index holds no chunks-file hash, so that hash is recorded, not compared.
2. **Scan the whole document once for each pathway.** For each of the 13 pathways in turn, read every non-excluded chunk against that pathway's term list and the tagging tests. The pass is per pathway, not per chunk, so no pathway is judged only in passing while another is being looked for.
3. **Write each statement.** For each hit, record: the `chunkId`, the locator (section, paragraphs and pages), the tag, the strength, the evidence extract, the block type, the orientation with its extract, and the agent instruction.
4. **Summarise each pathway group.** In one to three sentences, say what QAA says about the pathway in this subject. Mark the summary as the mapper's reading, and cite the chunk ids it rests on. Every chunk id in the summary's basis, and every paragraph number its text cites, is a chunk that holds a statement in this pathway; `validate-map.js` rejects a map that breaks this (SRB-1). If there is no statement, write `none` with no summary.
5. **Write the document-level agent instructions.** Cover anything that applies to the whole map: for example, "this benchmark's statements on writing are about research reports, not essays", or "orientation is mostly academic".
6. **Count coverage** for every pathway, including those with none.
7. **Self-check.**
   - Every tag is a catalogue id with the prefix.
   - Every block type is one of the 15.
   - Every extract appears verbatim in the chunk text, checked by script.
   - Every extract is 4 to 25 words.
   - Every pathway appears once in the coverage list.
   - No statement is about the provider rather than students.
8. **Status.** Every statement starts as `proposed`. Abbott confirms statements in batches. Only `confirmed` statements may be cited as grounding.

## 6. Output template

One file per benchmark. The JSON is the record, and the consulting agent reads the JSON. A Markdown view may be generated from it on demand for a person's review; it is never edited by hand, never committed and never added to the mirror (MDV-1).

```json
{
  "mapVersion": "1.0",
  "rules": "source-mapping-rules.md v1.1.1",
  "project": "adapt",
  "tagPrefix": "adapt-",
  "source": {
    "id": "qaa/psychology-2023",
    "title": "Subject Benchmark Statement: Psychology",
    "issuer": "QAA",
    "year": 2023,
    "text": { "file": "tools/standards/core/qaa/benchmarks/psychology-2023.txt", "sha256": "" },
    "chunksFile": { "file": "tools/standards/core/qaa/benchmarks/psychology-2023.chunks.json", "sha256": "" },
    "chunks": 0,
    "excludedChunks": 0
  },
  "mappedBy": { "agent": "", "date": "", "sessionRef": "" },
  "agentInstructions": [
    "Whole-map notes for the consulting agent."
  ],
  "coverage": {
    "adapt-referencing": { "direct": 0, "indirect": 0 },
    "adapt-presenting": "none"
  },
  "pathways": {
    "adapt-referencing": {
      "summary": {
        "text": "The mapper's reading of what QAA says about this pathway in this subject.",
        "basis": ["qaa/psychology-2023/3.28-3.32"],
        "status": "proposed"
      },
      "statements": [
        {
          "chunkId": "qaa/psychology-2023/3.28-3.32",
          "locator": { "section": "3", "paragraphs": "3.28-3.32", "pages": "" },
          "tag": "adapt-referencing",
          "strength": "direct",
          "extract": "verbatim, 4 to 25 words",
          "blockType": "assessment_and_feedback",
          "orientation": "academic",
          "orientationExtract": "verbatim, 4 to 25 words",
          "agentInstruction": "What this is good for, and what it must not be used to claim.",
          "status": "proposed"
        }
      ]
    }
  },
  "excluded": [
    { "chunkId": "qaa/psychology-2023/toc", "reason": "table of contents" }
  ]
}
```

All 13 pathways appear under `coverage`. Under `pathways`, only those with at least one statement appear.

## 7. What the map never holds

- Whole paragraphs of QAA text. Full text stays in the source file and is read there.
- Paraphrase presented as QAA's words.
- Tags for pathways outside the catalogue, or a tag remapped to fit.
- Any judgement about the course being built. That belongs to the consulting agent.

## 8. Relation to what exists

- The project's earlier map **[ADAPT]**, `source-kb/source-maps/qaa-psychology-2023.json`, was set aside on 22 September 2026 and is superseded by STD-1. It stays in place until the first map made under these rules replaces it.

## 9. Settled points (Abbott, 29 September 2026)

- The extracted texts are committed as backup: source material only, never published, and they may be adapted for use in the project. Each entry in `index.json` quotes the statement's own copyright notice.
- Extracts are 4 to 25 words, never more than two sentences. Full text is read from the source file.
- JSON is the record, and a Markdown view is generated from it. **Note added 1 October 2026 (adp-0206):** amended by MDV-1; the view is made on demand and never committed (section 6).
