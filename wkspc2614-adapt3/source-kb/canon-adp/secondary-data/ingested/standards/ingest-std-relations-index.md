---
document:  The standards relations index: how the frameworks, benchmarks, assessment criteria and guidance documents relate
version:   0.3.1-draft, 3 October 2026
owner:     std
status:    draft; first written with runs 0056 and 0057 (Abbott, 05:40: "map these web of relationships between the standard frameworks, the guidance documents, and the subject benchmarks"). Every edge marked `inferred` is our reading; `primary` edges are stated in a held text
---

# Standards relations index

## What it is

One place for the links between standards documents, so that a statement in one can be followed to the statements it relates to in another. It holds **edges between documents** (below) and points to the **statement-level maps** kept in each document (a guidance document's S4 `maps`, an assessment-criteria document's `echoes`, a framework document's shared descriptors). It is regenerated or extended whenever a standards document is added.

## The documents

| Id | Variant | Kind of standard | Levels | Status |
|---|---|---|---|---|
| std:doc:qaa-fheq-2024-framework | framework | qualification framework, England, Wales and Northern Ireland, with the common material | FHEQ 4 to 8 | 0.3.0 |
| std:doc:qaa-fqheis-2024-framework | framework | qualification framework, Scotland | SCQF 7 to 12 | 0.1.0 |
| std:doc:welsh-government-cqfw-2009-framework | framework | credit and qualifications framework, Wales | CQFW entry to 8 | 0.1.0 |
| std:doc:qaa-psychology-2023-benchmarks | subject-benchmark | subject standard | threshold at FHEQ 6 | 0.1.0 |
| 53 more benchmark texts (held in `stan/core/qaa/benchmarks/`) | subject-benchmark | subject standards | threshold at FHEQ 6 | held, not ingested (S-02) |
| std:doc:bristol-generic-2024-assesscriteria | assessment-criteria | marking criteria | FHEQ 4 to 7 | 0.1.0 |
| std:doc:cardiffmet-generic-2020-assesscriteria | assessment-criteria | band descriptors | 3 to 7 | 0.1.0 |
| std:doc:qaa-enterprise-2018-guidance | guidance (proposed) | cross-cutting theme: enterprise | none | 0.1.0 |
| std:doc:qaa-advancehe-esd-2021-guidance | guidance (proposed) | cross-cutting theme: sustainability | none | 0.1.0 (full text, run 0063) |
| std:doc:qaa-advancehe-esd-2021-execsummary | execsummary (proposed) | its executive summary | none | 0.2.0 (run 0057) |

## How they stack

```
frameworks           FHEQ / FQHEIS / CQFW      what a level means (threshold, typical holder)
   |  set at L6 threshold
subject benchmarks   54 subjects               what the subject's graduate shows (threshold, typical, excellent)
   |  measured by                \
assessment criteria  Bristol, Cardiff Met    guidance     enterprise, ESD (cross-cutting)
   how far work meets a level's standard,       level-free capabilities, reaching subjects
   band by band on the UK marking scale         through the benchmarks' theme sections
```

Frameworks say what each level is; benchmarks say what one subject's graduate shows at the honours threshold and above; assessment criteria measure work against a level band by band; guidance states capabilities without level and reaches subjects through the benchmarks. Academic practice pathways (ACPRAC-DAT's thirteen) cut across all four as categories.

## Edges

