# Judgement file for run 0098, QAA Subject Benchmark Statement: Criminology (March 2022). std run agent.
# Read by tools/bm_build.py. Every text field below is ours; the issuer's words reach the document only through `source`.
HON = "bachelor's with honours"
MA = "master's"
CIT = "QAA (2022), Criminology Subject Benchmark Statement, para "

META = dict(
    run='0098', p1='2026-10-03 16:55',
    title='Subject Benchmark Statement: Criminology',
    heading='Subject Benchmark Statement: Criminology (QAA, March 2022)',
    edition='March 2022 (fourth edition)', published='2022-03',
    status='current', supersedes='the third edition (2019), revised from the 2014 and 2007 editions (D1, back matter)',
    subjects=[dict(scheme='hecos', code='100484', label='criminology', basis='stated'),
              dict(scheme='cah', code='CAH15-01-02', label='sociology', basis='inferred'),
              dict(scheme='hecos', code='100483', label='criminal justice', basis='stated')],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (fourth edition of this Statement)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("This document holds the academic standards QAA sets for criminology degrees in the UK: what an honours "
                     "graduate should be able to do at three rungs (threshold, typical and excellent), shown as an eleven-row table, "
                     "plus threshold outcomes for a master's degree, research-methods and ethics expectations by stage and the duties "
                     "it places on course teams for inclusion, sustainability, employability and accessibility. Use it to describe, "
                     "design or review a criminology course or to help a student see where their work stands; cite paragraph numbers "
                     "and never treat it as regulation."),
    summary=("Criminology (QAA, March 2022) covers the bachelor's degree with honours (FHEQ level 6, FQHEIS level 10, stated) and "
             "sets threshold outcomes for postgraduate (master's) degrees. Section 4 states three rungs in one table: threshold "
             "(third class), typical (2:2 and 2:1) and excellent (first class), eleven outcomes each, worded with rising "
             "criticality and 'exceptional'; section 2 adds research-philosophy expectations at threshold and typical, excellent "
             "and postgraduate levels. Its cross-cutting themes are equality, diversity and inclusion; education for sustainable "
             "development (with green criminology); employability, entrepreneurship and enterprise; and accessibility. It names "
             "the British Society of Criminology, the British Sociological Association, the ESRC, the College of Policing and the "
             "National Probation Service, and points to Annex D of the FHEQ for the classification descriptions."),
    authority='reference: a sector reference point published by QAA as a membership body; in England not a sector-recognised standard, in Wales and Scotland a key reference point, in Northern Ireland part of quality requirements (D1, front matter)')

S2 = dict(
    governs='the academic standards of criminology degrees, chiefly the bachelor\'s degree with honours, with threshold standards for postgraduate degrees',
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"This document relates mainly to bachelor\'s degrees with honours, although Criminology is also studied at levels above and below this" (D1, 1.3)',
    statedSubjects=[
        dict(name='Criminology', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100484', label='criminology'), dict(scheme='cah', code='CAH15-01-02', label='sociology')]),
        dict(name='single honours ... joint honours', locator='(D1, 1.1; 1.8; 2.21)', kind='programme title', codes=[dict(scheme='hecos', code='100484', label='criminology')]),
        dict(name='police studies, security, criminal justice policy, international criminology, forensic psychology and criminal justice', locator='(D1, 1.4)', kind='specialism',
             codes=[dict(scheme='hecos', code='100483', label='criminal justice'), dict(scheme='hecos', code='100486', label='policing'), dict(scheme='hecos', code='100387', label='forensic psychology')]),
        dict(name='green criminology', locator='(D1, 1.15; 1.16)', kind='specialism', codes=[dict(scheme='hecos', code='100484', label='criminology')])])

SECTIONS = {'1': 'Context and purposes of a Criminology degree', '2': 'Distinctive features of a Criminology degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.7', 'Purposes of a Criminology degree'), ('1.8', '1.8', 'Characteristics of a Criminology degree'),
       ('1.9', '1.14', 'Equality, diversity and inclusion'), ('1.15', '1.23', 'Sustainability'),
       ('1.24', '1.27', 'Entrepreneurship and enterprise education'), ('2.1', '2.1', 'Design'),
       ('2.2', '2.2', 'Threshold and typical level'), ('2.3', '2.3', 'Excellent level'), ('2.4', '2.4', 'Postgraduate level'),
       ('2.5', '2.16', 'Skills and competencies'), ('2.17', '2.18', 'Accessibility'), ('2.19', '2.23', 'Progression'),
       ('2.24', '2.25', 'Flexibility'), ('2.26', '2.30', 'Partnership'), ('2.31', '2.34', 'Monitoring and review'),
       ('3.1', '3.4', 'Content'), ('3.5', '3.7', 'Teaching and learning'), ('3.8', '3.10', 'Assessment'),
       ('4.1', '4.4', 'Introduction'), ('4.5', '4.5', 'Criminology subject-specific expectations'),
       ('4.6', '4.6', 'Benchmark standard for postgraduate degrees')]

G = {
    '1.1': 'single and joint honours; core curriculum', '1.2': 'academic, not occupational, standards; areas not content',
    '1.3': 'honours focus; foundation and master\'s around it', '1.4': 'origins at postgraduate level; specialisms',
    '1.5': 'a changing field with a stable core', '1.6': 'what criminology is concerned with',
    '1.7': 'the list is open', '1.8': 'core areas for single and joint honours',
    '1.9': 'inclusion debates at the heart of the field', '1.10': 'duty to embed inclusion in curricula',
    '1.11': 'inclusion built into course design', '1.12': 'belonging and safe dialogue',
    '1.13': 'inclusion in review; removing barriers', '1.14': 'diverse intake; under-represented groups',
    '1.15': 'sustainability as current curriculum', '1.16': 'green criminology',
    '1.17': 'theory with practice; proactive discipline', '1.18': 'ethics tied to sustainability',
    '1.19': 'ESD principles quoted', '1.20': 'multidisciplinary teaching for ESD',
    '1.21': 'content for global citizenship', '1.22': 'skills; volunteering and placements',
    '1.23': 'where to find ESD guidance', '1.24': 'methodological skills at honours level',
    '1.25': 'research ethics and employability', '1.26': 'wide career routes; workforce links',
    '1.27': 'employability opportunities and safeguards', '2.1': 'research and enquiry underpin the subject',
    '2.2': 'research philosophy at threshold and typical', '2.3': 'research philosophy at excellent',
    '2.4': 'research competence at postgraduate level', '2.5': 'basic research design and reflexivity',
    '2.6': 'basic qualitative approaches', '2.7': 'advanced qualitative analysis',
    '2.8': 'basic quantitative techniques', '2.9': 'advanced quantitative techniques',
    '2.10': 'methods in practice, higher or postgraduate', '2.11': 'mixing data; stages of analysis',
    '2.12': 'knowing research ethics and codes', '2.13': 'ethical problems and strategies',
    '2.14': 'limits of ethical strategies', '2.15': 'ethics debates and data law',
    '2.16': 'ethical literacy for all', '2.17': 'varied entry routes',
    '2.18': 'accessible, single-tier teaching and assessment', '2.19': 'progression from foundations to graduate skills',
    '2.20': 'yearly progress; readiness for further study', '2.21': 'joint honours outcomes',
    '2.22': 'exit awards; Scottish four-year degree', '2.23': 'specialising; independent work late on',
    '2.24': 'varied teaching styles', '2.25': 'independent research and its risks',
    '2.26': 'influence on crime policy', '2.27': 'research partnerships and their aims',
    '2.28': 'partners in justice and government', '2.29': 'partner charities and NGOs',
    '2.30': 'educational partnerships; placements', '2.31': 'monitoring and periodic review',
    '2.32': 'external reviewers', '2.33': 'external examining', '2.34': 'accreditation by professional bodies',
    '3.1': 'debates that characterise the field', '3.2': 'theory, evidence and open dialogue',
    '3.3': 'empirical work driving theory', '3.4': 'contested core concepts',
    '3.5': 'modes of study; accessible materials', '3.6': 'principles for teaching, learning and assessment',
    '3.7': 'settings for teaching and learning', '3.8': 'purposes of assessment; monitoring outcomes',
    '3.9': 'what assessment covers', '3.10': 'scaffolded modules',
    '4.1': 'threshold standards for the honours award', '4.2': 'classes rest on level 6 or level 10',
    '4.3': 'most exceed the threshold; kinds of evidence', '4.4': 'three rungs named',
    '4.5': 'the rung table: eleven outcomes at three rungs', '4.6': 'threshold outcomes for master\'s degrees'}

CTYPE = {'1.6': 'area', '1.8': 'area', '2.6': 'area', '2.8': 'area', '3.1': 'area', '3.2': 'area',
         '1.27': 'practice', '2.24': 'practice', '2.30': 'practice', '3.5': 'practice', '3.6': 'practice',
         '3.7': 'practice', '3.8': 'practice', '3.9': 'practice', '3.10': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='none', heading='Contents', kind='other: table of contents'),
    dict(number='1; 2; 3; 4', heading='section headings', kind='other: headings, recorded as sections in S3'),
    dict(number='5', heading='Membership of the Advisory Group for the Subject Benchmark Statement for Criminology', kind='other: back matter (review group members, 2022, 2019, 2014 and 2007)'),
    dict(number='none', heading='publication details and copyright notice', kind='other: back matter, read for S1 and S8')]

P = {}
def s(i, **k):
    P[i] = k

FD = {'must': "a duty (the issuer's 'must')", 'should': "an expectation (the issuer's 'should')",
      'will': "a stated expectation (the issuer's 'will')",
      'describes': "a stated expectation worded with 'expected' or 'important', which is not one of the five force words"}

def prov(i, force, verbs, about, para, prac, what, nb, when, q, award=HON, level='none', **k):
    aw = 'honours degree' if award == HON else 'degree'
    s(i, type='requirement' if force == 'must' else 'expectation', rung='none', force=force, level=level,
      appliesTo='criminology courses and course teams', addressee='provider', verbs=verbs, about=about, domain='none',
      award=award, para=para, prac=prac,
      ben=('n/a', 'a duty on the course provider; the student meets its effect, not a standard to reach'),
      aaw=(f"Describe this as {FD[force]} on the course provider, not a standard students are assessed against: {what}. "
           f"It applies to criminology courses at {aw} level and above where the issuer says so. "
           f"Cite it as {CIT}{i.split('.b')[0]}{', item ' + 'abcd'[int(i.split('.b')[1]) - 1] if '.b' in i else ''}, and do not call it a regulatory requirement. "
           f"Set it beside {nb}."),
      aad=(f"Raise this with a programme team or teacher when {when}. Frame it as a duty of the course and ask: '{q}' "
           f"Do not put it to a student as something they must achieve, and do not read the paragraph out at length."), **k)

def learn(i, force, verbs, about, domain, award, level, para, prac, ben, aaw, aad, type='expectation', **k):
    s(i, type=type, rung='none', force=force, level=level, appliesTo='students of the subject', addressee='learner',
      verbs=verbs, about=about, domain=domain, award=award, para=para, prac=prac, ben=ben, aaw=aaw, aad=aad, **k)

# ---------------------------------------------------------------- section 1: provider duties and one learner expectation
prov('1.10', 'must', ['engage', 'embedded', 'create'], 'embedding equality, diversity and inclusion in the curriculum',
     "Criminology staff carry a responsibility to make inclusion real in practice as well as in theory; the study of equality, diversity and inclusion must run through and across curricula, and the discipline must work to make learning, design and delivery inclusive.",
     "Embed the study of equality, diversity and inclusion in every part of the curriculum, not one module, and make design and delivery inclusive; staff share a duty to practise inclusion, and equality law applies to students and staff alike.",
     'equality, diversity and inclusion must be studied throughout the curriculum and built into how courses are designed and taught',
     'paras 1.11 to 1.13 (the other inclusion duties), para 3.6 item d and spine:6',
     'a team reviews where equality, diversity and inclusion sit in the curriculum',
     'Where in each year do students study equality, diversity and inclusion, and how is delivery itself made inclusive?')
