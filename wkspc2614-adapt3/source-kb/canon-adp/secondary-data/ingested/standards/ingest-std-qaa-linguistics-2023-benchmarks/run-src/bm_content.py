# bm_content.py: judgement for run 0118, QAA Subject Benchmark Statement Linguistics (September 2023). std.
# Brief: tools/BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft. Built by tools/bm_build.py.
HON = "bachelor's with honours"
CITE = 'QAA (2023) Linguistics Subject Benchmark Statement'
F = 'std:doc:qaa-fheq-2024-framework'

META = dict(
    run='0118', p1='2026-10-03 17:59',
    title='Subject Benchmark Statement Linguistics',
    heading='Subject Benchmark Statement: Linguistics (QAA, September 2023)',
    edition='September 2023', published='2023-09',
    status='current',
    supersedes='std:doc:qaa-linguistics-2019-benchmarks (the fourth edition, 2019, named in the back matter; not ingested)',
    subjects=[
        dict(scheme='hecos', code='100328', label='linguistics', basis='stated'),
        dict(scheme='cah', code='CAH19-01-07', label='linguistics', basis='stated'),
        dict(scheme='hecos', code='100970', label='applied linguistics', basis='stated'),
        dict(scheme='hecos', code='100972', label='phonetics', basis='stated'),
        dict(scheme='hecos', code='101016', label='sociolinguistics', basis='stated'),
        dict(scheme='hecos', code='101035', label='psycholinguistics', basis='stated'),
        dict(scheme='hecos', code='101410', label='historical linguistics', basis='stated'),
        dict(scheme='hecos', code='100971', label='phonetics and phonology', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2023 revision with the cross-cutting themes (the back matter names a 2019 fourth edition; this one as the fifth is inferred)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a Linguistics graduate should know and be able to do at the end of an honours degree "
                     "(FHEQ Level 6, FQHEIS Level 10). It gives one rung only, a list of fifteen minimum threshold items, beside a separate list of "
                     "fifteen generic skills and a few expected outcomes in its narrative sections; anything above the threshold is left to the "
                     "degree classification descriptions in Annex D of the FHEQ. Reach for it when designing, approving, reviewing or describing a "
                     "Linguistics course or its outcomes, single or combined honours. It is not a curriculum and not a regulatory requirement, and "
                     "it names no professional body of its own."),
    summary=("Published by QAA in September 2023 for UK higher education, the statement covers General and Applied Linguistics at "
             "undergraduate honours level. It sets out the subject's context and purposes with four cross-cutting themes (equality, "
             "diversity and inclusion; accessibility; sustainability, tied to the UN Sustainable Development Goals; enterprise and "
             "entrepreneurship education), the distinctive features of courses (design, progression, flexibility, partnership, monitoring "
             "and review), content by levels of linguistic analysis, domains of language use and applied fields, teaching and assessment, "
             "and its benchmark standards. The standards are a threshold rung only (para 4.5, fifteen items) and a list of fifteen generic "
             "skills (para 4.6); typical and excellent performance are referred to Annex D. It names no professional, statutory or "
             "regulatory body beyond PSRBs in general and the Office for Students."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised "
               "standard under the Office for Students' regulatory framework; a key reference point in Wales and Scotland; part of quality "
               "requirements in Northern Ireland (D1, front matter: Relationship to legislation)"),
)

S2 = dict(
    governs='what a graduate in Linguistics (General and Applied) is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject',
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"The purpose of this Statement is to make explicit the context, content, scope and benchmark standards of undergraduate degrees in the subject area of Linguistics, which encompasses the interrelated areas of General and Applied Linguistics." (D1, 1.1)',
    statedSubjects=[
        dict(name='Linguistics', locator='(D1, 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100328', label='linguistics'), dict(scheme='cah', code='CAH19-01-07', label='linguistics')]),
        dict(name='General Linguistics', locator='(D1, 1.1)', kind='specialism', codes=[dict(scheme='hecos', code='100328', label='linguistics')]),
        dict(name='Applied Linguistics', locator='(D1, 1.1; 3.4)', kind='specialism', codes=[dict(scheme='hecos', code='100970', label='applied linguistics')]),
        dict(name='phonetics; phonology', locator='(D1, 3.1; 3.2)', kind='specialism', codes=[dict(scheme='hecos', code='100972', label='phonetics'), dict(scheme='hecos', code='100971', label='phonetics and phonology')]),
        dict(name='sociolinguistics', locator='(D1, 3.3)', kind='specialism', codes=[dict(scheme='hecos', code='101016', label='sociolinguistics')]),
        dict(name='psycholinguistics', locator='(D1, 3.3)', kind='specialism', codes=[dict(scheme='hecos', code='101035', label='psycholinguistics')]),
        dict(name='historical linguistics', locator='(D1, 3.3)', kind='specialism', codes=[dict(scheme='hecos', code='101410', label='historical linguistics')]),
        dict(name='single, joint, combined and major-minor honours', locator='(D1, 2.3; 2.7)', kind='programme title', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of a Linguistics Degree', '2': 'Distinctive features of Linguistics degrees',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context'), ('1.2', '1.6', 'Purposes and characteristics of a Linguistics degree'),
       ('1.7', '1.11', 'Equality, diversity and inclusion'), ('1.12', '1.16', 'Accessibility'),
       ('1.17', '1.21', 'Sustainability'), ('1.22', '1.31', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.3', 'Design'), ('2.4', '2.9', 'Progression'), ('2.10', '2.12', 'Flexibility'),
       ('2.13', '2.18', 'Partnership'), ('2.19', '2.22', 'Monitoring and review'),
       ('3.1', '3.4', 'Content'), ('3.5', '3.7', 'Teaching and learning'), ('3.8', '3.13', 'Assessment'),
       ('4.1', '4.4', 'Benchmark standards'), ('4.5', '4.5', 'Minimum threshold standards'), ('4.6', '4.6', 'Generic skills')]

G = {
    '1.1': 'purpose and coverage: General and Applied Linguistics at undergraduate level',
    '1.2': 'what linguistics studies: structural, cognitive, social, cultural and historical sides of language',
    '1.3': 'systematic, theory-and-data inquiry across sciences, social sciences and humanities',
    '1.4': 'an open, evolving view of the subject rather than fixed boundaries',
    '1.5': 'course diversity and common subject combinations',
    '1.6': 'breadth of current linguistic research and the varied settings of courses',
    '1.7': 'EDI built into curriculum, research, values and assessment',
    '1.8': 'reflexivity and EDI within subject knowledge itself',
    '1.9': 'language, social hierarchy and symbolic power',
    '1.10': 'collaborative learning and diverse students enrich EDI learning',
    '1.11': 'real-life assessment linked to EDI issues',
    '1.12': 'all modes of language; accessible formats and adjustments',
    '1.13': 'professional communication with respect for diversity; active, independent learners',
    '1.14': 'multilingual home backgrounds enrich the classroom',
    '1.15': 'students bring their own linguistic experience to theory',
    '1.16': 'provider awareness of accessibility needs; accessible digital content',
    '1.17': 'linguistics and sustainability: analysing factors behind environmental harm',
    '1.18': 'two principles for engaging with sustainability',
    '1.19': 'links to UNESCO goals SDG4, SDG5, SDG8 and SDG16',
    '1.20': 'discourse analysis applied to climate and environmental questions',
    '1.21': 'documentation and endangered-language work in sustainability dialogue',
    '1.22': 'enterprise education for careers and links with external organisations',
    '1.23': 'entrepreneurship competencies beyond employment',
    '1.24': 'critical, creative and analytical skills that create value',
    '1.25': 'enterprise capabilities, citing the 2018 enterprise guidance',
    '1.26': 'societal impact of linguistic skills; telling employers about them',
    '1.27': 'modules and placements build professional attributes',
    '1.28': 'information technology and data skills',
    '1.29': 'sectors that employ graduates',
    '1.30': 'graduates in data-led and AI-related industries',
    '1.31': 'employability from data analysis and pattern finding',
    '2.1': 'core and optional modules, research training and critical reflection',
    '2.2': 'growing independence; a final independent research project',
    '2.3': 'single honours covers most of section 3; joint routes select from it',
    '2.4': 'no single model of sequential study',
    '2.5': 'progression across levels towards the threshold at FHEQ 6 and FQHEIS 10',
    '2.6': 'signs of progression; readiness for postgraduate study',
    '2.7': 'joint and combined routes reach the core skills and add others',
    '2.8': 'typical duration, exit awards and Scottish four-year honours',
    '2.9': 'micro-credentials as funding changes',
    '2.10': 'flexible entry and clear entry information',
    '2.11': 'flexible content, modes and timing; online provision',
    '2.12': 'resources and training for accessible delivery; uneven access to technology',
    '2.13': 'transferable skills and equal access to partnerships',
    '2.14': 'partnership activities tied to learning outcomes',
    '2.15': 'mobility and exchange across cultures',
    '2.16': 'global outlook even without mobility',
    '2.17': 'partners offering teaching qualifications, as in TESOL',
    '2.18': 'skills employers value; experiential learning',
    '2.19': 'periodic course review against external reference points',
    '2.20': 'external reviewers in periodic review',
    '2.21': 'external examiners and consistency of standards',
    '2.22': 'accreditation of professionally oriented courses',
    '3.1': 'introductory modules across the levels of analysis',
    '3.2': 'six levels of analysis described, phonetics to pragmatics',
    '3.3': 'thirteen domains of language use and development',
    '3.4': 'applied fields from applied to clinical, computational and forensic linguistics',
    '3.5': 'teaching, learning and assessment aligned to aims and stage',
    '3.6': 'course documentation at the outset; varied teaching methods listed',
    '3.7': 'inclusive teaching and a sense of belonging',
    '3.8': 'assessment aligned to aims and stage',
    '3.9': 'what varied assessment methods evaluate',
    '3.10': 'assessment methods listed',
    '3.11': 'balance of knowledge and skills in assessment; SDG themes',
    '3.12': 'clear rationale and criteria for assessment',
    '3.13': 'formative, diagnostic feedback throughout',
    '4.1': 'the standards are the minimum for honours; joint routes use a subset',
    '4.2': 'most students exceed the threshold; Annex D for classification',
    '4.3': 'expected grasp of core areas and the domains of language use',
    '4.4': 'expected knowledge of empirical phenomena and their terminology',
    '4.5': 'threshold rung: fifteen items',
    '4.6': 'fifteen generic skills valued by employers',
}

CTYPE = {'3.1': 'area', '3.2': 'area', '3.3': 'area', '3.4': 'area',
         '3.5': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice',
         '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice'}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2, S7, SB5 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group (and the 2019, 2015, 2007 and 2002 review groups)', kind='other: back matter, read for S7 (edition history)'),
    dict(number='none', heading='Appendix 1: Indicative course titles', kind='other: back matter, read for S2 (course titles)'),
    dict(number='none', heading='Appendix 2: Signposting to other Subject Benchmark Statements', kind='other: back matter, read for S7'),
    dict(number='none', heading='copyright and address line', kind='other: read for S1'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- statements in sections 1 and 2
s('1.13', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students of the subject',
  addressee='learner', verbs=['communicate'], about='professional communication across settings, respecting diversity', domain='generic-skill', award=HON,
  para="Linguistics students work in many settings and are normally expected to grow in their ability to communicate professionally while respecting linguistic, social and cultural diversity; they are also helped to become active, confident and independent learners.",
  prac="Plan for a steady growth in professional communication across the course, set in varied environments, with respect for linguistic, social and cultural difference built in; support students to learn actively and independently and to read their academic setting critically.",
  ben="Over your course you are normally expected to get better at communicating in a professional way, wherever you are working, while showing respect for differences of language, society and culture. You will also be helped to learn actively and on your own, with growing confidence.",
  aaw=f"Present this as a described expectation of growth through the course, not a threshold the award requires: the issuer's wording is 'normally expected', which sits outside must, should and will. Place it at honours level (fheq:6) and cite it as {CITE}, para 1.13. Do not state it as a pass condition; set it beside the threshold item on communicating observations (qaa/linguistics-2023/4.5.b11), the generic skill on communication to audiences (qaa/linguistics-2023/4.6.b3) and the honours descriptor on communication ({F} qaa/fheq-2024/4.15.b8).",
  aad="Raise it when a student or team talks about placements, group work or speaking to people from other language backgrounds. With a student, say plainly that the course expects them to grow in professional communication and in respect for difference; with staff, frame it as a progression the modules should build. Ask: 'Where in your course have you had to communicate with people whose language or culture differs from yours?' and 'What would you do differently next time?' Avoid reading it as a fixed hurdle at a set mark.")

s('1.19.b4', type='expectation', rung='none', force='should', level='none', appliesTo='those who design and deliver education',
  addressee='provider', verbs=['develop'], about='attention to linguistic diversity for inclusive education (SDG4)', domain='none', award='none',
  para="Using, analysing and understanding language underpins empowerment, inclusion and fair access, so language and linguistic diversity should receive particular attention in any effort to make education inclusive for everyone (SDG4, Quality Education).",
  prac="Give language and linguistic diversity deliberate attention when making education inclusive: language use and understanding shape who gains access, inclusion and opportunity, in line with SDG4 (Quality Education).",
  ben=('n/a', 'a principle for those who shape education, not an outcome a student reaches'),
  aaw=f"Treat this as a 'should' addressed to whoever designs or runs education, given within the statement's list of links to the UN Sustainable Development Goals (SDG4). It holds at no single level and binds no student. Cite it as {CITE}, para 1.19 (fourth bullet); do not present it as a regulatory duty. Set it beside the accessibility paragraphs (qaa/linguistics-2023/1.12 to 1.16), the provider expectation on access to technology (qaa/linguistics-2023/2.12) and the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance).",
  aad="Raise it with a programme team discussing inclusive curricula, language support or education for sustainable development. Put it in practitioner terms: inclusive education needs explicit attention to the languages and varieties students bring. Ask: 'Which languages and varieties do your students use, and where does the course recognise them?' Do not hand it to a student as something they must achieve.")

s('1.26', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['articulate', 'demonstrate'], about='explaining and showing skills to employers', domain='generic-skill', award=HON,
  para="The curriculum builds skills with real social reach, such as questioning language ideologies, scrutinising institutional policy, exposing hidden assumptions in discourse and weighing theories against data; graduates are able to explain and show these skills, and other useful personal attributes, to employers.",
  prac="Make the social uses of linguistic skill visible in modules (challenging language ideologies, scrutinising policy, uncovering assumptions in discourse, testing theory against data) and give students practice in naming and evidencing those skills for employers.",
  ben="You will be able to explain to employers, and show them, the skills your study has given you: questioning beliefs about language, examining how institutions use it, spotting hidden assumptions and judging theories against evidence.",
  aaw=f"Present this as an outcome graduates are able to show (force: will) at honours level (fheq:6), within the enterprise and entrepreneurship section. Cite it as {CITE}, para 1.26. Do not claim it guarantees employment or that it is a threshold item; it sits outside the rung list. Set it beside the generic skills (qaa/linguistics-2023/4.6.b13, 4.6.b15), the honours descriptor's qualities for employment ({F} qaa/fheq-2024/4.15.b9.1) and the 2018 enterprise guidance (std:doc:qaa-enterprise-2018-guidance).",
  aad="Raise it when a student prepares a CV, a placement application or an interview, or when staff plan employability work. With a student, use 'you' and ask them to name a skill and the evidence for it. Ask: 'Which piece of your linguistics work shows you questioning an assumption?' and 'How would you explain that to someone outside the subject?' Avoid lecturing on the issuer's list of sectors.")

s('2.5', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on an honours course',
  addressee='learner', verbs=['progress'], about='progression through levels to the honours threshold', domain='none', award=HON,
  para="On an honours degree (FHEQ Level 6; FQHEIS Level 10) students will move from one level of study to the next under each institution's rules, and each level is expected to add knowledge, skills, expertise and experience that lead to meeting the threshold subject skills.",
  prac="Map each level of the course so that it adds knowledge, skills, expertise and experience in steps that lead to the threshold subject skills at the end; progression rules remain the institution's own.",
  ben="You will move up through the levels of your course under your institution's rules, and each year should build what you know and can do until you reach the standard needed for your honours degree.",
  aaw=f"Present this as a 'will' about progression across the levels of an honours course that ends at FHEQ Level 6 (FQHEIS Level 10), as the paragraph itself states. Cite it as {CITE}, para 2.5. Do not claim it sets level-by-level outcomes; the statement gives none below honours. Set it beside the threshold list (qaa/linguistics-2023/4.5.b1 to 4.5.b15), the progression signs in para 2.6 and the reference framework's steps spine:4 to spine:6 (std:ref:uk-framework, R8).",
  aad="Raise it when a student asks how first and second year relate to the final standard, or when a team designs level outcomes. Put it simply: each year builds towards the final threshold. Ask: 'What can you do now that you could not do a year ago?' and 'Which threshold skills still feel furthest away?' Avoid implying the statement fixes what each year must contain.")

s('2.7', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students on combined, joint or major-minor routes',
  addressee='learner', verbs=['achieve', 'add'], about='core subject skills on joint and combined routes', domain='subject-skill', award=HON,
  para="Students on combined, joint or major-minor routes will reach the core parts of the subject's specific and generic skills and will add others that their joint course requires; they may also study where the two subjects overlap.",
  prac="On joint, combined or major-minor routes, secure the core of the subject's specific and generic skills, then let the partner subject's requirements add to them; consider space for interdisciplinary study across the two.",
  ben="If you study linguistics with another subject, you will gain the core linguistics skills, both subject-specific and general, and add others that your other subject asks for. You may also get to explore where the two subjects meet.",
  aaw=f"Present this as a 'will' for joint, combined and major-minor honours (fheq:6): such graduates reach the core of the skills, not every item. Cite it as {CITE}, para 2.7, and read it with para 4.1, which says joint degrees draw on a subset of the standards. Do not claim joint-honours students must meet all fifteen threshold items; set it beside qaa/linguistics-2023/4.5.b1 to 4.5.b15 and qaa/linguistics-2023/4.6.b1 to 4.6.b15.",
  aad="Raise it with joint-honours students or with teams designing combined routes. With a student, explain that they need the core skills of linguistics plus what the other subject adds. Ask: 'Which linguistics skills does your course treat as core for you?' and 'Where do your two subjects meet?' Avoid telling a joint student they are held to the single-honours range.")

s('2.9', type='expectation', rung='none', force='describes', level='none', appliesTo='higher education providers',
  addressee='provider', verbs=['consider'], about='considering standalone micro-credentials', domain='none', award='none',
  para="As funding models change, providers will more and more need to consider standalone micro-credentials that can count towards larger awards; these need to attract students for professional and personal growth and to add to the study of the subject.",
  prac="Consider short standalone credentials that can stack into larger awards, designed so they appeal to learners for professional and personal development and still advance the study of linguistics.",
  ben=('n/a', 'a forecast about provider planning, not something a student achieves'),
  aaw=f"Present this as a forecast about provider planning, worded as a growing necessity ('will increasingly be necessary', 'will need to'), not as a standard on students or a firm obligation. Cite it as {CITE}, para 2.9. Do not claim the statement requires micro-credentials or sets their level; it gives none. Set it beside the flexibility paragraphs (qaa/linguistics-2023/2.10 to 2.12).",
  aad="Raise it only with programme or portfolio teams planning short courses or stackable credit. Frame it as a trend the subject community expects, with two tests: appeal to learners and value to the subject. Ask: 'Would this short course stand on its own for a learner, and would it count towards a degree?' Do not present it to students.")

s('2.12', type='expectation', rung='none', force='must', level='none', appliesTo='providers delivering accessible, inclusive and flexible content',
  addressee='provider', verbs=['recognised'], about='resourcing accessible delivery and uneven access to technology', domain='none', award='none',
  para="Accessible, inclusive and flexible content requires suitable resources and staff training to keep quality consistent, and where courses use digital technology, students' unequal access to it needs to be recognised so that no one is disadvantaged.",
  prac="Resource and train staff for accessible, inclusive and flexible delivery; where you use digital technology, account for students' differing access to devices and connectivity so that none is disadvantaged.",
  ben=('n/a', 'a duty on the provider; the student meets its effect'),
  aaw=f"Present this as a provider necessity ('requires', 'needs to be recognised', recorded as must; the reading is ours and is listed for review), not a student outcome. It holds for delivery at every level and names none. Cite it as {CITE}, para 2.12. Do not claim it is a legal duty; the paragraph cites no law. Set it beside the accessibility paragraphs (qaa/linguistics-2023/1.12 to 1.16) and para 2.11 on flexible delivery.",
  aad="Raise it with a programme team moving teaching or assessment online, or when a student reports trouble getting online. With staff, ask what resources and training the change needs and who might lack devices or connection. Ask: 'Which students would struggle to reach this material, and what is the alternative?' Do not put it to a student as their responsibility.")

s('2.20', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers',
  addressee='provider', verbs=['use', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para="Externality is essential to UK quality assurance: providers will bring external reviewers into periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
  prac="Involve external reviewers in periodic review, asking them to test proposed changes, confirm that threshold standards are met and judge whether content fits the subject.",
  ben=('n/a', 'a duty on the provider in quality assurance'),
  aaw=f"Present this as a provider 'will' in quality assurance: external reviewers take part in periodic review. It applies to the course, not to a level of student achievement. Cite it as {CITE}, para 2.20. Do not claim it is an Office for Students condition; the statement says it is not a regulatory requirement in England. Set it beside para 2.19 on review, para 2.21 on external examiners and the threshold list (qaa/linguistics-2023/4.5.b1 to 4.5.b15).",
  aad="Raise it with programme teams preparing for periodic review or revalidation. Frame it as the place where outside reviewers test changes against the threshold standards. Ask: 'Which threshold items would an external reviewer find hard to trace in your modules?' Do not raise it with students as something they do.")

# ---------------------------------------------------------------- section 4 paragraphs
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers',
  addressee='provider', verbs=['refer'], about='using Annex D to judge achievement above threshold', domain='none', award=HON,
  para="Most students will do clearly better than the minimum threshold; each provider decides what counts as evidence of that and should refer to Annex D, which describes the four honours classifications (1st, 2.1, 2.2 and 3rd) for FHEQ Level 6 and FQHEIS Level 10.",
  prac="Set your own evidence for achievement above the threshold, and use Annex D, which describes each honours class at FHEQ Level 6 (FQHEIS Level 10), when you describe the 1st, 2.1, 2.2 and 3rd.",
  ben=('n/a', 'a duty on the provider; the student-facing account of classes belongs to the provider\'s own criteria'),
  aaw=f"Present this as a provider 'should': refer to Annex D when deciding how achievement above the threshold is evidenced. It concerns the honours award at FHEQ Level 6 and FQHEIS Level 10. Cite it as {CITE}, para 4.2, and Annex D as {F}, Annex D (qaa/fheq-2024/annex-d/...; the 3rd column, such as qaa/fheq-2024/annex-d/summary/r1/3rd, is the threshold). Do not claim the statement itself defines typical or excellent standards; it does not.",
  aad="Raise it with staff writing marking criteria or classification descriptors for linguistics. Frame it as a pointer: the subject sets the floor, Annex D describes the classes above it. Ask: 'How do your criteria for a 2.1 differ from the threshold list?' Avoid telling a student that the threshold list describes a good result.")

s('4.3', type='expectation', rung='none', force='will', level='fheq:6', appliesTo="graduates with a bachelor's degree in the subject",
  addressee='learner', verbs=['have'], about='core areas of analysis and the domains of language', domain='understanding', award=HON,
  para="Graduates will be expected to grasp the basic ideas and analytic methods of the core areas, from phonetics to discourse, a foundation for substantial knowledge of the domains where language systems arise, such as acquisition, variation and change, language in society and language as a cognitive object.",
  prac="Ensure every graduate meets the basic concepts and analytic methods of the core areas (phonetics, phonology, morphology, syntax, semantics, pragmatics and discourse), then builds on them into domains such as acquisition, variation and change, society and cognition.",
  ben="You will be expected to understand the basic ideas and methods of analysis in the core areas of linguistics, such as sounds, word structure, sentence structure, meaning, use in context and discourse, and to use them to learn about how language is acquired, varies, changes, works in society and works in the mind.",
  aaw=f"Present this as a 'will be expected' outcome for honours graduates (fheq:6) that frames the threshold list rather than belonging to it. Cite it as {CITE}, para 4.3. Do not present the named core areas as a compulsory syllabus; para 1.5 says the statement does not set definitive design criteria. Set it beside qaa/linguistics-2023/4.5.b1 and 4.4, and the honours descriptor on systematic understanding ({F} qaa/fheq-2024/4.15.b1).",
  aad="Raise it when a student asks what a linguistics graduate is supposed to know, or when a team checks core module coverage. With a student, list the core areas in plain terms and ask which feel secure. Ask: 'Could you analyse a short sample of data at each level, from sound to discourse?' Avoid reciting the paragraph or treating every area as equally weighted on every course.")

s('4.4', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['have'], about='empirical phenomena, terminology and methods', domain='knowledge', award=HON,
  para="A graduate is expected to know a range of empirical language phenomena and the technical terms and methods used to describe and analyse them; this knowledge may be mainly descriptive but usually rests on a suitable theoretical framework.",
  prac="Expose students to a range of real language phenomena and to the terminology and methods for describing and analysing them, framed by theory even where the work is mostly descriptive.",
  ben="You are expected to know about a range of real language phenomena and the technical terms and methods used to describe and analyse them, usually within a theory that explains them.",
  aaw=f"Present this as a described expectation ('is expected to', outside must, should and will) for honours graduates at fheq:6, not as an item on the threshold list. Cite it as {CITE}, para 4.4. Do not claim it requires a particular theoretical school. Set it beside qaa/linguistics-2023/4.3, the threshold item on knowledge of concepts and methods (qaa/linguistics-2023/4.5.b1) and Annex D's knowledge strand at threshold ({F} qaa/fheq-2024/annex-d/knowledge/r1/3rd).",
  aad="Raise it when a student is unsure whether describing data is enough, or when staff review how theory frames descriptive work. Say plainly that description is fine if it is grounded in a theory. Ask: 'Which theory helps you explain the pattern you described?' Avoid presenting it as a separate hurdle from the threshold list.")

# ---------------------------------------------------------------- 4.5 threshold rung
TH_NOTE = "Most students go well beyond it (para 4.2)."
def t(k, verbs, about, domain, para, prac, ben, what, beside, when, q):
    s('4.5.b%d' % k, type='threshold', rung='threshold', force='threshold', level='fheq:6',
      appliesTo='honours graduates at the threshold', addressee='learner', verbs=verbs, about=about,
      domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=(f"Present this as threshold item {k} of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here {what}. "
           f"Cite it as {CITE}, para 4.5, bullet {k}. "
           f"Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. "
           f"Set it beside {beside} and the reference framework's step spine:6 (std:ref:uk-framework, R8)."),
      aad=(f"Raise it when {when}. "
           f"With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. "
           f"Ask: {q} "
           f"Do not read the list aloud or treat it as the level most students reach. {TH_NOTE}"))

t(1, ['demonstrate'], 'fundamental analytical concepts and methods of inquiry', 'knowledge',
  "Show knowledge of the basic analytic concepts and methods of inquiry that a linguistics degree calls for.",
  "Graduates at threshold show they know the field's basic analytic concepts and its methods of inquiry.",
  "You will show that you know the basic concepts linguists use to analyse language and the main ways they investigate it.",
  'knowledge of the basic analytic concepts and methods of inquiry',
  f"qaa/linguistics-2023/4.3, the honours descriptor on systematic understanding ({F} qaa/fheq-2024/4.15.b1) and Annex D's knowledge strand (qaa/fheq-2024/annex-d/knowledge/r1/3rd)",
  'a student wonders whether they have the basics, or a team audits its introductory modules',
  "'Which analytic concepts do you use without having to look them up?' and 'Which method of inquiry could you explain to a first-year student?'")
t(2, ['take'], 'systematic identification, description and analysis', 'subject-skill',
  "Approach language phenomena systematically: identifying, describing and then analysing them.",
  "Graduates at threshold identify, describe and analyse language phenomena in an orderly, systematic way.",
  "You will be able to work through language data step by step: spotting a feature, describing it and then analysing it.",
  'working systematically from identifying to describing to analysing language phenomena',
  f"qaa/linguistics-2023/4.5.b5 and the honours descriptor on accurate use of established techniques ({F} qaa/fheq-2024/4.15.b2)",
  'a student jumps straight to interpretation, or staff set data-analysis tasks',
  "'What did you notice first, how did you describe it, and only then what did you conclude?'")
t(3, ['ask'], 'well-motivated questions about language', 'subject-skill',
  "Pose well-grounded questions about how language is structured and used.",
  "Graduates at threshold pose well-grounded questions about language structure and use.",
  "You will be able to ask good, well-reasoned questions about how language is built and how people use it.",
  'posing well-grounded questions about language structure and use',
  f"qaa/linguistics-2023/4.5.b6 and the honours descriptor on framing questions ({F} qaa/fheq-2024/4.15.b7)",
  'a student is choosing a project or dissertation topic',
  "'Why is your question worth asking, and what in the data or the literature prompted it?'")
t(4, ['apply'], 'basic data collection, elicitation and transcription', 'subject-skill',
  "Use the basic methods for gathering or eliciting and transcribing data that suit the different branches of linguistics, from corpora and media texts to elicitation, introspection, experiments, questionnaires, interviews and fieldwork.",
  "Graduates at threshold apply basic techniques for collecting or eliciting and transcribing data suited to the sub-disciplines, such as corpora, media and political or advertising texts, elicitation tasks, introspection, laboratory work, questionnaires, interviews or fieldwork.",
  "You will be able to use the basic ways of gathering and transcribing language data that fit your area, such as corpora, media texts, experiments, questionnaires, interviews or fieldwork.",
  'basic techniques for gathering, eliciting and transcribing data',
  f"qaa/linguistics-2023/4.6.b8, the honours descriptor on applying methods ({F} qaa/fheq-2024/4.15.b6) and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r1/3rd)",
  'a student plans data collection or staff design methods training',
  "'Which data-gathering method suits your question, and how will you transcribe what you collect?'")
t(5, ['apply'], 'level-specific analytical concepts applied to data', 'subject-skill',
  "Use the analytic concepts belonging to each level of linguistic analysis on suitable sets of data.",
  "Graduates at threshold apply the analytic concepts of each level of linguistic analysis to suitable data sets.",
  "You will be able to take the concepts for each level of analysis, such as sounds, words or sentences, and use them on real data.",
  'applying the concepts of each level of analysis to suitable data',
  f"qaa/linguistics-2023/4.5.b2 and the honours descriptor on arguing and solving problems ({F} qaa/fheq-2024/4.15.b3.1)",
  'a student meets a new data set or staff write problem sets',
  "'Which level of analysis does this data call for, and which concept would you start with?'")
t(6, ['formulate', 'construct', 'test'], 'generalisations and hypothesis testing', 'subject-skill',
  "Draw linguistic generalisations and build and test hypotheses within linguistics, using fitting evidence.",
  "Graduates at threshold formulate linguistic generalisations and construct and test hypotheses on suitable evidence.",
  "You will be able to draw general patterns from language data and set up and test hypotheses using the right kind of evidence.",
  'forming generalisations and building and testing hypotheses on evidence',
  f"the generic skill on hypotheses (qaa/linguistics-2023/4.6.b1) and the honours descriptor on critical evaluation ({F} qaa/fheq-2024/4.15.b7)",
  'a student moves from describing examples to claiming a pattern',
  "'What would count as evidence against your generalisation, and have you looked for it?'")
t(7, ['evaluate'], 'weighing alternative analyses of data', 'subject-skill',
  "Weigh competing analyses of a data set, understanding how theories shape analysis and decide what counts as evidence.",
  "Graduates at threshold evaluate alternative analyses of a data set, understanding how theory organises analysis and settles what counts as evidence.",
  "You will be able to compare different analyses of the same data and judge between them, knowing how theory shapes analysis and what counts as evidence.",
  'judging between competing analyses of the same data',
  f"qaa/linguistics-2023/4.5.b8, qaa/linguistics-2023/4.6.b6 and the honours descriptor on uncertainty ({F} qaa/fheq-2024/4.15.b4)",
  'two analyses of the same data seem equally plausible to a student',
  "'Which analysis accounts for more of the data, and what does each theory treat as evidence?'")
t(8, ['evaluate'], 'weighing alternative theories', 'understanding',
  "Weigh competing theories, drawing on what linguistic theory is and on what counts as an explanation in linguistics.",
  "Graduates at threshold evaluate alternative theories, grounded in an understanding of linguistic theory and of explanation in the field.",
  "You will be able to compare and judge rival theories, knowing what a linguistic theory is and what makes a good explanation.",
  'judging between rival theories and what counts as an explanation',
  f"qaa/linguistics-2023/4.5.b7, qaa/linguistics-2023/4.6.b2 and the honours descriptor on commenting on research ({F} qaa/fheq-2024/4.15.b3.2)",
  'a student meets two schools of thought on the same question',
  "'What does each theory explain that the other cannot?'")
t(9, ['present'], 'presenting data with discipline conventions', 'subject-skill',
  "Set out linguistic data and analysis with the methods and conventions of each sub-discipline, such as bracketing, tree diagrams, formal logic, graphs, tables, matrices and transcription systems.",
  "Graduates at threshold present data and analysis using each sub-discipline's conventions: bracketing, tree diagrams, formal logic, graphs, tables, matrices and transcription systems.",
  "You will be able to set out your data and analysis using the conventions your area expects, such as tree diagrams, brackets, logic notation, graphs, tables or phonetic transcription.",
  'presenting data and analysis with the conventions of each sub-discipline',
  f"qaa/linguistics-2023/4.6.b3, the honours descriptor on communication ({F} qaa/fheq-2024/4.15.b8) and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r4/3rd)",
  'a student is unsure how to lay out an analysis or staff write assessment guidance',
  "'Which notation does your sub-field expect here, and would a specialist read it without help?'")
t(10, ['utilise', 'address'], 'linguistics applied to real-world problems', 'subject-skill',
  "Bring linguistic terms, theory and research to bear on problems in the world beyond the discipline.",
  "Graduates at threshold use linguistic terminology, theory and research to tackle real-world problems.",
  "You will be able to use linguistic terms, theory and research to help with real problems outside your course.",
  'using linguistic terms, theory and research on real problems',
  f"qaa/linguistics-2023/1.26, the applied fields in para 3.4 and the honours descriptor on applying methods ({F} qaa/fheq-2024/4.15.b6)",
  'a student asks what linguistics is for, or a team plans applied or placement modules',
  "'What problem outside the university could your linguistics help with, and how?'")
t(11, ['understand', 'communicate'], 'language, ideology, power and identity', 'understanding',
  "Grasp, and explain to others, what can be observed about how language represents ideology, power, social identities and realities.",
  "Graduates at threshold understand and communicate observations on how language represents ideology, power, social identity and social reality.",
  "You will understand, and be able to explain, how language can carry ideology and power and shape how identities and social realities are shown.",
  'understanding and explaining how language represents ideology, power and identity',
  f"qaa/linguistics-2023/4.5.b12, para 1.9 and the honours descriptor on communication ({F} qaa/fheq-2024/4.15.b8)",
  'a student analyses media, political or institutional texts',
  "'Whose view does this text take for granted, and which language features show it?'")
t(12, ['analyse'], 'representations of minority groups', 'subject-skill',
  "Analyse how language represents minority groups across regional, sociocultural and situational settings.",
  "Graduates at threshold analyse how language depicts minority groups across regional, sociocultural and situational settings.",
  "You will be able to analyse how language portrays minority groups in different places, cultures and situations.",
  'analysing how language represents minority groups',
  f"qaa/linguistics-2023/4.5.b11, the EDI paragraphs (qaa/linguistics-2023/1.7 to 1.11) and the honours descriptor on critical evaluation ({F} qaa/fheq-2024/4.15.b7)",
  'a student works on representation, discourse or sociolinguistic data',
  "'How do the word choices in this text position the group it describes?'")
t(13, ['identify', 'examine'], 'variation across contexts', 'subject-skill',
  "Find and investigate cases of language variation, and their causes, across situational, social, cultural, regional and historical contexts, including multilingual and cross-cultural ones.",
  "Graduates at threshold identify and examine examples of, and reasons for, variation across situational, social, cultural, regional, historical, multilingual and cross-cultural contexts.",
  "You will be able to spot and look into how and why language varies between situations, social groups, cultures, regions and periods, as well as between languages.",
  'identifying and examining variation and its causes across contexts',
  f"the domains in para 3.3 (sociolinguistics, historical linguistics) and the honours descriptor on systematic understanding ({F} qaa/fheq-2024/4.15.b1)",
  'a student meets dialect, register or language-change data',
  "'What explains this variation: the situation, the speaker's group, the region or the period?'")
t(14, ['evaluate'], "language's role in shaping norms and identities", 'subject-skill',
  "Judge how language helps shape sociocultural norms, identities and realities in public and private domains.",
  "Graduates at threshold evaluate how far language shapes sociocultural norms, identities and realities, in public and in private domains.",
  "You will be able to judge how language helps to shape social norms, identities and realities, in public life and in private.",
  "judging language's part in shaping norms, identities and realities",
  f"qaa/linguistics-2023/4.5.b11 and the honours descriptor on critical evaluation ({F} qaa/fheq-2024/4.15.b7)",
  'a student studies discourse, identity or language attitudes',
  "'How does this way of speaking make some behaviour seem normal, and for whom?'")
t(15, ['show'], 'language and ideology in global and sustainability contexts', 'understanding',
  "Show some grasp of how language use and beliefs about language bear on globalisation, mobility, sustainability and social justice.",
  "Graduates at threshold show some grasp of how language use and language ideologies connect with globalisation, mobility, sustainability and social justice.",
  "You will show some understanding of how language use and beliefs about language connect with globalisation, migration and movement, sustainability and social justice.",
  'some understanding of language and ideology in global and sustainability contexts',
  f"the sustainability paragraphs (qaa/linguistics-2023/1.17 to 1.21), qaa/linguistics-2023/4.6.b13 and the honours descriptor on uncertainty and limits of knowledge ({F} qaa/fheq-2024/4.15.b4)",
  'a student or team links linguistics to sustainability, migration or justice',
  "'Where in your course have you seen language tied to global movement or environmental debate?'")

# ---------------------------------------------------------------- 4.6 generic skills (outcome list, no modal)
def gs(k, verbs, about, strand, para, prac, ben, beside, when, q):
    s('4.6.b%d' % k, type='outcome', rung='none', force='describes', forceFrom='4.6', level='fheq:6',
      appliesTo='students of the subject', addressee='learner', verbs=verbs, about=about,
      domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
      aaw=(f"Present this as generic skill {k} of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. "
           f"It refines the honours level (fheq:6) in the {strand} strand (std:ref:uk-framework, R3). "
           f"Cite it as {CITE}, para 4.6, bullet {k}, and do not claim every graduate must show it at a set standard. "
           f"Set it beside {beside}."),
      aad=(f"Raise it when {when}. "
           f"With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. "
           f"Ask: {q} "
           f"Avoid presenting it as a pass requirement."))

gs(1, [], 'forming and testing hypotheses', 'strand:thinking',
   "Forming hypotheses and testing them.",
   "Give students practice in forming hypotheses and testing them.",
   "You will have the chance to practise forming hypotheses and testing them, a skill employers value.",
   f"the threshold item qaa/linguistics-2023/4.5.b6 and the honours descriptor on framing questions ({F} qaa/fheq-2024/4.15.b7)",
   'a student describes their project to an employer', "'Can you give an example of a hunch you turned into a testable claim?'")
gs(2, ['assessing'], 'weighing contrasting theories', 'strand:thinking',
   "Judging the strengths of competing theories and explanations.",
   "Develop students' ability to weigh the merits of contrasting theories and explanations.",
   "You will build your ability to weigh up competing theories and explanations, which employers value.",
   f"qaa/linguistics-2023/4.5.b8 and qaa/linguistics-2023/4.6.b6 (close in wording; listed in Part E)",
   'a student must choose between explanations in an essay', "'What makes one explanation stronger than the other here?'")
gs(3, [], 'communication suited to the audience', 'strand:communication',
   "Communicating in spoken, non-verbal and graphic forms, in a format that suits the audience.",
   "Give practice in spoken, non-verbal and graphic communication, choosing the format for the audience.",
   "You will practise communicating in speech, in other non-verbal ways and with visuals, choosing a format that suits your audience.",
   f"qaa/linguistics-2023/4.5.b9, the honours descriptor on communication ({F} qaa/fheq-2024/4.15.b8) and Annex D's transferable strand (qaa/fheq-2024/annex-d/transferable/r1/3rd)",
   'a student prepares a presentation or poster', "'Who is your audience, and why did you choose this format for them?'")
gs(4, [], 'research and experimental design, alone and in groups', 'strand:application',
   "Designing experiments and designing and carrying out research projects, alone and in groups.",
   "Build experimental design and the design and conduct of research projects, both individual and group, into the course.",
   "You will learn to design experiments and to plan and carry out research projects, on your own and with others.",
   f"qaa/linguistics-2023/4.5.b4, the honours descriptor on applying methods ({F} qaa/fheq-2024/4.15.b6) and Annex D on group work (qaa/fheq-2024/annex-d/transferable/r2/3rd)",
   'a student plans a group or individual project', "'What part of the design did you shape yourself, and what did the group decide together?'")
gs(5, ['understanding'], 'ethical and appropriate use of evidence', 'strand:application',
   "Knowing how to use evidence and data properly and ethically.",
   "Teach the proper and ethical use of evidence and data, including in students' own research.",
   "You will come to understand how to use evidence and data properly and ethically.",
   f"qaa/linguistics-2023/4.6.b14 and the honours descriptor on decisions in complex contexts ({F} qaa/fheq-2024/4.15.b9.2)",
   'a student collects data from people or handles sensitive material', "'What consent and care does this data need, and how will you store and cite it?'")
gs(6, ['evaluating'], 'weighing theories, explanations and evidence', 'strand:thinking',
   "Judging the merits of contrasting theories and explanations and of the evidence for them.",
   "Develop students' judgement of contrasting theories, explanations and the evidence behind them.",
   "You will build your ability to judge competing theories and explanations, and the evidence behind each.",
   f"qaa/linguistics-2023/4.6.b2 (close in wording; Part E), qaa/linguistics-2023/4.5.b7 and the honours descriptor on critical evaluation ({F} qaa/fheq-2024/4.15.b7)",
   'a student reviews literature with conflicting findings', "'Which evidence would change your mind about this theory?'")
gs(7, ['distinguishing'], 'telling descriptive systems apart from data', 'strand:thinking',
   "Keeping apart a system of description and the data it is used to describe.",
   "Help students separate descriptive frameworks from the data they describe.",
   "You will learn to tell the difference between a system for describing language and the language data itself.",
   f"qaa/linguistics-2023/4.4 and the honours descriptor on arguing with established ideas ({F} qaa/fheq-2024/4.15.b3.1)",
   'a student confuses a category label with what speakers actually do', "'Is that a fact about the data or about the way we chose to describe it?'")
gs(8, ['abstracting', 'synthesising', 'collecting', 'analysing', 'manipulating'], 'handling information and data of many kinds', 'strand:application',
   "Abstracting and combining information, and gathering, analysing and working with varied kinds of data.",
   "Give students practice in abstracting and synthesising information and in collecting, analysing and manipulating varied data.",
   "You will practise drawing out and combining information and gathering, analysing and working with many kinds of data.",
   f"qaa/linguistics-2023/4.5.b4, qaa/linguistics-2023/1.28 and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r4/3rd)",
   'a student describes data work to an employer', "'What kinds of data have you handled, and what did you do with each?'")
gs(9, ['interpreting'], 'reading diagrams, tables and graphs', 'strand:thinking',
   "Making sense of information shown in diagrams, tables and graphs.",
   "Build students' skill in interpreting diagrams, tables and graphs.",
   "You will build your skill in reading and making sense of diagrams, tables and graphs.",
   f"qaa/linguistics-2023/4.5.b9 and Annex D's transferable strand on numeracy (qaa/fheq-2024/annex-d/transferable/r1/3rd)",
   'a student meets quantitative results in a paper', "'What does this graph show, and what does it leave out?'")
gs(10, ['searching', 'synthesising', 'giving'], 'finding and combining sources with proper acknowledgement', 'strand:application',
   "Tracking down and combining information from varied formats, with proper acknowledgement and source lists.",
   "Teach students to search for and synthesise information in many formats and to acknowledge and list their sources properly.",
   "You will learn to find and combine information from many kinds of source and to credit and list your sources properly.",
   f"the honours descriptor on managing learning from scholarly and primary sources ({F} qaa/fheq-2024/4.15.b5)",
   'a student starts a literature search or asks about referencing', "'Where did you look, and how will a reader find each source you used?'")
gs(11, ['undertaking'], 'competent self-directed study', 'strand:autonomy',
   "Carrying out competent study and learning under one's own direction.",
   "Develop students' capacity for competent self-directed study.",
   "You will build your ability to study and learn well on your own.",
   f"the honours descriptors on managing own learning ({F} qaa/fheq-2024/4.15.b5, 4.15.b9.3) and Annex D (qaa/fheq-2024/annex-d/transferable/r3/3rd)",
   'a student struggles to plan independent study', "'How do you decide what to study next when no one sets it?'")
gs(12, ['understanding'], 'health and safety and EDI at work', 'strand:autonomy',
   "Grasping why health and safety, and equality, diversity and inclusiveness, matter in the workplace.",
   "Make sure students learn why health and safety and equality, diversity and inclusiveness matter at work.",
   "You will come to understand why health and safety, and equality, diversity and inclusion, matter in a workplace.",
   f"the EDI paragraphs (qaa/linguistics-2023/1.7 to 1.11) and the honours descriptor on personal responsibility ({F} qaa/fheq-2024/4.15.b9.1)",
   'a student prepares for a placement, lab work or fieldwork', "'What risks and inclusion questions does this setting raise for you and others?'")
gs(13, ['appreciating', 'engaging'], 'current debates: sustainability, employability, decolonisation', 'strand:thinking',
   "Valuing and taking part in current debates on sustainability, employability and global perspectives, decolonisation and anti-racism among them.",
   "Give students room to engage with live debates on sustainability, employability and global outlooks, decolonisation and anti-racism among them.",
   "You will have the chance to take part in current debates about sustainability, careers and global perspectives, including decolonisation and anti-racism.",
   f"qaa/linguistics-2023/4.5.b15, the sustainability paragraphs (qaa/linguistics-2023/1.17 to 1.21) and std:doc:qaa-advancehe-esd-2021-guidance",
   'a student or team discusses decolonising the curriculum or sustainability', "'Which current debate does your own linguistics work speak to?'")
gs(14, ['appreciating', 'act', 'display'], 'sustainable and ethical conduct', 'strand:autonomy',
   "Seeing the need to act sustainably and to behave and conduct oneself ethically.",
   "Help students see why sustainable action and ethical conduct matter, and give them chances to practise both.",
   "You will come to see why acting sustainably and behaving ethically matter, and practise both.",
   f"qaa/linguistics-2023/4.6.b5 and the honours descriptor on personal responsibility ({F} qaa/fheq-2024/4.15.b9.1)",
   'a student plans fieldwork, data use or a placement', "'What would acting sustainably and ethically look like in this project?'")
gs(15, ['communicating'], 'communicating language knowledge to policy stakeholders', 'strand:communication',
   "Conveying knowledge about language with authority and sensitivity to those responsible for policies where language matters.",
   "Give students practice in communicating subject knowledge with authority and sensitivity to policy stakeholders for whom language is central.",
   "You will practise explaining what you know about language, clearly and sensitively, to people who make policies where language matters.",
   f"qaa/linguistics-2023/4.5.b10, the language planning and policy field in para 3.4 and the honours descriptor on communication ({F} qaa/fheq-2024/4.15.b8)",
   'a student works on language policy, education or public engagement', "'How would you explain this finding to someone writing a language policy?'")

# 4.5.b9: the skeleton span stops at the page break; the item runs on after the page number "18".
P['4.5.b9']['find'] = ("present linguistic data and analysis using the appropriate methods and conventions specific to each sub-discipline of Linguistics, "
                       "including bracketing, tree diagrams,\n\n18\nformal logic, graphs, tables, matrices and specific transcription systems")

GRADE = {}
TH = {'1.13': 'theme:accessibility', '1.19.b4': 'theme:esd', '1.26': 'theme:enterprise'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.5; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.5; 4.2'),
            dict(id='cqfw:6', role='inferred', locator='std:doc:qaa-fheq-2024-framework 2.24 (CQFW levels 4 to 8 compare with the FHEQ); the statement names Wales but not the CQFW'),
            dict(id='spine:6', role='inferred', locator='std:ref:uk-framework R2 (step 6: FHEQ 6, SCQF 10 for honours)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.5: "(FHEQ Level 6; FQHEIS Level 10)"; 4.2)'),
                dict(**{'from': 'fheq:6'}, to='cqfw:6', relation='compares-with', basis='inferred from std:doc:qaa-fheq-2024-framework 2.24 (Part E)'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='equivalent', basis='inferred from std:ref:uk-framework R2 (Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.7', '1.8', '1.9', '1.10', '1.11', '2.13', '3.7', '3.11', '4.6']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '2.11', '2.12']),
      dict(id='theme:esd', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '3.11', '4.5', '4.6']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '4.6'])]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-linguistics-2019-benchmarks (not yet ingested)', note='front matter names key changes from the previous statement; the back matter dates the fourth edition 2019'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2); above-threshold performance is left to it'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Level 6 (2.5; 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Level 10 (2.5; 4.2)'),
    dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='cited as QAA 2018 (1.25) and in the reference list'),
    dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='in the reference list only'),
    dict(rel='refersTo', target='QAA UK Quality Code for Higher Education (2019), Advice and Guidance (not yet ingested)', note='front matter; reference list'),
    dict(rel='refersTo', target="QAA's Glossary (not ingested)", note='front matter: explains unfamiliar terms'),
    dict(rel='cites', target='UNESCO Sustainable Development Goals (not a standards document; not ingested)', note='1.19; 3.11 (the UN SDGs); reference list'),
    dict(rel='readWith', target='the 16 Subject Benchmark Statements in Appendix 2 (anthropology to Welsh), each std:doc:qaa-<subject>-<year>-benchmarks', note='Appendix 2: related statements'),
]