```yaml
# framework to framework
- { from: std:doc:qaa-fqheis-2024-framework, to: std:doc:qaa-fheq-2024-framework, type: sharesDescriptors, note: "master's and doctoral descriptors (4.17, 4.18) are common; held once in the FHEQ document (D-std-0010)", basis: primary }
- { from: std:doc:welsh-government-cqfw-2009-framework, to: std:doc:qaa-fheq-2024-framework, type: levelEquivalent, note: "CQFW 4 to 8 with FHEQ 4 to 8", basis: inferred }
# benchmark to framework
- { from: std:doc:qaa-psychology-2023-benchmarks, to: std:doc:qaa-fheq-2024-framework, type: thresholdAt, note: "honours threshold, FHEQ 6 (descriptor 4.15)", basis: primary }
# assessment criteria to framework
- { from: std:doc:bristol-generic-2024-assesscriteria, to: std:doc:qaa-fheq-2024-framework, type: marriesThreshold, note: "levels 4 to 7 stated; the level 6 grid follows Annex D's class wording band for band; 63 cells echo a framework statement (7+ words)", basis: primary }
- { from: std:doc:cardiffmet-generic-2020-assesscriteria, to: std:doc:qaa-fheq-2024-framework, type: marriesThreshold, note: "levels 4 to 7 stated; 37 cells echo; levels 3 and 4 reuse descriptor 4.10 closely", basis: primary }
- { from: std:doc:cardiffmet-generic-2020-assesscriteria, to: std:doc:welsh-government-cqfw-2009-framework, type: levelEquivalent, note: "level 3 read as CQFW 3; short CQFW level 6 phrases echoed", basis: inferred }
# guidance to guidance
- { from: std:doc:qaa-enterprise-2018-guidance, to: "QAA and HEA ESD guidance 2014", type: cites, note: "green and social entrepreneurship rely on entrepreneurial competencies", basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: "QAA and HEA ESD guidance 2014", type: supersedes, basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-execsummary, to: std:doc:qaa-advancehe-esd-2021-guidance, type: summaryOf, basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: std:doc:qaa-enterprise-2018-guidance, type: cites, note: "employers and enterprise section; resources", basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: "the subject benchmark statements", type: readWith, note: "the guidance says to use it beside them", basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: std:doc:qaa-enterprise-2018-guidance, type: overlaps, note: "seven of eight key competencies have an enterprise outcome counterpart; only normative is ESD's own (full ESD document GU2)", basis: inferred }
# guidance to framework and criteria (statement maps held in each guidance document's S4)
- { from: std:doc:qaa-enterprise-2018-guidance, to: std:doc:qaa-fheq-2024-framework, type: mapsTo, note: "20 records; mostly FHEQ 6 and 7 wider abilities", basis: inferred }
- { from: std:doc:qaa-enterprise-2018-guidance, to: std:doc:bristol-generic-2024-assesscriteria, type: mapsTo, note: "skills criteria: problem-solving, insight, decision-making, self-management, communication, teamwork", basis: inferred }
- { from: std:doc:qaa-enterprise-2018-guidance, to: std:doc:cardiffmet-generic-2020-assesscriteria, type: mapsTo, note: "argument, analysis, research, presentation", basis: inferred }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: std:doc:qaa-fheq-2024-framework, type: mapsTo, note: "39 records, Levels 4 to 7, as Table 2's verbs span them", basis: inferred }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: std:doc:bristol-generic-2024-assesscriteria, type: mapsTo, basis: inferred }
# benchmarks to guidance (scan of the 54 held benchmark texts)
- { from: "36 benchmarks", to: std:doc:qaa-enterprise-2018-guidance, type: cites, basis: primary }
- { from: "49 benchmarks", to: std:doc:qaa-advancehe-esd-2021-guidance, type: cites, note: "either edition", basis: primary }
- { from: "52 benchmarks", to: theme:enterprise, type: themeParagraph, basis: primary }
- { from: "54 benchmarks", to: theme:esd, type: themeParagraph, basis: primary }
- { from: "12 benchmarks", to: theme:enterprise, type: themeInStandards, basis: primary }
- { from: "37 benchmarks", to: theme:esd, type: themeInStandards, basis: primary }
- { from: "23 benchmarks", to: employability, type: themeInStandards, basis: primary }
# out of the profile, for information
- { from: "ing run 0053, Advance HE PSF 2023 (theory)", to: std:doc:qaa-enterprise-2018-guidance, type: relatedTo, note: "staff standards beside the guidance's educator family", basis: inferred }
```

Edge types: `sharesDescriptors`, `levelEquivalent`, `thresholdAt`, `marriesThreshold`, `cites`, `supersedes`, `summaryOf`, `readWith`, `overlaps`, `mapsTo`, `themeParagraph`, `themeInStandards`, `relatedTo`. Proposed for the profile with P5b.