prov('1.11', 'must', ['embedded', 'respected'], 'inclusive learning design',
     "Equality and diversity must be built in when courses and curricula are planned and designed, for instance through equity in design and evaluation, safe spaces for students to voice views, student input to assessment and delivery and a curriculum that is flexible and accessible; students will be treated with respect as individual learners and may share in creating knowledge.",
     "Build equality and diversity into the planning and design stage through learning design: equity in course evaluation, safe settings for discussion, student input to assessment and delivery and a curriculum that is flexible, accessible and offered in several modes.",
     'equality and diversity must be designed into courses from the planning stage',
     'paras 1.10 and 1.12, para 2.18 (accessibility) and spine:6',
     'a team plans or redesigns a course or module',
     'At what point in your design process do you test the course for equity, and which students have a say in it?')
prov('1.12', 'must', ['addressed', 'ensure', 'supported'], 'belonging and safe dialogue across the learning journey',
     "Equality and diversity should be revisited at every stage of study, and the discipline must make sure students feel they belong and that their experience adds to their learning; students should be helped to voice views on sensitive and contested topics in a safe, collegial setting and to reflect on how their experience shapes them, and criminology should look critically at widening links with outside communities.",
     "Plan for belonging at each stage: students must feel their experience is an asset, not a barrier. Support open discussion of sensitive and controversial topics safely, help students see how their experience shapes their views and widen engagement with outside communities at undergraduate and postgraduate levels.",
     'students must be helped to feel they belong, with safe, respectful dialogue on sensitive topics at every stage',
     'paras 1.11 and 1.13 and para 3.6 item d (distressing content)',
     'a team discusses belonging, retention or how sensitive topics are taught',
     'How do students on your course learn that their own experience counts, and how do you prepare them to discuss distressing material?')
prov('1.13', 'must', ['form', 'consider', 'identify', 'establish'], 'inclusive review and removing barriers',
     "Equality and diversity should underpin how the discipline is practised and delivered; inclusion must be treated as continuing quality review and enhancement, course teams must look for hidden or open barriers to success for some groups and for changes that would welcome under-represented groups; teams should build an environment with role models, active support and careful language.",
     "Treat inclusion as part of every review: course teams must check for hidden or overt barriers that hold back particular groups and plan changes to welcome under-represented students, and should provide visible staff role models, active support and considered language.",
     'course teams must review courses for barriers that hold back some groups and act on them',
     'paras 1.12 and 1.14, para 2.31 (monitoring and review) and para 3.8 (monitoring outcomes by protected characteristics)',
     'a course team prepares a periodic or annual review',
     'Which groups of your students do less well, and what in the course might explain it?')
prov('1.14', 'should', ['directed', 'ensure', 'supports'], 'attention to under-represented groups',
     "Criminology draws students from many backgrounds, including mature students, those from non-traditional or less affluent backgrounds, carers and disabled students; more attention should go to under-represented groups at every stage from recruitment to after graduation, so that inclusive practice is seen inside and outside the institution.",
     "Pay deliberate attention to under-represented groups across recruitment, marketing, teaching and career support through to after graduation, so that inclusive practice is visible to students and to the outside world.",
     'under-represented groups should receive more attention at every stage, from recruitment to after graduation',
     'para 1.13 and para 2.17 (entry routes)',
     'a team looks at recruitment, widening participation or graduate outcomes',
     'Which under-represented groups do you reach at recruitment, and do you follow them through to graduate outcomes?')
prov('1.15', 'should', ['based', 'ensuring'], 'keeping the curriculum current',
     "For the discipline to last, its purpose needs to be clear; a course's internal sustainability should rest not only on recruitment but on a current curriculum that takes in new theoretical and methodological work such as green, queer and southern criminology, indigenous knowledge and zemiology.",
     "Judge a course's sustainability by more than recruitment: keep the curriculum current, bringing in emerging approaches such as green, queer and southern criminology, indigenous knowledge and zemiology.",
     'course sustainability should be judged by a current curriculum, not only by recruitment',
     'para 1.16 (green criminology) and para 1.17',
     'a team reviews curriculum currency or a course\'s viability',
     'Which emerging approaches in criminology does your curriculum cover, and when was that last reviewed?')
prov('1.16', 'should', ['include'], 'green criminology in the curriculum',
     "Green criminology, which studies crime that harms the environment, ecological justice and environmental law, has grown in influence; curriculum design should consider its perspectives.",
     "Consider green criminology when designing the curriculum: crimes against the environment, ecological justice and environmental law, including individual, corporate and state failings.",
     'curriculum design should take account of green criminology',
     'para 1.15 and paras 1.19 to 1.21 (education for sustainable development)',
     'a team decides what the curriculum covers on environmental harm',
     'Where, if anywhere, do students meet green criminology on your course?')
prov('1.17', 'should', ['aim', 'considered'], 'proactive, partnership-based sustainable education',
     "Criminology joins scholarship and practice, and sustainable education means working with justice agencies, practitioners and other sectors and cultures; together with justice agencies at home and abroad, the discipline should aim to act ahead of problems rather than only react, and should consider innovation and shared concepts and practice, pedagogy included.",
     "Link theory to practice through work with criminal justice agencies, practitioners and other sectors; aim for a curriculum that anticipates problems rather than reacting, and consider innovation in concepts, practice and pedagogy when developing courses.",
     'the discipline should aim to be proactive and work with justice agencies and practitioners',
     'paras 1.22 and 1.27 and paras 2.26 to 2.30 (partnership)',
     'a team plans partnerships or practice links',
     'Which agencies or practitioners shape your curriculum now, and how?')
prov('1.18', 'should', ['considered'], 'ethics in course development',
     "Ethics runs through teaching, research and the discipline's theory and methods, and is tied to sustainability; it should be considered when courses are developed, updated and reviewed, not least because emotive topics call for a careful balance of equality, diversity, open-mindedness, impartiality and accessibility.",
     "Consider ethics at each stage of developing, updating and reviewing a course, and plan how emotive topics will be taught with care for equality, openness, impartiality and accessibility.",
     'ethics should be considered whenever courses are developed, updated or reviewed',
     'paras 2.12 to 2.16 (research ethics) and para 3.6 item d',
     'a team reviews how ethics and emotive topics are handled',
     'How does your course review check the treatment of ethics and of emotive topics?')
prov('1.20', 'should', ['guide', 'empowers'], 'multidisciplinarity guiding curriculum and teaching',
     "Understanding that criminology draws on many disciplines should guide curriculum development and teaching methods, helping learners grasp critically how culture, economy, environment and globalisation connect.",
     "Let criminology's multidisciplinary nature guide curriculum and teaching methods, so that students learn to see critically how culture, the economy, the environment and globalisation interlock.",
     "the subject's multidisciplinary nature should guide curriculum and teaching",
     'paras 1.19 and 1.21 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance',
     'a team discusses how sustainability enters teaching',
     'Where does your course ask students to connect culture, economy, environment and globalisation?')
prov('1.21', 'should', ['offer', 'enables'], 'knowledge for sustainable development and global citizenship',
     "Criminology should also give students knowledge across topics such as poverty, social justice and environmental and social harm, building awareness of sustainable development and global citizenship and the skills to act on social, environmental and economic concerns.",
     "Offer content on poverty, social justice and environmental and social harms, so that students gain awareness of sustainable development and global citizenship and the skills to address such concerns.",
     'courses should offer content that builds awareness of sustainable development and global citizenship',
     'paras 1.19 and 1.20 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance',
     'a team maps sustainable development in the curriculum',
     'Which modules address poverty, social justice or environmental harm, and how is that assessed?')
prov('1.22', 'should', ['encouraged', 'embedded'], 'volunteering and placements for sustainability',
     "Criminology students build skills such as critical thinking, argument and listening that matter for global citizenship and for justice and security work; where possible they should be encouraged to take up volunteering or placements linked to sustainability, and such learning can sit inside modules.",
     "Where possible, encourage volunteering and work placements connected with sustainability, and consider building service and work-based learning into modules.",
     'students should be encouraged, where possible, to volunteer or take placements linked to sustainability',
     'para 1.27 (employability opportunities) and para 2.30 (educational partnerships)',
     'a team plans placements, volunteering or applied learning',
     'What volunteering or placement routes can your students take, and are any linked to sustainability?')
learn('1.24', 'describes', ['develop', 'comprehend'], 'methodological skills at honours level', 'subject-skill', HON, 'fheq:6',
      "Honours students in criminology are expected to build skills for grasping methodological concepts and principles, including how theory relates to method in research and specialist knowledge of what criminal justice agencies do.",
      "Plan for honours students to develop methodological understanding, including the link between theory and methods and specialist knowledge of the roles and practices of criminal justice agencies.",
      "You are expected to build the skills to understand research methods and their principles, including how theory and methods connect, and to learn in some depth what criminal justice agencies do and how.",
      ("Present this as " + FD['describes'] + " for honours students: skills for understanding methodological concepts and principles. "
       "It holds for the honours award, at FHEQ level 6 and FQHEIS level 10. Cite it as " + CIT + "1.24; do not claim it is a rung or a regulatory standard. "
       "Set it beside para 2.1 (the same expectation), the rung cells 4.5.b19 to 4.5.b21 (research strategies), qaa/fheq-2024/4.15.b2 and spine:6."),
      ("Bring this up when a student asks why methods matter in a criminology degree. Put it in plain words, in the second person for a student and as a question of course design for staff. "
       "Ask: 'How would you explain the link between a theory you know and the method you would use to test it?' Avoid reading the paragraph aloud at length."))
prov('1.27', 'should', ['offered', 'consider'], 'employability opportunities',
     "Chances for students to build employability skills should be offered at a suitable point, through placements, volunteering, employability-linked assessment or guest speakers; safeguards protect students from exploitation or harassment at work, and it matters that placement employers consider accessibility and reasonable adjustments.",
     "Offer employability opportunities at a fitting point in the course, inside or outside the formal curriculum, with safeguards against exploitation and harassment and attention to accessibility and reasonable adjustments on placements.",
     'courses should offer chances to build employability skills at a fitting point',
     'para 1.22, para 2.18 (reasonable adjustments) and para 2.30',
     'a team plans employability, placements or guest teaching',
     'At what point in the course do students meet employability activity, and how are they protected on placement?')

# ---------------------------------------------------------------- section 2: research expectations by level, ethics, access, progression
learn('2.1', 'describes', ['develop', 'comprehend'], 'methodological concepts and principles', 'subject-skill', HON, 'fheq:6',
      "Because research and critical enquiry underpin criminology, students are expected to build skills for grasping methodological concepts and principles, including how theory, evidence and method relate.",
      "Design the research methods strand so that students build an understanding of methodological concepts and of the relationship between theory, evidence and methods.",
      "Research and critical enquiry are at the heart of criminology, so you are expected to build the skills to understand research methods, including how theory, evidence and methods fit together.",
      ("Present this as " + FD['describes'] + " for students across the honours degree (FHEQ level 6, FQHEIS level 10). Cite it as " + CIT + "2.1. "
       "Do not claim it is a rung on its own; the rungs for research philosophy follow in paras 2.2 and 2.3. Set it beside para 1.24, paras 2.2 to 2.4, qaa/fheq-2024/4.15.b2 and spine:6."),
      ("Bring this up when a student or team asks what the methods strand is for. Put it in plain words, in the second person for a student and as a question of course design for staff. "
       "Ask: 'How do theory, evidence and method fit together in a study you have read?' Avoid reading the paragraph aloud at length."))

