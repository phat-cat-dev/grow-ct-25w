# bm_content.py: run 0112, QAA Subject Benchmark Statement: Housing Studies (March 2022), std run agent.
# Every judgement for tools/bm_build.py. Written fresh from the held text (benchmark rule 6); our words except `source`.
HON = "bachelor's with honours"
MA = "master's"
SID = 'qaa/housing-studies-2022/'
CITE = 'QAA, 2022, Housing Studies Subject Benchmark Statement, para '

META = dict(
    run='0112', p1='2026-10-03 17:45',
    title='Subject Benchmark Statement: Housing Studies',
    heading='Subject Benchmark Statement: Housing Studies (QAA, March 2022)',
    edition='March 2022 (fourth edition)', published='2022-03',
    status='current',
    supersedes='the third edition (2019), named in the membership section; the front matter refers to the previous Statement',
    subjects=[dict(scheme='hecos', code='100196', label='housing', basis='stated'),
              dict(scheme='cah', code='CAH13-01-04', label='planning (urban, rural and regional)', basis='inferred')],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision (fourth edition of Housing Studies)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it explains in passing',
    agentDefinition=(
        "An agent reading this document meets the UK sector reference point for Housing Studies degrees: what an honours "
        "graduate must understand at the threshold (19 items, para 4.3), what a master's graduate adds (para 4.6 and 4.7), the "
        "transferable skills both awards share (para 4.8) and the expectations the statement sets for course design, teaching "
        "and assessment, above all on inclusion, sustainability and employability. The typical and excellent rungs are not "
        "listed: the statement hands them to each provider's marking scheme and to Annex D of the qualification frameworks. "
        "Cite statements by their S4 ids and the issuer's paragraph numbers; read the honours items against FHEQ Level 6 and "
        "the master's items against FHEQ Level 7."),
    summary=(
        "Housing studies is an interdisciplinary, vocational field built on the household's need for a home, drawing on the "
        "social sciences, law, health, planning and the built environment. The statement covers bachelor's degrees with honours "
        "(FHEQ Level 6, FQHEIS Level 10) and master's degrees (FHEQ Level 7, FQHEIS Level 11) and informs foundation degrees "
        "and housing modules elsewhere. It states one rung list, the threshold (19 items, para 4.3), and leaves the typical "
        "(2:1, 2:2) and excellent (1st) rungs to providers' marking schemes (para 4.4, 4.5) with Annex D as the reference "
        "(para 4.2); it adds four master's outcomes (para 4.6), a pointer to the FHEQ Level 7 descriptor (para 4.7) and eight "
        "transferable skills for both awards (para 4.8). Three cross-cutting themes run through it: equality, diversity and "
        "inclusion; education for sustainable development, built on the UN SDGs and UNESCO's key competencies; and "
        "employability and enterprise education; accessibility has its own section. The Chartered Institute of Housing is "
        "the one professional body, accrediting many courses and offering its own progression route."),
    authority='reference: a sector reference point published by QAA as a membership organisation; not a sector-recognised standard in England, a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs="what can be expected of a Housing Studies graduate at honours and master's level, and the nature of courses in the subject",
    awards=[HON, MA, "informs: foundation degrees and housing modules in other courses"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"The Statement explicitly sets out the nature and academic standards of bachelor\'s degrees with honours and master\'s degrees carrying this subject in their title or containing Housing Studies as a significant part of their course content, for the subject community of housing studies." (D1, 1.6)',
    statedSubjects=[
        dict(name='Housing Studies', locator='(D1, 1.6)', kind='subject', codes=[dict(scheme='hecos', code='100196', label='housing')]),
        dict(name='foundation degrees in Housing Studies; modules with substantial housing or homelessness content in urban studies, geography, planning, health, social work and social care', locator='(D1, 1.6)', kind='programme title', codes=[]),
        dict(name='Housing Studies joint honours', locator='(D1, 2.7)', kind='programme title', codes=[dict(scheme='hecos', code='100196', label='housing')])])

SECTIONS = {'1': 'Context and purposes of a Housing Studies degree', '2': 'Distinctive features of a Housing Studies degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.7', 'Purposes of a Housing Studies degree'),
       ('1.8', '1.11', 'Characteristics of a Housing Studies degree'), ('1.12', '1.19', 'Equality, diversity and inclusion'),
       ('1.20', '1.21', 'Sustainability'),
       ('1.22', '1.23', 'Sustainability: developing sustainable development knowledge in housing studies'),
       ('1.24', '1.25', 'Sustainability: developing sustainable development competencies'),
       ('1.26', '1.30', 'Sustainability: developing learning environments to promote sustainable development'),
       ('1.31', '1.35', 'Employability and enterprise education'),
       ('2.1', '2.4', 'Design'), ('2.5', '2.6', 'Accessibility'), ('2.7', '2.12', 'Progression'), ('2.13', '2.14', 'Flexibility'),
       ('2.15', '2.15', 'Partnership'), ('2.16', '2.19', 'Monitoring and review'),
       ('3.1', '3.1', 'Content'), ('3.2', '3.4', 'Teaching, learning and assessment'), ('3.5', '3.14', 'Teaching and learning'),
       ('3.15', '3.20', 'Assessment'),
       ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level (3rd class)'), ('4.4', '4.4', 'Typical level (2:1 or 2:2)'),
       ('4.5', '4.5', 'Excellent level (1st class)'), ('4.6', '4.7', "Master's level degrees in Housing Studies"),
       ('4.8', '4.8', 'Transferable and generic skills')]