## The reference layer (META D-0211; built 3 October 2026)

| Id | Distils | Defines |
|---|---|---|
| std:ref:uk-framework | FHEQ, FQHEIS, CQFW (and the Dublin descriptors) | the **spine** (`spine:entry-1` to `spine:8`) and the five **strands** (`strand:knowledge`, `strand:thinking`, `strand:application`, `strand:communication`, `strand:autonomy`) |
| std:ref:qaa-universal-benchmark | the 54 QAA subject benchmarks (top tier; discipline and group tiers to follow by the HESA groupings) | the benchmark outline and the shared threshold expectations |
| std:ref:qaa-guidance | the enterprise and ESD guidance | the shared competency set and the ladder of situation |
| std:ref:uk-assesscriteria | Bristol and Cardiff Met generic criteria | the **band axis** (`band:fail-low` to `band:80-100`) and the shared degree ladder |

**How they link across**, through three shared axes:

```
             spine (levels)        strands (what kind of act)        band (how well, within a level)
framework     defines spine:4..8    defines the five strands           (threshold part = pass band)
benchmark     threshold at spine:6  Annex D's four categories ->       rungs -> bands via Annex D
              master's at spine:7   the five strands                   (threshold 40-49 ... excellent 70+)
guidance      placed on 4..7        competencies -> the five strands   process-over-product row wanted
              (inferred)            (+ attributes and values)
criteria      levels on spine:3..7  criterion rows -> the five strands defines the band axis
```

One sentence: **a statement anywhere in the standards collection can be placed by step, strand and band**, and the reference documents say which words carry each. Verbs mark the strand; qualifiers of context, depth and independence (frameworks, benchmarks), situation (guidance) and degree (criteria) mark the step and the band.

## The three strands from guidance to subject

1. **cites**: the benchmark names the guidance (weakest; a reference).
2. **themeParagraph**: the benchmark says what the theme means in its subject, outside its standards.
3. **themeInStandards**: a benchmark standard (threshold, typical or excellent) uses the theme. Only this strand binds a subject's level.