T22 = ("2.2 At threshold and typical level, students are expected to understand arguments in the philosophy of explanation in contemporary criminological research. "
       "Thus, an understanding of the concepts of ontology and epistemology for the design, analysis, interpretation and dissemination of criminological research will be important. "
       "Students will also be expected to understand the fundamental distinction which can be made between qualitative and quantitative research strategies, as well as the debates surrounding mixing the two (mixed methods research), "
       "and from this develop an understanding of inductive and deductive relationships between theory and research. "
       "They should also be able to discern which data collection and analysis methods are suitable for different kinds of research questions, bearing in mind that research may use multiple methods and/or mixed methods.")
s('2.2', find=T22, type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours students at the threshold level',
  addressee='learner', verbs=['understand', 'discern'], about='philosophy of explanation and research strategies (threshold)', domain='understanding', award=HON,
  para="At the threshold level (set jointly with typical) students are expected to understand arguments about explanation in criminological research; ontology and epistemology; the split between qualitative and quantitative research, with mixed methods; inductive and deductive reasoning; they should also be able to tell which data collection and analysis methods suit which research questions.",
  prac="By threshold, students should grasp the philosophy of explanation; ontology and epistemology; the qualitative-quantitative distinction, with mixed methods; inductive and deductive reasoning. They should also be able to match methods of data collection and analysis to research questions.",
  ben="To reach the threshold standard, you should understand the debates about how criminological research explains things, the difference between qualitative and quantitative research, including ways of mixing them; you should also be able to pick methods that suit a research question.",
  aaw=("Treat this as the research-philosophy expectation the issuer sets jointly for the threshold and typical rungs of the honours degree (FHEQ level 6, FQHEIS level 10), worded as 'expected to' with a 'should' for choosing methods. "
       "Cite it as " + CIT + "2.2. Do not claim it applies to master's study or that it is regulatory. "
       "Set it beside the excellent paragraph 2.3, the table row 4.5.b19 to 4.5.b21, qaa/fheq-2024/4.15.b2 and spine:6."),
  aad=("Raise this when a student struggles to justify a research design or asks what ontology and epistemology have to do with them. "
       "Put it plainly as knowing why you chose your methods; with staff, frame it as the floor the methods teaching must secure. "
       "Ask: 'Is your question better answered with numbers, with accounts or with both, and why?' Do not read the paragraph aloud or present the excellent expectations in 2.3 as the minimum."))
s('2.2.typical', find=T22, type='typical', rung='typical', force='should', level='fheq:6', appliesTo='honours students at the typical level',
  addressee='learner', verbs=['understand', 'discern'], about='philosophy of explanation and research strategies (typical)', domain='understanding', award=HON,
  para="The issuer sets the same research-philosophy expectation for the typical level as for threshold: understanding debates on explanation, ontology and epistemology, research strategies, mixed methods and induction and deduction; and being able to match methods to questions.",
  prac="At the typical level, expect the same grasp of research philosophy and strategy as at threshold, shown more securely; most students should be able to justify their choice of methods for a question.",
  ben="To reach the typical standard, you should understand the debates about explanation in criminological research and the main research strategies; you should also be able to explain clearly why a method suits your question.",
  aaw=("Treat this as the typical-rung reading of a paragraph the issuer sets jointly for threshold and typical in the honours degree (FHEQ level 6, FQHEIS level 10); the wording does not change between the two rungs. "
       "Cite it as " + CIT + "2.2. Do not invent a separate typical standard or present it as the minimum. "
       "Set it beside the threshold record 2.2, the excellent paragraph 2.3 and Annex D's cognitive cells qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."),
  aad=("Raise this when a student working at second-class level asks how to strengthen a methods section. "
       "Put it in plain words as justifying your design securely; with staff, use it to check the middle bands. "
       "Ask: 'Could you defend your choice of method against someone who prefers the other approach?' Do not present it as the pass threshold, and do not read the paragraph out."))
s('2.3', type='excellent', rung='excellent', force='should', level='fheq:6', appliesTo='honours students at the excellent level',
  addressee='learner', verbs=['discuss', 'criticise', 'apply', 'demonstrate', 'appreciate'], about='critique of research philosophy (excellent)', domain='understanding', award=HON,
  para="At the excellent (first-class) level students are expected not only to discuss how theory and method relate but to critique and apply criminological concepts in designing research; they should be able to criticise the explanatory philosophy of criminological studies and see the ethical stakes of methods and the political weight of different readings of data.",
  prac="At first-class level, students should go beyond discussing theory and method: they critique and apply criminological concepts in research design, critique the philosophy of explanation in studies and weigh the ethics of methods and the politics of interpreting findings.",
  ben="To reach the excellent standard, you should be able to critique how criminological studies explain things, use criminological ideas to design research and see the ethical side of your methods and the political side of how findings are read.",
  aaw=("Treat this as the excellent-rung expectation for research philosophy in the honours degree (FHEQ level 6, FQHEIS level 10): an aspiration that marks first-class work, worded with 'should'. "
       "Cite it as " + CIT + "2.3. Do not present it as required for the award or as a master's standard (para 2.4 covers postgraduate study). "
       "Set it beside para 2.2, the excellent cell 4.5.b21 and Annex D's first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."),
  aad=("Raise this when a student aiming for a first asks how to make a methods discussion stand out. "
       "Put it as an aspiration in plain words; with staff, use it to describe the top band. "
       "Ask: 'What does your design assume about how crime can be known, and what is at stake politically in how your data are read?' Never present it as what every student must reach."))
learn('2.4', 'describes', ['comprehend', 'develop', 'criticise', 'apply', 'recognise'], 'research competence at postgraduate level', 'subject-skill', MA, 'fheq:7',
      "At postgraduate level students are expected to grasp key methodological concepts, critique and apply criminological thought in research design and recognise subtle debates, with a wider range of skills than undergraduates and the ability to design and carry out research in real-world settings using many methods.",
      "At postgraduate level, expect students to critique and apply concepts in research design, engage with nuanced methodological debates and design and run criminological research in real settings with a wide repertoire of methods.",
      "At postgraduate level, you are expected to critique and apply criminological ideas when designing research, follow subtle debates about method and design and carry out real-world research using a wide range of methods.",
      ("Present this as " + FD['describes'] + " for postgraduate study in criminology, read as the master's degree (FHEQ level 7, FQHEIS level 11, inferred). "
       "Cite it as " + CIT + "2.4. Do not apply it to the honours degree or call it regulatory. "
       "Set it beside the master's outcomes 4.6.b4 and 4.6.b6, qaa/fheq-2024/4.17.b2 and spine:7."),
      ("Raise this with master's students or a postgraduate team when research design or a dissertation plan is discussed. "
       "Put it plainly as designing and running real-world research with a wide choice of methods. "
       "Ask: 'Which debates about method bear on your project, and how will you answer them?' Do not apply it to undergraduates or read the paragraph aloud."))
learn('2.5', 'describes', ['develop', 'design', 'reflect'], 'foundations of research design and reflexivity', 'subject-skill', HON, 'fheq:6',
      "Early in the degree students are expected to have grounding, for both qualitative and quantitative methods, in forming research questions, designing research and reflecting on design and practice, with attention to positionality and power.",
      "In early methods teaching, cover forming a research question, designing a study and reflecting on design and practice, with explicit attention to positionality and power, across qualitative and quantitative traditions.",
      "Early on, you are expected to learn how to form a research question, design a study and reflect on your research, thinking about your own position and the power differences involved.",
      ("Present this as " + FD['describes'] + " for the early, basic stage of the honours degree, on the route to FHEQ level 6. "
       "Cite it as " + CIT + "2.5. Do not present 'basic level' as a framework level or claim it is regulatory. "
       "Set it beside paras 2.6 and 2.8 (basic qualitative and quantitative methods), the cell 4.5.b19 and spine:6."),
      ("Raise this when a student starts planning a first project or asks what positionality means. "
       "Put it plainly as learning to ask a good question and to think about your own place in the research. "
       "Ask: 'How might who you are affect what participants tell you?' Avoid reading the paragraph aloud at length."))
learn('2.6', 'describes', ['have'], 'basic knowledge of qualitative approaches', 'knowledge', HON, 'fheq:6',
      "At a basic level students are expected to know the range of qualitative approaches available; the issuer's list is illustrative, running from case studies, interviews, focus groups, observation and ethnography to participatory, decolonising, internet, visual and evaluation methods, sampling, indexing and interpreting qualitative data.",
      "Introduce the main qualitative approaches early, choosing from a broad menu that includes interviewing, focus groups, observation, ethnography (virtual too), participatory and decolonising methods, documentary, visual and internet research, sampling and the limits of interpretation.",
      "Early on, you are expected to know the main qualitative approaches, such as interviews, focus groups, observation and ethnography, and how qualitative data are sampled, organised and interpreted.",
      ("Present this as " + FD['describes'] + ": basic knowledge of qualitative approaches in the honours degree, with an illustrative list, not a required syllabus. "
       "Cite it as " + CIT + "2.6. Do not claim each listed method must be taught or assessed. "
       "Set it beside para 2.7 (more advanced qualitative techniques), para 2.8 (basic quantitative methods) and qaa/fheq-2024/4.15.b2."),
      ("Raise this when a team plans the qualitative methods strand or a student asks which methods they should know. "
       "Put it plainly as knowing the main options and when each is used. "
       "Ask: 'Which two qualitative approaches could answer your question, and what would each miss?' Do not present the list as a checklist every student must master."))
learn('2.7', 'describes', ['demonstrate'], 'advanced qualitative analysis', 'subject-skill', HON, 'fheq:6',
      "In the later, more advanced stages, students would be expected to show knowledge, and perhaps use, of some qualitative techniques and software, such as coding, analysis and interpretation, using packages like ATLAS.ti or NVivo.",
      "In later years, give students the chance to know and possibly use techniques for coding, analysing and interpreting qualitative data, with software such as ATLAS.ti or NVivo.",
      "Later in your studies, you would be expected to know, and perhaps use, some techniques for coding, analysing and interpreting qualitative data, possibly with software such as NVivo.",
      ("Present this as a hedged expectation ('would be expected to', 'some of', 'possible use') for the later stages of the honours degree, not a requirement to use every technique. "
       "Cite it as " + CIT + "2.7. Do not claim that software use is required. "
       "Set it beside para 2.6, para 2.9 (advanced quantitative techniques) and qaa/fheq-2024/4.15.b2."),
      ("Raise this when a student is choosing how to analyse interview or text data. "
       "Put it plainly as knowing how qualitative data are coded and interpreted. "
       "Ask: 'How will you move from your transcripts to findings you can defend?' Do not suggest that particular software is compulsory."))
learn('2.8', 'describes', ['have'], 'basic knowledge of quantitative techniques', 'knowledge', HON, 'fheq:6',
      "For quantitative methods, early in the degree students are expected to know some of the techniques available, illustratively questionnaire design, survey sampling, experimental design, evaluation, statistical software, comparing means, correlation and causation, secondary data and descriptive and inferential statistics.",
      "Introduce basic quantitative techniques early, drawing on a menu such as questionnaire design, survey sampling, experimental design and trials, statistical software (for example SPSS or R), comparing means, correlation versus causation, secondary data and basic statistical tests.",
      "Early on, you are expected to know some basic quantitative techniques, such as designing a questionnaire, sampling, using statistics software, telling correlation from causation and running simple statistical tests.",
      ("Present this as " + FD['describes'] + ": basic quantitative knowledge in the honours degree, with an illustrative list of techniques. "
       "Cite it as " + CIT + "2.8. Do not claim every technique listed must be taught. "
       "Set it beside para 2.9 (advanced quantitative techniques), the cells 4.5.b25 to 4.5.b27 (analysing empirical data) and Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd (numeracy)."),
      ("Raise this when a student is anxious about statistics or a team plans the quantitative strand. "
       "Put it plainly as the basic tools for working with numbers about crime. "
       "Ask: 'Can you explain why a link between two figures does not show that one causes the other?' Do not present the list as a test everyone must pass item by item."))
