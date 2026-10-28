---
id: std:ref:qaa-universal-benchmark
title: "Reference benchmark (universal): what the QAA subject benchmark statements share"
profile: standards/reference
kind: reference-benchmark
tier: universal          # CAH0; then group (CAH1), discipline (CAH2), subject (CAH3) (Abbott, 07:57, 08:29; META D-0214)
scope: qaa
sources:
  - { id: "stan's 54 held QAA benchmark texts (2022 to 2026 editions)", version: "stan core a3c925b (W-std-0001)", role: text-only }
  - { id: std:doc:qaa-psychology-2023-benchmarks, version: 0.1.1, role: primary }
builtFrom: "section 4 (Benchmark standards) of each held text, by stan's chunk headings; rung lines and bullet items counted; concepts by keyword rule; verbs placed on revised Bloom through ing:doc:bloom-anderson-krathwohl-2001; scripts rb_analyse.py, rb_more.py, rb_concepts.py, rb_build.py in run-src/"
sharedIds: "uses the spine and strands defined in std:ref:uk-framework"
consumers: "context packs for a HESA grouping in ADAPT's Phase D context dialogue (Abbott, 07:57); an institutional context informs a pack but does not define it"
ours: "a distillation by std; not an issued standard; no issuer's text is reproduced"
pins: { template: "standards/reference 0.1.0-draft", layers: "META D-0211" }
lifecycle: drafted
researchedBy: "std, run R-0002 (reference sweep)"
version: 0.1.3
---

# Reference benchmark (universal): what the 54 QAA subject benchmarks share

> Built by std (run R-0002; Abbott, 07:51 and 07:57; tiers aligned to HESA at 08:29). The top tier of four: **universal** (CAH0, all 54 benchmarks), then **group** (CAH1), **discipline** (CAH2) and **subject** (CAH3) references (R0). A distillation, not an issued standard. Counts state their denominators; concept and strand assignments are ours, marked `inferred`. Only Psychology has a full ingestion document so far; the rest are read as held texts (`text-only`), so this build rests on section 4 of each statement and will firm up as S-02 ingests the other 53.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
What every QAA subject benchmark statement expects of an honours graduate, whatever the subject, and how the statements are built. Reach for it to see the shared core of subject standards, to write context for a grouping before its own reference exists, and to tell a subject's distinctive standards from the common ones.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Fifty of the 54 statements share one four-section structure, ending in the benchmark standards. Those standards are set at the honours threshold (`spine:6`), in 30 statements also at master's (`spine:7`), and 52 refer to the FHEQ's Annex D classification descriptions. Most use a threshold rung alone or threshold, typical and excellent. Across the 41 statements whose threshold items could be read as lists, the shared core is subject knowledge, theory, critical evaluation, analysis, research methods, application, communication to audiences, independence and ethics (R8). As in the frameworks, the rungs climb by qualifiers, not verbs: "critical" and "critically" mark about one threshold item in ten and one excellent item in four.

## Part R Reference

### R0 Tiers
<!-- label: both; status: drafted; basis: primary (Abbott, 07:57 and 08:29; META D-0214) -->
Benchmark references follow HESA's Common Aggregation Hierarchy (version 1.3.4). CAH0 is ours, for what every benchmark shares.

| Tier | HESA | Covers | File | Id | Level of the knowledge hierarchy |
|---|---|---|---|---|---|
| universal | CAH0 | all 54 benchmarks (this document) | `ingest-std-qaa-universal-reference-benchmark` | `std:ref:qaa-universal-benchmark` | universal |
| group | CAH1 (21 groups, such as law; business and management) | the benchmarks in one CAH1 group | `ingest-std-qaa-<cah1 slug>-group-reference-benchmark` | `std:ref:qaa-<cah1>-group-benchmark` | practice (practice map) |
| discipline | CAH2 (35 groups) | the benchmarks in one CAH2 group | `ingest-std-qaa-<cah2 slug>-discipline-reference-benchmark` | `std:ref:qaa-<cah2>-discipline-benchmark` | knowledge stream (knowledge map) |
| subject | CAH3 (167 groups) | the benchmarks covering one CAH3 subject | `ingest-std-qaa-<cah3 slug>-subject-reference-benchmark` | `std:ref:qaa-<cah3>-subject-benchmark` | reference (reference map) |

