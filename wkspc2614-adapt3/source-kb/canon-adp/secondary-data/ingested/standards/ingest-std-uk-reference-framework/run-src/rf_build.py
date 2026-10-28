import json,collections
R=json.load(open('rf_recs.json')); T=json.load(open('rf_tables.json')); B=json.load(open('rf_bloom.json'))
STEPS=['entry-2','entry-3','1','2','3','4','5','6','7','8']
SRC=['cqfw','fheq','fqheis','dublin']; AB={'cqfw':'C','fheq':'F','fqheis':'Q','dublin':'D'}
STR=[('K','knowledge','Knowledge and understanding','what is known and understood: its breadth, depth, currency and the awareness of its limits'),
     ('C','thinking','Thinking and judgement','analysing, interpreting, evaluating, arguing and judging, including problem-solving'),
     ('A','application','Application and enquiry','using knowledge, methods and techniques; investigating and researching; carrying out tasks'),
     ('M','communication','Communication','conveying information, ideas, problems and solutions to audiences'),
     ('R','autonomy','Autonomy, responsibility and learning','independence, responsibility for self and others, decisions, initiative and the capacity to keep learning')]
cnt=collections.Counter((r['src'],r['strand']) for r in R)
ex=collections.defaultdict(list)
for r in R: ex[(r['src'],r['strand'])].append(r['id'])
o=[];w=o.append
w('''---
id: std:ref:uk-framework
title: "Reference framework: the UK qualification and level frameworks (FHEQ, FQHEIS, CQFW)"
profile: standards/reference
kind: reference-framework
scope: uk
sources:
  - { id: std:doc:qaa-fheq-2024-framework, version: 0.3.1, role: primary, note: "the FHEQ's descriptors 4.10 to 4.18, and the QF-EHEA Dublin descriptors (Annex B) as held there" }
  - { id: std:doc:qaa-fqheis-2024-framework, version: 0.1.1, role: primary, note: "the FQHEIS's own descriptors 4.11, 4.13, 4.14, 4.16; SCQF 11 and 12 share the FHEQ's 4.17 and 4.18" }
  - { id: std:doc:welsh-government-cqfw-2009-framework, version: 0.1.1, role: primary, note: "the CQFW level descriptors, Entry 1 to Level 8" }
builtFrom: "the three documents' S4 descriptor records (statementType descriptor; 197 records with a level), their S5 crosswalks and SL tables, and their held texts for qualifier terms; scripts rf_analyse.py, rf_tables.py, rf_bloom.py, rf_build.py in run-src/"
sharedIds: "defines the spine (spine:entry-1 to spine:8) and the strands (strand:knowledge, strand:thinking, strand:application, strand:communication, strand:autonomy) that the reference benchmark and the reference guidance reuse"
ours: "a distillation by std; not an issued standard; no issuer's text is reproduced"
pins: { template: "standards/reference 0.1.0-draft", layers: "META D-0211" }
lifecycle: drafted
researchedBy: "std, run R-0001 (reference sweep)"
version: 0.1.0
---

# Reference framework: the UK frameworks (FHEQ, FQHEIS, CQFW)

> Built by std (run R-0001; Abbott, 07:51: "pull out the common hierarchies and terminologies, the commonalities in particular language ... how they all link across"). A distillation of three ingested frameworks, not an issued standard. It defines the **spine** and the **strands** the other references reuse. Every classification here (strand, verb placement, qualifier group) is ours and marked `inferred`; every alignment of levels is the issuers' own and marked `stated`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The common shape of the UK's higher education frameworks. Reach for it to place any level-based statement on one ladder (the spine), to sort it into one of five strands, and to see which words carry a level. It is the hub the reference benchmark, the reference guidance and the assessment criteria link to.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The three frameworks describe the same ladder in different units. The CQFW climbs from Entry 1 to Level 8 in three strands per level. The FHEQ and FQHEIS describe awards, each in two parts: what was shown for the award, and what a typical holder can also do. The Dublin descriptors describe cycles in five headings. Lined up where the issuers state it, they share one spine of eight steps above entry, five strands and one statement shape: a verb, its object, and a qualifier of context, depth or independence. Across Levels 4 to 8 the verbs barely change. The qualifiers carry the level: routine to complex to unpredictable; coherent to systematic to forefront to original; guidance to autonomy to personal responsibility to leadership.

## Part R Reference

### R1 Common structure
<!-- label: both; status: drafted; basis: primary -->

| Layer | CQFW | FHEQ | FQHEIS | Dublin (QF-EHEA) | Reference |
|---|---|---|---|---|---|
| Unit | level | qualification descriptor at a level | qualification descriptor at a level | cycle | **step** on the spine |
| Parts of a unit | three strands | two parts: outcomes demonstrated for the award (threshold); wider abilities of typical holders, with qualities for employment | as the FHEQ | five headings | **part**: `threshold` or `typical`, where the source has them; otherwise one |
| Item | a sentence | a list item under a lead-in | a list item under a lead-in | a sentence | **statement**, sorted into a **strand** |
| Item shape | verb + object + qualifier | lead-in (who, modality) + verb or noun phrase + qualifier | as the FHEQ | lead-in + verb + object + qualifier | **lead-in + verb + object + qualifier** (R4.1) |
| Statements held | 94 | 44 own descriptor items (with Annex D and common material separately) | 35 | 25 | 197 with a level |

**The reference outline**, shared by all three: *spine step, then part (threshold or typical), then strand, then statement.* Any level-based standard can be written to this outline.

### R2 Spine
<!-- label: both; status: drafted; basis: primary for the alignments; each row says which source states it -->

| Step | CQFW | FHEQ | FQHEIS (SCQF) | QF-EHEA | Typical awards | Alignment stated by |
|---|---|---|---|---|---|---|
| `spine:entry-1` to `spine:entry-3` | Entry 1 to 3 | | | | | CQFW only |
| `spine:1` to `spine:3` | Levels 1 to 3 | | | | | CQFW only (below higher education) |
| `spine:4` | Level 4 | Level 4 | SCQF 7 | none | CertHE; HNC | FHEQ 2.24 (CQFW 4 to 8 compare with the FHEQ's); FHEQ Table 1 (CertHE: FHEQ 4, SCQF 7) |
| `spine:5` | Level 5 | Level 5 | SCQF 8 | short cycle | foundation degree; DipHE; HND | FHEQ 2.24; Table 1 |
| `spine:6` | Level 6 | Level 6 | SCQF 9 (ordinary bachelor's) and SCQF 10 (honours) | first cycle (honours) | bachelor's degree, with or without honours | FHEQ 2.24; Table 1 (per qualification: honours at SCQF 10, other bachelor's awards at SCQF 9) |
| `spine:7` | Level 7 | Level 7 | SCQF 11 | second cycle | master's degree | FHEQ 2.24; 4.8 and 4.17 (one descriptor shared by FHEQ 7 and SCQF 11) |
| `spine:8` | Level 8 | Level 8 | SCQF 12 | third cycle | doctoral degree | FHEQ 2.24; 4.8 and 4.18 (shared by FHEQ 8 and SCQF 12) |

Two steps need care. **Step 6 holds two Scottish levels**: SCQF 9 and 10 are both bachelor's, ordinary and honours. **Steps 7 and 8 hold one text for two frameworks**: the shared descriptors. The CQFW states no equivalence of its own; the FHEQ document states the comparison (2.23, 2.24).

### R3 Strands
<!-- label: both; status: drafted; basis: inferred for the assignment of statements (rf_analyse.py: a keyword rule on each record's `about` and `paraphrase`, our words); primary for each source's own headings -->

The five strands every framework tracks, each defined here for reuse by the other references:

| Id | Strand | What it covers |
|---|---|---|''')
for k,slug,name,desc in STR: w(f'| `strand:{slug}` | {name} | {desc} |')
w('''
**Each source's own headings, mapped to the strands:**

| Source | Its headings | Mapped to |
|---|---|---|
| CQFW | knowledge and understanding; application and action; autonomy and accountability | knowledge and thinking (one heading for both); application; autonomy. **No communication heading** |
| FHEQ, FQHEIS | threshold outcomes; wider abilities of typical holders; qualities and transferable skills for employment | not by heading: each item sorted by content (rule above) |
| FHEQ Annex D (classification descriptions, Level 6) | knowledge and understanding; cognitive skills; practical skills; transferable skills | knowledge; thinking; application; communication and autonomy |
| Dublin descriptors | knowledge and understanding; applying knowledge and understanding; making judgements; communication; learning skills | knowledge; application; thinking; communication; autonomy (one to one) |

**Statements per strand** (descriptor records with a level; our assignment):

| Strand | CQFW | FHEQ | FQHEIS | Dublin |
|---|---|---|---|---|''')
for k,slug,name,desc in STR: w(f"| `strand:{slug}` | {cnt[('cqfw',k)]} | {cnt[('fheq',k)]} | {cnt[('fqheis',k)]} | {cnt[('dublin',k)]} |")
w(f"| total | {sum(cnt[('cqfw',k)] for k,*_ in STR)} | {sum(cnt[('fheq',k)] for k,*_ in STR)} | {sum(cnt[('fqheis',k)] for k,*_ in STR)} | {sum(cnt[('dublin',k)] for k,*_ in STR)} |")
w('''
Occurrences (first three statement ids per source and strand) are listed in the build output `run-src/rf_recs.json`; a strand is never asserted without them.

### R4 Concordance

#### R4.1 Statement shapes
<!-- label: both; status: drafted; basis: primary -->

| Source | Lead-in | Force (S4) | Item form |
|---|---|---|---|
| CQFW | none: each sentence stands alone | describes (94) | verb first, in the imperative mood, then object and qualifier |
| FHEQ, FQHEIS: threshold part | awarded to students who have demonstrated ... | threshold (FHEQ 21, FQHEIS 17) | noun phrase (a systematic understanding of ...) or verb phrase (the ability to ...) |
| FHEQ, FQHEIS: typical part | typical holders will be able to ... | will (FHEQ 23 with employment qualities, FQHEIS 18) | verb first, then object and qualifier |
| Dublin descriptors | awarded to students who ... | describes | verb phrase (have demonstrated, can apply, have the ability to ...) |

**The common shape**, which every source fits:

> [lead-in: who, and how firmly] + **verb** + **object** + **qualifier** (of context, of depth, of independence)

The verb says what kind of act (the strand); the object says what it acts on; the qualifier says **how far** (the step). R4.2 and R4.3 show that the step lives mostly in the qualifier.

#### R4.2 Verbs
<!-- label: both; status: drafted; basis: inferred: each verb placed on the revised Bloom taxonomy (ing:doc:bloom-anderson-krathwohl-2001, its verb-form records) at its highest placement; ''' + f"{B['placed']} of {B['total']}" + ''' verb uses placed; the rest are not in the taxonomy's list (address, communicate, undertake, take, exercise, initiate the most frequent) -->

**Mean revised-Bloom process by step** (1 remember, 2 understand, 3 apply, 4 analyse, 5 evaluate, 6 create; *n* = verbs placed):

| Step | CQFW | FHEQ | FQHEIS | Dublin |
|---|---|---|---|---|''')
for s in STEPS:
    m=B['mean'].get(s,{})
    cells=[f"{m[x][0]:.1f} (n {m[x][1]})" if x in m else '' for x in SRC]
    w(f"| `spine:{s}` | "+' | '.join(cells)+' |')
