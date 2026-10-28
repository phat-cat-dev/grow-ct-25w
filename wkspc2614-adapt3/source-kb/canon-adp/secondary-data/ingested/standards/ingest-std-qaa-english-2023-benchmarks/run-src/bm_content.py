# bm_content.py: judgement file for run 0105, QAA Subject Benchmark Statement English (September 2023), std.
# Built by tools/bm_build.py english-2023 (BM-BRIEF 0.2.2; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Statements: the benchmark standards table in 4.2 (three columns, threshold, typical and excellent, held text linearised
# cell by cell, so each skeleton bullet 4.2.b1 to b85 is one cell item, assigned to its column by reading the rows), the
# excellent rung's defining paragraph (4.2.ex1); the subject knowledge paragraph that spans the three columns (4.2.sk1 to
# sk3); the outcome lists 1.6 (can) and 2.2 (will know about); and five obliging or outcome paragraphs or sentences
# (2.4, 2.5, 2.10, 3.3.s1, 4.2).

HON = "bachelor's with honours"
SID = 'qaa/english-2023'
CITE = 'QAA (2023), English Subject Benchmark Statement'
KN, UN, SK, GS = 'knowledge', 'understanding', 'subject-skill', 'generic-skill'
LEAD_T = 'This is the minimum requirement that should be reached by graduates of a bachelor'
LEAD_TY = 'Graduates who have studied English as a significant component of their degree are able to:'
LEAD_EX = 'Graduates are able to:'

META = dict(
  run='0105', p1='2026-10-03 17:11',
  title='Subject Benchmark Statement English',
  heading='Subject Benchmark Statement: English (QAA, September 2023)',
  edition='September 2023', published='2023-09',
  status='current', supersedes='Subject Benchmark Statement for English, fourth edition (2019), as section 6 names it',
  subjects=[
    dict(scheme='hecos', code='100320', label='English studies', basis='stated'),
    dict(scheme='cah', code='CAH19-01', label='English studies', basis='stated'),
    dict(scheme='hecos', code='100318', label='English language', basis='stated'),
    dict(scheme='cah', code='CAH19-01-02', label='English language', basis='stated'),
    dict(scheme='hecos', code='100319', label='English literature', basis='stated'),
    dict(scheme='cah', code='CAH19-01-03', label='literature in English', basis='stated'),
    dict(scheme='hecos', code='100046', label='creative writing', basis='stated'),
    dict(scheme='cah', code='CAH19-01-05', label='creative writing', basis='stated'),
    dict(scheme='cah', code='CAH19-01-01', label='English studies (non-specific)', basis='inferred')],
  awards=[HON], levels=['fheq:6', 'fqheis:10'],
  nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
  series='QAA Subject Benchmark Statements, 2023 revision with the cross-cutting themes (fifth edition of this statement, inferred)',
  partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
  agentDefinition=("QAA's UK reference point for what an honours graduate in English, across language, literature and creative writing, "
    "knows, understands and can do. Its standards form one table with three columns (threshold, typical, excellent) and rows for "
    "generic skills; subject knowledge; embedded equality, access, sustainability and enterprise; creative writing. It stands beside "
    "two earlier outcome lists. Reach for it when designing, reviewing or describing an English course, its modules or its "
    "outcomes. It is not a curriculum and not a regulatory requirement in England."),
  summary=("Published by QAA in September 2023, the statement covers English in its broad sense (language, literature and creative "
    "writing, in single, joint and interdisciplinary honours courses) and sets out the subject's purposes, its distinctive "
    "features (design, progression, flexibility, partnership, review) and its content, teaching and assessment. Its benchmark "
    "standards for the bachelor's degree with honours are a single table read across three columns: 26 threshold items, 27 "
    "typical items and 33 excellent records (the excellent rung's defining paragraph and 32 items), with a paragraph on subject "
    "knowledge that spans all three. Earlier lists say what English graduates can do (1.6) and will know about (2.2). It carries "
    "the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; "
    "enterprise and entrepreneurship education) and treats large language models under academic integrity. It cites FHEQ "
    "Level 6 with FQHEIS Level 10 and Annex D for the honours classifications; it names UNESCO and points to the Creative "
    "Writing and Linguistics statements, but names no professional body for the subject."))

