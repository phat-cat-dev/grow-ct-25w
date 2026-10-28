---
id: std:ref:uk-assesscriteria
title: "Reference assessment criteria: what level-based generic marking criteria share"
profile: standards/reference
kind: reference-assessment-criteria
scope: uk
sources:
  - { id: std:doc:bristol-generic-2024-assesscriteria, version: 0.1.1, role: primary }
  - { id: std:doc:cardiffmet-generic-2020-assesscriteria, version: 0.1.1, role: primary }
builtFrom: "the two documents' AC1 to AC8: bands (AC3), criteria (AC4), ladders (AC6.1), modality (AC6.2), progressions (AC7) and fields (AC8); merged by hand on the UK marking scale"
sharedIds: "uses the spine and strands defined in std:ref:uk-framework; defines the band axis (band:fail-low to band:80-100) for reuse"
ours: "a distillation by std; not an issued standard; no issuer's text is reproduced"
pins: { template: "standards/reference 0.1.0-draft", layers: "META D-0211" }
lifecycle: drafted
researchedBy: "std, run R-0004 (reference sweep)"
version: 0.1.1
---

# Reference assessment criteria: generic, level-based marking criteria (UK)

> Built by std (run R-0004; Abbott, 07:57: "1 yes", a reference for assessment criteria beside the other three). A distillation of two institutions' generic criteria, not an issued standard. It defines the **band axis** that ties marks to the spine, the benchmarks' rungs and the frameworks' thresholds. With two sources, every commonality is a hypothesis for the next set to test.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The common shape of UK generic marking criteria. Reach for it to place any band, mark or class on one axis, to see which words grade a band, and to write criteria or feedback in a shared language.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Both sets are grids with three axes and a cell: level, criterion and band. Both pass at 40 below master's level and mark in tens on the UK scale, so their bands meet on one axis. That axis runs from a low fail to 80 to 100. Both grade bands with one degree ladder: very limited, little, limited, some, sound, clear, good, consistent, thorough, effective, excellent, exceptional and outstanding. The criteria differ in number and grouping but cover the same five strands, except that Cardiff Met has no row for autonomy.

## Part R Reference

### R1 Common structure
<!-- label: both; status: drafted; basis: primary -->

| Axis | Bristol | Cardiff Met | Reference |
|---|---|---|---|
| level | 4 to 7 (FHEQ, stated) | 3 to 7 (FHEQ 4 to 7 stated; 3 as CQFW 3) | **level**, on the spine |
| criterion | 11 to 14 per level, in four categories, varying by level | six at every level: an overall summary and five criteria | **criterion**, sorted into a strand |
| band | seven at levels 4 to 6, six at level 7; labelled by marks, with three mark points each | seven at every level, labelled by class | **band**, on the band axis (R2) |
| cell | a phrase or one or two sentences | a paragraph, cut into sentences (AC5a) | **cell**: descriptor of what the work shows in that band |

**Reference outline:** level, then criterion (in its strand), then band, then cell. A cell's shape is degree word + verb + object, with an independence qualifier at the higher bands.

### R2 Spine and band axis
<!-- label: both; status: primary for each set's own labels; inferred for the class equivalents Bristol leaves unstated -->

**Levels on the spine:** Bristol 4 to 7 on `spine:4` to `spine:7`; Cardiff Met 3 to 7 on `spine:3` to `spine:7`.

**The band axis** (defined here; ids reused by the other references):

| Band id | Marks | Undergraduate class | Master's (level 7) | Pass? | Benchmark rung (via Annex D) |
|---|---|---|---|---|---|
| `band:fail-low` | 0 to 19 (Bristol); 1 to 29 (Cardiff Met) | clear fail | fail | no | |
| `band:fail-high` | 20 to 39 (Bristol); 30 to 39 (Cardiff Met) | narrow fail | fail | no | |
| `band:40-49` | 40 to 49 | third | fail (below the level 7 pass) | yes below level 7 | threshold |
| `band:50-59` | 50 to 59 | lower second | pass | yes | typical (accounting: typical) |
| `band:60-69` | 60 to 69 | upper second | merit | yes | typical to very good |
| `band:70-79` | 70 to 79 | first | distinction | yes | excellent |
| `band:80-100` | 80 to 100 | first (Cardiff Met: first class plus) | distinction | yes | excellent |

**The threshold link:** at award level, the pass band (`band:40-49` below level 7, `band:50-59` at level 7) is where the criteria meet the frameworks' threshold part and the benchmarks' threshold rung. Bristol states this alignment in its preamble; Cardiff Met's band labels state the classes.

