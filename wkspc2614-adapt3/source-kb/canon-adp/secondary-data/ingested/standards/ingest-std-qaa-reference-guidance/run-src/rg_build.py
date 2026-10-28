import json
G=json.load(open('rg_data.json')); Q=json.load(open('rg_qual.json'))
SN=[('K','knowledge'),('C','thinking'),('A','application'),('M','communication'),('R','autonomy')]
BR=['remember','understand','apply','analyze','evaluate','create']
def pct(k,q): n=Q[k]['n']; c=Q[k]['q'].get(q,0); return f"{100*c/n:.0f}% ({c})"
SHARED=[ # (esd competency, eee theme, ids, prac, ben)
 ('systems thinking','decision',"outcome.systems.s4; enterprise outcome.decision.b3","Graduates analyse and synthesise complex, connected information to see how a situation works as a whole.","You pull together complex, connected information to see how the whole situation works."),
 ('anticipatory thinking','communication; opportunity',"outcome.anticipatory.s1, s8, s9; enterprise outcome.opportunity.b4","Graduates picture possible futures, weigh their risks and use them to decide what to do.","You picture possible futures, weigh up their risks and use them to decide what to do."),
 ('critical thinking','decision',"outcome.critical.s5; enterprise outcome.decision.b2","Graduates weigh information and build reasoned arguments, alone and with others.","You weigh up information and build reasoned arguments, on your own and with others."),
 ('strategic thinking','implementation; decision',"narrative.strategic.1; enterprise outcome.implementation.b1","Graduates plan and manage action and resources towards a goal and review how it went.","You plan and manage action and resources towards a goal, and review how it went."),
 ('collaborative','communication; implementation',"outcome.collaborative.s5, s9; enterprise outcome.communication.b3","Graduates work with stakeholders, build trust, negotiate and lead.","You work with the people involved, build trust, negotiate and take the lead."),
 ('integrated problem-solving','creativity; opportunity',"outcome.problem.s2 to s4; enterprise outcome.creativity.b1, outcome.opportunity.b2","Graduates generate several workable solutions to real problems and choose between them.","You come up with several workable answers to real problems and choose between them."),
 ('self-awareness','reflection; the mindset family',"outcome.selfaware.k1, s3; enterprise outcome.reflection.b3","Graduates evaluate their own capabilities and learning needs and act on them.","You work out your own strengths and what you still need to learn, and act on it."),
]
o=[];w=o.append
w(f'''---
id: std:ref:qaa-guidance
title: "Reference guidance: what QAA's cross-cutting theme guidance documents share"
profile: standards/reference
kind: reference-guidance
scope: qaa
sources:
  - {{ id: std:doc:qaa-enterprise-2018-guidance, version: 0.1.2, role: primary }}
  - {{ id: std:doc:qaa-advancehe-esd-2021-guidance, version: 0.1.1, role: primary }}
builtFrom: "the two documents' S4 records (310 in all; {G['eee']['student']+G['esd']['student']} addressed to students or graduates), their GU analyses and held texts; scripts rg_analyse.py, rg_build.py in run-src/"
sharedIds: "uses the spine and strands defined in std:ref:uk-framework"
consumers: "context packs (Abbott, 07:57), through the reference benchmarks' theme sub-sections"
ours: "a distillation by std; not an issued standard; no issuer's text is reproduced"
pins: {{ template: "standards/reference 0.1.0-draft", layers: "META D-0211" }}
lifecycle: drafted
researchedBy: "std, run R-0003 (reference sweep)"
version: 0.1.0
---

# Reference guidance: QAA's cross-cutting themes (enterprise, sustainability)

> Built by std (run R-0003; Abbott, 07:51). A distillation of the two theme guidance documents held, not an issued standard. Two sources are few. This build fixes the shape that later guidance documents (equality, diversity and inclusion; accessibility; digital; Advance HE's compilations) will be added to, and each addition will test it.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The common shape of sector guidance on a cross-cutting theme. Reach for it to see what theme guidance asks of every student and graduate whatever the theme, how it differs from a framework or benchmark (level-free, competency-led, future-facing), and how a theme's expectations attach to the levels and strands.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Both documents speak in four voices: to students and graduates (what they should be able to do), to educators (what to offer), to institutions (what to commit to), and about pedagogy. Their standards core is a set of **competencies** stated as outcomes with no level. Both centre on the same practice: thinking about futures under uncertainty, judging, planning and leading change with others, solving real problems in several ways, and reflecting on oneself. Seven of ESD's eight competencies have an enterprise counterpart. Where frameworks qualify by depth and independence, theme guidance qualifies by **uncertainty, change, the future and other people**.

## Part R Reference

### R1 Common structure
<!-- label: both; status: drafted; basis: primary -->

| Reference family | What it holds | Enterprise (families) | ESD (families) |
|---|---|---|---|
| purpose | why the theme matters and what it aims at | aim, principle | aim |
| definitions and vocabulary | the theme's terms and its capabilities named | vocab | (Part B; competencies named in Table 1) |
| competencies | the capabilities, named and described | vocab, mindset | competency (Table 1), narrative |
| progression | how capability grows | journey (four stages) | ways of thinking, practising and being |
| **outcomes** | what a graduate should be able to do | outcome (23, seven themes) | outcome (128, eight competencies by three columns) |
| opportunities | what teaching should offer | delivery (33) | students, employers, communities, environment |
| assessment | how to assess the theme | assessment (9), goal | assessment (7), design |
| educator | what educators do or need | educator (4) | academics (6) |
| institution | what the provider commits to | institution (5) | principle (5), services (3) |
| pedagogy | teaching models, named only | GU7 | GU7 |

**The reference outline:** purpose, vocabulary, competencies, progression, outcomes, then opportunities, assessment, educator and institution. Only the outcomes and the competencies are student-facing standards. The rest are conditions for meeting them.

### R2 Spine
<!-- label: both; status: drafted; basis: inferred -->
Neither document has levels. Both describe growth: enterprise in four stages, ESD as a journey through ways of thinking, practising and being. Placed on the spine (std:ref:uk-framework R2), by our reading:

| Spine | Enterprise stage | ESD outcome columns (verb profile) |
|---|---|---|
| `spine:4` | awareness | knowledge column (35 of 38 outcomes open with L4 verbs) |
| `spine:5` | mindset; early capability | skills column, apply and analyse |
| `spine:6` | capability | skills column, evaluate and judge |
| `spine:7` | effectiveness | skills and values columns, negotiate, facilitate, lead |

### R3 Strands
<!-- label: both; status: drafted; basis: inferred: student- and graduate-addressed records sorted by keyword rule (rg_analyse.py) -->

| Strand | Enterprise ({G['eee']['student']}) | ESD ({G['esd']['student']}) |
|---|---|---|''')
for k,s in SN: w(f"| `strand:{s}` | {G['eee']['strand'].get(k,0)} | {G['esd']['strand'].get(k,0)} |")
w(f'''
The guidance documents weight the strands differently from the frameworks. Application, autonomy and communication carry a larger share; knowledge a smaller. Communication, the frameworks' weakest strand, is fuller here: stakeholders, negotiation, mediation, persuasion.

**Employability tags** (all records): enterprise direct {G['eee']['emp'].get('direct',0)}, bridge {G['eee']['emp'].get('bridge',0)}, academic {G['eee']['emp'].get('academic',0)}; ESD direct {G['esd']['emp'].get('direct',0)}, bridge {G['esd']['emp'].get('bridge',0)}, academic {G['esd']['emp'].get('academic',0)}. Theme guidance is mostly **bridge**: capabilities that hold in study and at work.

### R4 Concordance

#### R4.1 Statement shapes
<!-- label: both; status: drafted; basis: primary -->

| Source | Lead-in | Item form |
|---|---|---|
| enterprise | graduates should be able to | verb-initial, one capability per item, grouped by theme |
| ESD | a student with this competency can | verb-initial, in three columns: knowledge, skills, attributes and values |
| both | (educators) delivery should include opportunities to; (institutions) an institution will, ESD is best achieved when | opportunity or commitment, not a student standard |

The student-facing shape is the frameworks' shape without a level: lead-in, verb, object, qualifier. ESD adds a third kind of outcome the frameworks and benchmarks lack: **attributes and values**.

#### R4.2 Verbs
<!-- label: both; status: drafted; basis: inferred: first verb of each student-facing record on revised Bloom (ing:doc:bloom-anderson-krathwohl-2001) -->

| Bloom process | Enterprise | ESD |
|---|---|---|''')
for b in BR: w(f"| {b} | {G['eee']['bloom'].get(b,0)} | {G['esd']['bloom'].get(b,0)} |")
w(f'''
Enterprise leans to **create** (generate, develop, design); ESD to **analyse** and **create**. Both use action verbs that frameworks keep for the upper levels: lead, negotiate, mediate, facilitate.

#### R4.3 Qualifiers
<!-- label: both; status: drafted; basis: primary for presence (each student-facing record's held span) -->

| Qualifier | Enterprise | ESD | Group |
|---|---|---|---|''')
for q,g in [('opportunit','opportunity'),('risk','uncertainty'),('uncertain','uncertainty'),('change','change'),('future','future'),('complex','complexity'),('multiple','plurality'),('others','other people'),('stakeholder','other people'),('value','value and values'),('values','value and values'),('ethical','value and values'),('sustainab','theme'),('reflect','self'),('critical','depth'),('independent','independence')]:
    w(f"| {q} | {pct('eee',q)} | {pct('esd',q)} | {g} |")
