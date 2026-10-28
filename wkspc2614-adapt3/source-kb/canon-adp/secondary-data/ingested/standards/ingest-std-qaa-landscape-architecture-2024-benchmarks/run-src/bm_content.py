# bm_content.py: run 0114, QAA Subject Benchmark Statement: Landscape Architecture (April 2024), std run agent.
# Judgement file for tools/bm_build.py (brief BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Written fresh from the held text alone (benchmark rule 6). Every text field below is our own words.

HON = "bachelor's with honours"
MA = "master's"
CITE = 'QAA, 2024, Landscape Architecture Subject Benchmark Statement, para %s'

META = dict(
    run='0114', p1='2026-10-03 17:44',
    title='Subject Benchmark Statement: Landscape Architecture',
    heading='Subject Benchmark Statement: Landscape Architecture (QAA, April 2024)',
    edition='April 2024 (fifth edition)', published='2024-04',
    status='current', supersedes='Subject Benchmark Statement: Landscape Architecture, fourth edition (2019), as the advisory group list states',
    subjects=[dict(scheme='hecos', code='100124', label='landscape architecture and design', basis='inferred'),
              dict(scheme='cah', code='CAH13-01-03', label='landscape design', basis='inferred'),
              dict(scheme='hecos', code='100588', label='landscape studies', basis='inferred')],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2024 revision with cross-cutting themes (fifth edition of this statement)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=('This document records what the QAA expects a graduate in landscape architecture to know, understand and be able to do, '
                     'chiefly at honours level, with a short list of further expectations for master\'s graduates. Use it to find a threshold, '
                     'typical or excellent standard by id, to see how the four cross-cutting themes and generative AI show in the subject, '
                     'and to trace the Landscape Institute\'s accreditation context. It is a sector reference point, not a regulation; each '
                     'statement is cited by the issuer\'s paragraph number and set beside the FHEQ, FQHEIS and Annex D records it sits at.'),
    summary=('Landscape architecture studies, plans, designs, manages and conserves landscapes of every type and scale, drawing on the arts, '
             'humanities and the natural and social sciences. The statement covers honours degrees (FHEQ level 6, FQHEIS level 10) and adds '
             'a threshold list for master\'s graduates (level 7, FQHEIS 11). It states three rungs for honours: a long threshold list of 56 '
             'items in seven skill groups (intellectual; analytical and data interpretation; practical; self-management and professional '
             'development; digital literacy; communication; interpersonal and teamwork), and three items each for typical and excellent '
             'that build on the whole threshold list. Its themes are equality, diversity and inclusion, accessibility, sustainability and '
             'employability, enterprise and entrepreneurship, with generative AI treated in assessment and in the digital skills. The '
             'Landscape Institute accredits courses and sets the competency framework; IFLA sets international principles.'),
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point for academic standards in Wales and Scotland, not a sector-recognised standard in England (D1, front matter)')

S2 = dict(
    governs='the academic standards and the scope of honours degrees in landscape architecture in the UK, with expectations for master\'s graduates',
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"This Subject Benchmark Statement aims to clarify the scope and standards of degree courses in Landscape Architecture." (D1, 1.1)',
    statedSubjects=[
        dict(name='Landscape Architecture', locator='(D1, 1.1; 1.2)', kind='subject',
             codes=[dict(scheme='hecos', code='100124', label='landscape architecture and design'), dict(scheme='cah', code='CAH13-01-03', label='landscape design')]),
        dict(name='Landscape Architecture with Planning (dual honours)', locator='(D1, 3.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100124', label='landscape architecture and design'), dict(scheme='hecos', code='100197', label='planning')]),
        dict(name='Planning, Urban Design or Ecology (subjects a course may be offered with)', locator='(D1, 2.22)', kind='subject',
             codes=[dict(scheme='hecos', code='100197', label='planning'), dict(scheme='hecos', code='100347', label='ecology')]),
        dict(name='landscape planning, management, ecology and science (practitioner specialisms)', locator='(D1, 1.10; 2.5)', kind='specialism',
             codes=[dict(scheme='hecos', code='100588', label='landscape studies'), dict(scheme='hecos', code='100864', label='ecosystem ecology and land use')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Landscape Architecture degree', '2': 'Distinctive features of Landscape Architecture courses',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.8', 'Context and purposes of a Landscape Architecture degree'),
       ('1.9', '1.9', 'The professional body context'),
       ('1.10', '1.18', 'The professional body context: The Landscape Institute'),
       ('1.19', '1.19', 'The professional body context: The International Federation of Landscape Architects (IFLA)'),
       ('1.20', '1.22', 'Key points in relation to the cross-cutting themes'),
       ('1.23', '1.24', 'Equality, diversity and inclusion (EDI)'),
       ('1.25', '1.25', 'Accessibility'),
       ('1.26', '1.26', 'Sustainability'),
       ('1.27', '1.27', 'Employability, enterprise and entrepreneurship education'),
       ('2.1', '2.2', 'Distinctive features of Landscape Architecture courses'),
       ('2.3', '2.9', 'Professional accreditation'),
       ('2.10', '2.10', 'Course design'),
       ('2.11', '2.16', 'Progression'),
       ('2.17', '2.19', 'Alternative routes'),
       ('2.20', '2.21', 'Flexibility'),
       ('2.22', '2.22', 'Partnerships'),
       ('2.23', '2.24', 'Apprenticeships'),
       ('2.25', '2.25', 'Monitoring and review: Internal'),
       ('2.26', '2.27', 'Monitoring and review: Externality'),
       ('2.28', '2.28', 'Monitoring and review: Professional review'),
       ('3.1', '3.1', 'Content, structure and delivery'),
       ('3.2', '3.2', 'Core areas common to all Landscape Architecture courses'),
       ('3.3', '3.7', 'Teaching and learning'),
       ('3.8', '3.14', 'Assessment'),
       ('4.1', '4.3', 'Introduction'),
       ('4.4', '4.4', 'Threshold level: Subject knowledge, understanding and skills'),
       ('4.5', '4.5', 'Typical standard'),
       ('4.6', '4.6', 'Excellent standard'),
       ('4.7', '4.7', "Master's degrees")]

G = {
    '1.1': 'the aim: scope and standards of degree courses',
    '1.2': 'a profession and an academic subject drawing on many fields',
    '1.3': 'what research and scholarship in the subject seek to understand',
    '1.4': 'the work the discipline does, at every scale; policy role through the LI',
    '1.5': 'how practitioners change places, from city parks to national infrastructure; the 2019 DEFRA review quoted',
    '1.6': 'a place-focused discipline: three sensitivities (natural systems, cultural identity, global and local decisions)',
    '1.7': 'leading green infrastructure, with five kinds of place it aims to create',
    '1.8': 'contributing to policy on protected landscapes',
    '1.9': 'two professional bodies: IFLA internationally, the LI in the UK',
    '1.10': 'the LI as the chartered body and whom it represents',
    '1.11': 'LI members follow its code of practice, tied to IFLA ethical principles',
    '1.12': 'the LI accredits courses; its report on the core activities of the profession',
    '1.13': 'the four cross-cutting themes of this edition',
    '1.14': 'the themes complement each other and the statement',
    '1.15': 'the LI competency framework covers all four themes, with four example competencies',
    '1.16': 'employability and enterprise implicit in the competency framework',
    '1.17': 'the code of practice repeated with the theme context',
    '1.18': 'two LI steps on EDI: a built-environment memorandum and a landscape-sector declaration',
    '1.19': 'IFLA, its role in education and the IFLA/UNESCO charter definition',
    '1.20': 'providers already bear legal duties on the themes and sector targets',
    '1.21': 'section 4 names the standards; the theme expectations are set out here',
    '1.22': 'three features of projects and briefs that serve all the themes',
    '1.23': 'inclusive curricula and pedagogy, widening participation, zero tolerance of discrimination',
    '1.24': 'students build EDI literacy through four kinds of inquiry',
    '1.25': 'accessibility in delivery, physical and academic',
    '1.26': 'course content and education for sustainability: seven areas of understanding',
    '1.27': 'courses may help students towards a rewarding professional life: four opportunities',
    '2.1': 'distinctiveness from the European Landscape Convention and its definition of landscape',
    '2.2': 'the convention obliges the UK to provide landscape training; three measures',
    '2.3': 'LI accreditation leading to chartered titles',
    '2.4': 'four areas of the LI accreditation criteria',
    '2.5': 'each course finds its own focus; accredited courses map to the competency framework',
    '2.6': 'credit and level for accreditation set in the LI procedures',
    '2.7': 'the LI lists accredited courses; some courses are not accredited',
    '2.8': 'meeting this statement is not accreditation; consult the LI',
    '2.9': 'accreditation decisions rest with the LI',
    '2.10': 'provider design frameworks and six features course design may have',
    '2.11': 'progression through the honours levels to the threshold; a second or above fits a student for postgraduate study',
    '2.12': 'joint and combined honours students reach core elements of the skills',
    '2.13': 'exit awards, three-year and four-year (Scottish) durations, part-time credit',
    '2.14': 'honours as a step towards the master\'s; some courses ask for a year in practice',
    '2.15': 'chartership route needs an accredited master\'s of 180 credits at level 7',
    '2.16': 'accredited master\'s graduates become LI associate members',
    '2.17': 'four-year integrated undergraduate degrees',
    '2.18': 'one-year conversion routes before the master\'s stage',
    '2.19': 'integrated master\'s degrees over four years',
    '2.20': 'modes, timing and micro-credentials',
    '2.21': 'prospective students and funding arrangements',
    '2.22': 'courses vary in focus; joint subjects and dual accreditation',
    '2.23': 'the Level 3 Landscape Technician qualification as a possible entry route',
    '2.24': 'the Level 7 Chartered Landscape Professional apprenticeship',
    '2.25': 'internal monitoring and periodic review',
    '2.26': 'external reviewers in periodic review',
    '2.27': 'external examining in the subject, from practice and academia',
    '2.28': 'professional review of accredited courses by an LI review group',
    '3.1': 'iterative processes students use to resolve problems',
    '3.2': 'content by course focus; four groups of common areas (context, systems and process, stakeholders, delivery)',
    '3.3': 'teaching techniques and the studio-based culture',
    '3.4': 'projects simulate practice, from small sites to strategic planning',
    '3.5': 'a cumulative approach from survey to specification',
    '3.6': 'tutorials, presentations, the design studio and collaborative projects',
    '3.7': 'placements and visiting practitioners',
    '3.8': 'assessment follows QAA principles and advice',
    '3.9': 'formative and summative assessment at all levels',
    '3.10': 'formative assessment defined',
    '3.11': 'summative assessment defined',
    '3.12': 'the range of assessment methods students meet',
    '3.13': 'recognition of prior learning',
    '3.14': 'generative AI: challenges to integrity and design, the need for openness',
    '4.1': 'the threshold is the minimum for an honours award',
    '4.2': 'most exceed the threshold; typical and excellent described; above threshold follows marking schemes',
    '4.3': 'providers decide the evidence and refer to Annex D',
    '4.4': 'threshold standard: seven skill groups',
    '4.5': 'typical standard: three items beyond threshold',
    '4.6': 'excellent standard: three items beyond typical',
    '4.7': 'master\'s graduates at threshold: eight further qualities',
}
CTYPE = {'1.6': 'area', '3.2': 'area', '3.3': 'practice', '3.4': 'practice', '3.5': 'practice', '3.6': 'practice', '3.7': 'practice',
         '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice', '3.14': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='none', heading='Contents', kind='other: table of contents'),
    dict(number='5', heading='List of references and further resources', kind='other: reference list, read for SB6 and D3'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: membership lists 2000 to 2024, read for supersedes'),
    dict(number='none', heading='section heading lines', kind='other: headings, recorded in SECTIONS and SUB'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ statements outside the rungs
s('1.25.b1', find='physically to resources and facilities, including field work', type='expectation', rung='none', force='should', level='none',
  appliesTo='courses in the subject', addressee='provider', verbs=[], about='physical access to resources and fieldwork', domain='none', award='none',
  para='Courses should consider how inclusive, fair design opens physical access to resources and facilities, fieldwork among them.',
  prac='Consider how your course should open physical access to its resources and facilities, fieldwork included, through inclusive design in every part of delivery.',
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=('Present this as a provider expectation with should-force (' + CITE % '1.25' + '), on physical access, not as a student outcome or a legal duty. '
       'It holds for the course at any level. Set it beside 1.25.b2 on academic access and 4.4.b46 on inclusive communication, and note that the legal duties sit with the provider (1.20).'),
  aad=('Raise it with a programme team planning studios, site visits or fieldwork. Ask: which sites, rooms and field trips would a disabled student find hard to reach, and what is the alternative? '
       'Put it as a design question for staff; do not hand it to a student as something they must achieve.'))
s('1.25.b2', find='academically where alternative forms of teaching, learning, assessment and feedback might be appropriate.', type='expectation', rung='none', force='should', level='none',
  appliesTo='courses in the subject', addressee='provider', verbs=[], about='academic access through alternative forms of delivery', domain='none', award='none',
  para='Courses should consider how inclusive design opens academic access, offering other forms of teaching, learning, assessment or feedback where they suit.',
  prac='Consider how your course should open academic access, by offering alternative ways of teaching, learning, assessing and giving feedback where these fit.',
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=('Present this as a provider expectation with should-force (' + CITE % '1.25' + ') on academic access through alternative forms of delivery; it is not a student outcome. '
       'Do not claim it requires any one adjustment. Set it beside 1.25.b1 and the assessment range in 3.12.'),
  aad=('Raise it when a programme team reviews assessment or feedback. Ask: where could a student show the same outcome another way, and is that option written into the module? '
       'Keep it with staff; do not present it to a student as their responsibility.'))

L126 = dict(type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject, through course content', addressee='both', domain='understanding', award='none')
def k126(n, **k):
    s('1.26.b%d' % n, **L126, **k)
def aaw126(topic, nb):
    return ('Present this as a will-statement on what course content will give students the chance to show (' + CITE % '1.26' + '): understanding of ' + topic + '. '
            'It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. '
            'Set it beside ' + nb + ', the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1).')
def aad126(q):
    return ('Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. '
            'Ask: "' + q + '" Do not read the list aloud; pick the item that fits the conversation.')
k126(1, verbs=['transform'], about='values and actions for sustainability and the UN goals',
     para='Course content will let students show they understand values and actions for sustainability that change society and lead to regenerative futures, as the UN goals illustrate.',
     prac='Course content will give students chances to show they understand sustainability values and actions that change society towards regenerative futures, with the UN goals as illustration.',
     ben='You will have chances to show you understand the values and actions that move society towards a regenerative, sustainable future, using the UN goals as examples.',
     aaw=aaw126('sustainability values and actions, illustrated by the UN goals', '1.26.b2 and 4.4.b11'),
     aad=aad126('Which of the UN goals does your current project touch, and how?'))
k126(2, verbs=[], about='systems thinking: biodiversity and natural capital',
     para='Course content will let students show they understand systems thinking centred on biodiversity, natural systems, natural capital and the ecosystem services that flow from them, at several scales.',
     prac='Course content will give students chances to show systems thinking about biodiversity, natural capital and ecosystem services, and how people interact with them at different scales.',
     ben='You will have chances to show you can think in systems about biodiversity, natural capital and the services ecosystems give us, at different scales.',
     aaw=aaw126('systems thinking on biodiversity, natural capital and ecosystem services', '1.26.b1 and 4.4.b10'),
     aad=aad126('What does your site give people and wildlife, and what would change if you altered it?'))
k126(3, verbs=[], about='climate change: causes, effects, mitigation and adaptation',
     para='Course content will let students show they understand the causes and effects of climate change and see chances for mitigation, adaptation and resilience.',
     prac='Course content will give students chances to show they understand climate change and can spot openings for mitigation, adaptation and resilience.',
     ben='You will have chances to show you understand what causes climate change, what it does, and where design can reduce it or help places adapt.',
     aaw=aaw126('climate change and the openings for mitigation, adaptation and resilience', '1.26.b5'),
     aad=aad126('Where in your scheme could you cut emissions or help the place cope with a changing climate?'))
k126(4, verbs=[], about='legislation and policy at many levels',
     para='Course content will let students show they understand international, national and local law and past, current and emerging policy across levels and subjects.',
     prac='Course content will give students chances to show they understand law at international, national and local level and policy past, present and emerging.',
     ben='You will have chances to show you understand the law and policy, from global to local, that shape sustainable landscape work.',
     aaw=aaw126('the legislative and policy context of sustainability', '3.2 (legislative and planning policy context)'),
     aad=aad126('Which law or policy sets limits or opportunities for your project?'))
k126(5, verbs=[], about='design for adaptation, resilience and regeneration',
     para='Course content will let students show they understand design that helps communities and landscapes adapt, become resilient and regenerate.',
     prac='Course content will give students chances to show they understand design that helps communities and landscapes adapt, become resilient and regenerate.',
     ben='You will have chances to show you understand how design can help communities and landscapes adapt, recover and renew.',
     aaw=aaw126('design for adaptation, resilience and regeneration', '1.26.b3'),
     aad=aad126('How would your design help this community or landscape recover from a shock?'))
k126(6, verbs=[], about='case studies, best practice and live projects',
     para='Course content will let students show understanding through case studies and good practice across scales and kinds of development, with live projects where possible.',
     prac='Course content will give students chances to show understanding through case studies and good practice at many scales, and live projects that face uncertainty where possible.',
     ben='You will have chances to show what you understand through case studies, good practice and, where possible, live projects that imagine sustainable futures.',
     aaw=aaw126('sustainability through case studies, best practice and live projects', '4.4.b16 on precedent study'),
     aad=aad126('Which precedent shows sustainability at the scale you are working at?'))
k126(7, find="materiality in relation to the main palettes of materials they might specify, including the extraction of raw materials and disposal of waste.", verbs=['specify'], about='materiality: extraction and waste',
     para='Course content will let students show they understand the materials they may specify, from extracting raw materials to disposing of waste.',
     prac='Course content will give students chances to show they understand materiality in the palettes they may specify, including extraction and waste.',
     ben='You will have chances to show you understand where the materials you might specify come from and what happens to them as waste.',
     aaw=aaw126('materiality across the life of the materials students may specify', '4.4.b17 and 4.4.b18'),
     aad=aad126('Where does this material come from, and where will it end up?'))

s('2.5', type='requirement', rung='none', force='must', level='none', appliesTo='courses seeking or holding LI accreditation', addressee='provider',
  verbs=['determine', 'map', 'demonstrate'], about='mapping accredited courses to the LI competency framework', domain='none', award='none',
  para='Each course will set its own identity and focus; accredited courses must map themselves to the LI competency framework to show where knowledge requirements are met.',
  prac='Your course sets its own focus (design, planning, management or ecology); if it is accredited it must map to the LI competency framework, showing where each knowledge requirement is met.',
  ben=('n/a', 'a requirement on accredited courses, set by the professional body'),
  aaw=('Present this as a requirement on accredited courses (' + CITE % '2.5' + '), set by the Landscape Institute, not by the statement; "required" is read as must. '
       'Do not claim that meeting the statement brings accreditation (2.8). Set it beside 2.4 and the LI competency framework (not yet ingested).'),
  aad=('Raise it with a programme team seeking or renewing LI accreditation. Ask: where in the course map does each competency get taught and assessed? '
       'Frame it for staff; do not give it to a student as a requirement on them.'))
s('2.11', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='honours students of the subject', addressee='learner',
  verbs=['progress', 'builds'], about='progression through the levels to the threshold', domain='none', award=HON,
  para='Across an honours degree students move up level by level; each level is expected to build towards meeting every threshold skill, usually through credit for all learning and assessment.',
  prac='Plan each level so it builds towards all the threshold skills, with credit for the full range of learning and assessment; a second or above usually fits a graduate for postgraduate study.',
  ben='As you move through each year, what you learn and do should build towards the full set of threshold skills; a second-class result or better usually prepares you for postgraduate study.',
  aaw=('Present this as the issuer\'s expectation on progression (' + CITE % '2.11' + '), worded with "expected" and "would", so read as describes, not must. '
       'It is at FHEQ level 6 (FQHEIS 10) for honours. Set it beside the threshold list 4.4, Annex D 3rd cells (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6; do not claim it sets entry rules for postgraduate study.'),
  aad=('Raise it when a student asks how the years fit together or whether they can go on to a master\'s. Ask: which threshold skills has each year built so far? '
       'Avoid presenting a second-class result as a guarantee of a place.'))
s('2.12', find="2.12 Undergraduates studying Landscape Architecture courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.", type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint and combined honours students', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint honours: core skills plus those of the other subject', domain='subject-skill', award=HON,
  para='Students on joint or combined honours will reach core elements of the subject and generic skills and add others from their other subject.',
  prac='Joint or combined honours students will reach core elements of the specific and generic skills and add skills from their other subject.',
  ben='If you study the subject with another, you will reach the core skills and add others from your second subject, with room to explore where they meet.',
  aaw=('Present this as a will-expectation for joint and combined honours (' + CITE % '2.12' + ') at FHEQ level 6. '
       'Do not claim joint students meet every threshold item in 4.4; the statement says core elements. Set it beside 4.4 and the FHEQ honours descriptor qaa/fheq-2024/4.15.i1.'),
  aad=('Raise it with a joint honours student unsure what is expected of them. Ask: which of the core skills does your landscape half cover, and what does your other subject add? '
       'Avoid implying they must cover the whole single-honours list.'))
s('2.15', type='requirement', rung='none', force='must', level='fheq:7', appliesTo='anyone starting the LI Pathway to Chartership', addressee='learner',
  verbs=['commence', 'requires'], about='the accredited master\'s for the chartership route', domain='none', award=MA,
  para='Starting the formal route to chartered status must begin from a master\'s the LI accredits, carrying 180 credits or more at level 7.',
  prac='Tell students that the Pathway to Chartership must begin from an LI-accredited master\'s of at least 180 credits at level 7.',
  ben='If you want to become a chartered landscape architect, you must first complete a master\'s the professional body accredits, worth 180 credits or more at level 7.',
  aaw=('Present this as a professional body requirement (' + CITE % '2.15' + '), "requires" read as must; it is the LI\'s rule, not an academic standard. '
       'It concerns the master\'s at FHEQ level 7 (spine:7). Set it beside 2.16 and the master\'s list 4.7; do not claim an honours degree alone opens the route.'),
  aad=('Raise it when a student asks how to become chartered. Ask: are you planning an accredited master\'s, and does the one you have in mind carry at least 180 credits at level 7? '
       'Keep it plain and point them to the LI for detail.'))
s('2.21', find="2.21 Prospective students should be aware that funding arrangements for study (including eligibility for fee and maintenance funds) will vary depending on the duration, mode of study and the country in which they study, and are advised to speak to the appropriate funding body and the institution before committing to a programme.", type='expectation', rung='none', force='should', level='none', appliesTo='prospective students', addressee='learner',
  verbs=['vary', 'speak'], about='checking funding before committing', domain='none', award='none',
  para='Prospective students should know funding varies with length, mode and country of study, and are advised to talk to the funding body and the institution first.',
  prac='Prospective students should be told that funding differs by duration, mode and nation, and pointed to the funding body and the institution before they commit.',
  ben='Before you commit, you should know that funding depends on how long, how and where you study; talk to the funding body and the university first.',
  aaw=('Present this as advice with should-force to prospective students (' + CITE % '2.21' + '); it is not an academic standard. '
       'Do not state funding rules; the statement gives none. Set it beside 2.20 on modes of study.'),
  aad=('Raise it when an applicant asks about part-time or four-year routes. Ask: have you checked with your funding body how your choice of mode and length affects support? '
       'Do not give funding figures.'))
s('2.26', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review', addressee='provider',
  verbs=['use', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para='Providers will use external reviewers in periodic review to bring an outside view and make sure threshold standards are met and content fits the subject.',
  prac='In periodic review your institution will bring in external reviewers for an outside view, checking that threshold standards are met and content suits the subject.',
  ben=('n/a', 'a duty on the provider in quality review'),
  aaw=('Present this as a will-expectation on providers (' + CITE % '2.26' + ') about externality in review; it is a quality process, not a student outcome. '
       'Set it beside 2.27 on external examining and 4.4 as the threshold reviewers check.'),
  aad=('Raise it with a programme team preparing for periodic review. Ask: who will give the outside view, and will they test the course against the threshold list? '
       'Do not raise it with students as a standard.'))
s('3.3', type='expectation', rung='none', force='will', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['employ', 'impart', 'stimulate/inspire'], about='a range of teaching techniques and the design studio', domain='none', award='none',
  para='All courses will use a range of teaching methods; the subject is marked by a studio-based, shared learning culture with projects of rising scale and complexity.',
  prac='Your course will use varied teaching methods, from lectures to design charettes, within a studio-based culture where projects grow in scale and complexity.',
  ben=('n/a', 'a duty on the course in how it teaches'),
  aaw=('Present this as a will-expectation on courses (' + CITE % '3.3' + ') about teaching methods; the statement does not prescribe any one method. '
       'Set it beside 3.4 to 3.6 on projects and the studio, and do not claim a set studio contact time.'),
  aad=('Raise it with staff designing teaching. Ask: where does the studio let students apply new knowledge in projects of rising scale? '
       'Keep it for staff; a student meets it as their timetable, not as a target.'))
s('3.9', type='expectation', rung='none', force='will', level='none', appliesTo='students at every level of study', addressee='both',
  verbs=['experience'], about='formative and summative assessment at all levels', domain='none', award='none',
  para='Students at every level will meet both formative and summative assessment.',
  prac='At every level your course will give students both formative and summative assessment.',
  ben='At every stage you will have both practice assessment with feedback and assessment that counts towards your marks.',
  aaw=('Present this as a will-expectation (' + CITE % '3.9' + ') for every level of study; 3.10 and 3.11 define the two kinds. '
       'Do not claim a set ratio between them. Set it beside 3.12 on methods.'),
  aad=('Raise it when a student asks whether a task counts. Ask: is this piece for feedback only, or does it count, and how will you use the feedback? '
       'Explain the difference plainly.'))
s('4.3', find="4.3 Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. That Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with 1st, 2.1, 2.2 and 3rd class honours.", type='requirement', rung='none', force='should', level='fheq:6', appliesTo='providers judging achievement for the award', addressee='provider',
  verbs=['determining', 'refer'], about='providers refer to Annex D for evidence of achievement', domain='none', award=HON,
  para='Each provider decides what evidence shows achievement and should refer to Annex D of the Frameworks, which describes the four honours classifications.',
  prac='Your institution decides what counts as evidence of achievement and should refer to Annex D of the Frameworks, with its descriptions of first, upper second, lower second and third.',
  ben=('n/a', 'a duty on the provider in judging achievement'),
  aaw=('Present this as a should-duty on providers (' + CITE % '4.3' + ') to read the honours classes against Annex D (std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/...). '
       'It holds at FHEQ level 6 and FQHEIS 10. Do not claim the statement sets its own marking scale; set it beside 4.1, 4.2 and the rungs 4.4 to 4.6.'),
  aad=('Raise it with a team writing marking criteria. Ask: does each band in your criteria line up with the Annex D class it stands for? '
       'Keep it for staff, not students.'))

# ------------------------------------------------------------------ threshold, 4.4 (seven groups)
GROUPS = [(1, 18, 'Intellectual'), (19, 25, 'Analytical and data interpretation'), (26, 29, 'Practical'),
          (30, 39, 'Self-management and professional development'), (40, 43, 'Digital literacy'), (44, 49, 'Communication'),
          (50, 56, 'Interpersonal and teamwork')]
def group(n):
    for a, b, h in GROUPS:
        if a <= n <= b:
            return a, b, h
TYP = {'knowledge': '4.5.b1', 'understanding': '4.5.b1', 'subject-skill': '4.5.b3', 'generic-skill': '4.5.b2'}

def th(n, verbs, about, domain, para, prac, ben, topic, q, fw, ad, find=None):
    a, b, h = group(n)
    sib = ', '.join('4.4.b%d' % x for x in (n - 1, n + 1) if a <= x <= b)
    aaw = ('Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the ' + h.lower() + ' group (' + CITE % '4.4' + '). '
           'Describe it as ' + topic + '; do not call it a regulation or apply it to the master\'s list in 4.7. '
           'Set it beside the honours descriptor qaa/fheq-2024/' + fw + ', the Annex D third-class cell qaa/fheq-2024/annex-d/' + ad + ', spine:6'
           + (', the neighbouring items ' + sib if sib else '') + ' and the typical rung ' + TYP[domain] + '.')
    aad = ('Raise it when a student or a module team asks what honours expects on ' + topic + '. '
           'Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. '
           'Ask: "' + q + '" Do not read the list aloud, and present it as the floor, not the goal.')
    r = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6', appliesTo='honours graduates at the threshold',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben, aaw=aaw, aad=aad)
    if find:
        r['find'] = find
    P['4.4.b%d' % n] = r

T = 'To reach the threshold, you will be able to '
# Intellectual
th(1, ['analyse', 'synthesising', 'develop'], 'analysis and balanced argument', 'generic-skill',
   'At threshold, can analyse information and draw its results together into a balanced case.',
   'At threshold, graduates can analyse information and combine what they find into balanced arguments.',
   T + 'analyse information and pull the results together into a fair, balanced argument.',
   'analysing information and building balanced arguments', 'Where in your last report did you weigh both sides before concluding?',
   '4.15.b7', 'cognitive/r2/3rd')
th(2, ['demonstrate'], 'decisions in complex, unpredictable settings', 'generic-skill',
   'At threshold, can show sound decision-making where situations are complex and hard to predict.',
   'At threshold, graduates can show they make decisions in complex, unpredictable settings.',
   T + 'show that you can make decisions when a situation is complex and hard to predict.',
   'decision-making in complex, unpredictable settings', 'Tell me about a design decision you made when the site or brief kept changing.',
   '4.15.b9.2', 'cognitive/r3/3rd')
th(3, ['apply', 'develop'], 'critical thinking towards a professional position', 'subject-skill',
   'At threshold, can think critically to reach an informed stance of their own as an emerging landscape professional.',
   'At threshold, graduates can use critical thinking to form their own informed position as future landscape professionals.',
   T + 'think critically and reach your own informed view as someone entering the landscape profession.',
   'critical thinking towards a personal professional position', 'What do you stand for as a landscape professional, and what shaped that view?',
   '4.15.b7', 'cognitive/r2/3rd')
th(4, ['appreciate', 'integrate'], 'stakeholder perspectives in proposals', 'subject-skill',
   'At threshold, can see a landscape as different stakeholders see it and build their needs into proposals.',
   'At threshold, graduates can view landscapes through different stakeholders\' eyes and fold their needs into proposals.',
   T + 'see a landscape as the different people with a stake in it see it, and build their needs into your proposals.',
   'stakeholder perspectives in proposals', 'Whose view of this site did your proposal leave out, and how could you include it?',
   '4.15.b3.1', 'knowledge/r3/3rd')
th(5, ['understand', 'allow', 'inform'], 'competing theories and priorities in judgement', 'understanding',
   'At threshold, can understand and make room for rival theories and priorities so that judgements and proposals rest on good evidence.',
   'At threshold, graduates understand and allow for competing theories and priorities, so their judgements and proposals are well evidenced.',
   T + 'understand rival theories and priorities and take them into account so your judgements rest on good evidence.',
   'weighing competing theories and priorities', 'Which competing priority did you have to trade off, and on what evidence?',
   '4.15.b4', 'knowledge/r2/3rd')
th(6, ['evaluate', 'using'], 'evaluating alternative proposals', 'subject-skill',
   'At threshold, can assess alternative proposals with suitable tools and techniques.',
   'At threshold, graduates can evaluate alternative proposals with fitting tools and techniques.',
   T + 'compare and judge different proposals using the right tools and techniques.',
   'evaluating alternative proposals', 'How did you decide between your two options, and what tool did you use to compare them?',
   '4.15.b7', 'cognitive/r2/3rd')
th(7, ['formulate', 'interpret', 'identifying'], 'project briefs and their aims', 'subject-skill',
   'At threshold, can draft and read project briefs, setting suitable aims and objectives for known and new problems at varied scales.',
   'At threshold, graduates can write and interpret project briefs, setting aims and objectives for familiar and new problems at many scales.',
   T + 'write and read project briefs, setting sensible aims and objectives for problems old and new, small and large.',
   'formulating and interpreting project briefs', 'If you rewrote this brief, what aims would you set and why?',
   '4.15.b7', 'cognitive/r3/3rd')
th(8, ['identify', 'generate'], 'from theory to policies, plans and interventions', 'subject-skill',
   'At threshold, can pick the theory, concepts, principles and techniques that produce fitting policies, strategies, plans or interventions across scales of space and time.',
   'At threshold, graduates can find the relevant theory and techniques and turn them into policies, strategies, plans or interventions at varied spatial and time scales.',
   T + 'choose the theory and techniques that lead to good policies, strategies, plans or practical changes, at scales of space and time.',
   'turning theory into policies, plans and interventions', 'Which principle drove your strategy, and does it hold over twenty years as well as one?',
   '4.15.b3.1', 'knowledge/r2/3rd')
th(9, ['identify', 'research', 'apply'], 'researching and applying knowledge to problems', 'subject-skill',
   'At threshold, can find, research and use knowledge on known and new problems at a range of scales.',
   'At threshold, graduates can identify and research what they need to know and apply it to familiar and new problems of varied scale.',
   T + 'work out what you need to know, research it and use it on familiar and new problems of any size.',
   'researching and applying knowledge to problems', 'What did you need to find out for this project, and how did you find it?',
   '4.15.b6', 'cognitive/r3/3rd')
th(10, ['appreciate', 'reflect', 'formulate'], 'the ecosystem context of projects', 'subject-skill',
   'At threshold, can grasp and reflect on the ecosystem around a landscape project and frame proposals that conserve and balance it.',
   'At threshold, graduates appreciate and reflect on a project\'s ecosystem context and can frame proposals that conserve it and keep it in balance.',
   T + 'understand and reflect on the ecosystem your project sits in, and design proposals that protect it and keep it in balance.',
   'the ecosystem context of projects', 'What ecosystem does your site belong to, and how does your proposal keep it in balance?',
   '4.15.b1', 'knowledge/r1/3rd')
th(11, ['demonstrate'], 'creativity and innovation for sustainability', 'subject-skill',
   'At threshold, can show creativity and new ideas within a sustainable frame.',
   'At threshold, graduates can show creativity and innovation in a sustainable context.',
   T + 'show creative, new thinking that also respects sustainability.',
   'creativity and innovation within a sustainable context', 'What is new in your scheme, and what makes it sustainable as well?',
   '4.15.b6', 'cognitive/r4/3rd')
th(12, ['plan', 'execute', 'evaluating', 'drawing'], 'planning and carrying out research', 'generic-skill',
   'At threshold, can plan and conduct research, assess its results and reach sound conclusions.',
   'At threshold, graduates can plan and carry out research, evaluate the outcomes and draw valid conclusions.',
   T + 'plan and carry out research, judge what it shows and reach sound conclusions.',
   'planning and carrying out research', 'How did you check that your conclusions follow from what you found?',
   '4.15.b6', 'knowledge/r3/3rd')
th(13, ['engage'], 'secondary sources and referencing', 'generic-skill',
   'At threshold, can work with secondary research sources, finding suitable academic literature and citing it by standard conventions.',
   'At threshold, graduates can use secondary sources, find suitable academic literature and reference it to standard conventions.',
   T + 'find and use published research and academic reading, and reference it properly.',
   'using secondary sources and referencing', 'Which sources did you lean on most, and how did you know they were sound?',
   '4.15.b5', 'cognitive/r1/3rd')
th(14, ['understand', 'arise'], 'where ethical, legal or data issues arise', 'understanding',
   'At threshold, can understand where questions of ethics, law or data protection may come up.',
   'At threshold, graduates understand where questions of ethics, law or data protection may arise in their work.',
   T + 'tell where ethical, legal or data protection questions may come up in your work.',
   'where questions of ethics, law or data protection may arise', 'Did your survey or consultation raise any data protection question?',
   '4.15.b4', 'knowledge/r2/3rd')
th(15, ['understand'], 'intellectual property in design', 'understanding',
   'At threshold, can understand what intellectual property is and how it affects creative design settings.',
   'At threshold, graduates understand the role and effect of intellectual property in creative design work.',
   T + 'understand how intellectual property works in design and how it affects your work and others\'.',
   'intellectual property in creative design', 'Whose ideas or images did you draw on, and how did you credit them?',
   '4.15.b1', 'knowledge/r2/3rd')
th(16, ['identify', 'analyse', 'critique'], 'precedent study', 'subject-skill',
   'At threshold, can find, analyse and critique fitting precedents.',
   'At threshold, graduates can identify, analyse and critique suitable precedent studies.',
   T + 'find good precedents, analyse them and judge what they do well or badly.',
   'precedent study', 'Which precedent taught you most, and what would you do differently from it?',
   '4.15.b3.2', 'cognitive/r1/3rd')
th(17, ['identify', 'specify'], 'specifying hard materials and planting', 'subject-skill',
   'At threshold, can choose and specify suitable hard materials and planting for a range of proposals.',
   'At threshold, graduates can identify and specify suitable hard materials and vegetation for varied proposals.',
   T + 'choose and specify the right hard materials and plants for different proposals.',
   'specifying hard materials and vegetation', 'Why did you choose these plants and surfaces for this site?',
   '4.15.b2', 'practical/r1/3rd',
   find='identify and specify appropriate hard materials and vegetation for a range of proposals')
th(18, ['understand'], 'material properties and cost', 'knowledge',
   'At threshold, can understand how materials perform structurally and environmentally, and the broad cost of specifying them.',
   'At threshold, graduates understand the structural, performance and sustainability qualities of materials and the broad financial effects of specifying them.',
   T + 'understand how materials perform, how sustainable they are and roughly what specifying them costs.',
   'the properties and cost of specified materials', 'What would this surface cost over its life, and how long will it last?',
   '4.15.b1', 'knowledge/r1/3rd',
   find='understand the structural, performance and sustainability characteristics and the broad financial implications of material specification.')
# Analytical and data interpretation
th(19, ['identify'], 'geomatic information', 'subject-skill',
   'At threshold, can identify suitable geomatic information: gathering, modelling and analysing data tied to location.',
   'At threshold, graduates can identify suitable geomatic information, that is acquiring, modelling and analysing spatially referenced data.',
   T + 'identify the right spatial data for a task and know how it is gathered, modelled and analysed.',
   'geomatic information and spatial data', 'What spatial data did you use for this site, and where did it come from?',
   '4.15.b2', 'practical/r4/3rd')
th(20, ['identify', 'collate', 'make'], 'evidence sources and sampling', 'subject-skill',
   'At threshold, can find and gather suitable sources of evidence and choose samples well.',
   'At threshold, graduates can identify and collate suitable evidence and select samples effectively.',
   T + 'find and gather the right evidence and choose your samples sensibly.',
   'sources of evidence and sample selection', 'How did you choose where and what to sample?',
   '4.15.b2', 'knowledge/r3/3rd')
th(21, ['identify', 'apply'], 'qualitative and quantitative analysis', 'subject-skill',
   'At threshold, can choose and use fitting qualitative or quantitative techniques to analyse information.',
   'At threshold, graduates can identify and apply suitable qualitative or quantitative analysis techniques.',
   T + 'choose and use the right qualitative or numerical methods to analyse information.',
   'qualitative and quantitative analysis', 'Why was that method the right one for this data?',
   '4.15.b2', 'practical/r4/3rd')
th(22, ['demonstrate'], 'precision in recording and analysing data', 'subject-skill',
   'At threshold, can show due precision when identifying, recording and critically analysing data from field, laboratory or secondary sources.',
   'At threshold, graduates can show suitable precision in identifying, recording and critically analysing data from field, lab or secondary sources.',
   T + 'record and analyse data from the field, the lab or published sources with the care and accuracy the task needs.',
   'precision with data from field, laboratory and secondary sources', 'How accurate did your survey need to be, and was it?',
   '4.15.b2', 'practical/r2/3rd')
th(23, ['prepare', 'process', 'interpret', 'present', 'using'], 'handling and presenting data with software', 'subject-skill',
   'At threshold, can prepare, process, interpret and present data with suitable techniques and software.',
   'At threshold, graduates can prepare, process, interpret and present data using fitting techniques and software.',
   T + 'prepare, process, interpret and present data using the right techniques and software.',
   'preparing, interpreting and presenting data', 'What does this chart or map tell a reader in one glance?',
   '4.15.b2', 'practical/r4/3rd')
th(24, ['solve', 'using'], 'numerical problem-solving', 'generic-skill',
   'At threshold, can solve numerical problems with computer-based and other methods.',
   'At threshold, graduates can solve numerical problems using computers and other techniques.',
   T + 'solve number problems, with a computer or by other means.',
   'solving numerical problems', 'Which calculations did the project need, and how did you check them?',
   '4.15.b3.1', 'transferable/r1/3rd')
th(25, ['identify', 'analyse', 'present', 'use'], 'financial information in decisions', 'subject-skill',
   'At threshold, can find, analyse and present cost information and draw on it in decisions matched to the scale of the proposals.',
   'At threshold, graduates can find, analyse and present financial data and draw on it in decisions fitted to the nature and scale of proposals.',
   T + 'find, analyse and present cost information and use it in decisions that suit the size of the proposal.',
   'financial information in decision-making', 'How did cost shape the choices you made in this scheme?',
   '4.15.b9.2', 'practical/r4/3rd',
   find='identify, analyse and present financial information and use it in decision-making at a level appropriate to the nature and scale of the proposals.')
# Practical
th(26, ['devise', 'plan', 'undertake'], 'safe desk, field and studio investigations', 'subject-skill',
   'At threshold, can design, plan and carry out desk, field and studio investigations responsibly, sensitively and safely.',
   'At threshold, graduates can design, plan and carry out investigations at the desk, in the field and in the studio, responsibly, sensitively and safely.',
   T + 'design, plan and carry out desk, field and studio investigations in a careful, responsible and safe way.',
   'safe and responsible investigations', 'What did you do to keep yourself and others safe on your last site visit?',
   '4.15.b6', 'practical/r2/3rd')
th(27, ['understand', 'comply'], 'access rights, health and safety, research ethics', 'subject-skill',
   'At threshold, can understand and keep to access rights and health and safety rules, with ethical care in research, with people and in the environment.',
   'At threshold, graduates understand and comply with rights of access and health and safety requirements, including ethics in research, with people and in the environment.',
   T + 'understand and follow rules on access to land and on health and safety, and act ethically when working with people and places.',
   'access rights, health and safety and research ethics', 'Did you have the right to be on that land, and who did you need to ask?',
   '4.15.b2', 'practical/r1/3rd')
th(28, ['demonstrate'], 'scale and proportion in design or management', 'subject-skill',
   'At threshold, can show clear, fitting use of scale and proportion in designing or managing landscapes.',
   'At threshold, graduates can show a clear, suitable use of scale and proportion in landscape design or management.',
   T + 'use scale and proportion clearly and well when you design or manage a landscape.',
   'scale and proportion', 'How does a person standing in your space feel its size?',
   '4.15.b2', 'practical/r3/3rd')
th(29, ['apply', 'present'], 'models, hand drawing and graphics to present', 'subject-skill',
   'At threshold, in design areas, can use model-making, hand drawing and other graphic skills to show proposals to expert and lay audiences.',
   'At threshold, in design subject areas, graduates can apply model-making, hand drawing and other graphic skills to put proposals before expert and lay audiences.',
   T + 'in design work, use models, hand drawing and other graphics to show your proposals to experts and the public.',
   'physical models, hand drawing and graphics', 'Which drawing or model best explains your idea to someone outside the profession?',
   '4.15.b8', 'practical/r3/3rd')
# Self-management and professional development
th(30, ['work', 'using'], 'working well as an individual', 'generic-skill',
   'At threshold, can work well alone, showing initiative, managing self, time and tasks, and reflecting.',
   'At threshold, graduates can work effectively on their own, showing initiative, managing themselves, their time and their tasks, and reflecting.',
   T + 'work well on your own, using initiative, managing your time and tasks and reflecting on how it went.',
   'working effectively as an individual', 'How did you plan your own time on the last long project?',
   '4.15.b9.1', 'transferable/r3/3rd')
th(31, ['identify'], 'personal goals and responsibilities', 'generic-skill',
   'At threshold, can name personal goals and responsibilities.',
   'At threshold, graduates can identify their individual goals and responsibilities.',
   T + 'set out your own goals and what you are responsible for.',
   'individual goals and responsibilities', 'What are you aiming for this term, and what is yours to deliver?',
   '4.15.b9.1', 'transferable/r4/3rd')
th(32, ['set', 'perform'], 'targets and allocated roles', 'generic-skill',
   'At threshold, can set realistic targets and act as allocated roles and responsibilities require.',
   'At threshold, graduates can set realistic targets and perform as their allocated roles and responsibilities need.',
   T + 'set realistic targets and do what your role in a team asks of you.',
   'realistic targets and allocated roles', 'Was the target you set yourself realistic, and how do you know?',
   '4.15.b9.1', 'transferable/r4/3rd')
th(33, ['reflect', 'evaluate'], 'reflecting on own performance', 'generic-skill',
   'At threshold, can reflect on and judge their own performance.',
   'At threshold, graduates can reflect on and evaluate their own performance.',
   T + 'look back on your own work and judge how well you did.',
   'reflecting on and evaluating their own performance', 'What would you change if you started that project again?',
   '4.15.b5', 'transferable/r5/3rd')
th(34, ['develop'], 'adaptable approach to study and work', 'generic-skill',
   'At threshold, can build an adaptable, flexible way of studying and working.',
   'At threshold, graduates can develop an adaptable, flexible approach to study and work.',
   T + 'adapt how you study and work when things change.',
   'an adaptable, flexible approach to study and work', 'When the brief changed, how did you adjust your way of working?',
   '4.15.b9.3', 'transferable/r3/3rd')
th(35, ['develop'], 'time management and organisation', 'generic-skill',
   'At threshold, can build good time management and organisation, planning and carrying out a workload.',
   'At threshold, graduates can develop effective time management and organisation, including planning and executing a workload.',
   T + 'manage your time and organise your workload from plan to finish.',
   'time management and organisation', 'How did you plan your workload across deadlines this term?',
   '4.15.b9.1', 'transferable/r3/3rd')
th(36, ['demonstrate'], 'professional competence and conduct, with EDI', 'generic-skill',
   'At threshold, can show the competence, behaviour and attitude the profession needs, with regard to equity, diversity and inclusion.',
   'At threshold, graduates can show the competence, behaviour and attitude the profession requires, with attention to equity, diversity and inclusion.',
   T + 'show the skills, conduct and attitude the profession expects, including fairness and respect for everyone.',
   'professional competence, behaviour and attitude, with equity, diversity and inclusion', 'How did you make sure everyone in your team and your consultation was treated fairly?',
   '4.15.b9.1', 'transferable/r4/3rd')
th(37, ['recognise', 'respect', 'work'], 'professional codes of conduct', 'generic-skill',
   'At threshold, can recognise, respect and keep within fitting professional codes of conduct.',
   'At threshold, graduates can recognise, respect and work within suitable professional codes of conduct.',
   T + 'know, respect and work within the codes of conduct of the profession.',
   'professional codes of conduct', 'Which part of the professional code applied to your work this term?',
   '4.15.b9.2', 'transferable/r4/3rd')
th(38, ['recognise', 'respect'], 'moral, ethical, ecological and social issues', 'generic-skill',
   'At threshold, can recognise and respect the moral, ethical, social and ecological questions the subject raises.',
   'At threshold, graduates can recognise and respect the ethical, moral, social and ecological issues of the subject.',
   T + 'see and respect the moral, ethical, ecological and social questions landscape work raises.',
   'the moral, ethical, ecological and social issues of the subject', 'Who gains and who loses from this scheme, people and nature alike?',
   '4.15.b4', 'transferable/r5/3rd')
th(39, ['develop', 'display', 'acquire'], 'generic skills for employability and CPD', 'generic-skill',
   'At threshold, can build and show the generic skills needed to gain new competences for work, career growth and continuing professional development.',
   'At threshold, graduates can develop and display generic skills to gain new competencies for employability, career progression and CPD.',
   T + 'build and show the general skills you need to keep learning for work, career and professional development.',
   'generic skills for employability and professional development', 'Which skill will you need next in your career, and how will you get it?',
   '4.15.b9.3', 'transferable/r3/3rd',
   find='develop and display the generic skills required to acquire new competencies for employability, career progression and continuing professional development.')
# Digital literacy
th(40, ['identify', 'apply', 'communicate'], 'hardware and software to communicate', 'generic-skill',
   'At threshold, can choose and use hardware and software suited to the scale of the work to communicate proposals well to different audiences.',
   'At threshold, graduates can identify and apply hardware and software fitted to the scale of work to communicate proposals to varied audiences.',
   T + 'choose and use the right hardware and software for the job to share your proposals with different audiences.',
   'hardware and software for communicating proposals', 'Why did you pick this software for this audience?',
   '4.15.b8', 'transferable/r1/3rd')
th(41, ['use'], 'internet and social media', 'generic-skill',
   'At threshold, can use the internet and social media fittingly, to communicate and to find information.',
   'At threshold, graduates can use the internet and social media appropriately for communication and as an information source.',
   T + 'use the internet and social media sensibly to communicate and find information.',
   'the internet and social media', 'How do you check that what you find online is reliable?',
   '4.15.b8', 'transferable/r1/3rd')
th(42, ['have', 'implement'], 'awareness of emerging technologies', 'generic-skill',
   'At threshold, can show awareness of new technologies and of good, fitting ways to put them to use.',
   'At threshold, graduates are aware of emerging technologies and of effective, suitable ways to implement them.',
   T + 'keep aware of new technologies and how to use them well.',
   'awareness of emerging technologies', 'Which new tool have you tried lately, and was it worth it?',
   '4.15.b9.3', 'transferable/r1/3rd')
th(43, ['apply'], 'digital tools across survey, analysis and design', 'subject-skill',
   'At threshold, can use suitable technology lawfully and well at each stage of survey, analysis and design, from CAD, GIS and BIM to drones, AI and spatial computing.',
   'At threshold, graduates can apply suitable technology legally and appropriately across survey, analysis and design: CAD, visualisation, GIS, BIM, fabrication, AI, AR and VR, drones and apps among them.',
   T + 'use the right digital tools legally and well through survey, analysis and design, such as CAD, GIS, BIM, 3D printing, AI, drones and survey apps.',
   'digital tools across survey, analysis and design', 'Which digital tool did you use at each stage of your last project, and was its use legal and fitting?',
   '4.15.b2', 'practical/r3/3rd',
   find='effectively apply suitable technology in an appropriate and legal way for the production of work at various stages of the survey, analysis and design processes; including, for example, but not exclusively: − computer aided drafting (CAD) − visualisation and image manipulation − digital model making − geographic information systems (GIS) − building information modelling (BIM) − computer-based processing, including, for example, National Building Specification − data processing − CAD/CAM/CNC for model making, 3D printing and laser cutting − artificial intelligence (AI), including generative text and images − spatial computing, for example augmented reality (AR) / virtual reality (VR) − drones, for example site mapping and plant species identification − smartphone applications, including, for example, plant identification and other applications for site surveys.')
# Communication
th(44, ['identify', 'engage', 'test', 'inform'], 'engaging diverse stakeholders', 'subject-skill',
   'At threshold, can find and involve the many different stakeholders at the right stages of a project to test and shape research and proposals.',
   'At threshold, graduates can identify and engage diverse stakeholders at suitable project stages to test and inform research and proposals.',
   T + 'find and involve the different people with a stake in a project at the right moments, to test and shape your ideas.',
   'engaging diverse stakeholders', 'Who did you consult, at which stage, and what changed as a result?',
   '4.15.b8', 'transferable/r2/3rd')
th(45, ['understand', 'select', 'apply'], 'choosing communication methods for the audience', 'generic-skill',
   'At threshold, can understand, choose and use approaches, tools and techniques that suit the audience and the material.',
   'At threshold, graduates can understand, select and apply approaches, tools and techniques suited to the audience and the material.',
   T + 'choose and use ways of communicating that suit both the audience and what you are showing.',
   'matching communication to audience and material', 'How would you present this scheme differently to a council committee and to residents?',
   '4.15.b8', 'practical/r4/3rd')
th(46, ['ensure'], 'inclusive, accessible communication', 'generic-skill',
   'At threshold, can make sure communication is inclusive and accessible to as many people as possible, above all where stakeholders include minorities or people with varied needs.',
   'At threshold, graduates can make communication inclusive and accessible to as wide a range of people as possible, particularly minority groups and those with diverse needs.',
   T + 'make your communication inclusive and accessible to as many people as possible, especially those often left out.',
   'inclusive and accessible communication', 'Who might not be able to read or reach your materials, and what would help them?',
   '4.15.b8', 'transferable/r1/3rd')
th(47, ['communicate'], 'clear communication in many forms', 'generic-skill',
   'At threshold, can communicate clearly, briefly, confidently and fittingly to varied audiences in writing, speech and graphics, including physical and digital models.',
   'At threshold, graduates can communicate clearly, concisely, confidently and appropriately to varied audiences in written, spoken and graphic forms, including models and visual media.',
   T + 'communicate clearly, briefly and confidently in writing, speech, drawings and models to different audiences.',
   'clear communication in written, verbal and graphic forms', 'Could someone grasp your main idea from your boards in a minute?',
   '4.15.b8', 'transferable/r1/3rd')
th(48, ['communicate'], 'accuracy and the limits of illustrative graphics', 'generic-skill',
   'At threshold, can communicate accurately where possible and, where not, as with illustrative graphics, be open about the limits of the output.',
   'At threshold, graduates can communicate accurately where they can, and where they cannot (as with illustrative graphics) make the limits of the output clear.',
   T + 'be accurate where you can, and where an image is only illustrative, say so clearly.',
   'accuracy and the limits of illustrative outputs', 'What does this visualisation show accurately, and what is artistic licence?',
   '4.15.b8', 'practical/r4/3rd')
th(49, ['explore', 'capitalise', 'ensuring'], 'AI and emerging tools in communication', 'generic-skill',
   'At threshold, can try out and make use of new digital tools such as AI in preparing communication and presentations, while checking the outputs are fit and accurate.',
   'At threshold, graduates can explore and use emerging digital tools such as AI to prepare communication and presentations, ensuring the outputs are appropriate and accurate.',
   T + 'try new digital tools such as AI when preparing material, and check that what they produce is accurate and fit to use.',
   'using AI and emerging digital tools in communication', 'Where did AI help your presentation, and how did you check its output?',
   '4.15.b8', 'transferable/r1/3rd',
   find='explore and capitalise on emerging digital tools (such as AI) in the preparation of communication materials and presentation while ensuring the appropriateness and accuracy of the outputs generated.')
# Interpersonal and teamwork
th(50, ['contribute'], 'setting group aims and roles', 'generic-skill',
   'At threshold, can help confidently and well to set a group\'s aims, objectives and roles.',
   'At threshold, graduates can contribute confidently and effectively to setting group aims, objectives and roles.',
   T + 'help your group agree its aims and who does what, with confidence.',
   'setting group aims and roles', 'How did your group agree who would do what?',
   '4.15.b9.1', 'transferable/r2/3rd')
th(51, ['contribute', 'demonstrating', 'consider', 'appreciate', 'respect', 'evaluate'], 'respectful group discussion', 'generic-skill',
   'At threshold, can take part constructively and sensitively in group discussion, weighing and respecting others\' views, especially those of people with varied life experience.',
   'At threshold, graduates can contribute constructively and sensitively to group discussion, considering and respecting others\' views, particularly from diverse life experiences.',
   T + 'take part in group discussions constructively and with care, listening to and respecting views unlike your own.',
   'respectful, constructive group discussion', 'When someone in your group disagreed, how did you weigh their view?',
   '4.15.b9.1', 'transferable/r2/3rd')
th(52, ['apply', 'address', 'provide'], 'multidisciplinary problems and holistic solutions', 'generic-skill',
   'At threshold, can bring knowledge, critical thought and understanding to multidisciplinary problems and offer complete, joined-up solutions.',
   'At threshold, graduates can apply knowledge and critical thinking to multidisciplinary problems and offer comprehensive, holistic solutions.',
   T + 'bring what you know and think to problems that cross disciplines, and offer joined-up answers.',
   'multidisciplinary problems and holistic solutions', 'Which other discipline did your solution depend on, and how did you work with it?',
   '4.15.b3.1', 'cognitive/r3/3rd')
th(53, ['contribute'], 'contributing to group outputs', 'generic-skill',
   'At threshold, can contribute well to a group\'s outputs, such as reports and presentations.',
   'At threshold, graduates can contribute effectively to group outputs, including reports and presentations.',
   T + 'play your full part in producing a group\'s reports and presentations.',
   'contributing to group outputs', 'What was your part in the group report?',
   '4.15.b8', 'transferable/r2/3rd')
th(54, ['demonstrate', 'lead'], 'leading a group', 'generic-skill',
   'At threshold, can show the ability to lead a group across a range of projects.',
   'At threshold, graduates can show they can lead a group in a range of projects.',
   T + 'lead a group on different kinds of project.',
   'leading a group', 'When did you last lead a group, and what did you learn?',
   '4.15.b9.1', 'transferable/r2/3rd')
th(55, ['demonstrate', 'led'], 'being led within a group', 'generic-skill',
   'At threshold, can show the ability to be led as a group member across a range of projects.',
   'At threshold, graduates can show they can work under another\'s lead in a group across varied projects.',
   T + 'work well under someone else\'s lead in a group.',
   'being led as part of a group', 'How did you support the person leading your group?',
   '4.15.b9.1', 'transferable/r2/3rd')
th(56, ['demonstrate'], 'community engagement and consultation', 'understanding',
   'At threshold, can show awareness of the interdisciplinary character and processes of community engagement and consultation.',
   'At threshold, graduates can show awareness of the interdisciplinary nature and processes of community engagement and consultation.',
   T + 'show you understand how community engagement and consultation work and who takes part in them.',
   'community engagement and consultation', 'Which professions took part in the consultation you saw, and what did each bring?',
   '4.15.b1', 'knowledge/r3/3rd',
   find='demonstrate an awareness of the interdisciplinary nature and processes involved in community engagement and consultation exercises.')

# ------------------------------------------------------------------ typical (4.5) and excellent (4.6)
def rung(r, n, verbs, about, domain, para, prac, ben, ad, q, find=None):
    lead = '4.5' if r == 'typical' else '4.6'
    other = ('4.6.b%d' % n) if r == 'typical' else ('4.5.b%d' % n)
    cls = 'upper second (2.1)' if r == 'typical' else 'first (1st)'
    cell = ad + ('/2.1' if r == 'typical' else '/1st')
    aaw = ('Present this as the ' + r + ' standard, which the statement describes as going beyond ' + ('threshold' if r == 'typical' else 'typical') + ' for honours, at FHEQ level 6 and FQHEIS level 10 (' + CITE % lead + '). '
           'It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. '
           'Set it beside ' + other + ', the Annex D ' + cls + ' cell qaa/fheq-2024/annex-d/' + cell + ' and spine:6.')
    aad = ('Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. '
           'Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. '
           'Ask: "' + q + '" Never present this rung as the minimum.')
    rec = dict(type=r, rung=r, force='describes', forceFrom=lead, level='fheq:6', appliesTo='honours graduates at the %s standard' % r,
               addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben, aaw=aaw, aad=aad)
    if find:
        rec['find'] = find
    P['%s.b%d' % (lead, n)] = rec

rung('typical', 1, ['achieved', 'demonstrated'], 'all outcomes met, with advanced knowledge and skills', 'knowledge',
     'At the typical standard, has met every required course outcome and shown advanced knowledge, understanding and cognitive, practical and transferable skills consistently.',
     'At the typical standard, graduates have met all required course outcomes and shown advanced knowledge, understanding and cognitive, practical and transferable skills, consistently.',
     'At the typical standard, you have met every outcome your course sets and shown advanced knowledge and skills, consistently.',
     'summary/r1', 'Across your modules, where have you gone past simply meeting the outcomes?')
rung('typical', 2, [], 'more critical reflection, responsibility and autonomy', 'generic-skill',
     'At the typical standard, applies the threshold knowledge, understanding and skills with more critical reflection, personal responsibility and autonomy.',
     'At the typical standard, graduates apply the threshold knowledge, understanding and skills with more critical reflection, personal responsibility and independence.',
     'At the typical standard, you use the threshold knowledge and skills with more critical reflection and take more responsibility for your own work.',
     'summary/r3', 'Where did you decide something for yourself rather than wait to be told?')
rung('typical', 3, ['demonstrated', 'showing', 'addressing'], 'more insight, initiative, problem-solving and creativity', 'subject-skill',
     'At the typical standard, applies and carries out the threshold knowledge and skills well and fittingly, with more insight, initiative, strong problem-solving and creativity.',
     'At the typical standard, graduates apply and execute the threshold knowledge and skills effectively, showing more insight, initiative, strong problem-solving and creativity.',
     'At the typical standard, you put the threshold skills to work well, with more insight, initiative, creativity and strong problem-solving.',
     'summary/r4', 'Which problem in your project did you solve in a way you are proud of?',
     find='demonstrated effective and appropriate application and execution of the knowledge, understanding and skills listed above, showing more insight, initiative, strong problem- solving ability and creativity in addressing their work.')
rung('excellent', 1, ['achieved', 'demonstrated'], 'all outcomes met, with strong knowledge and skills', 'knowledge',
     'At the excellent standard, has met every required course outcome and shown strong knowledge, understanding and cognitive, practical and transferable skills.',
     'At the excellent standard, graduates have met all required course outcomes and shown strong knowledge, understanding and cognitive, practical and transferable skills.',
     'At the excellent standard, you have met every outcome your course sets and shown strong knowledge and skills across the board.',
     'summary/r1', 'What would show an examiner that your knowledge is strong, not only sufficient?')
rung('excellent', 2, [], 'originality, independent reflection, leadership and ethics', 'generic-skill',
     'At the excellent standard, applies the threshold knowledge and skills with more originality, independent critical reflection, responsibility, autonomy and leadership, and clear professional and ethical awareness.',
     'At the excellent standard, graduates apply the threshold knowledge and skills with greater originality, independent critical reflection, responsibility, autonomy and leadership, and clear professional and ethical awareness.',
     'At the excellent standard, you use the threshold knowledge and skills with real originality, reflect critically on your own, lead others and show clear professional and ethical judgement.',
     'summary/r3', 'Where did you lead, and what ethical judgement did you have to make?')
rung('excellent', 3, ['demonstrated', 'showing'], 'fluent application with originality and exceptional initiative', 'subject-skill',
     'At the excellent standard, applies and carries out the threshold knowledge and skills fluently and well, with more originality, insight, new approaches, exceptional initiative and problem-solving.',
     'At the excellent standard, graduates apply and execute the threshold knowledge and skills fluently and effectively, with greater originality, insight, novel approaches and exceptional initiative and problem-solving.',
     'At the excellent standard, you put the threshold skills to work fluently, with original insight, new approaches and exceptional initiative in solving problems.',
     'summary/r4', 'What in your work did nobody show you how to do?',
     find='demonstrated effective, fluent and appropriate application and execution of the knowledge, understanding and skills listed above, showing higher levels of originality, insight, novel approaches, with exceptional initiative and problem-solving skills.')

# ------------------------------------------------------------------ master's threshold (4.7)
def ma(n, verbs, about, domain, para, prac, ben, fw, q):
    sib = ', '.join('4.7.b%d' % x for x in (n - 1, n + 1) if 1 <= x <= 8)
    aaw = ('Present this as a threshold standard for master\'s graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (' + CITE % '4.7' + '). '
           'It carries will-force; do not apply it to the honours award or claim it is the LI\'s accreditation rule. '
           'Set it beside the master\'s descriptor qaa/fheq-2024/' + fw + ', spine:7 and the neighbouring items ' + sib + '.')
    aad = ('Raise it with a master\'s student, or a team designing a master\'s, when the talk turns to what lifts work above honours. '
           'Put it plainly, in the second person for a student and as an outcome to evidence for staff. '
           'Ask: "' + q + '" Do not read the list aloud or treat it as an aspiration; it is the master\'s minimum.')
    P['4.7.b%d' % n] = dict(type='threshold', rung='threshold', force='will', forceFrom='4.7', level='fheq:7', appliesTo='master\'s graduates at the threshold',
                            addressee='learner', verbs=verbs, about=about, domain=domain, award=MA, para=para, prac=prac, ben=ben, aaw=aaw, aad=aad)
M = 'As a master\'s graduate, you will show '
ma(1, [], 'a questioning, critical approach', 'generic-skill',
   'A master\'s graduate at threshold will also show a questioning, critical approach.',
   'Master\'s graduates at threshold will also show a questioning and critical approach.',
   M + 'that you question and think critically.', '4.17.b4.1', 'What assumption in your field have you questioned this year?')
ma(2, [], 'capacity for critical reflection', 'generic-skill',
   'A master\'s graduate at threshold will also show the capacity to reflect critically.',
   'Master\'s graduates at threshold will also show a capacity for critical reflection.',
   M + 'that you can reflect critically on your work and ideas.', '4.17.b4.1', 'What did reflecting on that project change in how you work?')
ma(3, [], 'independent thinking and action', 'generic-skill',
   'A master\'s graduate at threshold will also show the capacity to think and act independently.',
   'Master\'s graduates at threshold will also show a capacity for independent thought and action.',
   M + 'that you can think and act on your own.', '4.17.b6', 'Which part of your project did you steer entirely yourself?')
ma(4, [], 'more originality, insight and reflection', 'subject-skill',
   'A master\'s graduate at threshold will also show more originality, insight and critical reflection.',
   'Master\'s graduates at threshold will also show greater originality, insight and critical reflection than at honours.',
   M + 'more originality, insight and critical reflection than at honours.', '4.17.b3', 'What is original in your proposal?')
ma(5, ['synthesise', 'integrate', 'relate'], 'synthesising concepts and relating them to practice', 'subject-skill',
   'A master\'s graduate at threshold will also be able to draw concepts and ideas together and connect them to practice.',
   'Master\'s graduates at threshold will also be able to synthesise and integrate concepts and ideas and relate them to practical contexts.',
   M + 'that you can bring ideas together and connect them to real practice.', '4.17.b3', 'How does the theory you used change what happens on site?')
ma(6, [], 'professional working, roles, ethics and values', 'understanding',
   'A master\'s graduate at threshold will also show a good grasp of how professionals work, their roles and duties, and the ethics and values of practice.',
   'Master\'s graduates at threshold will also show good awareness and understanding of professional practice, roles, responsibilities, ethics and values.',
   M + 'a good grasp of how the profession works: its roles, duties, ethics and values.', '4.17.b8.1', 'What would your responsibilities be on a live project, and to whom?')
ma(7, ['undertaking'], 'professionalism in assignments', 'generic-skill',
   'A master\'s graduate at threshold will also show professionalism in carrying out assignments.',
   'Master\'s graduates at threshold will also show professionalism in undertaking assignments.',
   M + 'professionalism in how you carry out your assignments.', '4.17.b8.1', 'Would a client be happy with how you handled your last assignment?')
ma(8, [], 'alternative methods of retrieval, collection and analysis', 'understanding',
   'A master\'s graduate at threshold will also show understanding of how to use other methods of finding information and collecting and analysing data.',
   'Master\'s graduates at threshold will also understand how to apply other methods for retrieving information and for collecting and analysing data.',
   M + 'that you understand different ways to find information and to collect and analyse data.', '4.17.b2', 'Which other method could have answered your research question, and why did you not use it?')

# ------------------------------------------------------------------ links, themes, levels
GRADE = {'4.6.b1': '4.5.b1', '4.6.b2': '4.5.b2', '4.6.b3': '4.5.b3'}
TH = {'1.25.b1': 'theme:accessibility', '1.25.b2': 'theme:accessibility'}
for _n in range(1, 8):
    TH['1.26.b%d' % _n] = 'theme:esd'

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.11'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.11'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.14; 2.15; 2.19'),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.14; 2.19'),
                  dict(id='fheq:4', role='cites', locator='D1, 2.19 (integrated master\'s, Levels 4 to 7)'),
                  dict(id='fheq:5', role='cites', locator='D1, 2.19 (integrated master\'s, Levels 4 to 7)'),
                  dict(id='fqheis:7', role='cites', locator='D1, 2.17 (FQHEIS Levels 7 to 10)'),
                  dict(id='fqheis:8', role='cites', locator='D1, 2.17; 2.19'),
                  dict(id='fqheis:9', role='cites', locator='D1, 2.17; 2.19'),
                  dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 (honours standards, generic skills)'),
                  dict(id='spine:7', role='refers', locator='std:ref:uk-framework R2 (master\'s standards in 4.7)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.11: degree with honours, FHEQ Level 6; FQHEIS Level 10)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.14: Level 7 (FHEQ) or Level 11 (FQHEIS); 2.19)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.13', '1.15', '1.18', '1.22', '1.23', '1.24', '2.23', '4.4']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.13', '1.15', '1.20', '1.22', '1.25', '2.23', '4.4']),
      dict(id='theme:esd', role='carries', carriedIn=['1.13', '1.15', '1.22', '1.26', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.13', '1.16', '1.20', '1.22', '1.27', '2.10', '4.4']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['3.14', '4.4'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-landscape-architecture-2019-benchmarks (not yet ingested)', note='the fourth edition, 2019, named in the advisory group list (section 6)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the honours classification descriptions providers should refer to (4.3); also the Frameworks named in 4.2'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 4 to 7 (2.11, 2.14, 2.17, 2.19)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 7 to 11 (2.11, 2.14, 2.17, 2.19)'),
      dict(rel='thresholdAt', target='std:ref:uk-framework, spine:6 and spine:7', note='inferred: the honours rungs at spine:6, the master\'s list at spine:7'),
      dict(rel='refersTo', target='Landscape Institute competency framework, code of practice and accreditation criteria (not yet ingested)', note='1.11, 1.15 to 1.17, 2.4 to 2.6'),
      dict(rel='refersTo', target='QAA Quality Code Advice and Guidance on Assessment; QAA Guiding Principles; External Examining Principles (not yet ingested)', note='3.8; 2.27; front matter'),
      dict(rel='readWith', target='std:doc:qaa-advancehe-esd-2021-guidance', note='inferred: listed in section 5 as Education for Sustainable Development Guidance; the sustainability theme (1.26)'),
      dict(rel='readWith', target='std:doc:qaa-enterprise-2018-guidance', note='inferred: listed in section 5; the employability, enterprise and entrepreneurship theme (1.27)')]

SB1 = ['Both a long-standing profession and an academic subject, grounded in research across the arts, humanities and the physical, natural, environmental and social sciences, with analogue and digital representation as tools of analysis and communication (D1, 1.2).',
       'It asks what landscape means, how it forms and changes, how people use it, and how to conserve, restore and manage existing landscapes and create sustainable, resilient, inclusive ones for the future (D1, 1.3).',
       'It works on landscapes of every kind and scale, urban, rural and in between, across assessment, planning, design, management and conservation, and feeds national policy (D1, 1.4, 1.8).',
       'A place-focused discipline linking human and natural systems, sensitive to natural systems, cultural identity and heritage, and the pull between global and local decisions (D1, 1.6).',
       'It sees itself as the profession best placed to lead green infrastructure, making places rich in nature, healthy, thriving, well drained and climate positive (D1, 1.7).',
       'Its definition of landscape comes from the European Landscape Convention, which the UK has signed; the IFLA/UNESCO charter defines the landscape architect\'s role (D1, 1.19, 2.1, 2.2).',
       'Teaching centres on the design studio and on projects of rising scale and complexity that simulate practice, from site survey to specification (D1, 3.3 to 3.6).',
       'The professional route runs through LI accreditation and an accredited master\'s to chartered status (D1, 2.3, 2.15, 2.16).']
SB2 = [dict(theme='theme:edi', inThisSubject='the LI\'s competencies on equality, diversity and inclusivity, its built-environment memorandum and landscape-sector declaration; inclusive curricula and EDI literacy for students; professional conduct with regard to equity, diversity and inclusion and inclusive group work (D1, 1.15, 1.18, 1.23, 1.24; 4.4)',
            statements=['4.4.b36', '4.4.b46', '4.4.b51']),
       dict(theme='theme:accessibility', inThisSubject='the LI competency on inclusive environments; access to studios, resources and fieldwork and alternative forms of teaching and assessment; communication that reaches people with diverse needs; the LI broadening entry routes (D1, 1.15, 1.25, 2.23; 4.4)',
            statements=['1.25.b1', '1.25.b2', '4.4.b46']),
       dict(theme='theme:esd', inThisSubject='named sustainability and education for sustainability: climate, resilience, systems thinking on biodiversity and natural capital, policy, regenerative design, case studies and materiality; creativity in a sustainable context and the sustainability of materials (D1, 1.15, 1.26; 4.4)',
            statements=['1.26.b1', '1.26.b2', '1.26.b3', '1.26.b4', '1.26.b5', '1.26.b6', '1.26.b7', '4.4.b10', '4.4.b11', '4.4.b18']),
       dict(theme='theme:enterprise', inThisSubject='implicit in the LI competencies (practice types, business, contracts, indemnity); courses may offer professional networks, industry standards, ethical practice and CPD; course design reflecting industry and employability (D1, 1.16, 1.27, 2.10; 4.4)',
            statements=['4.4.b39']),
       dict(theme='theme:generative-ai', inThisSubject='generative AI challenges academic integrity and the design process, so openness and critical reflection are central; AI appears among the digital tools students use and in preparing communication (D1, 3.14; 4.4)',
            statements=['4.4.b43', '4.4.b49'])]
SB3 = dict(areas=[dict(component='1.6', gloss='the sensitivities the discipline draws on: natural systems, cultural identity and heritage, global and local decision-making'),
                  dict(component='3.2', gloss='context: global to local; social, cultural, economic and environmental; law and planning policy; history; professional and ethical'),
                  dict(component='3.2', gloss='systems and process: landscape change, protected landscapes, green infrastructure, management, natural capital'),
                  dict(component='3.2', gloss='stakeholders: interdisciplinary working, users and uses, community participation'),
                  dict(component='3.2', gloss='delivery: research methods, site survey, landscape assessment, site design at many scales, masterplanning, placemaking, materials, contract administration, communication')],
           practices=[dict(component='3.3', kind='teaching', gloss='lectures, seminars, design exercises, site visits, tutorials, charettes and group work in a studio culture'),
                      dict(component='3.4', kind='learning', gloss='projects that simulate practice, small and strategic'),
                      dict(component='3.5', kind='teaching', gloss='cumulative projects from survey to management proposals'),
                      dict(component='3.6', kind='learning', gloss='tutorials, critiques, peer discussion in the studio, collaborative projects with other courses or practices'),
                      dict(component='3.7', kind='learning', gloss='placements and visiting practitioners'),
                      dict(component='3.9', kind='assessment', gloss='formative and summative assessment at every level (3.10, 3.11 define them)'),
                      dict(component='3.12', kind='assessment', gloss='portfolios, studio, lab and field work, writing, presentations, digital resources, examinations, a final self-led project, work-integrated assessment'),
                      dict(component='3.13', kind='assessment', gloss='recognition of prior learning'),
                      dict(component='3.14', kind='assessment', gloss='generative AI, integrity and openness')])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.4', award=HON, items=56),
                  dict(rung='threshold', leadIn='4.7', award=MA, items=8),
                  dict(rung='typical', leadIn='4.5', award=HON, items=3),
                  dict(rung='excellent', leadIn='4.6', award=HON, items=3)],
           rungBases='4.1: the threshold is the minimum for the honours award; 4.2: most students exceed it and the statement also describes typical and excellent standards, judged by the provider\'s marking schemes; typical and excellent each build on the whole threshold list (\"listed above\"), so no threshold item is paired with them. Threshold records: 64 in all, 56 honours and 8 master\'s.',
           outcomeLists=[dict(leadIn='1.26', gloss='understanding course content gives students chances to show, for sustainability', items=7, award=['none'])],
           outcomes=[dict(outcome='all outcomes met, with advanced then strong knowledge and skills', threshold='none', typical='4.5.b1', excellent='4.6.b1', basis='inferred', domain='knowledge', award=HON),
                     dict(outcome='reflection, responsibility and autonomy', threshold='none', typical='4.5.b2', excellent='4.6.b2', basis='inferred', domain='generic-skill', award=HON),
                     dict(outcome='application with insight, initiative and problem-solving', threshold='none', typical='4.5.b3', excellent='4.6.b3', basis='inferred', domain='subject-skill', award=HON)])
SB4A_FULL = []
SB5 = [dict(body='Landscape Institute (LI)', says='the royal chartered professional body for the landscape profession in the UK; a statutory consultee on national policy; sets the code of practice and the competency framework (which covers the four themes); accredits undergraduate and postgraduate courses against criteria; accredited courses map to the competency framework; reviews accredited courses through a Professional Review Group; the chartership route needs an accredited 180-credit level 7 master\'s; accredited master\'s graduates become associate members; leads EDI work in the sector (D1, 1.4, 1.9 to 1.12, 1.15 to 1.18, 2.3 to 2.9, 2.15, 2.16, 2.23, 2.28)',
            requirements='not yet ingested: LI competency framework, code of practice and accreditation criteria (Part E)'),
       dict(body='International Federation of Landscape Architects (IFLA)', says='the international federation; does not accredit but sets broad standards for national accreditation; its global ethical principles align with the LI code; its charter with UNESCO defines the profession (D1, 1.9, 1.11, 1.17, 1.19)',
            requirements='not yet ingested: IFLA/UNESCO charter and IFLA Global Ethical Principles (Part E)'),
       dict(body='Royal Town Planning Institute (RTPI)', says='a signatory of the 2022 built-environment EDI memorandum; a body some courses seek dual accreditation from (D1, 1.18, 2.22)', requirements='not yet ingested (Part E)'),
       dict(body='Royal Institute of British Architects (RIBA)', says='a signatory of the 2022 EDI memorandum; a possible second accrediting body (D1, 1.18, 2.22)', requirements='not yet ingested (Part E)'),
       dict(body='Chartered Institute of Building (CIOB); Institution of Civil Engineers (ICE); Royal Institution of Chartered Surveyors (RICS)', says='co-signatories of the 2022 EDI memorandum with the LI (D1, 1.18)', requirements='not-applicable-by-design: named only as signatories'),
       dict(body='Association of Professional Landscapers (APL); British Association of Landscape Industries (BALI); Society of Garden Designers (SGD)', says='joined the LI in a 2022 declaration for a more diverse, inclusive landscape industry (D1, 1.18)', requirements='not-applicable-by-design: named only as signatories')]
SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI)', carriedIn=['1.13', '1.15', '1.18', '1.22', '1.23', '1.24', '2.23', '4.4'], statements=['4.4.b36', '4.4.b46', '4.4.b51']),
                   dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.13', '1.15', '1.20', '1.22', '1.25', '2.23', '4.4'], statements=['1.25.b1', '1.25.b2', '4.4.b46']),
                   dict(id='theme:esd', named='Sustainability; education for sustainability (front matter: education for sustainable development)', carriedIn=['1.13', '1.15', '1.22', '1.26', '4.4'], statements=['1.26.b1', '1.26.b2', '1.26.b3', '1.26.b4', '1.26.b5', '1.26.b6', '1.26.b7', '4.4.b10', '4.4.b11', '4.4.b18']),
                   dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education', carriedIn=['1.13', '1.16', '1.20', '1.22', '1.27', '2.10', '4.4'], statements=['4.4.b39']),
                   dict(id='theme:generative-ai', named='Generative AI', carriedIn=['3.14', '4.4'], statements=['4.4.b43', '4.4.b49'])],
           frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.11', '2.14', '2.17', '2.19', '4.2', '4.3']),
                       dict(framework='scqf', levels=['fqheis:7', 'fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.11', '2.14', '2.17', '2.19'])],
           bodies=[dict(body='Landscape Institute', citedIn=['1.4', '1.9', '1.10', '1.11', '1.12', '1.15', '1.17', '1.18', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.15', '2.16', '2.22', '2.23', '2.28']),
                   dict(body='International Federation of Landscape Architects', citedIn=['1.9', '1.11', '1.17', '1.19']),
                   dict(body='Royal Town Planning Institute', citedIn=['1.18', '2.22']),
                   dict(body='Royal Institute of British Architects', citedIn=['1.18', '2.22']),
                   dict(body='Chartered Institute of Building; Institution of Civil Engineers; Royal Institution of Chartered Surveyors', citedIn=['1.18']),
                   dict(body='Association of Professional Landscapers; British Association of Landscape Industries; Society of Garden Designers', citedIn=['1.18'])],
           sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.3'], role='the four honours classifications providers should refer to'),
                            dict(document='std:doc:qaa-fheq-2024-framework; std:doc:qaa-fqheis-2024-framework', named='the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2', '4.3'], role='marking above threshold in line with provider schemes'),
                            dict(document='OfS Sector Recognised Standards (not ingested; regulator\'s, England)', named='the Office for Students\' Sector Recognised Standards', citedIn=['4.2'], role='standards in use in England'),
                            dict(document='QAA Quality Code Advice and Guidance, Assessment; QAA Guiding Principles (not yet ingested)', named='the QAA Guiding Principles and the Advice and Guidance document on Assessment', citedIn=['3.8'], role='design and delivery of assessment'),
                            dict(document='QAA External Examining Principles (not yet ingested)', named='the principles set out by QAA', citedIn=['2.27'], role='external examination'),
                            dict(document='QAA Glossary (not ingested)', named='QAA\'s Glossary', citedIn=['front matter'], role='explains unfamiliar terms'),
                            dict(document='UN Sustainable Development Goals (external)', named='the UN Sustainability Goals', citedIn=['1.26'], role='illustrate sustainability values and actions'),
                            dict(document='European Landscape Convention (Council of Europe; external)', named='European Landscape Convention (ELC)', citedIn=['2.1', '2.2'], role='definition of landscape; the duty to provide training'),
                            dict(document='IFLA/UNESCO Charter for Landscape Architectural Education (not ingested)', named='IFLA/UNESCO Charter for Landscape Architectural Education', citedIn=['1.19'], role='defines the profession'),
                            dict(document='LI Competency Framework; Professional Code of Practice; Procedures and Guidelines for Higher Education Accreditation; Skills for Greener Places (not yet ingested)', named='as named in the text', citedIn=['1.11', '1.12', '1.15', '1.16', '1.17', '2.5', '2.6'], role='the professional body\'s requirements and context'),
                            dict(document='DEFRA Landscape Review Final Report, 2019 (external)', named='the 2019 Landscape Review of DEFRA', citedIn=['1.5'], role='quoted on the changing countryside'),
                            dict(document='Advance HE inclusive curricula guidance (not ingested)', named='Advance HE', citedIn=['1.23'], role='definition of inclusive curricula and pedagogy')])