S2 = dict(
  governs="what can be expected of an English graduate at the end of an honours degree, and what courses in the subject provide",
  awards=[HON], levels=['fheq:6', 'fqheis:10'],
  statedScope='"This document is a QAA Subject Benchmark Statement for English that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter)',
  statedSubjects=[
    dict(name='English (language, literature and creative writing, in its broadest sense)', locator='(D1, 1.1, 1.2)', kind='subject', codes=[dict(scheme='hecos', code='100320', label='English studies'), dict(scheme='cah', code='CAH19-01', label='English studies')]),
    dict(name='English Literature; English Language; English Language and Literature; English Literature and Creative Writing', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100319', label='English literature'), dict(scheme='hecos', code='100318', label='English language'), dict(scheme='hecos', code='100046', label='creative writing')]),
    dict(name='joint, combined and major-minor degrees with English', locator='(D1, 1.1, 2.5)', kind='programme title', codes=[]),
    dict(name='undergraduate courses leading to a named award with English in its title (postgraduate provision outside scope)', locator='(D1, 1.3)', kind='programme title', codes=[])])

SECTIONS = {'1': 'Context and purposes of an English Degree', '2': 'Distinctive features of an English Degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.3', 'Context and purposes of an English Degree'),
       ('1.4', '1.7', 'Purposes and characteristics of an English Degree'),
       ('1.8', '1.11', 'Equality, diversity and inclusion'), ('1.12', '1.13', 'Accessibility'),
       ('1.14', '1.16', 'Education for Sustainable Development'), ('1.17', '1.22', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.3', 'Design'), ('2.4', '2.6', 'Progression'), ('2.7', '2.7', 'Accessibility and flexibility'),
       ('2.8', '2.8', 'Partnership'), ('2.9', '2.12', 'Monitoring and review'),
       ('3.1', '3.4', 'Content'), ('3.5', '3.9', 'Teaching and learning'), ('3.10', '3.12', 'Assessment'),
       ('4.1', '4.2', 'Introduction')]

G = {
 '1.1': 'language, literature and creative writing; single, joint and interdisciplinary honours; course titles',
 '1.2': 'English in its broad sense; neighbouring subjects; Linguistics and Creative Writing statements',
 '1.3': 'scope limited to undergraduate named awards; postgraduate provision noted',
 '1.4': 'studying meaning through communication; what the subject enables',
 '1.5': 'capacities shared with the SHAPE subjects (a list)', '1.6': 'what English graduates can do (an outcome list)',
 '1.7': 'dialogue, debate and difference in teaching', '1.8': 'diversity, plural voices and contested narratives',
 '1.9': 'the history of the discipline and persistent imbalances', '1.10': 'diversifying curricula; core and optional',
 '1.11': 'graduates who argue well and attend to audiences', '1.12': 'accessible courses and attention to practical challenges',
 '1.13': 'routes of entry; international and adult students', '1.14': 'ESD defined; English working towards it',
 '1.15': 'environment, ecocriticism, world literatures and global citizenship', '1.16': 'creativity and sustainable futures',
 '1.17': 'what enterprise education supports', '1.18': 'four core abilities; careers and value',
 '1.19': 'communication and context as enterprise', '1.20': 'collaboration, self-management and integrity',
 '1.21': 'creativity, resilience and new technologies', '1.22': 'critical thinking and problem-solving for enterprise',
 '2.1': 'varied approaches across the sector', '2.2': 'what graduates will know about (an outcome list)',
 '2.3': 'pointer to the content paragraphs (a reference)', '2.4': 'progression across levels to the threshold; postgraduate study',
 '2.5': 'combined, joint and major-minor routes', '2.6': 'exit awards; course length in the four nations',
 '2.7': 'flexible and accessible teaching and assessment (examples)', '2.8': 'placements and partner organisations',
 '2.9': 'monitoring and periodic review', '2.10': 'external reviewers in periodic review',
 '2.11': 'external examiners and threshold standards', '2.12': 'accreditation for vocational outcomes',
 '3.1': 'varied design; combinations with other subjects', '3.2': 'English language: varieties, methods and sub-disciplines',
 '3.3': 'English literature: periods, forms, contexts and theory', '3.4': 'creative writing within English',
 '3.5': 'dialogue, collaboration and co-creation in teaching', '3.6': 'structured preparation for classes',
 '3.7': 'independent study and flipped lectures', '3.8': 'small-group teaching', '3.9': 'libraries, corpora and the capstone project',
 '3.10': 'diverse assessment; accessibility', '3.11': 'forms of assessment (a list)', '3.12': 'what assessment rewards (a list)',
 '4.1': 'the threshold as the minimum for honours', '4.2': 'Annex D; the three-column standards table'}

CTYPE = {k: 'area' for k in ['3.2', '3.3', '3.4']}
CTYPE.update({k: 'practice' for k in ['2.7', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12']})

EXCLUDED = [
  dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2, S7 and SB6'),
  dict(number='1, 2, 3, 4', heading='section heading lines', kind='other: headings, recorded in SECTIONS'),
  dict(number='5', heading='List of references and further resources', kind='other: four references, read for SB6'),
  dict(number='6', heading='Membership of the Advisory Groups (2023, 2019, 2015, 2007)', kind='other: authorship history, read for S7 supersedes')]

# ------------------------------------------------------------------ statements
P = {}

def fq(fw):
    """the FQHEIS level 10 counterpart of an FHEQ level 6 descriptor id (4.16 has no b3.1 or b3.2)."""
    return fw.replace('4.15', '4.16').replace('b3.1', 'b3').replace('b3.2', 'b3')

# ---- outcome list 1.6 ("English graduates can:")
def k16(k, verbs, about, domain, core, ben, nb, fw, when, q):
    P['1.6.b%d' % k] = dict(
      type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates in English', addressee='learner',
      verbs=verbs, about=about, domain=domain, award=HON,
      para=f"English graduates can show {core}.",
      prac=f"Expect a graduate of an English course to show {core}; the statement names it as part of what marks the subject out.",
      ben=f"By the end of your English degree, you can {ben}.",
      aaw=(f"Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), "
           f"for the honours degree at FHEQ level 6 (FQHEIS level 10): {about}. Cite it as {CITE}, para 1.6, bullet {k}. "
           f"Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the "
           f"standards themselves are the 4.2 table. Set it beside {nb}, qaa/fheq-2024/{fw} and qaa/fqheis-2024/{fq(fw)}."),
      aad=(f"Raise this when {when}. With a student, put it plainly as something the subject builds in you over the degree; with staff, "
           f"frame it as a distinctive capacity an English course develops. Ask: {q} Avoid reading the list aloud or treating it as the pass standard."))

k16(1, ['read'], 'close, analytical and critical reading in context', SK,
    "the capacity to read texts closely and critically, aware of literary form and of the history and language around them",
    "read texts closely and critically, aware of their form and of their historical and linguistic setting",
    '4.2.b47 and 4.2.b48', '4.15.b2', 'a student asks what reading at degree level involves',
    "'When you read a passage closely, what do you notice first: its form, its language or its moment in history?'")
k16(2, ['understand'], 'verbal creativity and aesthetic features of texts', UN,
    "a grasp of creativity in language, including the aesthetic qualities of literary and other cultural works",
    "understand how language can be creative, and the aesthetic qualities of literary and other cultural works",
    '4.2.b52 and 1.6.b3', '4.15.b1', 'a student wonders why style and wordplay matter',
    "'Where in a text you know well does the language itself do something surprising?'")
k16(3, ['analyse', 'respond', 'using'], 'analysing discourse and the force of language', SK,
    "the capacity to analyse spoken and written texts and discourse and to respond to how language moves and persuades, with fitting methods and terms",
    "analyse spoken and written texts and discourse, and respond to how language moves and persuades, using suitable methods and terms",
    '4.2.b10, 4.2.b12 and 4.2.b13', '4.15.b7', 'a student is preparing a discourse or rhetorical analysis',
    "'What method would you use to show how this speech tries to persuade its audience?'")
k16(4, ['reflect'], 'reflecting on reading, writing and interpretation', SK,
    "critical reflection on what happens when we read, write and interpret",
    "think critically about what happens when you read, write and interpret",
    '4.2.b30, 4.2.b35 and 4.2.b40', '4.15.b7', 'a student is writing a reflective or methodological section',
    "'How has the way you read changed since you started the course?'")
k16(5, ['develop'], 'independent and persuasive interpretations, creative work included', SK,
    "the capacity to build their own imaginative and convincing readings of literary, critical, linguistic or creative material, possibly by producing new creative work",
    "build your own imaginative and convincing readings of literary, critical, linguistic or creative material, perhaps by writing new creative work of your own",
    '4.2.b25 to 4.2.b27', '4.15.b3.1', 'a student worries their reading is not original enough',
    "'What is your reading of this text that someone else in the seminar might not have reached?'")
k16(6, ['articulate'], 'critical understanding of complex texts and their history', UN,
    "the capacity to express a critical grasp of demanding texts and ideas and of how they relate historically",
    "explain critically how demanding texts and ideas work and how they relate to each other over time",
    '4.2.b29, 4.2.b34 and 4.2.b39', '4.15.b1', 'a student is planning a period or survey essay',
    "'How does this text answer, or argue with, something written before it?'")
k16(7, ['communicate'], 'clear, accurate and effective communication in all modes', GS,
    "clear, accurate and effective communication, spoken, unspoken and written",
    "communicate clearly, accurately and effectively, whether speaking, writing or through other means",
    '4.2.b1, 4.2.b3 and 4.2.b6', '4.15.b8', 'a student asks how presentations and written work are judged',
    "'Which do you find hardest to get across clearly: spoken or written argument?'")
k16(8, ['apply'], 'scholarly research and bibliographic skills', GS,
    "the capacity to use research and bibliographic skills that suit the subject",
    "use the research and referencing skills that suit English",
    '4.2.b68 and 4.2.b70', '4.15.b5', 'a student starts a research essay or dissertation',
    "'How do you find, record and cite the critical sources for an essay?'")

# ---- outcome list 2.2 ("graduates who have studied English will know about:")
def k22(k, about, core, ben, nb, when, q):
    P['2.2.b%d' % k] = dict(
      type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates in English, by the parts of the subject studied',
      addressee='learner', verbs=[], about=about, domain=KN, award=HON,
      para=f"Will know about {core}, depending on which parts of the subject they took.",
      prac=f"Graduates will know about {core}, as far as their course covered it; map which modules supply this knowledge.",
      ben=f"Depending on the parts of English you study, you will know about {ben}.",
      aaw=(f"Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree "
           f"at FHEQ level 6 (FQHEIS level 10): {about}. Cite it as {CITE}, para 2.2, bullet {k}. Do not claim every graduate knows "
           f"the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside "
           f"{nb}, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."),
      aad=(f"Raise this when {when}. With a student, say in plain words what knowing this involves and that it depends on the modules "
           f"you choose; with staff, frame it as coverage to check in programme design. Ask: {q} Avoid reading the list aloud or "
           f"implying every student meets every item."))

k22(1, 'the expressive resources of language', "what language offers for expression", "what language gives you to express things",
    '1.6.b2 and 4.2.b82', 'a student asks what a language module adds to a literature degree',
    "'What can a writer do with sound, syntax or word choice that changes what a sentence means?'")
k22(2, 'periods and the main literary genres', "literature or language across periods and the chief genres of prose, poetry and drama",
    "literature or language across different periods and the main genres of prose, poetry and drama",
    '3.3.s1 and 4.2.sk2', 'a student is choosing optional modules across periods',
    "'Which period or genre have you studied least so far?'")
k22(3, 'the range of literatures in English', "how wide the body of literature written in English is",
    "how wide the range of literature written in English is", '3.3 and 1.15', 'a student asks about world or postcolonial literature options',
    "'Which literatures in English from outside Britain have you read?'")
k22(4, 'regional and global varieties of English', "the varieties of English spoken and written in regions and around the world",
    "the varieties of English used in different regions and around the world", '3.2 and 4.2.sk1',
    'a student asks what Global Englishes or dialect study covers', "'Which variety of English do you speak, and how does it differ from another you know?'")
k22(5, 'how English is built and used', "the history, structure, levels and discourse uses of English",
    "the history and structure of English, its levels of analysis and how it works in discourse", '3.2 and 4.2.sk1',
    'a student starts a language or linguistics strand', "'Can you name the levels at which a linguist analyses a sentence?'")
k22(6, 'how texts are made and received', "the ways culture, language, technology and economics shape how, where and by whom texts are made and taken up",
    "how culture, language, technology and money shape how, where and by whom texts are made and read", '3.3 and 4.2.sk2',
    'a student studies book history, publishing or media', "'Who could afford to read this text when it first appeared, and how did it reach them?'")
k22(7, 'readers and audiences shaping texts', "the part readers and audiences play in shaping texts",
    "the part readers and audiences play in shaping texts", '4.2.b52 and 4.2.b11', 'a student asks about reader-response or reception',
    "'How might a reader today take this text differently from its first audience?'")
k22(8, 'relations between genres and media', "how genres and media relate to one another",
    "how different genres and media relate to each other", '3.3 and 4.2.b82', 'a student works on adaptation or multimodal texts',
    "'What changes when this story moves from page to screen?'")
k22(9, 'critical, theoretical, linguistic and stylistic terms', "the concepts and terms of criticism, theory, linguistics and stylistics",
    "the concepts and vocabulary of criticism, theory, linguistics and stylistics", '4.2.sk1 to 4.2.sk3',
    'a student is unsure which terms to use in analysis', "'Which technical term would sharpen the point you are making here?'")

# ---- obliging or outcome paragraphs in sections 2 and 3
P['2.4'] = dict(
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on an English honours degree', addressee='learner',
  verbs=['progress', 'builds', 'include'], about='progression towards the threshold across the degree', domain='none', award=HON,
  find="Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10), a student of English will progress from one level of study to the next, in line with the regulations and processes for each provider. At each level, the attainment of knowledge, expertise and experience builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.",
  para="Across an honours degree (FHEQ Level 6; FQHEIS Level 10) an English student will move up through the levels under the provider's rules, each level building towards the threshold skills, usually by completing and gaining credit for all learning and assessment.",
  prac="Plan each level so it builds towards the threshold standards in 4.2, and make sure progression rules require students to complete and gain credit for every part of the course, practical work included.",
  ben="As you move through each year of your honours degree, what you learn builds towards the minimum standard for graduating, and you will usually need to pass and gain credit for everything you are assessed on.",
  aaw=(f"Describe this as a 'will' expectation about progression through the honours degree, stated at FHEQ Level 6 and FQHEIS Level 10. "
       f"Cite it as {CITE}, para 2.4. Do not claim it sets credit rules, which belong to each provider, or that a second-class degree "
       f"guarantees postgraduate entry. Set it beside 4.1, the threshold column of 4.2 and qaa/fheq-2024/4.15.i1 with spine:6."),
  aad=("Raise this when a student or a programme team asks how earlier years relate to the final standard. With a student, explain in "
       "plain second-person words that each year builds towards the minimum for graduating; with staff, frame it as level design and "
       "progression rules. Ask: 'Which skills from the final-year minimum does this first-year module start to build?' Avoid suggesting "
       "the statement sets credit or progression regulations."))
P['2.5'] = dict(
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on combined, joint or major-minor routes with English',
  addressee='learner', verbs=['achieve', 'add'], about='outcomes on joint and combined routes', domain='none', award=HON,
  find="Undergraduates studying a combined, joint or major-minor route will achieve learning outcomes relating to English, and will add more according to their other subjects.",
  para="Students on combined, joint or major-minor routes will meet outcomes in English and will gain further ones from their other subjects.",
  prac="On joint and combined routes, set outcomes in English and let the partner subject add its own; make clear which ones the English part carries.",
  ben="If you take English with another subject, you will meet outcomes in English and gain more from your other subject.",
  aaw=(f"Describe this as a 'will' expectation for joint, combined and major-minor honours routes at FHEQ level 6 (FQHEIS level 10): such "
       f"students meet English outcomes and add others from their second subject. Cite it as {CITE}, para 2.5. Do not claim joint "
       f"students must meet every single-honours outcome in full; the standards table speaks of English as a significant component. "
       f"Set it beside 1.1, the 4.2 lead-ins and spine:6."),
  aad=("Raise this when a joint-honours student or a programme team asks which English outcomes apply. With a student, say plainly that you "
       "meet English outcomes and others from your second subject; with staff, frame it as dividing outcomes between the two subjects. "
       "Ask: 'Which of your outcomes come from English and which from your other subject?' Avoid implying a joint student needs every "
       "single-honours item."))
P['2.10'] = dict(
  type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  find="Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.",
  para="Providers will bring in external reviewers during periodic review, for an outside view on proposed changes and to confirm that threshold standards are met and the content suits the subject.",
  prac="Include external reviewers in periodic review of English courses, asking them to comment on planned changes, on whether threshold standards are met and on whether content suits the subject.",
  ben=('n/a', 'a provider duty in course review; nothing for the student to do'),
  aaw=(f"Treat this as a 'will' expectation on the provider, not a student outcome: external reviewers take part in periodic review. Cite it "
       f"as {CITE}, para 2.10. Do not claim it is a regulatory requirement or describe it as something students meet. Set it beside "
       f"2.9 and 2.11 on review and external examining, and beside the threshold column of 4.2."),
  aad=("Raise this with a programme team preparing for periodic review. Put it in practitioner terms: who the external reviewers are and "
       "what they will be asked to judge. Ask: 'What evidence will show a reviewer that threshold standards are met?' Avoid raising it with "
       "students as if it were their task."))
P['3.3.s1'] = dict(
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='single honours English Literature students', addressee='learner',
  verbs=['encounter', 'gain'], about='pre-1800 texts in single honours English Literature', domain=KN, award=HON,
  find="Single honours English Literature students will normally encounter texts from before 1800, and may gain knowledge of literature from one or more early periods (Medieval and Renaissance periods, 17th and 18th centuries), as may some students on joint degrees.",
  para="Students on single honours English Literature will normally meet texts written before 1800 and may come to know one or more early periods; some joint students may too.",
  prac="In a single honours English Literature course, normally include texts from before 1800, with the chance to study one or more early periods in depth.",
  ben="On a single honours English Literature course you will normally read texts from before 1800, and you may study one or more early periods in depth.",
  aaw=(f"Describe this as a 'will normally' expectation for single honours English Literature at FHEQ level 6 (FQHEIS level 10): students read "
       f"texts from before 1800, and may study early periods. Cite it as {CITE}, para 3.3. Do not extend it to joint or language degrees as a "
       f"rule, and keep the hedge 'normally'. Set it beside 4.2.sk2 (pre-1800 awareness for single honours), 2.2.b2 and qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a student or a team plans module choices across periods. With a student, say plainly that a single honours "
       "literature course will normally include older texts; with staff, frame it as coverage to check. Ask: 'Which texts from before 1800 "
       "have you studied, and which period would you like to know better?' Avoid presenting it as binding on every English course."))
P['4.2'] = dict(
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['determining', 'refer'], about='judging achievement above threshold with Annex D', domain='none', award=HON,
  find="Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees.",
  para="Each provider decides how to evidence achievement above the threshold and should use Annex D, which describes the degree classes for honours at FHEQ Level 6 and FQHEIS Level 10.",
  prac="When setting how marks above the threshold are evidenced and classified, consult Annex D's descriptions of the classes for honours degrees.",
  ben=('n/a', 'a provider duty on how classifications are judged'),
  aaw=(f"Treat this as a 'should' on the provider: it sets its own method for evidencing achievement above the threshold and should refer to "
       f"Annex D. Cite it as {CITE}, para 4.2. Do not claim the statement itself defines the degree classes or that this binds the "
       f"student. Set it beside std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st) and 4.1."),
  aad=("Raise this with a programme team or examiners when they align marking criteria with degree classes. Frame it for staff as using "
       "Annex D beside the typical and excellent columns. Ask: 'Which Annex D band does this typical-column item most resemble?' Avoid "
       "giving it to students as a task of theirs."))

# ---- the 4.2 table: threshold, typical and excellent columns
R = {
 'threshold': dict(force='threshold', ff=LEAD_T,
   para=lambda c: f"Will have shown, as the minimum for the honours degree, {c}.",
   prac=lambda c: f"At threshold, every honours graduate in English will have shown {c}; check that each passing student can evidence it.",
   ben=lambda b: f"As a minimum for your honours degree, you will {b}.",
   aaw=lambda d: (f"Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 "
        f"(FQHEIS level 10): {d['about']}. Cite it as {CITE}, para 4.2, standards table, threshold column, {d['row']} row. Do not present "
        f"it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside "
        f"{d['nb']}, qaa/fheq-2024/{d['fw']}, qaa/fqheis-2024/{fq(d['fw'])} and spine:6."),
   aad=lambda d: (f"Raise this when {d['when']}. With a student, say plainly in the second person that this is the floor for the honours "
        f"degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: {d['q']} Avoid reading "
        f"the table aloud or treating this minimum as the target.")),
 'typical': dict(force='will', ff=LEAD_TY,
   para=lambda c: f"Are able to show, at the typical level reached by most honours graduates, {c}.",
   prac=lambda c: f"At the typical level, most honours graduates in English show {c}; design teaching so that the main cluster of students reaches it.",
   ben=lambda b: f"At the level most students reach by the end of the degree, you are able to {b}.",
   aaw=lambda d: (f"Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to "
        f"do at FHEQ level 6 (FQHEIS level 10), above the threshold: {d['about']}. Cite it as {CITE}, para 4.2, standards table, typical "
        f"column, {d['row']} row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. "
        f"Set it beside {d['nb']}, qaa/fheq-2024/{d['fw']} and Annex D's upper second description qaa/fheq-2024/annex-d/{d['ad']}/2.1."),
   aad=lambda d: (f"Raise this when {d['when']}. With a student, put it plainly in the second person as what most people show by the end "
        f"of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: {d['q']} "
        f"Avoid presenting it as the pass mark or reading the table aloud.")),
 'excellent': dict(force='will', ff=LEAD_EX,
   para=lambda c: f"Are able to show, at the excellent level for the honours degree, {c}.",
   prac=lambda c: f"At the excellent level, the strongest honours graduates in English show {c}; treat it as evidence for the top band, not a requirement.",
   ben=lambda b: f"If you reach the excellent level, you are able to {b}.",
   aaw=lambda d: (f"Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 "
        f"(FQHEIS level 10), well above the threshold: {d['about']}. Cite it as {CITE}, para 4.2, standards table, excellent column, "
        f"{d['row']} row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside {d['nb']}, "
        f"qaa/fheq-2024/{d['fw']} and Annex D's first-class description qaa/fheq-2024/annex-d/{d['ad']}/1st."),
   aad=lambda d: (f"Raise this when {d['when']}. With a student, put it plainly as a mark of the best work, something to stretch towards "
        f"rather than a requirement; with staff, frame it as evidence for the top band. Ask: {d['q']} Avoid presenting it as the minimum "
        f"or as a checklist every student must complete.")),
}

def kr(rung, k, row, verbs, about, domain, core, ben, nb, fw, ad, when, q, find=None, appliesTo=None):
    t = R[rung]
    d = dict(about=about, row=row, nb=nb, fw=fw, ad=ad, when=when, q=q)
    r = dict(type=rung, rung=rung, force=t['force'], forceFrom=t['ff'], level='fheq:6',
             appliesTo=appliesTo or 'graduates who studied English as a significant component of their degree, at the %s level' % rung,
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON,
             para=t['para'](core), prac=t['prac'](core), ben=t['ben'](ben), aaw=t['aaw'](d), aad=t['aad'](d))
    if find:
        r['find'] = find
    P['4.2.b%d' % k] = r

T, TY, EX = 'threshold', 'typical', 'excellent'
COM, AFF, DIG, COL = 'communication (generic skills)', 'affective power of language (generic skills)', 'digital (generic skills)', 'collaboration (generic skills)'
CRE, CRT, EVI = 'creativity (generic skills)', 'critical thinking (generic skills)', 'evidence (generic skills)'
CLO, PLU = 'close reading (subject knowledge)', 'interpretation (subject knowledge)'
TSK, PER, INT, FBK, ENT = ('assessment tasks and time (embedded understanding)', 'perspectives (embedded understanding)',
                           'integrity and citation (embedded understanding)', 'feedback (embedded understanding)', 'enterprise and values (embedded understanding)')
CW = 'creative writing'
CWA = 'graduates who studied Creative Writing as a significant component of their degree, at the %s level'

# communication row
kr(T, 1, COM, ['communicate', 'structuring', 'using'], 'clear communication and lucid argument for an audience', GS,
   "the capacity to get ideas across clearly in speech, other modes and writing, building lucid arguments in a style that suits the audience",
   "get your ideas across clearly in speech, writing and other forms, building lucid arguments in a style that suits your audience",
   '4.2.b3, 4.2.b6 and 1.6.b7', '4.15.b8', 'transferable/r1', 'a student asks what counts as a clear argument at pass level',
   "'Who is the reader of this essay, and what do they need first to follow your case?'")
kr(T, 2, COM, ['understand'], 'writing as a process of revision and editing', GS,
   "an understanding that good writing comes through revising and editing",
   "understand that good writing comes through revising and editing your drafts",
   '4.2.b5, 4.2.b9 and 3.12.b10', '4.15.b8', 'transferable/r5', 'a student submits first drafts unrevised',
   "'What did you change between your first draft and the version you handed in?'")
kr(TY, 3, COM, ['communicate', 'structuring', 'using', 'incorporating'], 'coherent, rigorous argument that draws in other views', GS,
   "clear communication in every mode, with lucid, coherent and rigorous arguments, persuasive expression and other writers' arguments built in",
   "communicate clearly in every mode, building coherent and rigorous arguments, writing persuasively and drawing other writers' arguments into your own",
   '4.2.b1 and 4.2.b6', '4.15.b8', 'transferable/r1', 'a student wants to move from a pass to a good essay',
   "'Where in this essay do you bring in a critic's argument, and what does it do for your own?'")
kr(TY, 4, COM, ['position'], "taking a clear stance among others' arguments", GS,
   "a clear stance of their own in relation to the arguments of others, pitched for the audience",
   "take a clear position in relation to other people's arguments, pitched for your audience",
   '4.2.b7 and 4.2.b3', '4.15.b7', 'cognitive/r2', 'a student summarises critics without a view of their own',
   "'Where do you stand in relation to the critics you quote, and how would a reader know?'")
kr(TY, 5, COM, ['deploy', 'deploys', 'improve'], 'reflective revision from draft to draft', GS,
   "a reflective way of writing that uses revision to make each draft better than the last",
   "reflect on how you write and use revision to make each draft better than the last",
   '4.2.b2 and 4.2.b9', '4.15.b8', 'transferable/r5', 'a student asks how to use feedback on a draft',
   "'What did revision change in your argument, not just your sentences?'")
kr(EX, 6, COM, ['communicate', 'structuring'], 'incisive argument for complex, cogent central claims', GS,
   "clear communication in every mode, including lucid, rigorous and incisive arguments that support complex, demanding and well-expressed central claims",
   "communicate clearly in every mode, building incisive, rigorous arguments for complex and demanding central claims",
   '4.2.b3 and 4.2.b1', '4.15.b8', 'transferable/r1', 'a student aims for a first-class essay',
   "'Can you state your central claim in one sentence, and is it one a reader could dispute?'")
kr(EX, 7, COM, ['identify', 'articulate'], "concise, accurate assessment of other writers' arguments", GS,
   "the capacity to name the strengths and weaknesses of other writers' arguments briefly and accurately",
   "name the strengths and weaknesses of other writers' arguments briefly and accurately",
   '4.2.b4 and 4.2.b37', '4.15.b7', 'cognitive/r2', 'a student is writing a critical review or literature survey',
   "'What is the strongest point in this critic's argument, and where does it give way?'")
kr(EX, 8, COM, ['amend', 'develop'], 'revising positions in light of new evidence', GS,
   "the capacity to change and extend their positions when new evidence and claims appear (the item continues after a page break)",
   "change and extend your position when new evidence or claims come to light",
   '4.2.b4 and 4.2.b46', '4.15.b4', 'cognitive/r2', 'a student meets evidence that cuts against their thesis',
   "'What would make you change your mind about this argument?'")
kr(EX, 9, COM, ['deploy'], 'disciplined writing habits and re-reading before submission', GS,
   "a disciplined commitment to their own writing, rereading their prose carefully before handing it in",
   "commit to your own writing with discipline, rereading your prose carefully before you hand it in",
   '4.2.b5 and 4.2.b60', '4.15.b9.1', 'transferable/r3', 'a student loses marks to avoidable slips',
   "'How many times do you read a piece through before you submit it, and what do you look for?'")

# affective power of language row
kr(T, 10, AFF, ['recognise', 'manipulate', 'persuade'], 'the affective power of language', SK,
   "a recognition that language carries emotional force and can manipulate as well as persuade",
   "recognise that language has emotional force and can manipulate people as well as persuade them",
   '4.2.b12, 4.2.b13 and 1.6.b3', '4.15.b7', 'cognitive/r2', 'a student analyses political speech or advertising',
   "'Where does this text try to make you feel something rather than think something?'")
kr(T, 11, AFF, ['temper'], 'implied audiences and writing for an audience', SK,
   "awareness of the audiences texts imply and of the need to adjust their own writing to particular readers",
   "notice the audiences that texts imply, and adjust your own writing to the particular readers you have",
   '4.2.b12 and 4.2.b13', '4.15.b8', 'transferable/r1', 'a student writes in one register for every task',
   "'Who is this text written for, and who are you writing for in your reply?'")
kr(TY, 12, AFF, ['recognise', 'respond', 'using', 'communicate'], 'responding to affective language and writing for different audiences', SK,
   "recognition of and response to the emotional force of language, with fitting methods and terms, and clear, coherent communication to varied audiences",
   "recognise and respond to the emotional force of language with suitable methods and terms, and communicate clearly to different audiences",
   '4.2.b10, 4.2.b11 and 4.2.b13', '4.15.b7', 'cognitive/r2', 'a student moves from noticing effects to analysing them',
   "'What technique produces the effect you noticed, and how would you name it?'")
kr(EX, 13, AFF, ['analyse', 'using'], 'analysing affective language for defined audiences', SK,
   "analysis of the emotional force of language, using methods and terms suited to specific, defined audiences",
   "analyse the emotional force of language, using methods and terms suited to specific, defined audiences",
   '4.2.b12 and 4.2.b14', '4.15.b7', 'cognitive/r2', 'a student writes a sophisticated stylistic or rhetorical analysis',
   "'How would your analysis change if you were writing it for a specialist journal rather than a general reader?'")
kr(EX, 14, AFF, ['have', 'enables', 'persuade', 'move'], 'command of rhetoric; handling sensitive material', SK,
   "a command of rhetoric that lets them persuade and at times move their readers, with deftness in handling sensitive topics and difficult material",
   "use rhetoric well enough to persuade and sometimes move your readers, and handle sensitive topics and difficult material with skill",
   '4.2.b13 and 4.2.b12', '4.15.b8', 'transferable/r1', 'a student writes on a painful or contested subject',
   "'How do you write about this difficult material in a way that respects your readers?'")

# digital row
kr(T, 15, DIG, ['use'], 'comfort with technology and digital platforms', GS,
   "ease with technology and digital communication and use of a range of digital platforms",
   "be at ease with technology and digital communication and use a range of digital platforms",
   '4.2.b16 and 4.2.b17', '4.15.b8', 'practical/r1', 'a student is asked to produce a blog, podcast or digital edition',
   "'Which digital tools have you used to present your work so far?'")
kr(TY, 16, DIG, ['use'], 'confident use of digital platforms', GS,
   "ease with technology and digital communication and confident use of a range of digital platforms",
   "be at ease with technology and use a range of digital platforms with confidence",
   '4.2.b15 and 4.2.b17', '4.15.b8', 'practical/r1', 'a student plans a digital or multimodal assessment',
   "'Which platform suits this piece best, and why?'")
kr(EX, 17, DIG, ['deploy', 'exploit'], 'inventive use of new technologies to communicate', GS,
   "use of several digital platforms, possibly with inventive use of new technologies to communicate their work",
   "use several digital platforms and, where it helps, put new technologies to inventive use in sharing your work",
   '4.2.b16 and 1.21', '4.15.b8', 'practical/r1', 'a student wants to experiment with form or medium',
   "'What could a new tool let you do with this work that print cannot?'")

# collaboration row
kr(T, 18, COL, ['collaborate', 'work'], 'collaboration and independent work with self-management', GS,
   "the capacity to work with others and on their own, showing autonomy, adaptability, resilience and self-management",
   "work both with others and on your own, showing independence, adaptability, resilience and self-management",
   '4.2.b20, 4.2.b21 and 1.5.b2', '4.15.b9.1', 'transferable/r3', 'a student starts a group project',
   "'When did you last have to manage your own work without anyone checking on it?'")
kr(T, 19, COL, ['develop'], 'working relationships in teams', GS,
   "the capacity to build working relationships with others in a team",
   "build working relationships with other people in a team",
   '4.2.b20 and 4.2.b22', '4.15.b9.1', 'transferable/r2', 'a student finds group work difficult',
   "'What helped, or got in the way of, working well with your last group?'")
kr(TY, 20, COL, ['collaborate', 'work', 'demonstrate', 'adopt'], 'teamwork skills and roles within a group', GS,
   "collaboration and independent work with autonomy, adaptability, resilience and self-management, the core skills of teamwork such as listening and answering questions constructively; and the taking of set tasks and roles in a group",
   "work with others and on your own with independence and resilience, use core teamwork skills such as listening and answering questions constructively; and take on set tasks and roles in a group",
   '4.2.b18, 4.2.b19 and 4.2.b22', '4.15.b9.1', 'transferable/r2', 'a group is dividing up roles for a project',
   "'Which role did you take in your last group, and which would you take next time?'")
kr(EX, 21, COL, ['collaborate', 'work'], 'collaboration and independence at the excellent level', GS,
   "work with others and on their own, showing autonomy, adaptability, resilience and self-management (the same wording as the threshold item)",
   "work both with others and on your own, showing independence, adaptability, resilience and self-management",
   '4.2.b18 and 4.2.b20', '4.15.b9.1', 'transferable/r3', 'a strong student asks what more group work can show',
   "'How did you balance leading your own part with supporting the group's whole?'")
kr(EX, 22, COL, ['listen', 'ask', 'respond'], 'skilled participation in teamwork', GS,
   "skilled teamwork: listening, asking searching questions and answering even critical questions constructively",
   "take a skilled part in teamwork: listen to others, ask searching questions and answer even critical ones constructively",
   '4.2.b20 and 4.2.b24', '4.15.b9.1', 'transferable/r2', 'a student meets sharp questions in a seminar or group',
   "'How do you answer a question that challenges your idea in front of others?'")
kr(EX, 23, COL, ['encompassing'], 'holding many perspectives and ideologies', GS,
   "skill in taking in a broad range of viewpoints, attitudes, ethics and ideologies",
   "take in a broad range of viewpoints, attitudes, ethics and ideologies with skill",
   '4.2.b62 and 4.2.b64', '4.15.b4', 'cognitive/r1', 'a group holds very different views on a text or issue',
   "'Which view in your group was furthest from yours, and what did you learn from it?'")
kr(EX, 24, COL, ['arrive'], "being central to a group's success, through leadership or negotiation", GS,
   "frequent importance to their group's success, either by leading openly or through skills such as negotiating disagreement to reach agreement",
   "often be key to your group's success, by leading openly or by skills such as negotiating disagreement until the group agrees",
   '4.2.b20 and 4.2.b43', '4.15.b9.2', 'transferable/r2', 'a group stalls over a disagreement',
   "'How did your group reach agreement the last time it disagreed?'")

# creativity row (generic skills, page 15)
kr(T, 25, CRE, ['develop'], 'creativity and interpretation of material', SK,
   "creativity, developing readings of literary, critical, linguistic or creative material in their interpretation and writing",
   "be creative and develop your own readings of literary, critical, linguistic or creative material in how you interpret and write",
   '4.2.b26, 4.2.b27 and 1.6.b5', '4.15.b3.1', 'cognitive/r4', 'a student asks how creativity is judged in a critical essay',
   "'What is creative about the reading you are proposing?'")
kr(TY, 26, CRE, ['develop', 'showing'], 'independent, imaginative interpretation', SK,
   "creativity, with independent and imaginative readings of literary, critical, linguistic or creative material and an independent approach in their interpretation and writing",
   "be creative, developing independent and imaginative readings of literary, critical, linguistic or creative material, with your own approach to interpretation and writing",
   '4.2.b25 and 4.2.b27', '4.15.b3.1', 'cognitive/r4', 'a student relies heavily on lecture readings',
   "'Which part of this reading is yours rather than the lecturer's?'")
kr(EX, 27, CRE, ['develop', 'showing'], 'original, independent interpretation', SK,
   "creativity, with independent and imaginative readings of literary, critical, linguistic or creative material that show originality as well as independence in interpretation and writing",
   "be creative, developing independent and imaginative readings of literary, critical, linguistic or creative material that are original as well as your own",
   '4.2.b26 and 4.2.b84', '4.15.b3.1', 'cognitive/r4', 'a student aims for originality in a dissertation',
   "'What would a reader learn from your reading that they could not find elsewhere?'")

# critical thinking row
kr(T, 28, CRT, ['think', 'display'], 'critical thinking: understanding, analysis and interpretation', GS,
   "critical thought, with the capacity to understand, analyse and interpret",
   "think critically and show that you can understand, analyse and interpret",
   '4.2.b33 and 1.5.b4', '4.15.b7', 'cognitive/r2', 'a student asks what critical means in feedback',
   "'What question does your essay ask of the text, rather than about it?'")
kr(T, 29, CRT, ['articulate'], 'critical understanding of complex texts and their history', UN,
   "the capacity to express a critical grasp of demanding texts and ideas and of how they relate over time",
   "explain critically how demanding texts and ideas work and how they relate to each other over time",
   '4.2.b34 and 1.6.b6', '4.15.b1', 'knowledge/r1', 'a student writes a contextual or period essay',
   "'How does this text connect with what came before it?'")
kr(T, 30, CRT, ['reflect', 'evaluate'], 'reflecting on reading and writing; evaluating forms and artefacts', SK,
   "critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts",
   "reflect critically on reading and writing, and judge literary and linguistic forms and other cultural works",
   '4.2.b35 and 1.6.b4', '4.15.b7', 'transferable/r5', 'a student writes a reflective commentary',
   "'What did writing this piece teach you about how you read?'")
kr(T, 31, CRT, ['show'], 'rigour and precision with data and evidence', GS,
   "rigour and precision in using and weighing data and evidence",
   "use and weigh data and evidence with rigour and precision",
   '4.2.b36 and 3.12.b8', '4.15.b7', 'practical/r4', 'a student quotes loosely or uses evidence carelessly',
   "'Does this quotation prove the point you attach to it?'")
kr(T, 32, CRT, ['follow', 'negotiate', 'recognise'], 'following debate, negotiating disagreement, seeing ambiguity', GS,
   "the capacity to follow arguments and debates, work through disagreement and spot ambiguity",
   "follow arguments and debates, work through disagreement and notice where meaning is ambiguous",
   '4.2.b37 and 3.12.b6', '4.15.b4', 'cognitive/r2', 'a seminar debate becomes heated',
   "'Where in this debate could both sides be partly right?'")
kr(TY, 33, CRT, ['think', 'display'], 'wide powers of critical thought', GS,
   "critical thought, with wide-ranging capacity to understand, analyse and interpret",
   "think critically, with a wide-ranging capacity to understand, analyse and interpret",
   '4.2.b28 and 4.2.b38', '4.15.b7', 'cognitive/r2', 'a student moves from description to analysis',
   "'What does this analysis show that a summary would not?'")
kr(TY, 34, CRT, ['articulate'], 'advanced critical understanding of complex texts', UN,
   "the capacity to express an advanced critical grasp of demanding texts and ideas and of how they relate over time",
   "explain with advanced critical understanding how demanding texts and ideas work and relate to each other over time",
   '4.2.b29 and 4.2.b39', '4.15.b1', 'knowledge/r1', 'a student works with dense theory or difficult texts',
   "'Which idea in this text took you longest to grasp, and how would you now explain it?'")
kr(TY, 35, CRT, ['reflect', 'evaluate'], 'rigorous reflection on reading and writing; evaluating forms', SK,
   "rigorous critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts",
   "reflect critically and rigorously on reading and writing, and judge literary and linguistic forms and other cultural works",
   '4.2.b30 and 4.2.b40', '4.15.b7', 'transferable/r5', 'a student evaluates form in close analysis',
   "'Why might the writer have chosen this form rather than another?'")
kr(TY, 36, CRT, ['show'], 'rigour and precision with data and evidence (typical)', GS,
   "rigour and precision in using and weighing data and evidence (the same wording as the threshold item)",
   "use and weigh data and evidence with rigour and precision",
   '4.2.b31 and 4.2.b42', '4.15.b7', 'practical/r4', 'a student builds a corpus or evidence-based argument',
   "'How did you choose your evidence, and what did you leave out?'")
kr(TY, 37, CRT, ['engage', 'negotiate', 'recognise', 'understand'], 'engaging in debate and the uses of ambiguity', GS,
   "engagement with arguments and debates, working through disagreement and understanding how ambiguity is used",
   "engage with arguments and debates, work through disagreement and understand how ambiguity can be used",
   '4.2.b32 and 4.2.b43', '4.15.b4', 'cognitive/r2', 'a student meets a deliberately ambiguous text',
   "'What does the ambiguity in this passage allow the writer to do?'")
kr(EX, 38, CRT, ['think', 'display'], 'extensive powers of critical thought', GS,
   "critical thought, with an extensive capacity to understand, analyse and interpret",
   "think critically, with an extensive capacity to understand, analyse and interpret",
   '4.2.b33 and 4.2.b28', '4.15.b7', 'cognitive/r2', 'a student aims for the top band',
   "'What does your analysis notice that most readers would miss?'")
kr(EX, 39, CRT, ['articulate'], 'sophisticated critical understanding of complex texts', UN,
   "the capacity to express a sophisticated critical grasp of demanding texts and ideas and of how they relate over time",
   "explain with sophisticated critical understanding how demanding texts and ideas work and relate to each other over time",
   '4.2.b34 and 4.2.b29', '4.15.b1', 'knowledge/r1', 'a student plans an ambitious comparative essay',
   "'How would you trace this idea across three centuries of writing?'")
kr(EX, 40, CRT, ['reflect'], 'precise, detailed reflection on reading and writing', SK,
   "critical reflection on reading and writing in exact detail",
   "reflect critically and in exact detail on reading and writing",
   '4.2.b35 and 4.2.b30', '4.15.b7', 'transferable/r5', 'a student writes a reflective or methodological chapter',
   "'Which precise moment in your reading changed your interpretation?'")
kr(EX, 41, CRT, ['evaluate'], 'evaluating forms and artefacts in wide context', SK,
   "evaluation of literary and linguistic forms and other cultural artefacts within a broad intellectual and historical setting",
   "judge literary and linguistic forms and other cultural works within a broad intellectual and historical setting",
   '4.2.b35 and 4.2.b39', '4.15.b7', 'knowledge/r1', 'a student places a text in its intellectual history',
   "'What larger intellectual debate does this form take part in?'")
kr(EX, 42, CRT, ['show'], 'rigour and precision with data and evidence (excellent)', GS,
   "rigour and precision in using and weighing data and evidence (the same wording as the lower columns)",
   "use and weigh data and evidence with rigour and precision",
   '4.2.b36 and 4.2.b46', '4.15.b7', 'practical/r4', 'a student handles complex or conflicting evidence',
   "'Where does your evidence pull against your claim, and how do you deal with it?'")
kr(EX, 43, CRT, ['engage', 'negotiate', 'understand', 'analyse', 'appreciate'], 'active debate and the value of ambiguity', GS,
   "active engagement with arguments and debates, highly effective negotiation of disagreement and an understanding, analysis and appreciation of what ambiguity does and is worth",
   "engage actively in arguments and debates, negotiate disagreement very effectively and understand, analyse and value what ambiguity does",
   '4.2.b37 and 4.2.b24', '4.15.b4', 'cognitive/r2', 'a student leads a seminar discussion',
   "'How would you help a group that disagrees reach a better question rather than a winner?'")

# evidence row
kr(T, 44, EVI, ['identify', 'gather', 'synthesise', 'organise', 'deploy'], 'gathering and using some evidence for an argument', GS,
   "the capacity to find, collect, combine, arrange and use some evidence to support an argument",
   "find, collect, combine, arrange and use some evidence to support an argument",
   '4.2.b45 and 4.2.b31', '4.15.b5', 'cognitive/r1', 'a student starts researching an essay',
   "'What evidence have you gathered so far, and which piece does the most work?'")
kr(TY, 45, EVI, ['process', 'interpret', 'situating', 'formulating', 'cite'], 'interpreting evidence and framing research questions', GS,
   "the capacity to work through and interpret the evidence they collect, set it in wider contexts and frame research questions that take their enquiry further (weaker students at this level may still cite evidence descriptively)",
   "work through and interpret the evidence you collect, set it in wider contexts and frame research questions that take your enquiry further",
   '4.2.b44 and 4.2.b46', '4.15.b7', 'cognitive/r1', 'a student plans a dissertation question',
   "'What question does your evidence raise that you have not yet asked?'")
kr(EX, 46, EVI, ['interpret', 'analyses', 'construct', 'produce', 'articulate'], 'independent analysis of evidence and well-defined enquiry', GS,
   "independent, critical interpretation and analysis of the evidence they gather, with sharply defined lines of enquiry that yield cogent, well-built arguments and firm judgements showing critical understanding of complex texts and ideas",
   "interpret and analyse the evidence you gather independently and critically, and follow sharply defined lines of enquiry to cogent, well-built arguments and firm judgements",
   '4.2.b45 and 4.2.b8', '4.15.b6', 'cognitive/r1', 'a student designs an independent research project',
   "'What is your line of enquiry, and how will you know when it has reached a judgement?'")

# subject knowledge: close reading row
kr(T, 47, CLO, ['understand'], 'the technique of close reading', SK,
   "an understanding of how close reading works",
   "understand how close reading works",
   '4.2.b48, 4.2.b49 and 1.6.b1', '4.15.b2', 'practical/r1', 'a student asks what close reading is for',
   "'Pick one line: what does it do, word by word?'")
kr(TY, 48, CLO, ['deploy', 'anchor'], 'using close reading in argument', SK,
   "use of close reading, which at the lower second may stay formulaic, descriptive and loosely tied to the argument, and at the upper second is anchored more firmly in their own case",
   "use close reading, and tie what you notice in a passage firmly into your own argument rather than describing it",
   '4.2.b47 and 4.2.b49', '4.15.b2', 'practical/r1', 'feedback says a student describes rather than analyses',
   "'How does this observation about the passage move your argument forward?'")
kr(EX, 49, CLO, ['develop'], 'incisive close reading embedded in argument', SK,
   "sharp, original observations drawn from sustained attention to passages, alert to form, device and figures of speech, linked to a reading of the whole text and woven into the argument",
   "draw sharp, original observations from sustained attention to passages, alert to form and figurative language, and weave them into your reading of the whole text",
   '4.2.b48 and 4.2.b27', '4.15.b2', 'practical/r1', 'a student aims to make close reading the engine of an essay',
   "'How does this detail change how we read the whole text?'")

# subject knowledge: interpretation row
kr(T, 50, PLU, ['show', 'understand', 'implies'], 'plurality of meaning without mere opinion', UN,
   "awareness that texts can bear several meanings and an understanding that this does not reduce interpretation to personal opinion",
   "know that a text can carry several meanings, and understand that this does not make every reading just a matter of opinion",
   '4.2.b51, 4.2.b52 and 4.2.b32', '4.15.b4', 'cognitive/r2', "a student says any reading is valid if it is their opinion",
   "'What in the text supports your reading, and what would count against it?'")
kr(TY, 51, PLU, ['show', 'evaluate'], 'evaluating competing interpretations', UN,
   "the capacity to weigh the grounds and worth of different readings",
   "weigh the grounds and worth of different readings of a text",
   '4.2.b50 and 4.2.b52', '4.15.b7', 'cognitive/r2', 'a student meets conflicting critical readings',
   "'Which of these two readings is better grounded, and why?'")
kr(EX, 52, PLU, ['recognise', 'carry'], 'richness of language; readers and texts shaping each other', UN,
   "a recognition of how rich language is and how it carries many, often ambiguous meanings, of how readers shape texts and of how texts shape readers' responses",
   "recognise how rich language is and how it carries many meanings, and how readers shape texts and texts shape readers",
   '4.2.b51 and 1.6.b2', '4.15.b4', 'knowledge/r1', 'a student explores reception or reader-response theory',
   "'How has this text shaped the way its readers respond, and how have they shaped it?'",
   find="recognise the richness of language and its ability to carry multiple and often ambiguous meanings, of the role of readers in shaping texts, and of texts in shaping the responses of readers.")

# embedded understanding: assessment tasks and time row
kr(T, 53, TSK, ['understand', 'carry'], 'carrying out varied tasks and supervised long projects', GS,
   "the capacity to understand and complete a range of assessment tasks, including starting and finishing their own long projects under supervision",
   "understand and complete a range of assessment tasks, including starting and finishing your own long project with a supervisor",
   '4.2.b55 and 3.9', '4.15.b6', 'practical/r2', 'a student begins a dissertation',
   "'What is the first milestone in your project, and when is it due?'")
kr(T, 54, TSK, ['understand', 'recognise', 'delivering'], 'planning time for deadlines', GS,
   "an understanding that time must be planned to meet several deadlines and that meeting them is wise, though they may not always manage it",
   "understand that you need to plan your time to meet several deadlines and that meeting them matters, even if you do not always manage it",
   '4.2.b57 and 4.2.b60', '4.15.b9.1', 'transferable/r3', 'a student has bunched deadlines',
   "'Which deadline is most at risk this month, and what will you do about it?'")
kr(TY, 55, TSK, ['adapt'], 'adapting to different demands and tasks', GS,
   "quick adaptation to differing demands and tasks",
   "adapt quickly to different demands and tasks",
   '4.2.b53 and 4.2.b58', '4.15.b9.2', 'transferable/r4', 'a student faces an unfamiliar form of assessment',
   "'What is new about this task, and what from earlier work can you carry over?'")
kr(TY, 56, TSK, ['take', 'seeking'], 'owning work and seeking help early', GS,
   "responsibility for their own work and readiness to seek help when they need it",
   "take responsibility for your own work and ask for help early when you need it",
   '4.2.b59 and 4.2.b54', '4.15.b9.1', 'transferable/r3', 'a student is struggling but has not asked for help',
   "'Who could you ask about this, and what is stopping you?'")
kr(TY, 57, TSK, ['plan', 'deliver'], 'planning time to meet set deadlines', GS,
   "planning of their time so that work arrives by several set deadlines",
   "plan your time so that your work arrives by each of several set deadlines",
   '4.2.b54 and 4.2.b60', '4.15.b9.1', 'transferable/r3', 'a student plans a term with several submissions',
   "'What does your plan for the next four weeks look like?'")
kr(EX, 58, TSK, ['respond'], 'creative, independent response to assessment', GS,
   "creative and independent responses to assessment tasks",
   "respond creatively and independently to assessment tasks",
   '4.2.b55 and 4.2.b27', '4.15.b9.2', 'transferable/r4', 'a student wants to take a risk with an assignment',
   "'What would a bolder answer to this task look like?'")
kr(EX, 59, TSK, ['seeking'], 'proactive help-seeking', GS,
   "a proactive approach to asking for help when needed",
   "ask for help proactively when you need it",
   '4.2.b56 and 4.2.b76', '4.15.b5', 'transferable/r3', 'a strong student hesitates to use support',
   "'Which kind of help would most improve your best work?'")
kr(EX, 60, TSK, ['manage', 'juggling', 'meet', 'leaving', 'revise'], 'efficient time management with time to revise', GS,
   "efficient management of time, balancing competing demands to meet deadlines and leaving room to revise and proofread before submission",
   "manage your time well, balancing competing demands to meet deadlines and leaving room to revise and proofread before you submit",
   '4.2.b57 and 4.2.b9', '4.15.b9.1', 'transferable/r3', 'a student finishes work the night before',
   "'When would you need to finish a draft to leave a day for proofreading?'")

# embedded understanding: perspectives row
kr(T, 61, PER, ['recognise', 'listening', 'meet'], 'awareness of multiple perspectives and the value of listening', GS,
   "awareness that many perspectives exist, past and present, local and global, and recognition that listening to other views matters, whether in class or in texts",
   "know that many perspectives exist, past and present, local and global, and see why listening to other views matters, in class and in what you read",
   '4.2.b62 and 1.8', '4.15.b4', 'cognitive/r1', 'a discussion touches on cultural difference or contested history',
   "'Whose perspective is missing from this text or this discussion?'")
kr(TY, 62, PER, ['listen', 'disagree'], 'listening to views one disagrees with', GS,
   "a willingness to listen to other perspectives, including ones they may disagree with",
   "listen to other perspectives, including ones you disagree with",
   '4.2.b61 and 4.2.b64', '4.15.b7', 'cognitive/r1', 'a student dismisses a view without hearing it',
   "'Can you put the opposing view in a way its holder would accept?'")
kr(TY, 63, PER, ['articulate', 'position'], 'stating views fairly and placing one\'s own among them', GS,
   "the capacity to state those other perspectives fairly and to place their own views within a range of positions",
   "state other people's perspectives fairly and place your own views within the range of positions",
   '4.2.b65 and 4.2.b4', '4.15.b7', 'cognitive/r1', 'a student writes an argument on a contested question',
   "'Where does your view sit among the others you have described?'")
kr(EX, 64, PER, ['working'], 'cultural sensitivity in working with others', GS,
   "sensitivity to cultural contexts and to shared and differing backgrounds when working with others",
   "be sensitive to cultural contexts and to the backgrounds you share or do not share with others when you work together",
   '4.2.b62 and 4.2.b23', '4.15.b9.1', 'transferable/r2', 'a mixed group works together on a project',
   "'What did you need to learn about your groupmates' backgrounds to work well together?'")
kr(EX, 65, PER, ['articulate', 'position'], 'placing one\'s own views precisely among others', GS,
   "the capacity to state other perspectives fairly and place their own views exactly within a range of positions",
   "state other people's perspectives fairly and place your own views exactly within the range of positions",
   '4.2.b63 and 4.2.b7', '4.15.b7', 'cognitive/r1', 'a student refines a nuanced argument',
   "'Exactly how does your position differ from the nearest one to it?'")

# embedded understanding: integrity and citation row
kr(T, 66, INT, ['show'], 'awareness of academic integrity, including use of large language models', GS,
   "awareness that academic integrity and ethical care are needed when using other people's writing and research, including large language models as writing aids, though their references may sometimes be inaccurate",
   "know that you must act with academic integrity and ethical care when using other people's writing and research, including AI language tools, even if your references are sometimes inaccurate",
   '4.2.b67 and 4.2.b68', '4.15.b5', 'transferable/r4', 'a student asks whether they may use an AI writing tool',
   "'How would you show a reader which parts of this work came from you and which from a tool or a source?'")
kr(TY, 67, INT, ['show'], 'academic integrity, including use of large language models', GS,
   "academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included",
   "act with academic integrity and ethical responsibility when using other people's writing and research, including AI language tools that help you write",
   '4.2.b66 and 4.2.b69', '4.15.b5', 'transferable/r4', 'a student uses AI tools in drafting',
   "'What would you write in a note explaining how you used an AI tool on this essay?'")
kr(TY, 68, INT, ['offer'], 'clear bibliographies and accurate citation', GS,
   "clear and complete bibliographies and accurate citation of others' work",
   "give clear, complete bibliographies and cite other people's work accurately",
   '4.2.b70 and 1.6.b8', '4.15.b5', 'practical/r2', 'a student loses marks on referencing',
   "'Could a reader find every source you cite from your bibliography alone?'")
kr(EX, 69, INT, ['show'], 'academic integrity at the excellent level, including large language models', GS,
   "academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included (the same wording as the typical item)",
   "act with academic integrity and ethical responsibility when using other people's writing and research, including AI language tools that help you write",
   '4.2.b67 and 4.2.b70', '4.15.b5', 'transferable/r4', 'a strong student weighs the ethics of AI in research',
   "'Where would using a language model help your research, and where would it weaken your integrity?'")
kr(EX, 70, INT, ['construct'], 'consistent, accurate referencing throughout', GS,
   "clear, complete bibliographies with consistent, accurate citation and referencing from start to finish",
   "build clear, complete bibliographies and cite and reference consistently and accurately throughout",
   '4.2.b68 and 4.2.b9', '4.15.b5', 'practical/r2', 'a student prepares a dissertation for submission',
   "'Is every reference in the same style and checked against its source?'")

# embedded understanding: feedback row
kr(T, 71, FBK, ['paying', 'address'], 'seeing the value of feedback', GS,
   "awareness that attending to feedback from staff or peers pays off, though they may need prompting to act on it",
   "see the value of paying attention to feedback from staff or classmates, even if you sometimes need a nudge to act on it",
   '4.2.b73 and 4.2.b75', '4.15.b9.3', 'transferable/r5', 'a student has not read their feedback',
   "'What was the main point in your last feedback, and what have you done with it?'")
kr(T, 72, FBK, ['need', 'enable', 'offer'], 'needing structure to give peer feedback', GS,
   "a possible need for structure before they can give feedback to peers",
   "may need some structure to help you give feedback to your classmates",
   '4.2.b74 and 4.2.b71', '4.15.b8', 'transferable/r2', 'a workshop asks students to comment on each other\'s drafts',
   "'What one question could you ask about a classmate's draft that would help them most?'")
kr(TY, 73, FBK, ['pay', 'address', 'seek'], 'attending to feedback from staff and peers', GS,
   "attention to feedback from staff and peers (the issuer adds that weaker students may need prompting and stronger ones tend to seek it out)",
   "pay attention to feedback from staff and classmates, and seek it out where you can",
   '4.2.b71 and 4.2.b75', '4.15.b9.3', 'transferable/r5', 'a student wants to improve between assignments',
   "'Which piece of feedback have you acted on most, and what changed?'")
kr(TY, 74, FBK, ['offer'], 'constructive suggestions to peers', GS,
   "constructive and supportive suggestions for their peers",
   "give your classmates constructive and supportive suggestions",
   '4.2.b72 and 4.2.b22', '4.15.b8', 'transferable/r2', 'a student takes part in peer review',
   "'How could you phrase that criticism so it helps the writer revise?'")
kr(EX, 75, FBK, ['engage', 'receive', 'using', 'reflect'], 'close, consistent use of feedback to reflect', GS,
   "close and steady engagement with feedback from staff and peers, using it to reflect on their own practice and assumptions",
   "engage closely and steadily with feedback from staff and classmates, and use it to reflect on your own practice and assumptions",
   '4.2.b73 and 4.2.b76', '4.15.b9.3', 'transferable/r5', 'a strong student wants to keep improving',
   "'What assumption of yours did your last feedback challenge?'")
kr(EX, 76, FBK, ['seek', 'use', 'improve'], 'seeking feedback to improve communication', GS,
   "active seeking of feedback and its use to improve their written and spoken communication",
   "actively seek feedback and use it to improve your written and spoken communication",
   '4.2.b75 and 4.2.b59', '4.15.b9.3', 'transferable/r3', 'a student is preparing an important presentation or submission',
   "'Who could you ask for feedback before you submit, and what would you ask them?'")

# embedded understanding: enterprise and values row (two items; read as the threshold cell, see Part E)
kr(T, 77, ENT, ['understand', 'transfer'], 'transferring core skills to employment and entrepreneurship', GS,
   "an understanding of how to carry communication, collaboration, creativity and critical thinking, with experience of research questions, self-directed study and work alone and with others, into employment and social and commercial entrepreneurship, with the skill to do so effectively",
   "understand how to carry your communication, collaboration, creativity and critical thinking, together with what you learned from research and from working alone and in groups, into jobs and social or commercial ventures",
   '1.18, 1.22 and 4.2.b20', '4.15.b9.1', 'transferable/r4', 'a student asks how an English degree leads to work',
   "'Which skill from your degree would you describe first to an employer, and with what example?'")
kr(T, 78, ENT, ['learned', 'act'], 'acting with integrity and an understanding of values', GS,
   "the habit of acting with integrity and with an understanding of their own values and those of others",
   "act with integrity and with an understanding of your own values and other people's",
   '1.20 and 4.2.b67', '4.15.b9.2', 'transferable/r4', 'a student faces an ethical choice in a group or placement',
   "'Which of your values guided that decision, and whose values did it affect?'")

# creative writing rows (lead-in: graduates who studied Creative Writing as a significant component)
kr(T, 79, CW, ['generate', 'develop'], 'generating creative work and developing it by revision', SK,
   "the capacity to produce creative work and improve it through editing and revision",
   "produce creative work and improve it through editing and revision",
   '4.2.b81 and 3.4', '4.15.b6', 'cognitive/r4', 'a creative writing student asks what the minimum is for a portfolio',
   "'Which piece have you taken through more than one draft, and what changed?'", appliesTo=CWA % 'threshold')
kr(T, 80, CW, ['show', 'read', 'respond'], 'audiences, dissemination and responding to work', SK,
   "awareness of differing audiences and ways of reaching them, and the capacity to read and respond to published and unfinished creative work",
   "know about different audiences and ways of reaching them, and read and comment on both published creative writing and drafts in progress",
   '4.2.b83 and 3.4', '4.15.b7', 'cognitive/r2', 'a student prepares for a writing workshop',
   "'Who is this piece for, and where might it be read or heard?'", appliesTo=CWA % 'threshold')
kr(TY, 81, CW, ['generate', 'develop', 'conduct', 'support', 'understand'], 'original work supported by research, writing as research', SK,
   "the capacity to produce and develop original creative work and research in support of it, understanding writing itself as a kind of research",
   "produce and develop original creative work with research to support it, understanding your writing as a form of research in its own right",
   '4.2.b79 and 4.2.b84', '4.15.b6', 'cognitive/r4', 'a student plans the research behind a creative project',
   "'What did you need to find out in order to write this piece?'", appliesTo=CWA % 'typical')
kr(TY, 82, CW, ['deploy'], 'using the rules and possibilities of language across forms and media', SK,
   "use of what written and spoken language allows, its rules and conventions included, across forms, genres and media, aware of the history and culture of language use and literature, media technologies included",
   "use what written and spoken language allows, its rules and conventions included, across forms, genres and media, aware of the history and culture behind them",
   '4.2.b85 and 2.2.b8', '4.15.b2', 'practical/r1', 'a student moves between page, performance and screen forms',
   "'Which convention of this form are you keeping, and which are you breaking on purpose?'", appliesTo=CWA % 'typical')
kr(TY, 83, CW, ['read', 'respond'], 'critical and practical response to published and draft work', SK,
   "critical and practical reading of and response to published work and work in progress",
   "read published work and drafts in progress and respond to them both critically and practically",
   '4.2.b80 and 4.2.b74', '4.15.b7', 'cognitive/r2', 'a student gives workshop feedback',
   "'What would you suggest the writer try next, and why?'", appliesTo=CWA % 'typical')
kr(EX, 84, CW, ['integrate', 'combine', 'produce'], 'ambitious, markedly original work with enterprise and flair', SK,
   "creative integration of all the qualities described with independent enterprise and flair, producing ambitious and strikingly original work",
   "bring all these qualities together creatively, with independent enterprise and flair, to produce ambitious and strikingly original work",
   '4.2.b81 and 4.2.b27', '4.15.b6', 'cognitive/r4', 'a student aims for the top band in a creative dissertation',
   "'What in this piece could only you have written?'", appliesTo=CWA % 'excellent')
kr(EX, 85, CW, ['deploy'], 'discriminating engagement with the powers of language', SK,
   "a creative and discerning engagement with what language can express and imagine",
   "engage creatively and with discernment with what language can express and imagine",
   '4.2.b82 and 1.6.b2', '4.15.b2', 'practical/r1', 'a student revises for precision of language',
   "'Which word in this line would you change, and what would the change gain?'", appliesTo=CWA % 'excellent',
   find="deploy a creative and discriminating engagement with the expressive and imaginative powers of language.")

# ---- the excellent rung's defining paragraph
P['4.2.ex1'] = dict(
  type='excellent', rung='excellent', force='will', forceFrom='4.1', level='fheq:6',
  appliesTo='graduates who have reached the excellent standard', addressee='learner',
  verbs=['demonstrate', 'show', 'displays', 'applies'], about='what defines the excellent standard', domain=UN, award=HON,
  find="Graduates who have attained an excellent standard demonstrate to a higher level the capabilities and skills and show evidence of extensive independent reading, originality of thought and expression, and in-depth understanding. Excellent work displays wide-ranging knowledge of the subject and applies it in subtle and effective ways, showing exceptional critical insight, analytic rigour and creativity.",
  para="Graduates at the excellent standard show the same capabilities at a higher level, with wide independent reading, original thought and expression and deep understanding; their work brings broad knowledge to bear subtly and effectively, with outstanding critical insight, analytical rigour and creativity.",
  prac="Read the excellent column through this definition: the top band shows the same capabilities at a higher pitch, wide independent reading; original thought and expression; broad knowledge used with subtlety, insight, rigour and creativity.",
  ben="If you reach the excellent level, you show the same skills at a higher level: you read widely on your own, think and write originally, understand deeply and use broad knowledge with subtlety, insight, rigour and creativity.",
  aaw=(f"Describe this as the definition of the excellent standard that heads the excellent column, for the honours degree at FHEQ level 6 "
       f"(FQHEIS level 10). Cite it as {CITE}, para 4.2, standards table, excellent column heading. Do not claim it is a pass requirement or "
       f"that most graduates reach it. Set it beside 4.2.b38, 4.2.b46, 4.2.b84 and qaa/fheq-2024/4.15.b1, "
       f"and beside Annex D's first-class descriptions qaa/fheq-2024/annex-d/knowledge/r1/1st and qaa/fheq-2024/annex-d/cognitive/r4/1st."),
  aad=("Raise this when a student or staff member asks what separates excellent work from good work. With a student, put it plainly as what "
       "the best work looks like, something to stretch towards; with staff, frame it as the profile behind the top band. Ask: 'Where in your "
       "recent work did your own reading take you beyond the reading list?' Avoid presenting it as the minimum or reading it aloud."))

# ---- the subject knowledge paragraph spanning the three columns
def sk(k, about, find, verbs, para, prac, ben, nb, when, q):
    P['4.2.sk%d' % k] = dict(
      type='expectation', rung='none', force='will', level='fheq:6', appliesTo='graduates in English, by the elements of their degree',
      addressee='learner', verbs=verbs, about=about, domain=KN, award=HON, find=find, para=para, prac=prac, ben=ben,
      aaw=(f"Describe this as subject knowledge stated with 'will' across all three columns of the standards table, varying in breadth and "
           f"depth from threshold to excellent and by the elements of the degree, at FHEQ level 6 (FQHEIS level 10): {about}. Cite it as "
           f"{CITE}, para 4.2, standards table, subject knowledge (the row spanning all three columns). Do not claim every graduate covers "
           f"each element, since 'may include' lists depend on the degree's make-up, or that it is a regulatory requirement. Set it beside "
           f"{nb}, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."),
      aad=(f"Raise this when {when}. With a student, explain in plain second-person words what knowledge your mix of modules gives you and "
           f"that depth grows from pass to top marks; with staff, frame it as the content map for each element. Ask: {q} Avoid reading the "
           f"paragraph aloud or treating its 'may include' lists as compulsory content."))

sk(1, 'subject knowledge for language elements',
   "The subject knowledge (including relevant contextual knowledge) will vary depending on the elements of the degree. The breadth, depth and range of knowledge will vary over the threshold, typical and excellent standards. For language elements, this may include the investigation and analysis of spoken, written and multimodal communication and culture; the origins and historical development of English; its regional, national and global circulation; the structure and use of varieties of English; knowledge of key subdisciplinary areas, and of qualitative, quantitative and mixed methods of analysis. Students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology, and apply scholarly bibliographic skills appropriate to the subject.",
   ['vary', 'understand', 'deploy', 'apply'],
   "Subject knowledge will differ with the parts of the degree and grow in range and depth across the three standards; for language it may cover analysing spoken, written and multimodal communication, the history, spread and varieties of English, its sub-disciplines and methods; students will understand and use the field's concepts and terms and apply scholarly bibliographic skills.",
   "For the language parts of an English degree, plan knowledge of English in use and in history, its varieties and sub-disciplines and its methods of analysis, and make sure students use the field's concepts and terms and its referencing skills.",
   "If your degree includes English language, you will know how spoken, written and multimodal communication works, how English developed and varies and the main methods for studying it; and you will use the subject's concepts, terms and referencing skills.",
   '3.2, 2.2.b4 and 2.2.b5', 'a student on a language strand asks what they are expected to know',
   "'Which method of language analysis do you feel most at home with, and which least?'")
sk(2, 'subject knowledge for literature elements',
   "For literature elements, this may include close, analytical reading; knowledge of stylistic, expressive, formal and rhetorical properties of texts; the interconnections between literary texts and other forms of expression; awareness of pre-1800 texts for single honours English; alertness to the social, historical and cultural contexts of the processes of composition and production of texts, the histories of their reception and forms of dissemination. Students will engage with literature and/or language from different periods and from the full range of principal literary genres across prose, poetry and drama; students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology and apply scholarly bibliographic skills appropriate to the subject.",
   ['engage', 'understand', 'deploy', 'apply'],
   "For literature it may cover close reading, the stylistic and formal features of texts, links with other forms, pre-1800 texts for single honours and the contexts of production, reception and circulation; students will engage with several periods and the main genres, use the field's concepts and terms and apply scholarly bibliographic skills.",
   "For the literature parts of an English degree, cover close reading, form and style, links across forms, pre-1800 texts for single honours and the contexts of making and reception, across periods and all main genres, with the field's terms and referencing skills.",
   "If your degree includes English literature, you will read closely, know how texts work in form and style and in their contexts, study several periods and all the main genres; and you will use the subject's concepts, terms and referencing skills.",
   '3.3, 3.3.s1 and 2.2.b2', 'a student on a literature strand asks what range they must cover',
   "'Which period or genre is thinnest in your reading so far?'")
sk(3, 'subject knowledge for creative writing elements',
   "For Creative Writing elements in the context of English, this may include a process of reflection on the development of individual and peer writing practices informed by broad and critical reading of writing produced in a wide range of social, historical and cultural contexts; understanding the complex interactive relationship between writers, publishers, texts and audiences; developing the discipline of writing to specific briefs, and showing awareness of the importance of the drafting process and the benefits of working collaboratively. Students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology and apply scholarly bibliographic skills appropriate to the subject.",
   ['understand', 'deploy', 'apply'],
   "For creative writing it may cover reflecting on one's own and peers' writing through wide critical reading, the relations of writer, publisher, text and audience, writing to a brief, drafting and collaboration; students will use the field's concepts and terms and apply scholarly bibliographic skills.",
   "For the creative writing parts of an English degree, build reflection on own and peer practice from wide reading, knowledge of publishing and audiences, writing to briefs, drafting and collaboration, with the field's terms and referencing skills.",
   "If your degree includes creative writing, you will reflect on your own and others' writing in light of wide reading, understand how writers, publishers, texts and audiences connect, write to briefs, draft and collaborate; and you will use the subject's concepts, terms and referencing skills.",
   '3.4 and 4.2.b79 to 4.2.b85', 'a creative writing student asks what critical knowledge is expected of them',
   "'How has your reading changed the way you draft?'")

# ------------------------------------------------------------------ rung links
CHAINS = [
  ('communicating arguments to an audience', '4.2.b1', '4.2.b3', '4.2.b6', GS),
  ('writing as a process of revision', '4.2.b2', '4.2.b5', '4.2.b9', GS),
  ("engaging other writers' arguments", 'none', '4.2.b4', '4.2.b7', GS),
  ('the affective power of language', '4.2.b10', '4.2.b12', '4.2.b13', SK),
  ('digital communication', '4.2.b15', '4.2.b16', '4.2.b17', GS),
  ('collaboration and independent work', '4.2.b18', '4.2.b20', '4.2.b21', GS),
  ('creative interpretation', '4.2.b25', '4.2.b26', '4.2.b27', SK),
  ('critical thinking', '4.2.b28', '4.2.b33', '4.2.b38', GS),
  ('critical understanding of complex texts', '4.2.b29', '4.2.b34', '4.2.b39', UN),
  ('reflecting on reading and writing', '4.2.b30', '4.2.b35', '4.2.b40', SK),
  ('rigour with data and evidence', '4.2.b31', '4.2.b36', '4.2.b42', GS),
  ('debate, disagreement and ambiguity', '4.2.b32', '4.2.b37', '4.2.b43', GS),
  ('gathering and analysing evidence', '4.2.b44', '4.2.b45', '4.2.b46', GS),
  ('close reading', '4.2.b47', '4.2.b48', '4.2.b49', SK),
  ('plurality and evaluation of interpretations', '4.2.b50', '4.2.b51', '4.2.b52', UN),
  ('assessment tasks', '4.2.b53', '4.2.b55', '4.2.b58', GS),
  ('time management', '4.2.b54', '4.2.b57', '4.2.b60', GS),
  ('seeking help', 'none', '4.2.b56', '4.2.b59', GS),
  ('listening to other perspectives', '4.2.b61', '4.2.b62', 'none', GS),
  ('placing own views among others', 'none', '4.2.b63', '4.2.b65', GS),
  ('academic integrity', '4.2.b66', '4.2.b67', '4.2.b69', GS),
  ('bibliographies and citation', 'none', '4.2.b68', '4.2.b70', GS),
  ('using feedback', '4.2.b71', '4.2.b73', '4.2.b75', GS),
  ('peer feedback', '4.2.b72', '4.2.b74', 'none', GS),
  ('generating and developing creative work', '4.2.b79', '4.2.b81', '4.2.b84', SK),
  ('responding to creative work', '4.2.b80', '4.2.b83', 'none', SK),
  ('language across forms and media', 'none', '4.2.b82', '4.2.b85', SK)]
GRADE = {}
for _n, _t, _ty, _ex, _d in CHAINS:
    if _ty != 'none' and _t != 'none':
        GRADE[_ty.split('/')[-1]] = _t
    if _ex != 'none' and _ty != 'none':
        GRADE[_ex] = _ty
GRADE.update({'4.2.b22': '4.2.b20', '4.2.b41': '4.2.b35'})
for _k, _v in GRADE.items():
    assert P[_k]['domain'] == P[_v]['domain'], (_k, _v)
TH = {}

# ------------------------------------------------------------------ levels, themes, relations
S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.4; 4.2 (Annex D for FHEQ Level 6 degrees)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.4; 4.2 (Annex D for FQHEIS Level 10 degrees)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.4: "a degree with honours (FHEQ Level 6; FQHEIS Level 10)"; 4.2 names both for Annex D); matches std:doc:qaa-fheq-2024-framework Table 1 (honours: FHEQ 6, SCQF 10) and the reference framework spine:6')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.7', '1.8', '1.9', '1.10', '1.11', '3.5', '4.2']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.12', '1.13', '2.7', '3.10', '4.2']),
      dict(id='theme:esd', role='carries', carriedIn=['1.14', '1.15', '1.16', '4.2']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '2.8', '4.2']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['4.2'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-english-2019-benchmarks (not ingested)', note='section 6 names the fourth edition (2019), revised from the 2015 third edition; the 2023 advisory group wrote this edition (D1, section 6)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the four honours classifications, for achievement above threshold (D1, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Level 6 (D1, 2.4, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Level 10 (D1, 2.4, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-creative-writing-2024-benchmarks', note='courses with creative writing reference it; the creative writing rows point to it for the full standards (D1, 1.2, 3.4, 4.2); the edition meant in 2023 was the 2019 one (Part E)'),
      dict(rel='refersTo', target='std:doc:qaa-linguistics-2023-benchmarks (not yet ingested)', note='courses with Linguistics elements are likely to reference it (D1, 1.2)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='listed in section 5, behind the ESD paragraphs (1.14 to 1.16)'),
      dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='listed in section 5, behind the enterprise paragraphs (1.17 to 1.22)'),
      dict(rel='refersTo', target='QAA Quality Code for Higher Education and its Advice and Guidance (not ingested)', note='front matter; section 5')]

# ------------------------------------------------------------------ the variant's sections
SB1 = [
  "English studies meaning made through communication in English and related languages, across language, literature and creative writing, and is often studied jointly or with neighbouring subjects such as film, media, cultural or translation studies (D1, 1.1, 1.2, 1.4).",
  "Its distinctive emphasis is discourse and meaning, aesthetics and rhetoric: close and critical reading in context, analysis of written and spoken texts and reflection on reading, writing and interpretation (D1, 1.6).",
  "It joins critical and creative response, so producing new creative work sits beside interpretation and analysis (D1, 1.4, 1.6, 3.4).",
  "It values dialogue, debate and difference, and engages with diverse perspectives and with the discipline's own colonial, patriarchal and elitist history (D1, 1.7 to 1.10).",
  "It builds four core capacities named throughout: communication, collaboration, creativity and critical thinking (D1, 1.4, 1.5, 1.18, 3.10).",
  "Teaching leans on small groups, independent and collaborative study, flipped lectures, use of libraries, archives and corpora and a capstone project (D1, 3.5 to 3.9).",
  "Assessment is deliberately diverse, from essays and examinations to digital objects, performance and portfolios (D1, 3.10, 3.11)."]
SB2 = [
  dict(theme='theme:edi', inThisSubject="plural voices and contested narratives, a reckoning with the discipline's colonial, patriarchal and elitist history and with imbalances among students and staff, diversified curricula beyond a core and periphery and graduates attentive to diverse audiences; in the standards, listening to and fairly placing other perspectives and cultural sensitivity in group work (D1, 1.7 to 1.11, 4.2)", statements=['4.2.b61', '4.2.b62', '4.2.b63', '4.2.b64', '4.2.b65', '4.2.b23']),
  dict(theme='theme:accessibility', inThisSubject="accessible courses with inclusive methods and assessment, attention to neurodiversity, health conditions, caring, commuting and religious observance, many routes of entry, responsive design and accessible digital resources (D1, 1.12, 1.13, 2.7, 3.10); the standards table names access in its embedded row heading but no single item carries it", statements=[]),
  dict(theme='theme:esd', inThisSubject="the study of English contributes to sustainable development through its four core capacities, ecocriticism, world literatures and global varieties of English, the colonial past and resource extraction and global citizenship in a multilingual world (D1, 1.14 to 1.16); in the standards, awareness of perspectives from local to global", statements=['4.2.b61']),
  dict(theme='theme:enterprise', inThisSubject="communication, collaboration, creativity and critical thinking framed as enterprise skills, with careers across many sectors, placements and partnerships; in the standards, transferring these skills to work and entrepreneurship and acting with integrity (D1, 1.17 to 1.22, 2.8, 4.2)", statements=['4.2.b77', '4.2.b78', '4.2.b20']),
  dict(theme='theme:generative-ai', inThisSubject="large language models appear only under academic integrity: graduates use them as writing aids with integrity and ethical responsibility, the threshold allowing occasional inaccuracy in references (D1, 4.2)", statements=['4.2.b66', '4.2.b67', '4.2.b69'])]
SB3 = dict(
  areas=[dict(component='3.2', gloss='English language: spoken, written and multimodal communication, varieties, history, sub-disciplines and methods'),
         dict(component='3.3', gloss='English literature: prose, poetry and drama across periods, contexts, theory, reception and dissemination'),
         dict(component='3.4', gloss='creative writing within English: reflective practice, original work, publishing and audiences')],
  practices=[dict(component='2.7', kind='teaching', gloss='responsive design, varied assessment and accessible digital resources'),
             dict(component='3.5', kind='teaching', gloss='dialogue, instruction, independent and group work, co-creation; online and face to face'),
             dict(component='3.6', kind='learning', gloss='guided preparation for classes'),
             dict(component='3.7', kind='learning', gloss='independent study before class; flipped lectures'),
             dict(component='3.8', kind='teaching', gloss='seminars, tutorials and workshops for dialogue and peer critique'),
             dict(component='3.9', kind='learning', gloss='libraries, archives, corpora and a capstone project'),
             dict(component='3.10', kind='assessment', gloss='diverse assessment, also for accessibility'),
             dict(component='3.11', kind='assessment', gloss='forms of assessment, from essays to digital objects and portfolios'),
             dict(component='3.12', kind='assessment', gloss='what assessment rewards, from argument to imaginative communication')])
OUTCOMES = [dict(outcome=n, threshold=t, typical=ty, excellent=ex, basis='inferred', domain=d, award=HON) for n, t, ty, ex, d in CHAINS]
SB4 = dict(
  rungs=[dict(rung='threshold', leadIn='4.2', award=HON, items=26),
         dict(rung='typical', leadIn='4.2', award=HON, items=27),
         dict(rung='excellent', leadIn='4.2', award=HON, items=33)],
  rungBases=("4.1: the statement sets the minimum threshold standards a student will have shown at the award of honours; 4.2: most "
             "students perform well above it, judged with Annex D. The standards are one table with three columns, each headed by a rung "
             "definition (threshold: the minimum that should be reached; typical: the main cluster; excellent: a defining paragraph, "
             "recorded as 4.2.ex1) and the lead-in 'are able to'. Rows: generic skills (communication, affective language, digital, "
             "collaboration, creativity, critical thinking, evidence); subject knowledge (close reading, interpretation, then a paragraph "
             "spanning all three columns, recorded as 4.2.sk1 to sk3 with rung none); embedded understanding of EDI, access, "
             "sustainability and entrepreneurship; creative writing, with its own lead-in. Cells hold several bullets each, so the "
             "columns hold different numbers of items."),
  outcomeLists=[dict(leadIn='1.6', gloss='what English graduates can do (introduced with can)', items=8, award=[HON]),
                dict(leadIn='2.2', gloss='what graduates will know about, by the aspects studied', items=9, award=[HON]),
                dict(leadIn='4.2', gloss='subject knowledge across all three columns, by the elements of the degree (will)', items=3, award=[HON])],
  outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [
  dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed', says='the statement supports them on academic standards, their requirements are a further reference point and courses with vocational outcomes may need their accreditation (D1, front matter, 2.12)', requirements='not-applicable-by-design: no body named (Part E)'),
  dict(body='Office for Students (regulator, England)', says='under its regulatory framework the statements are not sector-recognised standards in England (D1, front matter)', requirements='not yet ingested (Part E)')]
SB6 = dict(
  themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.7', '1.8', '1.9', '1.10', '1.11', '3.5', '4.2'], statements=['4.2.b61', '4.2.b62', '4.2.b63', '4.2.b64', '4.2.b65', '4.2.b23']),
          dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students; 4.2: access)', carriedIn=['1.12', '1.13', '2.7', '3.10', '4.2'], statements=[]),
          dict(id='theme:esd', named='Education for Sustainable Development (4.2: sustainability)', carriedIn=['1.14', '1.15', '1.16', '4.2'], statements=['4.2.b61']),
          dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '2.8', '4.2'], statements=['4.2.b77', '4.2.b78', '4.2.b20']),
          dict(id='theme:generative-ai', named='large language models (sometimes known as artificial intelligence)', carriedIn=['4.2'], statements=['4.2.b66', '4.2.b67', '4.2.b69'])],
  frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.4', '4.2']),
              dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.4', '4.2'])],
  bodies=[dict(body='PSRBs (unnamed)', citedIn=['front matter', '2.12']),
          dict(body='Office for Students (regulator, England)', citedIn=['front matter']),
          dict(body='UNESCO (source of the ESD definition)', citedIn=['1.14']),
          dict(body='The British Academy (SHAPE)', citedIn=['1.5', '5'])],
  sharedDocuments=[
    dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold'),
    dict(document='std:doc:qaa-creative-writing-2024-benchmarks', named='the Creative Writing Subject Benchmark Statement', citedIn=['1.2', '3.4', '4.2'], role='reference for courses with creative writing; full creative writing standards'),
    dict(document='std:doc:qaa-linguistics-2023-benchmarks (not yet ingested: Part E)', named='the Subject Benchmark Statement for Linguistics', citedIn=['1.2'], role='reference for courses with linguistics elements'),
    dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE (2021) Education for Sustainable Development Guidance', citedIn=['5'], role='listed reference behind the ESD paragraphs'),
    dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['5'], role='listed reference behind the enterprise paragraphs'),
    dict(document='UNESCO (2019) and the UN Sustainable Development Goals (external, not ingested)', named='UNESCO, 2019; the UN\'s Sustainable Development Goals', citedIn=['1.14'], role='definition of ESD'),
    dict(document='The British Academy (2020) SHAPE (external, not ingested)', named='Social Sciences, Humanities and the Arts for People and the Economy/Environment (SHAPE)', citedIn=['1.5', '2.8', '5'], role='the family of subjects whose general capabilities English shares'),
    dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code for Higher Education; The UK Quality Code for Higher Education', citedIn=['front matter', '5'], role='course design, teaching, external expertise, monitoring'),
    dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
    dict(document='Quality Enhancement Review (Wales); Quality Enhancement Framework (Scotland) (not ingested)', named='the same', citedIn=['front matter'], role='where the statement is a key reference point')])

B1 = [
  dict(slug='threshold-standard', definition='the minimum a student will have shown to be awarded the honours degree, and the least that should be reached (D1, 4.1, 4.2)', beneficiaryDefinition='the least you need to have shown by the end of your honours degree', scopeNote='the threshold column of the 4.2 table', category='unknown', practices=['education']),
  dict(slug='typical-standard', definition='what the typical student in the main cluster of results attains (D1, 4.2)', beneficiaryDefinition='what most people show by the end of the degree', scopeNote='the typical column of the 4.2 table', category='unknown', practices=['education']),
  dict(slug='excellent-standard', definition='the capabilities shown at a higher level, with wide independent reading, originality and deep understanding (D1, 4.2)', beneficiaryDefinition='what the strongest work shows, beyond the typical', scopeNote='the excellent column of the 4.2 table', category='unknown', practices=['education']),
  dict(slug='shape-subjects', definition='the social sciences, humanities and arts grouped as subjects for people and the economy or environment, whose general capabilities English shares (D1, 1.5)', category='unknown', practices=['education']),
  dict(slug='ecocriticism', definition='criticism that puts the environment at the centre of interpretation (D1, 1.15)', beneficiaryDefinition='reading texts with the environment as the main focus', category='unknown', practices=['education']),
  dict(slug='flipped-approach', definition='teaching in which students read and form responses before class, which then discusses them (D1, 3.7)', beneficiaryDefinition='you prepare and form your views before the class, which then builds on them', category='unknown', practices=['education'])]
B2A = [
  dict(concept='threshold-standard', form='Threshold Standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='typical-standard', form='Typical Standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='excellent-standard', form='Excellent Standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='shape-subjects', form='SHAPE subjects', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='ecocriticism', form='Ecocriticism', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
  dict(concept='flipped-approach', form="'flipped' approach", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific')]
B4 = []; B5 = []
D3 = []

E = [
  "SB4, rung shape: one table under 4.2 with three columns (Threshold Standard, Typical Standard, Excellent Standard), its header repeated on each page; the held text linearises it cell by cell, threshold cell then typical cell then excellent cell for each row, with no column marks. Each bullet (skeleton 4.2.b1 to b85) is assigned to its column by reading the row: threshold 26, typical 27, excellent 32 items plus the excellent rung's defining paragraph (4.2.ex1), so 33. The skeleton's rung counts (85 threshold) were wrong. For P3: the column of each bullet is our reading, not marked in the held text.",
  "SB4, rows with uncertain column breaks, for P3: communication (b1 to b2 threshold, b3 to b5 typical, b6 to b9 excellent); affective language (b10 and b11 threshold, b12 typical, b13 and b14 excellent); collaboration (b18 and b19 threshold, b20 typical, b21 to b24 excellent); assessment tasks (b53 and b54, b55 to b57, b58 to b60); perspectives (b61, b62 and b63, b64 and b65); feedback (b71 and b72, b73 and b74, b75 and b76).",
  "SB4, enterprise and values row (4.2.b77, b78): only two bullets, with no second or third cell in the held text. Read as the threshold cell; the cell may span all three columns in the original layout. Wanted: the PDF page for this row.",
  "S4, 4.2.b8 ends at a page break ('in light of new evidence and'); the rest of the item ('claims, appropriate to the intended audience') follows the repeated table header on the next page. The span keeps the skeleton's cut so `source` holds no header text; the paraphrase covers the whole item.",
  "S4, skeleton corrections by `find`: 4.2.b52, whose skeleton span ran on through the subject knowledge paragraph, is cut at the end of its bullet; the paragraph is recorded as 4.2.sk1 (with its two opening sentences and the language elements), 4.2.sk2 (literature elements) and 4.2.sk3 (creative writing elements), rung none, force will. 4.2.b85 is cut before 'For a full expression of Creative Writing benchmark standards, please consult the Creative Writing Benchmark Statement' (a pointer, not a standard). 2.4, 2.5, 2.10 and 4.2 are cut as their obliging sentences; 3.3.s1 is our id for 3.3's first sentence.",
  "S4, ids: 4.2.ex1, 4.2.sk1 to sk3 and 3.3.s1 are ours, not the issuer's numbering; the builder sorts them after the numbered records.",
  "S4, force: threshold cells take `threshold` from the column definition ('the minimum requirement that should be reached', given by `forceFrom`) and from 4.1; typical and excellent cells take `will` from their lead-ins ('are able to'), by `forceFrom`; 4.2.ex1 (plain present 'demonstrate') takes `will` from 4.1 by `forceFrom`. For Abbott at P3: the threshold definition also carries 'requirement' and 'should'.",
  "S4, 1.6: an outcome list introduced with 'can' ('English graduates can:'), recorded as 8 outcome items with force `will` (the builder reads 'can' with 'able to' as will). For Abbott: keep as will, or describes? The list echoes the standards table and 3.12.",
  "S4, 2.2: an outcome list in 'will know about', qualified by 'depending on the aspects of the subject they have studied'; recorded as 9 knowledge outcomes at fheq:6 (level from 2.4). 2.3's 'paragraphs 3.2-3.4' is a reference (DPN-1), not cut.",
  "S4, 2.4: recorded as its first three sentences (will progress; builds towards the threshold; will usually include credit). Its fourth sentence ('it would be expected ... would be capable of') is outside the five words and not taken; its fifth ('may require', of postgraduate entry) is hedged and not taken.",
  "S4, not taken as statements (D-std-0002 (a)): 1.5 (capacities the subject develops, plain present); 1.11 and 1.21 (graduates and students described in plain present); 2.11 ('will be asked', 'will consider': a description of the external examiner system, hedged by 'typically'); 2.12 ('may also require' accreditation: hedged); 3.5 ('there will usually be' a mix of online modes); 3.7 ('will very often take a flipped approach', 'will then be encouraged': descriptive); 4.1 (the definition of the threshold, used as `forceFrom`); the typical column's definition ('the level of attainment reached by the typical student').",
  "S4, plain-present provider norms not recorded as statements (template open point 5): 1.12 ('English courses are designed to be highly accessible'; staff 'reflect current legislation'); 2.7 (programmes 'make use of' inclusive methods, with four examples); 2.9 (review processes); 3.6 (preparation 'is clearly structured'); 3.11 and 3.12 (forms of assessment; what assessment 'rewards').",
  "S4, obliging words outside the five: 'requirement' (the threshold definition, recorded as the threshold force) and 'necessity' (4.2.b54, b66: what students understand or are aware of, not an obligation on them) recorded with their cells' force, not as must.",
  "S4, domain: our reading. The issuer heads the first rows 'Generic skills', but the affective-language row (b10 to b14), the creativity row (b25 to b27) and the reflection and evaluation items (b30, b35, b40, b41) concern the subject's own texts and methods and are recorded as subject-skill; b29, b34, b39 (critical understanding of texts and their history) and the interpretation row (b50 to b52) as understanding. The embedded understanding rows are generic-skill.",
  "S4, gradeOf: 48 links, all inferred (the issuer pairs nothing; a row only groups cells): within each traced outcome in SB4, typical to threshold and excellent to typical, plus 4.2.b22 to b20 (teamwork) and 4.2.b41 to b35 (evaluating forms). Less plain, for P3: b21 to b20 (b21 repeats the threshold wording b18 at the excellent rung), b55 to b53 (adapting to tasks against carrying out tasks), b58 to b55, b13 to b12.",
  "S4, repeated wording across rungs: b18 and b21 (collaboration), b31, b36 and b42 (rigour with evidence), b67 and b69 (integrity) are word for word the same in two or three columns; the rung is given by the column alone.",
  "S4, verbs: 2.2's items are noun phrases with no action verb, so `verbs` is empty. 4.2.b46 has the issuer's 'analyses' (sic) and b85 'deploy'; verbs are recorded as spelled.",
  "S3: sub-headings fall at the end of the paragraph before them in the held text (for example 'Equality, diversity and inclusion' closes 1.7, 'Purposes and characteristics of an English Degree' closes 1.3), so the skeleton's components 1.3, 1.7, 1.11, 1.13 and 1.16 carry a following heading. Sub-heading ranges in SUB are ours, from the contents list.",
  "SB6, themes: the skeleton's candidate hits were one paragraph early (from the trailing headings); confirmed hits are EDI 1.8 to 1.11 (with 1.7 and 3.5 on difference and perspectives), accessibility 1.12, 1.13, 2.7, 3.10, ESD 1.14 to 1.16, enterprise 1.17 to 1.22 and 2.8 (careers), with all four in the 4.2 row heading 'Embedded understanding of EDI, access, sustainability and entrepreneurship'. Large language models appear only in the integrity row (4.2.b66, b67, b69) and are recorded as theme:generative-ai by the batch 1 convention.",
  "SB6, frameworks: FHEQ Level 6 and FQHEIS Level 10 named together in 2.4 and 4.2. CQFW is not cited. 'Scottish Highers' (1.13) and Scottish four-year honours (2.6) name no framework.",
  "SB5 and SB6, bodies: no professional body for the subject is named; PSRBs appear only generically (front matter, 2.12). The Office for Students is named as England's regulator. UNESCO (1.14) and The British Academy (1.5 via SHAPE; section 5) are named organisations, not PSRBs; listed in SB6 only.",
  "SB6, shared documents: the Creative Writing statement is cited without a year (1.2, 3.4, 4.2); in September 2023 the current edition was 2019, but the ingested one is 2024. Linked to std:doc:qaa-creative-writing-2024-benchmarks; for P3. The Linguistics statement (1.2) is not yet ingested. The ESD guidance (2021) and the enterprise guidance (2018) are cited only in section 5 (excluded matter); 1.14 cites UNESCO (2019) directly.",
  "S2, subjects: HECoS 100320 (English studies, whose non-preferred terms include 'English') and CAH19-01 are stated by the subject name; 100318, 100319 and 100046 (with CAH19-01-02, CAH19-01-03 and CAH19-01-05) are stated by the course titles in 1.1. CAH19-01-01 (English studies, non-specific) is inferred as the CAH3 home of 100320. Linguistics (CAH19-01-07) is a neighbouring statement, not entered.",
  "S7, supersedes: section 6 names the fourth edition (2019), revised by QAA from the 2015 third edition; this edition (September 2023) is therefore read as the fifth (inferred). The 2023 advisory group is the one that wrote it.",
  "Patterns differing from Psychology: one three-column table in place of separate rung lists, linearised cell by cell; rung definitions as column headings rather than lead-ins; varying numbers of items per cell; a paragraph spanning all three columns; a separate creative writing lead-in inside the table; an outcome list with 'can' (1.6); large language models under integrity; no professional body.",
  "S9: not researched in P1.",
  "S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check."]
