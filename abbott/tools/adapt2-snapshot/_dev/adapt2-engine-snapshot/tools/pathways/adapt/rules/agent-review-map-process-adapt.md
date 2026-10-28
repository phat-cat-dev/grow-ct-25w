# Agent review of a map: ADAPT (v1.1)

Drafted by ADAPT's prompt thread on 29 September 2026; landed by adp-0193 under STD-1. It belongs to `tools/pathways/adapt/rules/`, moved there by RJ-0048 (D-0041, D-0044, adp-0213).

**Change note, 2 October 2026 (adp-0214, RJ-0049).** Step 7 replaced to follow SFS-1 (1 October 2026, `open-decisions.md`): the consulting agent reads the consultation bundle only, never the extract and never the benchmark source file. Section 5 below is new: the call contract `tools/pathways/core/tools/consult-maps.js` and `tools/subject/core/tools/subject-lookup.js` give Phase D's D0 and D1 to call when they are built (Phase D is not built, D-0007; nothing here is wired into any gate by this revision). Known inconsistency not fixed here: step 3 below still names the group key as `adapt-<pathway>`, read directly from a map; the bundle's own group key is `path-<pathway-id>` (RULINGS 3, adp-0214, RJ-0049), and no committed map uses that prefix yet (D-0045's rename is ruled, not landed, pending RJ-0033). Step 3's wording was in scope for v1.0's "read the map directly" model, superseded in substance by section 5's bundle-only contract; left as written rather than rewritten, since RULINGS 3 scoped this revision to step 7 and the new call-contract section only. Whoever builds Phase D's D0/D1 should read section 5, not step 3, for the group key.

It is the second of the two parts of the **context-consultation process**. It tells a **consulting agent** (at present, the Phase D sources step writing a context pack) how to use a map made under `source-mapping-rules.md`. It is kept short on purpose: the mapper has already done the reading, and this agent reads the map, not the benchmark.

Parts specific to ADAPT are marked **[ADAPT]**.

---

## 1. Inputs

- **The context being written.** Subject (HESA code), pathway, tier and orientation qualifier, taken from the context definition at D0 **[ADAPT]**.
- **The map for each benchmark that matches the subject.** Found through the `source-kb` record, with a HESA walk-up from most specific to least.

## 2. Steps

1. **Find the map.** If the subject has no benchmark or the benchmark has no map, record a grounding gap that names the subject and the missing map, and stop this process.
2. **Read the whole-map `agentInstructions` first.** They bind everything that follows.
3. **Open the group for the course's pathway** (`adapt-<pathway>`). If `coverage` says `none`, record a grounding gap: "QAA's <subject> benchmark makes no statement about <pathway>". Stop there. Do not borrow a neighbouring pathway's statements to fill the gap.
4. **Take the confirmed statements only.** A `proposed` statement may be read but never cited.
5. **Order the statements:**
   - `direct` before `indirect`;
   - then statements whose orientation matches the context's qualifier;
   - `both` counts as matching either.
6. **Obey each statement's `agentInstruction`.** Where it limits use ("not a requirement on students", "about research reports only"), the limit holds in anything written from it.
7. **Read the bundle only (SFS-1).** Never read the extract and never read the benchmark source file in `tools/standards/core/qaa/benchmarks/`, however incomplete the bundle's own wording seems. Everything the agent may use is already in the consultation bundle `consult-maps.js` returns, per confirmed pair: `studentFacingStatement`, the group's why-it-matters line, `scopeElement`, `strength`, `chunkId` and `agentInstruction`. If a pair's bundle entry lists a field under `fieldsMissing` (every confirmed pair on every map committed today does, since none of the three carries these fields yet), that field is genuinely absent for this statement; do not invent a value for it and do not go to the extract or the source file to fill it in.
8. **Cite by `chunkId`** in the grounding line of the gate record (SSC-1). A sentence in the pack that rests on QAA must trace to a cited statement.
9. **Say what was used.** For each map consulted, list:
   - the statements used;
   - the statements read but not used, each with a one-line reason;
   - any grounding gap.

## 3. Rules

- The map is evidence of what QAA says, not of what the course should do. The agent decides the use and states it as its own proposal.
- Never present an indirect statement as QAA naming the pathway.
- Never cite the group summary. It is the mapper's reading. Cite the statements it rests on.
- An empty group is a result to report, not a failure to hide.

## 4. Output

This is written into the gate's draft record under GDP-1:

```json
{
  "consultation": [
    {
      "map": "qaa/psychology-2023",
      "group": "adapt-referencing",
      "used": [{ "chunkId": "", "strength": "", "howUsed": "" }],
      "readNotUsed": [{ "chunkId": "", "why": "" }],
      "groundingGaps": []
    }
  ]
}
```

## 5. Call contract, for Phase D's D0 and D1

Not wired into any gate: Phase D is not built (D-0007). This section states the contract Phase D's D0 and D1 must call when they are built; nothing here runs automatically today.

**Subject lookup**, `tools/subject/core/tools/subject-lookup.js`, function `lookupSubject(code, options)`:
- **In:** a HECoS or CAH code (the context's subject, D0 **[ADAPT]**).
- **Out:** `{ input, benchmarks: [ { benchmark, matchLevel, label, source } ], gap }`, most specific CAH level first (`hecos` ranks above `cah3`, `cah3` above `cah2`, `cah2` above `cah1`). `source` is `"tagged"` once M2 runs, `"stated"` until then (only psychology has a stated lookup file today). `gap` is non-null, naming the reason, when the code is covered by no benchmark.

**Consultation**, `tools/pathways/core/tools/consult-maps.js`, function `consult(benchmarkIds, pathwayId, tier, options)`:
- **In:** the benchmark ids `lookupSubject` returned, the course's pathway id, and its tier.
- **Out:** one bundle, `{ pathwayId, tier, tierFilterApplied: false, tierNote, benchmarks: [ { benchmarkId, gap, confirmedPairs } ] }`. `tierFilterApplied` is always `false` today: no ruled capability cards are committed, so `tier` is carried into the bundle but never used to filter; `tierNote` says so. Each `confirmedPairs` entry carries `chunkId`, `strength`, `agentInstruction`, `studentFacingStatement`, `whyItMatters`, `scopeElement`, and `fieldsMissing` naming any of the last three absent from that statement. No `extract`, no `orientationExtract`, and no other benchmark text ever appears in the bundle (SFS-1).
- **Gaps:** one of `no-benchmark`, `no-map`, `map-not-active`, `no-group`, `empty-group`, `no-confirmed-pairs`, each with a `detail` string naming what was found. A per-benchmark gap leaves that benchmark's `confirmedPairs` empty; it does not stop the other benchmarks in the same bundle from being consulted.

## 6. Whether this step is needed

If the mapper writes good agent instructions, this document is mostly steps 3, 4 and 8, and could shrink to a paragraph in the Phase D command doc. It is kept separate for now so that META can adopt the consulting half without the mapping half.