SB1 = [
    "The study of the human capacity for language in every mode, spoken, signed and written: its structure, its processing in the mind and brain, and how it is acquired, used, interpreted and changes in social, cultural and historical settings (D1, 1.2).",
    "Its guiding principle is that linguistic behaviour can be explained by systematic study, with theoretical models tested against empirical data, by both cognitive and social approaches (D1, 1.3).",
    "Broad and interdisciplinary, spanning the sciences, social sciences and humanities; the statement keeps the subject's boundaries deliberately open and evolving (D1, 1.3, 1.4, 1.6).",
    "Taught through levels of analysis (phonetics, phonology, morphology, syntax, semantics, pragmatics) applied to domains of language use and to applied fields such as clinical, computational and forensic linguistics, language teaching and lexicography (D1, 3.1 to 3.4).",
    "Reflexive and socially engaged: students examine their own linguistic identities and attitudes, and the subject studies language, power and social hierarchy and works in partnership with communities (D1, 1.8, 1.9).",
    "Commonly studied in combination, with English, TESOL, other languages, psychology, philosophy, politics and many more; single honours covers most of the content, joint routes a selection (D1, 1.5, 2.3, 2.7).",
]

SB2 = [
    dict(theme='theme:edi', inThisSubject="EDI sits inside the subject knowledge itself: comparative study of unrelated, often non-European languages, attention to vernaculars, minority languages and representation, reflexivity about one's own language attitudes, and research done with communities; assessment linked to real-life EDI issues (D1, 1.7 to 1.11); threshold items on ideology, power and minority groups and a generic skill on EDI at work (D1, 4.5, 4.6)",
         statements=['4.5.b11', '4.5.b12', '4.6.b12']),
    dict(theme='theme:accessibility', inThisSubject="an inclusive view of all modes of language, sign included; accessible formats and reasonable adjustments; multilingual home backgrounds as a resource; provider awareness of disabled students' needs and accessible digital content (D1, 1.12 to 1.16); resourcing accessible delivery and uneven access to technology (D1, 2.11, 2.12)",
         statements=['1.13', '2.12']),
    dict(theme='theme:esd', inThisSubject="headed Sustainability: language as central to articulating sustainable futures; links to UNESCO's goals SDG4, SDG5, SDG8 and SDG16; discourse analysis of climate communication; endangered-language and documentation work opening space for other knowledges (D1, 1.17 to 1.21); SDG themes in assessment (D1, 3.11); a threshold item and two generic skills (D1, 4.5, 4.6)",
         statements=['1.19.b4', '4.5.b15', '4.6.b13', '4.6.b14']),
    dict(theme='theme:enterprise', inThisSubject="enterprise and entrepreneurship education for careers and wider social value, placements and external links; the subject's critical, creative and analytical mix; IT and data skills; graduates sought in publishing, technology, AI, teaching, therapy, data science and more (D1, 1.22 to 1.31); employability among the debates in the generic skills (D1, 4.6)",
         statements=['1.26', '4.6.b13']),
]