B1 = [dict(slug='landscape', definition='an area as people perceive it, whose character comes from natural and human factors acting and interacting, as the European Landscape Convention defines it (D1, 2.1)', beneficiaryDefinition='a place as people see it, shaped by nature and by people together', scopeNote='the statement takes the convention\'s definition', category='unknown', practices=['education', 'landscape architecture']),
      dict(slug='green-infrastructure', definition='the network of green spaces whose principles the profession leads, linking towns and cities with the surrounding landscape (D1, 1.7; 3.2)', beneficiaryDefinition='the connected parks, green spaces and natural features in and around towns', scopeNote='named, not defined, in the text', category='unknown', practices=['landscape architecture']),
      dict(slug='geomatic-information', definition='the acquisition, modelling and analysis of data referenced to location (D1, 4.4)', beneficiaryDefinition='data tied to places on the ground, and how it is gathered and analysed', scopeNote='defined in passing in threshold item 4.4.b19', category='unknown', practices=['landscape architecture']),
      dict(slug='formative-assessment', definition='assessment for development, giving feedback to help learning; it does not count to final marks (D1, 3.10)', beneficiaryDefinition='practice tasks that give you feedback but do not count to your marks', scopeNote='set against summative assessment', category='unknown', practices=['education']),
      dict(slug='summative-assessment', definition='assessment showing how far a learner has met intended outcomes, with marks counting to the final mark (D1, 3.11)', beneficiaryDefinition='assessment that counts towards your marks', scopeNote='uses assessment criteria', category='unknown', practices=['education']),
      dict(slug='recognition-of-prior-learning', definition='entry with credit for learning gained elsewhere, in or outside education (D1, 3.13)', beneficiaryDefinition='getting credit for what you have already learned before you join', scopeNote='also called accreditation of prior learning (APL)', category='unknown', practices=['education']),
      dict(slug='externality', definition='an outside view in quality assurance, through external reviewers and examiners (D1, 2.26, 2.27)', beneficiaryDefinition='people from outside your university checking its courses and marks', scopeNote='', category='unknown', practices=['education']),
      dict(slug='pathway-to-chartership', definition='the LI\'s formal professional qualification route for landscape architects, entered from an accredited master\'s (D1, 2.15)', beneficiaryDefinition='the route to becoming a chartered landscape architect', scopeNote='', category='unknown', practices=['landscape architecture'])]