### R3 Strands
<!-- label: both; status: drafted; basis: inferred: each criterion row placed in a strand by its name and AC8 fields -->

| Strand | Bristol criteria | Cardiff Met criteria |
|---|---|---|
| `strand:knowledge` | content knowledge; critical approach (in part) | knowledge |
| `strand:thinking` | logical argument and evaluation of perspectives; problem-solving; explanation and interpretation; critical approach; decision-making | analysis; argument |
| `strand:application` | use of evidence and sources; specialist skills and techniques; research | research |
| `strand:communication` | communication; academic skills; teamwork | presentation |
| `strand:autonomy` | self-management; insight; decision-making (in part) | none: the overall summary carries independence in a few phrases |

### R4 Concordance

#### R4.1 Cell shapes
<!-- label: both; status: drafted; basis: primary -->
**Bristol** writes a short phrase per cell: degree word, verb, object. **Cardiff Met** writes a paragraph per cell, opening at levels 3 and 4 with a "may demonstrate" form and from level 5 with plain statements (AC6.2). **Common shape:** [degree word] + verb + object + [independence or scope qualifier]. It is the frameworks' statement shape with the degree word moved to the front.

#### R4.2 The degree ladder
<!-- label: both; status: drafted; basis: primary (each set's AC6.1 ladder, mean band position); merged by std -->

Terms both sets use, with each set's mean band (0 = lowest band, 6 = 80 to 100):

| Term | Bristol | Cardiff Met | Reference band |
|---|---|---|---|
| very limited | 0.4 | 0.2 | `band:fail-low` |
| little | 0.9 | 0.6 | `band:fail-high` |
| limited | 1.7 | 1.6 | `band:40-49` |
| some | 2.4 | 2.4 | `band:40-49` |
| sound | 3.7 | 3.3 | `band:50-59` to `band:60-69` |
| clear, clearly | 4.0 | 3.5 to 3.8 | `band:60-69` |
| good | 4.2 | 4.0 | `band:60-69` |
| well | 4.0 | 4.3 | `band:60-69` |
| successfully | 4.5 | 4.4 | `band:60-69` |
| very good | 4.7 | 5.0 | `band:70-79` |
| confident | 4.7 | 5.0 | `band:70-79` |
| thorough, thoroughly | 4.3 to 4.8 | 4.7 | `band:70-79` |
| effectively | 4.8 | 5.0 | `band:70-79` |
| highly | 5.8 | 4.8 | `band:70-79` to `band:80-100` |
| high | 6.0 | 5.0 | `band:70-79` to `band:80-100` |
| detailed | 5.7 | 5.0 | `band:70-79` to `band:80-100` |
| innovative | 5.6 | 5.4 | `band:70-79` to `band:80-100` |
| excellent | 5.4 | 5.8 | `band:80-100` |
| exceptional | 6.0 | 6.0 | `band:80-100` |
| outstanding | 6.0 | 6.0 | `band:80-100` |

**One set only:**
- Bristol: sufficient, consistent(ly), comprehensive, capable, confidence.
- Cardiff Met: poor, minimal, very little, basic, generally, satisfactory, secure, mastery, strong, perceptive(ly).

**Disagreement:** "informed" sits at 60 to 69 for Bristol (3.9) and at 80 to 100 for Cardiff Met (5.7).

#### R4.3 The independence ladder
<!-- label: both; status: drafted; basis: primary -->

| Band | Bristol | Cardiff Met |
|---|---|---|
| `band:40-49` | with external guidance; with limited external guidance | |
| `band:50-59` | | reliance on tutor support |
| `band:60-69` | | independent thinking |
| `band:70-79` | autonomous | |
| `band:80-100` | autonomously; initiative; setting own goals | |

Bristol carries independence band by band; Cardiff Met barely does. The frameworks carry it level by level (std:ref:uk-framework R4.3). A reference criteria set should carry both.

#### R4.4 Deficits and modality
<!-- label: both; status: drafted; basis: primary -->
Deficit terms per pass-band cell: Bristol 0.10, Cardiff Met 0.93 (against Cardiff Met's own rule that pass bands are written positively). Bristol is plain throughout; Cardiff Met hedges ("may") at levels 3 and 4.

### R5 Divergences
<!-- label: both; status: drafted; basis: primary -->
1. Band labels: marks only (Bristol) or classes (Cardiff Met).
2. Level 7: Bristol merges the two fail bands and passes at 50; Cardiff Met labels level 7 by master's outcomes.
3. Coverage: Cardiff Met adds level 3.
4. Criteria: Bristol's change by level; Cardiff Met's are fixed.
5. No autonomy criterion at Cardiff Met.
6. Cell length: phrase or paragraph.

### R6 Links
<!-- label: both; status: drafted; basis: primary where stated; inferred where marked -->
```yaml
- { to: std:ref:uk-framework, type: marriesThreshold, note: "the pass band at award level meets the threshold part at each spine step", basis: primary }
- { to: std:ref:qaa-universal-benchmark, type: rungsOn, note: "threshold onto band:40-49; typical onto band:50-59 and band:60-69; excellent onto band:70-79 and band:80-100, through Annex D's classes", basis: inferred }
- { to: std:ref:qaa-guidance, type: missingRow, note: "both guidance documents ask for criteria that reward how a solution was reached; neither set has that row (R7)", basis: primary }
- { to: [ing:doc:solo-biggs-collis-1982, ing:doc:feedback-literacy-carless-boud-2018], note: "SOLO's levels as the theory of a degree ladder; feedback literacy for how students read criteria", basis: inferred }
```

### R7 Findings
<!-- label: editorial; status: drafted; basis: inferred -->
1. **One degree ladder serves both sets.** It can be the shared vocabulary for writing any band.
2. **The five strands cover both sets' criteria.** A reference criteria set has one row per strand at least, with autonomy explicit.
3. **Two rows to add:**
   - independence by band (Bristol has it; Cardiff Met does not);
   - an "approach to the problem" row that rewards the route as well as the result, which both guidance documents ask for.
4. **The band axis is the link across.** It joins marks to classes, classes to benchmark rungs, and the pass band to the frameworks' threshold.

### R8 Shared expectations by band (student-facing and practitioner-facing)
<!-- label: both; status: drafted; basis: inferred: each band's statement distils the degree and independence terms both sets place there; our words; any criterion -->

```yaml
- { band: band:fail-low, forPractitioner: "Very little of what the task asks for is shown; major gaps throughout.", forBeneficiary: "Your work shows very little of what was asked, with large gaps." }
- { band: band:fail-high, forPractitioner: "Little of what the task asks for is shown, with significant gaps; close to the pass but short of it.", forBeneficiary: "Your work shows a little of what was asked, but not yet enough to pass." }
- { band: band:40-49, forPractitioner: "Some of what is asked is shown, within limits and with guidance; the threshold for the level.", forBeneficiary: "You show some of what was asked, within limits and with help: enough to pass at this level." }
- { band: band:50-59, forPractitioner: "A sound, generally secure response that shows the main requirements, still relying on some support.", forBeneficiary: "Your work is sound and covers the main points, though you still lean on some support." }
- { band: band:60-69, forPractitioner: "A clear, good and consistent response, done well, with independent thinking.", forBeneficiary: "Your work is clear, good and consistent, and shows your own thinking." }
- { band: band:70-79, forPractitioner: "A thorough, confident and effective response, very good throughout, working autonomously.", forBeneficiary: "Your work is thorough, confident and very good, and you work on your own initiative." }
- { band: band:80-100, forPractitioner: "An excellent to exceptional response, innovative and outstanding, setting its own goals.", forBeneficiary: "Your work is excellent, original and stands out; you set your own goals." }
```

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { term: band, sense: "a mark range with its descriptor; here placed on the band axis" }
- { term: pass band, sense: "the lowest passing band at a level; the threshold link" }
- { term: degree word, sense: "the term that grades a band (limited, sound, thorough, exceptional)" }
```

## Part D Sources
<!-- label: both; status: drafted; basis: primary -->

### D1 The source documents
std:doc:bristol-generic-2024-assesscriteria 0.1.1; std:doc:cardiffmet-generic-2020-assesscriteria 0.1.1.

### D2 Build log
- 2026-10-03 08:00 to 08:02, std, run R-0004: ladders merged from both documents' AC6.1; bands from AC3; criteria from AC4.

### D3 Wanted sources
- More generic criteria sets (a sector set if one exists; other universities') to test the ladder; W-std-0007 (Cardiff Met's simplified descriptors).

## Part E Gaps and questions
- E1 Two sources only.
- E2 The fail bands' ranges differ (0 to 19 and 20 to 39; 1 to 29 and 30 to 39); the axis keeps the issuers' ranges beside its ids.

---

## Change notes
- 0.1.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.0, 3 October 2026: first build, run R-0004 (Abbott, 07:57).