SB3 = dict(
    areas=[dict(component='3.1', gloss='introductory study across the core levels of linguistic analysis'),
           dict(component='3.2', gloss='levels of analysis: phonetics, phonology, morphology, syntax, semantics, pragmatics'),
           dict(component='3.3', gloss='domains of language use and development: acquisition, historical, evolutionary, typological, socio-, psycho- and neurolinguistics, history and philosophy of language, corpus, discourse, stylistics, educational linguistics'),
           dict(component='3.4', gloss='applied fields: applied, clinical, computational and forensic linguistics; translation and interpreting; language teaching and TESOL; language planning and policy; lexicography')],
    practices=[dict(component='3.5', kind='teaching', gloss='methods aligned to aims and to the stage of progression'),
               dict(component='3.6', kind='teaching', gloss='lectures, seminars, practicals and lab work, research-methods workshops, tutorials, group study, projects, data exercises, specialist software, placements, VLEs'),
               dict(component='3.7', kind='learning', gloss='inclusive learning environment, belonging and engagement'),
               dict(component='3.8', kind='assessment', gloss='assessment aligned to aims and stage; formative and summative'),
               dict(component='3.9', kind='assessment', gloss='what assessment should be able to evaluate, from analysis of linguistic systems to applying language-learning principles'),
               dict(component='3.10', kind='assessment', gloss='essays, projects, examinations, presentations, problem sets, data work, materials design, lab work, portfolios, reviews, online resources, peer and self-evaluation, skills tasks'),
               dict(component='3.11', kind='assessment', gloss='balancing knowledge and skills; inclusivity and the SDGs in assessment themes'),
               dict(component='3.12', kind='assessment', gloss='clear rationale and explicit criteria'),
               dict(component='3.13', kind='assessment', gloss='formative and diagnostic feedback throughout')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=15)],
    rungBases="threshold only: 4.5 defines the threshold as the minimally acceptable attainment of an honours graduate; 4.2 says most students do much better and refers providers to Annex D (std:doc:qaa-fheq-2024-framework) for the classes above it. No typical or excellent rung.",
    outcomeLists=[dict(leadIn='4.6', gloss='generic skills of value to employers (an opportunity to develop, no modal)', items=15, award=['honours'])],
    outcomes=[])