learn('2.9', 'describes', ['demonstrate'], 'advanced quantitative techniques', 'subject-skill', HON, 'fheq:6',
      "In the later, more advanced stages, students would be expected to show knowledge, and perhaps use, of some quantitative techniques such as t-tests, ANOVA and other multivariate analysis, systematic reviews, secondary and big data, data mapping, graphical presentation and online data analysis.",
      "In later years, offer some advanced quantitative techniques, such as t-tests, ANOVA, multivariate analysis, systematic reviewing, big and secondary data, mapping, data visualisation and analysis of social media data.",
      "Later in your studies, you would be expected to know, and perhaps use, some advanced quantitative techniques, such as t-tests, ANOVA, systematic reviews, mapping data or analysing online data.",
      ("Present this as a hedged expectation ('would be expected to', 'some of') for the later stages of the honours degree. "
       "Cite it as " + CIT + "2.9. Do not claim each technique is required. "
       "Set it beside para 2.8, para 2.10 (higher or postgraduate methods) and qaa/fheq-2024/4.15.b2."),
      ("Raise this when a student plans a quantitative dissertation or asks which tests to learn. "
       "Put it plainly as a choice of advanced tools. "
       "Ask: 'Which test suits your data and question, and what would it not tell you?' Do not treat the list as compulsory."))
learn('2.10', 'describes', ['use'], 'methods in practice at higher or postgraduate level', 'subject-skill', [HON, MA], 'none',
      "At higher or postgraduate level there is a further expectation of knowing and understanding, and perhaps using in practice, computer-assisted personal interviewing, qualitative software, systematic reviews and virtual ethnography.",
      "At higher or postgraduate level, give students knowledge and understanding, and where possible practice, of computer-assisted interviewing, qualitative analysis software, systematic reviewing and virtual ethnography.",
      "At a higher or postgraduate stage, you are expected to know and understand, and may use, methods such as computer-assisted interviewing, qualitative analysis software, systematic reviews and online ethnography.",
      ("Present this as " + FD['describes'] + " for the higher stages of the honours degree or for postgraduate study; the issuer does not say which, so give no single framework level. "
       "Cite it as " + CIT + "2.10. Do not claim the methods must be used, only known and understood. "
       "Set it beside paras 2.7 and 2.9 and the master's outcome 4.6.b4."),
      ("Raise this when an advanced student or postgraduate asks which specialist methods to learn. "
       "Put it plainly as knowing these methods well enough to choose among them. "
       "Ask: 'Would any of these methods strengthen your project?' Do not present them as compulsory."))
learn('2.11', 'should', ['gain'], 'mixing data and the stages of analysis', 'understanding', [HON, MA], 'none',
      "All students should also acquire a basic grasp of two things: how qualitative and quantitative data can be combined, including triangulation, data integration and inductive, deductive and abductive reasoning; and the stages of analysis from reduction and display to comparison and integration.",
      "Teach every student the basics of mixing qualitative and quantitative data (triangulation and integration), of induction, deduction and abduction and of the stages of data analysis.",
      "You should gain a basic understanding of how numerical and qualitative data can be combined, of reasoning by induction, deduction and abduction and of the stages of analysing data.",
      ("Present this as " + FD['should'] + " for all students in criminology, at every stage; it names no framework level. "
       "Cite it as " + CIT + "2.11. Do not present it as an advanced or optional topic. "
       "Set it beside para 2.2 (mixed methods), the cells 4.5.b25 to 4.5.b27 and qaa/fheq-2024/4.15.b2."),
      ("Raise this when a student plans to use more than one kind of data. "
       "Put it plainly as knowing how different data can be brought together. "
       "Ask: 'How will you bring your survey results and interviews together, and what happens if they disagree?' Avoid reading the list of analysis stages aloud."))
learn('2.12', 'should', ['show', 'engage', 'know'], 'knowledge of research ethics and codes', 'knowledge', [HON, MA], 'none',
      "Ethics is basic to all research; at every level students are expected to know what ethics means, the policy frameworks, the difference between personal, legal and professional ethics and the main codes criminologists use, and should show they can discuss the value and limits of codes; they are also expected to know how to get ethical approval locally.",
      "Teach ethics at every level: what ethics means, policy frameworks, the split between individual, legal and professional ethics and the main codes (such as the British Society of Criminology's); students should show they can discuss what codes achieve and where they fall short, and know your institution's approval process.",
      "At every stage, you are expected to know what research ethics means and the main codes criminologists use; you should be able to discuss what those codes do well and badly, and know how to get ethical approval for your own research.",
      ("Present this as an expectation for students at all levels ('expected to', with a 'should' for discussing codes). "
       "Cite it as " + CIT + "2.12, and name the British Society of Criminology's Statement of Ethics only as the issuer's example. "
       "Do not claim a particular code is mandatory. Set it beside paras 2.13 to 2.16 and the professional cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."),
      ("Raise this when a student is preparing an ethics application or asks why codes of ethics matter. "
       "Put it plainly as knowing the rules and being able to question them. "
       "Ask: 'Which code applies to your project, and where might it not fit your situation?' Do not read the codes aloud at length."))
learn('2.13', 'describes', ['consider', 'choosing', 'maintaining', 'engaging'], 'strategies for ethical problems', 'subject-skill', [HON, MA], 'none',
      "Ethical problems include interviews that revive painful experiences, using material without consent and steering data towards a favoured theory; students are expected to be able to weigh up approaches such as a fitting research design, informed or valid consent, confidentiality and ethical approaches to hard-to-reach and vulnerable groups.",
      "Use common ethical problems, such as distress in interviews, lack of consent and biased handling of data, to teach strategies: suitable design, informed consent, confidentiality and protocols for hard-to-reach and vulnerable groups.",
      "You are expected to be able to think through ways of handling ethical problems in research, such as choosing a suitable design, getting informed consent, keeping things confidential and working carefully with vulnerable people.",
      ("Present this as " + FD['describes'] + ": students can consider strategies for common ethical problems; the list is illustrative. "
       "Cite it as " + CIT + "2.13. Do not present the strategies as settled answers; para 2.14 says they are not straightforward. "
       "Set it beside paras 2.12 and 2.14."),
      ("Raise this when a student designs research with people who may be distressed or vulnerable. "
       "Put it plainly as planning how to protect participants. "
       "Ask: 'What could go wrong ethically in your study, and what will you do if it does?' Avoid reading the examples aloud."))
learn('2.14', 'should', ['have'], 'the limits of ethical strategies', 'understanding', [HON, MA], 'none',
      "At higher and postgraduate levels students are expected to see that these strategies are not simple, for instance when confidentiality cannot be guaranteed or has to be broken; there should also be awareness of ways to minimise harm and protect confidentiality.",
      "At higher and postgraduate levels, push students to see the limits of ethical strategies, such as when confidentiality has to be broken, and to know ways of minimising harm and safeguarding confidentiality.",
      "At a higher or postgraduate stage, you are expected to see that ethical strategies are rarely simple, for example when confidentiality cannot be kept, and you should know ways to reduce harm and protect confidentiality.",
      ("Present this as " + FD['should'] + " for the higher stages of the honours degree or for postgraduate study; the issuer does not separate the two, so give no single level. "
       "Cite it as " + CIT + "2.14. Do not claim it applies from the start of the degree. "
       "Set it beside paras 2.13 and 2.15 and qaa/fheq-2024/4.15.b4 (uncertainty and the limits of knowledge)."),
      ("Raise this when an advanced student's project touches on disclosure of harm or illegal acts. "
       "Put it plainly as knowing where your promises to participants end. "
       "Ask: 'Is there anything a participant might tell you that you could not keep confidential, and how will you tell them that in advance?' Do not read the paragraph aloud."))
learn('2.15', 'describes', ['be'], 'ethics debates and data protection law', 'knowledge', [HON, MA], 'none',
      "At higher and postgraduate levels students are expected to know the wider debates on ethics, such as whether discipline codes are needed, and to know what the law and personal ethics require, including current data protection law and its research exemptions.",
      "At higher and postgraduate levels, cover debates about codes of ethics and what data protection law requires of researchers, including relevant principles and exemptions.",
      "At a higher or postgraduate stage, you are expected to know the debates about research ethics codes and what data protection law asks of you as a researcher.",
      ("Present this as " + FD['describes'] + " for the higher stages of the honours degree or for postgraduate study. "
       "Cite it as " + CIT + "2.15. Do not give legal advice or claim it sets out what the law requires. "
       "Set it beside paras 2.14 and 2.16."),
      ("Raise this when an advanced student handles personal data in research. "
       "Put it plainly as knowing your legal duties as a researcher. "
       "Ask: 'What personal data will you hold, and what does data protection law expect you to do with it?' Do not offer legal rulings."))
learn('2.16', 'describes', ['gain', 'ensure'], 'ethical literacy', 'subject-skill', [HON, MA], 'none',
      "Overall, all students are expected to reach a suitable level of ethical literacy so that research participants stay safe and well.",
      "Make sure every student reaches a level of ethical literacy fit for keeping research participants safe and well.",
      "You are expected to become ethically literate enough to keep the people in your research safe and well.",
      ("Present this as the summary expectation on research ethics for all students, " + FD['describes'] + ". "
       "Cite it as " + CIT + "2.16. Do not define ethical literacy more tightly than the issuer does. "
       "Set it beside paras 2.12 to 2.15 and the professional cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."),
      ("Raise this when a student or team reviews readiness for fieldwork. "
       "Put it plainly as being able to keep participants safe. "
       "Ask: 'How would you know if your research was harming someone, and what would you do?' Avoid lecturing from the paragraph."))
prov('2.18', 'must', ['avoided', 'adjusted', 'offered', 'considered'], 'accessible, single-tier teaching and assessment',
     "Teaching methods depend on course aims; a two-tier system singling out students with extra needs must be avoided, so teaching and assessment may be tailored, varied formats should be offered to all and expectations should be clear; reasonable adjustments should be considered for fieldwork, equal access to trips, placements and volunteering pursued and assessment criteria should be clear and accessible.",
     "Avoid a two-tier system: offer varied formats to all students, keep expectations transparent, tailor teaching and assessment where needed, consider reasonable adjustments for fieldwork, reduce hidden costs of trips and placements and give clear, accessible assessment criteria at each stage.",
     'teaching and assessment must not split students into two tiers by need; adjustments and accessible formats are for all',
     'paras 1.11 and 1.27 and para 3.8 (adjustments to assessment)',
     'a team reviews assessment formats, fieldwork or placement access',
     'Are your alternative formats open to every student, or only to those with a formal adjustment?')
learn('2.19', 'describes', ['develop', 'appreciate', 'strengthen', 'demonstrate'], 'progression from foundations to graduate skills', 'generic-skill', HON, 'fheq:6',
      "Early in the degree students are expected to build core theoretical knowledge and basic study skills, then strengthen analysis, interpretation and communication and by graduation show problem-solving, evaluation and reflection and the attributes for self-managed, lifelong learning.",
      "Sequence the course so that core theory and study skills come first, analysis, interpretation and communication grow next and problem-solving, evaluation, reflection and self-managed learning are shown by graduation.",
      "You are expected to start with core theory and study skills, build your analysis, interpretation and communication as you go and by the end show that you can solve problems, evaluate, reflect and manage your own learning.",
      ("Present this as " + FD['describes'] + " about progression across the honours degree, ending in generic skills at FHEQ level 6 and FQHEIS level 10. "
       "Cite it as " + CIT + "2.19. Do not claim it sets year-by-year standards. "
       "Set it beside paras 2.20 and 2.23, qaa/fheq-2024/4.15.b5 (managing own learning), qaa/fheq-2024/4.15.b9.3 and spine:6."),
      ("Raise this when a student asks how the years of the degree build on each other. "
       "Put it plainly as a path from foundations to independent learning. "
       "Ask: 'Which of these skills feel secure now, and which do you need to build next year?' Do not read the paragraph aloud."))