w('''
**Reading.** The verbs climb from the entry levels (about 3, apply) to CQFW Level 3 (4.0, analyse), then **flatten**: from step 4 to step 8 every source sits between about 4 and 5, and the FHEQ's mean even falls. Verbs separate the strands (R3), not the higher education levels. A writer who climbs Bloom's verbs to show a higher level is using a tool these frameworks do not use above step 3.

**Verbs by strand and step** (the issuers' verbs as recorded in S4, with the sources using each: C CQFW, F FHEQ, Q FQHEIS, D Dublin; at most eight per cell, those in more sources first):

| Step | Knowledge | Thinking | Application | Communication | Autonomy |
|---|---|---|---|---|---|''')
for s in STEPS:
    cells=[]
    for k,slug,*_ in STR:
        d=T['verbs'].get(f'{s}|{k}',{})
        items=sorted(d.items(),key=lambda x:(-len(x[1]),x[0]))[:8]
        cells.append(', '.join(f"{v} ({src})" for v,src in items))
    w(f"| `spine:{s}` | "+' | '.join(cells)+' |')
w('''
#### R4.3 Qualifiers
<!-- label: both; status: drafted; basis: primary for presence (each term searched in the statements' held spans), inferred for the grouping -->

Where each qualifier appears on the spine, and in which sources (C CQFW, F FHEQ, Q FQHEIS, D Dublin). Read down a group to see the ladder.
''')
GN={'context':'Context: how defined and familiar the situation is','depth':'Depth: how deep, current and original the knowledge and thinking are','independence':'Independence: how much guidance, and how much responsibility'}
for g in ('context','depth','independence'):
    w(f'**{GN[g]}**\n\n| Term | '+' | '.join(f'`{s}`' for s in STEPS)+' |\n|---|'+'---|'*len(STEPS))
    for term,d in T['lex'][g].items():
        if any(d.values()): w(f'| {term} | '+' | '.join(d[s] for s in STEPS)+' |')
    w('')