SB4A_FULL = []

SB5 = [
    dict(body='professional, statutory and regulatory bodies (PSRBs), none named', says='the statement supports PSRBs on the academic standards expected of students; providers may weigh PSRB requirements; courses with professional or vocational outcomes may need their evaluation and accreditation (D1, front matter, 2.22)', requirements='not-applicable: no body named'),
    dict(body='Office for Students', says="in England the statement is not a sector-recognised standard under the OfS regulatory framework (D1, front matter)", requirements='not yet ingested (Part E)'),
]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.7', '1.8', '1.9', '1.10', '1.11', '2.13', '3.7', '3.11', '4.6'], statements=['4.5.b11', '4.5.b12', '4.6.b12']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '2.11', '2.12'], statements=['1.13', '2.12']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '3.11', '4.5', '4.6'], statements=['1.19.b4', '4.5.b15', '4.6.b13', '4.6.b14']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '4.6'], statements=['1.26', '4.6.b13'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.5', '4.2']),
                dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.5', '4.2'])],
    bodies=[dict(body='professional, statutory and regulatory bodies (PSRBs), generic', citedIn=['front matter', '2.22']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd); the only account of achievement above the threshold'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA 2018 (Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers)', citedIn=['1.25', 'back matter'], role='source of the enterprise capabilities listed in 1.25'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE (2021) Education for Sustainable Development Guidance', citedIn=['back matter'], role='further reading for the sustainability theme'),
        dict(document='QAA UK Quality Code for Higher Education and its Advice and Guidance (not yet ingested: Part E)', named='The UK Quality Code for Higher Education; Advice and Guidance', citedIn=['front matter', 'back matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document="QAA Glossary (not ingested: Part E)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UNESCO Sustainable Development Goals (not a QAA document; not ingested)', named="UNESCO's education for sustainable development goals; United Nations Sustainable Development Goals", citedIn=['1.19', '3.11', 'back matter'], role='frames the sustainability theme (SDG4, SDG5, SDG8, SDG16 in 1.19; five goals named in 3.11)')])