learn('2.20', 'describes', ['progress', 'meeting', 'undertaking'], 'progress towards the threshold and readiness for postgraduate study', 'generic-skill', HON, 'fheq:6',
      "Across an honours degree, which the issuer places at FHEQ level 6 and FQHEIS level 10, students move through the years under each institution's rules, each year expected to build towards the threshold subject-specific and generic skills; a graduate with a second-class degree or better would be expected to be ready for postgraduate study in criminology or a related field.",
      "Plan each year to move students towards the threshold subject-specific and generic skills; those finishing with a second-class degree or higher would be expected to be ready for postgraduate study.",
      "Each year of your degree is meant to build towards the minimum skills for the award, and if you finish with a second-class degree or better you would be expected to be ready for postgraduate study.",
      ("Present this as " + FD['describes'] + " about progress through the honours degree at FHEQ level 6 and FQHEIS level 10, which the issuer names here. "
       "Cite it as " + CIT + "2.20. Do not claim it guarantees entry to postgraduate study. "
       "Set it beside para 2.19, the threshold cells of para 4.5 (4.5.b1 onward), qaa/fheq-2024/4.15.b9.3 and spine:6."),
      ("Raise this when a student asks whether their degree prepares them for a master's. "
       "Put it plainly as what a good result opens up. "
       "Ask: 'What result are you on track for, and what would you need for the course you have in mind?' Do not promise admission or treat a second-class degree as the pass mark."))
learn('2.21', 'will', ['achieve', 'add', 'explore'], 'joint honours outcomes', 'subject-skill', HON, 'fheq:6',
      "Joint honours students will attain the core subject-specific and generic skills of criminology, add others from their second subject and may explore where the two meet.",
      "In joint honours courses, students will reach the core specific and generic criminology skills; plan for the skills the other subject adds and for interdisciplinary work where the two overlap.",
      "If you study criminology with another subject, you will gain the core criminology skills, add skills from your other subject and may explore where the two overlap.",
      ("Present this as " + FD['will'] + " for joint honours students at FHEQ level 6 and FQHEIS level 10: the core of the subject, not all of it. "
       "Cite it as " + CIT + "2.21. Do not claim joint honours students meet every single honours expectation in full. "
       "Set it beside para 1.8 (core areas for single and joint honours) and the threshold cells of para 4.5."),
      ("Raise this when a joint honours student asks how their degree compares with single honours. "
       "Put it plainly as the core of criminology plus your other subject. "
       "Ask: 'Where do your two subjects meet, and could your project sit there?' Avoid reading the paragraph aloud."), type='outcome')
prov('2.23', 'should', ['enable', 'develop', 'occur', 'produce'], 'specialising and independent work later in the course',
     "As students progress, chances to specialise are expected to grow; higher levels should help them deepen analytical and critical skills, core and optional modules will let them build expertise and assessed independent study such as a dissertation will normally come near the end.",
     "Increase specialisation as students progress: higher levels should deepen analysis and critique, core and optional modules will let students focus and an assessed independent project, empirical, policy-based or theoretical, normally comes near the end.",
     "higher levels of study should deepen students' analytical and critical skills, with independent work near the end",
     'paras 2.19 and 2.25 (independent research) and qaa/fheq-2024/4.15.b6',
     'a team designs later-year modules or the dissertation',
     'How does your final year let students specialise and produce an independent piece of work?')
learn('2.25', 'describes', ['undertake'], 'independent research and reflection on its risks', 'subject-skill', HON, 'fheq:6',
      "Most criminology degrees ask students to do some independent research, usually a project or dissertation late in the course, which calls for mature, intelligent reflection on its risks and its moral and ethical issues.",
      "Where the course includes a project or dissertation, prepare students to reflect critically on its risks and its moral and ethical issues before they start.",
      "Most courses ask you to carry out independent research, such as a dissertation, near the end; you need to reflect maturely and critically on its risks and its ethical issues.",
      ("Present this as the issuer's description of a common requirement in most courses, not a rule for every course; its 'requirement' and 'needed' are recorded as describes. "
       "Cite it as " + CIT + "2.25. Do not claim every criminology degree must include a dissertation. "
       "Set it beside paras 2.16 and 2.23, the master's outcome 4.6.b6 and qaa/fheq-2024/4.15.b6."),
      ("Raise this when a student plans a dissertation or project. "
       "Put it plainly as thinking through the risks before you begin. "
       "Ask: 'What are the moral and ethical risks of your project, to others and to you?' Do not tell a student that every course must include a dissertation."))
prov('2.32', 'will', ['use', 'gain', 'ensure'], 'external review',
     "Externality is key to UK quality assurance; providers will use external reviewers in periodic review to gain an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
     "Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and subject content are checked.",
     'providers will use external reviewers in periodic review to check threshold standards and content',
     'para 2.31, para 2.33 (external examiners) and para 4.1',
     'a team prepares for periodic review',
     'Who will act as your external reviewer, and which threshold standards will they check against?')

# ---------------------------------------------------------------- section 3
prov('3.5', 'describes', ['ensure'], 'accessible learning materials',
     "Students meet course materials in many ways and modes, full or part-time, with core texts, journals and online resources; it matters that these materials are accessible.",
     "Check that every learning resource, printed, online or streamed, is accessible to all students in every mode of study.",
     "learning materials need to be accessible (the issuer calls this important, not one of the five force words)",
     'paras 1.11 and 2.18', 'a team selects or reviews learning resources',
     'How do you check that online and streamed materials are accessible to every student?')
T36 = ['a) Criminology is neither purely deductive nor purely descriptive; theorisation needs both to guide the collection of data and to be grounded in evidence. Similarly, interpretation of data has to be guided by theorisation. Students are, therefore, given opportunities to acquire capacities of thinking in both abstract and concrete terms and to relate the two. It is expected that criminological theory is a core, foundational aspect of any Criminology degree.',
       'b) Bodies of evidence in criminology are often consistent with alternative interpretations embodied in rival theoretical perspectives. Students are required to weigh alternative interpretations in terms of consistency with evidence, logic, fit with other findings and breadth of explanatory power. Therefore, students are provided with opportunities to rehearse and revise their own ideas and where these fit into their own understanding of criminology and the criminal justice system.',
       'c) Criminology is an ever-evolving discipline and reflects current social, political and public disputes. Therefore, students are provided with opportunities to develop awareness of, and reflect on, their own values and those of their cultural, global and political environment, and an appreciation of how alternative values impact upon rival interpretations of evidence. Learning, teaching and assessment approaches within criminology should enable students to engage with these social, political and public disputes, and offer opportunities to apply criminological knowledge to contemporary crime problems.',
       'd) Criminology attracts students from diverse academic and social backgrounds; their learning and skills development needs vary accordingly. To reflect this, degree courses need to provide flexible and varied teaching, learning and assessment strategies to ensure that all students have as equal an opportunity as possible to acquire the necessary knowledge and skills to graduate in Criminology. Where possible, criminological learning, teaching and assessment approaches should be designed to be as inclusive as possible to remove the need for alternative assessment. Alongside this, all involved in the delivery of learning, teaching and assessment within criminology should recognise the emotive nature of much of criminology, and the challenges and impact of engaging with potentially distressing content.']
prov('3.6.b1', 'describes', ['guide', 'relate'], 'theory as a core of the degree',
     "Criminology is neither purely deductive nor descriptive: theory guides data collection and interpretation and has to rest on evidence, so students get chances to think abstractly and concretely and link the two; theory is expected to be a core, foundational part of any criminology degree.",
     "Make criminological theory a foundational, core strand of the degree, and give students repeated practice moving between abstract theory and concrete evidence.",
     'criminological theory is expected to be a core, foundational part of every criminology degree',
     'the rung row 4.5.b1 to 4.5.b3 (concepts and theories), para 3.2 and spine:6',
     'a team decides how much theory the course carries', 'Where in each year do students move between theory and evidence?', find=T36[0])
learn('3.6.b2', 'must', ['weigh', 'rehearse', 'revise'], 'weighing rival interpretations of evidence', 'subject-skill', HON, 'fheq:6',
      "Evidence in criminology often fits rival theories, so students are required to weigh alternative readings by how well they match the evidence, their logic, how they sit with other findings and how much they explain, and are given chances to test and revise their own ideas.",
      "Students must weigh competing interpretations against evidence, logic, fit with other findings and explanatory power; give them repeated chances to rehearse and revise their own positions.",
      "You are required to weigh rival explanations of the same evidence, judging them by how well they fit the evidence and other findings, how logical they are and how much they explain, and to test and revise your own ideas.",
      ("Present this as a requirement on students ('required', recorded as must) in the honours degree at FHEQ level 6 and FQHEIS level 10. "
       "Cite it as " + CIT + "3.6, item b. Do not claim it sets a mark or a rung. "
       "Set it beside the rung row 4.5.b25 to 4.5.b27 (weighing competing theories), qaa/fheq-2024/4.15.b7 and Annex D's qaa/fheq-2024/annex-d/cognitive/r2/3rd."),
      ("Raise this when a student presents one theory as the obvious answer. "
       "Put it plainly as weighing explanations against each other. "
       "Ask: 'What would a rival theory make of the same evidence, and which explanation fits better and why?' Avoid reading the paragraph aloud."),
      type='requirement', find=T36[1])
prov('3.6.b3', 'should', ['enable', 'engage', 'apply'], 'engaging with public disputes and with values',
     "Criminology mirrors current social, political and public disputes, so students get chances to reflect on their own values and those around them and on how values shape rival readings of evidence; learning, teaching and assessment should let students engage with these disputes and apply criminological knowledge to current crime problems.",
     "Design learning, teaching and assessment so that students engage with live social and political disputes, reflect on their own values and apply criminological knowledge to current crime problems.",
     'learning, teaching and assessment should let students engage with live disputes and apply criminological knowledge to current problems',
     'para 1.8 (a reflective approach and own values), the rung row 4.5.b10 to 4.5.b12 and qaa/fheq-2024/4.15.b3.1',
     'a team plans assessment on contemporary crime problems',
     'Which assessments ask students to apply criminology to a live public dispute?', find=T36[2])
prov('3.6.b4', 'should', ['provide', 'designed', 'recognise'], 'inclusive strategies and distressing content',
     "Students come from diverse backgrounds with varying needs, so courses need flexible, varied strategies giving all as equal a chance as possible; approaches should be designed to be inclusive enough to make alternative assessment unnecessary, and everyone teaching should recognise the emotive nature of the subject and the impact of distressing content.",
     "Use flexible, varied teaching and assessment so all students have as equal a chance as possible, design for inclusion so alternative assessment is rarely needed and plan for the emotional impact of distressing material.",
     'teaching and assessment should be inclusive by design, and staff should recognise the impact of distressing content',
     'paras 1.12, 2.18 and 3.8', 'a team designs assessment or plans teaching of distressing topics',
     'How do you prepare and support students before they study distressing material?', find=T36[3])