w('''**The three ladders**, distilled (ours; each rung a term the sources use at that step):

| Step | Context | Depth | Independence |
|---|---|---|---|
| `spine:entry-2` to `spine:entry-3` | simple, familiar | (what one knows) | with guidance |
| `spine:1` to `spine:2` | routine, well-defined, straightforward | (facts, procedures) | under direction; some autonomy |
| `spine:3` | non-routine, complex but defined | (theory enters) | autonomy within limits |
| `spine:4` | complex, routine for the field | basic, underlying, coherent | personal responsibility |
| `spine:5` | complex; abstract; specialised | well-established, critical | personal responsibility; initiative |
| `spine:6` | complex and unpredictable | systematic, detailed, forefront, current | initiative and personal responsibility |
| `spine:7` | complex, unpredictable, unfamiliar | comprehensive, critical, originality | autonomy, self-direction, independent learning |
| `spine:8` | complex, unpredictable, new | original, new knowledge, at the forefront | leadership, autonomy in a field |

#### R4.4 Key terms
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { term: level, sense: "a step of achievement; the CQFW's unit and the frameworks' common axis (here, the spine)" }
- { term: descriptor, sense: "the text that says what achievement at a level, or for an award, means" }
- { term: threshold, sense: "the minimum for an award (FHEQ, FQHEIS: outcomes demonstrated for the award); the base of the reference benchmark's rungs" }
- { term: typical, sense: "what most holders can also do (FHEQ, FQHEIS); not part of the award's condition" }
- { term: award, sense: "the qualification at a level (CertHE, foundation degree, bachelor's, master's, doctorate)" }
- { term: credit, sense: "volume of learning; Annex C's typical minimums per nation; not used to define a level" }
- { term: cycle, sense: "the QF-EHEA's unit: short, first, second, third; on spine steps 5 to 8" }
- { term: autonomy, sense: "the independence strand's core term: from guidance and direction to self-direction and leadership" }
- { term: forefront, sense: "the depth term that marks steps 6 to 8: knowledge at or informed by the leading edge of a field" }
```

### R5 Divergences
<!-- label: both; status: drafted; basis: primary -->
1. **Below higher education.** Only the CQFW covers Entry 1 to Level 3; the FHEQ and FQHEIS start at step 4.
2. **Two parts or one.** The FHEQ and FQHEIS split each descriptor into a threshold and a typical part; the CQFW and Dublin descriptors have one part.
3. **No communication strand in the CQFW.** Its three strands leave communication implicit; the FHEQ, FQHEIS and Dublin descriptors name it.
4. **Accountability.** The CQFW speaks of accountability and of others' work (supervising, leading); the FHEQ speaks of personal responsibility and qualities for employment.
5. **Force.** The CQFW describes; the FHEQ and FQHEIS state a threshold and what typical holders will do.
6. **Step 6 in Scotland** holds two levels (SCQF 9 and 10); the FHEQ has one.
7. **Annex D** (FHEQ, Level 6 only) adds classification bands within step 6, used by the benchmarks and by assessment criteria, not by the other frameworks.

### R6 Links
<!-- label: both; status: drafted; basis: primary for links the sources state; inferred where marked -->
```yaml
# to the other references
- { to: std:ref:qaa-universal-benchmark, type: thresholdAt, note: "benchmark threshold standards sit at spine:6 (honours), master's standards at spine:7", basis: primary }
- { to: std:ref:qaa-universal-benchmark, type: sharesStrands, note: "Annex D's four categories (knowledge, cognitive, practical, transferable) are this reference's strands; 52 benchmarks cite Annex D", basis: inferred }
- { to: std:ref:qaa-guidance, type: placedOn, note: "the guidance outcomes' verbs placed on the spine in its R2, inferred", basis: inferred }
# to assessment criteria
- { to: std:doc:bristol-generic-2024-assesscriteria, type: marriesThreshold, note: "levels 4 to 7 on spine:4 to spine:7; the pass band at award level meets the threshold part", basis: primary }
- { to: std:doc:cardiffmet-generic-2020-assesscriteria, type: marriesThreshold, note: "levels 3 to 7 on spine:3 to spine:7", basis: primary }
# to the theory side (associations, proposed until reference theories exist; D-0211)
- { strand: strand:knowledge, to: [ing:doc:bloom-anderson-krathwohl-2001, ing:doc:solo-biggs-collis-1982], note: "knowledge dimension; uni- and multistructural", basis: inferred }
- { strand: strand:thinking, to: [ing:doc:delphi-report-facione-1990, ing:doc:critical-being-barnett-1997, ing:doc:critical-lenses-brookfield-1995, ing:doc:solo-biggs-collis-1982], note: "critical thinking; relational and extended abstract", basis: inferred }
- { strand: strand:application, to: [ing:doc:research-skill-development-willison-2007, ing:doc:information-search-process-kuhlthau-1991, ing:doc:experiential-learning-kolb-1984], note: "enquiry and practice", basis: inferred }
- { strand: strand:communication, to: [ing:doc:academic-literacies-lea-street-1998, ing:doc:academic-literacy-across-the-curriculum-wingate-2018], note: "writing and communicating in the discipline", basis: inferred }
- { strand: strand:autonomy, to: [ing:doc:reflective-practitioner-schon-1983, ing:doc:feedback-literacy-carless-boud-2018, ing:doc:new-taxonomy-marzano-kendall-2007], note: "self-direction, reflection, self-regulation (Marzano's self-system)", basis: inferred }
- { qualifiers: depth, to: [ing:doc:solo-biggs-collis-1982], note: "SOLO's structural complexity is the closest theory to the depth ladder", basis: inferred }
```

### R7 Findings
<!-- label: editorial; status: drafted; basis: inferred -->
1. **Write a level with qualifiers, not verbs.** Above step 3 the frameworks keep their verbs and change their qualifiers. An outcome moves up a level by changing its context (familiar to complex to unpredictable), its depth (coherent to systematic to original) or its independence (with guidance to autonomous to leading), not by swapping "describe" for "evaluate".
2. **Choose the verb by strand.** The verb marks what kind of act: knowing, thinking, applying, communicating or self-directing. The five strands are a check that a set of outcomes covers all five.
3. **One outline serves all.** Step, part, strand, statement; and lead-in, verb, object, qualifier. The benchmarks (std:ref:qaa-universal-benchmark) and the guidance (std:ref:qaa-guidance) fit it, so do Bristol's and Cardiff Met's criteria. That is the link across.
4. **Communication is the frameworks' weakest strand** (none in the CQFW; few statements elsewhere) and **autonomy the strongest at the top** (steps 6 to 8). Guidance documents fill the first gap (R6 of the reference guidance).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
See R4.4. Spine and strand ids are this reference's own terms: `spine:<step>` and `strand:<slug>`.

## Part D Sources
<!-- label: both; status: drafted; basis: primary -->

### D1 The source documents
std:doc:qaa-fheq-2024-framework 0.3.1; std:doc:qaa-fqheis-2024-framework 0.1.1; std:doc:welsh-government-cqfw-2009-framework 0.1.1; their held texts in `designs/ingest/standards/held/frameworks/`; ing:doc:bloom-anderson-krathwohl-2001 for verb placements.

### D2 Build log
- 2026-10-03 07:52 to 08:05, std, run R-0001: 197 descriptor records with a level taken from the three documents' S4 (Annex D's classification cells and the provider rules left out: not level descriptors); strands assigned by keyword rule; verbs placed on revised Bloom; qualifier terms searched in each statement's held span. Scripts in `run-src/`.

### D3 Wanted sources
- W-std-0018: the SCQF level descriptors, which would add SCQF 1 to 6 and confirm SCQF 7 to 12 from source.
- W-std-0019: the CQFW's own publication.

## Part E Gaps and questions
- E1 The strand assignment is a keyword rule; P3 should sample it.
- E2 Bloom's list does not hold the frameworks' commonest responsibility verbs (address, undertake, take, exercise, initiate); a SOLO or Marzano placement may suit them better.
- E3 The RQF (England's regulated qualifications) and the EQF are named by the FHEQ but not held.

---

## Change notes
- 0.1.0, 3 October 2026: first build, run R-0001 (Abbott, 07:51; META D-0211).
''')
open('/home/claude/wkspc2601-library/ingested/standards/ingest-std-uk-reference-framework/ingest-std-uk-reference-framework.md','w').write('\n'.join(o)+'\n')
print('ok')