Each benchmark is placed by the HESA codes (HECoS) of its stated subjects (its ingestion document's `subjects`), so the lower tiers wait on S-02. Each tier carries the R8 expectation statements for its grouping, which context packs for that grouping are authored against.

### R1 Common structure
<!-- label: both; status: drafted; basis: primary (stan's chunk headings) -->

| Section | Generic title | Statements with it |
|---|---|---|
| 1 | Context and purposes of a <subject> degree, with sub-sections on the cross-cutting themes | 53 (one titles it "context and characteristics") |
| 2 | Distinctive features of a <subject> degree | 53 |
| 3 | Content, structure and delivery (teaching, learning and assessment) | 51 (two use variant titles) |
| 4 | Benchmark standards | 54 |
| after | references and further resources; membership of the advisory group | 47; 53 |

**Departures:** early childhood studies and engineering retitle section 3; earth sciences retitles section 1; osteopathy uses six sections (context; education and training; knowledge, understanding and skills; teaching and learning; assessment; standards).

**Cross-cutting theme sub-sections in section 1** (heading found as written): accessibility 54, sustainability 54, equality, diversity and inclusion 46, enterprise and entrepreneurship 22 (the rest treat enterprise without that heading).

**Section 4's own outline**, in most statements:
1. scope: the award(s) the standards apply to (honours; master's in 30);
2. a pointer to Annex D (52);
3. the rung model, each rung with a lead-in;
4. items under sub-headings: subject knowledge, understanding and skills (most common), generic skills, knowledge and understanding, subject-specific skills.

### R2 Spine and rungs
<!-- label: both; status: drafted; basis: primary for the counts; inferred for the placing of rungs on Annex D's classes, except where a statement says so -->

| Rung model in section 4 | Statements |
|---|---|
| threshold, typical, excellent | 24 |
| threshold only | 15 |
| threshold and excellent | 7 |
| threshold and typical | 5 |
| threshold, typical, very good, excellent | 2 (accounting, geography) |
| no rung named | 1 (architecture) |

**On the spine:** the threshold rung is the honours threshold at `spine:6` (FHEQ 6, SCQF 10). Master's standards, where given, sit at `spine:7`. **Within step 6**, the rungs line up with Annex D's classes. Accounting states this in full: threshold for a pass or third, typical for a lower second, very good for an upper second, excellent for a first. The others leave it implicit (inferred). Through Annex D the rungs reach the UK marking scale the assessment-criteria references use.

### R3 Strands
<!-- label: both; status: drafted; basis: inferred: concepts by keyword rule on threshold items (rb_concepts.py) -->

Statements (of 41 with threshold item lists) whose threshold items touch each concept:

| Strand | Concept | Statements |
|---|---|---|
| `strand:knowledge` | subject knowledge and understanding | 37 |
| `strand:communication` | oral or other communication to audiences | 33 |
| `strand:thinking` | analysis and problem-solving | 32 |
| `strand:application` | applying knowledge to practice or problems | 32 |
| `strand:application` | research and enquiry methods | 32 |
| `strand:thinking` | critical evaluation of evidence and arguments | 31 |
| `strand:application` | information and sources | 30 |
| `strand:knowledge` | theories, concepts and debates | 30 |
| `strand:autonomy` | ethics, integrity and values | 28 |
| `strand:application` | data, numbers and quantitative reasoning | 27 |
| `strand:application` | digital skills | 27 |
| `strand:knowledge` | history, context and currency of the field | 27 |
| `strand:autonomy` | independent and self-directed learning | 27 |
| `strand:autonomy` | sustainability | 25 |
| `strand:communication` | teamwork and collaboration | 25 |
| `strand:autonomy` | professional practice and employability | 24 |
| `strand:application` | enterprise and creativity | 23 |
| `strand:autonomy` | equality, diversity and inclusion | 22 |
| `strand:autonomy` | reflection and personal development | 21 |
| `strand:communication` | written communication | 12 |

Every strand is covered by most statements; communication is covered mainly as communication to audiences and teamwork, and writing as such is named in only 12. Annex D's four categories (knowledge and understanding, cognitive, practical, transferable skills) map onto the strands as in std:ref:uk-framework R3.

### R4 Concordance

#### R4.1 Statement shapes
<!-- label: both; status: drafted; basis: primary -->
Lead-ins found in section 4, by modality: "will have" 66; "should be able to" 41; "will be able to" 12; "should have" 2.

The common lead-in names the award and subject, then the graduate, then the modality: on graduating with an honours degree in the subject, the graduate will have, or should be able to. Two item forms follow it:
- **verb-initial**, after "be able to": demonstrate, understand, identify, apply, appreciate, recognise, use, work;
- **noun-phrase**, after "will have": a knowledge of, an understanding of, the ability to.

The shape is the frameworks' shape, with the subject as the object.

#### R4.2 Verbs
<!-- label: both; status: drafted; basis: inferred: first word of each item; revised Bloom via ing:doc:bloom-anderson-krathwohl-2001 -->

| Rung | Items read | First words, commonest | Mean Bloom (placed) |
|---|---|---|---|
| threshold | 1285 | demonstrate, understand, identify, apply, appreciate, recognise, work, use | 3.75 (n 559) |
| typical | 122 | demonstrate, understand, work, present, research, identify, critical, values | 3.32 (n 50) |
| excellent | 449 | demonstrate, understand, identify, critically, show, communicate, provide, reflect | 3.88 (n 124) |

The verbs hardly move between rungs. Demonstrate, understand and identify lead at threshold and recur at excellent.

#### R4.3 Qualifiers
<!-- label: both; status: drafted; basis: primary for presence in items; inferred for grouping -->

Share of items using each qualifier, by rung:

| Qualifier | Threshold | Typical | Excellent |
|---|---|---|---|
| critical | 6.8% (88) | 9.8% (12) | 14.3% (64) |
| critically | 3.5% (45) | 14.8% (18) | 10.5% (47) |
| exceptional | 0.0% (0) | 0.8% (1) | 8.5% (38) |
| independent | 1.1% (14) | 4.1% (5) | 2.4% (11) |
| independently | 1.5% (19) | 1.6% (2) | 3.6% (16) |
| original | 0.5% (6) | 3.3% (4) | 1.8% (8) |
| originality | 0.8% (10) | 2.5% (3) | 1.8% (8) |
| creative | 2.3% (30) | 5.7% (7) | 5.6% (25) |
| complex | 2.9% (37) | 10.7% (13) | 5.8% (26) |
| advanced | 1.9% (25) | 2.5% (3) | 4.0% (18) |
| comprehensive | 1.4% (18) | 2.5% (3) | 1.6% (7) |
| sophisticated | 1.2% (15) | 0.8% (1) | 0.9% (4) |
| some | 1.2% (16) | 1.6% (2) | 0.9% (4) |
| sound | 0.6% (8) | 2.5% (3) | 0.7% (3) |
| ethical | 4.7% (60) | 0.0% (0) | 4.0% (18) |
| professional | 5.4% (69) | 5.7% (7) | 4.5% (20) |
| digital | 5.3% (68) | 4.9% (6) | 4.2% (19) |
| sustainable | 1.6% (20) | 0.8% (1) | 3.1% (14) |
| diversity | 1.8% (23) | 0.8% (1) | 2.7% (12) |

**Reading.** The rungs climb by:
- **critical** wording: about 10% of threshold items, 25% of excellent;
- **exceptional**: none at threshold, 8.5% at excellent;
- **independence** and **originality**: each roughly doubles.

This is the frameworks' finding inside step 6: the same verbs, carried higher by qualifiers. Ethical, professional and digital wording sits at the threshold. These are baseline expectations, not marks of excellence.

#### R4.4 Key terms
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { term: threshold, sense: "the minimum every honours graduate in the subject has shown; spine:6" }
- { term: typical, sense: "what most graduates show; in some statements tied to a lower or upper second" }
- { term: excellent, sense: "the best performance; in accounting tied to a first" }
- { term: benchmark standards, sense: "section 4: the rungs and their items" }
- { term: subject knowledge, understanding and skills, sense: "the commonest sub-heading of section 4's items" }
- { term: generic skills, sense: "the second commonest: skills not specific to the subject" }
- { term: Annex D, sense: "the FHEQ's outcome classification descriptions for Level 6, cited by 52 statements" }
```

### R5 Divergences
<!-- label: both; status: drafted; basis: primary -->
1. **Four rungs** (accounting, geography): a very good rung between typical and excellent.
2. **No rung named** (architecture): standards set by the professional route.
3. **Tables or prose in place of lists** (anthropology, architecture, biomedical sciences, computing, education studies, veterinary nursing): their items are not counted in R3 and R4.
4. **Master's standards** in 30 statements, at `spine:7`; not in the others.
5. **Structure** departures in four statements (R1).
6. **Enterprise** carries its own sub-heading in only 22 statements, against accessibility and sustainability in all 54.

### R6 Links
<!-- label: both; status: drafted; basis: primary where the statements state the link; inferred where marked -->
```yaml
- { to: std:ref:uk-framework, type: thresholdAt, note: "threshold at spine:6; master's at spine:7", basis: primary }
- { to: std:ref:uk-framework, type: sharesStrands, note: "Annex D's four categories onto the five strands", basis: inferred }
- { to: std:ref:qaa-guidance, type: themeParagraph, note: "accessibility, sustainability, EDI and enterprise sub-sections in section 1; the guidance documents are the themes' references", basis: primary }
- { to: std:ref:uk-assesscriteria, type: marriesThreshold, note: "rungs, through Annex D's classes, onto the UK marking scale (the reference assessment criteria, to build)", basis: inferred }
- { to: "the discipline and group tiers (R0)", type: parentOf, basis: primary }
```

### R7 Findings
<!-- label: editorial; status: drafted; basis: inferred -->
1. **A common core exists.** At threshold, most subjects ask for the same ten or so things (R8). A context pack can start from this core and add the grouping's and the subject's own.
2. **Subjects differ in objects, not in shape.** The lead-in, verbs and qualifiers are shared. What differs is the subject matter the verbs act on and the professional setting. Group and discipline references should therefore distil objects and settings, not verbs.
3. **The rungs are written like Annex D.** Critical, independent, original and exceptional carry the climb. A reference for a grouping should report that ladder for the grouping's own statements.

### R8 Shared expectations (student-facing and practitioner-facing)
<!-- label: both; status: drafted; basis: inferred: each statement distils a concept that at least half of the statements with threshold item lists share; our words; force describes; at spine:6, threshold -->

Abbott, 07:57: each reference carries "student-facing statements or practitioner facing statements that define ... the shared commonalities" for its grouping, for context packs to be authored against. Universal tier, threshold rung:

```yaml
- id: qaa-universal/threshold/subject-knowledge-and-understanding
  strand: strand:knowledge
  spine: spine:6
  rung: threshold
  sharedBy: 37   # of 41 statements with threshold item lists
  forPractitioner: "Graduates show broad and well-founded knowledge of the subject's core content."
  forBeneficiary: "You know the core content of your subject well and can show it."
  status: drafted
  core: true
- id: qaa-universal/threshold/oral-or-other-communication-to-audiences
  strand: strand:communication
  spine: spine:6
  rung: threshold
  sharedBy: 33   # of 41 statements with threshold item lists
  forPractitioner: "Graduates communicate the subject clearly to different audiences and in different forms."
  forBeneficiary: "You can explain your subject clearly to different audiences, in more than one form."
  status: drafted
  core: true
- id: qaa-universal/threshold/analysis-and-problem-solving
  strand: strand:thinking
  spine: spine:6
  rung: threshold
  sharedBy: 32   # of 41 statements with threshold item lists
  forPractitioner: "Graduates analyse problems and work towards solutions using the subject's approaches."
  forBeneficiary: "You break problems down and work out solutions using your subject's methods."
  status: drafted
  core: true
- id: qaa-universal/threshold/applying-knowledge-to-practice-or-problems
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 32   # of 41 statements with threshold item lists
  forPractitioner: "Graduates apply subject knowledge to practical situations and problems."
  forBeneficiary: "You can use what you know on real problems and in practical settings."
  status: drafted
  core: true
- id: qaa-universal/threshold/research-and-enquiry-methods
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 32   # of 41 statements with threshold item lists
  forPractitioner: "Graduates understand and use the subject's methods of research and enquiry."
  forBeneficiary: "You know how research is done in your subject and can carry out an enquiry yourself."
  status: drafted
  core: true
- id: qaa-universal/threshold/critical-evaluation-of-evidence-and-arguments
  strand: strand:thinking
  spine: spine:6
  rung: threshold
  sharedBy: 31   # of 41 statements with threshold item lists
  forPractitioner: "Graduates evaluate evidence and arguments critically and reach reasoned judgements."
  forBeneficiary: "You weigh up evidence and arguments critically and come to reasoned conclusions."
  status: drafted
  core: true
- id: qaa-universal/threshold/information-and-sources
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 30   # of 41 statements with threshold item lists
  forPractitioner: "Graduates find, select and use information and sources appropriate to the subject."
  forBeneficiary: "You can find, choose and use the right sources and information for your subject."
  status: drafted
  core: true
- id: qaa-universal/threshold/theories
  strand: strand:knowledge
  spine: spine:6
  rung: threshold
  sharedBy: 30   # of 41 statements with threshold item lists
  forPractitioner: "Graduates understand the subject's main theories and concepts and the debates between them."
  forBeneficiary: "You understand the main ideas and theories in your subject and where people disagree about them."
  status: drafted
  core: true
- id: qaa-universal/threshold/ethics
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 28   # of 41 statements with threshold item lists
  forPractitioner: "Graduates recognise and act on the ethical issues and responsibilities of the subject."
  forBeneficiary: "You recognise the ethical questions in your subject and act responsibly."
  status: drafted
  core: true
- id: qaa-universal/threshold/data
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 27   # of 41 statements with threshold item lists
  forPractitioner: "Graduates handle data and numbers appropriately for the subject."
  forBeneficiary: "You can work with data and numbers in the way your subject needs."
  status: drafted
  core: true
- id: qaa-universal/threshold/digital-skills
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 27   # of 41 statements with threshold item lists
  forPractitioner: "Graduates use the digital tools and technologies the subject relies on."
  forBeneficiary: "You can use the digital tools your subject depends on."
  status: drafted
  core: true
- id: qaa-universal/threshold/history
  strand: strand:knowledge
  spine: spine:6
  rung: threshold
  sharedBy: 27   # of 41 statements with threshold item lists
  forPractitioner: "Graduates place the subject in its history and context and know where it currently stands."
  forBeneficiary: "You know how your subject developed, the settings it works in and what is current in it."
  status: drafted
  core: true
- id: qaa-universal/threshold/independent-and-self-directed-learning
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 27   # of 41 statements with threshold item lists
  forPractitioner: "Graduates manage their own learning and work independently."
  forBeneficiary: "You can manage your own learning and work on your own."
  status: drafted
  core: true
- id: qaa-universal/threshold/sustainability
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 25   # of 41 statements with threshold item lists
  forPractitioner: "Graduates understand the subject's bearing on sustainability and the environment."
  forBeneficiary: "You understand how your subject affects sustainability and the environment."
  status: drafted
  core: true
- id: qaa-universal/threshold/teamwork-and-collaboration
  strand: strand:communication
  spine: spine:6
  rung: threshold
  sharedBy: 25   # of 41 statements with threshold item lists
  forPractitioner: "Graduates work effectively with others."
  forBeneficiary: "You can work well with other people."
  status: drafted
  core: true
- id: qaa-universal/threshold/professional-practice-and-employability
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 24   # of 41 statements with threshold item lists
  forPractitioner: "Graduates understand the subject's professional settings and are prepared for work."
  forBeneficiary: "You understand how your subject is used at work and are ready for it."
  status: drafted
  core: true
- id: qaa-universal/threshold/enterprise-and-creativity
  strand: strand:application
  spine: spine:6
  rung: threshold
  sharedBy: 23   # of 41 statements with threshold item lists
  forPractitioner: "Graduates show creativity and enterprise in applying the subject."
  forBeneficiary: "You can be creative and enterprising in how you use your subject."
  status: drafted
  core: true
- id: qaa-universal/threshold/equality
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 22   # of 41 statements with threshold item lists
  forPractitioner: "Graduates recognise diversity and inclusion as they bear on the subject."
  forBeneficiary: "You understand how diversity and inclusion matter in your subject."
  status: drafted
  core: true
- id: qaa-universal/threshold/reflection-and-personal-development
  strand: strand:autonomy
  spine: spine:6
  rung: threshold
  sharedBy: 21   # of 41 statements with threshold item lists
  forPractitioner: "Graduates reflect on their learning and practice and plan their development."
  forBeneficiary: "You can reflect on how you learn and work, and plan how to improve."
  status: drafted
  core: true
- id: qaa-universal/threshold/written-communication
  strand: strand:communication
  spine: spine:6
  rung: threshold
  sharedBy: 12   # of 41 statements with threshold item lists
  forPractitioner: "Graduates write in the forms the subject requires."
  forBeneficiary: "You can write in the forms your subject needs."
  status: drafted
  core: false   # below half: shown for completeness
```

**Above threshold** (typical and excellent; universal tier), the same expectations with:

| Rung | For practitioners | For students |
|---|---|---|
| typical | More of the work is critical, more is independent, and knowledge is wider and more current. | More of what you do is critical and independent, and you know more of what is current. |
| excellent | Critical and independent throughout; some originality; work described as exceptional. | You are critical and independent throughout, show some original thinking, and your work stands out. |

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
See R4.4.

## Part D Sources
<!-- label: both; status: drafted; basis: primary -->

### D1 The source documents
stan's 54 held texts with chunks (W-std-0001, received 03:02, held at `designs/ingest/standards/stan/core/qaa/benchmarks/`); std:doc:qaa-psychology-2023-benchmarks 0.1.1.

### D2 Build log
- 2026-10-03, std, run R-0002: section 4 of each held text by chunk headings; rung lines by keyword; bullet items counted per rung; first words and qualifiers counted; concepts by keyword rule (scripts in `run-src/`).

### D3 Wanted sources
- W-std-0024: the HESA codes of each benchmark's stated subjects (from S-02 ingestion), for the group tier.

## Part E Gaps and questions
- E1 Text-only: 53 of 54 statements are read as held texts, not ingested documents; the counts will be redone from S-02's records.
- E2 Rung segmentation by keyword misses rungs set out as tables; typical and excellent counts are low and indicative.
- E3 Concept keywords are broad (for example, "others" counts towards teamwork); P3 should sample them.

---

## Change notes
- 0.1.3, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.2, 3 October 2026, 10:28: the D3 wanted source given its W id (W-std-0024) from the wanted-sources list (the ingest tool's G7 warning, nts report). No statement changed.
- 0.1.1, 3 October 2026, 08:30: R0 tiers aligned to HESA's CAH: universal CAH0, group CAH1, discipline CAH2, subject CAH3 (Abbott, 08:29; META D-0214); the REF families dropped.
- 0.1.0, 3 October 2026: first build, run R-0002 (Abbott, 07:51, 07:57; META D-0211).