prov('3.8', 'should', ['monitor', 'reflect'], 'monitoring assessment outcomes',
     "Assessment drives learning, progress and development, and serves to monitor progress, motivate, give feed-forward and grade against criteria; reasonable adjustments may be needed for inclusion, and course teams should monitor student outcomes, for example by protected characteristics, and reflect on assessment strategies.",
     "Monitor student outcomes, including by protected characteristics, to find unintended differences, reflect on assessment strategies and make reasonable adjustments to assessment where needed.",
     'course teams should monitor outcomes, including by protected characteristics, and reflect on assessment',
     'paras 1.13, 2.18 and 3.9', 'a team reviews assessment results or an awarding gap',
     'Do you break down your assessment outcomes by protected characteristics, and what have you changed as a result?')
prov('3.10', 'should', ['scaffolded', 'build'], 'scaffolded modules',
     "Modules in a criminology course should be scaffolded so that students can build on earlier learning as they progress.",
     "Scaffold modules so each builds on what students learned before, year on year.",
     'modules should be scaffolded so students build on earlier learning', 'paras 2.19 and 3.9 and spine:6',
     'a team maps modules across the years', 'Which earlier module does each final-year module build on?')

# ---------------------------------------------------------------- section 4
prov('4.2', 'should', ['assessed', 'allow', 'achieve'], 'curricula enabling the honours outcomes',
     "Students are assessed against their curricula, which should let them reach the required outcomes and show the higher learning of an honours degree; at base every class shows the student has reached level 6 (England, Wales and Northern Ireland) or level 10 (Scotland).",
     "Design curricula so that students can reach the required outcomes and show honours-level learning; every class of degree, a third included, means level 6 (FHEQ) or level 10 (FQHEIS) has been met.",
     'curricula should let students achieve the required outcomes and show the characteristics of FHEQ level 6 (FQHEIS level 10)',
     'paras 4.1, 4.4 and 4.5, the honours descriptor qaa/fheq-2024/4.15 and spine:6',
     'a team checks that module outcomes add up to the honours level',
     'Can you show where each honours-level outcome is assessed?', level='fheq:6')

# the rung table, read row by row: threshold, typical, excellent cells (skeleton ids 4.5.b1 to 4.5.b33)
ROWS = [
    ('key concepts and theories', 'knowledge', '4.15.b1', 'knowledge/r2',
     "Which criminological theory can you explain well, and where does it work less well in practice?",
     [(['describe', 'examine', 'evaluate'], 'describing and examining key concepts and theories', "set out and look closely at the main concepts and theories of criminology, and judge how well they work when applied"),
      (['describe', 'examine', 'evaluate'], 'critically examining key concepts and theories', "set out and critically interrogate the main concepts and theories of criminology, and judge how well they work when applied"),
      (['describe', 'examine', 'evaluate'], 'exceptional critical examination of key concepts and theories', "set out and critically interrogate, to an exceptional standard, the main concepts and theories of criminology, and judge how well they work when applied")]),
    ('victimisation and criminalisation', 'understanding', '4.15.b3.1', 'cognitive/r2',
     "How would a theory you know explain why some people or acts come to be treated as criminal?",
     [(['assess'], 'assessing processes of victimisation and criminalisation', "weigh up, using criminological theory, the political and social processes by which people are victimised and criminalised"),
      (['assess'], 'critically assessing processes of victimisation and criminalisation', "weigh up critically, using criminological theory, the political and social processes by which people are victimised and criminalised"),
      (['provide'], 'exceptional critical assessment of victimisation and criminalisation', "give an exceptionally critical appraisal, using criminological theory, of the political and social processes by which people are victimised and criminalised")]),
    ('social diversity and inequality', 'understanding', '4.15.b1', 'knowledge/r1',
     "How do class, gender, race or other social divisions shape the cases you have studied?",
     [(['provide'], 'an account of diversity and inequality in crime and its responses', "give an account of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them"),
      (['provide'], 'critical understanding of diversity and inequality in crime and its responses', "show a critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them"),
      (['demonstrate'], 'exceptional critical understanding of diversity and inequality', "show an exceptionally critical understanding of how social diversity and inequality shape crime, harm, deviance and victimisation and the ways societies respond to them")]),
    ('criminal justice agency practice', 'understanding', '4.15.b7', 'cognitive/r2',
     "Pick a criminal justice agency: how have its practices changed, and how would you judge them?",
     [(['evaluate'], 'evaluating criminal justice agency practice', "judge how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places"),
      (['evaluate'], 'critically evaluating criminal justice agency practice', "judge critically how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places"),
      (['evaluate'], 'exceptional critical evaluation of criminal justice agency practice', "judge critically, to an exceptional standard, how criminal justice agencies work and change, against shifting values and relationships among people, groups and public and private bodies in different places")]),
    ('governance, risk and rights in the treatment of lawbreakers', 'understanding', '4.15.b7', 'knowledge/r2',
     "What values and risks shape how people who break the law are dealt with in the UK systems you know?",
     [(['examine'], 'examining governance, risk and rights in dealing with lawbreakers', "look into the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law"),
      (['assess'], 'critically assessing governance, risk and rights in dealing with lawbreakers', "appraise critically the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law"),
      (['demonstrate'], 'exceptional critical assessment of governance, risk and rights', "give an exceptionally critical appraisal of the governance, risk management and human rights values and processes that shape how UK criminal justice systems, and the agencies that run sentences and their alternatives, treat people who break the law")]),
    ('human rights and harm prevention', 'subject-skill', '4.15.b3.1', 'cognitive/r3',
     "How would you use a human rights argument to judge a measure meant to keep people safe?",
     [(['apply', 'evaluate'], 'applying human rights to judge harm prevention', "use ideas of human rights to judge efforts to prevent harm and keep people safe"),
      (['provide', 'apply', 'evaluate'], 'critical use of human rights to judge harm prevention', "understand ideas of human rights critically and use them to judge, critically, efforts to prevent harm and keep people safe"),
      (['provide', 'evaluate'], 'exceptional critical use of human rights to judge harm prevention', "show an exceptionally critical understanding and use of ideas of human rights, judging critically efforts to prevent harm and keep people safe")]),
    ('research strategies and methods', 'subject-skill', '4.15.b2', 'practical/r1',
     "For your research question, which method fits best, and why not the others?",
     [(['use', 'assess', 'identify'], 'using and choosing research strategies and methods', "use a variety of research strategies and methods, judge when each fits and choose a suitable strategy for a given research problem"),
      (['use', 'assess', 'identify'], 'critically choosing research strategies and methods', "use a variety of research strategies and methods, judge critically when each fits and choose a suitable strategy for a given research problem"),
      (['use', 'provide', 'identify'], 'accurate, exceptional choice of research strategies and methods', "use a variety of research strategies and methods accurately, appraise to an exceptional standard when each fits and choose a suitable strategy for a given research problem every time")]),
    ('comparative analysis', 'subject-skill', '4.15.b7', 'cognitive/r2',
     "What does comparing two places or systems show you, and what can it hide?",
     [(['evaluate'], 'evaluating the use of comparison', "judge the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them"),
      (['evaluate'], 'critically evaluating the use of comparison', "judge critically the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them"),
      (['evaluate'], 'exceptional critical evaluation of comparison', "judge critically, to an exceptional standard, the strengths and weaknesses of comparative approaches to crime, harm, deviance and victimisation and to how societies deal with them")]),
    ('analysing empirical data', 'subject-skill', '4.15.b6', 'practical/r4',
     "What do the figures and accounts you have gathered say about the theories you are testing?",
     [(['summarise', 'analyse', 'evaluate'], 'summarising and analysing data to weigh theories', "summarise and analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories"),
      (['summarise', 'analyse', 'evaluate'], 'critical analysis of data to weigh theories', "summarise and critically analyse quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, so as to weigh rival criminological theories critically"),
      (['provide', 'evaluate'], 'exceptional summary and critical analysis of data', "summarise and critically analyse, to an exceptional standard, quantitative and qualitative evidence on crime, harm, deviance, victimisation and how societies respond, weighing rival theories critically")]),
    ('explaining complex social problems', 'understanding', '4.15.b3.1', 'cognitive/r3',
     "Choose a social problem: how would two theories explain it differently?",
     [(['explain', 'evaluate'], 'explaining and evaluating complex social problems', "explain and judge complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance"),
      (['explain', 'evaluate'], 'explaining and critically evaluating complex social problems', "explain and judge critically complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance"),
      (['provide'], 'exceptional critical explanation of complex social problems', "explain and judge critically, to an exceptional standard, complex social problems using criminological theories about crime, social class, victimisation and how societies respond to crime and deviance")]),
    ('what sets criminology apart', 'knowledge', '4.15.b4', 'knowledge/r2',
     "What makes a criminological explanation different from a journalistic or a legal one?",
     [(['analyse'], 'analysing how criminology differs from other understandings', "analyse how criminology differs from other ways of understanding crime and society"),
      (['analyse'], 'critically analysing how criminology differs from other understandings', "analyse critically how criminology differs from other ways of understanding crime and society"),
      (['demonstrate'], 'exceptional critical analysis of what sets criminology apart', "show an exceptionally critical analysis of how criminology differs from other ways of understanding crime and society")]),
]
RNG = [('threshold', 'threshold', 'At the threshold (third-class) level', 'To reach the threshold standard'),
       ('typical', 'should', 'At the typical (2:2 and 2:1) level', 'To reach the typical standard'),
       ('excellent', 'should', 'At the excellent (first-class) level', 'To reach the excellent standard')]
GRADE = {}
OUT = []
for r, (short, dom, fh, ad, ask, cells) in enumerate(ROWS, 1):
    ids = ['4.5.b%d' % (3 * (r - 1) + c) for c in (1, 2, 3)]
    th, ty, ex = ids
    for c, ((verbs, about, do), (rung, force, lead, blead)) in enumerate(zip(cells, RNG)):
        i = ids[c]
        if rung == 'threshold':
            prac = f"At threshold, set teaching and assessment so that every honours graduate can {do}; this is the minimum for the award."
            aaw = (f"Treat this as the threshold outcome on {short}: the minimum every honours graduate in criminology is expected to show, at third-class level (FHEQ level 6, FQHEIS level 10). "
                   f"Cite it as {CIT}4.5, threshold column, row {r}. Do not call it a regulatory requirement or apply it to master's study. "
                   f"Set it beside the typical cell {ty}, the excellent cell {ex}, the honours descriptor qaa/fheq-2024/{fh}, Annex D's cell qaa/fheq-2024/annex-d/{ad}/3rd and spine:6.")
            aad = (f"Raise this when a student asks what passing with honours means for {short}, or when a team checks that a module secures the minimum. "
                   f"Tell a student in plain words what you need to be able to do; with staff, frame it as the floor every assessment route must reach. "
                   f"Ask: '{ask}' Do not read the cell out at length or treat the typical or excellent cell as the pass mark.")
        elif rung == 'typical':
            prac = f"At the typical level (2:2 and 2:1), most graduates should be able to {do}; design assessment so they can show it."
            aaw = (f"Treat this as the typical outcome on {short}: what most honours graduates in criminology should reach at lower or upper second-class level (FHEQ level 6, FQHEIS level 10), not the minimum. "
                   f"Cite it as {CIT}4.5, typical column, row {r}. Do not present it as a pass requirement or as a regulatory standard. "
                   f"Set it beside the threshold cell {th}, the excellent cell {ex}, the honours descriptor qaa/fheq-2024/{fh} and Annex D's cells qaa/fheq-2024/annex-d/{ad}/2.2 and qaa/fheq-2024/annex-d/{ad}/2.1.")
            aad = (f"Raise this when a student wants to know what a good second-class answer on {short} looks like, or when staff calibrate marking. "
                   f"Explain it in plain words as the usual standard, above the minimum; with staff, use it to describe the middle bands. "
                   f"Ask: '{ask}' and 'Where is your work more descriptive than critical?' Do not present it as the minimum needed to pass.")
            GRADE[i] = th + '|stated'
        else:
            prac = f"At the excellent level (first class), graduates should be able to {do}; design assessment with room to show it."
            aaw = (f"Treat this as the excellent outcome on {short}: an aspiration that marks first-class work in an honours degree in criminology (FHEQ level 6, FQHEIS level 10). "
                   f"Cite it as {CIT}4.5, excellent column, row {r}. Do not present it as required for the award or as a master's standard. "
                   f"Set it beside the typical cell {ty}, the threshold cell {th}, the honours descriptor qaa/fheq-2024/{fh} and Annex D's first-class cell qaa/fheq-2024/annex-d/{ad}/1st.")
            aad = (f"Raise this when a student aims for a first or asks how to stretch their work on {short}. "
                   f"Put it as an aspiration in plain words; with staff, use it to describe what lifts work into the top band. "
                   f"Ask: '{ask}' and 'What would make your analysis exceptional rather than sound?' Never present it as what everyone must reach.")
            GRADE[i] = ty + '|stated'
        s(i, type=rung, rung=rung, force=force, level='fheq:6', appliesTo=f'honours graduates at the {rung} level', addressee='learner',
          verbs=verbs, about=about, domain=dom, award=HON,
          para=f"{lead}, a graduate should be able to {do}.", prac=prac, ben=f"{blead}, you should be able to {do}.", aaw=aaw, aad=aad)
    OUT.append(dict(outcome=short, threshold=th, typical=ty, excellent=ex, basis='stated', domain=dom, award=HON))