Benchmarks by strand 3, with the paragraphs (the statement's own numbers):

**Enterprise in benchmark standards (12):** agriculture-rural-environmental-sciences-animal-studies-consumer-science-forestry-food-horticulture-and-human-nutrition-2024 (4.2), art-and-design-2026 (4.4), communication-media-film-and-cultural-studies-2024 (4.10, 4.5, 4.8), computing-2022 (4.6), counselling-and-psychotherapy-2022 (4.3, 4.7), creative-writing-2024 (4.3, 4.4, 4.5), dance-drama-and-performance-2024 (4.7), english-2023 (4.2), housing-studies-2022 (4.8), librarianship-information-knowledge-records-and-archives-management-2025 (4.11), physics-astronomy-and-astrophysics-2025 (4.6), public-policy-and-public-administration-2025 (4.7).

**Sustainability in benchmark standards (37):** accounting-2025 (4.5, 4.8), agriculture-rural-environmental-sciences-animal-studies-consumer-science-forestry-food-horticulture-and-human-nutrition-2024 (4.2), archaeology-2022 (4.3, 4.4), architectural-technology-2022 (4.6, 4.8), architecture-2026 (4.7), art-and-design-2026 (4.4), biomedical-science-and-biomedical-sciences-2023 (4.5), biosciences-2023 (4.5), communication-media-film-and-cultural-studies-2024 (4.4, 4.7, 4.9), computing-2022 (4.14, 4.6), counselling-and-psychotherapy-2022 (4.13, 4.3), creative-writing-2024 (4.3, 4.4, 4.5, 4.7), dance-drama-and-performance-2024 (4.11, 4.14, 4.7, 4.8), early-childhood-studies-2022 (4.4), earth-sciences-environmental-sciences-and-environmental-studies-2022 (4.6), engineering-2023 (4.11, 4.15, 4.8), english-2023 (4.2), finance-2025 (4.4), geography-2022 (4.5, 4.8), health-studies-2024 (4.1, 4.5), history-2022 (4.6), history-of-art-architecture-and-design-2026 (4.5), housing-studies-2022 (4.3, 4.8), land-construction-real-estate-and-surveying-2024 (4.3), landscape-architecture-2024 (4.4), law-2023 (4.4), librarianship-information-knowledge-records-and-archives-management-2025 (4.8), linguistics-2023 (4.5, 4.6), mathematics-statistics-and-operational-research-2023 (4.9), optometry-2024 (4.5), osteopathy-2024 (6.4), policing-in-partnership-with-2022 (4.4), social-policy-2026 (4.13, 4.5, 4.7), social-work-2026 (4.11), theology-and-religious-studies-2022 (4.6), town-and-country-planning-2024 (4.7), veterinary-nursing-2024 (4.2).

**Employability in benchmark standards (23):** accounting-2025 (3.9), agriculture-rural-environmental-sciences-animal-studies-consumer-science-forestry-food-horticulture-and-human-nutrition-2024 (4.3), archaeology-2022 (4.4), architectural-technology-2022 (4.5, 4.8), art-and-design-2026 (4.4), computing-2022 (4.10), counselling-and-psychotherapy-2022 (4.10, 4.13, 4.3), creative-writing-2024 (4.3, 4.4), earth-sciences-environmental-sciences-and-environmental-studies-2022 (4.6, 4.8), english-2023 (4.2), health-studies-2024 (4.4, 4.5), housing-studies-2022 (4.8), land-construction-real-estate-and-surveying-2024 (4.3), landscape-architecture-2024 (4.4), languages-cultures-and-societies-2023 (4.11), law-2023 (4.3), librarianship-information-knowledge-records-and-archives-management-2025 (4.12), linguistics-2023 (4.6), osteopathy-2024 (6.8), philosophy-2025 (4.11), policing-in-partnership-with-2022 (4.4), psychology-2023 (4.10), social-policy-2026 (4.12, 4.5, 4.7).

**Not citing the enterprise guidance (18):** archaeology-2022, architecture-2026, art-and-design-2026, classics-and-ancient-history-including-byzantine-studies-and-modern-greek-2022, counselling-and-psychotherapy-2022, criminology-2022, early-childhood-studies-2022, economics-2023, education-studies-2025, forensic-science-2022, history-2022, history-of-art-architecture-and-design-2026, law-2023, music-2025, osteopathy-2024, philosophy-2025, policing-in-partnership-with-2022, social-work-2026.

**Not citing ESD guidance (5):** anthropology-2024, history-of-art-architecture-and-design-2026, librarianship-information-knowledge-records-and-archives-management-2025, philosophy-2025, policing-in-partnership-with-2022.


## Statement-level maps (where they live)

| From | To | Where | Field |
|---|---|---|---|
| guidance statement | framework statement, criterion, pathway | each guidance document, S4 | `maps` |
| assessment-criteria cell | framework statement | each assessment-criteria document, AC5 | `echoes` |
| FQHEIS descriptor | FHEQ descriptor | the FQHEIS document, S5 | pointer |
| benchmark statement | guidance family, theme | not yet: when each benchmark is ingested (S-02) | proposed `theme`, `mapsTo` |

## What to build next

1. When each benchmark is ingested, tag theme paragraphs and theme-bearing standards with the theme id and a `mapsTo` to the guidance family (each guidance document's GU6 suggestion).
2. A cross-framework level map at statement level (FHEQ, FQHEIS, CQFW), pending since the FHEQ run.
3. A machine-readable copy of the edges (`ingest-std-relations-index.json`) once the edge types are agreed.

## Change notes
- 0.3.1-draft, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.3.0-draft, 3 October 2026, 08:03: the reference layer: four reference documents and the three shared axes (spine, strands, band) by which they link (Abbott, 07:51, 07:57; META D-0211).
- 0.2.0-draft, 3 October 2026, 06:59: the full ESD guidance (run 0063) and the renamed executive summary (`execsummary`, D-std-0012) added; edges `summaryOf`, `readWith` and the ESD guidance's citation of the enterprise guidance; the overlap now seven of eight.
- 0.1.0-draft, 3 October 2026, 05:54: first written (std; runs 0056, 0057).