B2A = [dict(concept='landscape', form='Landscape', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='green-infrastructure', form='green infrastructure', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='geomatic-information', form='geomatic information', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='formative-assessment', form='Formative assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='summative-assessment', form='Summative assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='recognition-of-prior-learning', form='recognition of prior learning (RPL)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='recognition-of-prior-learning', form='accreditation of prior learning (APL)', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
       dict(concept='externality', form='Externality', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='pathway-to-chartership', form='Pathway to Chartership', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []
D3 = [dict(source='Landscape Institute Competency Framework', why='SB5 requirements; the four theme competencies (1.15) and accreditation mapping (2.5)', url='www.landscapeinstitute.org/education/introducing-the-new-entry-standards-and-competency-framework/'),
      dict(source='Landscape Institute (2022) Criteria for Accreditation of Higher Education Programmes; Procedures and guidelines for higher education accreditation', why='SB5 requirements (2.4, 2.6)', url='landscapeinstitute.org (links in section 5)'),
      dict(source='IFLA/UNESCO Charter for Landscape Architectural Education; IFLA Global Ethical Principles', why='SB5 requirements for IFLA (1.11, 1.19)', url='www.iflaworld.com')]

E = [
    'Subject codes inferred (SB-2): the text names no HECoS or CAH code; 100124 landscape architecture and design, CAH13-01-03 landscape design and 100588 landscape studies are inferred from the HESA stores, as are 100197 planning, 100347 ecology and 100864 in statedSubjects; for P3.',
    'Rungs: threshold (4.4, 56 items in seven headed groups), typical (4.5, 3 items) and excellent (4.6, 3 items) for honours, plus a master\'s threshold list (4.7, 8 items, award master\'s, fheq:7). The skeleton\'s count of 64 threshold items is 56 honours plus 8 master\'s.',
    'Pattern differing from Psychology: the threshold lead-in (4.4) has no modal ("demonstrate ... through which they can"); force recorded as threshold with forceFrom 4.1, which defines the threshold as the minimum for the award.',
    'Pattern differing from Psychology: typical (4.5) and excellent (4.6) lead-ins have no modal ("demonstrate they have"); 4.2 says the statement "describes" them, so force is describes, not will. For Abbott.',
    'Pattern differing from Psychology: typical and excellent items build on the whole threshold list ("listed above"), so no gradeOf to a single threshold item; excellent to typical links (4.6.b1 to b3 onto 4.5.b1 to b3) are inferred from their parallel wording, not paired by the issuer.',
    'Pattern: the master\'s list is its own numbered paragraph (4.7), so its ids are 4.7.b1 to b8, not the .masters suffix the batch 1 convention gives to master\'s columns in a table; rung threshold, award master\'s, force will from its lead-in.',
    'Pattern: the threshold list is split by seven sub-headings that the held text runs onto the end of the item before; the skeleton spans for 4.4.b18, b25, b39, b43, b49 and b56, 4.5.b3, 4.6.b3, 1.25.b2 and 1.26.b7 carried the next heading, and the paragraph spans of 2.12, 2.21 and 4.3 a page number or the next heading; all were re-cut with find; 4.4.b17 was re-cut the same way for safety. Domains within the groups are our assignment (intellectual mostly subject-skill; self-management, communication and teamwork generic-skill), for P3.',
    'Typo in the held text: 4.2 reads "typical end excellent standards" (for "and"); kept in source.',
    'Statements cut outside the rungs: 1.25.b1 and b2 (should, provider), 1.26.b1 to b7 (will, course content giving students chances to show understanding), 2.5 (required, read as must), 2.11 (expected, would: describes), 2.12 (will), 2.15 (requires, read as must, a professional body rule), 2.21 (should), 2.26 and 3.3 (will, provider), 3.9 (will), 4.3 (should). Doubtful cuts for P3: 2.26 and 3.3 read like plain provider norms with will; 1.26 is a will on course content rather than an outcome list.',
    'Obliging words outside the five (for Abbott): "expected to" (1.11, 1.17: LI members; 2.11: progression, recorded as describes); "required"/"requires" (1.15, 2.5, 2.15, 2.28); "It is important that" (1.23); "advised" (2.8, 2.21); "encouraged" (2.24, 2.28); "obliged" (2.2, the UK government under the ELC).',
    'Not statements, by rule: 1.15 bullets and 1.11/1.17 are the LI\'s requirements on its members, not on students or courses (recorded in SB5); 2.4 lists the LI\'s accreditation criteria; 2.28 the review group\'s duties; 2.2 the government\'s duty under the ELC.',
    'Plain-present or hedged provider norms, not statements (template open point 5): 2.10 (course design might), 2.25, 2.27 (external examiners typically), 3.2 (courses are likely to address), 3.5 (will often), 3.7 (most courses will offer), 3.8 (assessment aligns), 3.12 (likely to experience), 3.13 (will usually offer RPL), 1.22 (can), 1.27 (might); 4.1 and 4.2 define the rungs and are recorded as lead-ins, not statements.',
    'Level mismatch in the held text: 2.17 gives a four-year integrated undergraduate degree as Levels 3 to 6 (FQHEIS 7 to 10), while 2.19 gives the integrated master\'s as Levels 4 to 7 (FQHEIS 8 to 11). FHEQ defines no Level 3; cqfw:3 would be the nearest shared id. Not recorded as a crosswalk; S5 records only the stated 6 to 10 and 7 to 11 equivalences.',
    'Apprenticeship levels in 2.23 and 2.24 (Level 3 Landscape Technician, Level 6 award, Level 7 Chartered Landscape Professional) name no framework (likely RQF or the apprenticeship levels); not mapped to level ids.',
    'Theme words outside the themes (SB-10): "sustainable" (1.3), "accessible green spaces" (1.5) and "ecological sustainability" (1.19) describe the discipline, not the theme; recorded in SB1, not SB6. Front matter names the four themes (excluded matter).',
    'Generative AI recorded as theme:generative-ai (3.14 and in 4.4.b43, b49), per the batch 1 convention.',
    'Frameworks: FHEQ and FQHEIS cited (FQHEIS by name, filed under scqf); CQFW and SCQF by name not cited. Annex D cited in 4.3 and listed in section 5 as QAA (2019); now in the 2024 Frameworks (std:doc:qaa-fheq-2024-framework).',
    'Generic-skill levels (SB-4): every generic-skill item takes fheq:6 (honours) or fheq:7 (master\'s), both in S5; the descriptor each refines is named in its author-agent-written instruction (qaa/fheq-2024/4.15.* or 4.17.*), with spine:6 or spine:7 from the reference framework; the Annex D third-class cell named for each threshold item is our reading, for P3.',
    'Supersedes: the 2019 fourth edition is named only in the advisory group list (section 6); the front matter lists key changes without its date.',
    'Bodies requirements not yet ingested (SB-9): LI competency framework, code of practice and accreditation criteria; IFLA charter and ethical principles; RTPI and RIBA accreditation (D3).',
    'Verbs: noun-phrase items (4.5.b2, 4.6.b2, 4.7.b1 to b4, b6, b8 and several 1.26 items) carry no verb of their own; verbs recorded as empty rather than borrowed from the lead-in.',
    'S9 commentary not researched in P1.',
]