OUT.append(dict(outcome='philosophy of explanation and research strategy', threshold='2.2', typical='2.2.typical', excellent='2.3', basis='inferred', domain='understanding', award=HON))
GRADE['2.2.typical'] = '2.2|stated'
GRADE['2.3'] = '2.2.typical'

# master's threshold outcomes (4.6)
MAS = [
    (1, ['informed'], 'systematic understanding of criminological topics', 'knowledge', '4.17.b1',
     "show systematic understanding of, and critical awareness about, topics shaped by criminology",
     "a master's student asks how much depth is expected across the field", "Which topics in your field do you know systematically, and where are the gaps?"),
    (2, ['inform', 'influence'], 'history of ideas and social and political theory', 'understanding', '4.17.b1',
     "show critical awareness of how ideas developed over time, their cultural setting and the social and political theories that shape criminological practice",
     "a student treats theory as fixed rather than shaped by history and politics", "Where did the ideas behind your topic come from, and whose politics do they carry?"),
    (3, [], 'the intersectionality of power', 'understanding', '4.17.b1',
     "show critical awareness of how intersecting forms of power bear on criminal justice agencies and on responses to crime, harm, deviance and victimisation",
     "a student analyses inequality one dimension at a time", "How do class, race, gender and other forms of power combine in the case you are studying?"),
    (4, ['identify', 'dealing', 'design'], 'methodologies and an own research design', 'subject-skill', '4.17.b4.2',
     "pick suitable methodologies for complex problems and design an original research project",
     "a master's student plans a dissertation", "Why is this methodology the right one for your problem, and what would make you change it?"),
    (5, ['develop', 'work'], 'critical discussion, independence and originality', 'generic-skill', '4.17.b6',
     "carry critical discussion and analysis of complex ideas forward and work independently with some originality",
     "a student relies heavily on supervision or on summary", "What in your argument is your own, and how did you reach it without being told?"),
    (6, ['complete'], 'a substantial research project', 'subject-skill', '4.17.b3',
     "complete a substantial empirical project, systematic review or systematic case study grounded in broad current understanding of the subject",
     "a student scopes a final project", "Is your project substantial enough, and which current work in the field does it build on?"),
]
for k, verbs, about, dom, fh, do, when, ask in MAS:
    s('4.6.b%d' % k, type='threshold', rung='threshold', force='threshold', level='fheq:7', appliesTo="holders of a master's degree in criminology",
      addressee='learner', verbs=verbs, about=about, domain=dom, award=MA,
      para=f"Beyond the honours outcomes, a master's graduate should be able to {do}.",
      prac=f"At master's level, make sure graduates can {do}; this adds to the honours outcomes.",
      ben=f"On a master's course in criminology, you should be able to {do}.",
      aaw=(f"Treat this as a threshold outcome for a master's degree in criminology, added to the honours outcomes, at FHEQ level 7 and FQHEIS level 11 (levels inferred from the award). "
           f"Cite it as {CIT}4.6. Do not claim it applies to the honours degree or that it is a regulatory requirement. "
           f"Set it beside the master's descriptor qaa/fheq-2024/{fh}, spine:7, para 2.4 and the honours outcomes in para 4.5."),
      aad=(f"Raise this with master's students or a postgraduate course team when {when}. "
           f"Put it plainly as what a master's graduate should be able to show. Ask: '{ask}' "
           f"Do not read the list aloud or apply it to undergraduates."))

TH = {'1.10': 'theme:edi', '1.11': 'theme:edi', '1.12': 'theme:edi', '1.13': 'theme:edi', '1.14': 'theme:edi',
      '1.15': 'theme:esd', '1.16': 'theme:esd', '1.17': 'theme:esd', '1.18': 'theme:esd', '1.20': 'theme:esd', '1.21': 'theme:esd', '1.22': 'theme:esd',
      '1.24': 'theme:enterprise', '1.27': 'theme:enterprise', '2.18': 'theme:accessibility'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.20; 4.2; 4.5'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.20; 4.2; 4.5'),
                  dict(id='fheq:7', role='inferred', locator="D1, 2.4; 4.6 (master's degree; level from std:doc:qaa-fheq-2024-framework S5, Table 1)"),
                  dict(id='fqheis:11', role='inferred', locator="D1, 4.6 (master's degree; shares the FHEQ level 7 descriptor, std:doc:qaa-fheq-2024-framework S5)")],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.20; 4.2; 4.5)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='shared-descriptor', basis='inferred (std:doc:qaa-fheq-2024-framework S5; Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.9', '1.10', '1.11', '1.12', '1.13', '1.14']),
      dict(id='theme:esd', role='carries', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.24', '1.25', '1.26', '1.27']),
      dict(id='theme:accessibility', role='carries', carriedIn=['2.17', '2.18'])]

S7 = [dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='4.5: the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees'),
      dict(rel='thresholdAt', target='std:doc:qaa-fheq-2024-framework, 4.15 (fheq:6)', note='2.20; 4.2: each class means level 6 has been achieved'),
      dict(rel='readWith', target='std:doc:qaa-fqheis-2024-framework, 4.16 (fqheis:10)', note='2.20; 4.2'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.19 and 1.21 quote it; 1.23 points to QAA\'s ESD pages'),
      dict(rel='refersTo', target='British Society of Criminology, Statement of Ethics', note='2.12; not yet ingested (Part E)'),
      dict(rel='refersTo', target="British Sociological Association, Code of Ethics", note='2.12; not yet ingested (Part E)'),
      dict(rel='refersTo', target="Economic and Social Research Council, guidelines for research training", note='1.4; not yet ingested (Part E)')]

SB1 = [
    "Criminology studies how people and acts are criminalised and victimised, what crime, harm and deviance mean and what causes them, how they are prevented and managed and how they are represented (D1, 1.6)",
    "A multidisciplinary field first taught in the UK at postgraduate level from the late 1950s; undergraduate degrees came later (D1, 1.4)",
    "Its theories and areas of enquiry keep changing, fed by staff research and by neighbouring subjects such as sociology, law and philosophy, while its core stays steady (D1, 1.5)",
    "Theoretical and empirical at once, with practical application; many of its theoretical advances have come from empirical studies (D1, 3.2; 3.3)",
    "Marked by debate over how to explain its subject, put theory into research, inform policy and human rights, handle data and manage research ethics (D1, 3.1)",
    "Contested values in what counts as crime, harm, criminalisation and victimisation lie at its centre (D1, 3.4)",
    "Joins scholarship and practice, working with justice agencies, government and charities in research and teaching partnerships (D1, 1.17; 2.26 to 2.30)",
    "Its material is often emotive and distressing, so ethics and care run through its teaching and research (D1, 1.18; 3.6)",
    "Taught as single or joint honours, with foundation degrees leading towards the honours standard and master's degrees going beyond it (D1, 1.1; 1.3)"]

SB2 = [dict(theme='theme:edi', inThisSubject="Inclusion is part of the subject matter (discrimination, colonialism, bias in justice) and a duty on course teams: embedded curricula, belonging, safe dialogue on sensitive topics, review for barriers and attention to a diverse intake (D1, 1.9 to 1.14)",
            statements=['1.10', '1.11', '1.12', '1.13', '1.14', '3.6.b4', '3.8']),
       dict(theme='theme:esd', inThisSubject="Sustainability means both a current curriculum (green, queer and southern criminology, zemiology) and education for sustainable development: green criminology, ethics, global citizenship and placements linked to sustainability (D1, 1.15 to 1.23)",
            statements=['1.15', '1.16', '1.17', '1.18', '1.20', '1.21', '1.22']),
       dict(theme='theme:enterprise', inThisSubject="Named with employability: methodological and research-ethics skills, wide career routes including policing and probation and employability opportunities with safeguards (D1, 1.24 to 1.27)",
            statements=['1.24', '1.27']),
       dict(theme='theme:accessibility', inThisSubject="Varied entry routes and a single-tier approach: adjustments, varied formats for all, fair access to fieldwork and placements, accessible materials and criteria (D1, 2.17; 2.18; 3.5)",
            statements=['2.18', '3.5'])]

SB3 = dict(areas=[dict(component='1.6', gloss='the concerns of criminology: criminalisation, victimisation, causes, prevention, responses and representation'),
                  dict(component='1.8', gloss='core areas for single and joint honours, from the history of the discipline to ethics in research'),
                  dict(component='2.6', gloss='qualitative approaches at a basic level (illustrative list)'),
                  dict(component='2.8', gloss='quantitative techniques at a basic level (illustrative list)'),
                  dict(component='3.1', gloss='the debates that characterise modern criminology'),
                  dict(component='3.2', gloss='theory and evidence across state crime, crimes of the powerful, security and digital crime')],
           practices=[dict(component='1.27', kind='learning', gloss='employability through placements, volunteering and guest speakers'),
                      dict(component='2.24', kind='teaching', gloss='a wide and flexible range of teaching styles'),
                      dict(component='2.30', kind='learning', gloss='placements, field trips and work-based modules through partnerships'),
                      dict(component='3.5', kind='learning', gloss='modes of study and resources, which need to be accessible'),
                      dict(component='3.6', kind='teaching', gloss='four principles: theory and evidence, rival readings, values, inclusion'),
                      dict(component='3.7', kind='teaching', gloss='lectures, seminars, tutorials, placements, online and fieldwork'),
                      dict(component='3.8', kind='assessment', gloss='purposes of assessment; monitoring outcomes'),
                      dict(component='3.9', kind='assessment', gloss='what assessment methods take into account'),
                      dict(component='3.10', kind='teaching', gloss='scaffolding modules across the years')])

SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=11),
                  dict(rung='threshold', leadIn='2.2', award=HON, items=1),
                  dict(rung='threshold', leadIn='4.6', award=MA, items=6),
                  dict(rung='typical', leadIn='4.5', award=HON, items=11),
                  dict(rung='typical', leadIn='2.2', award=HON, items=1),
                  dict(rung='excellent', leadIn='4.5', award=HON, items=11),
                  dict(rung='excellent', leadIn='2.3', award=HON, items=1)],
           rungBases="4.4 names three rungs for the honours graduate: threshold (3rd class), typical (2:2 or 2:1) and excellent (1st class); 4.5 is one table with three columns, each row stating one outcome three times in rising wording, so gradeOf is stated by row; 2.2 (threshold and typical jointly) and 2.3 (excellent) set research-philosophy rungs; 4.6 gives threshold standards for postgraduate (master's) degrees",
           outcomeLists=[],
           outcomes=OUT)