B1 = [
    dict(slug='threshold-standard', definition='the least level of attainment acceptable for an honours graduate in the subject (D1, 4.5)', beneficiaryDefinition='the minimum you need to reach to gain your honours degree', scopeNote='the only rung this statement gives', category='unknown', practices=['education']),
    dict(slug='levels-of-linguistic-analysis', definition='the tiers at which language is analysed, from speech sounds through word structure and sentence structure to meaning and use in context (D1, 3.1, 3.2)', beneficiaryDefinition='the layers at which you study language, from sounds up to meaning and use', scopeNote='phonetics, phonology, morphology, syntax, semantics, pragmatics', category='unknown', practices=['education']),
    dict(slug='applied-linguistics', definition='study of practical, real-world problems that involve language, drawing on linguistics and neighbouring disciplines and working with those affected (D1, 3.4)', beneficiaryDefinition='using linguistics to help solve real problems involving language', scopeNote='one of the two areas the statement covers (1.1)', category='unknown', practices=['education']),
    dict(slug='psrb', definition='a professional, statutory or regulatory body (D1, front matter)', beneficiaryDefinition='an organisation that sets or checks standards for a profession', scopeNote='none is named in this statement', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='threshold-standard', form='threshold standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
    dict(concept='levels-of-linguistic-analysis', form='levels of linguistic analysis', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='applied-linguistics', form='Applied linguistics', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='psrb', form='professional, statutory and regulatory bodies (PSRBs)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [
    dict(source='QAA Subject Benchmark Statement Linguistics, 2019 (fourth edition)', why='to confirm the supersedes link and compare the standards'),
    dict(source='QAA UK Quality Code for Higher Education (2019) and Advice and Guidance', why='cited in the front matter and reference list; not yet ingested'),
]

E = [
    'Rungs: threshold only (4.5, 15 items). No typical or excellent rung; 4.2 says most students exceed the threshold and refers providers to Annex D (as Archaeology, run 0085). Pattern differs from Psychology.',
    'Threshold lead-in wording: "students should be able to acquire a range of subject-specific and generic skills including:" (4.5). Force recorded as threshold because 4.5 defines the rung as the minimally acceptable attainment; the lead-in modal is "should be able to", not Psychology\'s "will". For P3.',
    'The threshold lead-in names both subject-specific and generic skills, but its fifteen items are mostly subject-specific; the separate generic skills list (4.6) has no rung and no modal ("offer students the opportunity to develop"). Recorded as an outcome list with force describes, rung none, domain generic-skill, level fheq:6. P3: whether 4.6 should count as part of the threshold through 4.5\'s "generic skills".',
    '4.6.b2 ("assessing the merits of contrasting theories and explanations") and 4.6.b6 ("evaluating the merits of contrasting theories, explanations and evidence") nearly repeat each other; both kept as the issuer gives them.',
    'Skeleton correction: 4.5.b9 ran only to the page break ("tree diagrams,"); recut with find to include its continuation after the page number, so its source holds the stray page number "18".',
    'Skeleton correction: the theme hits were one paragraph early, because each sub-heading line falls at the end of the paragraph before it (for example "Equality, diversity and inclusion" sits in 1.6). Themes placed by sub-heading: EDI 1.7 to 1.11, accessibility 1.12 to 1.16, sustainability 1.17 to 1.21, enterprise 1.22 to 1.31; and 4.5 and 4.6 placed under their own sub-headings.',
    'Skeleton candidates not taken as statements: 1.18.b1 and b2 and 1.19.b1 to b3 (descriptive principles and SDG links); 3.2, 3.3, 3.6, 3.9 and 3.10 list items (content areas, teaching and assessment methods: components, not standards).',
    'Obliging words outside the five: 1.13 "are normally expected to" (describes); 4.4 "is expected to" (describes); 2.9 "will increasingly be necessary" and "will need to" (a forecast; describes); 2.12 "requires" and "needs to be recognised" (recorded as must). For Abbott.',
    '4.3 "will be expected to" recorded as will; it frames the threshold list and is not itself a rung item (rung none).',
    'Plain-present provider norms, not recorded as statements (template open point 5): 1.16 (providers aware of accessibility needs; accessible formats); 2.3 (honours courses have an introductory module); 2.10 (institutions provide entry information); 2.13 (institutions ensure equal access to partnerships); 3.5, 3.6 (documentation at the outset), 3.7, 3.8, 3.12 and 3.13 (assessment practice). For P3.',
    'Plain-present student outcomes not recorded: 1.24 ("students develop capabilities that make them ... able to"), 1.28 (IT and data skills gained), 2.6 (a second-class graduate is capable of postgraduate study). For P3.',
    '2.21 (external examiners "will be asked", "will consider") read as a description of the external examining system, not a standard; 2.2 and 2.22 use "may" and are not statements.',
    'Inferred code: hecos 100971 phonetics and phonology (the text names phonetics and phonology separately, 3.2). The CAH parent of CAH19-01-07 is CAH19-01 English studies, not added. Other fields named (translation, lexicography, forensic, clinical, computational linguistics) are applied areas, not given codes.',
    'Inferred levels and crosswalks: cqfw:6 (from std:doc:qaa-fheq-2024-framework 2.24; the statement names Wales but not the CQFW) and spine:6 (std:ref:uk-framework R2). The FHEQ 6 to FQHEIS 10 equivalence is stated (2.5).',
    'Generic skills levels: each 4.6 item is set at fheq:6 as the honours level it refines; the statement gives no level per skill. Inferred.',
    'Series: the 2023 statement as the fifth edition is inferred from the back matter (fourth edition 2019; third 2015; earlier 2007 and 2002). Supersedes 2019 by the same reading.',
    'Bodies: none named as a PSRB. Bodies named only in the excluded membership lists (Linguistics Association of Great Britain, British Association for Applied Linguistics, British Council, Chartered College of Teaching, University Council for Modern Languages, International Clinical Phonetics and Linguistics Association) and UCAS (Appendix 1) are not recorded in SB5. Speech and Language Therapy is named as a profession (1.29, 3.4) with no regulator named.',
    'Office for Students: requirements not yet ingested.',
    'SB6 documents not ingested: the Quality Code and Advice and Guidance, QAA Glossary, UNESCO and UN SDGs.',
    'TH tags only statements inside a theme\'s own paragraphs (1.13, 1.19.b4, 1.26); SB6 also lists the threshold and generic items that name a theme (4.5.b11, 4.5.b12, 4.5.b15, 4.6.b12 to 4.6.b14). 4.5.b11 and 4.5.b12 under EDI are our reading (ideology, power, minority groups; the item does not use the theme name).',
    'Different from Psychology: no master\'s award; threshold only; a separate unmoded generic skills list; Appendix 1 (course titles) and Appendix 2 (related statements); the enterprise section is long (1.22 to 1.31) and includes graduate sectors.',
    'Agent instructions (aaw, aad) set each standard beside FHEQ 4.15 descriptor ids, Annex D threshold cells and std:ref:uk-framework spine and strand ids; the strand for each 4.6 skill is our assignment.',
]