w('''
**Reading.** Frameworks and benchmarks qualify a statement by depth and independence. Theme guidance qualifies it by **situation**: uncertain, changing, future, involving others, carrying value. Critical and independent wording is rare. This is the guidance's distinctive contribution to the shared language: a third ladder, of situation, beside the frameworks' context ladder.

#### R4.4 Key terms
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { term: competency, sense: "a capability combining knowledge, skill and disposition; both documents' core unit (ESD: eight, after UNESCO; enterprise: behaviours, attributes, competencies)" }
- { term: attribute, sense: "a personal quality (open-minded, resilient); ESD's attributes-and-values column" }
- { term: mindset, sense: "enterprise's stage of seeing oneself as capable; ESD's ways of being" }
- { term: opportunity, sense: "enterprise's object of action; ESD's chance to learn (opportunities offered)" }
- { term: stakeholder, sense: "the other people a graduate works with or for; both documents" }
- { term: employability, sense: "kept apart from the themes by both; most theme capabilities are bridges to it" }
```

### R5 Divergences
<!-- label: both; status: drafted; basis: primary -->
1. **Values.** ESD's normative competency and attributes-and-values column have no enterprise counterpart.
2. **Ventures and finance.** Enterprise's venture creation, financial and business literacy and intellectual property have no ESD counterpart.
3. **Grid or list.** ESD sets its outcomes in a competency-by-column grid; enterprise in themed lists.
4. **Stages.** Enterprise names four stages of growth; ESD names three ways but no stages.
5. **Systems.** ESD's systems thinking is fuller than anything in enterprise.

### R6 Links
<!-- label: both; status: drafted; basis: primary where stated; inferred where marked -->
```yaml
- { to: std:ref:uk-framework, type: placedOn, note: "outcomes placed on spine:4 to spine:7 by stage and verb profile (R2)", basis: inferred }
- { to: std:ref:qaa-universal-benchmark, type: themeParagraph, note: "the benchmarks' section 1 theme sub-sections: sustainability in all 54, enterprise headed in 22; 49 cite ESD guidance, 36 the enterprise guidance", basis: primary }
- { to: std:ref:assessment-criteria, type: needsCriterion, note: "both documents ask for criteria that reward how a solution was reached over the solution", basis: primary }
- { from: std:doc:qaa-advancehe-esd-2021-guidance, to: std:doc:qaa-enterprise-2018-guidance, type: cites, basis: primary }
# to the theory side (associations, proposed)
- { strand: strand:application, to: [ing:doc:experiential-learning-kolb-1984, ing:doc:situated-learning-lave-wenger-1991], note: "learning through real problems and practice", basis: inferred }
- { family: values, to: [ing:doc:affective-domain-krathwohl-bloom-masia-1964, ing:doc:significant-learning-fink-2003], note: "attributes and values; Fink's human dimension and caring", basis: inferred }
- { strand: strand:autonomy, to: [ing:doc:new-taxonomy-marzano-kendall-2007, ing:doc:reflective-practitioner-schon-1983], note: "self-system, metacognition, reflection", basis: inferred }
```

### R7 Findings
<!-- label: editorial; status: drafted; basis: inferred -->
1. **Theme guidance adds a ladder of situation.** Where frameworks raise a level by depth and independence, guidance raises the stakes by situation: more uncertain, more changing, more future-facing, more involving others. An outcome can climb on all three ladders.
2. **It adds a kind of outcome.** Attributes and values sit beside knowledge and skills. The frameworks and benchmarks have no place for them, so a reference outcome set should.
3. **One competency set serves both themes.** Seven competencies are shared (R8). Later theme guidance should be tested against them before it is given its own.

### R8 Shared expectations (student-facing and practitioner-facing)
<!-- label: both; status: drafted; basis: inferred: each statement distils a competency both documents state, citing both documents' record ids; our words; level-free -->

```yaml''')
for comp,theme,ids,p,s in SHARED:
    w(f"- id: qaa-guidance/shared/{comp.replace(' ','-')}\n  esdCompetency: {json.dumps(comp)}\n  enterpriseTheme: {json.dumps(theme)}\n  occurrences: {json.dumps(ids)}\n  forPractitioner: {json.dumps(p)}\n  forBeneficiary: {json.dumps(s)}\n  status: drafted")
