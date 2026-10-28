# Judgement for run 0126, QAA Subject Benchmark Statement: Policing (March 2022), std run agent.
# Keys are S4 ids under qaa/policing-in-partnership-with-2022/. Written fresh from the held text (benchmark rule 6).
HON = "bachelor's with honours"
CITE = 'QAA (2022), Policing Subject Benchmark Statement, para %s'
NA_PROV = 'a duty on those who design and run the course; the student meets its effect, not a standard to reach'

META = dict(
    run='0126', p1='2026-10-03 18:23',
    title='Subject Benchmark Statement Policing',
    heading='Subject Benchmark Statement: Policing (QAA, March 2022)',
    edition='March 2022', published='2022-03',
    status='current', supersedes='none-stated',
    subjects=[
        dict(scheme='hecos', code='100486', label='policing', basis='stated'),
        dict(scheme='cah', code='CAH16-01-01', label='law', basis='inferred'),
        dict(scheme='cah', code='CAH16-01', label='law', basis='inferred'),
        dict(scheme='cah', code='CAH16', label='law', basis='inferred'),
        dict(scheme='hecos', code='100484', label='criminology', basis='inferred'),
        dict(scheme='hecos', code='100483', label='criminal justice', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 series with cross-cutting themes (first edition for Policing, written in partnership with the College of Policing)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what an honours graduate in Policing should know and be able to do, written in partnership with "
                     "the College of Policing. It sets one rung only, the threshold, as two lists (subject knowledge and skills; generic skills), "
                     "and leaves achievement above it to Annex D of the qualifications frameworks. Reach for it when designing, reviewing or "
                     "describing a Policing degree, including the College's licensed entry routes in England and Wales. It is not the National "
                     "Policing Curriculum, not a licence condition and not regulation."),
    summary=("Published by QAA in March 2022 as the first Policing statement, it sets out the context of policing education in each UK nation "
             "(the PEQF entry routes in England and Wales, Police Scotland's own training, the PSNI degree), the purposes and characteristics "
             "of a degree, its distinctive features (design, employer involvement, progression, flexibility, partnership, monitoring), content, "
             "teaching and assessment, and 29 threshold standards for the bachelor's degree with honours (FHEQ level 6, FQHEIS level 10). "
             "No typical or excellent rung is stated. It treats equality, diversity and inclusion, accessibility, sustainability (with "
             "horizon scanning) and employability, and names the College of Policing as the professional body throughout."),
    authority=('reference: a sector reference point; not a sector-recognised standard in England, a key reference point in Wales and '
               'Scotland, part of the quality requirements in Northern Ireland; reviewed by the College of Policing (D1, front matter)'),
)

S2 = dict(
    governs='the bachelor\'s degree with honours in Policing: its context, purposes, distinctive features, content and delivery, and threshold standards',
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Policing that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter)',
    statedSubjects=[
        dict(name='Policing', locator='(D1, front matter; 1.10)', kind='subject', codes=[dict(scheme='hecos', code='100486', label='policing')]),
        dict(name='BSc (Hons) Policing and Criminology (Applied Practice)', locator='(D1, 1.8)', kind='programme title',
             codes=[dict(scheme='hecos', code='100486', label='policing'), dict(scheme='hecos', code='100484', label='criminology')]),
        dict(name='policing, criminal justice and criminology programmes', locator='(D1, 2.14)', kind='specialism',
             codes=[dict(scheme='hecos', code='100484', label='criminology'), dict(scheme='hecos', code='100483', label='criminal justice')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Policing degree', '2': 'Distinctive features of a Policing degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.2', 'Context'), ('1.3', '1.5', 'Context: England and Wales'), ('1.6', '1.7', 'Context: Scotland'),
       ('1.8', '1.9', 'Context: Northern Ireland'), ('1.10', '1.12', 'Purposes of a Policing degree'),
       ('1.13', '1.16', 'Characteristics of a Policing degree'), ('1.17', '1.19', 'Equality, diversity and inclusion'),
       ('1.20', '1.23', 'Accessibility'), ('1.24', '1.26', 'Sustainability and horizon scanning: Sustainability'),
       ('1.27', '1.29', 'Sustainability and horizon scanning: Horizon scanning'), ('2.1', '2.4', 'Design'),
       ('2.5', '2.9', 'Employer involvement'), ('2.10', '2.12', 'Progression'), ('2.13', '2.14', 'Flexibility'),
       ('2.15', '2.19', 'Partnership'), ('2.20', '2.23', 'Monitoring and review'), ('3.1', '3.3', 'Content'),
       ('3.4', '3.10', 'Teaching and learning'), ('3.11', '3.13', 'Assessment'), ('3.14', '3.14', 'Assessment strategy'),
       ('3.15', '3.17', 'Assessment strategy: Forms of assessment'), ('4.1', '4.2', 'Introduction'),
       ('4.3', '4.3', 'Threshold level: Subject knowledge, understanding and skills'), ('4.4', '4.4', 'Threshold level: Generic skills')]

G = {
    '1.1': 'the stated mission of UK policing today',
    '1.2': 'professionalising policing; core capabilities the service needs',
    '1.3': 'the College of Policing and its standard-setting role',
    '1.4': 'the PEQF and its three entry routes to constable',
    '1.5': 'unlicensed Policing degrees still have value',
    '1.6': 'Scotland: no higher education entry route; Police Scotland College',
    '1.7': 'Scottish degrees designed with Police Scotland; special constables',
    '1.8': 'Northern Ireland: the PSNI degree and graduate certificate',
    '1.9': 'theory beneath applied practice; reflective, integrated curriculum',
    '1.10': 'the main purpose: competent policing professionals',
    '1.11': 'what programmes introduce students to',
    '1.12': 'a protected space for communication skills',
    '1.13': 'constable capabilities aligned to honours level',
    '1.14': 'alignment to CVF, Peelian Principles and Code of Ethics',
    '1.15': 'what a holder of the degree can do',
    '1.16': 'a degree that excludes no group',
    '1.17': 'EDI at the core; equality duties; impact assessment',
    '1.18': 'EDI and ethics embedded; students own their conduct',
    '1.19': 'inclusive teaching and assessment planned from the start',
    '1.20': 'widening access; physical and digital barriers',
    '1.21': 'inclusion for all rather than target groups',
    '1.22': 'varied routes and flexible delivery for access',
    '1.23': 'accessibility law and what online provision lets students do',
    '1.24': 'honours programmes and sustainable development',
    '1.25': 'what education for sustainable development is',
    '1.26': 'programmes designed with the SDGs; eight themes',
    '1.27': 'future challenges feeding programme review',
    '1.28': 'trends the College of Policing foresees',
    '1.29': 'other changes that may reshape programmes',
    '2.1': 'programmes designed for progressive learning',
    '2.2': 'what programmes enable graduates to do',
    '2.3': 'skills planned across every module',
    '2.4': 'the National Policing Curriculum in licensed programmes',
    '2.5': 'employer and professional body involvement; trust',
    '2.6': 'staff associations and volunteers in programme review',
    '2.7': 'engaging and upskilling the existing workforce',
    '2.8': 'operational deployments; workplace tutors and assessors',
    '2.9': 'research and practitioner-researchers shaping degrees',
    '2.10': 'progression year by year to the threshold',
    '2.11': 'joint honours students',
    '2.12': 'exit awards; four-year Scottish honours',
    '2.13': 'varied teaching methods; independent and work-based learning',
    '2.14': 'the final-year independent project or dissertation',
    '2.15': 'what a partnership is',
    '2.16': 'an institutional strategy for partnerships',
    '2.17': 'partners and the national qualifications framework',
    '2.18': 'awarding body safeguards for standards and experience',
    '2.19': 'written agreements, due diligence and records',
    '2.20': 'monitoring and periodic review',
    '2.21': 'external reviewers in periodic review',
    '2.22': 'external examiners and threshold standards',
    '2.23': 'professional accreditation for vocational courses',
    '3.1': 'a constantly evolving subject',
    '3.2': 'five core themes for every policing award',
    '3.3': 'sixteen indicative topics',
    '3.4': 'from teacher-centred to learner-centred police education',
    '3.5': 'student-centred and experiential learning',
    '3.6': 'the Student as Producer model',
    '3.7': 'students as producers of knowledge',
    '3.8': 'academic and practitioner knowledge combined',
    '3.9': 'conditions for co-producing knowledge',
    '3.10': 'practice and academia merged; reflective practice',
    '3.11': 'assessment in licensed PEQF programmes',
    '3.12': 'other programmes may not need practical skills',
    '3.13': 'applied assessment for every Policing degree',
    '3.14': 'co-designed assessment; strategy principles and safeguards',
    '3.15': 'varied, inclusive assessment with student voice',
    '3.16': 'full assessment information; balance of methods',
    '3.17': 'regular review of assessments',
    '4.1': 'the threshold as a minimum for honours',
    '4.2': 'most exceed it; Annex D for the classes',
    '4.3': 'threshold subject knowledge, understanding and skills',
    '4.4': 'threshold generic skills',
}
CTYPE = {'3.1': 'area', '3.2': 'area', '3.3': 'area', '2.13': 'practice', '2.14': 'practice', '3.4': 'practice', '3.5': 'practice',
         '3.6': 'practice', '3.13': 'practice', '3.15': 'practice', '3.16': 'practice'}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines (sections 1 to 4)', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references', kind='references'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: membership, College of Policing EDI note and acknowledgements; read for S1 and S8'),
]

# ------------------------------------------------------------------ helpers for the agent instructions
FW6 = 'the FHEQ honours descriptor (qaa/fheq-2024/4.15) and spine:6'
P = {}


def ref(i):
    if '.b' in i:
        n, k = i.split('.b')
        return '%s, item %s' % (n, k)
    return i


FWORD = {'will': "an outcome the statement expects ('will')", 'must': "a requirement ('must')", 'should': "an expectation ('should')",
         'threshold': 'a threshold standard'}


def aaw_of(i, r):
    c = CITE % ref(i)
    bes = r.pop('bes')
    xn = r.pop('xn', '')
    if r['rung'] == 'threshold':
        s = [f"Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here {r['about']}.",
             f"Cite it as {c}, and set it beside {bes}.",
             "Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."]
    elif r['addressee'] in ('learner', 'both'):
        s = [f"Describe this as {FWORD[r['force']]} of {r['appliesTo']} at honours level (FHEQ 6, FQHEIS 10), about {r['about']}.",
             f"Cite it as {c}, and set it beside {bes}.",
             "Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."]
    else:
        s = [f"Describe this as {FWORD[r['force']]} on those who design and run Policing degrees, about {r['about']}: a course duty, not a student outcome.",
             f"Cite it as {c}, and set it beside {bes}.",
             "Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."]
    if xn:
        s.append(xn)
    return ' '.join(s)


def aad_of(i, r):
    when, ask = r.pop('when'), r.pop('ask')
    if r['rung'] == 'threshold':
        s = [f"Raise it when {when}.",
             "With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show.",
             f"Ask: \"{ask}\"",
             "Do not read the issuer's list aloud or imply that this minimum is what most students reach."]
    elif r['addressee'] in ('learner', 'both'):
        s = [f"Raise it when {when}.",
             "With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible.",
             f"Ask: \"{ask}\"",
             "Avoid quoting the paragraph at length or treating it as a pass mark."]
    else:
        s = [f"Raise it when {when}.",
             "Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience.",
             f"Ask: \"{ask}\"",
             "Do not give it to a student as something they must achieve."]
    return ' '.join(s)


def s(i, **k):
    k.setdefault('award', HON)
    P[i] = k


def prov(i, force, verbs, about, para, prac, when, ask, bes, xn='', ben=None, **k):
    s(i, type='requirement' if force == 'must' else 'expectation', rung='none', force=force, level='none',
      appliesTo=k.pop('appliesTo', 'those who design and run Policing degrees'), addressee='provider', verbs=verbs, about=about,
      domain='none', para=para, prac=prac, ben=ben or ('n/a', NA_PROV), when=when, ask=ask, bes=bes, xn=xn, **k)


# ------------------------------------------------------------------ section 1
s('1.10', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['develop', 'demonstrate'], about='understanding of the profession and its legal setting', domain='understanding',
  para="The degree's main aim is to equip students with the knowledge, skills and behaviours of competent policing professionals; across the course students will build and show an understanding of the profession and of the legal and regulatory setting of policing and criminal justice.",
  prac="Plan the course so that, from start to finish, students will build and show an understanding of the policing profession and of the law and regulation that frame policing and the criminal justice system.",
  ben="Across your course you will build and show an understanding of policing as a profession and of the laws and rules that shape policing and criminal justice.",
  when='a student asks what the degree is for, or a team sets the overall aims of the course',
  ask='Where in your work so far have you shown how the law shapes a policing decision?',
  bes='1.15, 2.2.b9 and 4.3.b2, and the FHEQ honours descriptor qaa/fheq-2024/4.15.b1')
s('1.12', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['develop'], about='communication and interpersonal skills', domain='generic-skill',
  para="In a safe space for trying out ideas and skills, students will develop effective communication and interpersonal skills, and many varied scenarios will ready them for what they meet as policing professionals.",
  prac="Give students a protected setting and a wide range of scenarios in which they will develop effective communication and interpersonal skills for professional policing.",
  ben="In a safe setting with many practice scenarios, you will develop the communication and people skills that policing work needs.",
  when='a student worries about speaking, interviewing or dealing with the public, or staff plan scenario-based teaching',
  ask='Which scenario so far tested your communication most, and what would you do differently next time?',
  bes='4.4.b2, qaa/fheq-2024/4.15.b8 and spine:6')
s('1.15', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='holders of a Policing degree', addressee='learner',
  verbs=['evaluate', 'reach', 'communicate', 'develop', 'establish'], about='judgement, evidence-informed decisions and linking theory to practice', domain='generic-skill',
  para="A Policing graduate will be able to weigh evidence, arguments and assumptions, judge soundly and convey those judgements well, and will have the qualities for work that calls for personal responsibility and decisions based on evidence in complex, unpredictable conditions; the graduate should also be able to build sound research, evidence-based techniques and problem-solving skills, and to connect theory with professional practice.",
  prac="Graduates will be able to evaluate evidence and argument, judge soundly, communicate well and decide responsibly on evidence in complex situations; they should also be able to use research, evidence-based practice and problem-solving at work and tie theory to practice.",
  ben="You will be able to weigh up evidence and arguments, reach sound judgements, explain them clearly and make responsible decisions based on evidence in complex situations, linking what you learn to policing practice.",
  when='a student asks what employers expect from a policing graduate, or a team writes programme-level outcomes',
  ask='Can you show a decision you made where the evidence was incomplete, and how you justified it?',
  bes='4.3.b13 and 4.4.b3, and qaa/fheq-2024/4.15.b7 and 4.15.b9.2')
prov('1.16', 'should', ['evidence'], 'a degree that excludes no group',
     para="The characteristics of a Policing degree should show a system that neither discriminates against, ranks nor shuts out any group on grounds of protected characteristics, socioeconomic background or location.",
     prac="Check admissions, curriculum, teaching and assessment so the degree should show no discrimination, stratification or exclusion by protected characteristic, social background or where students live.",
     when='a team reviews admissions, curriculum or assessment for fairness',
     ask="Which of the course's processes could disadvantage a student because of background or location?",
     bes='1.17, 1.19 and 1.20, and the equality theme in SB2')
prov('1.17', 'must', ['treated', 'consider', 'completing'], 'fair treatment and equality impact assessment',
     para="The subject's curriculum champions equality, diversity and inclusion; every student and stakeholder must be treated with openness, fairness, dignity and respect, and those designing courses should also consider an Equality Impact Assessment, done jointly with the force where a course is co-created.",
     prac="Treat every student and partner openly, fairly and with dignity: that is a must. Keep in view the Public Sector Equality Duty (Section 75 in Northern Ireland) and consider an Equality Impact Assessment, shared with the police force where you co-create the course.",
     when='a team designs a course, especially with a police force partner, or a student raises unfair treatment',
     ask='Has an Equality Impact Assessment been done for this course, and who took part in it?',
     bes='1.16, 1.18 and 3.2.b5, with the Equality Act 2010 as listed in SB6')
s('1.18', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='all students of Policing', addressee='both',
  verbs=['understand', 'embody'], about='ethics as the highest standard of conduct', domain='understanding',
  para="EDI should be real concepts built into the culture and practice of the subject, with ethics running through the curriculum; all Policing students must understand why ethics matter as the highest standards and carry their learning into practice by owning their professional conduct.",
  prac="Embed EDI in the culture and practice of the course, operational or not, with ethics as a thread throughout; every student must understand ethics as the top standard and carry it into daily conduct, taking responsibility for their own behaviour.",
  ben="You must understand why ethics sit at the heart of policing, put your learning into practice every day and take responsibility for behaving to the highest ethical standards.",
  when='a student faces an ethical dilemma on placement or in a scenario, or staff plan where ethics appears in each module',
  ask="What would you do if a colleague's conduct fell short of the standards you have learned?",
  bes='4.3.b7, 2.2.b1 and qaa/fheq-2024/annex-d/professional/r2/3rd')
prov('1.19', 'should', ['designed', 'planned'], 'inclusive and accessible teaching and assessment',
     para="The subject accepts that students learn in different ways and at different rates; inclusive teaching benefits everyone, and because variety alone may still exclude some, methods of teaching and assessment should be planned from the start to be inclusive and accessible.",
     prac="Design and plan teaching and assessment to be inclusive and accessible from the outset rather than adding variety later; varied styles on their own may still exclude some students.",
     when='a team designs modules or assessments, or asks why some groups do less well',
     ask='Which assessment in this module would be hardest for a student with a disability or caring duties, and why?',
     bes='1.20, 3.14.b9 and 3.15')
prov('1.20', 'must', ['demonstrate'], 'commitment to widening access',
     para="Those offering Policing must show their commitment to widening access and to every student reaching their potential, attending to physical and digital barriers as well as to how students best take in and use knowledge.",
     prac="Show, with evidence, a commitment to widening access: address physical access, digital divides (devices and connectivity) and the wider design of teaching so every student can reach their potential.",
     when='a team plans blended or online delivery or reviews widening access',
     ask='What evidence shows that students without reliable devices or connectivity can still take full part?',
     bes='1.19, 1.22 and 1.23.b1 to 1.23.b4')
prov('1.22', 'should', ['place'], 'flexible delivery and varied routes',
     para="Offering varied routes into police education widens participation; those offering the subject should stress flexible delivery so learning is accessible and the workforce recruited is more diverse and closer to the communities it serves.",
     prac="Stress flexible delivery and varied routes (work-based, knowledge-focused, graduate entry) so learning is accessible and recruits better reflect the communities they will serve.",
     when='a team weighs entry routes or modes of delivery',
     ask='Which entry route or mode of study would widen who can join this course?',
     bes='1.20, 1.4 (the three entry routes) and 2.13')
A123 = dict(appliesTo='students, through the accessible provision of the course')
prov('1.23.b1', 'should', ['access'], 'course support available online',
     para="Students should be able to reach course support online so they can work round illness, travel problems or caring duties.",
     prac="Put support material online so students can keep studying through illness, transport trouble or family and caring commitments.",
     when="a student's illness, travel or caring duties threaten their study",
     ask='Can a student who misses a session reach all of its support material online?',
     bes='1.20, 1.23.b2 to 1.23.b4 and the Accessibility Regulations 2018 listed in SB6', **A123)
prov('1.23.b2', 'should', ['keep'], 'pausing and replaying content',
     para="Students should be able to keep up with fast or complex content because they can pause, rewind and revisit it.",
     prac="Provide recorded or online content that students can pause, rewind and revisit to keep up with its pace and complexity.",
     when='content is delivered quickly or is technically dense',
     ask='Can students pause and replay the hardest parts of this module?',
     bes='1.23.b1, 1.23.b3 and 1.20', **A123)
prov('1.23.b3', 'should', ['review'], 'revisiting content before work-based assessment',
     para="Students should be able to go over course content repeatedly to deepen learning, above all before assessments in the workplace.",
     prac="Let students revisit content as often as they need, especially before assessments set in the workplace.",
     when='students prepare for assessments in the workplace',
     ask='How often can a student revisit content before a work-based assessment?',
     bes='1.23.b2, 3.11 and 3.14.b9', **A123)
prov('1.23.b4', 'should', ['reflect'], 'time to reflect before posting questions',
     para="Students should be able to reflect on content and research ideas before asking questions in a discussion forum, which suits those who need time to think or who are working in a second language.",
     prac="Where a forum exists, give students time to reflect before they post questions; this helps those who deliberate and those working in a second language.",
     when='a module uses online discussion',
     ask='Do quieter students, or those using a second language, get time to think before they post?',
     bes='1.19, 1.23.b3 and 3.15', **A123)
prov('1.26', 'should', ['designed'], 'designing programmes with the SDGs',
     find='Programmes should be designed with reference to the United Nations 17 sustainable development goals (SDGs) (United Nations, 2021) from which the following provide the opportunity to be explicitly placed within the Policing curricula:',
     para="Programmes should be designed with the UN's 17 Sustainable Development Goals in mind; the statement names eight themes from them that a Policing curriculum can take up explicitly, from wellbeing and inclusive education to safe communities, environmental impact, just societies and partnership.",
     prac="Design the programme with reference to the SDGs, placing the eight named themes (wellbeing, inclusive education, equity, economic vitality and skills, safe communities, environmental impact, access to justice, partnership) openly in the curriculum.",
     when='a team maps sustainability into modules',
     ask='Which of the eight SDG themes does each core module address, and where?',
     bes='1.24, 1.25, 4.4.b6 and the sustainability theme in SB2')
prov('1.27', 'should', ['inform'], 'future challenges in programme review',
     para="To keep the honours qualification current, present and coming challenges to policing and criminal justice should shape the regular review of programmes, so that graduates leave with up-to-date knowledge and skills.",
     prac="Feed current and emerging challenges (such as climate change, inequality and technological change, 1.28) into each programme review so content stays current.",
     when='a team plans periodic review or refreshes content',
     ask='Which emerging trend in policing changed this course at its last review?',
     bes='1.28, 1.29 and 3.17')

# ------------------------------------------------------------------ 2.2 outcome list (lead-in: programmes will enable graduates to)
def o22(k, verbs, about, domain, para, prac, ben, when, ask, bes):
    s('2.2.b%d' % k, type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
      verbs=verbs, about=about, domain=domain, para=para, prac=prac, ben=ben, when=when, ask=ask, bes=bes)


o22(1, ['comprehend'], 'the highest professional standards', 'understanding',
    "Graduates will grasp why lawful, ethical, safe and effective policing demands the highest professional standards.",
    "Programmes will enable graduates to comprehend why the highest professional standards govern lawful, ethical, safe and effective policing.",
    "You will understand why policing has to meet the highest professional standards to be lawful, ethical, safe and effective.",
    'a student asks why professional standards are taught so heavily', 'Where have you seen a professional standard change how a task was done?',
    '4.3.b3, 4.3.b7 and 3.2.b2')
o22(2, ['conduct'], 'evidence-based research', 'subject-skill',
    "Graduates will be able to carry out research grounded in evidence.",
    "Programmes will enable graduates to conduct research based on evidence.",
    "You will be able to carry out your own research based on evidence.",
    'a student begins research methods or the final project', 'What question about policing would you most like to research, and what evidence would answer it?',
    '2.14, 4.3.b11 and 4.4.b1')
o22(3, ['develop'], 'evidence-based policing and problem solving', 'understanding',
    "Graduates will come to understand evidence-based policing and problem-solving.",
    "Programmes will enable graduates to develop an understanding of evidence-based policing and of problem-solving.",
    "You will come to understand how evidence-based policing and problem-solving work.",
    'a student meets evidence-based policing for the first time', 'How would you test whether a policing tactic actually works?',
    '4.3.b11 and 4.3.b12')
o22(4, ['develop'], 'front-line policing areas', 'knowledge',
    "Graduates will gain knowledge of several areas of front-line professional policing.",
    "Programmes will enable graduates to develop knowledge of several front-line areas of professional policing.",
    "You will learn about several areas of front-line policing.",
    'a student chooses options or asks about front-line roles', 'Which front-line area do you know least about so far?',
    '4.3.b4 and 3.3')
o22(5, ['embed'], 'equality, diversity, inclusion and human rights', 'subject-skill',
    "Graduates will actively build equality, diversity, inclusivity and human rights into what they do.",
    "Programmes will enable graduates to embed equality, diversity, inclusion and human rights in their practice, actively and without waiting to be asked.",
    "You will actively build equality, diversity, inclusion and human rights into how you work.",
    'a scenario or placement raises fairness or rights', 'How did you take human rights into account in your last scenario exercise?',
    '4.3.b8, 3.2.b5 and 1.18')
o22(6, ['understand'], 'wellbeing and professional resilience', 'understanding',
    "Graduates will understand why wellbeing and professional resilience matter.",
    "Programmes will enable graduates to understand the importance of wellbeing and professional resilience.",
    "You will understand why looking after your wellbeing and resilience matters in policing.",
    'a student finds placement or study demanding', 'What helps you recover after a difficult shift or deadline?',
    '4.3.b17')
o22(7, ['understand'], 'digital policing and cyber-enabled crime', 'knowledge',
    "Graduates will understand digital policing and crime enabled by cyber means.",
    "Programmes will enable graduates to understand the ideas behind digital policing and cyber-enabled crime.",
    "You will understand how policing works in the digital world and how crime uses online tools.",
    'a student studies digital evidence or online crime', 'How would you explain cyber-enabled crime to a victim with no technical background?',
    '4.3.b6 and 4.4.b9')
o22(8, ['develop'], 'policing, criminal justice and criminology', 'knowledge',
    "Graduates will gain thorough knowledge of policing, criminal justice and criminology.",
    "Programmes will enable graduates to develop broad and thorough knowledge across policing, criminal justice and criminology.",
    "You will build a thorough knowledge of policing, criminal justice and criminology.",
    'a student asks how criminology modules fit the degree', 'Which criminological theory helps you most to explain a policing problem?',
    '4.3.b1 and qaa/fheq-2024/4.15.b1')
o22(9, ['understand'], 'the criminal justice system and policing', 'understanding',
    "Graduates will understand how the criminal justice system relates to policing.",
    "Programmes will enable graduates to understand the criminal justice system as it bears on policing.",
    "You will understand how policing fits into the wider criminal justice system.",
    'a student follows a case from arrest to court', 'What happens to a case after the police pass it on?',
    '1.10 and 4.3.b2')
o22(10, ['develop'], 'legislation, powers and policy in practice', 'knowledge',
    "Graduates will know legislation, police powers and policy and how they apply in professional practice.",
    "Programmes will enable graduates to develop knowledge of legislation, powers and policy and of their use in practice.",
    "You will know the laws, powers and policies that govern policing and how they are used in practice.",
    'a student is unsure which power applies in a scenario', 'Which power would you rely on here, and what limits it?',
    '4.3.b2 and 4.3.b14')
o22(11, ['recognise'], 'protecting people who are vulnerable or at risk', 'understanding',
    "Graduates will recognise that the police service has a basic duty to identify and professionally support people who are vulnerable or at risk.",
    "Programmes will enable graduates to recognise the service's core duty to identify and support vulnerable people and those at risk.",
    "You will recognise that a core duty of the police is to spot and support people who are vulnerable or at risk.",
    'a scenario involves a vulnerable person', 'What signs of vulnerability might be easy to miss in this situation?',
    '4.3.b9 and 3.3')
o22(12, ['select', 'apply'], 'specialist strategies for public protection', 'subject-skill',
    "Graduates will be able to choose and use suitable specialist strategies and techniques to support people who need public protection.",
    "Programmes will enable graduates to select and apply specialist strategies and techniques that protect people in need.",
    "You will be able to choose and use specialist strategies to protect and support people who need it.",
    'a student plans a response to a safeguarding case', 'Which strategy would you choose to protect this person, and why that one?',
    '4.3.b5 and 4.3.b9')
o22(13, ['develop'], 'national strategies such as counter terrorism', 'knowledge',
    "Graduates will know national policing strategies, counter terrorism among them.",
    "Programmes will enable graduates to develop knowledge of national policing strategies, for instance on counter terrorism.",
    "You will learn about national policing strategies, such as those on counter terrorism.",
    'a student asks how local policing links to national priorities', 'How does a national strategy show up in everyday local policing?',
    '4.3.b5 and 4.4.b5')

# ------------------------------------------------------------------ section 2, other statements
prov('2.3', 'should', ['planned', 'consider'], 'skills planned across all modules',
     para="Programme design should be planned as a whole to build, assess and strengthen graduate skills that transfer to policing and beyond; every module should take account of reflection, critical thinking, decisions, communication, ethics, EDI, evidence-based practice, problem solving, leadership and teamwork.",
     prac="Plan the programme as a whole: each module should attend to reflective practice, critical thinking, decision-making, communication, ethics, EDI, evidence-based practice, problem-solving, styles of leadership and teamwork.",
     when='a team maps skills across modules', ask='Which module builds leadership and teamwork, and how is it assessed?',
     bes='2.2, 4.4 and qaa/fheq-2024/4.15.b9.1')
prov('2.4', 'must', ['ensure', 'map'], 'the National Policing Curriculum in licensed programmes',
     para="For a programme seeking the professional body's licence, the design must build the College of Policing's National Policing Curriculum into the degree and map learning so every element is covered; licensed programmes are also reviewed regularly and yearly by the body.",
     prac="If you seek College of Policing licensing, you must build the NPC into the degree and map learning so every element appears in the design; expect regular and annual professional review.",
     when='a team plans to seek College of Policing licensing', ask='Where does the curriculum map show each NPC element taught and assessed?',
     bes='1.4, 3.11 and the College of Policing in SB5', xn='Do not extend it to Policing degrees that do not seek a licence.')
prov('2.6', 'should', ['represented'], 'volunteers in programme consultation',
     para="Staff associations matter for change across policing, and volunteers should also be formally represented when programmes are developed and reviewed, for example through students who volunteer as special constables.",
     prac="Formally involve volunteers, such as special constables and police support volunteers, in the consultations that develop and review the programme, alongside staff associations.",
     when='a team sets up programme consultation or review panels', ask='Who speaks for volunteers when this programme is reviewed?',
     bes='2.5, 2.7 and 2.20')
prov('2.9', 'must', ['mirror'], 'practitioner-researchers informing degree design',
     para="Current research in the discipline shapes how degrees are made and shows employers their worth; an evidence-based approach to creating degrees must follow other professions where experienced practitioner-researchers inform practice.",
     prac="When creating the degree, follow other professions in drawing on experienced practitioner-researchers; that evidence-based approach is a must and helps graduate skills transfer.",
     when='a team recruits staff or plans research-informed teaching', ask='Which practitioner-researchers shape the content of this degree?',
     bes='2.2.b2, 4.3.b11 and 3.13')
s('2.11', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours students', addressee='learner',
  verbs=['achieve', 'add'], about='joint honours students and the core skills', domain='subject-skill',
  para="Joint honours students will reach the core subject-specific and generic skills of Policing and add others from their second subject, and may explore where the two overlap.",
  prac="Joint honours students will achieve the core subject and generic skills of Policing, adding others from the partner subject; leave room to explore the overlap.",
  ben="If you study Policing with another subject, you will gain the core skills of Policing, add others from your second subject and can explore where the two meet.",
  when='a joint honours student asks what they must cover', ask='Which of the threshold skills does your Policing half cover, and which come from your other subject?',
  bes='4.3, 4.4 and 2.10')
s('2.14', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='final-year students on most policing, criminal justice and criminology programmes', addressee='learner',
  verbs=['design', 'undertake', 'complete'], about='the independent final-year project or dissertation', domain='subject-skill',
  para="In the last year of most programmes in policing, criminal justice or criminology, students must design, carry out and finish an independent problem-based project or dissertation, normally showing maturity, handling the practical, ethical and organisational sides of research, engaging critically with evidence, literature, law and policy, and linking research to practice and policy.",
  prac="Require a final-year independent project or dissertation that each student must design, conduct and complete, in which they normally show mature research judgement, critical use of evidence, law and policy, and links to practice.",
  ben="In your final year you must design, carry out and complete your own research project or dissertation, dealing with its practical and ethical sides and linking research to policing practice and policy.",
  when='a student plans the final-year project', ask='What policing problem will your project tackle, and what ethical or access issues must you settle first?',
  bes='2.2.b2, 4.4.b1 and qaa/fheq-2024/4.15.b6')
prov('2.16', 'should', ['provides'], 'an institutional strategy for partnerships',
     para="There should be a clear institutional strategy for partnership with other agencies that guides anyone entering such arrangements, which may cover whole courses or parts such as placements and may call for other sites, support or facilities.",
     prac="Set a clear institutional strategy for partnerships with agencies, covering whole courses or parts such as work placements, and plan for the sites, support and facilities they need.",
     when='a team plans a partnership or work placements', ask='Which institutional strategy governs this partnership, and does it cover placements?',
     bes='2.15, 2.17 to 2.19 and the QAA work-based learning guidance in SB6')
prov('2.17', 'must', ['meet', 'ensure'], 'partners and the national qualifications framework',
     para="Partners co-creating or delivering policing awards must satisfy the national qualifications framework that applies, and the awarding organisation should be responsible for making sure the standards are met.",
     prac="Partners must meet the relevant national qualifications framework (FHEQ or FQHEIS); the awarding organisation should carry the responsibility for assuring the standards.",
     when='a team sets up co-created delivery with a police force', ask='How does the awarding body check that partner-delivered modules meet honours level?',
     bes='2.18, 2.19 and ' + FW6)
prov('2.18', 'must', ['ensure'], 'standards and student experience in partnerships',
     para="The awarding body must make arrangements to keep the academic standard of the policing award; partnership input should also enrich the student experience, and where other agencies deliver some or all of the course there should be an effective process for managing and overseeing that experience.",
     prac="As awarding body you must have arrangements that hold the academic standard of the award; where agencies deliver part or all of the course, run an effective process to manage and oversee the whole student experience.",
     when='another agency delivers part of the course', ask='Who oversees the student experience on the modules a partner delivers?',
     bes='2.17, 2.19 and 2.21')
prov('2.19', 'should', ['include'], 'written partnership agreements and due diligence',
     para="Partnerships for police qualifications should rest on legally binding written agreements setting out detailed arrangements and risks, with due diligence during the partnership and before renewal, governance recorded and kept current, and continuous monitoring by the awarding institution.",
     prac="Put each partnership on a legally binding written agreement that sets out arrangements and risks; carry out due diligence during it and before renewal; keep governance records current and monitor continuously.",
     when='a partnership is agreed or comes up for renewal', ask='When was due diligence last done on this partnership, and what did it find?',
     bes='2.16, 2.17 and 2.18')

# ------------------------------------------------------------------ 3.2 core themes (lead-in: content should be)
def c32(k, verbs, about, para, prac, ask, bes):
    prov('3.2.b%d' % k, 'should', verbs, about, para=para, prac=prac, ask=ask, bes=bes,
         when='a team checks core content against the five themes',
         ben=('n/a', 'a duty on course design; the student outcomes it serves are in 4.3'))


c32(1, ['designed', 'understand', 'upholding', 'making'], 'impartiality',
    "Impartiality: the course should be designed so that students understand the context of the profession, uphold its standards and decide on objective grounds free of bias.",
    "Design the course so students learn to uphold professional standards and to decide on objective, impartial grounds, without bias or prejudice.",
    'Where does the course make students test their own decisions for bias?', '4.3.b7 and 4.3.b14')
c32(2, ['reflect'], 'integrity',
    "Integrity: course content should reflect the highest standards expected of people in policing, including acting as a role model.",
    "Make content reflect the highest standards expected of people in policing, including being a role model.",
    'Which module asks students to consider what being a role model means?', '1.18 and 4.3.b7')
c32(3, ['reflect', 'act'], 'public service',
    "Public service: course content should reflect that people in policing are responsible for acting in the best interests of society as a whole.",
    "Make content show that people in policing carry a responsibility to act in the best interests of society as a whole.",
    'How does the course show the tension between public service and other pressures?', '1.1 and 2.2.b11')
c32(4, ['designed', 'understand'], 'transparency',
    "Transparency: policing awards should be designed so students understand why those working or volunteering in policing need to be open in their actions, decisions and communications.",
    "Design the award so students see why openness in actions, decisions and communication is needed of everyone working or volunteering in policing.",
    'Where do students practise explaining a decision openly to the public?', '4.3.b7 and 4.4.b2')
c32(5, ['designed', 'include', 'understand', 'champion'], 'diversity',
    "Diversity: policing awards should be designed so students understand and champion equality, diversity and inclusion in society.",
    "Design the award so students both understand equality, diversity and inclusion and champion them in society.",
    'How does the course prepare students to champion inclusion, not only describe it?', '2.2.b5 and 4.3.b8')

# ------------------------------------------------------------------ section 3, assessment
prov('3.11', 'must', ['require', 'integrate', 'map'], 'assessment in licensed PEQF programmes',
     para="How a Policing degree is assessed depends partly on whether it is a licensed PEQF programme; licensed programmes require assessment that blends theory with the applied outcomes, ties to the workplace and the NPC and meets the academic provider's needs, and where it applies such assessment should map theory to practice as new constables also reach Independent Patrol Status and Full Occupational Competence.",
     prac="For licensed PEQF programmes (PCDA, DHEP) assessment is required to blend theory with application, reflect the student's own policing setting, link to the NPC and meet the academic awarding body's rules; it should map theory to practice alongside IPS and FOC.",
     when='a team designs assessment for a PCDA or DHEP', ask='How does each assessment show progress towards Independent Patrol Status as well as academic credit?',
     bes='2.4, 3.12 and 3.13', xn='Do not apply it to unlicensed degrees, which may not assess practical policing skills (3.12).')
prov('3.13', 'should', ['focus', 'provide', 'test'], 'applied assessment blending theory and practice',
     para="Academic and practical skills complement each other, so every Policing assessment, licensed or not, should centre on applied learning, let students show grounded theory and practice, test a mix of study and workforce-relevant skills, and give all students the chance to explore contemporary policing critically.",
     prac="Make every assessment applied: blend theory and practice, test academic and workforce-relevant skills together, and let all students explore contemporary policing critically, with debate and current research behind their learning.",
     when='a team reviews whether assessments are applied enough', ask='Which assessment in this module asks students to apply theory to a real policing problem?',
     bes='3.14.b1 to 3.14.b10, 3.15 and 4.3.b11')
prov('3.14', 'must', ['demonstrate', 'provide'], 'co-designed assessment and an assessment strategy',
     find='All providers of degrees in Policing must be able to demonstrate that assessments have been co-designed with either policing practitioners or other employers to ensure that assessments are designed with a practice-based focus to enhance student employability. All degrees must provide an assessment strategy that enables students to demonstrate that they have achieved an appropriate level in the required areas of the degree programme and to facilitate learning.',
     para="Every provider of a Policing degree must be able to show that assessments were co-designed with police practitioners or other employers for a practice focus that helps employability, and every degree must have an assessment strategy that lets students show they have reached the right level and that supports learning.",
     prac="Co-design assessments with police practitioners or other employers and keep the evidence: that is a must. Have an assessment strategy that shows students reaching the required level and supports their learning.",
     when='a team plans or revalidates its assessment strategy', ask='Which employer helped design this assessment, and what record shows it?',
     bes='3.14.b1 to 3.14.b10, 3.16 and 2.5')


def a314(k, force, verbs, about, para, prac, ask, bes):
    prov('3.14.b%d' % k, force, verbs, about, para=para, prac=prac, ask=ask, bes=bes,
         when='a team checks its assessment strategy against the principles and safeguards')


a314(1, 'should', ['link'], 'assessment aligned to outcomes',
     "Assessments should tie straight to the module's and the course's learning outcomes.",
     "Align each assessment directly with the module and course learning outcomes.",
     'Which learning outcome does this assessment test, and is any outcome left untested?', '3.14.b2 and 3.14.b3')
a314(2, 'should', ['measure'], 'measuring knowledge, understanding and skills',
     "Assessments should measure what students have learned: knowledge gained, understanding built and skills or abilities acquired.",
     "Make assessments measure the knowledge, understanding and skills students have actually gained.",
     'What does this assessment tell you about a student\'s skills, not only their knowledge?', '4.3 and 4.4')
a314(3, 'should', ['assessed'], 'assessing the central aspects of outcomes',
     "Students should be assessed on the central parts of the learning outcomes, on what is taught and learned.",
     "Assess students on the core of the learning outcomes and on what the course actually teaches.",
     'Does this assessment test something the module never taught?', '3.14.b1')
a314(4, 'should', [], 'consistent workload and credit',
     "Assessment workload should be consistent and fair relative to credit value.",
     "Keep assessment workload consistent and fair across modules of the same credit value.",
     'Do two modules of equal credit ask for very different amounts of assessed work?', '3.14.b5')
a314(5, 'should', ['facilitate'], 'progression across modules and levels',
     "Assessments should support a path of progressive development for students across modules and levels.",
     "Sequence assessments so they build students' development from module to module and level to level.",
     'How does the final-year assessment build on what was assessed in earlier years?', '2.10 and spine:6')
a314(6, 'should', ['emphasise'], 'deep, active, reflective learning',
     "Assessments should stress deep, active and reflective learning.",
     "Set assessments that reward deep, active and reflective learning rather than recall.",
     'Could a student pass this assessment by memorising alone?', '3.15 and 4.3.b18')
a314(7, 'should', ['improve'], 'assessment that improves learning',
     "Assessments should actively and constructively improve how students learn.",
     "Use assessment to improve student learning, not only to grade it.",
     'What does a student learn from doing this assessment, beyond the mark?', '3.14.b10 and 3.16')
a314(8, 'should', ['focus'], 'skills and their transfer',
     "Assessments should centre on skills and on their transfer.",
     "Assess skills and whether students can carry them into new settings.",
     'Where does an assessment ask students to use a skill in a new setting?', '4.4.b8 and 3.13')
a314(9, 'must', ['ensure', 'accommodated'], 'inclusive assessment',
     "Assessments must put inclusivity at their core so all students' ways of learning are catered for and experience is equal.",
     "Build inclusion into the core of every assessment so all learning styles are met and students have a comparable experience: a must.",
     'Which students might this assessment disadvantage, and what is the alternative?', '1.19 and 3.15')
a314(10, 'must', ['demonstrate'], 'timely, detailed feedback',
     "Assessment strategies must show that every student gets timely, detailed and relevant feedback.",
     "Show in the assessment strategy that every student receives timely, detailed and relevant feedback: a must.",
     'How long do students wait for feedback, and can they use it before the next assessment?', '3.16 and 3.14.b7')
prov('3.15', 'should', ['use', 'show'], 'varied, participative and inclusive assessment',
     para="Those offering the degree should aim for a mix of assessments and new methods that draw students into active participation and critical reflection, with chances to show skills in writing, speech and visual form, alone and in groups and through independent research; they should show how student voice shapes the design of assessment and that inclusive assessment is considered.",
     prac="Use varied and innovative assessment (written, oral, visual; individual and group; independent research), show how student voice informs its design, and build in constructive alignment, clear criteria, timeliness, adaptability and constructive feedback.",
     when='a team redesigns assessment or gathers student views', ask="How did students' views shape the assessments in this programme?",
     bes='3.14.b9, 3.16 and 1.19')
prov('3.16', 'must', ['given'], 'full assessment information and a balance of methods',
     para="Throughout the course students must receive full details of each assessment and the criteria or rubric used; there should be a fitting balance of diagnostic, formative and summative methods and chances in class or online to tackle challenging questions; applied assessment may take forms such as reflective writing, policy briefs, case studies, presentations or digital portfolios.",
     prac="Give students full details of every assessment and its criteria or rubric (a must); balance diagnostic, formative and summative assessment; give practice with challenging questions; consider applied forms such as policy briefs and digital portfolios.",
     when='a student is unsure how they will be assessed, or a team writes module guides', ask='Where can a student find the full brief and rubric for each assessment?',
     bes='3.14.b10, 3.15 and 3.17')
prov('3.17', 'should', ['reviewed'], 'reviewing assessments for currency and integrity',
     para="Assessments should be reviewed regularly to keep them current and valid and to reduce risks to academic integrity.",
     prac="Review assessments on a regular cycle so they stay current and valid and give little room for academic misconduct.",
     when='a team runs its annual review or meets an integrity concern', ask='When was this assessment last reviewed, and what changed?',
     bes='1.27, 2.20 and 3.14')
prov('4.2', 'should', ['refer'], 'Annex D for achievement above the threshold',
     para="Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, which describes the four honours classes (1st, 2:1, 2:2 and 3rd) for honours at FHEQ level 6 and FQHEIS level 10.",
     prac="Decide what evidence shows achievement above the threshold, and use the Annex D descriptions of the four honours classes when you judge it.",
     when='a team sets marking criteria or a student asks what a good degree looks like', ask='How do your marking criteria separate a 2:1 from a 2:2 in this module?',
     bes='4.1, 4.3, 4.4 and the Annex D bands (qaa/fheq-2024/annex-d; SL6 of std:doc:qaa-fheq-2024-framework)',
     ben=('n/a', 'tells the course how to judge achievement above the threshold; the student-facing standards are 4.3 and 4.4'))
P['4.2']['level'] = 'fheq:6'

# ------------------------------------------------------------------ threshold rung: 4.3 subject, 4.4 generic (lead-in: should be able to; 4.1 defines the minimum)
def th(n, k, verbs, about, domain, para, prac, ben, when, ask, bes):
    s('%s.b%d' % (n, k), type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6',
      appliesTo='honours graduates at the threshold level', addressee='learner', verbs=verbs, about=about, domain=domain,
      para=para, prac=prac, ben='At the threshold, ' + ben, when=when, ask=ask, bes=bes)


th('4.3', 1, ['apply'], 'the interdisciplinary nature of policing', 'understanding',
   "At threshold, applies a deep understanding of how policing, criminal justice and criminology connect to present or future professional duties.",
   "At threshold, graduates apply an in-depth grasp of how policing, criminal justice and criminology interlock to their professional responsibilities, now or later.",
   "you can apply a deep understanding of how policing, criminal justice and criminology fit together to your current or future work.",
   'a student asks how criminology modules connect to policing work', 'Can you show how a criminological idea changed how you would handle a policing task?',
   '2.2.b8 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)')
th('4.3', 2, ['understand', 'evaluate'], 'criminal law applied to policing', 'understanding',
   "At threshold, understands and judges how criminal law is applied in policing.",
   "At threshold, graduates understand and evaluate the way criminal law is applied to policing.",
   "you understand how criminal law is applied in policing and can judge how well it is applied.",
   'a student studies powers, offences or case law', 'In this case, was the law applied well, and how would you judge it?',
   '2.2.b10 and qaa/fheq-2024/4.15.b7')
th('4.3', 3, ['apply'], 'safe, lawful and effective policing', 'knowledge',
   "At threshold, applies thorough knowledge and understanding of policing that is safe, lawful and effective.",
   "At threshold, graduates bring a deep knowledge of what makes policing safe, lawful and effective to bear on practice.",
   "you can use detailed knowledge of what makes policing safe, lawful and effective.",
   'a student reviews an incident or scenario', 'What made this response safe, lawful and effective, or not?',
   '2.2.b1 and qaa/fheq-2024/4.15.b1')
th('4.3', 4, ['understand'], 'policing specialisms', 'knowledge',
   "At threshold, understands several specialisms within policing, for example response, community and roads policing, intelligence and investigation.",
   "At threshold, graduates understand several policing specialisms, for example response, neighbourhood, roads, intelligence and investigation.",
   "you understand several policing specialisms, such as response, community and roads policing, intelligence and investigation.",
   'a student considers which area of policing to work in', 'Which specialism could you explain to a new recruit, and which could you not yet?',
   '2.2.b4 and 3.3')
th('4.3', 5, ['select', 'apply'], 'choosing strategies for complex contexts', 'subject-skill',
   "At threshold, chooses and uses suitable current policing strategies in complex, interrelated contexts.",
   "At threshold, graduates select and apply fitting contemporary policing strategies to complex, interconnected situations.",
   "you can choose and use suitable modern policing strategies in complex situations where many factors interact.",
   'a student plans a response to a complex scenario', 'Why did you choose that strategy over the alternatives here?',
   '2.2.b12 and qaa/fheq-2024/4.15.b9.2')
th('4.3', 6, ['apply'], 'digital policing and technology-related crime', 'knowledge',
   "At threshold, applies broad knowledge and understanding of digital policing and crime involving technology.",
   "At threshold, graduates apply broad knowledge of digital policing and of crime that involves technology.",
   "you can use a broad knowledge of digital policing and of crime that involves technology.",
   'a student meets digital evidence or online offending', 'What digital evidence would you look for in this case, and how would you secure it?',
   '2.2.b7 and 4.4.b9')
th('4.3', 7, ['understand', 'adopt'], 'an ethical approach and professional values', 'understanding',
   "At threshold, understands and takes an ethical approach in line with the police service's highest professional values and standards.",
   "At threshold, graduates understand and adopt an ethical stance matching the service's highest professional values and standards.",
   "you understand and take an ethical approach that matches the highest professional values of the police service.",
   'a student faces an ethical dilemma or discusses misconduct', 'Which professional value guided your choice here?',
   '1.18, 3.2.b2 and qaa/fheq-2024/annex-d/professional/r2/3rd')
th('4.3', 8, ['take'], 'promoting equality, diversity, inclusion and human rights', 'subject-skill',
   "At threshold, takes personal responsibility for advancing equality, diversity, inclusivity and human rights.",
   "At threshold, graduates take personal responsibility for promoting equality, diversity, inclusion and human rights.",
   "you take personal responsibility for promoting equality, diversity, inclusion and human rights.",
   'a scenario raises fairness, bias or rights', 'What did you personally do in that situation to protect someone\'s rights?',
   '2.2.b5, 3.2.b5 and 4.4.b6')
th('4.3', 9, ['synthesise'], 'supporting victims, witnesses and the vulnerable', 'subject-skill',
   "At threshold, brings together specialist current theories, ideas and methods that can be used to support victims, witnesses, vulnerable people and those at risk.",
   "At threshold, graduates synthesise specialist, interconnected theories and methods for supporting victims, witnesses and people who are vulnerable or at risk.",
   "you can combine specialist theories and methods to support victims, witnesses and people who are vulnerable or at risk.",
   'a student works on a victim or safeguarding case', 'Which ideas did you draw together to decide how to support this person?',
   '2.2.b11 and qaa/fheq-2024/4.15.b3.1')
th('4.3', 10, ['adopt'], 'preventing and detecting crime; suspects and offenders', 'subject-skill',
   "At threshold, uses specialist current theories and methods to prevent crime, detect it, and deal with suspects and offenders.",
   "At threshold, graduates adopt specialist, interconnected theories and methods to prevent and detect crime and to handle suspects and offenders.",
   "you can use specialist theories and methods to prevent and detect crime and to deal with suspects and offenders.",
   'a student plans an investigation or crime prevention measure', 'What theory supports the prevention approach you chose?',
   '4.3.b9 and 2.2.b10')
th('4.3', 11, ['evaluate', 'apply'], 'evidence-based research in policing', 'subject-skill',
   "At threshold, critically judges evidence-based research and applies it to the complexities of policing.",
   "At threshold, graduates critically evaluate evidence-based research and apply it to complex policing problems.",
   "you can critically judge research evidence and use it on complex policing problems.",
   'a student cites research in an assignment or proposes a change in practice', 'How strong is the evidence behind that study, and does it fit this setting?',
   '2.2.b2, 2.2.b3 and qaa/fheq-2024/4.15.b3.2')
th('4.3', 12, ['select', 'apply'], 'problem solving with evidence', 'subject-skill',
   "At threshold, chooses and uses specialist strategies, methods and research evidence to solve complex problems.",
   "At threshold, graduates select and apply specialist strategies, methods and research evidence to complex problem solving.",
   "you can choose and use specialist methods and research evidence to work through complex problems.",
   'a student tackles a recurring local problem', 'What evidence told you this approach would solve the problem?',
   '2.2.b3 and qaa/fheq-2024/4.15.b7')
th('4.3', 13, ['make'], 'informed decisions in complex situations', 'subject-skill',
   "At threshold, makes informed decisions in complex, unpredictable and interrelated situations, based on critical thinking and evidence.",
   "At threshold, graduates make informed decisions in complex, unpredictable, interconnected situations, grounded in critical thinking and evidence.",
   "you can make informed decisions in complex and unpredictable situations, based on critical thinking and evidence.",
   'a student reflects on a decision under pressure', 'What did you know, and not know, when you made that decision?',
   '1.15 and qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2)')
th('4.3', 14, ['act', 'apply'], 'guidelines and professional discretion', 'subject-skill',
   "At threshold, works within chosen guidelines and uses professional discretion.",
   "At threshold, graduates act within selected guidelines and exercise professional discretion.",
   "you can work within the relevant guidelines and use professional discretion well.",
   'a scenario leaves room for discretion', 'Where did the guidance stop, and how did you use your discretion?',
   '3.2.b1 and qaa/fheq-2024/annex-d/professional/r2/3rd')
th('4.3', 15, ['understand', 'apply'], 'conflict management', 'subject-skill',
   "At threshold, understands and uses conflict management skills.",
   "At threshold, graduates understand and apply the skills of managing conflict.",
   "you understand and can use the skills of managing conflict.",
   'a student prepares for or debriefs a confrontation', 'What did you do to calm that situation, and what would you change?',
   '1.12 and 4.4.b2')
th('4.3', 16, ['apply'], 'leadership, teams and partnership working', 'understanding',
   "At threshold, applies a deep understanding of leadership, teamwork and working in partnership.",
   "At threshold, graduates apply an in-depth understanding of leadership, team working and partnership working.",
   "you can use a deep understanding of leadership, teamwork and working with partner agencies.",
   'a student leads a group task or works with another agency', 'What kind of leadership did that task need, and did you provide it?',
   '2.3 and 4.4.b4')
th('4.3', 17, ['understand', 'apply'], 'wellbeing and resilience of self and others', 'subject-skill',
   "At threshold, understands and uses techniques that protect their own and others' wellbeing and resilience in every situation.",
   "At threshold, graduates understand and apply techniques that keep themselves and others well and resilient in all situations.",
   "you understand and use techniques to look after your own and others' wellbeing and resilience in any situation.",
   'a student is under strain or supports a struggling peer', 'What do you do to look after yourself and others after a hard day?',
   '2.2.b6')
th('4.3', 18, ['engage'], 'continual self-reflection to improve practice', 'subject-skill',
   "At threshold, reflects on self actively and continually, developing ways to improve own practice.",
   "At threshold, graduates engage actively in continual self-reflection and develop strategies to improve their practice.",
   "you reflect on your own work actively and continually and find ways to improve it.",
   'a student writes a reflective account or debriefs a placement', 'What will you do differently next time, and why?',
   '4.4.b10 and qaa/fheq-2024/annex-d/transferable/r5/3rd')

th('4.4', 1, ['deploy'], 'research design, collection, analysis and interpretation', 'generic-skill',
   "At threshold, uses a range of established techniques accurately to design research and to collect, analyse and interpret data.",
   "At threshold, graduates accurately deploy established techniques to design research and to gather, analyse and interpret its data.",
   "you can use established research techniques accurately to design a study and to gather, analyse and interpret data.",
   'a student plans research methods or analyses data', 'Why is that method the right one for your question?',
   'qaa/fheq-2024/4.15.b2 (qaa/fqheis-2024/4.16.b4) and 2.14')
th('4.4', 2, ['organise', 'communicate'], 'communicating to specialist and lay audiences', 'generic-skill',
   "At threshold, organises and conveys connected information for specialist and non-specialist audiences.",
   "At threshold, graduates organise and communicate interconnected information to specialist and lay audiences.",
   "you can organise connected information and explain it to experts and to people outside policing.",
   'a student prepares a briefing, report or presentation', 'How would you change this briefing for a community meeting rather than a senior officer?',
   'qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) and 1.12')
th('4.4', 3, ['evaluate', 'identify'], 'critical evaluation to find solutions', 'generic-skill',
   "At threshold, critically judges arguments, assumptions and abstract ideas to find possible solutions.",
   "At threshold, graduates critically evaluate arguments, assumptions and abstract concepts to find possible solutions.",
   "you can critically judge arguments, assumptions and abstract ideas to find possible solutions.",
   'a student weighs competing arguments', 'What assumption sits beneath that argument, and does it hold?',
   'qaa/fheq-2024/4.15.b7 and 4.3.b12')
th('4.4', 4, ['act', 'take'], 'autonomy and responsibility in complex contexts', 'generic-skill',
   "At threshold, works independently and takes responsibility for personal or group tasks in complex settings.",
   "At threshold, graduates act autonomously and take responsibility for individual or group tasks in complex settings.",
   "you can work on your own initiative and take responsibility for your own and group tasks in complex settings.",
   'a student manages a group project or independent task', 'What did you take responsibility for in that task, without being told?',
   'qaa/fheq-2024/4.15.b9.1 and 4.15.b9.2, and spine:6')
th('4.4', 5, ['appreciate'], 'political, economic, social, technological, environmental, legal and ethical debates', 'generic-skill',
   "At threshold, appreciates today's debates affecting the discipline, whether political, economic, social, technological, environmental, legal or ethical.",
   "At threshold, graduates appreciate the live political, economic, social, technological, environmental, legal and ethical debates that shape policing as a discipline.",
   "you understand today's debates that affect policing, whether political, economic, social, technological, environmental, legal or ethical.",
   'a student discusses current affairs or policy change', 'Which current debate do you think will most change policing in five years?',
   '3.1 and qaa/fheq-2024/4.15.b4')
th('4.4', 6, ['understand'], 'debates on EDI and sustainability', 'generic-skill',
   "At threshold, understands current debates on equality, diversity, inclusion and sustainability.",
   "At threshold, graduates understand contemporary debates on equality, diversity, inclusion and sustainability.",
   "you understand current debates about equality, diversity, inclusion and sustainability.",
   'a student meets a debate about fairness or sustainability in policing', 'What are the strongest arguments on each side of that debate?',
   '4.3.b8, 1.26 and the themes in SB2')
th('4.4', 7, ['understand'], 'culture and working practices', 'generic-skill',
   "At threshold, understands how culture affects ways of working.",
   "At threshold, graduates understand the effect of culture on working practices.",
   "you understand how culture shapes the way people work.",
   'a student reflects on workplace culture on placement', 'How did the culture of the team you worked with shape what people did?',
   '2.5 and 2.7')
th('4.4', 8, ['apply'], 'innovative methods in employment', 'generic-skill',
   "At threshold, uses at work a range of innovative methods and techniques learned on the course.",
   "At threshold, graduates apply a range of innovative methods and techniques they have learned to employment.",
   "you can use a range of new methods and techniques you have learned in your work.",
   'a student links coursework to a job or placement', 'Which method from your course have you used at work, and how did it go?',
   'qaa/fheq-2024/4.15.b6 and 4.15.b9.3')
th('4.4', 9, ['select', 'apply'], 'digital skills at work', 'generic-skill',
   "At threshold, chooses and uses a range of digital skills and techniques at work.",
   "At threshold, graduates choose and use a range of digital skills and techniques at work.",
   "you can choose and use a range of digital skills and tools at work.",
   'a student uses digital systems on placement or in study', 'Which digital tool do you rely on, and which would you like to learn?',
   '4.3.b6 and qaa/fheq-2024/annex-d/transferable/r1/3rd')
th('4.4', 10, ['engage', 'identify', 'address'], 'self-reflection on learning needs', 'generic-skill',
   "At threshold, reflects actively on self to find and meet own learning needs.",
   "At threshold, graduates engage actively in self-reflection to identify and address their own learning needs.",
   "you reflect actively on yourself to spot and meet your own learning needs.",
   'a student plans their personal development', 'What is the one thing you most need to learn next, and how will you learn it?',
   '4.3.b18 and qaa/fheq-2024/4.15.b5')
th('4.4', 11, ['understand'], 'continuing professional development', 'generic-skill',
   "At threshold, understands why continuing professional development matters.",
   "At threshold, graduates understand the importance of engaging in continuing professional development.",
   "you understand why it matters to keep developing professionally throughout your career.",
   'a student asks about life after graduation', 'How will you keep your knowledge current after you graduate?',
   'qaa/fheq-2024/4.15.b9.3 and 1.29')

# ------------------------------------------------------------------ compose the agent instructions
for _i, _r in P.items():
    _r['aaw'] = aaw_of(_i, _r)
    _r['aad'] = aad_of(_i, _r)

GRADE = {}
TH = {'1.17': 'theme:edi', '1.18': 'theme:edi', '1.19': 'theme:edi, theme:accessibility', '1.20': 'theme:accessibility',
      '1.22': 'theme:accessibility', '1.23.b1': 'theme:accessibility', '1.23.b2': 'theme:accessibility', '1.23.b3': 'theme:accessibility',
      '1.23.b4': 'theme:accessibility', '1.26': 'theme:esd'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 1.4; 1.13; 1.24; 1.27; 2.10; 4.2'),
                  dict(id='fqheis:10', role='cites', locator='D1, 1.4; 1.13; 1.24; 1.27; 2.10; 4.2')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis="stated (D1, 1.13: constable capabilities align to Level 6 (FHEQ) and Level 10 (FQHEIS); 2.10: a degree with honours at both)")])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.16', '1.17', '1.18', '1.19', '2.2', '2.3', '3.2', '3.3', '3.14', '3.15', '4.3', '4.4']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.19', '1.20', '1.21', '1.22', '1.23']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.24', '1.25', '1.26', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.26', '2.6', '2.16', '3.14'])]
