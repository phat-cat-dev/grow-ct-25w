---
document:  ing: the pathways terminology database
owner:     adp ing
version:   0.1.2, 4 October 2026, 10:53, verb_in_context (ing N-0120); 0.1.1, 4 October 2026, 10:37, rebuilt after D-ing-0057 (ing N-0119); 0.1.0, 4 October 2026, 10:33 (ing N-0118)
status:    a working compilation, rebuilt from the cores by `build-ing-db.py`; never a record; the cores are the source
---

# The pathways terminology database

`ing-pathways.sqlite` compiles the 13 pathway cores and the card vocabulary into one SQLite database. Rebuild it after any core changes: `python3 build-ing-db.py`. The script fails if it reaches no pathways or no terms.

## What is in it (built 4 October 2026, 10:33)

| Table | Rows | From |
|---|---|---|
| pathway | 13 | each core's front matter |
| concept | 366 | A3 tiers (39) and capabilities (87), A4 and B1 concepts (240) |
| term | 387 | B2a terms named by the authors (274) and B2b associated vocabulary (113); 359 distinct forms |
| term_block | 113 | B2b: the tier each associated term belongs to, its sources and agreement weight |
| framework_block | 19 | B3: concepts a pathway defines its own way |
| relation | 85 | B4: higher-level-than, broader, narrower, part-of, related, contrasts-with |
| theory_relation | 132 | A9: derivedFrom, related, extends, contrastsWith, with targets |
| search_term | 337 | A10: direct terms (the term list as words) and associated terms |
| card | 88 | A10 competencies, and the card vocabulary for all 13 pathways |
| card_word | 635 | each card's verbs, measures and keywords |
| card_theory, card_process, card_framework | 110, 96, 124 | A10 per card |
| verb_in_context | 167 | D-ing-0058: each verb with its statement, statement type, source, subject, read-as and relation: 144 from the cards' own statements, 23 from the pilot's benchmark extracts |

Views: `concept_hierarchy` (A3 parents with B4's narrower and part-of, 104 edges) and `term_across_pathways` (27 terms in more than one pathway, led by discourse community in five).

## The hierarchy

Each pathway is a ladder: three tiers (`higher-level-than`), capabilities under each tier (A3 `parent`), concepts under capabilities and tiers (B4 `narrower`, `part-of`), and terms under concepts (B2a named forms, preferred and admitted; B2b associated vocabulary placed in a tier). Across pathways the joins are shared terms and A9's relations.

## Gaps the compilation found

[Rebuilt 4 October 2026, 10:37: gaps 1 and 2 closed by D-ing-0057: 53 definitions added to A4 in eleven cores; every B2a term and every B4 relation now reaches a declared concept. B2b's associated vocabulary stays as candidates and is mostly undefined by design (108 concepts).]

1. **47 concepts named in B2a have no definition** in A3, A4 or B1, mostly the guide's glossary terms added by the vocabulary sweep (D-ing-0050), for example essay, plan, editing and proofreading in Academic Writing. By count: Academic Writing 11, Criticality 7, Finding and Using Sources 6, Work-Based Learning 6, Referencing 5, Understanding Learning, Assessment and Feedback 5, and one or two in four others; none in the three pathways drafted today.
2. **15 B4 relations** point at a concept the core does not declare (for example editing and proofreading, keyword and synonym, references list and bibliography).
3. Terms are keyed to a concept slug within a pathway; the same idea in two pathways has two slugs (discourse community in five). A shared concept list across pathways is TERMINOLOGY-DAT's job (META), not this database's.

## Example queries

```sql
-- every term under one pathway's tiers, with its tier
SELECT t.form, t.list, b.component FROM term t LEFT JOIN term_block b ON b.pathway = t.pathway AND b.concept = t.concept WHERE t.pathway = 'presenting';
-- the verbs used across all cards, by count
SELECT word, count(*) FROM card_word WHERE kind = 'verb' GROUP BY word ORDER BY 2 DESC;
-- terms shared between pathways
SELECT * FROM term_across_pathways ORDER BY pathways DESC;
```

---

## Change notes
- 0.1.2: 4 October 2026, 10:53: table verb_in_context (D-ing-0058; ing N-0120).
- 0.1.1: 4 October 2026, 10:37: rebuilt after D-ing-0057; gaps 1 and 2 closed (ing N-0119).
- 0.1.0: 4 October 2026, 10:33: created (Abbott, 10:33; ing N-0118).