w('''```

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
See R4.4.

## Part D Sources
<!-- label: both; status: drafted; basis: primary -->

### D1 The source documents
std:doc:qaa-enterprise-2018-guidance 0.1.2; std:doc:qaa-advancehe-esd-2021-guidance 0.1.1; their held texts in `designs/ingest/standards/held/guidance/`.

### D2 Build log
- 2026-10-03, std, run R-0003: student- and graduate-addressed records sorted into strands; verbs placed on Bloom; qualifier terms searched in held spans; families aligned by hand from both documents' GU1; shared competencies from the ESD document's GU2 crosswalk.

### D3 Wanted sources
- QAA's or Advance HE's guidance on equality, diversity and inclusion, accessibility and digital, the other cross-cutting themes the benchmarks carry, to test this shape.
- W-std-0013 (EntreComp) and W-std-0009 (UNESCO 2017): the competency frameworks behind the two documents.

## Part E Gaps and questions
- E1 Two sources only: every commonality here is a hypothesis for the next guidance document to test.
- E2 The strand rule differs from the frameworks' (keywords suited to competency language); P3 should compare the two on a sample.

---

## Change notes
- 0.1.0, 3 October 2026: first build, run R-0003 (Abbott, 07:51; META D-0211).
''')
open('/home/claude/wkspc2601-library/ingested/standards/ingest-std-qaa-reference-guidance/ingest-std-qaa-reference-guidance.md','w').write('\n'.join(o)+'\n')
print('ok')