S7 = [dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='Level 6 (1.4, 1.13, 1.24, 1.27, 2.10)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='Level 10 (1.4, 1.13, 1.24, 1.27, 2.10)'),
      dict(rel='refersTo', target='College of Policing: PEQF and the National Policing Curriculum (not yet ingested; Part E)', note='1.4, 2.4, 3.11'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance: Work-based Learning (2018) (not yet ingested)', note='front matter; 2.8; 2.16'),
      dict(rel='overlaps', target='std:doc:qaa-criminology-2022-benchmarks', note='inferred, not cited: shared ground in criminology and criminal justice (2.2.b8, 4.3.b1)')]
SB1 = [
    "Policing education serves a profession whose stated mission is safer communities through fair and firm law enforcement, crime prevention, keeping the peace, protection and bringing offenders to justice (D1, 1.1).",
    "It is professional education, shaped by a national drive to recognise policing as a profession, with the College of Policing setting standards in England and Wales (D1, 1.2, 1.3).",
    "Its routes differ by nation: three licensed PEQF entry routes in England and Wales, no higher education entry route in Scotland, and a PSNI degree in Northern Ireland; unlicensed degrees still have value (D1, 1.4 to 1.8).",
    "Theory underpins applied practice: critical thinking, analysis and reflective learning through a curriculum that integrates theory and practice (D1, 1.9, 1.11).",
    "Ethics and the Code of Ethics, the Peelian Principles and the Competency Values Framework are foundations of the learning (D1, 1.14, 1.18).",
    "Evidence-based policing, problem-solving and research by practitioner-researchers are central (D1, 1.15, 2.2, 2.9).",
    "Employers and the professional body are closely involved, sometimes co-creating the degree with a police force (D1, 2.5 to 2.8, 3.14).",
    "Teaching has moved from teacher-centred to learner-centred, experiential and co-produced learning (D1, 3.4 to 3.10).",
]
SB2 = [dict(theme='theme:edi', inThisSubject='EDI is set at the core of the curriculum with ethics as a common thread; all students and stakeholders are to be treated fairly under the Public Sector Equality Duty, and students are to promote EDI and human rights in practice (D1, 1.16 to 1.19, 2.2, 3.2, 4.3)',
            statements=['1.16', '1.17', '1.18', '1.19', '2.2.b5', '3.2.b5', '3.14.b9', '4.3.b8', '4.4.b6']),
       dict(theme='theme:accessibility', inThisSubject='widening access across physical and digital barriers, varied entry routes and flexible delivery, the 2018 accessibility regulations, and online provision suited to students with shift work, caring duties or a second language (D1, 1.19 to 1.23)',
            statements=['1.19', '1.20', '1.22', '1.23.b1', '1.23.b2', '1.23.b3', '1.23.b4']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability, beside horizon scanning: programmes designed with the SDGs, with eight themes named for the Policing curriculum, including the environmental impact of policing and access to justice (D1, 1.24 to 1.26)',
            statements=['1.26', '4.4.b6']),
       dict(theme='theme:enterprise', inThisSubject='named as employability in the front matter: assessment co-designed with employers to enhance employability, the value of work-based learning, and job market skills among the SDG themes (D1, front matter, 1.26, 2.16, 3.14)',
            statements=['2.16', '3.14'])]
SB3 = dict(areas=[dict(component='3.1', gloss='a changing subject responding to political, economic, social, technological, environmental and ethical change'),
                  dict(component='3.2', gloss='five core themes: impartiality, integrity, public service, transparency, diversity'),
                  dict(component='3.3', gloss='sixteen indicative topics, from operational policing and investigation to cyber crime, intelligence and public protection')],
           practices=[dict(component='2.13', kind='teaching', gloss='varied methods; classroom, work-based and field-based learning; independent learning'),
                      dict(component='2.14', kind='learning', gloss='final-year independent problem-based project or dissertation'),
                      dict(component='3.4', kind='teaching', gloss='a shift to learner-centred police education'),
                      dict(component='3.5', kind='learning', gloss='student-centred and experiential learning cycles'),
                      dict(component='3.6', kind='teaching', gloss='the Student as Producer model and collaborative teaching'),
                      dict(component='3.13', kind='assessment', gloss='applied assessment blending theory and practice'),
                      dict(component='3.15', kind='assessment', gloss='varied, innovative and inclusive forms with student voice'),
                      dict(component='3.16', kind='assessment', gloss='full information, balanced diagnostic, formative and summative methods, applied forms')])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.3 and 4.4 (heading: Threshold level)', award=HON, items=29)],
           rungBases='4.1 defines the threshold as the minimum an honours graduate will have shown; 4.2 says most students perform well above it and sends the classes above it to Annex D. No typical or excellent rung is stated.',
           outcomeLists=[dict(leadIn='2.2', gloss='what programmes will enable graduates to do', items=13, award=['honours'])],
           outcomes=[])