SB4A_FULL = []

SB5 = [dict(body='British Society of Criminology', says='the UK professional body for criminology; it contributed to the thinking behind the statement, and its Statement of Ethics is an example of the codes students should know (D1, 1.2; 2.12)', requirements='not yet ingested (Part E)'),
       dict(body='British Sociological Association', says='its Code of Ethics is a second example of the codes criminologists use (D1, 2.12)', requirements='not yet ingested (Part E)'),
       dict(body='Economic and Social Research Council', says='its research training guidelines often guide postgraduate courses (D1, 1.4)', requirements='not yet ingested (Part E)'),
       dict(body='College of Policing', says='with the National Probation Service, its workforce development positions criminology as an applied and theoretical qualification (D1, 1.26)', requirements='not yet ingested (Part E)'),
       dict(body='National Probation Service', says='named with the College of Policing for developing the criminal justice workforce (D1, 1.26)', requirements='not yet ingested (Part E)'),
       dict(body='Advance HE', says='publishes the ESD guidance jointly with QAA and supports its principles (D1, 1.19)', requirements='std:doc:qaa-advancehe-esd-2021-guidance'),
       dict(body='professional and regulatory bodies (unnamed)', says='may evaluate and accredit courses with professional and vocational outcomes, through visits and desk review (D1, 2.34)', requirements='not yet ingested (Part E)')]

SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.8', '1.9', '1.10', '1.11', '1.12', '1.13', '1.14', '1.18', '2.18', '3.6', '3.8'], statements=['1.10', '1.11', '1.12', '1.13', '1.14', '3.6.b4', '3.8']),
                   dict(id='theme:esd', named='Sustainability; Education for Sustainable Development (ESD)', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23'], statements=['1.15', '1.16', '1.17', '1.18', '1.20', '1.21', '1.22']),
                   dict(id='theme:enterprise', named='Entrepreneurship and enterprise education; employability', carriedIn=['1.24', '1.25', '1.26', '1.27'], statements=['1.24', '1.27']),
                   dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.11', '1.17', '1.18', '1.27', '2.17', '2.18', '3.5'], statements=['2.18', '3.5'])],
           frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.20', '4.2', '4.5']),
                       dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.20', '4.2', '4.5'])],
           bodies=[dict(body='British Society of Criminology', citedIn=['1.2', '2.12']),
                   dict(body='British Sociological Association', citedIn=['2.12']),
                   dict(body='Economic and Social Research Council', citedIn=['1.4']),
                   dict(body='College of Policing', citedIn=['1.26']),
                   dict(body='National Probation Service', citedIn=['1.26']),
                   dict(body='Advance HE', citedIn=['1.19']),
                   dict(body='professional and regulatory bodies (unnamed)', citedIn=['2.34']),
                   dict(body='partners named as examples: police forces, Ministry of Justice, prisons, probation, youth justice, local government, Europol, UNODC, UK and international NGOs', citedIn=['2.27', '2.28', '2.29'])],
           sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.5'], role='further detail on typical expectations at each classification'),
                            dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Advance HE and QAA (2021); ESD Guidance, 2021', citedIn=['1.19', '1.21'], role='definition and aims of education for sustainable development'),
                            dict(document='not yet ingested: QAA web pages on ESD (Quality Code advice), listed in Part E', named='www.qaa.ac.uk/quality-code/education-for-sustainable-development', citedIn=['1.23'], role='further guidance on developing ESD'),
                            dict(document='not yet ingested: listed in Part E', named="British Society of Criminology's Statement of Ethics; British Sociological Association's Code of Ethics", citedIn=['2.12'], role='examples of ethics codes students should know')])

B1 = [dict(slug='green-criminology', definition='the study of crimes that harm the environment, of ecological justice and of environmental law and criminality, from individual and corporate crime to state failure (D1, 1.16)',
           beneficiaryDefinition='the part of criminology that looks at harm to the environment and at justice for the natural world',
           scopeNote='named with queer and southern criminology, indigenous knowledge and zemiology as emerging approaches (D1, 1.15)', category='unknown', practices=['education']),
      dict(slug='ethical-literacy', definition='a level of ethical understanding enough to keep research participants safe and well (D1, 2.16)',
           beneficiaryDefinition='knowing research ethics well enough to protect the people you study', scopeNote='the summary of paras 2.12 to 2.15', category='unknown', practices=['education']),
      dict(slug='mixed-methods-research', definition='research that combines qualitative and quantitative strategies (D1, 2.2; 2.11)',
           beneficiaryDefinition='research that uses both numbers and accounts', scopeNote='with triangulation and data integration (2.11)', category='unknown', practices=['education'])]
B2A = [dict(concept='green-criminology', form='green criminology', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='ethical-literacy', form="'ethical literacy'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='mixed-methods-research', form='mixed methods research', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []

D3 = [dict(source="British Society of Criminology, Statement of Ethics", why='named as an example code in 2.12; a body document to ingest as its own standards document'),
      dict(source="British Sociological Association, Code of Ethics", why='named as an example code in 2.12'),
      dict(source='Economic and Social Research Council, guidelines for research training', why='named in 1.4 as guiding postgraduate courses')]

E = [
    "Rung shape (new against Psychology): 4.5 is one three-column table (threshold 3rd class; typical 2:2 and 2:1; excellent 1st class) whose eleven rows each state one outcome three times in rising wording ('critically', 'to an exceptional level'). Each cell has its own span, so each keeps its skeleton id (4.5.b1 to 4.5.b33, read row by row: threshold, typical, excellent) rather than the `.typical` and `.excellent` suffixes the batch-1 convention uses for one shared span; gradeOf is stated by row.",
    "Skeleton corrections: the skeleton marked all 33 table cells typical and 4.3.b1 to 4.3.b4 and 4.6.b1 to 4.6.b6 threshold. Rungs judged by column; 4.3's four items are kinds of evidence (knowledge and understanding, cognitive, practical and transferable skills), not statements; 4.6's items are threshold standards for the master's degree.",
    "Rung lead-ins also in section 2 (new against Psychology): 2.2 sets one research-philosophy expectation for threshold and typical jointly (recorded twice on one span, 2.2 and 2.2.typical, gradeOf stated as the same text); 2.3 sets the excellent rung (gradeOf 2.2.typical, inferred: the issuer pairs the paragraphs by heading, not by item); 2.4 the postgraduate level.",
    "Typical rung spans two classes (2:2 and 2:1) as one rung; Annex D splits them. Recorded as one rung.",
    "Master's (4.6): 'threshold standards for a postgraduate degree', in addition to the honours ones; award master's; level fheq:7 and fqheis:11 inferred from the FHEQ Table 1 (std:doc:qaa-fheq-2024-framework S5), not stated. 2.4, 2.10, 2.14 and 2.15 say 'postgraduate' or 'higher or postgraduate' without naming the award.",
    "Force: the 4.5 and 4.6 lead-ins say 'should be able to'. Threshold cells and 4.6 items take force threshold (4.1 and 4.3 define the threshold as the minimum for the award); typical and excellent cells take should.",
    "Obliging words outside the five, recorded as describes, for Abbott: 'expected to' or 'there is an expectation' (1.24, 2.1, 2.4 to 2.10, 2.13, 2.15, 2.16, 2.19, 2.20, 2.25); 'requirement' and 'is needed' in 2.25 (said of most courses only, so not must); 'important to ensure' (3.5); 'need to' (3.6 item d, recorded with its should); 'responsibility' (1.10, recorded with its must); 'has to' (1.15); 'necessity' (1.25, not recorded). 'Required' in 3.6 item b is recorded as must.",
    "Mixed modals in one paragraph: 1.12 and 1.13 carry both should and must; recorded must, with the should parts kept as should in the paraphrase. 2.2, 2.12 and 2.14 mix 'expected to' with should; recorded should.",
    "Illustrative method lists (2.6 to 2.10, 2.13: 'may include', 'some of the following', 'such as'): each paragraph is one statement; the list items (2.6.b1 to 2.13.b4 in the skeleton) are not cut as statements because the issuer offers them as a menu. For P3.",
    "Plain-present provider norms and content lists, not statements (template open point 5): 1.6 and 1.8 (what criminology is concerned with; core areas courses 'include'), 2.24 ('courses ... include'), 2.30 ('Most Criminology courses ... will include'), 3.1 (debates that characterise the field), 3.9 (assessment 'take[s] account of, as a minimum'), 4.3 ('this will include'), and the 'students are given opportunities' sentences in 3.6 items a to c. 1.6, 1.8 and 3.1 are recorded as SB3 areas.",
    "Not recorded though worded with will or should: 1.2 and 4.1 (what the statement sets out), 1.7 (a reading instruction), 2.33 ('Typically, external examiners will be asked': descriptive), 1.25 and 1.26 (descriptive).",
    "3.6 has lettered items a) to d) inside one numbered paragraph; cut as 3.6.b1 to 3.6.b4 by find, in the issuer's order.",
    "Stage words in section 2 ('basic', 'higher or more advanced', 'higher or postgraduate', 'all levels') are stages of study, not framework levels; honours-only records carry the award's level fheq:6, mixed honours and postgraduate records carry level none.",
    "Provider duties carry domain none, as in Psychology run 0043; SB-4 asks for one of the four values on every benchmark standard. For Abbott.",
    "Subject codes: HECoS 100484 criminology (stated, by name); HECoS 100483 criminal justice (stated as a postgraduate specialism, 1.4); CAH15-01-02 is inferred, being HECoS 100484's CAH3 mapping, labelled sociology, which the text does not name as this subject. Policing (100486) and forensic psychology (100387) appear only in S2 statedSubjects as specialisms (1.4), not in the lookup subjects.",
    "Inferred gradeOf link: 2.3 to 2.2.typical. All 22 table links are stated by row.",
    "Inferred crosswalk: fheq:7 to fqheis:11 (from the FHEQ document, not this one).",
    "No CQFW citation in the text; Wales appears only through the Quality Assessment Framework for Wales in the front matter.",
    "Front matter (excluded) names the Office for Students' regulatory framework, the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland), the Quality Code's Advice and Guidance and QAA's Glossary; back matter names the Disabled Students' Commission. Not in SB6, being in excluded matter.",
    "The issuer's sub-headings run into the end of the preceding paragraph in the held text (for example 'Purposes of a Criminology degree' ends 1.4), so some `source` spans end with the next heading.",
    "Extraction artefacts in the held text: 'saf e' (1.11, 1.12, 1.13), 'successf ul' (1.25, 4.6.b6), 'f ast' (2.13). Sources carry them as held.",
    "Employability is named with entrepreneurship and enterprise in the key changes and in 1.25 to 1.27; recorded under theme:enterprise, no separate theme id.",
    "Partners named in 2.27 to 2.29 (police forces, Ministry of Justice, Europol, UNODC, charities and NGOs) are research partners, not PSRBs; grouped as one SB6 body entry, not in SB5.",
    "Section order differs from Psychology: the cross-cutting themes sit inside section 1, and research-methods expectations by level sit in section 2 before the section 4 table.",
    "ESD pages on QAA's website (1.23) not ingested; the ESD guidance itself is std:doc:qaa-advancehe-esd-2021-guidance.",
    "SB-10: 4.2 cites level 6 and level 10 'of the respective qualification frameworks' without naming the FHEQ or FQHEIS; recorded in SB6 for both frameworks."]
