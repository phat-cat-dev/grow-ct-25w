import json,collections
D=json.load(open('rb_data.json')); M=json.load(open('rb_more.json')); C=json.load(open('rb_concepts.json'))
agg=D['agg']; n_t=C['n']['threshold']
SN={'K':'strand:knowledge','C':'strand:thinking','A':'strand:application','M':'strand:communication','R':'strand:autonomy'}
EXP={ # concept: (practitioner, student) our words
 'subject knowledge and understanding':("Graduates show broad and well-founded knowledge of the subject's core content.","You know the core content of your subject well and can show it."),
 'theories, concepts and debates':("Graduates understand the subject's main theories and concepts and the debates between them.","You understand the main ideas and theories in your subject and where people disagree about them."),
 'history, context and currency of the field':("Graduates place the subject in its history and context and know where it currently stands.","You know how your subject developed, the settings it works in and what is current in it."),
 'critical evaluation of evidence and arguments':("Graduates evaluate evidence and arguments critically and reach reasoned judgements.","You weigh up evidence and arguments critically and come to reasoned conclusions."),
 'analysis and problem-solving':("Graduates analyse problems and work towards solutions using the subject's approaches.","You break problems down and work out solutions using your subject's methods."),
 'research and enquiry methods':("Graduates understand and use the subject's methods of research and enquiry.","You know how research is done in your subject and can carry out an enquiry yourself."),
 'data, numbers and quantitative reasoning':("Graduates handle data and numbers appropriately for the subject.","You can work with data and numbers in the way your subject needs."),
 'applying knowledge to practice or problems':("Graduates apply subject knowledge to practical situations and problems.","You can use what you know on real problems and in practical settings."),
 'information and sources':("Graduates find, select and use information and sources appropriate to the subject.","You can find, choose and use the right sources and information for your subject."),
 'digital skills':("Graduates use the digital tools and technologies the subject relies on.","You can use the digital tools your subject depends on."),
 'oral or other communication to audiences':("Graduates communicate the subject clearly to different audiences and in different forms.","You can explain your subject clearly to different audiences, in more than one form."),
 'teamwork and collaboration':("Graduates work effectively with others.","You can work well with other people."),
 'independent and self-directed learning':("Graduates manage their own learning and work independently.","You can manage your own learning and work on your own."),
 'reflection and personal development':("Graduates reflect on their learning and practice and plan their development.","You can reflect on how you learn and work, and plan how to improve."),
 'ethics, integrity and values':("Graduates recognise and act on the ethical issues and responsibilities of the subject.","You recognise the ethical questions in your subject and act responsibly."),
 'professional practice and employability':("Graduates understand the subject's professional settings and are prepared for work.","You understand how your subject is used at work and are ready for it."),
 'equality, diversity and inclusion':("Graduates recognise diversity and inclusion as they bear on the subject.","You understand how diversity and inclusion matter in your subject."),
 'sustainability':("Graduates understand the subject's bearing on sustainability and the environment.","You understand how your subject affects sustainability and the environment."),
 'enterprise and creativity':("Graduates show creativity and enterprise in applying the subject.","You can be creative and enterprising in how you use your subject."),
 'written communication':("Graduates write in the forms the subject requires.","You can write in the forms your subject needs."),
}
order=sorted(EXP,key=lambda k:(-len(C['docs']['threshold'].get(k,[])),k))
o=[];w=o.append
w(f'''---
id: std:ref:qaa-universal-benchmark
title: "Reference benchmark (universal): what the QAA subject benchmark statements share"
profile: standards/reference
kind: reference-benchmark
tier: universal          # tiers (Abbott, 07:57): universal, then discipline, then group (the HESA groupings); open point in R0
scope: qaa
sources:
  - {{ id: "stan's 54 held QAA benchmark texts (2022 to 2026 editions)", version: "stan core a3c925b (W-std-0001)", role: text-only }}
  - {{ id: std:doc:qaa-psychology-2023-benchmarks, version: 0.1.1, role: primary }}
builtFrom: "section 4 (Benchmark standards) of each held text, by stan's chunk headings; rung lines and bullet items counted; concepts by keyword rule; verbs placed on revised Bloom through ing:doc:bloom-anderson-krathwohl-2001; scripts rb_analyse.py, rb_more.py, rb_concepts.py, rb_build.py in run-src/"
sharedIds: "uses the spine and strands defined in std:ref:uk-framework"
consumers: "context packs for a HESA grouping in ADAPT's Phase D context dialogue (Abbott, 07:57); an institutional context informs a pack but does not define it"
ours: "a distillation by std; not an issued standard; no issuer's text is reproduced"
pins: {{ template: "standards/reference 0.1.0-draft", layers: "META D-0211" }}
lifecycle: drafted
researchedBy: "std, run R-0002 (reference sweep)"
version: 0.1.0
---

# Reference benchmark (universal): what the 54 QAA subject benchmarks share

> Built by std (run R-0002; Abbott, 07:51 and 07:57). The top tier of three: **universal** (all 54 benchmarks), then **discipline** and **group** references following the HESA groupings (R0). A distillation, not an issued standard. Counts state their denominators; concept and strand assignments are ours, marked `inferred`. Only Psychology has a full ingestion document so far; the rest are read as held texts (`text-only`), so this build rests on section 4 of each statement and will firm up as S-02 ingests the other 53.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
What every QAA subject benchmark statement expects of an honours graduate, whatever the subject, and how the statements are built. Reach for it to see the shared core of subject standards, to write context for a grouping before its own reference exists, and to tell a subject's distinctive standards from the common ones.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Fifty of the 54 statements share one four-section structure, ending in the benchmark standards. Those standards are set at the honours threshold (`spine:6`), in 30 statements also at master's (`spine:7`), and 52 refer to the FHEQ's Annex D classification descriptions. Most use a threshold rung alone or threshold, typical and excellent. Across the {n_t} statements whose threshold items could be read as lists, the shared core is subject knowledge, theory, critical evaluation, analysis, research methods, application, communication to audiences, independence and ethics (R8). As in the frameworks, the rungs climb by qualifiers, not verbs: "critical" and "critically" mark about one threshold item in ten and one excellent item in four.

## Part R Reference

### R0 Tiers
<!-- label: both; status: drafted; basis: primary for the ruling; proposed for the grouping -->
Abbott, 07:57: "reference-discipline-benchmarks and a reference-group-benchmark and then the reference-universal-benchmark to reflect the HESA groupings". Names and ids:

| Tier | Covers | File | Id |
|---|---|---|---|
| universal | all 54 benchmarks (this document) | `ingest-std-qaa-universal-reference-benchmark` | `std:ref:qaa-universal-benchmark` |
| discipline | a broad family of subject areas, such as humanities (proposed: the REF 2021 main panels A to D, pending Abbott) | `ingest-std-qaa-<discipline>-discipline-reference-benchmark` | `std:ref:qaa-<discipline>-discipline-benchmark` |
| group | a HESA subject area (CAH1, 21 areas; for example, historical, philosophical and religious studies) | `ingest-std-qaa-<cah1 slug>-group-reference-benchmark` | `std:ref:qaa-<cah1>-group-benchmark` |

Each benchmark is placed in its group by the HESA codes of its stated subjects (its ingestion document's `subjects`), so the lower tiers wait on S-02. Each tier carries the R8 expectation statements for its grouping.

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
| threshold, typical, excellent | {agg.get('rungset:threshold+typical+excellent',0)} |
| threshold only | {agg.get('rungset:threshold',0)} |
| threshold and excellent | {agg.get('rungset:threshold+excellent',0)} |
| threshold and typical | {agg.get('rungset:threshold+typical',0)} |
| threshold, typical, very good, excellent | {agg.get('rungset:threshold+typical+very good+excellent',0)} (accounting, geography) |
| no rung named | {agg.get('rungset:',0)} (architecture) |

**On the spine:** the threshold rung is the honours threshold at `spine:6` (FHEQ 6, SCQF 10). Master's standards, where given, sit at `spine:7`. **Within step 6**, the rungs line up with Annex D's classes. Accounting states this in full: threshold for a pass or third, typical for a lower second, very good for an upper second, excellent for a first. The others leave it implicit (inferred). Through Annex D the rungs reach the UK marking scale the assessment-criteria references use.

### R3 Strands
<!-- label: both; status: drafted; basis: inferred: concepts by keyword rule on threshold items (rb_concepts.py) -->

Statements (of {n_t} with threshold item lists) whose threshold items touch each concept:

| Strand | Concept | Statements |
|---|---|---|''')
for k in order:
    st=C['concepts'][k]; w(f"| `{SN[st]}` | {k} | {len(C['docs']['threshold'].get(k,[]))} |")