G = {
    '1.1': 'an interdisciplinary field since the 1980s, now international in reach',
    '1.2': 'starting point: the need for a home; production, consumption, rights, health',
    '1.3': 'the disciplines it draws on and the aim of the education',
    '1.4': 'students arrive by many routes; a strong vocational strand; CIH accreditation',
    '1.5': 'academic, vocational and professional dimensions combined',
    '1.6': 'scope: honours and master\'s, informing foundation degrees and modules',
    '1.7': 'the CIH\'s role and the statement\'s distance from its specification',
    '1.8': 'levels, locations in faculties and modes of study',
    '1.9': 'a framework, not a prescription of how outcomes are reached',
    '1.10': 'devolved governance reflected in courses across the four nations',
    '1.11': 'three complementary themes run through the statement',
    '1.12': 'courses uphold the Equality Act 2010',
    '1.13': 'social justice and an inclusive curriculum at the core',
    '1.14': 'co-produced knowledge and psychologically informed learning spaces',
    '1.15': 'graduates confident to challenge decision makers',
    '1.16': 'themes of inclusive housing knowledge (eight listed)',
    '1.17': 'questions for an inclusivity lens (twelve listed)',
    '1.18': 'inclusive learning experiences (five listed)',
    '1.19': 'inclusive behaviours of students and graduates (nine listed)',
    '1.20': 'ESD and the UN SDGs; the UNESCO statement quoted',
    '1.21': 'ESD as a lens linking economy, society and environment',
    '1.22': 'courses aimed at the SDGs\' social, economic and environmental concerns',
    '1.23': 'SDG 11 and the other goals that bear on housing',
    '1.24': 'the eight UNESCO key competencies, adapted for housing (Figure 2)',
    '1.25': 'ESD outcomes linking subject knowledge, competencies and SDGs',
    '1.26': 'the learning environment that ESD needs',
    '1.27': 'campus and community as a living laboratory',
    '1.28': 'sustainable development embedded in curriculum design',
    '1.29': 'ESD across content, teaching, structure and assessment',
    '1.30': 'ESD content: physical integrity, social justice, economic development',
    '1.31': 'a vocational subject with entrepreneurial attributes',
    '1.32': 'careers across sectors; placements and work-related activity',
    '1.33': 'entrepreneurship education beyond employment (Figure 3)',
    '1.34': 'transferable and self-management skills of graduates',
    '1.35': 'graduate knowledge, reflection, ethics and resilience',
    '2.1': 'interdisciplinary design around functional knowledge and skills',
    '2.2': 'CIH standards woven into a three-fold design',
    '2.3': 'external stakeholders in the curriculum',
    '2.4': 'contributing disciplines, restated',
    '2.5': 'accessible environments, materials and site visits',
    '2.6': 'lived experience of housing in the content; flexible recruitment',
    '2.7': 'progression through the honours levels to the threshold',
    '2.8': 'exit awards; Scottish four-year honours; route to postgraduate study',
    '2.9': 'postgraduate taught awards at Level 7 or 11; CIH chartered membership',
    '2.10': 'widening access, apprenticeships and CIH routes',
    '2.11': 'recognition of prior learning and support for diverse entrants',
    '2.12': 'doctoral study and early career research networks',
    '2.13': 'part-time and full-time routes; employer links',
    '2.14': 'blended and digital delivery mirroring sector practice',
    '2.15': 'partnerships for work experience; employer groups',
    '2.16': 'monitoring and periodic review',
    '2.17': 'external reviewers in periodic review',
    '2.18': 'external examining and accreditation',
    '2.19': 'CIH validation where accreditation is sought',
    '3.1': 'core knowledge and understanding of a typical course (26 topics)',
    '3.2': 'independent learners as the desired outcome',
    '3.3': 'a strategy matched to outcomes; work-based learning where accredited',
    '3.4': 'student-centred strategy; prior learning; EDI and ESD aligned',
    '3.5': 'evolving digital contexts and resilience in delivery',
    '3.6': 'digital expectations, library support and the digital divide',
    '3.7': 'teaching approaches (seven examples)',
    '3.8': 'accessible materials and clear module outcomes',
    '3.9': 'an extended research or practice project',
    '3.10': 'outcomes may integrate sustainability competencies and SDGs',
    '3.11': 'diverse environments as a living laboratory',
    '3.12': 'diverse voices, decolonisation and transformative learning',
    '3.13': 'blended learning and group work',
    '3.14': 'the learning environment housing education needs',
    '3.15': 'an aligned assessment and feedback strategy',
    '3.16': 'accessible mixed assessment; published criteria',
    '3.17': 'assessment of, for and as learning (Figure 4)',
    '3.18': 'self, peer and synoptic assessment; authentic tasks',
    '3.19': 'assessment types students meet (eight listed)',
    '3.20': 'a diverse range of methods with adjustments',
    '4.1': 'the threshold is the minimum for an honours award',
    '4.2': 'most perform above it; providers refer to Annex D',
    '4.3': 'the threshold rung: nineteen areas of systematic understanding',
    '4.4': 'typical rung left to providers\' marking schemes',
    '4.5': 'excellent rung left to providers\' marking schemes',
    '4.6': "master's outcomes: forefront knowledge and four abilities",
    '4.7': "master's level set by the FHEQ Level 7 and FQHEIS Level 11 descriptor",
    '4.8': 'eight transferable and generic skills for both awards',
}
CTYPE = {'1.16': 'area', '1.24': 'area', '3.1': 'area', '1.18': 'practice', '2.15': 'practice', '3.3': 'practice',
         '3.7': 'practice', '3.11': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice',
         '3.18': 'practice', '3.19': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and D3'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Housing Studies', kind='other: membership; read for the edition history (S8)'),
    dict(number='none', heading='Figures 1, 3 and 4 (images: the SDGs; entrepreneurship, enterprise and employability; assessment for, as and of learning)', kind='other: figures held only by caption'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- section 1 statements
s('1.10', type='expectation', rung='none', force='will', level='none', appliesTo='Housing Studies courses across the UK',
  addressee='provider', verbs=['reflected', 'take'], about='differences between the four nations', domain='none', award=[HON, MA],
  para="Courses will reflect global, national and devolved governance and will need to allow for how housing law, policy and governance, and the housing bodies, differ between England, Scotland, Wales and Northern Ireland, even though the CIH itself works UK-wide.",
  prac="Plan content so that it will take account of how housing law, policy and governance differ between the four nations, and of the different housing bodies in each, rather than teaching one nation's system as the UK model.",
  ben="You will learn how housing law, policy and governance differ between England, Scotland, Wales and Northern Ireland, and which housing bodies work in each.",
  aaw="Describe this as a provider expectation, worded 'will need to', that Housing Studies courses take account of the differences in housing law, policy and governance across the four UK nations. Cite it as " + CITE + "1.10. Do not present it as a regulatory rule or as an outcome a student must show on its own. Set it beside the threshold item on comparative housing systems (" + SID + "4.3.b8).",
  aad="Raise it when a programme team plans law and policy content, or when a student asks why other nations' systems appear in the course. With staff, ask which modules compare the four nations and where the devolved housing bodies are taught; with a student, ask which nation's system they expect to work in and what they know of the others. Avoid treating one nation's arrangements as the norm for the UK.")
s('1.13', type='expectation', rung='none', force='will', level='none', appliesTo='teaching and learning in housing studies',
  addressee='provider', verbs=['have', 'recognises', 'challenge'], about='an inclusive curriculum grounded in social justice', domain='none', award=[HON, MA],
  para="Because housing studies is about social justice, its teaching will centre on an inclusive curriculum that recognises how varied learners are, including that some may have lived through housing precarity, and that invites students to question decisions in policy and practice.",
  prac="Put an inclusive curriculum at the centre of teaching: assume some students may have known housing precarity at first hand, draw on the many policy networks the subject touches and encourage students to challenge decisions made in policy and in practice.",
  ben="You will study in a curriculum built around inclusion and social justice, one that recognises that you or others in your group may have lived through housing insecurity and that encourages you to challenge decisions in policy and practice.",
  aaw="Present this as an expectation, worded 'will', about how housing studies is taught: an inclusive curriculum rooted in social justice, at any level of the subject. Cite it as " + CITE + "1.13. Do not turn it into a student outcome or a regulatory duty. Set it beside the inclusive behaviours (para 1.19) and the threshold item on addressing social inequalities (" + SID + "4.3.b7).",
  aad="Raise it when a team reviews its curriculum for inclusion, or when a student says the course touches their own housing history. For staff, ask where the course acknowledges students' lived experience of precarity and where students practise challenging decisions; for a student, ask whether they feel able to bring their own experience into discussion if they wish. Avoid pressing any student to disclose their own housing circumstances.")
s('1.15', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['develop', 'engage', 'challenging'], about='confidence to engage and challenge stakeholders', domain='generic-skill', award=[HON, MA],
  para="Graduates will build the self-reflection and confidence to work strategically, collaboratively and critically with stakeholders in policy, practice and other disciplines, and will have been helped to challenge the decisions of any stakeholder with housing expertise.",
  prac="Graduates will leave able to reflect on themselves and to engage stakeholders across policy, practice and other disciplines strategically, collaboratively and critically; design support that lets them practise challenging decisions with housing knowledge behind them.",
  ben="You will develop the self-awareness and confidence to work with people across policy, practice and other disciplines, strategically and critically, and to challenge their decisions using what you know about housing.",
  aaw="Describe this as an expected graduate outcome, worded 'will', within the statement's section on equality, diversity and inclusion: confidence to engage and challenge stakeholders, a generic skill read at FHEQ Level 6 for honours. Cite it as " + CITE + "1.15. Do not claim it is a threshold item; it sits outside the rung list. Set it beside " + SID + "4.8.b2, qaa/fheq-2024/4.15.b9.1 and spine:6.",
  aad="Raise it when a student is preparing for placements, meetings with stakeholders or a debate on policy. Put it plainly: you are expected to grow the confidence to question decisions, using your housing knowledge. Ask: 'When did you last challenge a decision in a group, and what evidence did you use?' Avoid presenting it as a test they must already pass.")
s('1.22', type='requirement', rung='none', force='should', level='none', appliesTo='Housing Studies courses',
  addressee='provider', verbs=['focused', 'addressing'], about='courses directed at the SDGs\' concerns', domain='none', award=[HON, MA],
  para="In line with the SDGs set by UN member states in 2015, Housing Studies courses should be directed towards tackling social, economic and environmental concerns for a better world.",
  prac="Orient the course towards the social, economic and environmental concerns behind the 17 SDGs, so that its purpose is visible in module aims and content.",
  ben=('n/a', 'a duty on the course design; the student meets it through the curriculum'),
  aaw="Describe this as a 'should' on course design: Housing Studies courses are aimed at the social, economic and environmental concerns of the UN Sustainable Development Goals. Cite it as " + CITE + "1.22. Do not present it as a student outcome or as binding regulation. Set it beside the ESD paragraphs 1.25 and 1.28 (" + SID + "1.25, " + SID + "1.28) and the Advance HE and QAA ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance).",
  aad="Raise it with a programme team reviewing aims or validation documents. Ask: 'Where do your module aims name the SDGs or the concerns behind them?' and 'Which goal does each core module serve?' Avoid putting this to a student as something they must do.")
s('1.23', type='expectation', rung='none', force='describes', level='none', appliesTo='Housing Studies courses',
  addressee='provider', verbs=['ensure', 'discussing'], about='enough sustainability content for confident discussion', domain='none', award=[HON, MA],
  para="Quality, accessible housing runs through several SDGs, SDG 11 above all, and housing can help meet the others (for example SDGs 1, 3, 5 and 7); the stated expectation is that courses hold enough sustainability content for students to be aware of the issues and confident discussing them in housing.",
  prac="Give the course enough sustainability content, tied to SDG 11 and to goals such as 1, 3, 5 and 7, that students can discuss sustainability in a housing context with knowledge and confidence.",
  ben="You can expect enough teaching on sustainability, such as the UN goal on sustainable cities and goals on poverty, health, gender equality and energy, to discuss it confidently in housing.",
  aaw="Describe this as an expectation on courses (the statement says 'the expectation is', a word outside must, should, may and will): enough sustainability content for students to be aware and confident in discussing it. Cite it as " + CITE + "1.23. Do not convert it into a 'must' or a threshold outcome. Set it beside the threshold item on environmental sustainability (" + SID + "4.3.b16) and spine:6.",
  aad="Raise it when a team checks sustainability coverage, or when a student asks how housing links to the SDGs. Ask a student: 'Could you explain how housing quality affects health or energy use?'; ask staff which modules teach SDG 11 and its housing target. Avoid reading the SDG list aloud at length.")
s('1.25', type='requirement', rung='none', force='should', level='none', appliesTo='course and module outcomes for ESD',
  addressee='provider', verbs=['interconnect', 'develop'], about='ESD outcomes linking knowledge, competencies and SDGs', domain='none', award=[HON, MA],
  para="ESD learning outcomes at course and module level should link housing knowledge and skills with the sustainability competencies and the 17 SDGs; the stated expectation is that courses build the UNESCO competencies step by step and that assessment shows they are achieved.",
  prac="Write ESD outcomes that join housing knowledge and skills to the UNESCO sustainability competencies and the 17 SDGs; develop the competencies progressively across levels and make sure assessment evidences them.",
  ben=('n/a', 'a duty on outcome writing and assessment design; the student meets its effect'),
  aaw="Describe this as a 'should' on writing course and module outcomes for ESD, with a further stated expectation that the UNESCO competencies are developed progressively and assessed. Cite it as " + CITE + "1.25. Do not present the UNESCO competency list (Figure 2, para 1.24) as threshold outcomes. Set it beside " + SID + "1.28, the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance) and spine:6 for the honours level.",
  aad="Raise it with a team drafting outcomes or an assessment map. Ask: 'Which outcome in each module links a housing topic to a sustainability competency or SDG?' and 'Which assessment shows the competency was reached?' Avoid treating the competency figure as a checklist every module must cover.")

ESDENV = dict(type='requirement', rung='none', force='must', level='none', appliesTo='the learning environment for ESD', addressee='provider', domain='none', award=[HON, MA])
def env126(n, **k):
    s('1.26.b%d' % n, **ESDENV, **k)
AAD_ENV = " Avoid presenting it to a student as something they must arrange."
env126(1, verbs=['facilitated'], about='interdisciplinary or transdisciplinary learning',
  para="ESD needs a learning environment that supports interdisciplinary or transdisciplinary learning.",
  prac="Make room in the course for learning that crosses disciplines, for example shared modules or joint projects with planning, health or built environment students.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition the statement says ESD requires ('requires', read as must) of the learning environment: learning across disciplines. Cite it as " + CITE + "1.26 (first item). Do not present it as a student outcome. Set it beside the matching item in para 3.14 (" + SID + "3.14.b1).",
  aad="Raise it when a team plans shared or cross-disciplinary teaching. Ask: 'Where do students learn alongside other disciplines?'" + AAD_ENV)
env126(2, verbs=[], about='inclusive and accessible learning',
  para="ESD needs learning that includes everyone and that everyone can reach.",
  prac="Design ESD learning to be inclusive and accessible to all students, including off-campus and site-based activity.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition ESD requires of the learning environment: inclusive and accessible learning for all. Cite it as " + CITE + "1.26 (second item). Do not present it as a student outcome. Set it beside the accessibility paragraph (" + SID + "2.5) and " + SID + "3.14.b2.",
  aad="Raise it when sustainability activities involve visits or fieldwork. Ask: 'Could every student take part in this activity as planned?'" + AAD_ENV)
env126(3, verbs=['support'], about='policies that support synoptic assessment',
  para="ESD needs policies that allow synoptic assessment.",
  prac="Check that assessment regulations allow synoptic tasks that draw on several modules.",
  ben=('n/a', 'a condition set by the course regulations'),
  aaw="Describe this as a condition ESD requires: policies that permit synoptic assessment. Cite it as " + CITE + "1.26 (third item). Do not present it as a student outcome. Set it beside " + SID + "3.14.b6.",
  aad="Raise it with a team reviewing assessment regulations. Ask: 'Do your rules allow a task that draws on more than one module?'" + AAD_ENV)
env126(4, verbs=['provided', 'recognised'], about='extra and co-curricular opportunities',
  para="ESD needs extra-curricular and co-curricular opportunities that are offered and given recognition.",
  prac="Offer extra-curricular and co-curricular sustainability opportunities and give them formal recognition.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition ESD requires: extra and co-curricular opportunities, offered and recognised. Cite it as " + CITE + "1.26 (fourth item). Do not present it as a student outcome. Set it beside " + SID + "3.14.b4.",
  aad="Raise it when a team plans activity outside the timetable. Ask: 'How is sustainability work done outside modules recognised?'" + AAD_ENV)
env126(5, verbs=['utilised', 'develop', 'express'], about='learning spaces used as alternative locations',
  para="ESD needs campus, outdoor and other learning spaces to be used to the full as places where students build and show its competencies.",
  prac="Use the campus, outdoor settings and other spaces as places where students develop and demonstrate sustainability competencies.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition ESD requires: full use of campus and outdoor spaces as alternative settings for sustainability competencies. Cite it as " + CITE + "1.26 (fifth item). Do not present it as a student outcome. Set it beside the living laboratory paragraph (" + SID + "1.27) and " + SID + "3.14.b5.",
  aad="Raise it when a team looks for settings beyond the classroom. Ask: 'Which places on or near campus could students use to study housing and sustainability?'" + AAD_ENV)

s('1.27', type='requirement', rung='none', force='should', level='none', appliesTo='teaching, learning and assessment',
  addressee='provider', verbs=['take', 'uses'], about='the campus and community as a living laboratory', domain='none', award=[HON, MA],
  para="Teaching, learning and assessment should use the opportunities the campus, the local community and online settings offer; treating campus and community as a living laboratory can give authentic housing learning, and the stated expectation is that courses use varied environments to build sustainability understanding and competencies.",
  prac="Use the campus, the local community and online spaces as settings for learning and assessment, for instance as a living laboratory for housing questions, so that students build sustainability understanding and competencies in more than one environment.",
  ben="You can expect some of your learning and assessment to happen on campus, in the local community or online, treating real places as a living laboratory for housing and sustainability.",
  aaw="Describe this as a 'should' on teaching, learning and assessment, with a stated expectation that varied environments are used to develop sustainability competencies. Cite it as " + CITE + "1.27. Do not present the living laboratory as compulsory for every module. Set it beside " + SID + "1.26.b5 and " + SID + "3.11.",
  aad="Raise it when a team designs authentic tasks or field activity. Ask staff: 'Which assessment uses a real local housing setting?'; ask a student which local place they would study to see sustainability in practice. Avoid implying that online-only students miss the requirement.")
s('1.28', type='requirement', rung='none', force='should', level='none', appliesTo='curriculum design at course and module level',
  addressee='provider', verbs=['embedded', 'support'], about='sustainable development embedded in the curriculum', domain='none', award=[HON, MA],
  para="To advance sustainable development, the agenda should be built into curriculum design at course and module level, with learning environments that let students gain the knowledge, understanding and skills to act towards sustainable futures and to link housing with health and education.",
  prac="Embed sustainable development in the design of both the course and its modules, and provide environments in which students build the knowledge and skills to act for sustainable communities and to connect housing with health and education.",
  ben=('n/a', 'a duty on curriculum design; the student meets its effect'),
  aaw="Describe this as a 'should' on curriculum design: sustainable development embedded at course and module level. Cite it as " + CITE + "1.28. Do not present it as a student outcome or as regulatory. Set it beside " + SID + "1.25 and " + SID + "1.29.",
  aad="Raise it when a team maps sustainability across its modules. Ask: 'Is sustainable development part of each module's design, or added in one place only?' Avoid putting the design duty to a student.")
s('1.29', type='requirement', rung='none', force='should', level='none', appliesTo='modules: content, delivery and assessment',
  addressee='provider', verbs=['manifested', 'encouraged'], about='ESD across content, teaching and assessment', domain='none', award=[HON, MA],
  para="ESD should show in module content, teaching and learning methods, structure and delivery and assessment; inclusive, interdisciplinary approaches with recognised extra and co-curricular work are encouraged, and case studies, project research and visits to communities facing unsustainability can enrich learning.",
  prac="Make ESD visible in what modules teach, how they teach it, how they are structured and how they assess; use case studies, project-based research and community visits where symptoms of unsustainability show.",
  ben=('n/a', 'a duty on module design; the student meets its effect'),
  aaw="Describe this as a 'should' on modules: ESD present in content, teaching, structure, delivery and assessment. Cite it as " + CITE + "1.29. Do not present the suggested methods (case studies, visits) as required. Set it beside " + SID + "1.28 and " + SID + "3.14.b3.",
  aad="Raise it when a module leader reviews a module. Ask: 'Where does sustainability show in this module's assessment, not only its content?' Avoid putting it to a student as their duty.")
s('1.30', type='requirement', rung='none', force='should', level='none', appliesTo='ESD content and the subject area',
  addressee='provider', verbs=['focus', 'develop', 'strengthen'], about='the focus of ESD content and learning environments', domain='none', award=[HON, MA],
  para="ESD content should centre on keeping physical environments whole, on social justice and on economic development, drawing on diverse voices and other disciplines; the subject area should be able to build and strengthen environments, physical, virtual and digital, that promote sustainable development.",
  prac="Focus ESD content on physical environmental integrity, social justice and economic development, include under-represented voices and other disciplines, and keep improving physical and digital learning spaces for sustainability.",
  ben=('n/a', 'a duty on content and learning environments; the student meets its effect'),
  aaw="Describe this as a 'should' on ESD content and on the subject area's learning environments. Cite it as " + CITE + "1.30. Do not present it as a student outcome. Set it beside " + SID + "1.29 and the content item on sustainable development perspectives (para 3.1).",
  aad="Raise it when a team reviews reading lists and ESD topics. Ask: 'Do the sources in this module include voices from under-represented communities?' Avoid putting the duty to a student.")
s('1.34', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['equipped', 'motivate', 'identify', 'implement', 'manage'], about='transferable, self-management and problem-solving skills', domain='generic-skill', award=[HON, MA],
  para="Graduates will have transferable skills for present housing work and for new roles built on new technology; they will manage and motivate themselves and others, spot housing problems, own ideas and decisions to solve them, handle risk and know the limits of their professional competence and judgement.",
  prac="Graduates will carry transferable skills into current and emerging housing roles: self-management and motivating others, identifying housing problems, taking responsibility for ideas and decisions, managing risk and recognising the bounds of their own professional judgement.",
  ben="You will gain skills you can use in housing jobs now and in new roles that technology creates: managing yourself, motivating others, spotting housing problems, taking ownership of ideas and decisions, handling risk and knowing where your professional judgement stops.",
  aaw="Describe this as an expected graduate outcome, worded 'will', in the statement's employability section: transferable and self-management skills, a generic skill read at FHEQ Level 6 for honours and Level 7 for a master's. Cite it as " + CITE + "1.34. Do not claim it is on the threshold list. Set it beside " + SID + "4.8.b1, " + SID + "4.8.b6, qaa/fheq-2024/4.15.b9.2 and spine:6.",
  aad="Raise it when a student asks what employers will expect, or prepares for a placement or interview. Put it in plain words and ask: 'Tell me about a housing problem you identified and the decision you took about it' or 'Where are the limits of what you would decide alone?' Avoid presenting all of it as a minimum they must already have.")
s('1.35', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['have', 'reflect', 'organise', 'identify', 'transfer', 'pivot'], about='professional knowledge, reflection, ethics and resilience', domain='generic-skill', award=[HON, MA],
  para="Graduates will know housing well across policy, development, finance, management, research, sustainability and equality; reflect critically on their own knowledge, especially in fast-changing areas such as digital technology; direct their own learning and development; bring in good practice from neighbouring fields such as health and criminal justice; and work ethically, sensitively, resiliently and creatively, adapting as situations change.",
  prac="Graduates will combine broad housing knowledge with reflective, self-directed professional development, transfer good practice from allied fields, act ethically with attention to equality and diversity and stay resilient and adaptable in a changing sector.",
  ben="You will know housing broadly, from policy and finance to sustainability and equality; reflect on your own skills, especially as technology changes; take charge of your own development; borrow good practice from fields such as health; and work ethically, resiliently and creatively as things change.",
  aaw="Describe this as an expected graduate outcome, worded 'will', in the employability section: a profile of the reflective, ethical and adaptable housing professional, a generic skill read at FHEQ Level 6 for honours. Cite it as " + CITE + "1.35. Do not claim it is on the threshold list or that every clause is assessed. Set it beside " + SID + "4.8.b7, qaa/fheq-2024/4.15.b9.3, qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6.",
  aad="Raise it in personal tutoring or reflective writing on professional development. Ask: 'Which part of housing practice is changing fastest for you, and how are you keeping up?' and 'Where have you used an idea from another field?' Avoid reading the whole paragraph aloud.")

# ---------------------------------------------------------------- section 2 statements
s('2.5', type='requirement', rung='none', force='should', level='none', appliesTo='learning environments, materials and site visits',
  addressee='provider', verbs=['designed', 'participate', 'arranged'], about='accessible learning environments and site visits', domain='none', award=[HON, MA],
  para="Learning environments and materials should be accessible to students with a wide range of learning or mobility needs and to those whose prior learning was limited by structural inequality; all should be able to take full part, with adjustments and support where suitable, and site visits should be arranged so every student can attend.",
  prac="Design spaces, materials and site visits for students with learning, sensory or mobility needs and for those whose earlier education was limited by disadvantage; make adjustments in line with national frameworks and institutional services so that everyone can participate fully.",
  ben="You should be able to take a full part in your course whatever your learning or mobility needs or your background, with adjustments and support where you need them, including on site visits.",
  aaw="Describe this as a 'should' on providers: accessible environments, materials and site visits, with adjustments for disabled students and those affected by structural inequality. Cite it as " + CITE + "2.5. Do not present it as a student outcome or as the provider's whole legal duty, which lies in equality law. Set it beside " + SID + "1.26.b2 and " + SID + "3.16.",
  aad="Raise it when a site visit or new material is planned, or when a student mentions a barrier to taking part. For staff, ask: 'Could a wheelchair user or a dyslexic student join this visit and use these materials as planned?'; for a student, ask what would help them take part fully and point them to support. Avoid asking a student to justify their need.")
s('2.6', type='requirement', rung='none', force='should', level='none', appliesTo='course design and recruitment',
  addressee='provider', verbs=['recognised', 'share', 'allow'], about='lived experience in the content; flexible recruitment', domain='none', award=[HON, MA],
  para="Every student has lived somewhere, and some have faced the housing problems the course teaches; course design can recognise this so that the content raises no barriers and students may share experience if they choose, and recruitment should be flexible enough for learners with little academic background but sector experience to flourish.",
  prac="Design content so that students who have faced housing problems are not put off by it and can choose to share their experience; recruit flexibly, for example through whole-person approaches, links with feeder providers and induction support in academic writing and critical thinking for non-traditional entrants.",
  ben="If you have lived through housing problems yourself, the course should let you engage with that content safely and share your experience only if you wish; if you come from housing work rather than academic study, you should find a route in and support to start.",
  aaw="Describe this as a 'should' on recruitment flexibility, with course design advised to recognise students' lived experience of housing. Cite it as " + CITE + "2.6. Do not present it as an entry requirement or a student outcome. Set it beside " + SID + "1.13 and " + SID + "2.11.",
  aad="Raise it when a team plans admissions or content on homelessness and precarity. Ask staff: 'How does a student with lived experience opt in or out of sharing it?'; ask an applicant from the sector what support with academic writing would help. Avoid probing a student's own housing history.")
s('2.7', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='honours students, single and joint',
  addressee='learner', verbs=['progress', 'achieve'], about='progression to the threshold across the honours levels', domain='none', award=HON,
  para="Through an honours degree (FHEQ Level 6, FQHEIS Level 10) a student will move from level to level under institutional rules, each level building towards meeting every threshold subject-specific and generic skill; joint honours students will meet part of these and add others from their second subject.",
  prac="Plan each level of the honours course to build towards the full set of threshold subject and generic skills by the end; in joint honours, expect part of the set to be met here and the rest supplied by the other subject.",
  ben="As you move through each year of an honours degree you will build up, step by step, everything the threshold asks; if you study housing as a joint subject you will meet part of it here and add skills from your other subject.",
  aaw="Describe this as an expectation, worded 'will', that progression through the honours levels leads to all the threshold skills, with joint honours meeting part of them. Cite it as " + CITE + "2.7, which also states the FHEQ Level 6 and FQHEIS Level 10 equivalence. Do not claim the statement sets outcomes for each year. Set it beside the threshold list (" + SID + "4.3.b1 to 4.3.b18), " + SID + "4.8.b1 and spine:6.",
  aad="Raise it when a student asks how this year connects to the final standard, or a team maps outcomes by level. Ask: 'Which threshold items does this year's work build towards?' Avoid telling a first-year student they must already meet the final threshold.")
s('2.11', type='requirement', rung='none', force='should', level='none', appliesTo='postgraduate admissions, regulations and support',
  addressee='provider', verbs=['disadvantage', 'available'], about='fair recognition of prior learning and support for all', domain='none', award=[HON, MA],
  para="Courses recognise prior learning and entrants arrive by many routes; at postgraduate level, RPL and course rules should not penalise those admitted on alternative or older experience, and support should be open to all students, for example study skills packages to ease the move into higher-level study.",
  prac="Write RPL and course regulations so that postgraduate entrants with alternative, equivalent or dated experience are not disadvantaged, and offer support such as study skills packages to every student.",
  ben="If you join with work experience instead of the usual qualifications, the rules should not count against you, and you should be able to get support, such as help with study skills, regulations and difficulties.",
  aaw="Describe this as a 'should' on postgraduate regulations and support: RPL that does not disadvantage alternative entrants, and support for all. Cite it as " + CITE + "2.11. Do not present RPL as an entitlement to exemption. Set it beside " + SID + "2.6 and " + SID + "3.4.",
  aad="Raise it with an admissions tutor or an applicant from the housing sector. Ask: 'Would an applicant with ten years' practice and an old diploma be treated fairly by our rules?' or ask the applicant what prior learning they want recognised. Avoid promising a student exemption the regulations may not give.")
s('2.15', type='requirement', rung='none', force='must', level='none', appliesTo='courses and students seeking CIH chartered membership',
  addressee='both', verbs=['requires', 'facilitate'], about='work experience for CIH chartered membership; employer partnerships', domain='none', award=[HON, MA],
  para="Partnerships with housing organisations for work experience are core to undergraduate and postgraduate courses; CIH chartered membership accreditation requires set work experience in a housing role, and providers are expected to run employer groups that inform curriculum and skills.",
  prac="Build partnerships with housing employers to secure the prescribed work experience that CIH chartered membership requires; convene employer groups that meet regularly and invite partners to comment on curriculum and skills development.",
  ben="If you are aiming for chartered membership of the Chartered Institute of Housing, you must complete set work experience in a housing role; your course works with employers to help you find it and to bring guest speakers and projects.",
  aaw="Describe the requirement as the professional body's: CIH chartered membership accreditation requires prescribed work experience in a housing role ('requires', read as must); the employer groups are only 'anticipated' of providers. Cite it as " + CITE + "2.15. Do not claim the statement itself makes work experience compulsory for every degree. Set it beside " + SID + "2.19, " + SID + "4.3.b19 and " + SID + "4.8.b8.",
  aad="Raise it when a student asks about chartered membership, placements or working while studying. Ask a student: 'Do you intend to seek chartered membership, and where could you gain the work experience it needs?'; ask staff how employer groups shape the curriculum. Avoid telling a student who is not seeking membership that the experience is compulsory.")
s('2.16', type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies',
  addressee='provider', verbs=['draw', 'ensure'], about='external reference points in monitoring and review', domain='none', award=[HON, MA],
  para="Degree-awarding bodies monitor and periodically review their courses and will use external reference points, this statement among them, to keep their provision in line with sector norms.",
  prac="In monitoring and periodic review, use this statement among other external reference points to check that provision matches sector norms, and use monitoring data to understand achievement and plan ahead.",
  ben=('n/a', 'a quality assurance duty on the awarding body'),
  aaw="Describe this as an expectation, worded 'will', that awarding bodies use this statement as an external reference point in review. Cite it as " + CITE + "2.16. Do not claim the statement is binding in review in England, where its front matter says it is not a sector-recognised standard. Set it beside " + SID + "2.17.",
  aad="Raise it with a team preparing periodic review. Ask: 'Which parts of the statement did you check the course against, and what did you find?' Avoid putting it to a student.")
s('2.17', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers',
  addressee='provider', verbs=['use', 'ensure'], about='external reviewers confirm threshold standards', domain='none', award=[HON, MA],
  para="Externality is essential to UK quality assurance: providers will bring in external reviewers during periodic review to give an outside view of changes and confirm that threshold standards are met and content suits the subject.",
  prac="Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and subject content are confirmed.",
  ben=('n/a', 'a quality assurance duty on the provider'),
  aaw="Describe this as an expectation, worded 'will', that providers use external reviewers to confirm threshold standards and content. Cite it as " + CITE + "2.17. Do not present it as a student matter. Set it beside " + SID + "2.16 and the threshold list (para 4.3).",
  aad="Raise it with a team choosing external reviewers. Ask: 'Will the reviewer check the course against the threshold items in para 4.3?' Avoid putting it to a student.")
s('2.19', type='requirement', rung='none', force='must', level='none', appliesTo='courses seeking CIH accreditation',
  addressee='provider', verbs=['delivered', 'determines'], about='CIH accreditation shapes content and change', domain='none', award=[HON, MA],
  para="Courses may undergo internal monitoring, external review and CIH validation; where a course seeks CIH accreditation, the body's requirements shape the core content and skills it must deliver and the engagement with CIH that changes need.",
  prac="If the course seeks or holds CIH accreditation, deliver the content and skills the CIH requires and engage with the CIH, as it requires, before changing content or delivery.",
  ben=('n/a', 'a condition on accredited courses, met by the provider'),
  aaw="Describe this as a condition on CIH-accredited courses ('need to be delivered', 'required engagement', read as must): the CIH's requirements govern core content and changes. Cite it as " + CITE + "2.19. Do not present the CIH's requirements as part of this statement; they are the body's own (not yet ingested, Part E). Set it beside " + SID + "4.3.b19 and " + SID + "2.15.",
  aad="Raise it when an accredited course plans a change. Ask: 'Does this change touch content the CIH requires, and have you engaged the CIH?' Avoid putting it to a student.")

# ---------------------------------------------------------------- section 3 statements
s('3.3', type='expectation', rung='none', force='will', level='none', appliesTo='the teaching, learning and assessment strategy',
  addressee='provider', verbs=['include'], about='a strategy matched to outcomes; work-based learning where accredited', domain='none', award=[HON, MA],
  para="A typical course's strategy makes plain why its methods suit the intended outcomes, is expected to use varied approaches that meet varied learning styles and needs, and, where the course is professionally accredited, will include work-based or work-related learning for newcomers and experienced staff alike.",
  prac="Make the fit between methods and intended outcomes explicit; use a variety of approaches for different learners; on an accredited course, include work-based or work-related learning for students new to housing and for those already in it.",
  ben="You can expect a mix of teaching and assessment that suits different ways of learning; on a professionally accredited course you will have chances to learn through or about work, whether you are new to housing or already work in it.",
  aaw="Describe this as an expectation on the strategy ('is expected to', outside the five force words) with a firmer 'will' for work-based or work-related learning on accredited courses. Cite it as " + CITE + "3.3. Do not present work-based learning as required on unaccredited courses. Set it beside " + SID + "2.15 and " + SID + "3.7.",
  aad="Raise it when a team writes or reviews its learning and assessment strategy. Ask: 'Where does the strategy show why each method fits the outcomes?' and 'What work-related learning do students new to housing get?' Avoid putting it to a student as their task.")
s('3.4', type='expectation', rung='none', force='describes', level='none', appliesTo='the teaching, learning and assessment strategy',
  addressee='provider', verbs=['emphasises', 'incorporate', 'recognise'], about='student-centred strategy and recognition of prior learning', domain='none', award=[HON, MA],
  para="The strategy is anticipated to be student-centred with review built in; learning, teaching and assessment are expected to recognise prior knowledge and experience and to clarify any exemption; practitioners may advise; alignment with EDI and ESD is encouraged.",
  prac="Keep the strategy student-centred and reviewed, recognise what students already know and have done, make exemption routes clear, involve housing practitioners where useful and align activities with EDI and ESD themes.",
  ben="You can expect your course to recognise what you already know from life and work, to make clear whether any part can be exempted and to build in equality, inclusion and sustainability.",
  aaw="Describe this as an expectation (the statement says 'anticipated' and 'expected', words outside the five), not a requirement: a student-centred strategy that recognises prior learning. Cite it as " + CITE + "3.4. Do not present the exemption route as an entitlement. Set it beside " + SID + "2.11 and " + SID + "3.3.",
  aad="Raise it when a team reviews its strategy or a student asks whether experience counts. Ask staff: 'How does a student find out what prior learning could exempt them?' Avoid promising a student an exemption.")
s('3.6', type='requirement', rung='none', force='should', level='none', appliesTo='courses and institutions offering virtual and blended learning',
  addressee='provider', verbs=['underpinned', 'aware'], about='digital expectations, library support and the digital divide', domain='none', award=[HON, MA],
  para="Courses should be supported by clear guidance on what digital technology students need (with training if required) and on using library resources; institutions with virtual or blended learning should be alert to the digital divide and arrange support.",
  prac="Tell students clearly what digital technology they need and offer training; support use of the library; where delivery is virtual or blended, plan for students on the wrong side of the digital divide and, where you can, point applicants to preparatory resources.",
  ben="You should be told clearly what technology you need and offered training, shown how to use the library well and, if you study online or in a blended way, supported if you lack equipment or connection.",
  aaw="Describe this as a 'should' on courses and institutions: clear digital expectations, library support and attention to the digital divide. Cite it as " + CITE + "3.6. Do not present it as a student outcome. Set it beside " + SID + "3.8 and " + SID + "4.8.b5.",
  aad="Raise it when a course moves online or a student struggles with access. Ask a student: 'Do you have the device and connection the course expects, and do you know where to ask for help?'; ask staff where the digital requirements are published. Avoid assuming every student has reliable access.")
s('3.7', type='expectation', rung='none', force='describes', level='none', appliesTo='teaching on campus and online',
  addressee='provider', verbs=['used', 'accommodate'], about='a range of teaching approaches for different learners', domain='none', award=[HON, MA],
  para="In both campus and online settings a range of teaching approaches is expected, to suit different learning styles; the examples given run from lectures and seminars to supervision, directed study, fieldwork with adjustments, problem-based learning and negotiated or work-related learning.",
  prac="Use several teaching approaches, for example lectures, small-group work, one-to-one supervision, directed study, site visits with reasonable adjustments, problem-based and team work, and negotiated or work-related learning that serves employability.",
  ben="You can expect a mix of teaching, such as lectures, seminars, supervision, guided study, site visits, problem-solving in teams and learning through work.",
  aaw="Describe this as an expectation ('it is expected', a word outside the five) that a range of teaching approaches is used; the list is examples, not a required set. Cite it as " + CITE + "3.7. Do not present any single example as mandatory. Set it beside " + SID + "3.3 and " + SID + "3.11.",
  aad="Raise it when a team reviews its teaching mix. Ask: 'Which learners might this module's methods leave out?' Avoid reading the list of examples aloud as a checklist.")
s('3.8', type='expectation', rung='none', force='will', level='none', appliesTo='learning materials and module outcomes',
  addressee='provider', verbs=['specified', 'supported'], about='accessible materials and clear module outcomes', domain='none', award=[HON, MA],
  para="Materials are expected to be accessible to all and to give full, accurate course documentation, and each module's learning outcomes will be stated clearly and be achievable, with reading and other resources indicated.",
  prac="Provide accessible materials and complete, accurate documentation; for every module, state clear and achievable outcomes and indicate the reading and resources that support them.",
  ben="You will be given clear, achievable outcomes for every module, with guidance on what to read, and accessible, accurate information about your course.",
  aaw="Describe this as an expectation, worded 'will' for module outcomes and 'expected' for materials. Cite it as " + CITE + "3.8. Do not present it as a student outcome. Set it beside " + SID + "2.5 and " + SID + "3.15.",
  aad="Raise it when a module handbook is drafted or a student cannot find what a module expects. Ask a student: 'Do you know what this module's outcomes are and what to read for them?' Avoid treating unclear outcomes as the student's fault.")
s('3.11', type='requirement', rung='none', force='should', level='none', appliesTo='teaching practices and courses',
  addressee='provider', verbs=['provide', 'take'], about='alternative viewpoints, reflection and real-world challenges in diverse settings', domain='none', award=[HON, MA],
  para="Teaching should open up alternative viewpoints, reflection on experience and real problems, and courses should use campuses, communities and online spaces as a living laboratory for topics from housing innovation to local governance, with digital tools to record and repeat the experience inclusively.",
  prac="Use teaching that surfaces alternative viewpoints, reflection and real-world challenges; treat campus, community and sector settings as a living laboratory and use digital tools to record and share that learning inclusively.",
  ben="You should meet different viewpoints, reflect on experience and work on real housing challenges, often in the community, on campus or online.",
  aaw="Describe this as a 'should' on teaching practices and courses: alternative viewpoints, reflection, real-world challenges and diverse settings. Cite it as " + CITE + "3.11. Do not present the living laboratory as required for every module. Set it beside " + SID + "1.27 and " + SID + "3.12.",
  aad="Raise it when a team designs an authentic task. Ask: 'Which real local housing challenge could students work on in this module?' Avoid presenting it to a student as their duty.")
s('3.12', type='requirement', rung='none', force='should', level='none', appliesTo='course design and learning experiences',
  addressee='provider', verbs=['consider', 'transform', 'promote'], about='diverse voices, decolonisation and transformative learning', domain='none', award=[HON, MA],
  para="Course design should widen literature and resources to include more voices, especially tenants and under-represented communities; historical approaches and the decolonisation of the curriculum should get careful thought; learning should change ways of thinking and practising and make students informed advocates of sustainable development; and courses should offer multi, inter and trans-disciplinary experiences beyond UK-centred practice.",
  prac="Broaden reading lists with tenant voices and under-represented communities, reconsider historical approaches and decolonise the curriculum, aim for learning that changes how students think and practise and give interdisciplinary experiences beyond UK-centred housing practice.",
  ben="You should read and hear from a wider range of voices, including tenants and under-represented communities, question how housing history has been told and look beyond UK practice, so that you can speak up well for sustainable development.",
  aaw="Describe this as a set of 'should' expectations on course design: diverse voices, decolonisation, transformative learning and interdisciplinary experience. Cite it as " + CITE + "3.12. Do not present it as a student outcome. Set it beside " + SID + "1.30 and the content item on decolonising the curriculum (para 3.1).",
  aad="Raise it when a team reviews reading lists or module aims. Ask: 'Whose voices are missing from this module's sources, and where do tenants speak for themselves?' Avoid putting the duty to a student.")
s('3.13', type='requirement', rung='none', force='should', level='none', appliesTo='blended teaching and learning',
  addressee='provider', verbs=['promoted'], about='blended learning, group work and critical reflection', domain='none', award=[HON, MA],
  para="Blended learning is increasingly likely; digital teaching can be used creatively and fairly for an inclusive, immersive experience, group work builds collaborative competencies and chances for critical reflection on one's own and others' views should be promoted.",
  prac="Use digital and blended methods creatively and equitably, set real problems and group tasks (online too) and promote critical reflection on students' own perspectives and those of others.",
  ben="You should be given chances to reflect critically on your own views and those of others, often through group work and blended learning on real housing problems.",
  aaw="Describe this as a 'should' on promoting critical reflection, set in a description of blended learning. Cite it as " + CITE + "3.13. Do not present blended delivery as required. Set it beside " + SID + "4.8.b3 and " + SID + "4.8.b7.",
  aad="Raise it when a team designs online group tasks. Ask: 'Where in this task do students reflect on a view they disagree with?' Avoid putting it to a student as a rule.")

ENV = dict(type='requirement', rung='none', force='must', level='none', appliesTo='the learning environment for housing studies', addressee='provider', domain='none', award=[HON, MA])
def env314(n, **k):
    s('3.14.b%d' % n, **ENV, **k)
env314(1, verbs=['facilitated'], about='interdisciplinary or transdisciplinary learning',
  para="Housing studies education needs a learning environment that supports learning across disciplines.",
  prac="Provide learning that crosses disciplines, such as shared modules or joint projects.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition housing studies education requires ('requires', read as must) of its learning environment: learning across disciplines. Cite it as " + CITE + "3.14 (first item). Do not present it as a student outcome. Set it beside " + SID + "1.26.b1 and " + SID + "4.8.b3.",
  aad="Raise it when a team plans shared teaching. Ask: 'Where do students learn with other disciplines?'" + AAD_ENV)
env314(2, verbs=[], about='inclusive and accessible learning',
  para="Housing studies education needs learning that includes everyone and that everyone can reach.",
  prac="Make every part of learning inclusive and accessible to all students.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition housing studies education requires: inclusive and accessible learning. Cite it as " + CITE + "3.14 (second item). Do not present it as a student outcome. Set it beside " + SID + "2.5 and " + SID + "1.26.b2.",
  aad="Raise it when a team reviews access to its activities. Ask: 'Who could not take part in this activity as designed?'" + AAD_ENV)
env314(3, verbs=['underpins'], about='ESD underpinning learning',
  para="Housing studies education needs education for sustainable development to sit beneath learning.",
  prac="Let sustainable development underpin learning across the course, not one module alone.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition housing studies education requires: ESD as a foundation of learning. Cite it as " + CITE + "3.14 (third item). Do not present it as a student outcome. Set it beside " + SID + "1.28 and " + SID + "1.29.",
  aad="Raise it when a team maps ESD. Ask: 'Which modules would lose their point without sustainability?'" + AAD_ENV)
env314(4, verbs=['provided', 'recognised'], about='extra and co-curricular opportunities',
  para="Housing studies education needs extra-curricular and co-curricular opportunities that are offered and recognised.",
  prac="Offer and formally recognise extra and co-curricular opportunities.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition housing studies education requires: extra and co-curricular opportunities, offered and recognised. Cite it as " + CITE + "3.14 (fourth item). Do not present it as a student outcome. Set it beside " + SID + "1.26.b4.",
  aad="Raise it when a team plans activity outside modules. Ask: 'How is work outside the timetable recognised?'" + AAD_ENV)
env314(5, verbs=['utilised', 'develop', 'express'], about='campus, outdoor and virtual spaces for ESD competencies',
  para="Housing studies education needs campus, outdoor and virtual spaces to be used fully as alternative places to build and show ESD competencies.",
  prac="Use campus, outdoor and virtual spaces as settings in which students develop and show sustainability competencies.",
  ben=('n/a', 'a condition of the learning environment, provided by the course'),
  aaw="Describe this as a condition housing studies education requires: full use of campus, outdoor and virtual spaces for ESD competencies. Cite it as " + CITE + "3.14 (fifth item). Do not present it as a student outcome. Set it beside " + SID + "1.26.b5 and " + SID + "3.11.",
  aad="Raise it when a team looks for settings beyond the lecture room, virtual ones included. Ask: 'Which space could host a sustainability task in this module?'" + AAD_ENV)
env314(6, verbs=['support', 'enabling', 'integrate'], about='policies for synoptic assessment that connect modules',
  para="Housing studies education needs policies that allow synoptic assessment, so students connect learning across modules and integrate it as they progress.",
  prac="Allow synoptic assessment in regulations so that students can link and integrate learning across modules as they progress.",
  ben=('n/a', 'a condition set by the course regulations'),
  aaw="Describe this as a condition housing studies education requires: policies supporting synoptic assessment that links modules. Cite it as " + CITE + "3.14 (sixth item). Do not present it as a student outcome. Set it beside " + SID + "1.26.b3 and " + SID + "4.8.b1.",
  aad="Raise it with a team reviewing assessment rules. Ask: 'Where do students pull several modules together in one task?'" + AAD_ENV)

s('3.15', type='requirement', rung='none', force='should', level='none', appliesTo='each method of assessment',
  addressee='provider', verbs=['defined', 'aligned'], about='clear, aligned aims, content and marking criteria', domain='none', award=[HON, MA],
  para="Educators are encouraged to think creatively about assessment; a strategy for assessment and feedback helps students show their attainment and see their progress, and for each method the aims, content requirements and marking criteria should be clearly set out and aligned with the curriculum, teaching approaches and outcomes.",
  prac="For every assessment method, define aims, content requirements and marking criteria clearly and align them with the knowledge and skills taught, the teaching approaches and the course outcomes.",
  ben="For every assessment you should be told clearly what it is for, what it must contain and how it will be marked, and these should match what you were taught.",
  aaw="Describe this as a 'should' on assessment design: clear, aligned aims, content requirements and marking criteria for each method. Cite it as " + CITE + "3.15. Do not present it as a student outcome. Set it beside " + SID + "3.16 and the Annex D bands (std:doc:qaa-fheq-2024-framework, Annex D).",
  aad="Raise it when a student is unsure what a task wants, or a team writes a brief. Ask a student: 'Can you find the criteria for this task and say what a strong answer needs?'; ask staff whether the criteria match the module outcomes. Avoid blaming the student for an unclear brief.")
s('3.16', type='requirement', rung='none', force='should', level='none', appliesTo='students and the assessment regime',
  addressee='provider', verbs=['demonstrate', 'documented', 'distributed'], about='accessible mixed assessment and published criteria', domain='none', award=[HON, MA],
  para="Students should be able to show the full range of their abilities through a mix of assessment methods equally open to all backgrounds and situations; the means of assessment are expected to be documented and shared, and criteria published for all summative assessment.",
  prac="Offer varied assessment methods, each open on equal terms whatever students' educational background or circumstances, document and share how assessment works and publish criteria for every summative task.",
  ben="You should have the chance to show everything you can do through a mix of assessments that work for students from any background, with the arrangements and marking criteria shared with you in advance.",
  aaw="Describe this as a 'should' on giving students a fair chance to show their abilities through varied, accessible assessment, with an expectation that criteria are published. Cite it as " + CITE + "3.16. Do not present it as an outcome the student must show. Set it beside " + SID + "2.5 and " + SID + "3.15.",
  aad="Raise it when a student feels one assessment type disadvantages them, or a team reviews its assessment mix. Ask a student: 'Which kind of assessment lets you show your strengths best?'; ask staff whether any student group is held back by the current mix. Avoid presenting a preferred format as a right to choose.")
s('3.20', type='expectation', rung='none', force='describes', level='none', appliesTo='assessment across the course',
  addressee='provider', verbs=['employed', 'ensure'], about='a diverse range of assessment methods with adjustments', domain='none', award=[HON, MA],
  para="It is anticipated that varied assessment methods are used so that the whole range of housing knowledge, skills and standards is shown, with reasonable adjustments for disabled students where needed.",
  prac="Use a diverse range of methods so that every part of the knowledge, skills and standards can be evidenced, and make reasonable adjustments for disabled students.",
  ben="You can expect several kinds of assessment, so that you can show the full range of what you know and can do, with adjustments if you are disabled.",
  aaw="Describe this as an expectation (the statement says 'anticipated', a word outside the five) that diverse methods evidence the knowledge, skills and standards. Cite it as " + CITE + "3.20. Do not convert it into a 'must'. Set it beside " + SID + "3.16 and the threshold list (para 4.3).",
  aad="Raise it when a team checks whether its assessments cover every threshold item. Ask: 'Which threshold item has no assessment that evidences it?' Avoid presenting it to a student as their duty.")

# ---------------------------------------------------------------- section 4
s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='higher education providers',
  addressee='provider', verbs=['refer'], about='providers refer to Annex D for performance above threshold', domain='none', award=HON,
  para="Most students will do well above the minimum; each provider sets its own way of judging the evidence and should refer to Annex D, which classifies honours outcomes at FHEQ Level 6 and FQHEIS Level 10 and describes the four honours classes.",
  prac="When deciding what evidence shows performance above the threshold, use your own method but refer to Annex D's descriptions of the 1st, 2:1, 2:2 and 3rd at FHEQ Level 6 and FQHEIS Level 10.",
  ben=('n/a', 'a duty on the provider in setting classification evidence'),
  aaw="Describe this as a 'should' on providers: refer to Annex D of the qualification frameworks when judging performance above the threshold. Cite it as " + CITE + "4.2 and Annex D as std:doc:qaa-fheq-2024-framework, Annex D. Do not claim the statement sets its own classification criteria. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd and its 2.2, 2.1 and 1st cells, and spine:6.",
  aad="Raise it when a team writes marking criteria for honours. Ask: 'Where do your criteria for a 2:1 and a first draw on Annex D?' Avoid putting it to a student as their duty.")