SB4A_FULL = []
SB5 = [dict(body='College of Policing', says='the professional body for policing in England and Wales, an arm\'s-length body of the Home Office; partner in writing and reviewing the statement; sets the PEQF, licenses programmes that follow the National Policing Curriculum and reviews them; its Code of Ethics underpins the learning (D1, front matter, 1.3 to 1.5, 1.14, 2.4, 2.13, 3.11)',
            requirements='not yet ingested (Part E)'),
       dict(body='Police Scotland and the Scottish Police College', says='trains recruits in-house at Tulliallan; works with universities and offers credit-rated awards on the SCQF; helps design some criminology-focused degrees (D1, 1.6, 1.7)',
            requirements='not-applicable-by-design (Part E)'),
       dict(body='Scottish Institute for Policing Research', says='works with Police Scotland and universities on research and knowledge exchange (D1, 1.6)', requirements='not-applicable-by-design (Part E)'),
       dict(body='Police Service of Northern Ireland', says='has its own degree-level qualification for all new entrants, a BSc (Hons) and a graduate certificate (D1, 1.8)', requirements='not yet ingested (Part E)'),
       dict(body='Jisc', says='issues sector guidance on accessible websites and apps (D1, 1.23)', requirements='not-applicable-by-design (Part E)'),
       dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not-applicable-by-design (Part E)'),
       dict(body='Association of Police and Crime Commissioners and National Police Chiefs\' Council', says='source of the stated mission of policing (D1, 1.1)', requirements='not-applicable-by-design (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['front matter', '1.16', '1.17', '1.18', '1.19', '2.2', '2.3', '3.2', '3.3', '3.14', '3.15', '4.3', '4.4'],
                 statements=['1.16', '1.17', '1.18', '1.19', '2.2.b5', '3.2.b5', '3.14.b9', '4.3.b8', '4.4.b6']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.19', '1.20', '1.21', '1.22', '1.23'],
                 statements=['1.19', '1.20', '1.22', '1.23.b1', '1.23.b2', '1.23.b3', '1.23.b4']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['front matter', '1.24', '1.25', '1.26', '4.4'],
                 statements=['1.26', '4.4.b6']),
            dict(id='theme:enterprise', named='employability (front matter; no enterprise heading in the body)', carriedIn=['front matter', '1.26', '2.6', '2.16', '3.14'],
                 statements=['2.16', '3.14'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['1.4', '1.13', '1.24', '1.27', '2.10', '4.2']),
                dict(framework='scqf', levels=['fqheis:10'], citedIn=['1.4', '1.6', '1.13', '1.24', '1.27', '2.10', '4.2']),
                dict(framework='other: Policing Education Qualifications Framework (PEQF)', levels=[], citedIn=['1.4', '1.6', '1.8', '2.6', '3.11']),
                dict(framework='other: Competency Values Framework (CVF)', levels=[], citedIn=['1.14']),
                dict(framework='other: the relevant national qualification framework, unnamed', levels=[], citedIn=['2.17'])],
    bodies=[dict(body='College of Policing', citedIn=['front matter', '1.3', '1.4', '1.5', '1.14', '1.17', '1.28', '2.4', '2.13', '3.11']),
            dict(body='Police Scotland and the Scottish Police College', citedIn=['1.6', '1.7']),
            dict(body='Scottish Institute for Policing Research', citedIn=['1.6']),
            dict(body='Police Service of Northern Ireland', citedIn=['1.8']),
            dict(body='Home Office', citedIn=['1.3']),
            dict(body='Jisc', citedIn=['1.23']),
            dict(body='Office for Students', citedIn=['front matter']),
            dict(body='PSRBs, unnamed', citedIn=['front matter', '2.23'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classes, for achievement above the threshold'),
                     dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the UK Quality Code; Work-based Learning (QAA, 2018)', citedIn=['front matter', '2.8', '2.16'], role='course design, work-based learning and professional codes'),
                     dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                     dict(document='College of Policing National Policing Curriculum (not yet ingested)', named='National Policing Curriculum (NPC)', citedIn=['1.4', '2.4', '3.11'], role='curriculum for licensed programmes'),
                     dict(document='College of Policing Code of Ethics (not ingested)', named='College of Policing Code of Ethics', citedIn=['1.14'], role='principles of professional behaviour'),
                     dict(document='Equality Act 2010 (law)', named='Equality Act 2010; Public Sector Equality Duty', citedIn=['1.17'], role='equality duties'),
                     dict(document='Northern Ireland Act 1998 (law)', named='Section 75 of the Northern Ireland Act 1998', citedIn=['1.17'], role='equality duties in Northern Ireland'),
                     dict(document='Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 (law)', named='the Accessibility Regulations 2018', citedIn=['1.23'], role='accessible websites and apps'),
                     dict(document='UN Sustainable Development Goals (external)', named='United Nations 17 sustainable development goals', citedIn=['1.26'], role='frame of the sustainability theme'),
                     dict(document='quality frameworks of the nations (not ingested)', named="Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland)", citedIn=['front matter'], role='the regulatory status of the statement in each nation')])

B1 = [dict(slug='partnership-arrangement', definition='an arrangement between two or more organisations to deliver parts of teaching, learning, assessment and student support (D1, 2.15)',
           beneficiaryDefinition='when another organisation, such as a police force, delivers part of your course with the university', scopeNote='governed by 2.16 to 2.19', category='unknown', practices=['education']),
      dict(slug='education-for-sustainable-development', definition='building curriculum and content that equip learners to take informed, responsible decisions for the environment, the economy and a just society (D1, 1.25)',
           beneficiaryDefinition='learning that helps you make responsible choices for people and the planet', scopeNote='the ESD theme', category='unknown', practices=['education']),
      dict(slug='peqf', definition="the College of Policing's framework for a standardised approach to the initial education of constables in England and Wales, with three entry routes (D1, 1.4)",
           beneficiaryDefinition='the framework that sets the routes to becoming a police constable in England and Wales', scopeNote='not applicable in Scotland or Northern Ireland (1.6, 1.8)', category='unknown', practices=['education', 'policing']),
      dict(slug='monitoring-and-evaluation', definition='a periodic assessment of a course, internal or external, using current and past monitoring to understand achievement and plan the course (D1, 2.20)',
           scopeNote='part of quality assurance', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum a student of Policing will have shown when awarded honours (D1, 4.1)', scopeNote='the one rung the statement sets', category='unknown', practices=['education'])]
B2A = [dict(concept='partnership-arrangement', form='partnership', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='education-for-sustainable-development', form='Education for sustainable development', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='peqf', form='Policing Education and Qualification Framework', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='peqf', form='PEQF', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
       dict(concept='monitoring-and-evaluation', form='Monitoring and evaluation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []
B5 = []
D3 = [dict(citation='College of Policing, Policing Education Qualifications Framework and National Policing Curriculum (current editions)', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2018) UK Quality Code for Higher Education, Advice and Guidance: Work-based Learning', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted')]

E = [
    "Title: the cover reads 'Subject Benchmark Statement Policing In partnership with' followed by the College of Policing's logo, lost in extraction; the slug's 'in-partnership-with' comes from that line. Title recorded as 'Subject Benchmark Statement Policing'.",
    "Edition: the back matter says 'First edition, Published 30 March 2022', yet the front matter lists 'Key changes from the previous Subject Benchmark Statement'. supersedes is left none-stated; for P3.",
    "Rungs (differs from Psychology): one rung only, threshold, as two lists under the heading 'Threshold level': 4.3 subject knowledge, understanding and skills (18 items) and 4.4 generic skills (11 items). No typical or excellent rung; 4.2 hands the classes above threshold to Annex D (the Archaeology shape). The skeleton counted no rungs: corrected to threshold 29.",
    "Rungs, force: both threshold lead-ins say 'students should be able to', while 4.1 defines the list as the minimum threshold standards; force recorded as threshold with forceFrom 4.1 (batch 1 convention). For P3: should these read 'should'?",
    "Outcome list (differs from Psychology): 2.2 'Programmes will therefore enable graduates to' gives 13 graduate outcomes in a programme-design lead-in; recorded as outcomes (rung none, force will).",
    "Section order (differs from Psychology): section 1 has subsections per nation (England and Wales, Scotland, Northern Ireland) and the themes; section 2 'Distinctive features' is mostly provider matter (design, employer involvement, progression, flexibility, partnership, monitoring); assessment strategy (3.14 to 3.17) carries many obliging items.",
    "S4, obliging words outside the five, not taken as statements, for Abbott: 1.13 'needs to develop'; 1.15 'it is therefore important' (1.15 taken for its 'will' and 'should'); 1.23 stem 'are expected to adhere'; 1.24 'need to develop'; 2.5 'It is essential that'; 2.7 'There is a necessity'; 2.8 'Students need to prepare' and 'It is therefore essential'; 2.10 'it is expected that'; 2.21 'an essential component'.",
    "S4, 'required': 2.14 'students are required to design, undertake and complete' read as must (batch 1 convention).",
    "S4, provider 'will' norms not taken as statements: 1.14 'will align', 2.1 'Programmes will be designed', 2.21 'providers will use external reviewers', 2.22 'external examiners will be asked'; predictive or design norms, not outcomes. For P3.",
    "S4, plain-present provider norms, not statements (template open point 5): 2.13 (programmes 'include a diverse range' of methods), 2.20 (awarding bodies 'routinely collect and analyse'), 3.12 ('may not require').",
    "S4, list items: 1.23's four items ('students who should be able to' access, keep pace, review and reflect) read as accessible provision, addressee provider, student version not applicable. 1.26's eight SDG items are topics for the curriculum, not statements: the stem is the statement, cut by find. 3.3's sixteen indicative topics ('may include') are an S3 area, not statements.",
    "S4, 3.14: the stem's own two 'must' sentences are one statement (cut by find, without the 'should incorporate' lead-in); its ten items are statements, b1 to b8 'should', b9 and b10 'must'.",
    "S4, 3.15: 'students must have opportunities to co-create' is Matthews' (2016) argument as cited, not the issuer's obligation; force recorded should.",
    "S4, 3.11: force must from 'will require' and 'require' for licensed PEQF programmes; it also carries 'should map'. Licensed and unlicensed programmes differ (3.12).",
    "S4, 1.18: addressee both (EDI 'should' on the subject; 'must understand' ethics on students); force must.",
    "S4a: 41 of 89 statements are provider duties with no student version; their student-facing effect is in 4.3, 4.4 and 2.2.",
    "SB6, themes: the front matter names three cross-cutting themes, EDI, ESD and employability; employability is recorded under theme:enterprise (as in Psychology), though no enterprise heading appears. Accessibility is a body heading not named in the front matter. Horizon scanning (1.27 to 1.29) is beside sustainability but not a theme id; generative AI is not mentioned.",
    "SB6, frameworks: PEQF and the Competency Values Framework are professional frameworks with no levels; 2.17's 'relevant national qualification framework' names none. The SCQF is named in 1.6 with no level; FQHEIS Level 10 in six paragraphs.",
    "Levels: 2.12 names the Certificate and Diploma of Higher Education as exit awards (fheq:4, fheq:5) and 1.8 the PSNI Graduate Certificate; none is covered by the standards, so they are not in levelsCovered.",
    "Subjects: HECoS 100486 policing is stated; CAH16-01-01, CAH16-01 and CAH16 (law, the CAH home of policing in the HESA store), HECoS 100484 criminology and 100483 criminal justice are inferred, from 1.8, 2.14, 2.2.b8 and 4.3.b1; for P3 confirmation.",
    "SB5: the College of Policing's own requirements (PEQF, NPC, licensing) and the PSNI's are not yet ingested (D3). The other bodies set no requirements on courses: not-applicable-by-design.",
    "S7: overlap with the Criminology 2022 statement inferred, not cited.",
    "Pedagogy named for theory ingest, not ingested here: learner-centred and student-centred learning (3.4, 3.5), experiential learning (3.5), Student as Producer (Jameson et al, 2012; 3.6 to 3.10), students as partners (Matthews, 2016; 3.15), constructive alignment (3.15), inclusive learning and teaching (Thomas and May, 2010; Hockings, 2010; 1.21).",
    "Held text: extraction faults kept as held: 'hor izon' (contents), 'twenty-f irst' (1.1), 'inf luencing' (1.4), 'shif t' (3.4); 'Thorough the use' (1.19) is the issuer's typo.",
    "S1, licence: copyright notice only, no re-use terms; QAA's terms for holding and chunking are to check.",
    "S9: not researched in P1.",
]