w(f'''
Every strand is covered by most statements; communication is covered mainly as communication to audiences and teamwork, and writing as such is named in only 12. Annex D's four categories (knowledge and understanding, cognitive, practical, transferable skills) map onto the strands as in std:ref:uk-framework R3.

### R4 Concordance

#### R4.1 Statement shapes
<!-- label: both; status: drafted; basis: primary -->
Lead-ins found in section 4, by modality: "will have" {D['modal'].get('will have',0)}; "should be able to" {D['modal'].get('should be able to',0)}; "will be able to" {D['modal'].get('will be able to',0)}; "should have" {D['modal'].get('should have',0)}.

The common lead-in names the award and subject, then the graduate, then the modality: on graduating with an honours degree in the subject, the graduate will have, or should be able to. Two item forms follow it:
- **verb-initial**, after "be able to": demonstrate, understand, identify, apply, appreciate, recognise, use, work;
- **noun-phrase**, after "will have": a knowledge of, an understanding of, the ability to.

The shape is the frameworks' shape, with the subject as the object.

#### R4.2 Verbs
<!-- label: both; status: drafted; basis: inferred: first word of each item; revised Bloom via ing:doc:bloom-anderson-krathwohl-2001 -->

| Rung | Items read | First words, commonest | Mean Bloom (placed) |
|---|---|---|---|''')
for r in ('threshold','typical','excellent'):
    top=[v for v,c in D['verbs'].get(r,[]) if v not in ('the','a','an','knowledge','skills','application','how','be')][:8]
    bl=D['bloom'].get(r,{}); BR=['remember','understand','apply','analyze','evaluate','create']
    tot=sum(bl.values()); mean=sum((BR.index(k)+1)*v for k,v in bl.items())/tot if tot else 0
    w(f"| {r} | {M['items'].get(r,0)} | {', '.join(top)} | {mean:.2f} (n {tot}) |")