# 4.3 threshold list: lead-in 'Bachelor's degrees in Housing Studies are awarded to students who meet the following threshold standard, demonstrating systematic understanding of:'
def th(n, verbs, about, domain, para, prac, ben, beside, q):
    s('4.3.b%d' % n, type='threshold', rung='threshold', force='threshold', level='fheq:6', appliesTo='honours graduates at the threshold',
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=("Present this as part of the minimum standard for an honours degree in Housing Studies, a threshold the award requires: "
           "systematic understanding of " + about + ", at FHEQ Level 6 (FQHEIS Level 10). Cite it as " + CITE + "4.3 (item " + str(n) + "). "
           "Do not call it a regulatory requirement or a master's outcome, and do not invent typical or excellent versions, which the statement leaves to marking schemes (para 4.4, 4.5). "
           "Set it beside " + beside + " and spine:6."),
      aad=("Raise it when a student asks what an honours degree in housing expects them to understand about " + about + ", or when a team checks module coverage. "
           "For a student, put it plainly as part of the floor for passing, in the second person; for staff, frame it as coverage the course must evidence in assessment. "
           "Ask: '" + q + "' Avoid reading the item aloud at length or treating it as the mark of a 2:1 or a first."))
TB = 'To reach the threshold for an honours degree, '
th(1, [], 'housing as a social determinant of well-being', 'knowledge',
   "Will have systematic understanding of why housing is a key social factor in the well-being of residents and communities.",
   "At threshold, graduates understand systematically how housing shapes the well-being of residents and communities.",
   TB + "you will understand in a systematic way how housing affects the well-being of the people and communities who live in it.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "How does poor housing affect someone's health or well-being, and what evidence shows it?")
th(2, [], 'state intervention and the changing production, consumption and experience of housing', 'understanding',
   "Will have systematic understanding of why the state intervenes in housing markets and how producing, consuming and living in housing are changing.",
   "At threshold, graduates understand systematically the case for state intervention in housing markets and how production, consumption and experience of housing change.",
   TB + "you will understand why governments step into the housing market and how the way homes are built, bought, rented and lived in keeps changing.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd", "Why might a government intervene in the housing market rather than leave it alone?")
th(3, [], 'how housing problems emerge and the policy and legal responses', 'knowledge',
   "Will have systematic understanding of how housing problems arise and are recognised, and of how policy and law have developed to deal with them.",
   "At threshold, graduates understand systematically how housing problems evolve and are identified and how policy and legal frameworks respond.",
   TB + "you will understand how housing problems come about and are recognised, and how policy and the law have changed to tackle them.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "Pick one housing problem: how did it come to be seen as a problem, and what did law or policy do about it?")
th(4, ['formulated', 'implemented', 'interacts'], 'how housing policy is made and implemented', 'understanding',
   "Will have systematic understanding of how housing policy is made and carried out locally and nationally, and how it connects with wider public policy.",
   "At threshold, graduates understand systematically how local and national housing policy is formulated and put into effect and how it relates to wider public policy.",
   TB + "you will understand how housing policy is made and put into practice locally and nationally, and how it links with other public policy.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd", "How does a national housing policy become something a local council does, and which other policies does it touch?")
th(5, [], 'housing organisations and their governance', 'knowledge',
   "Will have systematic understanding of the different kinds of housing organisation, how each is governed and the difficulties governance faces.",
   "At threshold, graduates understand systematically the forms of housing organisation, their governance and its challenges.",
   TB + "you will understand the different types of housing organisation, how they are run and governed and what makes governing them hard.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "How is a housing association governed differently from a local authority housing department?")
th(6, [], 'models of housing need and responsive systems', 'understanding',
   "Will have systematic understanding of the different ways housing need is modelled and of building systems that respond to diverse individuals and groups.",
   "At threshold, graduates understand systematically different models of housing need and how to develop systems that respond to diverse people and groups.",
   TB + "you will understand the different ways of defining housing need and how to build systems that respond to many different people and groups.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd", "Which model of housing need would you use to plan for an ageing population, and what would it miss?")
th(7, ['work', 'address'], 'how housing bodies and professionals tackle wider social inequality', 'understanding',
   "Will have systematic understanding of how housing organisations and practitioners can act on wider social inequalities at structural, institutional and individual level.",
   "At threshold, graduates understand systematically how housing organisations and professionals can tackle social inequalities structurally, institutionally and individually.",
   TB + "you will understand how housing organisations and the people who work in them can tackle wider social inequality at every level, from systems to individuals.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd and " + SID + "1.19", "Where could a housing officer reduce inequality in their own daily work, and where does it need change at a higher level?")
th(8, ['identifying', 'implementing'], 'comparative housing systems and transferring good practice', 'subject-skill',
   "Will have systematic understanding of comparing housing systems and policies across the UK and beyond, finding and applying lessons and good practice where they fit.",
   "At threshold, graduates understand systematically how to compare housing systems and policies within the UK and internationally and how to identify and apply learning and good practice.",
   TB + "you will understand how to compare housing systems across the UK nations and other countries, and how to pick out and use lessons that work elsewhere.",
   "qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r1/3rd and " + SID + "1.10", "What could one UK nation learn from another's approach to homelessness, and would it transfer?")
th(9, ['involving', 'engage', 'face'], 'resident involvement and reaching seldom-heard groups', 'understanding',
   "Will have systematic understanding of why involving residents in decisions helps and how to reach individuals and groups seldom heard because of barriers to taking part.",
   "At threshold, graduates understand systematically the benefits of resident involvement in decisions and how to engage seldom-heard people and groups facing barriers.",
   TB + "you will understand why it helps to involve residents in decisions and how to reach people and groups who are rarely heard because something stops them taking part.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r2/3rd", "Which residents are hardest to hear in a consultation you know of, and what would reach them?")
th(10, [], 'housing economics and finance', 'knowledge',
   "Will have systematic understanding of the core principles of housing economics and housing finance.",
   "At threshold, graduates understand systematically the main principles of housing economics and finance.",
   TB + "you will understand the main ideas of how housing economics and housing finance work.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "What drives house prices and rents, and how is new social housing paid for?")
th(11, [], 'business planning, service management and delivery', 'knowledge',
   "Will have systematic understanding of the core principles of the business planning cycle and of managing and delivering services.",
   "At threshold, graduates understand systematically the main principles of business planning, service management and service delivery.",
   TB + "you will understand the main ideas behind business planning and how housing services are managed and delivered.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "How would a housing service plan and check whether it is delivering what tenants need?")
th(12, [], 'choosing and applying research methods in housing', 'subject-skill',
   "Will have systematic understanding of selecting and using suitable research methods and methodologies in a housing setting.",
   "At threshold, graduates understand systematically how to identify and apply appropriate research methods and methodologies in housing contexts.",
   TB + "you will understand how to choose the right research methods for a housing question and how to use them.",
   "qaa/fheq-2024/4.15.b2, qaa/fheq-2024/annex-d/practical/r1/3rd", "What method would you use to find out why tenants leave a scheme, and why that one?")
th(13, [], 'evidence-based solutions to housing issues', 'subject-skill',
   "Will have systematic understanding of how to find solutions to housing issues that rest on evidence.",
   "At threshold, graduates understand systematically how to identify solutions to housing issues grounded in evidence.",
   TB + "you will understand how to find answers to housing issues that are backed by evidence.",
   "qaa/fheq-2024/4.15.b3.1, qaa/fheq-2024/annex-d/cognitive/r3/3rd", "What evidence would persuade you that a solution to overcrowding actually works?")
th(14, [], 'presenting information, data and concepts to varied audiences', 'generic-skill',
   "Will have systematic understanding of presenting information, data and ideas to different audiences.",
   "At threshold, graduates understand systematically how to put information, data and concepts across to different audiences.",
   TB + "you will understand how to present information, data and ideas to different kinds of audience.",
   "qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r1/3rd", "How would you explain the same rent data to tenants and to a council committee?")
th(15, [], 'leadership and management in housing organisations', 'knowledge',
   "Will have systematic understanding of the core principles of leading and managing in housing and how to apply them in housing organisations.",
   "At threshold, graduates understand systematically the key principles of housing leadership and management and their application in housing organisations.",
   TB + "you will understand the main ideas of leadership and management in housing and how they are used in housing organisations.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "What makes a good manager of a housing team, and how have you seen it done?")
th(16, [], 'environmental sustainability and the climate crisis in housing', 'knowledge',
   "Will have systematic understanding of aspects of environmental sustainability, including how the climate crisis bears on designing, developing, maintaining and managing housing.",
   "At threshold, graduates understand systematically aspects of environmental sustainability, including the climate crisis's impact across the design, development, maintenance and management of housing.",
   TB + "you will understand environmental sustainability in housing, including how the climate crisis affects the way homes are designed, built, maintained and managed.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd and " + SID + "1.23", "How should the climate crisis change the way an older housing stock is maintained?")
th(17, [], 'renewal, refurbishment and regeneration with resident engagement', 'knowledge',
   "Will have systematic understanding of the core principles of renewing, refurbishing and regenerating housing, involving residents in these processes and reaching fair outcomes.",
   "At threshold, graduates understand systematically the principles of housing renewal, refurbishment and regeneration, resident engagement in them and equitable outcomes.",
   TB + "you will understand the main ideas of renewing, refurbishing and regenerating housing, how to involve residents and how to make the results fair.",
   "qaa/fheq-2024/4.15.b1, qaa/fheq-2024/annex-d/knowledge/r1/3rd", "Who gains and who loses when an estate is regenerated, and how can residents shape it?")
th(18, [], 'the causes of tenure-related stigma', 'understanding',
   "Will have systematic understanding of analysing what leads to stigma attached to housing tenure.",
   "At threshold, graduates understand systematically how to analyse the factors behind tenure-related stigma.",
   TB + "you will understand how to analyse why people are stigmatised because of the kind of housing tenure they live in.",
   "qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r1/3rd and " + SID + "1.16", "Why are social tenants sometimes stigmatised, and where does that come from?")
s('4.3.b19', type='threshold', rung='threshold', force='threshold', level='fheq:6', appliesTo='accredited honours courses',
  addressee='provider', verbs=['ensure', 'met'], about='CIH specification met in full on accredited courses', domain='none', award=HON,
  para="On accredited courses, the requirements of the CIH specification are to be met in full, as part of the threshold.",
  prac="If the course is accredited by the CIH, make sure every requirement of its specification is fully met.",
  ben=('n/a', 'a duty on accredited courses, not an understanding the student shows'),
  aaw="Describe this as a condition placed in the threshold list for accredited courses only: the CIH specification must be fully met. Cite it as " + CITE + "4.3 (item 19). Do not present it as a learning outcome or as applying to unaccredited courses; the CIH specification is the body's own document (not yet ingested, Part E). Set it beside " + SID + "2.19 and " + SID + "2.15.",
  aad="Raise it when an accredited course reviews its outcomes. Ask: 'Which CIH requirements does each module meet, and are any left uncovered?' Avoid putting it to a student as an item they must show.")

s('4.4', type='typical', rung='typical', force='will', level='fheq:6', appliesTo='honours graduates at 2:1 and 2:2',
  addressee='both', verbs=[], about='typical rung set by providers\' marking schemes', domain='none', award=HON,
  para="Criteria for achievement above the threshold at 2:1 and 2:2 will follow each provider's common or generic undergraduate marking scheme; the statement lists no typical items.",
  prac="Judge 2:1 and 2:2 work against your institution's common or generic undergraduate marking scheme; the statement gives no subject list for this rung.",
  ben="For a 2:1 or a 2:2 you will be judged against your university's own marking scheme, which goes beyond the threshold.",
  aaw="Describe this as the typical rung, stated as a 'will' that hands its criteria to each provider's marking scheme rather than listing outcomes. Cite it as " + CITE + "4.4. Do not invent subject-specific typical outcomes. Set it beside qaa/fheq-2024/annex-d/summary/r1/2.2 and qaa/fheq-2024/annex-d/summary/r1/2.1, the threshold list (" + SID + "4.3.b1) and spine:6.",
  aad="Raise it when a student asks what a 2:1 needs in this subject. Put it plainly: the subject sets the floor, your university's marking scheme sets the 2:1 and 2:2. Ask: 'Have you read the marking criteria for your next assessment?' Avoid presenting the threshold items as enough for a 2:1.")
s('4.5', type='excellent', rung='excellent', force='will', level='fheq:6', appliesTo='honours graduates at first class',
  addressee='both', verbs=[], about='excellent rung set by providers\' marking schemes', domain='none', award=HON,
  para="Criteria for excellent, first-class achievement will follow each provider's common or generic undergraduate marking scheme; the statement lists no excellent items.",
  prac="Judge first-class work against your institution's common or generic undergraduate marking scheme; the statement gives no subject list for this rung.",
  ben="For a first you will be judged against your university's own marking scheme for excellent work.",
  aaw="Describe this as the excellent rung, stated as a 'will' that hands its criteria to each provider's marking scheme. Cite it as " + CITE + "4.5. Do not invent subject-specific excellent outcomes or treat them as the minimum. Set it beside qaa/fheq-2024/annex-d/summary/r1/1st, " + SID + "4.4 and spine:6.",
  aad="Raise it when a student asks what a first looks like. Put it plainly: the subject leaves it to your university's criteria, which usually reward independence and originality. Ask: 'What would make your next piece go beyond what was taught?' Avoid presenting first-class qualities as the pass mark.")

# 4.6 master's (another award, not another rung: the brief's `.masters` convention)
def ma(i, find, verbs, about, domain, para, prac, ben, beside, q):
    s(i, find=find, type='threshold', rung='threshold', force='threshold', level='fheq:7', appliesTo="master's graduates in Housing Studies",
      addressee='learner', verbs=verbs, about=about, domain=domain, award=MA, para=para, prac=prac, ben=ben,
      aaw=("Present this as a condition of a master's award in Housing Studies, read at the threshold: " + about + ", at FHEQ Level 7 (FQHEIS Level 11). "
           "Cite it as " + CITE + "4.6. Do not apply it to the honours degree or call it regulatory. Set it beside " + beside + " and spine:7."),
      aad=("Raise it with a master's student planning a dissertation or critical review, or with a team writing master's outcomes. "
           "Put it plainly in the second person for a student and as a minimum for the award for staff. Ask: '" + q + "' "
           "Avoid reading the paragraph aloud or confusing it with the honours threshold."))
ma('4.6.masters', "Master's level degrees in Housing Studies are awarded to students who demonstrate understanding of knowledge in the housing domain, as outlined in the undergraduate threshold, much of which is at the forefront of the academic field of study and professional practice.",
   ['demonstrate'], 'understanding of housing knowledge much of it at the forefront of research and practice', 'knowledge',
   "Will have shown understanding of the housing knowledge set out for the honours threshold, much of it at the leading edge of scholarship and professional practice.",
   "Master's graduates show understanding of the housing knowledge in the undergraduate threshold, with much of it reaching the forefront of research and of practice.",
   "For a master's in housing you will show you understand the knowledge set for the honours degree, much of it at the leading edge of research and professional practice.",
   "qaa/fheq-2024/4.17.b1, " + SID + "4.3.b1", "Which part of your housing knowledge is closest to current research or new practice?")
ma('4.6.b1.masters', 'evaluate current research and advanced scholarship', ['evaluate'], 'evaluating current research and advanced scholarship', 'subject-skill',
   "Will be able to judge current research and advanced scholarship.",
   "Master's graduates evaluate current research and advanced scholarship critically.",
   "For a master's you will be able to judge the quality and value of current research and advanced scholarship.",
   "qaa/fheq-2024/4.17.b4.1", "Which recent housing study would you challenge, and on what grounds?")
ma('4.6.b2.masters', 'understand how knowledge is advanced through research', ['understand'], 'how research advances knowledge', 'understanding',
   "Will understand the ways research moves knowledge forward.",
   "Master's graduates understand how research advances knowledge.",
   "For a master's you will understand how research moves knowledge forward.",
   "qaa/fheq-2024/4.17.b3", "How did one study you know change what the field thought about housing?")
ma('4.6.b3.masters', 'identify the boundaries of knowledge', ['identify'], 'the limits of current knowledge', 'understanding',
   "Will be able to recognise where present knowledge stops.",
   "Master's graduates identify where the limits of current knowledge lie.",
   "For a master's you will be able to see where current knowledge in housing runs out.",
   "qaa/fheq-2024/4.17.b1", "What question in your topic does nobody yet have a good answer to?")
ma('4.6.b4.masters', 'create new insights in the field of study.', ['create'], 'creating new insight in the field', 'subject-skill',
   "Will be able to produce new insight in the field.",
   "Master's graduates create new insights in housing studies.",
   "For a master's you will be able to produce new insight in housing studies.",
   "qaa/fheq-2024/4.17.b3, qaa/fheq-2024/4.17.b6", "What will your dissertation add that was not known before?")

s('4.7', type='expectation', rung='none', force='describes', level='fheq:7', appliesTo="master's students",
  addressee='learner', verbs=['developed', 'enhanced', 'achieve'], about="higher-level skills at the FHEQ Level 7 and FQHEIS Level 11 descriptor", domain='generic-skill', award=MA,
  para="Higher-level skills grow through self-directed academic and professional development, and master's students are expected to achieve to the descriptor for a qualification at FHEQ Level 7 and SCQF Level 11 on the FQHEIS.",
  prac="Develop master's students' higher-level skills through self-directed academic and professional work, and set master's outcomes against the FHEQ Level 7 (FQHEIS Level 11) qualification descriptor.",
  ben="On a master's course you will build higher-level skills largely by directing your own academic and professional development, to the level set for master's qualifications across the UK.",
  aaw="Describe this as an expectation ('expected to', a word outside the five) that master's students achieve to the FHEQ Level 7 and FQHEIS Level 11 descriptor, which the statement adopts rather than restates. Cite it as " + CITE + "4.7. Do not copy the descriptor into a programme document as if it were the statement's own text. Set it beside qaa/fheq-2024/4.17.b1 to qaa/fheq-2024/4.17.b8.3 (shared by fqheis:11) and spine:7.",
  aad="Raise it when a master's student asks how master's study differs from undergraduate study. Put it plainly: more of the work is self-directed and the bar is set by the national master's descriptor. Ask: 'Which part of your learning are you now steering yourself?' Avoid reading the descriptor aloud at length.")

# 4.8 transferable and generic skills, both awards: lead-in 'Undergraduate and postgraduate degrees in Housing Studies are awarded to students who are able to:'
def gs(n, verbs, about, domain, para, prac, ben, b6, b7, q):
    s('4.8.b%d' % n, type='outcome', rung='none', force='will', level='fheq:6', appliesTo='undergraduate and postgraduate graduates',
      addressee='learner', verbs=verbs, about=about, domain=domain, award=[HON, MA], para=para, prac=prac, ben=ben,
      aaw=("Present this as a skill the statement makes a condition of both undergraduate and postgraduate Housing Studies awards ('are able to', recorded as will): " + about + ". "
           "Cite it as " + CITE + "4.8 (item " + str(n) + "). Do not present it as housing knowledge or as regulatory, and read it at the award's level. "
           "At honours set it beside " + b6 + " and spine:6; for a master's, beside " + b7 + " and spine:7."),
      aad=("Raise it when a student reflects on skills for a portfolio, placement or job application, or when a team maps skills across modules. "
           "Put it in plain words, in the second person for a student, and as a skill the award requires for staff. Ask: '" + q + "' "
           "Avoid reading the item aloud at length or implying the master's and honours versions demand the same depth."))
GB = 'By the end of your degree, '
gs(1, ['work', 'identify', 'produce'], 'independent and joint work on complex problems and synthesis of knowledge', 'generic-skill',
   "Will be able to work alone and with others to find complex problems and draw together what is known on a subject or topic.",
   "Graduates will work alone and in teams to pinpoint complex problems and synthesise the current state of knowledge on a subject or topic.",
   GB + "you will be able to work on your own and with others to spot complex problems and pull together what is already known about a topic.",
   "qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r2/3rd", "qaa/fheq-2024/4.17.b5", "Can you sum up in a page what is known about a housing problem you care about?")
gs(2, ['take', 'demonstrate', 'reach', 'communicate'], 'ownership of learning, judgement and communicating ideas', 'generic-skill',
   "Will be able to own their learning, show conceptual understanding, judge soundly and communicate ideas well to varied audiences.",
   "Graduates will take personal responsibility for their learning, show conceptual understanding, make sound judgements and communicate ideas effectively to different audiences.",
   GB + "you will be able to take charge of your learning, show you grasp the ideas, make sound judgements and explain your ideas well to different people.",
   "qaa/fheq-2024/4.15.b5, qaa/fheq-2024/4.15.b8, qaa/fheq-2024/annex-d/transferable/r1/3rd", "qaa/fheq-2024/4.17.b5, qaa/fheq-2024/4.17.b8.3", "When did you last change your view after weighing evidence, and how did you explain it?")
gs(3, ['collaborate', 'reflecting'], 'collaboration across disciplines in assessed and other activities', 'generic-skill',
   "Will be able to work with others in assessed and unassessed activities, including people from other disciplines, as the inter-professional nature of housing work demands.",
   "Graduates will collaborate in assessed and non-assessed activities, including with other disciplines, mirroring the inter-professional character of housing practice.",
   GB + "you will be able to work with others, including people from other professions, in assessed and unassessed tasks, as you will in housing work.",
   "qaa/fheq-2024/annex-d/transferable/r2/3rd, qaa/fheq-2024/4.15.b9.1", "qaa/fheq-2024/4.17.b8.1", "What did you learn from working with someone trained in another profession?")
gs(4, ['demonstrate', 'addressing'], 'awareness of and professional responsibility for equality, diversity and inclusion', 'generic-skill',
   "Will be able to show awareness of equality, diversity and inclusion issues and take professional responsibility for dealing with them.",
   "Graduates will show awareness of equality, diversity and inclusion issues and accept professional responsibility for addressing them.",
   GB + "you will be able to show that you understand issues of equality, diversity and inclusion and that you take professional responsibility for acting on them.",
   "qaa/fheq-2024/4.15.b9.1, " + SID + "1.19", "qaa/fheq-2024/4.17.b8.1", "Where in housing work would you have to act on unfairness, and what would you do?")
gs(5, ['use', 'assemble', 'evaluate'], 'using ICT to gather and evaluate information and data', 'generic-skill',
   "Will be able to use various information and communications technology packages to collect and judge information and data from many sources.",
   "Graduates will use a range of ICT packages to gather and weigh information and data from varied sources.",
   GB + "you will be able to use a range of software to gather and assess information and data from different sources.",
   "qaa/fheq-2024/annex-d/transferable/r1/3rd, qaa/fheq-2024/annex-d/practical/r4/3rd", "qaa/fheq-2024/4.17.b2", "Which tools do you use to find and check housing data, and how do you judge a source?")
gs(6, ['identify', 'formulate'], 'identifying housing problems, sustainability included, and alternative solutions', 'subject-skill',
   "Will be able to recognise housing problems, environmental and sustainability ones among them, and devise other possible solutions.",
   "Graduates will identify housing problems, environmental and sustainability ones among them, and devise alternative solutions.",
   GB + "you will be able to spot housing problems, including environmental and sustainability ones, and come up with different ways to solve them.",
   "qaa/fheq-2024/4.15.b7, qaa/fheq-2024/annex-d/cognitive/r3/3rd", "qaa/fheq-2024/4.17.b5", "For one housing problem, what are two different solutions and what does each cost the environment?")
gs(7, ['reflect', 'manage'], 'reflecting on and managing learning, development and ethical practice', 'generic-skill',
   "Will be able to reflect on and direct their own learning and personal development and their ethical and professional practice.",
   "Graduates will reflect on and direct their own learning, personal development and ethical, professional practice.",
   GB + "you will be able to reflect on and manage your own learning and personal growth, and how you act ethically and professionally.",
   "qaa/fheq-2024/annex-d/transferable/r3/3rd, qaa/fheq-2024/annex-d/transferable/r5/3rd, qaa/fheq-2024/4.15.b9.3", "qaa/fheq-2024/4.17.b8.3", "What would you change about how you learn, and why?")
gs(8, ['reflect', 'utilise', 'enhance'], 'using learning for employability and entrepreneurship', 'generic-skill',
   "Will be able to reflect deliberately on their learning and use it to improve employability and entrepreneurship in line with the career they want.",
   "Graduates will consciously reflect on and use their learning to strengthen their employability and entrepreneurship for the career they intend.",
   GB + "you will be able to think about what you have learned and use it to make yourself more employable and enterprising for the career you want.",
   "qaa/fheq-2024/annex-d/transferable/r4/3rd, qaa/fheq-2024/4.15.b9.3", "qaa/fheq-2024/4.17.b8.1", "Which thing you learned this year would most help you get the housing job you want?")

GRADE = {}
TH = {'1.13': 'theme:edi', '1.15': 'theme:edi',
      '1.22': 'theme:esd', '1.23': 'theme:esd', '1.25': 'theme:esd', '1.27': 'theme:esd', '1.28': 'theme:esd', '1.29': 'theme:esd', '1.30': 'theme:esd',
      '1.26.b1': 'theme:esd', '1.26.b2': 'theme:esd', '1.26.b3': 'theme:esd', '1.26.b4': 'theme:esd', '1.26.b5': 'theme:esd',
      '1.34': 'theme:enterprise', '1.35': 'theme:enterprise', '2.5': 'theme:accessibility', '2.6': 'theme:accessibility'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.7; 4.2'), dict(id='fqheis:10', role='cites', locator='D1, 2.7; 4.2'),
            dict(id='fheq:7', role='cites', locator='D1, 2.9; 4.7'), dict(id='fqheis:11', role='cites', locator='D1, 2.9; 4.7'),
            dict(id='spine:6', role='inferred', locator='std:ref:uk-framework R2 (honours)'),
            dict(id='spine:7', role='inferred', locator='std:ref:uk-framework R2 (master\'s)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.7: degree with honours, FHEQ Level 6, FQHEIS Level 10; 4.2)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.9; 4.7: one descriptor, FHEQ Level 7 and SCQF Level 11)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.11', '1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19']),
      dict(id='theme:esd', role='carries', carriedIn=['1.11', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.11', '1.31', '1.32', '1.33', '1.34', '1.35']),
      dict(id='theme:accessibility', role='carries', carriedIn=['2.5', '2.6'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-housing-studies-2019-benchmarks (not ingested)', note='the third edition (2019), named in section 6; the front matter lists key changes from the previous Statement'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2); the FHEQ Level 7 descriptor (4.7)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Levels 10 and 11 (2.7, 2.9, 4.7)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='quoted for the UNESCO definition of ESD (1.20); source of Figure 4 (3.17)'),
      dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='source of Figure 3 (1.33)'),
      dict(rel='refersTo', target='CIH specification for chartered membership and CIH Professional Standards (not yet ingested)', note='1.4, 2.2, 2.19, 4.3: Part E'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary; QAA guide to comparing qualifications in the UK and Ireland (not ingested)', note='front matter; 2.10')]
S8 = dict(published='2022-03', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='advisory group with members from all four nations, including the CIH (D1, front matter; section 6)',
          replacedBy='none', editions='first 2007 (original), second 2014, third 2019 (aligned with the 2018 Quality Code), fourth March 2022 (D1, section 6)')

SB1 = [
    'A field of study, interdisciplinary since the early 1980s, that starts from a household\'s basic need for a home in which to live well and flourish (D1, 1.1, 1.2, 2.1).',
    'It links home, dwellings and neighbourhoods with the institutions and actors that provide housing, across market and social sectors, judged by adequacy, affordability and security (D1, 1.2).',
    'It draws on the social sciences, law, health, geography, planning, surveying, construction, architecture and management; it applies theory to practical situations (D1, 1.3, 2.4, 3.1).',
    'It is vocational and functional: knowledge that can be applied, with a three-fold design joining behaviours and values, skills and knowledge, shaped by the CIH\'s professional standards (D1, 1.4, 2.1, 2.2).',
    'It sees itself as a subject of social justice, attentive to rights, homelessness and the lived experience of housing, including students\' own (D1, 1.2, 1.13, 2.6).',
    'Its courses reflect devolved housing law, policy and governance across the four UK nations (D1, 1.10).',
    'Students arrive by many routes, often already working in housing; recognition of prior learning, part-time study and employer partnerships are characteristic (D1, 1.4, 2.6, 2.11, 2.13, 2.15).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='framed as social justice: housing rights, disadvantage, intersectional inequality, class and tenure stigma and the most vulnerable groups as content; an inclusive curriculum that recognises students may have known housing precarity; inclusive behaviours for graduates (D1, 1.12 to 1.19); also in content and the generic skills (D1, 3.1, 4.8)',
         statements=['1.13', '1.15', '4.3.b7', '4.3.b18', '4.8.b4', '3.12']),
    dict(theme='theme:esd', inThisSubject='built on the UN SDGs, with SDG 11 and target 11.1 on adequate, safe and affordable housing at the centre; UNESCO\'s eight competencies adapted for housing; the campus and community as a living laboratory (D1, 1.20 to 1.30); repeated in delivery and in the threshold and generic skills (D1, 3.14, 4.3, 4.8)',
         statements=['1.22', '1.23', '1.25', '1.26.b1', '1.26.b2', '1.26.b3', '1.26.b4', '1.26.b5', '1.27', '1.28', '1.29', '1.30', '3.14.b3', '3.14.b5', '4.3.b16', '4.8.b6']),
    dict(theme='theme:enterprise', inThisSubject='headed employability and enterprise education: a vocational subject whose entrepreneurship includes social entrepreneurship, careers across public, private and third sectors, placements and the reflective, resilient practitioner (D1, 1.31 to 1.35); work experience through employer partnerships (D1, 2.15)',
         statements=['1.34', '1.35', '2.15', '4.8.b8']),
    dict(theme='theme:accessibility', inThisSubject='accessible environments, materials and site visits for students with learning or mobility needs and for those disadvantaged by structural inequality; content designed so lived experience of housing problems is not a barrier (D1, 2.5, 2.6); adjustments in teaching and assessment (D1, 3.7, 3.20)',
         statements=['2.5', '2.6', '1.26.b2', '3.14.b2', '3.16', '3.20']),
]
SB3 = dict(
    areas=[dict(component='3.1', gloss='26 core topics: meanings of home and homelessness; EDI and decolonisation; sustainable development and the climate crisis; people and place; history, policy, law, governance and regulation; leadership and management; politics; economics and finance; inequality and tenure stigma; strategic planning; devolution; place and regeneration; place and property management; housing practice and services; homelessness; housing and health; sustainable construction and retrofit; contemporary and digital practice; ethics and professionalism; research methods'),
           dict(component='1.16', gloss='themes of inclusive housing knowledge: rights, disadvantage, need, differential access, social harm, intersectional inequality, class and tenure stigma, vulnerable migrants and refugees'),
           dict(component='1.24', gloss='the eight UNESCO key competencies for sustainability adapted to housing (Figure 2)')],
    practices=[dict(component='3.7', kind='teaching', gloss='lectures, small groups, supervision, directed study, site and virtual visits, problem-based and team learning, negotiated and work-related learning'),
               dict(component='3.11', kind='teaching', gloss='alternative viewpoints, reflection and real challenges in a living laboratory'),
               dict(component='3.13', kind='learning', gloss='blended and online group learning on real problems'),
               dict(component='3.14', kind='learning', gloss='an interdisciplinary, inclusive learning environment with ESD and synoptic assessment'),
               dict(component='1.18', kind='learning', gloss='inclusive learning experiences around housing disadvantage and respect for views'),
               dict(component='2.15', kind='learning', gloss='work experience through employer partnerships'),
               dict(component='3.3', kind='learning', gloss='work-based and work-related learning on accredited courses'),
               dict(component='3.15', kind='assessment', gloss='an aligned assessment and feedback strategy with clear criteria'),
               dict(component='3.18', kind='assessment', gloss='self, peer and synoptic assessment; authentic tasks; ESD assessed in and beyond the curriculum'),
               dict(component='3.19', kind='assessment', gloss='essays, reports, policy briefs, exams, presentations, projects, journals, dissertations, digital and work-based assessment')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3', award=HON, items=19),
           dict(rung='threshold', leadIn='4.6', award=MA, items=5),
           dict(rung='typical', leadIn='4.4', award=HON, items=1),
           dict(rung='excellent', leadIn='4.5', award=HON, items=1)],
    rungBases="4.1: the threshold is the minimum for an honours award; 4.2: most students perform well above it, judged by each provider with reference to Annex D; 4.4 and 4.5: typical (2:1, 2:2) and excellent (1st) follow providers' marking schemes, with no subject items listed. The master's list (4.6) is another award, recorded at its threshold.",
    outcomeLists=[dict(leadIn='4.8', gloss='transferable and generic skills for undergraduate and postgraduate awards', items=8, award=['honours', "master's"])],
    outcomes=[])
SB4A_FULL = []
SB5 = [dict(body='Chartered Institute of Housing (CIH)',
            says='a leading UK and international professional body that accredits many courses and influences their outcomes; the statement draws on its accreditation but stays distinct from its specification; its Professional Standards Framework shapes course values; chartered membership needs prescribed work experience and a CIH-accredited Postgraduate Diploma usually meets its criteria; it offers its own progression routes and validates courses (D1, front matter, 1.4, 1.7, 1.10, 2.2, 2.9, 2.10, 2.11, 2.15, 2.19, 4.3)',
            requirements='not yet ingested (Part E)'),
       dict(body='Housing Studies Association; Collaborative Centre for Housing Evidence',
            says='external networks that support an early career research community (D1, 2.12)',
            requirements='not-applicable-by-design'),
       dict(body='Office for Students',
            says='its regulatory framework does not treat Subject Benchmark Statements as sector-recognised standards in England (D1, front matter)',
            requirements='not-applicable-by-design')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['front matter', '1.11', '1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.21', '1.23', '1.26', '1.29', '1.33', '1.35', '2.2', '2.6', '3.1', '3.2', '3.4', '3.12', '3.13', '3.14', '3.16', '4.8'],
                 statements=[SID + x for x in ['1.13', '1.15', '1.26.b2', '2.6', '3.12', '3.14.b2', '3.16', '4.3.b7', '4.3.b18', '4.8.b4']]),
            dict(id='theme:esd', named='Sustainability (front matter and 1.11: education for sustainable development; education for sustainability)', carriedIn=['front matter', '1.11', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30', '1.33', '1.35', '3.1', '3.4', '3.10', '3.12', '3.13', '3.14', '3.17', '3.18', '4.3', '4.8'],
                 statements=[SID + x for x in ['1.22', '1.23', '1.25', '1.26.b1', '1.26.b2', '1.26.b3', '1.26.b4', '1.26.b5', '1.27', '1.28', '1.29', '1.30', '3.12', '3.14.b3', '3.14.b5', '4.3.b16', '4.8.b6']]),
            dict(id='theme:enterprise', named='Employability and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['front matter', '1.11', '1.21', '1.31', '1.32', '1.33', '2.13', '2.15', '3.7', '4.8'],
                 statements=[SID + x for x in ['1.34', '1.35', '2.15', '4.8.b8']]),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.26', '2.5', '2.6', '3.7', '3.8', '3.14', '3.16', '3.20'],
                 statements=[SID + x for x in ['1.26.b2', '2.5', '3.8', '3.14.b2', '3.16', '3.20']])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.7', '2.9', '4.2', '4.7', 'back matter']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.7', '2.9', '2.10', '4.2', '4.7']),
                dict(framework='other: national qualification and credit frameworks, unnamed', levels=[], citedIn=['1.9'])],
    bodies=[dict(body='Chartered Institute of Housing', citedIn=['front matter', '1.4', '1.7', '1.10', '2.2', '2.9', '2.10', '2.11', '2.15', '2.19', '4.3', 'back matter']),
            dict(body='Housing Studies Association', citedIn=['2.12']),
            dict(body='Collaborative Centre for Housing Evidence', citedIn=['2.12']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='the four honours classifications, the reference for performance above the threshold'),
                     dict(document='std:doc:qaa-fheq-2024-framework', named='the descriptor for a higher education qualification at Level 7 on the FHEQ; QAA (2014) The Frameworks for Higher Education Qualifications', citedIn=['4.7', 'back matter'], role="sets the master's level"),
                     dict(document='std:doc:qaa-fqheis-2024-framework', named='SCQF Level 11 on the FQHEIS', citedIn=['4.7'], role="the Scottish name for the master's level"),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance (Advance HE and QAA, 2021)', citedIn=['1.20', '3.17', 'back matter'], role='the UNESCO definition of ESD; assessment of, for and as learning (Figure 4)'),
                     dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and entrepreneurship education (QAA 2018)', citedIn=['1.33', 'back matter'], role='Figure 3, the relationship of entrepreneurship, enterprise and employability'),
                     dict(document='not yet ingested: listed in Part E', named='QAA guide to comparing qualifications in the UK and Ireland', citedIn=['2.10'], role='comparing qualification frameworks'),
                     dict(document='not yet ingested: listed in Part E', named="Advice and Guidance to support the Quality Code; QAA's Glossary; The UK Quality Code for Higher Education (2018)", citedIn=['front matter', 'back matter'], role='course design and review; unfamiliar terms')])

B1 = [dict(slug='education-for-sustainable-development', definition='the process of building curriculum structures and subject content that support and enact sustainable development (D1, 1.20)',
           beneficiaryDefinition='learning designed so that you can understand and act for sustainable development', scopeNote='ESD in the text; theme:esd', category='unknown', practices=['education']),
      dict(slug='sustainable-development', definition='an aspirational, continuing process of addressing social, environmental and economic concerns for a better world (D1, 1.20)',
           beneficiaryDefinition='working on social, environmental and economic problems together to make the world better', scopeNote='as the statement defines it', category='unknown', practices=['education']),
      dict(slug='living-laboratory', definition='the campus, community and housing sector used as a setting for authentic learning (D1, 1.27, 3.11)',
           beneficiaryDefinition='using real places around you as somewhere to study housing', scopeNote='', category='unknown', practices=['education']),
      dict(slug='recognition-of-prior-learning', definition='mechanisms that credit learning gained before entry, from study or work (D1, 2.11)',
           beneficiaryDefinition='having what you already learned at work or elsewhere counted towards your course', scopeNote='RPL in the text', category='unknown', practices=['education'])]
B2A = [dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='sustainable-development', form='Sustainable Development', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='living-laboratory', form="'living laboratory'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='recognition-of-prior-learning', form='recognition of prior learning (RPL)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []
B5 = []
D3 = [dict(source='Chartered Institute of Housing: specification for chartered membership (course validation) and Professional Standards', why='the body\'s requirements linked from 2.19, 4.3 and SB5'),
      dict(source='QAA guide to comparing qualifications in the UK and Ireland', why='named in 2.10'),
      dict(source='UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives; United Nations (2015) Transforming Our World', why='the competencies and goals 1.20 to 1.25 build on')]

E = [
    'Run 0112 pattern: one rung list only. The threshold (4.3, 19 items) is listed; typical (4.4) and excellent (4.5) are one-sentence paragraphs that hand their criteria to providers\' marking schemes. Each is recorded as one rung statement (rung typical, excellent) with no items beneath it; SB4 outcomes is empty and no gradeOf link is made. Unlike Psychology (three parallel lists).',
    'Threshold lead-in (4.3) has no modal: "are awarded to students who meet the following threshold standard, demonstrating systematic understanding of"; force recorded as threshold, the issuer defining it as the minimum for the award (4.1).',
    '4.3.b19 ("for accredited courses, ensure requirements of CIH specification are fully met") is a provider condition inside the threshold list; recorded as a threshold record with domain none and addressee provider. For P3.',
    "Master's level: 4.6 is another award, recorded per the batch-1 convention as rung threshold, award master's, level fheq:7, with the id suffix .masters (the stem sentence as 4.6.masters, the four items as 4.6.b1.masters to 4.6.b4.masters, cut by find). Its lead-in also has no modal; force threshold.",
    "4.7 says master's students are \"expected to achieve\" to the FHEQ Level 7 and FQHEIS Level 11 descriptor: \"expected to\" is outside the five; force describes. For Abbott.",
    "4.8's lead-in covers \"Undergraduate and postgraduate degrees\": the eight skills are recorded once with award [bachelor's with honours, master's] and level fheq:6; at a master's they read at fheq:7. For P3 whether to split by award.",
    'Obliging words outside the five, recorded as describes: "the expectation is" (1.23), "anticipated" and "expected to" (3.4), "it is expected" (3.7), "anticipated" (3.20), "expected to" (4.7). Also met inside statements recorded at a modal they carry: "expectation is" (1.25, 1.27), "is expected to" (3.3, 3.8, 3.16), "anticipated" (2.15). For Abbott.',
    '"requires" read as must (convention: required is must): ESD "requires a learning environment in which" (1.26, five items) and housing studies education "requires a learning environment in which" (3.14, six items); CIH chartered membership "requires prescribed work experience" (2.15); "need to be delivered" and "required engagement" (2.19). The two environment lists overlap (four items near-identical); both recorded. For P3.',
    '"will need to" (1.10) recorded at its modal will; the need is plain. For Abbott.',
    'Plain-present provider norms, not statements (template open point 5): 1.4 (courses support students), 1.12 (courses acknowledge and promote the Equality Act 2010), 2.9 (objectives achieved at Level 7/11), 2.13, 2.14, 3.18 (assessment tasks ensure students are able to demonstrate at least the threshold).',
    'Not cut as statements: 1.16 (themes of inclusive knowledge, no modal); 1.17 (questions); 1.18 ("would include"); 1.19 (inclusive behaviours that "can be identified as", nine items: a list of graduate behaviours with no outcome lead-in; strong candidate for P3); 1.24 Figure 2 (26 competency items under "A Housing Studies student who displays this competency can", adapted from UNESCO and flattened from a table with its column headings run into the items; read as a description of the competencies, with 1.25 carrying the expectation; for P3); 2.8 ("would be expected"); 2.18 ("typically ... will be asked", a description of external examining); 3.2 (desired outcomes, no modal); 3.9 ("desirable"); 3.10 ("may"); 4.1 (introduces the threshold, used as rungBases).',
    'Skeleton corrections: 3.1 tagged as a typical rung lead-in because of "a typical Housing Studies course"; it is the content list (SB3 area), not a rung. Skeleton rung counts (threshold 23, typical 26) set aside. Candidate statements 1.16.b*, 1.17.b*, 1.18.b*, 1.19.b*, 1.24.b*, 3.1.b*, 3.7.b*, 3.19.b* not taken (see above); 3.7 recorded once as a paragraph statement because its list is examples.',
    'Headings run into the preceding paragraph in the held text (for example "Equality, diversity and inclusion" at the end of 1.11, "Sustainability" in the last item of 1.19, "Employability and enterprise education" at the end of 1.30); SB6 citedIn excludes paragraphs that carry a theme only through such a trailing heading.',
    'Codes: HECoS 100196 housing (basis stated: the statement names the subject, matching the HECoS term); CAH13-01-04 planning (urban, rural and regional) is the CAH3 parent of 100196 in the HESA store, basis inferred; the statement names no code. For P3.',
    'Levels inferred from the reference framework: spine:6 and spine:7 (std:ref:uk-framework R2), used in S5 and the agent instructions.',
    '2.10 cites "SCQF 5-8 equivalent" for CIH courses at Levels 2 to 5 and CIH entry at "Levels 4, 5 or 6" after Levels 3, 4 and 5 (framework unnamed, likely the RQF or CQFW); SCQF 5 and 6 fall outside the fqheis ids (fqheis:7 to 12), so no level ids are recorded for them. For P3.',
    '2.9 names "Postgraduate Certificate of Education" as a postgraduate exit award; likely a slip for Postgraduate Certificate (recall); not corrected.',
    'Foundation degrees (fheq:5) are informed by the statement (1.6, 1.9) but not covered; levelsCovered holds only the two awards it sets standards for.',
    'Bodies: the CIH\'s specification and Professional Standards are not yet ingested (SB5, D3). Advance HE is co-issuer of the ESD guidance, not a body here.',
    'Shared documents not yet ingested: QAA guide to comparing qualifications (2.10); Quality Code and its Advice and Guidance, QAA Glossary (front matter). The 2014 Frameworks cited in section 5 are read as the 2024 edition (std:doc:qaa-fheq-2024-framework); for P3.',
    'Supersedes: the third edition (2019) is named in section 6 but not ingested; S7 target is a placeholder id.',
    'Generative AI: not named in this statement (no theme:generative-ai).',
    'S9 not researched in P1.',
]
