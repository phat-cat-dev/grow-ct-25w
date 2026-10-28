# Component map — components against the data structures

_Generated 2026-10-10T01:06:58.938Z. Cross-references palette x patterns x shapes x src plugins x usage in `understanding-learning-assessment-feedback-introductory`._

## Palette entries

| palette id | kind | origin | build | src plugin | used (course) | realised by patterns | fits shapes |
|---|---|---|---|---|---|---|---|
| `palette/text` | component | core | available | (contrib) | 44 | evaluate-versions | teaching-prose, learning-outcomes, orientation, summary, visual-overview |
| `palette/accordion` | component | core | available | (contrib) | 1 | sequential-process, explore-model, evaluate-versions, survey-alternatives, recall-reveal, look-up-definitions | sequential-process, definitions |
| `palette/mcq` | component | core | available | (contrib) | 21 | retrieval-practice, spot-the-error, summative-mixed | retrieval-practice, summative-item |
| `palette/sortable` | component | abbott | available | adapt-abbott-sortable | 2 | retrieval-practice, build-from-parts, summative-mixed | ordering-task, summative-item |
| `palette/textinput` | component | core | deprecated | (contrib) | 5 | · | reflective-prompt |
| `palette/confidence` | component | abbott | available | adapt-abbott-confidence | 2 | · | self-efficacy-rating |
| `palette/assessmentresults` | component | core | available | (contrib) | 1 | · | summative-results |
| `palette/references` | component | abbott | available | adapt-abbott-references | 6 | · | further-reading |
| `palette/hotgraphic` | component | core | available | (contrib) | 1 | explore-model | visual-overview, hotspot-exploration |
| `palette/narrative` | component | core | available | (contrib) | · | sequential-process, explore-model, evaluate-versions | visual-overview, sequential-visual |
| `palette/timeline` | component | abbott | available | adapt-abbott-timeline | · | explore-model | visual-overview |
| `palette/resultsdebrief` | extension | abbott | available | adapt-abbott-resultsdebrief | · | · | summative-furniture |
| `palette/passreveal` | extension | abbott | available | adapt-abbott-pass-reveal | · | · | summative-furniture |
| `palette/annotated` | component | abbott | available | adapt-abbott-annotated | · | evaluate-versions, inline-commentary | exemplar-analysis, prose-with-inline-commentary |
| `palette/branching` | component | abbott | available | adapt-abbott-branching | · | decision-scenario | decision-scenario |
| `palette/checklist` | component | abbott | available | adapt-abbott-checklist | 5 | action-checklist | working-checklist, pre-submission-review |
| `palette/flipcard` | component | abbott | available | adapt-abbott-flipcard | 2 | explore-model, recall-reveal | paired-reveal, visual-overview |
| `palette/glossary` | component | abbott | available | adapt-abbott-glossary | · | look-up-definitions | inline-definitions |
| `palette/opentext` | component | abbott | available | adapt-abbott-opentext | 5 | write-own-thinking | reflective-prompt, notes |
| `palette/tabs` | component | abbott | available | adapt-abbott-tabs | · | survey-alternatives | parallel-content |
| `palette/matching` | component | core | available | (contrib) | 2 | match-pairs, sort-into-groups | pairing-task, summative-item |
| `palette/gmcq` | component | core | available | (contrib) | · | spot-the-error | visual-discrimination, summative-item |
| `palette/graphic` | component | core | available | (contrib) | · | explore-model | static-image, decorative-pairing |
| `palette/media` | component | core | available | (contrib) | · | sequential-process, explore-model | video-audio |
| `palette/slider` | component | core | available | (contrib) | · | place-on-a-scale | numeric-scale, summative-item |
| `palette/hotspot` | component | abbott | pending | — | · | spot-the-error, label-a-structure | label-a-structure, spot-the-error |

## Activity patterns

| pattern | intent | slotTypes | servesShapes | realisations |
|---|---|---|---|---|
| `retrieval-practice` | formative | check | fact, concept, principle | mcq, sortable |
| `sequential-process` | formative | worked-example | procedure | accordion, narrative, media |
| `explore-model` | formative | concept-intro, worked-example | structure, process, principle | hotgraphic, narrative, timeline, flipcard, accordion, graphic, media |
| `evaluate-versions` | formative | worked-example | contrast | annotated, accordion, narrative, text |
| `survey-alternatives` | formative | concept-intro, practical-guidance | parallel-options | tabs, accordion |
| `recall-reveal` | formative | concept-intro, worked-example | fact, concept | flipcard, accordion |
| `look-up-definitions` | formative |  | concept | glossary, accordion |
| `write-own-thinking` | formative | reflective-prompt | reflection | opentext |
| `decision-scenario` | formative | worked-example, practical-guidance | judgement | branching |
| `action-checklist` | formative | practical-guidance | criteria | checklist |
| `inline-commentary` | formative | concept-intro, practical-guidance | principle | annotated |
| `match-pairs` | formative | check | pairs | matching |
| `spot-the-error` | formative | check | error | mcq, gmcq, hotspot |
| `sort-into-groups` | formative | check, practical-guidance, concept-intro | classification | matching |
| `build-from-parts` | formative | check, practical-guidance, concept-intro | assembly, structure | sortable |
| `summative-mixed` | summative | summative-item |  | mcq, sortable |
| `place-on-a-scale` | formative | check, practical-guidance, concept-intro | judgement, criteria | slider |
| `label-a-structure` | formative | check, practical-guidance, concept-intro | structure | hotspot |

## Findings / gaps

1. **Palette components not used in this course (11):** narrative, timeline, annotated, branching, glossary, tabs, gmcq, graphic, media, slider, hotspot. Available to author with, not yet exercised.

2. **Built src plugins NOT represented in the palette (1):** adapt-abbott-reflective-store (reflectivestore). These can't be chosen by `/gate`'s palette selection until added.

3. **Palette entries with no resolvable source here (0):** none. (core = contrib, fetched at install; others should map to a src plugin. Entries flagged build=pending/deprecated are excluded — see below.)

4. **Designed but not built (build=pending, 1):** hotspot. Design retained; component awaiting (re)build; do not author with these yet.

5. **Deprecated (build=deprecated, 1):** textinput. Superseded; retained for provenance, not for new authoring.

6. **Pattern realisations pointing at a missing palette id (0):** none.

7. **Overlaps resolved (9 Oct 2026):** `textinput` vs `opentext` was a genuine duplicate (both serve reflective-prompt) — `textinput` is now build=deprecated and `opentext` is canonical (write-own-thinking realises opentext only). `mcq` vs `gmcq` is NOT a duplicate — `gmcq` is the graphic/image MCQ (visual-discrimination), a distinct core component kept alongside `mcq`.

8. **Two shape vocabularies:** patterns' `servesShapes` use `content-shapes/*` (15 knowledge-type shapes: fact, concept, structure, classification, procedure, process, principle, contrast, parallel-options, pairs, error, assembly, judgement, criteria, reflection), while palette `contentFit` uses a different set of shape names (teaching-prose, retrieval-practice, …). These are not reconciled; a component is matched to a slot through *patterns* (servesShapes), so the palette contentFit vocabulary is advisory. Worth unifying or cross-walking.