w('''
The verbs hardly move between rungs. Demonstrate, understand and identify lead at threshold and recur at excellent.

#### R4.3 Qualifiers
<!-- label: both; status: drafted; basis: primary for presence in items; inferred for grouping -->

Share of items using each qualifier, by rung:

| Qualifier | Threshold | Typical | Excellent |
|---|---|---|---|''')
for q in ['critical','critically','exceptional','independent','independently','original','originality','creative','complex','advanced','comprehensive','sophisticated','some','sound','ethical','professional','digital','sustainable','diversity']:
    row=[]
    for r in ('threshold','typical','excellent'):
        n=M['items'].get(r,0); c=M['qual'].get(r,{}).get(q,0); row.append(f"{100*c/n:.1f}% ({c})" if n else '')
    w(f"| {q} | "+' | '.join(row)+' |')
w('''
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
- { to: std:ref:assessment-criteria, type: marriesThreshold, note: "rungs, through Annex D's classes, onto the UK marking scale (the reference assessment criteria, to build)", basis: inferred }
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

```yaml''')
import yaml
for k in order:
    nk=len(C['docs']['threshold'].get(k,[]))
    p,s=EXP[k]
    w(f"- id: qaa-universal/threshold/{k.split(',')[0].replace(' ','-')}\n  strand: {SN[C['concepts'][k]]}\n  spine: spine:6\n  rung: threshold\n  sharedBy: {nk}   # of {n_t} statements with threshold item lists\n  forPractitioner: {json.dumps(p)}\n  forBeneficiary: {json.dumps(s)}\n  status: drafted\n  core: {'true' if nk*2>=n_t else 'false   # below half: shown for completeness'}")
w('''```

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
- The HESA codes of each benchmark's stated subjects (from S-02 ingestion), for the group tier.
- Abbott's choice of discipline families (R0).

## Part E Gaps and questions
- E1 Text-only: 53 of 54 statements are read as held texts, not ingested documents; the counts will be redone from S-02's records.
- E2 Rung segmentation by keyword misses rungs set out as tables; typical and excellent counts are low and indicative.
- E3 Concept keywords are broad (for example, "others" counts towards teamwork); P3 should sample them.

---

## Change notes
- 0.1.0, 3 October 2026: first build, run R-0002 (Abbott, 07:51, 07:57; META D-0211).
''')
open('/home/claude/wkspc2601-library/ingested/standards/ingest-std-qaa-universal-reference-benchmark/ingest-std-qaa-universal-reference-benchmark.md','w').write('\n'.join(o)+'\n')
print('ok')
