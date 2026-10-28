# Judgement for run 0108, QAA Subject Benchmark Statement: Geography (March 2022), std run agent.
# Built by tools/bm_build.py geography-2022 (brief BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
HON = "bachelor's with honours"
IM = "integrated master's"
BOTH = [HON, IM]
CITE = 'QAA, 2022, Geography Subject Benchmark Statement, para '
L6 = 'Hold it at FHEQ Level 6 (FQHEIS Level 10), the honours degree.'
L6IM = ("Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same wording to integrated master's "
        "degrees (4.4), so do not present it as a separate Level 7 standard.")
NOLEVEL = 'It carries no level: it concerns the course or the community, not one stage of study.'


def AAW(what, n, lvl, notc, beside):
    return (f'Describe this as {what}. {lvl} Cite it as {CITE}{n}, and do not claim {notc}. '
            f'Set it beside {beside}.')


def AAD(when, how, q, avoid):
    return f'Bring this up when {when}. Put it {how}, and ask: {q} Avoid {avoid}.'


STAFF = 'as a design or planning question for the programme team'
PLAIN = 'in plain words, in the second person to a student and as a course-design point to staff'

META = dict(
    run='0108', p1='2026-10-03 17:32',
    title='Subject Benchmark Statement: Geography',
    heading='Subject Benchmark Statement: Geography (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current', supersedes='the fourth edition, 2019 (D1, back matter): std:doc:qaa-geography-2019-benchmarks, not held',
    subjects=[dict(scheme='hecos', code='100409', label='geography', basis='inferred'),
              dict(scheme='cah', code='CAH26-01-01', label='geography (non-specific)', basis='inferred')],
    awards=BOTH, levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision (fifth edition for Geography)',
    partsB='partial: no glossary in the document; two terms it defines in passing (geocapabilities, 3.22; reproducibility, 3.27)',
    agentDefinition=('An agent reading this document can tell what a Geography honours graduate (and an integrated master\'s '
                     'graduate, held to the same table) is expected to know and do at three rungs, threshold, typical and '
                     'excellent, across knowledge and understanding, subject-specific skills and generic skills; which skills '
                     'and attributes the subject lists as outcomes; and what the statement asks of courses, above all inclusive, '
                     'safe, low-carbon fieldwork. Each statement carries the issuer\'s text, our paraphrase, a practitioner and a '
                     'student version and two instructions to AI agents, one for writing about the statement and one for '
                     'using it in dialogue.'),
    summary=('The QAA Geography statement (March 2022, fifth edition) covers single honours degrees and integrated '
             'master\'s degrees in Geography across the four UK nations, at FHEQ Level 6 (FQHEIS Level 10), with the '
             'integrated master\'s at FHEQ Level 7 (FQHEIS Level 11). It states its standards in one flattened table under '
             '4.8 with three columns, threshold, typical and excellent, and 22 rows (8 knowledge and understanding, 7 '
             'subject-specific skills, 7 generic skills), summarised in prose at 4.5 to 4.7; four further outcomes that '
             'successful graduates should have developed sit above the table. Section 3 lists subject-specific skills, '
             'generic intellectual skills, generic skills and personal attributes, most of which graduates are able to '
             'show (3.23). Its obligations fall mostly on courses: values and critical theory across the curriculum, '
             'fieldwork throughout the degree, and ethics, risk, inclusivity and carbon assessments before taught '
             'fieldwork. Themes: equity, equality, diversity and inclusion; accessibility; sustainability (ESD); '
             'employability, entrepreneurship and enterprise. Body: the Royal Geographical Society (with IBG). Shared '
             'documents: Annex D of the FHEQ, the ESD guidance and the enterprise guidance.'),
    authority='reference: a sector reference point, not a regulatory requirement; not sector-recognised standards in England, a key reference point in Wales and Scotland, part of quality requirements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs=('what a Geography honours or integrated master\'s graduate is expected to know, understand and be able to do, '
             'and the distinctive features, content and delivery of courses in the subject'),
    awards=BOTH, levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope=('"This document is a QAA Subject Benchmark Statement for Geography that defines what can be expected of a '
                 'graduate in the subject, in terms of what they might know, do and understand at the end of their '
                 'studies." (D1, front matter)'),
    statedSubjects=[
        dict(name='Geography', locator='(D1, front matter; 1.1; 3.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100409', label='geography'), dict(scheme='cah', code='CAH26-01-01', label='geography (non-specific)')]),
        dict(name="BA and BSc degree courses (and MA in Scotland), integrated master's programmes", locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100409', label='geography')]),
        dict(name='physical and human geography (named as the natural and social sides of the subject, not as titles)', locator='(D1, 3.3; 4.5)', kind='specialism',
             codes=[dict(scheme='hecos', code='100410', label='physical geography'), dict(scheme='hecos', code='100478', label='human geography')])])

SECTIONS = {'1': 'Context and purposes of a Geography degree', '2': 'Distinctive features of a Geography degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.2', 'Context'), ('1.3', '1.3', 'Purposes of a Geography degree'),
       ('1.4', '1.4', 'Characteristics of a Geography degree'), ('1.5', '1.9', 'Equity, equality, diversity and inclusion'),
       ('1.10', '1.10', 'Sustainability'), ('1.11', '1.12', 'Entrepreneurship and enterprise education'),
       ('2.1', '2.2', 'Design'), ('2.3', '2.6', 'Accessibility'), ('2.7', '2.10', 'Progression'), ('2.11', '2.13', 'Flexibility'),
       ('2.14', '2.18', 'Partnerships'), ('2.19', '2.21', 'Monitoring and review'),
       ('3.1', '3.12', 'Content: subject knowledge and understanding'), ('3.13', '3.21', 'Fieldwork'),
       ('3.22', '3.24', 'Skills, attributes and geocapabilities'), ('3.25', '3.30', 'Subject-specific skills'),
       ('3.31', '3.34', 'Generic skills and personal attributes'), ('3.35', '3.39', 'Teaching and learning'),
       ('3.40', '3.41', 'Assessment'), ('4.1', '4.8', 'Introduction')]

G = {
    '1.1': 'geography as integrated study of society and environment through scale, place, space and time',
    '1.2': 'an established subject with many routes in; BA, BSc, Scottish MA and integrated master\'s',
    '1.3': 'purposes: holistic thinking across sciences and humanities; STEM and SHAPE; graduates for real challenges',
    '1.4': 'breadth, plural ways of knowing, fieldwork and spatial technologies as defining traits',
    '1.5': 'a shared community duty to build equity and inclusion, beyond legal minimums',
    '1.6': 'colonial roots of the discipline and the duty to counter their legacies',
    '1.7': 'core values of the inclusive community, to run through the whole curriculum',
    '1.8': 'critical theory across the discipline; anticipatory design of learning sites',
    '1.9': 'supportive settings, working with discomfort, care for wellbeing',
    '1.10': 'sustainable development in geography and three ESD principles',
    '1.11': 'behaviours and capabilities for civic life, careers and economic change',
    '1.12': 'graduates\' data skills and their value for enterprise of many kinds',
    '2.1': 'progressive, aligned course design led by experts with student co-production',
    '2.2': 'experiential and theoretical design; overarching concepts that bound the subject',
    '2.3': 'inclusive, equitable design in every part of teaching and assessment',
    '2.4': 'live experiential learning, blended options and accessible resources',
    '2.5': 'students seeing themselves in the curriculum; barriers for some groups',
    '2.6': 'inclusive, affordable fieldwork as a duty on leaders and designers',
    '2.7': 'breadth first, then specialism, placed within the whole discipline',
    '2.8': 'growing critical judgement and independence as students progress',
    '2.9': 'how data collection shapes understanding of the world',
    '2.10': 'course lengths, exit awards and the Scottish four-year honours degree',
    '2.11': 'flexibility as part of an accessible, inclusive course',
    '2.12': 'what a flexible course accommodates and integrates',
    '2.13': 'resourcing flexible material; unequal access to technology',
    '2.14': 'internal and external partnerships and what they give students',
    '2.15': 'equal access to partnerships; partners share equity duties',
    '2.16': 'scales and sectors of partnership; student-centred design',
    '2.17': 'what employers value beyond core geographical skills',
    '2.18': 'learned societies and Chartered Geographer accreditation',
    '2.19': 'monitoring and periodic review by degree-awarding bodies',
    '2.20': 'external reviewers in periodic review',
    '2.21': 'external examiners and threshold standards',
    '3.1': 'single honours courses cover the knowledge areas that follow; others proportionally',
    '3.2': 'what characterises the discipline; four strands of concepts',
    '3.3': 'spatial distributions, change across scales and the effect of scale',
    '3.4': 'how places are made and remade; fieldwork in familiar and unfamiliar places',
    '3.5': 'systems thinking about human and natural worlds',
    '3.6': 'economic, social, cultural, political and environmental patterns; contested scales',
    '3.7': 'drivers of environmental change; energy and matter fluxes',
    '3.8': 'the history of the discipline, colonialism and decolonial practice',
    '3.9': 'representation, mapping and the politics of spatial data',
    '3.10': 'research design, ethics, safety and a range of methodologies',
    '3.11': 'GISci, GIS, remote sensing and statistics',
    '3.12': 'global and local perspectives applied to real problems, with their limits',
    '3.13': 'fieldwork integral to every course',
    '3.14': 'an expansive idea of the field and access to varied fields',
    '3.15': 'fieldwork required throughout the degree and what it develops',
    '3.16': 'collecting and analysing field data; resources needed',
    '3.17': 'virtual fieldwork and its limits',
    '3.18': 'ethical, safe fieldwork; ethics and risk assessments first',
    '3.19': 'inclusive, accessible, fair fieldwork; inclusivity impact assessment',
    '3.20': 'carbon audit and justified destinations',
    '3.21': 'staff training and capacity for fieldwork',
    '3.22': 'learning through geography; geocapabilities defined',
    '3.23': 'graduates show competence in most listed skills and attributes',
    '3.24': 'principles for building skills alongside knowledge',
    '3.25': 'intellectual skills and working across disciplines',
    '3.26': 'evidence, mixed analysis and choice of scale',
    '3.27': 'techniques, data ethics and reproducibility',
    '3.28': 'graduates\' research and data skills and their wider value',
    '3.29': 'resources for spatial data; critical spatial data science',
    '3.30': 'list: subject-specific skills',
    '3.31': 'lead-in to generic skills and attributes',
    '3.32': 'list: generic intellectual skills',
    '3.33': 'list: generic skills',
    '3.34': 'list: personal attributes',
    '3.35': 'innovative and changing teaching contexts',
    '3.36': 'the range of teaching approaches courses use',
    '3.37': 'roles of fieldwork and experiential learning',
    '3.38': 'independent research throughout the degree, often a dissertation',
    '3.39': 'a wide mix of teaching and learning styles',
    '3.40': 'an assessment and feedback strategy',
    '3.41': 'assessment methods students are likely to meet',
    '4.1': 'the threshold as the minimum for honours',
    '4.2': 'most exceed the threshold; refer to Annex D',
    '4.3': 'areas of achievement: knowledge and three kinds of skill',
    '4.4': 'the table covers honours and integrated master\'s; not prescriptive',
    '4.5': 'the threshold graduate in summary',
    '4.6': 'the typical graduate in summary',
    '4.7': 'the excellent graduate in summary',
    '4.8': 'four outcomes for successful graduates, then the rung table',
}
CTYPE = {**{f'3.{n}': 'area' for n in range(2, 13)},
         **{f'3.{n}': 'practice' for n in list(range(13, 22)) + list(range(35, 42))}}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1, S2 and S8'),
    dict(number='section headings 1 to 4', heading='section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7, SB5 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Geography', kind='other: back matter, read for S8 (edition history)'),
]

P = {}


def s(i, **k):
    P[i] = k


# ---------------------------------------------------------------- section 1
s('1.5', type='expectation', rung='none', force='will', level='none', appliesTo='everyone in the geography learning community',
  addressee='both', verbs=['engage', 'reflect', 'change'], about='a shared duty to embed equity and inclusion', domain='none', award='none',
  para=('The subject community has a shared duty, going past legal minimums, to build equity, equality, diversity and inclusion into its '
        'institutions, curricula and teaching, for example by widening participation, countering under-representation, refusing '
        'discrimination and closing awarding gaps; everyone in it will need to engage, reflect and change to meet that duty.'),
  prac=('Treat inclusion as a task for the whole community: staff, students and partners will need to engage, reflect and change, with '
        'concrete work on widening participation, under-represented groups, zero tolerance of harassment, neurodiverse access and awarding gaps.'),
  ben=('As a member of the geography learning community you will be asked to help make it fair and inclusive: to take part, reflect '
       'on your own assumptions and be ready to change.'),
  aaw=AAW('a shared expectation on the whole learning community, carried by "will need to", that everyone engages, reflects and changes to embed equity and inclusion',
          '1.5', NOLEVEL, 'that it is a legal duty under the Equality Act or a measurable student outcome',
          '1.6 to 1.9, the inclusion statements 2.6, 2.15 and 3.19, and the collaboration outcome 4.8.b1'),
  aad=AAD('a student or colleague asks what inclusion means in geography, or a programme team reviews its equity work',
          'in plain words, as something everyone shares rather than a rule for students alone',
          'What have you changed in how you work or study after thinking about who is included? Where do you see gaps in access or awarding on your course?',
          'reading the paragraph aloud, or presenting it to a student as a test they must pass'))
s('1.6', type='requirement', rung='none', force='must', level='none', appliesTo='the geography learning community',
  addressee='both', verbs=['acknowledged', 'countered'], about='acknowledging and countering colonial legacies', domain='none', award='none',
  para=('Because the discipline\'s knowledge grew partly out of colonial science that helped justify empire, its colonial and imperial '
        'legacies of systemic disadvantage, such as racism, classism, ableism, homophobia and patriarchy, must be acknowledged and countered '
        'through a learning community that includes everyone involved.'),
  prac=('Course teams must name and actively work against the colonial roots of geographical knowledge and their present-day legacies of '
        'disadvantage, building a community that includes students, academics, technicians, professional staff, visitors and partners.'),
  ben=('You will look at how geography\'s colonial past still shapes disadvantage today, and you belong to a community that must recognise '
       'and work against those legacies.'),
  aaw=AAW('an obligation (must) on the subject community to acknowledge and counter the colonial and imperial legacies in geography',
          '1.6', 'It carries no level: it binds the subject community at every stage of the degree.',
          'that it prescribes one decolonial curriculum, or that it is a regulatory condition',
          '1.7, 1.8, the knowledge paragraph 3.8 and the history-of-geography row 4.8.b8 with its typical and excellent cells'),
  aad=AAD('a student asks why the course examines geography\'s colonial history, or a team plans decolonising work',
          'plainly and without blame, in the second person for a student and as a curriculum obligation for staff',
          'Where in your modules do you meet the colonial history of the discipline? What would countering its legacies look like in your own work?',
          'lecturing at length from the text or treating it as an optional extra'))
s('1.7', type='expectation', rung='none', force='should', level='none', appliesTo='the geography curriculum',
  addressee='provider', verbs=['integrated'], about='core values across the whole curriculum', domain='none', award='none',
  para=('The inclusive community rests on care for people and places, respect for other views and ways of life, attention to decolonial '
        'demands and solidarity against injustice; these values should run through the whole curriculum rather than sit in single modules or sub-fields.'),
  prac=('Thread care, plural knowledges, respect, decolonial attention and solidarity through every part of the curriculum; they should not '
        'be confined to particular modules or sub-fields.'),
  ben=('n/a', 'a duty on course design; the student meets its effect across modules'),
  aaw=AAW('a curriculum expectation (should) that the subject\'s core values run through every module', '1.7',
          'It sets no level and applies to course design across all years.',
          'that students are assessed on holding these values, or that it is a regulatory rule', '1.6, 1.8 and the reflection outcome 4.8.b2'),
  aad=AAD('a programme team maps where values such as care and solidarity appear in its curriculum', STAFF,
          'Which modules carry these values, and which leave them out? Would a student meet them in every year?',
          'giving it to a student as a requirement on them'))
s('1.8', type='expectation', rung='none', force='should', level='none', appliesTo='the geography curriculum',
  addressee='provider', verbs=['applied'], about='critical theory across the discipline', domain='none', award='none',
  para=('The core values favour curricula that build critical thinking from progressive theory, among them critical race theory, '
        'decoloniality, disability, feminist and queer studies and science and technology studies; critical theory should be applied across '
        'geography, and the values also favour design that anticipates the barriers of each learning site, fieldwork and laboratories above all.'),
  prac=('Apply critical theory across every branch of the course, not only in human geography, and plan each learning site, whether online, in a classroom, '
        'outdoors or in a laboratory, with its likely barriers anticipated.'),
  ben=('n/a', 'a duty on course design'),
  aaw=AAW('a curriculum expectation (should) that critical theory is applied across the whole discipline', '1.8',
          'It sets no level; it shapes design throughout the degree.',
          'that its list of theories is closed, since the issuer says it is not limited', '1.7, 1.9 and the fieldwork access statements 2.6 and 3.19'),
  aad=AAD('a team asks whether physical geography modules need critical theory too, or plans inclusive laboratory or field teaching', STAFF,
          'Where does critical theory appear in your physical and quantitative modules? Which learning sites have you checked for barriers?',
          'putting it to a student as an obligation'))
s('1.12', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['collect', 'analyse', 'manipulate', 'solve', 'gather', 'evaluate'], about='data skills for innovation and enterprise',
  domain='subject-skill', award=HON,
  para=('Graduates will be able to gather, analyse and handle varied numerical and qualitative data; their spatial analysis, crossing scales '
        'and disciplines, lets them tackle complex social and economic problems and use evidence for innovation and decisions, and they '
        'see the worth of alternative economies and of green, social and digital entrepreneurship.'),
  prac=('Graduates will collect, analyse and work with quantitative and qualitative data, bring spatial analysis across scales and '
        'disciplines to complex social and economic problems, and use evidence to inform innovation and decisions, understanding green, '
        'social and digital enterprise.'),
  ben=('You will be able to collect, analyse and work with both numerical and qualitative data, use your spatial thinking to help solve '
       'complex social and economic problems, and understand different kinds of enterprise, including green, social and digital ones.'),
  aaw=AAW('an outcome graduates will reach ("are able to"), placed in the enterprise and entrepreneurship section', '1.12', L6,
          'that every graduate must be an entrepreneur, or that it adds a separate enterprise requirement',
          'the attribute 3.34.b3, the analysis row 4.8.b15, qaa/fheq-2024/4.15.b9.2 and spine:6'),
  aad=AAD('a student asks how geography skills lead to work or enterprise, or a team plans employability content', PLAIN,
          'Which data have you collected and analysed yourself? Where could that work help a business, charity or public body decide something?',
          'implying that only commercial enterprise counts, since social and environmental value count too'))

# ---------------------------------------------------------------- section 2
s('2.1', type='expectation', rung='none', force='should', level='none', appliesTo='Geography courses',
  addressee='provider', verbs=['built'], about='progressive, aligned course design', domain='none', award=BOTH,
  para=('Geography degrees aim at an integrative education; courses should rest on learning outcomes that grow in complexity and match '
        'teaching and assessment, with design led by subject experts and shaped by student engagement and co-creation.'),
  prac=('Design the course so its outcomes rise in complexity year on year and line up with how you teach and assess, and involve students '
        'in reviewing and co-producing the design.'),
  ben=('n/a', 'a duty on course design'),
  aaw=AAW('a course-design expectation (should): outcomes of rising complexity aligned with teaching and assessment', '2.1',
          'It spans the whole degree, up to FHEQ Level 6 (FQHEIS Level 10), or Level 7 for the integrated master\'s.',
          'that it fixes outcomes for any one year', '2.7 and 2.8 on progression, 3.40 on assessment, and qaa/fheq-2024/4.15.b1'),
  aad=AAD('a programme team plans outcomes across the years or checks alignment', STAFF,
          'Do your outcomes get harder each year? Does each assessment test the outcome it claims to?', 'giving it to a student as a duty'))
s('2.6', type='expectation', rung='none', force='should', level='none', appliesTo='fieldwork leaders and course designers',
  addressee='provider', verbs=['recognised', 'implementing', 'ensure'], about='inclusive and affordable fieldwork', domain='none', award='none',
  para=('Fieldwork needs access to many kinds of field; essential as it is, students\' individual needs during fieldwork should be '
        'recognised, fieldwork leaders are responsible for anticipatory design so that no field site excludes anyone on any protected '
        'characteristic, class, gender identity or neurodiversity and facilities suffice, and designers need to stop the extra costs of '
        'travel, clothing and kit from barring anyone.'),
  prac=('Recognise students\' individual needs in the field; fieldwork leaders are responsible for anticipating barriers of any protected '
        'characteristic, class, gender identity or neurodiversity and for adequate facilities, and course designers need to keep extra '
        'fieldwork, clothing or equipment costs from excluding anyone.'),
  ben=('n/a', 'a duty on fieldwork leaders and course designers; the student meets its effect'),
  aaw=AAW('a provider duty (should, with "responsible for" and "need to" beside it) to make fieldwork inclusive and affordable', '2.6',
          'It sets no level and applies to all fieldwork in the degree.',
          'that it lets a course drop fieldwork, which the issuer calls essential', '3.15, 3.18, 3.19, 3.20 and 1.8 on anticipatory design'),
  aad=AAD('a team plans a field trip or a student raises a barrier to taking part',
          'with staff as a planning duty, and with a student only to reassure them that removing barriers falls to the course',
          'What barriers of cost, access or identity could this trip create? Who would carry the extra cost?',
          'presenting it to a student as their duty'))
s('2.7', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students at the end of the course',
  addressee='learner', verbs=['situate'], about='placing a specialism within the wider discipline', domain='understanding', award=BOTH,
  para=('Study grows more specialised as the degree goes on, after a broad first grounding; by the end, students will be able to place '
        'their chosen specialisms within a wider grasp of geography, its approach, history and theory, and applicants need clear information '
        'on what each course offers.'),
  prac=('Build breadth early and specialism later, so that by the end students will situate their specialism within geography\'s wider '
        'approach, history and theory; tell applicants clearly what is distinctive about your course.'),
  ben=('Your degree will start broad and let you specialise later; by the end you will be able to show how your specialism fits into '
       'geography as a whole, including its history and theory.'),
  aaw=AAW('an end-of-course outcome ("are able to") about placing a specialism within the discipline', '2.7',
          'Hold it at FHEQ Level 6 (FQHEIS Level 10), and for the integrated master\'s at the end of that course.',
          'that it fixes which specialism a student must choose', '2.8, the history row 4.8.b8, qaa/fheq-2024/4.15.b1 and spine:6'),
  aad=AAD('a student is choosing options or a final-year project, or a team reviews breadth against specialism', PLAIN,
          'How does your chosen specialism connect to the rest of geography? Which wider debates does it draw on?',
          'treating specialisation as a reason to drop breadth'))
s('2.8', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students as they progress',
  addressee='learner', verbs=['evaluate', 'make', 'demonstrate', 'undertake'], about='growing critical judgement and independence',
  domain='subject-skill', award=BOTH,
  para=('As they progress, students are able to judge evidence and the value of their sources with growing sophistication; they will have '
        'chances to show deeper critical reflection and will show a growing capacity to carry out fieldwork or projects on their own with '
        'primary or secondary data.'),
  prac=('Plan for growth: students will evaluate evidence and sources with rising sophistication, will be given chances to show deeper '
        'critical reflection, and will take on fieldwork or projects with increasing independence.'),
  ben=('As you move through your degree you will judge evidence and sources more critically, and you will be able to plan and carry out '
       'fieldwork or projects more and more on your own.'),
  aaw=AAW('a progression outcome ("are able to", "will"): rising critical evaluation and independence in fieldwork or projects', '2.8',
          'Read it across the years of the degree up to FHEQ Level 6 (FQHEIS Level 10).',
          'that full independence is expected from the first year', '2.7, 2.9, the independent study row 4.8.b24 and qaa/fheq-2024/4.15.b5'),
  aad=AAD('a student asks how expectations change between years, or a team checks progression in fieldwork', PLAIN,
          'How much of your last fieldwork or project did you plan yourself? How do you now judge whether a source is reliable?',
          'expecting final-year independence from a first-year student'))
s('2.9', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students as they progress, and their courses',
  addressee='both', verbs=['develop'], about='how collecting data shapes knowledge of the world', domain='understanding', award=BOTH,
  para=('As they progress, students should come to understand more fully how the epistemology of collecting primary data affects what we '
        'take the world to be, and should have chances to grasp better how data relate to the real world and to geographical knowledge.'),
  prac=('Give students chances, as they progress, to see how collecting primary data shapes knowledge of the world and how data relate to '
        'reality; students should deepen this understanding over the course.'),
  ben='As you progress, you should come to understand how the way data are collected shapes what we think we know about the world.',
  aaw=AAW('a progression expectation (should) on students\' understanding of data and knowledge, with a matching duty on the course to give chances', '2.9',
          'Read it across the degree up to FHEQ Level 6 (FQHEIS Level 10).',
          'that it is a rung standard or that it concerns quantitative work alone', '2.8, 3.15, the epistemology row 4.8.b10 and the accuracy row 4.8.b12'),
  aad=AAD('a student reflects on fieldwork data or a team plans a methods module', PLAIN,
          'How did the way you collected your data shape what you concluded? What could a different method have shown?',
          'heavy philosophical terms without examples'))
s('2.13', type='expectation', rung='none', force='should', level='none', appliesTo='course design and resourcing',
  addressee='provider', verbs=['reflect', 'ensuring'], about='resourcing flexible material and unequal access to technology', domain='none', award='none',
  para=('Accessible, inclusive and flexible material needs extra resources to keep quality high, and design should allow for students\' '
        'unequal access to technology so that flexibility does not cause harm nobody planned.'),
  prac=('Resource flexible and accessible materials properly, and design them to work for students with limited devices or connectivity, '
        'so that flexibility does not backfire.'),
  ben=('n/a', 'a duty on course design and resourcing'),
  aaw=AAW('a provider expectation (should) on resourcing flexible delivery and allowing for unequal access to technology', '2.13',
          'It sets no level and applies across the course.', 'that it requires any particular platform', '2.3, 2.11, 2.12 and 3.40'),
  aad=AAD('a team moves teaching online or blends delivery', STAFF,
          'Which students lack reliable devices or internet? What happens to them if a task is online only?', 'putting the duty on students'))
s('2.15', type='expectation', rung='none', force='should', level='none', appliesTo='institutions',
  addressee='provider', verbs=['ensure'], about='equal access to partnerships', domain='none', award='none',
  para=('Institutions should make sure every student has an equal chance to take part in partnerships where relevant; partnerships inside '
        'the institution, such as societies and work across departments, count as much as external ones, and partners take on the same equity duties.'),
  prac=('Make partnership opportunities, from placements and projects to student societies, equally open to all students, and brief partners '
        'on the equity, equality, diversity and inclusion principles they share with you.'),
  ben=('n/a', 'a duty on the institution'),
  aaw=AAW('an institutional expectation (should) of equal access to partnerships', '2.15', 'It sets no level.',
          'that every student is guaranteed a placement', '2.14, 2.16, 2.17 and 1.5'),
  aad=AAD('a team plans placements or partner projects, or a student asks why they could not join one',
          'as a duty on the institution, and to a student as what they may fairly expect',
          'Who has taken up partnership opportunities so far, and who has not? What stops some students taking part?',
          'telling a student they must find their own partnership'))
s('2.16', type='expectation', rung='none', force='should', level='none', appliesTo='partnership activities',
  addressee='provider', verbs=['designed'], about='student-centred partnership activities', domain='none', award='none',
  para=('Partnerships may cross disciplines, institutions and sectors and may be brief or lasting; they should be designed around students '
        'and help them understand the subject beyond their studies.'),
  prac='Design every partnership activity, brief or lasting, around the student and around understanding geography outside the university.',
  ben=('n/a', 'a duty on course design'),
  aaw=AAW('a design expectation (should) for partnership activities', '2.16', 'It sets no level.',
          'that partnerships are compulsory', '2.14, 2.15 and 2.17'),
  aad=AAD('a team designs a placement or partner project', STAFF,
          'Who gains most from this partnership as designed? What will students learn about geography outside academia?',
          'giving it to a student as a requirement'))
s('2.20', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review',
  addressee='provider', verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para=('Externality is essential to UK quality assurance; providers will use external reviewers in periodic review to get an outside view '
        'of proposed changes and to check that threshold standards are met and content suits the subject.'),
  prac='Bring external reviewers into periodic review to test proposed changes, confirm threshold standards are met and check the content fits geography.',
  ben=('n/a', 'a duty on the provider in quality assurance'),
  aaw=AAW('a provider expectation (will) to use external reviewers in periodic review', '2.20',
          'It sets no level; it concerns review of the whole course.',
          'that it sets the review cycle or replaces external examining', '2.19, 2.21 and the threshold definition 4.1'),
  aad=AAD('a team prepares for periodic review', STAFF,
          'Who will act as external reviewer, and what will they check against? Which threshold standards might they question?',
          'raising it with students as their duty'))

# ---------------------------------------------------------------- section 3: paragraphs
s('3.3', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['demonstrate', 'evaluate'], about='spatial distributions and change across scales', domain='knowledge', award=HON,
  para=('Graduates will be able to show knowledge and explanation of how physical and human phenomena are distributed in space; they grasp '
        'change at different scales of time and space, judge the processes shaping past, present and future geographies, and see how the '
        'chosen scale affects conclusions.'),
  prac=('Graduates will show knowledge and explanation of spatial distributions in physical and human phenomena, understand rates of change '
        'across scales, evaluate the processes behind past, present and future geographies, and recognise how scale shapes conclusions.'),
  ben=('You will be able to explain where physical and human things are found and why, how they change over time and space, and how the '
       'scale you study at affects what you conclude.'),
  aaw=AAW('a knowledge outcome ("are able to") on spatial distributions and scale', '3.3', L6,
          'that it lists every topic a course must teach', '3.5, the rows 4.8.b5 and 4.8.b6 with their typical and excellent cells, and qaa/fheq-2024/4.15.b1'),
  aad=AAD('a student revises core ideas or asks what scale means in geography', PLAIN,
          'Can you explain why something you studied is found where it is? Would your conclusion change at a different scale?',
          'a list of definitions without an example'))
s('3.5', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['use', 'conceptualise'], about='systems thinking about human and natural worlds', domain='understanding', award=HON,
  para=('Graduates will be able to use systems thinking to frame patterns, processes, interactions and change critically in a world of '
        'people, biodiversity and geodiversity, taking in environmental effects on people, human effects on natural and climate systems, '
        'and environmental management.'),
  prac=('Graduates will apply a systems framework to think critically about patterns, processes and change, taking in environmental impacts '
        'on people, human impacts on biophysical and climate systems, and the management of environments.'),
  ben=('You will be able to use systems thinking to understand how people and the natural world affect each other, climate included, and '
       'how environments are managed.'),
  aaw=AAW('an outcome ("are able to") on systems thinking', '3.5', L6,
          'that it belongs to physical geography alone', '3.3, the reciprocal relationships row 4.8.b6 and qaa/fheq-2024/4.15.b3.1'),
  aad=AAD('a student links human and physical topics, or plans an integrated project', PLAIN,
          'What are the parts of the system you studied, and how do they affect each other? Where do people fit in it?',
          'systems jargon without a real case'))
s('3.15', type='requirement', rung='none', force='must', level='none', appliesTo='Geography degrees and their students',
  addressee='both', verbs=['required'], about='fieldwork through the whole degree', domain='none', award=BOTH,
  para=('Fieldwork, mixing directed, peer and self-directed learning with extended time in the field including multi-day and residential '
        'trips, is required across the whole degree so that core skills can progress, often ending in self-directed fieldwork; it builds '
        'teamwork, problem-based learning, research design, data handling, resilience and the handling of risk, and it alone links the real '
        'world to its measurement in spatial data.'),
  prac=('Include fieldwork at every stage of the degree, with extended and residential time in the field, so that core skills progress, '
        'typically to self-directed fieldwork by the end; this is a requirement, not an option.'),
  ben='You will do fieldwork throughout your degree, including longer and residential trips, building up to planning your own fieldwork by the end.',
  aaw=AAW('a course requirement ("required", read as must) that fieldwork runs through the whole degree', '3.15',
          'It holds across all years of the honours degree and the integrated master\'s.',
          'that virtual fieldwork can fully replace it, since the issuer says many kinds cannot be replicated (3.17)',
          '3.13, 3.14, 3.16 to 3.21 and the field research row 4.8.b13'),
  aad=AAD('a student asks why fieldwork is compulsory, or a team considers cutting field days',
          'plainly to a student and as a firm requirement to staff',
          'What skills did your last fieldwork build that a classroom could not? How does your fieldwork get more independent each year?',
          'suggesting a course may drop fieldwork'))
s('3.18', type='expectation', rung='none', force='should', level='none', appliesTo='those who plan and run taught fieldwork',
  addressee='provider', verbs=['planned', 'conducted', 'undertaken'], about='ethics and risk assessment before fieldwork', domain='none', award='none',
  para=('Fieldwork invites reflection on positionality, responsibility and relationships, so all fieldwork should be planned and run '
        'ethically, responsibly, carefully and safely for everyone involved, with an ethics assessment and a risk assessment before any taught fieldwork.'),
  prac=('Complete an ethics assessment and a risk assessment before every taught field trip, and plan it to be ethical, responsible, careful '
        'and safe for students, staff, the communities visited and other stakeholders.'),
  ben=('n/a', 'a duty on those who plan fieldwork; the student meets its effect'),
  aaw=AAW('a provider expectation (should) that every taught field trip has ethics and risk assessments first', '3.18', 'It sets no level.',
          'that students carry this duty on taught trips', '3.19, 3.20, 2.6 and the subject skill 3.30.b2'),
  aad=AAD('a team plans a trip, or a student asks how fieldwork safety is handled', STAFF,
          'Has the ethics assessment considered the communities you will visit? Who signs off the risk assessment?',
          'giving the assessment duty to students on taught trips'))
s('3.19', type='expectation', rung='none', force='should', level='none', appliesTo='those who plan fieldwork, and providers',
  addressee='provider', verbs=['planned', 'conducted', 'consider', 'undertaken'], about='inclusive, accessible and fair fieldwork', domain='none', award='none',
  para=('Fieldwork should be planned and run to be inclusive and accessible, minding students\' and staff\'s wellbeing and all protected '
        'characteristics; opportunities should be fair, providers should, as far as they can, fund their way round cost and other barriers, '
        'and an inclusivity impact assessment should come before all taught fieldwork.'),
  prac=('Plan every field trip for inclusion and access, mental and physical health included; fund ways round cost barriers where you can, '
        'and complete an inclusivity impact assessment beforehand.'),
  ben=('n/a', 'a duty on the provider and fieldwork planners'),
  aaw=AAW('a provider expectation (should) of inclusive, accessible and fair fieldwork, with an inclusivity impact assessment', '3.19',
          'It sets no level.', 'that the provider must meet every cost, since the issuer says to the extent possible', '2.6, 3.18, 3.20 and 1.5'),
  aad=AAD('a team plans fieldwork or a student cannot afford or reach a trip',
          'as a planning duty, and to a student as what they can fairly ask the course for',
          'What would stop a student joining this trip? What did the inclusivity assessment find?',
          'implying the student must solve access barriers alone'))
s('3.20', type='expectation', rung='none', force='should', level='none', appliesTo='those who plan taught fieldwork',
  addressee='provider', verbs=['considered', 'justified', 'balance'], about='carbon audit and justified destinations', domain='none', award='none',
  para=('The environmental impact and carbon footprint of fieldwork should be weighed through a carbon audit before all taught fieldwork; '
        'destinations and transport should be justified by programme outcomes, setting environmental cost against the learning and other gains '
        'of studying in a place.'),
  prac='Run a carbon audit before each taught trip and justify the destination and travel by the outcomes they serve, weighing carbon cost against learning gains.',
  ben=('n/a', 'a duty on fieldwork planners'),
  aaw=AAW('a provider expectation (should) to audit and justify the carbon cost of fieldwork', '3.20', 'It sets no level.',
          'that distant fieldwork is ruled out', '3.17 on virtual fieldwork, 3.18, 3.19 and std:doc:qaa-advancehe-esd-2021-guidance'),
  aad=AAD('a team chooses a field destination or a student asks about the environmental cost of trips', STAFF,
          'What did the carbon audit show? Which outcomes need this destination rather than a nearer one?', 'putting the audit on students'))
s('3.21', type='requirement', rung='none', force='must', level='none', appliesTo='the provider as employer of fieldwork staff',
  addressee='provider', verbs=['ensure', 'recognise'], about='training and capacity of fieldwork staff', domain='none', award='none',
  para=('Staff carry heavy responsibility in taught fieldwork; the provider\'s resourcing should make sure they are fully trained and '
        'supported, and employers must recognise that staff differ in their capacity to lead or join fieldwork.'),
  prac='Resource and train fieldwork staff fully; as employer you must recognise that colleagues differ in how far they can lead or take part in fieldwork.',
  ben=('n/a', 'a duty on the provider as employer'),
  aaw=AAW('a duty on the provider as employer: training and support (should) and recognition of staff capacity (must)', '3.21',
          'It sets no level.', 'that it sets staffing ratios', '3.18, 3.19 and 2.6'),
  aad=AAD('a department plans fieldwork staffing', 'as an employer and workload question for staff',
          'Who is trained to lead this trip? Have colleagues been able to say what they can take on?', 'raising it with students as their concern'))
s('3.26', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['use', 'apply', 'making', 'establish'], about='mixed analysis of evidence and choice of scale', domain='subject-skill', award=HON,
  para=('Graduates will be able to draw on varied evidence and apply suitable quantitative and qualitative analysis, judging soundly from '
        'what the evidence shows; they are numerate and can set the right space and time scales for their analysis.'),
  prac=('Graduates will use varied evidence, apply suitable quantitative and qualitative analysis, make informed judgements from it and choose '
        'suitable scales in space and time; they are numerate.'),
  ben=('You will be able to use many kinds of evidence, analyse it with numbers and with qualitative methods, judge soundly from it, and '
       'choose the right scale in space and time for your analysis.'),
  aaw=AAW('an outcome ("are able to") on evidence, mixed analysis and scale', '3.26', L6,
          'that it fixes particular techniques', '3.27, 3.28, the analysis row 4.8.b15 and qaa/fheq-2024/4.15.b2'),
  aad=AAD('a student plans an analysis or a dissertation method', PLAIN,
          'Why did you choose that method and that scale? What would the evidence not let you conclude?', 'presenting one method as always right'))
s('3.39', type='expectation', rung='none', force='will', level='none', appliesTo='honours degree courses in Geography',
  addressee='provider', verbs=['vary', 'have'], about='a wide range of teaching and learning styles', domain='none', award=HON,
  para=('The mix of teaching, learning and assessment differs between providers with their missions and aims, but geography honours courses '
        'will typically use a wide range of learning and teaching styles, fitting a subject that spans environment and society.'),
  prac='Use a wide range of teaching and learning styles, fitted to your mission and aims, as a subject spanning environment and society calls for.',
  ben=('n/a', 'a statement about course design'),
  aaw=AAW('an expectation (will, "characteristically") that honours courses use a wide range of teaching and learning styles', '3.39',
          'It sets no level.', 'that it prescribes particular methods', '3.35 to 3.38 and 3.40'),
  aad=AAD('a team reviews its teaching mix', STAFF,
          'Which styles does the course rely on most? Which learners might that leave behind?', 'giving it to a student as a duty'))
s('3.40', type='expectation', rung='none', force='will', level='none', appliesTo='the course\'s assessment and feedback strategy',
  addressee='provider', verbs=['allow', 'demonstrate', 'reflect', 'discuss'], about='an assessment and feedback strategy for every student',
  domain='none', award=BOTH,
  para=('An assessment and feedback strategy will let every student show what they have attained and reflect on and talk about their '
        'progress; each method has clear, aligned aims, requirements and criteria, formative work, self and peer review and authentic tasks '
        'are valued, and a mix of accessible methods is offered, sometimes with a choice of format.'),
  prac=('Build an assessment and feedback strategy that lets every student show their attainment and reflect on their progress, with clearly '
        'aligned aims and criteria for each method, formative and authentic tasks, self and peer review, and a mix of accessible formats.'),
  ben=('n/a', 'a duty on assessment design; the student meets it as varied, clearly explained assessment'),
  aaw=AAW('an expectation (will) on the course\'s assessment and feedback strategy', '3.40', 'It spans the whole degree.',
          'that it fixes assessment types or weightings', '3.41, 2.1 and the classification descriptions qaa/fheq-2024/annex-d'),
  aad=AAD('a team redesigns assessment or a student asks why formats vary', STAFF,
          'Can every student show what they know in at least one format that suits them? Are criteria clear before the task starts?',
          'presenting it to a student as their obligation'))

# ---------------------------------------------------------------- section 3: skill and attribute lists (lead-in 3.23: graduates "are able to" show most)
LISTS = {
    '3.30': ('subject-specific skills', 'subject-skill', 'a student plans fieldwork, a methods module or a dissertation'),
    '3.32': ('generic intellectual skills', 'generic-skill', 'a student reflects on how they think and argue, or a team maps intellectual skills'),
    '3.33': ('generic skills', 'generic-skill', 'a student prepares for work or reviews their study skills'),
    '3.34': ('personal attributes', 'generic-skill', 'a student reflects on personal development or prepares for applications'),
}


def li(i, gist, verbs, about, q, beside):
    stem = i.rsplit('.b', 1)[0]
    kind, dom, when = LISTS[stem]
    s(i, type='outcome', rung='none', force='will', forceFrom='3.23', level='fheq:6', appliesTo='graduates of the subject',
      addressee='learner', verbs=verbs, about=about, domain=dom, award=BOTH,
      para=f'Will be able to show {gist}, one of the {kind} listed, most of which graduates are able to show.',
      prac=f'Graduates will show {gist}; this is one of the {kind} listed, and graduates are expected to show most of them, not every one.',
      ben=f'You will develop {gist}; you are expected to show most, though not necessarily all, of the {kind} in this list.',
      aaw=(f'Describe this as one item in a list of {kind}, most of which graduates are able to show (3.23), so treat it as a broad '
           f'expectation rather than a rule for each item. {L6IM.replace("(4.4)", "(3.1)")} Cite it as {CITE}{stem}, and do not claim that '
           f'every graduate must show it. Set it beside {beside}.'),
      aad=(f'Bring this up when {when}. Put it plainly, in the second person for a student, and ask: {q} Avoid reading the whole list '
           f'aloud or implying that every item must be mastered.'))


li('3.30.b1', 'spatial awareness and careful observation', [], 'spatial awareness and observation',
   'What did you notice on your last field visit that a map would not show?', 'the field research row 4.8.b13 and qaa/fheq-2024/4.15.b2')
li('3.30.b2', 'the ability to spot the moral, ethical and safety questions in every part of geographical enquiry', ['recognising'],
   'ethics and safety in enquiry', 'What ethical or safety question did your last project raise, and how did you handle it?', '3.18, the positionality row 4.8.b21 and qaa/fheq-2024/4.15.b4')
li('3.30.b3', 'skill in carrying out fieldwork and collecting data while judging risks and how to reduce them', ['conducting', 'assessing'],
   'fieldwork, data collection and risk', 'What risks did you identify before your fieldwork, and what did you do about them?', '3.15, the row 4.8.b13 and qaa/fheq-2024/4.15.b6')
li('3.30.b4', 'skill with interpretative methods such as participant observation, ethnographic interviews and auto-ethnography', ['employing'],
   'interpretative methods', 'Which interpretative method have you used, and what did it let you see?', 'the collection row 4.8.b14 and qaa/fheq-2024/4.15.b2')
li('3.30.b5', 'skill with social survey methods such as questionnaires and semi-structured interviews', ['employing'],
   'social survey methods', 'How did you design your questions, and what would you change next time?', 'the collection row 4.8.b14 and qaa/fheq-2024/4.15.b2')
li('3.30.b6', 'laboratory skills such as preparing and analysing soil, water and sediment samples', ['employing'],
   'laboratory skills and methods', 'Which laboratory procedure can you run without help, and how do you check your results?', 'the analysis row 4.8.b16 and qaa/fheq-2024/annex-d/practical/r3/3rd')
li('3.30.b7', 'skill in generating, collecting and recording primary data and using secondary data sets, numerical and qualitative', [],
   'primary and secondary data', 'When did you choose existing data over collecting your own, and why?', 'the collection row 4.8.b14 and qaa/fheq-2024/4.15.b5')
li('3.30.b8', 'critical judgement, interpretation and combination of kinds of geographical evidence, from texts and archives to maps and laboratory data',
   ['evaluating', 'interpreting', 'combining'], 'evaluating and combining kinds of evidence',
   'How did you weigh two sources that pointed different ways?', 'the synthesis row 4.8.b17 and qaa/fheq-2024/4.15.b7')
li('3.30.b9', 'analysis and problem-solving with numerical and qualitative methods', [], 'analysis and problem-solving',
   'Which problem have you solved with data, and which method did you use?', 'the analysis row 4.8.b15 and qaa/fheq-2024/4.15.b3.1')
li('3.30.b10', 'collecting and analysing spatial and environmental information with tools such as GIS, remote sensing and statistical or mathematical models',
   ['applying', 'using'], 'spatial and environmental information methods', 'Which spatial tool are you most confident with, and what are its limits?',
   'the rows 4.8.b16 and 4.8.b23 and qaa/fheq-2024/4.15.b2')
li('3.30.b11', 'skill in making clear, effective maps, diagrams and visualisations', ['preparing'], 'maps, diagrams and visualisations',
   'Who was your last map for, and did it work for them?', 'the presentation row 4.8.b18 and qaa/fheq-2024/annex-d/practical/r4/3rd')

li('3.32.b1', 'skill in weighing up contrasting theories and explanations', ['assessing'], 'weighing contrasting theories',
   'Which two explanations of the same thing have you compared, and which convinced you?', 'the views row 4.8.b20 and qaa/fheq-2024/4.15.b7')
li('3.32.b2', 'awareness of the social, cultural and political settings in which knowledge is made, of the positions of researcher and researched, and of widening who makes knowledge',
   [], 'the politics and positionality of knowledge', 'Whose knowledge counted in your last project, and whose was missing?', 'the positionality row 4.8.b21, 3.8 and qaa/fheq-2024/4.15.b4')
li('3.32.b3', 'an understanding of how to use evidence and data properly and ethically', ['understanding'], 'ethical use of evidence and data',
   'When might using a data set be legal but still unethical?', '3.27, the accuracy row 4.8.b12 and qaa/fheq-2024/4.15.b7')
li('3.32.b4', 'skill in planning, designing and carrying out rigorous research alone and in groups, through to a final report', ['planning', 'designing', 'executing'],
   'planning and carrying out research', 'Which part of your research did you plan alone, and which with others?', '3.38, the field research row 4.8.b13 and qaa/fheq-2024/4.15.b6')
li('3.32.b5', 'numeracy and statistical literacy', [], 'numeracy and statistical literacy',
   'Can you explain what a statistical result in your work means in plain words?', 'the analysis row 4.8.b15 and qaa/fheq-2024/annex-d/transferable/r1/3rd')
li('3.32.b6', 'skill in abstracting and synthesising information', [], 'abstraction and synthesis',
   'Can you sum up a long reading in three points of your own?', 'the synthesis row 4.8.b17 and qaa/fheq-2024/annex-d/cognitive/r1/3rd')
li('3.32.b7', 'skill in building a reasoned argument', ['developing'], 'reasoned argument',
   'What is the main claim of your current essay, and what evidence carries it?', 'the argument row 4.8.b22 and qaa/fheq-2024/annex-d/cognitive/r2/3rd')
li('3.32.b8', 'responsibility for learning and reflection on that learning', ['taking'], 'responsibility for and reflection on learning',
   'What did you learn from your last piece of feedback, and what did you change?', 'the reflection row 4.8.b26 and qaa/fheq-2024/4.15.b5')

li('3.33.b1', 'effective study, autonomous learning and awareness of how learning works', ['developing'], 'study, autonomy and metacognition',
   'How do you know when you have really understood something?', 'the independent study row 4.8.b24 and qaa/fheq-2024/4.15.b9.3')
li('3.33.b2', 'decision-making, time management and setting priorities among tasks', ['prioritising'], 'decisions, time and priorities',
   'How did you decide what to do first last week?', 'the row 4.8.b24 and qaa/fheq-2024/annex-d/transferable/r3/3rd')
li('3.33.b3', 'skill in keeping and archiving records', [], 'record-keeping and archiving',
   'Could someone else follow your field notebook or data folder?', '3.27 on reproducibility and qaa/fheq-2024/annex-d/practical/r4/3rd')
li('3.33.b4', 'skill in synthesising, placing in context and critically judging information of varied styles and sources', ['synthesising', 'contextualising', 'evaluating'],
   'synthesising and evaluating information', 'How did you judge a source that was not academic?', 'the synthesis row 4.8.b17 and qaa/fheq-2024/annex-d/cognitive/r1/3rd')
li('3.33.b5', 'communication in speech, writing and graphics', [], 'oral, written and graphical communication',
   'Which form of communication do you find hardest, and why?', 'the row 4.8.b19 and qaa/fheq-2024/4.15.b8')
li('3.33.b6', 'skill in finding, handling and archiving datasets', [], 'retrieving and handling datasets',
   'Where did your last data set come from, and how did you store it?', 'the row 4.8.b23 and qaa/fheq-2024/annex-d/practical/r4/3rd')
li('3.33.b7', 'an understanding of intellectual property and data privacy', [], 'intellectual property and data privacy',
   'Whose permission did you need to use the images or data in your work?', '3.27 and qaa/fheq-2024/4.15.b9.1')
li('3.33.b8', 'communication with varied audiences in formats that suit them', ['employing'], 'communicating to varied audiences',
   'How would you explain your project to a local council rather than a tutor?', 'the argument row 4.8.b22 and qaa/fheq-2024/4.15.b8')
li('3.33.b9', 'teamwork in groups while recognising and respecting others\' viewpoints', ['work', 'recognise', 'respect'], 'group work and respect for others',
   'When did a teammate change your mind?', 'the group row 4.8.b25, 4.8.b1 and qaa/fheq-2024/annex-d/transferable/r2/3rd')
li('3.33.b10', 'creative approaches to solving problems', ['take'], 'creative problem-solving',
   'What unusual approach have you tried on a problem, and did it work?', 'qaa/fheq-2024/annex-d/cognitive/r4/3rd and qaa/fheq-2024/4.15.b9.2')

li('3.34.b1', 'motivation', [], 'motivation', 'What keeps you going when a task is hard?', 'the row 4.8.b24 and qaa/fheq-2024/4.15.b9.1')
li('3.34.b2', 'innovation', [], 'innovation', 'What have you done differently from the usual way, and why?', 'qaa/fheq-2024/annex-d/cognitive/r4/3rd')
li('3.34.b3', 'an entrepreneurial outlook', [], 'entrepreneurialism', 'Where could your geography skills create value for others, social or economic?',
   '1.12 and std:doc:qaa-enterprise-2018-guidance')
li('3.34.b4', 'the ability to work responsibly, on your own and with others', ['work'], 'responsible, autonomous and shared work',
   'When did you take responsibility for something that went wrong in a group?', 'the group row 4.8.b25 and qaa/fheq-2024/4.15.b9.1')
li('3.34.b5', 'self-awareness, reflection, resilience, self-management and confidence in yourself', [], 'self-awareness and resilience',
   'How did you recover after a setback in your studies?', 'the reflection row 4.8.b26 and qaa/fheq-2024/annex-d/transferable/r5/3rd')
li('3.34.b6', 'empathy and insight', [], 'empathy and insight', 'How did someone else\'s experience change how you saw a place?', '4.8.b1 and 4.8.b3')
li('3.34.b7', 'intellectual integrity and ethical conduct', [], 'integrity and ethical behaviour',
   'How do you make sure your work is honestly your own and fairly uses others\'?', '3.30.b2 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st')
li('3.34.b8', 'a sense of responsibility as a citizen at local, national and international scale, with a global outlook', [], 'responsible global citizenship',
   'What responsibility do you feel towards a place you have studied?', '1.10, 3.12 and std:doc:qaa-advancehe-esd-2021-guidance')
li('3.34.b9', 'the skills to keep learning throughout life', ['engage'], 'lifelong learning',
   'What will you need to keep learning after your degree, and how?', 'qaa/fheq-2024/4.15.b9.3 and spine:6')
li('3.34.b10', 'flexibility and adaptability', [], 'flexibility and adaptability',
   'When did a plan fail in the field, and how did you adapt?', '3.15 and qaa/fheq-2024/4.15.b9.2')
for _k in ('3.34.b1', '3.34.b2', '3.34.b6', '3.34.b10'):
    P[_k]['para'] = P[_k]['para'].replace('show ', 'show the attribute of ', 1)

# ---------------------------------------------------------------- section 4: paragraphs and rung summaries
s('4.1', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students awarded honours in Geography',
  addressee='learner', verbs=['demonstrated'], about='the threshold as the minimum for honours', domain='none', award=HON,
  para=('The section sets out the minimum threshold that a student will have shown on being awarded honours in Geography; meeting these '
        'standards over time shows they have the knowledge, understanding and skills expected of graduates.'),
  prac='Treat the threshold cells as the least every student awarded honours will have demonstrated, shown through assessment over the course.',
  ben='To be awarded an honours degree in geography, you will have shown at least the minimum standards in knowledge, understanding and skills.',
  aaw=AAW('the issuer\'s definition of the threshold: the least a student will have demonstrated for honours', '4.1',
          'Hold it at FHEQ Level 6 (FQHEIS Level 10); the issuer applies the same table to integrated master\'s degrees (4.4).',
          'that the threshold is the expected or typical result, since 4.2 says most do far better',
          '4.2, 4.5, the threshold cells 4.8.b5 to 4.8.b26 and qaa/fheq-2024/annex-d/summary/r1/3rd'),
  aad=AAD('a student asks what they must show to pass, or a team sets pass criteria', PLAIN,
          'Which of the minimum standards are you confident you meet? Where do you need more evidence?',
          'presenting the threshold as the goal, since most students exceed it'))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='each higher education provider',
  addressee='provider', verbs=['perform', 'refer'], about='Annex D for performance above the threshold', domain='none', award=HON,
  para=('Most students will do far better than the minimum; each provider decides what evidence shows this and should refer to Annex D, '
        'which describes the four honours classes, first, upper second, lower second and third, at FHEQ Level 6 (FQHEIS Level 10).'),
  prac=('Most of your students will exceed the threshold; decide what evidence shows this, and refer to Annex D of the qualifications '
        'frameworks, which describes the four honours classes at FHEQ Level 6 (FQHEIS Level 10).'),
  ben=('n/a', 'a duty on the provider in setting classification evidence'),
  aaw=AAW('a provider expectation (should) to judge performance above the threshold against Annex D', '4.2',
          'It concerns honours classification at FHEQ Level 6 (FQHEIS Level 10).',
          'that the issuer sets marks or class boundaries',
          '4.1, 4.5 to 4.7, std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d) and std:ref:uk-assesscriteria'),
  aad=AAD('a team writes classification criteria or marking descriptors', STAFF,
          'How do your criteria for a first differ from those for an upper second? Do they match the Annex D descriptions?',
          'putting it to a student as their duty'))
s('4.5', type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6', appliesTo='threshold graduates',
  addressee='learner', verbs=['possess', 'demonstrated'], about='the threshold graduate in summary', domain='understanding', award=BOTH,
  para=('A threshold graduate has basic knowledge of change in human and physical environments, of the links between them, of sustainability '
        'and of how places at different scales depend on each other; their view leans on formal teaching with limited criticality, and they '
        'show competence in the essential subject, intellectual and generic skills.'),
  prac=('At threshold, graduates hold a basic grasp of environmental and social change, its interrelations, sustainability and the '
        'interdependence of places, see the subject largely through what they were taught with little critique, and show competence in the essential skills.'),
  ben=('To reach the minimum for your degree, you will have a basic grasp of how human and physical environments change and connect, of '
       'sustainability and of how places depend on each other, and you will show you can use the essential skills.'),
  aaw=AAW('the issuer\'s summary of the threshold rung, the least a graduate shows for the award', '4.5', L6IM,
          'that it describes a typical graduate', '4.6, 4.7, the threshold cells in 4.8, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/summary/r1/3rd'),
  aad=AAD('a student fears failing or asks what the minimum looks like', 'plainly, in the second person, as the floor and not the aim',
          'Can you explain change and sustainability in your own words with an example? Which essential skills could you show evidence for now?',
          'presenting the threshold as what most students achieve'))
s('4.6', type='typical', rung='typical', force='describes', forceFrom='4.4', level='fheq:6', appliesTo='typical graduates',
  addressee='learner', verbs=['display', 'demonstrating'], about='the typical graduate in summary', domain='understanding', award=BOTH,
  para=('A typical graduate shows critical awareness of the subject\'s scope and methods on a solid base of knowledge, commands subject and '
        'generic skills consistently with proficiency in most higher intellectual skills, and stands above the threshold by applying their own perspectives critically.'),
  prac=('At the typical level, graduates show critical awareness of geography\'s scope and methods, consistent command of subject and generic '
        'skills, proficiency in most higher-level thinking skills, and critical use of their own perspectives.'),
  ben=('At the typical level, which most students reach, you show critical awareness of the subject and its methods, use your skills '
       'consistently, and bring your own view to your work critically.'),
  aaw=AAW('the issuer\'s summary of the typical rung, described with no modal, which most graduates reach above the threshold', '4.6', L6IM,
          'that it is the minimum for the award', '4.5, 4.7, the typical cells in 4.8 and qaa/fheq-2024/annex-d/summary/r1/2.2 and r1/2.1'),
  aad=AAD('a student asks what a good degree looks like', 'plainly, in the second person',
          'Where in your work do you bring your own perspective critically? Do you use your skills consistently or only sometimes?',
          'presenting the typical rung as the pass standard'))
s('4.7', type='excellent', rung='excellent', force='describes', forceFrom='4.4', level='fheq:6', appliesTo='graduates who reach excellence',
  addressee='learner', verbs=['distinguished', 'deployed', 'bring', 'link'], about='the excellent graduate in summary', domain='understanding', award=BOTH,
  para=('Excellent graduates stand out mainly through superior intellectual skills used across wide knowledge; they bring originality, '
        'insight and strong critical reflection, link theory and practice in research, and show this most in independent work such as '
        'dissertations, which may approach publishable quality.'),
  prac=('At the excellent level, graduates show superior intellectual skills across broad knowledge, originality and insight, and join theory '
        'to practice in research problems, most visibly in dissertations that may come near publishable standard.'),
  ben=('At the excellent level, you bring originality and insight to wide knowledge, join theory and practice in your research, and may '
       'produce independent work, such as a dissertation, close to publishable quality.'),
  aaw=AAW('the issuer\'s summary of the excellent rung, described with no modal, an aspiration above the typical', '4.7', L6IM,
          'that it is expected of every graduate or that publishable work is required', '4.6, the excellent cells in 4.8, qaa/fheq-2024/annex-d/summary/r1/1st and spine:6'),
  aad=AAD('a strong student asks how to reach a first, or a team designs dissertation criteria', 'plainly, in the second person',
          'Where does your work go beyond what you were taught? How does your dissertation connect theory and practice?',
          'making a student feel this is the minimum'))

# 4.8 bullets: what successful graduates should have developed, outside the rung table
B48 = dict(type='outcome', rung='none', force='should', level='fheq:6', appliesTo="successful graduates of honours and integrated master's degrees",
           addressee='learner', domain='generic-skill', award=BOTH)


def b48(i, n, verbs, about, para, prac, ben, q, beside, **k):
    s(i, **B48, verbs=verbs, about=about, para=para, prac=prac, ben=ben,
      aaw=AAW('an outcome that successful graduates should have developed, listed above the rung table', f'4.8 ({n} bullet)', L6IM.split(';')[0] + '.',
              'that it is graded by rung, since the issuer lists it outside the table', beside),
      aad=AAD('a student reflects on working with others or a team designs collaborative or reflective tasks', PLAIN, q,
              'reading the list aloud or turning it into a checklist of feelings'), **k)


b48('4.8.b1', 'first', ['collaborate', 'empathise', 'respect'], 'equitable, empathetic collaboration',
    'Should have built the ability to work with others fairly, with empathy and respect for their views, perspectives and needs.',
    'Graduates should have developed fair collaboration, empathy and respect for the views, perspectives and needs of others.',
    'You should have learned to work fairly with others, with empathy and respect for their views and needs.',
    'When did you last change your view after listening to someone? How did you make sure everyone in your group was heard?',
    'the group row 4.8.b25, 1.5, 3.33.b9 and qaa/fheq-2024/4.15.b9.1')
b48('4.8.b2', 'second', ['understand', 'reflect'], 'critical reflection on norms and values',
    'Should have built the ability to grasp, and think critically about, the norms and values behind their own and others\' views and actions.',
    'Graduates should have developed a critical understanding of the norms and values that shape their own and others\' views and actions.',
    'You should have learned to notice and question the values behind what you and others think and do.',
    'Which of your own assumptions have you questioned this year? What values sit behind a view you disagree with?',
    'the positionality row 4.8.b21, 1.7 and qaa/fheq-2024/4.15.b4')
b48('4.8.b3', 'third', ['work'], 'collaborating across difference',
    'Should have built the ability to work with people who bring different knowledge, views and experience.',
    'Graduates should have developed the ability to collaborate with people whose knowledge, views and experience differ from theirs.',
    'You should have learned to work well with people whose knowledge, views and experience differ from yours.',
    'Who in your last group saw things most differently from you, and what did you gain from that?',
    'the group row 4.8.b25, 2.15 and qaa/fheq-2024/annex-d/transferable/r2/3rd')
b48('4.8.b4', 'fourth', ['have'], 'awareness of emotions and wellbeing',
    'Should have built awareness and understanding of how their own and others\' emotional responses and wellbeing affect them and their work.',
    'Graduates should have developed an awareness and understanding of the effect of their own and others\' emotions and wellbeing.',
    'You should have learned to notice how your own and other people\'s feelings and wellbeing affect you and your work.',
    'How do your feelings about a place or a task affect your work? How do you notice when a teammate is struggling?',
    '1.9, 3.34.b5 and qaa/fheq-2024/4.15.b9.1',
    find="be aware of, and have an understanding of, the impact of their own, and others' emotional response and well-being.")

# ---------------------------------------------------------------- 4.8 table: one record per rung on each cell (flattened in the held text)
HEAD = {'knowledge': 'knowledge and understanding', 'understanding': 'knowledge and understanding',
        'subject-skill': 'subject-specific skills', 'generic-skill': 'generic skills'}
BAND = {'threshold': '3rd', 'typical': '2.2 and 2.1', 'excellent': '1st'}
RUNG_S1 = {
    'threshold': 'Describe this as the threshold standard for {name}: the least a Geography graduate shows for the award, not a typical result.',
    'typical': 'Describe this as the typical standard for {name}, which the issuer describes without a modal and which most graduates reach above the threshold.',
    'excellent': 'Describe this as the excellent standard for {name}, an aspiration the issuer describes above the typical, not a requirement.'}
AVOID = {'threshold': 'Do not read the table aloud, and make clear this is the floor, not the aim.',
         'typical': 'Do not read the table aloud, and never present this typical level as the pass mark.',
         'excellent': 'Do not read the table aloud, and never present this excellent level as the minimum.'}
GRADE = {}
ROWS = []


def you(g):
    return (' ' + g + ' ').replace(' their ', ' your ').replace(' they ', ' you ').replace(' to them ', ' to you ').strip()


def row(b, name, dom, fheq, annex, when, q, cells):
    base = f'4.8.b{b}'
    ids = {'threshold': base, 'typical': base + '.typical', 'excellent': base + '.excellent'}
    ROWS.append(dict(outcome=name, threshold=ids['threshold'], typical=ids['typical'], excellent=ids['excellent'],
                     basis='stated', domain=dom, award="bachelor's with honours; integrated master's"))
    for rung, (find, verbs, gist) in zip(('threshold', 'typical', 'excellent'), cells):
        i = ids[rung]
        others = ', '.join(v for k, v in ids.items() if k != rung)
        level = 'fheq:6'
        if rung == 'threshold':
            para = f'As the minimum for the award, the graduate can {gist}.'
            prac = f'At threshold, every graduate can {gist}; this is the floor for honours and integrated master\'s alike.'
            ben = f'To reach the minimum for your degree, you will be able to {you(gist)}.'
            force, ff = 'threshold', '4.1'
        elif rung == 'typical':
            para = f'A typical graduate can {gist}.'
            prac = f'At the typical level, which most graduates reach, graduates can {gist}.'
            ben = f'At the typical level, which most students reach, you will be able to {you(gist)}.'
            force, ff = 'describes', '4.4'
            GRADE[i] = ids['threshold'] + '|stated'
        else:
            para = f'An excellent graduate can {gist}.'
            prac = f'At the excellent level, graduates can {gist}.'
            ben = f'At the excellent level, you will be able to {you(gist)}.'
            force, ff = 'describes', '4.4'
            GRADE[i] = ids['typical'] + '|stated'
        aaw = (RUNG_S1[rung].format(name=name) + ' ' + L6IM + f' Cite it as {CITE}4.8, table, {HEAD[dom]}, {rung} column, and do not '
               f'call it a regulatory requirement. Set it beside {others}, {fheq} and qaa/fheq-2024/annex-d/{annex}/{BAND[rung].split(" and ")[-1]}'
               + (f' (with .../{annex}/2.2)' if rung == 'typical' else '') + '.')
        aad = (f'Bring this up when {when}. Put it plainly, in the second person to a student or as a design point to staff, and ask: {q} '
               + AVOID[rung])
        s(i, type=rung, rung=rung, force=force, forceFrom=ff, level=level, appliesTo=f'{rung} graduates of honours and integrated master\'s degrees',
          addressee='learner', verbs=verbs, about=f'{name} ({rung})', domain=dom, award=BOTH,
          para=para, prac=prac, ben=ben, aaw=aaw, aad=aad, find=find)


row(5, 'change and variability in societies and environments', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'knowledge/r1',
    'a student revises how societies and environments change, or a team writes outcomes on change',
    'Can you give an example of change in a society or environment and say what drove it?', [
        ('Describe and exemplify the nature of change and variability within societies and environments.', ['describe', 'exemplify'],
         'describe, with examples, how societies and environments change and vary'),
        ('Demonstrate comprehension of the nature of change and variability within societies and environments.', ['demonstrate'],
         'show a sound grasp of how societies and environments change and vary'),
        ('Demonstrate critical insight into the nature and causes of change and variability within societies and environments.', ['demonstrate'],
         'show critical insight into why and how societies and environments change and vary')])
row(6, 'the two-way relationships between societies and environments', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2',
    'a student links human and physical topics',
    'How does the environment you studied shape the people there, and how do they shape it, at more than one scale?', [
        ('Describe and exemplify the reciprocal relationships between societies and environments at multiple spatial and temporal scales.', ['describe', 'exemplify'],
         'describe, with examples, the two-way links between societies and environments across scales of space and time'),
        ('Demonstrate comprehension of the reciprocal relationships between societies and environments at multiple spatial and temporal scales.', ['demonstrate'],
         'show a sound grasp of the two-way links between societies and environments across scales of space and time'),
        ('Demonstrate critical insight of the complexity of the reciprocal relationships between societies and environments at multiple spatial and temporal scales.', ['demonstrate'],
         'show critical insight into how complex the two-way links between societies and environments are, across scales of space and time')])
row(7, 'sustainability and sustainable development', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2',
    'a student discusses sustainability or a team maps education for sustainable development',
    'What does sustainable development mean in a case you know, and who gains or loses from it?', [
        ('Describe approaches to sustainability and sustainable development in relation to the complex interactions between societies and environments.', ['describe'],
         'describe ways of approaching sustainability and sustainable development as they bear on how societies and environments interact'),
        ('Demonstrate comprehension of sustainability and sustainable development practices in relation to the complex interactions between societies and environments.', ['demonstrate'],
         'show a sound grasp of sustainability and sustainable development practice as it bears on how societies and environments interact'),
        ('Demonstrate critical insight into sustainability and sustainable development practices in relation to the complex interactions between societies and environments.', ['demonstrate'],
         'show critical insight into sustainability and sustainable development practice as it bears on how societies and environments interact')])
row(8, 'the history of geography and its making of knowledge', 'knowledge', 'qaa/fheq-2024/4.15.b4', 'knowledge/r2',
    'a student studies the history of the discipline or its colonial past',
    'Whose knowledge has geography included and left out, and what follows from that today?', [
        ('Describe the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history.', ['describe'],
         'describe how geography grew as a discipline, the settings in which its knowledge was and is made, and what that history means now'),
        ('Demonstrate comprehension of the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history.', ['demonstrate'],
         'show a sound grasp of the discipline\'s history, the settings of its knowledge-making then and now, and their present-day consequences'),
        ('Demonstrate a critical understanding of the history of geography as a discipline and the relevant contexts of past and present geographical knowledge production, and contemporary implications of this history.', ['demonstrate'],
         'show a critical understanding of the discipline\'s history, the settings of its knowledge-making then and now, and their present-day consequences')])
row(9, 'the diversity and interdependence of places', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'knowledge/r1',
    'a student compares places or scales',
    'How does the place you studied depend on places elsewhere? Why do places differ?', [
        ('Describe and exemplify the diversity and interdependency of places.', ['describe', 'exemplify'],
         'describe, with examples, how places differ and depend on one another'),
        ('Demonstrate comprehension of the diversity and interdependency of', ['demonstrate'],
         'show a sound grasp of how places at different scales differ and depend on one another'),
        ('Reflect on and appraise the reasons for the diversity and interdependency of', ['reflect', 'appraise'],
         'reflect on and judge the reasons why places at different scales differ and depend on one another')])
row(10, 'ways of producing geographical knowledge', 'understanding', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2',
    'a student meets different research traditions in human and physical geography',
    'How would a natural scientist and a humanities scholar each come to know your topic? What does each approach miss?', [
        ('Describe and exemplify the diversity of approaches to generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities.', ['describe', 'exemplify'],
         'describe, with examples, the different ways knowledge is produced across the natural sciences, social sciences and humanities'),
        ('Evaluate the diversity of approaches to the generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities.', ['evaluate'],
         'evaluate the different ways knowledge is produced across the natural sciences, social sciences and humanities'),
        ('Critically appraise the diversity of approaches to the generation of knowledge and understanding deriving from experience of the epistemologies of the natural and social sciences and humanities.', ['appraise'],
         'critically appraise the different ways knowledge is produced across the natural sciences, social sciences and humanities')])
row(11, 'applying geographical concepts', 'understanding', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r3',
    'a student applies ideas from class to a new case',
    'Can you take a concept from one module and use it to explain a new situation?', [
        ('Carry out routine investigations as instructed.', ['carry'], 'carry out routine investigations when told how'),
        ('Apply understanding of geographical concepts in different situations.', ['apply'], 'use their grasp of geographical concepts in varied situations'),
        ('Apply a reflective understanding of geographical concepts in different situations.', ['apply'], 'apply geographical concepts to varied situations with reflection')])
row(12, 'accuracy, precision and uncertainty in data', 'understanding', 'qaa/fheq-2024/4.15.b2', 'practical/r4',
    'a student handles measurements or questions of data quality',
    'What is the difference between how accurate and how precise your data are? How sure can you be of your result?', [
        ('Know the difference between accuracy and precision.', ['know'], 'tell accuracy apart from precision'),
        ('Apply a systematic approach to accuracy, precision and uncertainty.', ['apply'], 'handle accuracy, precision and uncertainty systematically'),
        ('Critically reflect on the accuracy, precision and uncertainty of research data.', ['reflect'], 'reflect critically on how accurate, precise and uncertain research data are')])
row(13, 'research design and execution in field research', 'subject-skill', 'qaa/fheq-2024/4.15.b6', 'practical/r1',
    'a student plans fieldwork or a dissertation',
    'What went wrong or nearly wrong in your field research design, and how would you change it?', [
        ('Illustrate the issues involved in applying research design and execution skills within the specific context of field- based research.', ['illustrate'],
         'illustrate the issues that arise in designing and carrying out research in the field'),
        ('Evaluate the issues involved in applying research design and execution skills within the specific context of field-based research.', ['evaluate'],
         'evaluate the issues that arise in designing and carrying out research in the field'),
        ('Formulate a sophisticated and comprehensive analysis of the issues involved in applying research design and execution skills within the specific context of field-based research, including alternative options.', ['formulate'],
         'formulate a thorough, sophisticated analysis of the issues in designing and carrying out field research, with alternative options')])
row(14, 'techniques for collecting geographical information', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'practical/r1',
    'a student chooses data-collection methods',
    'Which collection methods have you used, and why that one for your question?', [
        ('Illustrate diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources).', ['illustrate'],
         'illustrate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives'),
        ('Evaluate the diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources).', ['evaluate'],
         'evaluate the range of techniques for collecting geographical information, such as instruments, remote sensing, surveys, observation and archives'),
        ('Critically appraise and reflect on use of the diversity of techniques and approaches involved in collecting geographical information (for example, instrumentation, remote sensing, cartographic surveying, social survey, observation and the use of textual and archival sources).', ['appraise', 'reflect'],
         'critically appraise and reflect on their own use of the range of techniques for collecting geographical information')])
row(15, 'quantitative and qualitative analysis', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'practical/r4',
    'a student analyses data',
    'Why did you use numbers, words or both to analyse this? What would the other approach add?', [
        ('Illustrate both quantitative and qualitative approaches for analysis of geographical information and data and perform basic applications.', ['illustrate', 'perform'],
         'illustrate quantitative and qualitative ways of analysing geographical data and carry out basic applications of them'),
        ('Evaluate both quantitative and qualitative approaches for analysis of geographical information and data, including competence', ['evaluate'],
         'evaluate quantitative and qualitative ways of analysing geographical data, applying a range of them competently'),
        ('Critically appraise and reflect on the application of quantitative and qualitative approaches for analysis of geographical data, including excellent and', ['appraise', 'reflect'],
         'critically appraise and reflect on using quantitative and qualitative analysis, applying a range of approaches with excellence and sophistication')])
row(16, 'specialised techniques of analysis', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'practical/r3',
    'a student learns GIS, laboratory or other specialist analysis',
    'Which specialist technique do you trust most, and how do you know it worked?', [
        ('Illustrate diversity of specialised techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques).', ['illustrate'],
         'illustrate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods'),
        ('Evaluate the diversity of specialised techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques).', ['evaluate'],
         'evaluate the range of specialised techniques for analysing geographical information, such as spatial analysis, GIS and laboratory methods'),
        ('Demonstrate a mastery of techniques and approaches involved in analysing geographical information (for example, special techniques for the analysis of spatial information, GIS, laboratory techniques, qualitative and quantitative techniques) and very good judgement of their effectiveness.', ['demonstrate'],
         'show mastery of specialised analytical techniques and very good judgement of how well they work')])
row(17, 'synthesising and interpreting information', 'subject-skill', 'qaa/fheq-2024/4.15.b7', 'cognitive/r1',
    'a student writes up results',
    'What does your evidence add up to, and how does it fit what is already known?', [
        ('Summarise information and data and make accurate interpretations.', ['summarise', 'make'], 'summarise information and data and interpret them accurately'),
        ('Synthesize information and data and make accurate interpretations in the context of current geographical knowledge.', ['synthesize', 'make'],
         'bring information and data together and interpret them accurately in light of current geographical knowledge'),
        ('Synthesize information and data and make accurate and critically reflective interpretations in the context of current geographical knowledge.', ['synthesize', 'make'],
         'bring information and data together and interpret them accurately and with critical reflection in light of current geographical knowledge')])
row(18, 'presenting geographical information', 'subject-skill', 'qaa/fheq-2024/4.15.b8', 'practical/r4',
    'a student prepares maps, figures or presentations',
    'Why did you choose this map or format for this audience?', [
        ('Illustrate diversity of specialised techniques and approaches involved in presenting geographical knowledge and information (for example, GIS, cartography and different textual strategies).', ['illustrate'],
         'illustrate the range of specialised ways of presenting geographical knowledge, such as GIS, cartography and textual strategies'),
        ('Evaluate the diversity of specialised techniques and approaches involved in presenting geographical information (for example, GIS, cartography and dif ferent textual strategies).', ['evaluate'],
         'evaluate the range of specialised ways of presenting geographical information, such as GIS, cartography and textual strategies'),
        ('Critically evaluate and reflect on the appropriate application of the diversity of specialised geographical techniques and approaches.', ['evaluate', 'reflect'],
         'critically evaluate and reflect on how suitably specialised geographical techniques are applied')])
row(19, 'communicating geographical ideas', 'subject-skill', 'qaa/fheq-2024/4.15.b8', 'transferable/r1',
    'a student prepares any written, spoken or visual work',
    'Who is your audience, and how did you adapt your writing, talk or graphics for them?', [
        ('Communicate geographical ideas, principles and theories by written, oral and graphical means.', ['communicate'],
         'put across geographical ideas, principles and theories in writing, speech and graphics'),
        ('Communicate geographical ideas, principles and theories effectively and fluently by written, oral and graphical means.', ['communicate'],
         'put across geographical ideas, principles and theories well and fluently in writing, speech and graphics'),
        ('Communicate geographical ideas, principles and theories with flair, accuracy and sophistication by written, oral and graphical means.', ['communicate'],
         'put across geographical ideas, principles and theories with flair, precision and sophistication in writing, speech and graphics')])
row(20, 'views on geographical issues', 'generic-skill', 'qaa/fheq-2024/4.15.b7', 'cognitive/r2',
    'a student discusses a contested issue',
    'What do you think about this issue, and what would someone who disagrees say?', [
        ('Communicate personal views about geographical issues.', ['communicate'], 'express their own views on geographical issues'),
        ('Communicate and compare different views about geographical issues.', ['communicate', 'compare'], 'express and compare differing views on geographical issues'),
        ('Critically reflect on a range of views about geographical issues and come to a reasoned evaluation.', ['reflect', 'come'],
         'reflect critically on a range of views on geographical issues and reach a reasoned judgement')])
row(21, 'positionality and assumptions', 'generic-skill', 'qaa/fheq-2024/4.15.b4', 'transferable/r5',
    'a student reflects on fieldwork, research ethics or their own viewpoint',
    'How might your own background shape what you noticed or concluded? What follows from that?', [
        ('Demonstrate an awareness of their positionality and assumptions and the potential implications and consequences of them.', ['demonstrate'],
         'show awareness of their own positionality and assumptions and of what these may lead to'),
        ('Recognise their positionality and assumptions and evaluate the potential implications and consequences of them.', ['recognise', 'evaluate'],
         'recognise their positionality and assumptions and evaluate what these may lead to'),
        ('Recognise their positionality and assumptions and critically evaluate the potential implications and consequences of them.', ['recognise', 'evaluate'],
         'recognise their positionality and assumptions and critically evaluate what these may lead to')])
row(22, 'reasoned argument', 'generic-skill', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r2',
    'a student plans an essay or presentation',
    'What is your main claim, and which evidence carries it?', [
        ('Present material to support a reasoned argument.', ['present'], 'present material in support of a reasoned argument'),
        ('Synthesize material appropriately to support the presentation of a reasoned argument to the intended audience.', ['synthesize'],
         'draw material together suitably to put a reasoned argument to its intended audience'),
        ('Synthesize complex information to support the presentation of a reasoned argument to both specialist and non- specialist audiences.', ['synthesize'],
         'draw complex information together to put a reasoned argument to specialists and non-specialists alike')])
row(23, 'communications technology and ICT', 'generic-skill', 'qaa/fheq-2024/4.15.b8', 'transferable/r1',
    'a student uses digital tools for analysis or presentation',
    'Which digital tools do you use to analyse and present information, and how well do they serve you?', [
        ('Use communications and ICT to select, analyse, present and communicate geographical information.', ['use'],
         'use communication technologies and ICT to select, analyse, present and share geographical information'),
        ('Use communications and ICT effectively and appropriately to select, analyse, present and communicate geographical information.', ['use'],
         'use communication technologies and ICT well and suitably to select, analyse, present and share geographical information'),
        ('Use communications and ICT with a high level of competence to select, analyse, present and communicate geographical information.', ['use'],
         'use communication technologies and ICT highly competently to select, analyse, present and share geographical information')])
row(24, 'independent study and time management', 'generic-skill', 'qaa/fheq-2024/4.15.b5', 'transferable/r3',
    'a student struggles with deadlines or plans independent work',
    'How do you plan a week of independent study? What support do you still lean on?', [
        ('Undertake independent/ self-directed study/ learning (including time management) within a supportive framework.', ['undertake'],
         'study independently and manage their time within a supportive structure'),
        ('Undertake independent/ self-directed study/ learning (including time management) to achieve consistent, proficient and sustained attainment.', ['undertake', 'achieve'],
         'study independently and manage their time so as to attain consistently, proficiently and steadily'),
        ('Undertake highly autonomous and well organised study/ learning and time management to achieve consistent, proficient and sustained attainment.', ['undertake', 'achieve'],
         'study with high autonomy and good organisation, managing their time to attain consistently, proficiently and steadily')])
row(25, 'group work and leadership', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r2',
    'a student does group work',
    'What role did you take in your last group, and what did the group achieve because of you?', [
        ('Perform assigned tasks within a group setting and take part in group discussions.', ['perform', 'take'],
         'carry out tasks given to them in a group and join in its discussions'),
        ('Work as a participant or leader of a group and contribute effectively to the achievement of objectives.', ['work', 'contribute'],
         'work as a member or leader of a group and help it meet its aims'),
        ('Demonstrate group leadership and supportive participation of others within a group setting to achieve objectives.', ['demonstrate'],
         'lead a group and support others\' participation so that it meets its aims')])
row(26, 'reflecting on one\'s own learning', 'generic-skill', 'qaa/fheq-2024/4.15.b9.3', 'transferable/r5',
    'a student reflects on feedback or plans their development',
    'What are your strongest and weakest skills, and what will you do differently next time?', [
        ('Describe the process of learning and present a basic assessment of personal strengths and weaknesses.', ['describe', 'present'],
         'describe how they learn and give a basic account of their own strengths and weaknesses'),
        ('Analyse the process of learning and evaluate personal strengths and weaknesses.', ['analyse', 'evaluate'],
         'analyse how they learn and evaluate their own strengths and weaknesses'),
        ('Critically reflect on the process of learning, evaluating personal strengths and weaknesses and demonstrating an understanding of alternative strategies.', ['reflect', 'evaluating', 'demonstrating'],
         'reflect critically on how they learn, weighing their strengths and weaknesses and showing they understand other strategies')])

# rung summaries 4.5 to 4.7: the issuer pairs them (4.6 "distinguished from the threshold level", 4.7 "beyond the typical standard")
GRADE['4.6'] = '4.5|stated'
GRADE['4.7'] = '4.6|stated'

TH = {'1.5': 'theme:edi', '1.6': 'theme:edi', '1.7': 'theme:edi', '1.8': 'theme:edi', '1.12': 'theme:enterprise', '2.6': 'theme:accessibility'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 4.2 (Annex D for FHEQ Level 6)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 4.2 (Annex D for FQHEIS Level 10)'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.10 (integrated master\'s)'),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.10 (integrated master\'s)'),
                  dict(id='spine:6', role='inferred', locator='std:ref:uk-framework R2: the honours award and the table\'s level (Part E)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 4.2: Annex D for FHEQ Level 6 and FQHEIS Level 10 degrees)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.10: integrated master\'s at FHEQ Level 7, FQHEIS Level 11)'),
                      dict(**{'from': 'fheq:6'}, to='spine:6', relation='levelEquivalent', basis='inferred from std:ref:uk-framework R2 (Part E)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.5', '1.6', '1.7', '1.8', '1.9', '2.3', '2.5', '2.6', '2.15', '3.8', '3.19']),
      dict(id='theme:accessibility', role='carries', carriedIn=['2.3', '2.4', '2.5', '2.6', '2.11', '2.13', '3.19', '3.40']),
      dict(id='theme:esd', role='carries', carriedIn=['1.10', '3.2', '3.6', '3.12', '3.20', '4.5', '4.8']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.11', '1.12', '2.14', '3.34'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-geography-2019-benchmarks (fourth edition, 2019; not held)', note='edition history in the back matter, section 6'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2; section 5)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Levels 10 and 11 (2.10, 4.2)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='three ESD principles taken from it (1.10; section 5)'),
      dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note='the deeper generic analysis of enterprise (1.12; section 5)'),
      dict(rel='refersTo', target='Royal Geographical Society (with IBG): Chartered Geographer and programme accreditation (not yet ingested)', note='2.18; section 5 (Part E)'),
      dict(rel='refersTo', target='Equality Act 2010', note='protected characteristics (1.5)'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary', note='front matter')]
S8 = {'published': '2022-03', 'lastReviewed': 'none-stated', 'reviewCycle': 'none-stated',
      'consultation': 'advisory group of 2022 named; thanks to the Disabled Students\' Commission and two named contributors (D1, section 6)', 'replacedBy': 'none'}

SB1 = [
    'Geography studies how societies and environments shape each other, through the lenses of scale, place, space and time (D1, 1.1)',
    'It is at once a STEM and a SHAPE subject, joining natural and social sciences with arts and humanities, and courses run as BA, BSc, Scottish MA and integrated master\'s (D1, 1.2; 1.3)',
    'It values plural ways of knowing, qualitative and quantitative, and rests on fieldwork, laboratory work, spatial data analysis, modelling, GIS and remote sensing (D1, 1.4)',
    'It sees itself as an inclusive learning community that must face its colonial origins and carry values of care and solidarity through the whole curriculum (D1, 1.5 to 1.8)',
    'Fieldwork, in an expansive sense of the field from landscapes to archives and digital spaces, is required throughout the degree (D1, 3.13 to 3.15)',
    'Geocapabilities, the subject\'s own capabilities of thinking spatially and holistically about place, society and environment, grow as students progress (D1, 3.22)',
]
SB2 = [dict(theme='theme:edi', inThisSubject=('A collective duty to embed equity and inclusion, framed by the discipline\'s colonial past; carried into curriculum values, '
                                              'critical theory and inclusive fieldwork and partnerships (D1, 1.5 to 1.9; 2.6; 2.15; 3.19)'),
            statements=['1.5', '1.6', '1.7', '1.8', '2.6', '2.15', '3.19', '4.8.b1', '4.8.b3']),
       dict(theme='theme:accessibility', inThisSubject=('Inclusive design across teaching, assessment and above all fieldwork, with affordable trips, flexible delivery '
                                                        'and allowance for unequal access to technology (D1, 2.3 to 2.6; 2.11 to 2.13; 3.19; 3.40)'),
            statements=['2.6', '2.13', '3.19', '3.40']),
       dict(theme='theme:esd', inThisSubject=('Sustainable development is core content and a rung row; fieldwork carries a carbon audit; three principles from the ESD '
                                              'guidance shape teaching (D1, 1.10; 3.20; 4.5; 4.8)'),
            statements=['3.20', '4.5', '4.8.b7', '4.8.b7.typical', '4.8.b7.excellent', '3.34.b8']),
       dict(theme='theme:enterprise', inThisSubject=('Employability, entrepreneurship and enterprise read broadly: data and spatial skills for decisions, and social, '
                                                     'green and digital enterprise valued beside economic surplus (D1, 1.11; 1.12; 2.14; 3.34)'),
            statements=['1.12', '3.34.b3'])]
SB3 = dict(
    areas=[dict(component='3.2', gloss='the discipline as a whole and its four strands of concepts'),
           dict(component='3.3', gloss='spatial distribution and change across scales'),
           dict(component='3.4', gloss='place and how it is made'),
           dict(component='3.5', gloss='systems and human-environment interaction'),
           dict(component='3.6', gloss='human patterns and processes; development and sustainability'),
           dict(component='3.7', gloss='physical environmental change'),
           dict(component='3.8', gloss='history of the discipline and decolonial practice'),
           dict(component='3.9', gloss='representation and mapping'),
           dict(component='3.10', gloss='research design and methodologies'),
           dict(component='3.11', gloss='GISci, GIS, remote sensing and statistics'),
           dict(component='3.12', gloss='global and local issues and applied problem-solving')],
    practices=[dict(component='3.13', kind='learning', gloss='fieldwork as experiential learning in every course'),
               dict(component='3.14', kind='learning', gloss='access to many kinds of field'),
               dict(component='3.15', kind='teaching', gloss='fieldwork through the whole degree'),
               dict(component='3.16', kind='learning', gloss='field data collection and laboratory analysis'),
               dict(component='3.17', kind='teaching', gloss='virtual fieldwork'),
               dict(component='3.18', kind='teaching', gloss='ethics and risk assessment of fieldwork'),
               dict(component='3.19', kind='teaching', gloss='inclusive fieldwork and inclusivity assessment'),
               dict(component='3.20', kind='teaching', gloss='carbon audit of fieldwork'),
               dict(component='3.21', kind='teaching', gloss='staffing fieldwork'),
               dict(component='3.35', kind='teaching', gloss='innovative teaching contexts'),
               dict(component='3.36', kind='teaching', gloss='range of teaching approaches'),
               dict(component='3.37', kind='learning', gloss='roles of experiential learning'),
               dict(component='3.38', kind='learning', gloss='independent research and the dissertation'),
               dict(component='3.39', kind='teaching', gloss='a wide mix of styles'),
               dict(component='3.40', kind='assessment', gloss='assessment and feedback strategy'),
               dict(component='3.41', kind='assessment', gloss='assessment methods students meet')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.8', award="bachelor's with honours; integrated master's", items=23),
           dict(rung='typical', leadIn='4.8', award="bachelor's with honours; integrated master's", items=23),
           dict(rung='excellent', leadIn='4.8', award="bachelor's with honours; integrated master's", items=23)],
    rungBases=('One table at 4.8, flattened in the held text, lists each of 22 outcomes once under three columns headed Threshold, Typical '
               'and Excellent, in three blocks (knowledge and understanding 8, subject-specific skills 7, generic skills 7); 4.4 introduces '
               'it for honours and integrated master\'s alike; 4.5 to 4.7 summarise each rung in prose and are recorded as one record per rung. '
               'Threshold is the minimum for the award (4.1); typical and excellent carry no modal (describes).'),
    outcomeLists=[dict(leadIn='4.8', gloss='what successful graduates should have developed, above the table', items=4, award=BOTH),
                  dict(leadIn='3.30', gloss='subject-specific skills, most of which graduates show (3.23)', items=11, award=BOTH),
                  dict(leadIn='3.32', gloss='generic intellectual skills (3.23)', items=8, award=BOTH),
                  dict(leadIn='3.33', gloss='generic skills (3.23)', items=10, award=BOTH),
                  dict(leadIn='3.34', gloss='personal attributes (3.23)', items=10, award=BOTH)],
    outcomes=[dict(outcome='overall rung profile', threshold='4.5', typical='4.6', excellent='4.7', basis='stated', domain='understanding',
                   award="bachelor's with honours; integrated master's")] + ROWS)
SB4A_FULL = []
SB5 = [dict(body='Royal Geographical Society (with the Institute of British Geographers)',
            says=('a learned society institutions can work with, supporting understanding of careers and routes to accreditation, including '
                  'its Chartered Geographer status (D1, 2.18); the back matter adds its voluntary programme accreditation scheme, aligned with the statement (D1, section 5)'),
            requirements='not yet ingested (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, equality, diversity and inclusion', carriedIn=['1.5', '1.6', '1.7', '1.8', '1.9', '2.3', '2.5', '2.6', '2.15', '3.8', '3.19'],
                 statements=['1.5', '1.6', '1.7', '1.8', '2.6', '2.15', '3.19', '4.8.b1', '4.8.b3']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['2.3', '2.4', '2.5', '2.6', '2.11', '2.13', '3.19', '3.40'],
                 statements=['2.6', '2.13', '3.19', '3.40']),
            dict(id='theme:esd', named='Sustainability; Education for Sustainable Development (ESD)', carriedIn=['1.10', '3.2', '3.6', '3.12', '3.20', '4.5', '4.8'],
                 statements=['3.20', '4.5', '4.8.b7', '4.8.b7.typical', '4.8.b7.excellent']),
            dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)',
                 carriedIn=['1.11', '1.12', '2.14', '3.34'], statements=['1.12', '3.34.b3'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.10', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.10', '4.2'])],
    bodies=[dict(body='Royal Geographical Society (with the Institute of British Geographers)', citedIn=['2.18'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees',
                          citedIn=['4.2'], role='the descriptions of the four honours classes, for performance above the threshold'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="Advance HE and QAA's Education for Sustainable Development (ESD) Guidance",
                          citedIn=['1.10'], role='source of the three ESD principles for geography'),
                     dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers',
                          citedIn=['1.12'], role='the deeper generic analysis of enterprise education')])

B1 = [dict(slug='geocapabilities', definition=('the subject\'s own capabilities: grasping the weight of place, space, scale, landscape and nature in life on Earth, thinking '
                                               'spatially, seeing how society and environment shape each other, and thinking holistically and critically (D1, 3.22)'),
           beneficiaryDefinition='the ways of thinking that geography builds in you: spatially, about places, and about people and environments together',
           scopeNote='cited to Walkington and others (2018) in the back matter', category='unknown', practices=['geography']),
      dict(slug='reproducibility', definition='being able to repeat results and the inferences drawn from them (D1, 3.27)',
           beneficiaryDefinition='whether someone else could get the same results and conclusions from your work',
           scopeNote='named with openness and transparency in spatial data analysis', category='unknown', practices=['geography'])]
B2A = [dict(concept='geocapabilities', form='geocapabilities', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='reproducibility', form='reproducibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal')]
B4 = []
B5 = []
D3 = [dict(source='Royal Geographical Society (with IBG): programme accreditation criteria and Chartered Geographer requirements', why='SB5 requirements; S7'),
      dict(source='QAA Subject Benchmark Statement: Geography, fourth edition (2019)', why='S7 supersedes; edition comparison')]

E = [
    'Rung shape: one table (4.8) listing each outcome once under Threshold, Typical and Excellent columns, flattened in the held text in three blocks; recorded as one record per rung on each cell (batch 1 convention), ids 4.8.b5 to 4.8.b26 with .typical and .excellent. Unlike Psychology (separate lists per rung).',
    'Rung prose: 4.5, 4.6 and 4.7 summarise the threshold, typical and excellent graduate; recorded as rung records with gradeOf stated (4.6 "distinguished from the threshold level"; 4.7 "beyond the typical standard"). Their domain is set to understanding for want of a mixed value: P3 to confirm.',
    'Force: threshold cells take "threshold" from 4.1 (the minimum a student will have demonstrated for honours). The table lead-in (4.4, "expresses performance") has no modal, so typical and excellent cells and 4.6 and 4.7 are `describes` (forceFrom 4.4). For Abbott: confirm.',
    'Table cells split by page breaks, spans cut at the head only: 4.8.b9.typical and 4.8.b9.excellent (tail "places at various spatial scales." after page 20) and 4.8.b15.typical and 4.8.b15.excellent (tails "in the application of a range of these approaches." and "sophisticated application of a range of these approaches." after page 21). P3 to check the placement of the two tails.',
    'Row placements in the flattened table read by content and order; none uncertain apart from the split cells above. Row 4.8.b11 pairs "carry out routine investigations as instructed" (threshold) with applying concepts (typical, excellent): the issuer pairs them in one row, so gradeOf is stated, but the content match is loose.',
    'Award: the table is stated for "a bachelor\'s degree with honours or integrated master\'s degree" (4.4) with no separate master\'s column; records carry both awards at fheq:6. The integrated master\'s level (fheq:7, fqheis:11, from 2.10) has no wording of its own.',
    'Outcome lists 3.30 and 3.32 to 3.34 are recorded as statements: 3.23 says graduates "are able to demonstrate competence in most of" the skills and attributes itemised, so each item carries force will (forceFrom 3.23) with the "most of" qualifier in every version. P3 to confirm they count as an outcome list (lead-ins say "include").',
    '3.23 itself, the lead-in for those lists, is not cut as a separate record. 4.8.b4 is cut with find: the skeleton span ran into the whole table.',
    'Not cut, plain-present learner descriptions: 3.2 (its four bullets, "appreciate the geographical meanings") and 3.4, 3.6 to 3.12, 3.22, 3.25, 3.27 to 3.29 ("Geographers understand / are aware / are skilled"). They state what geographers know but have no modal; P3 to decide (open point 5).',
    'Not cut, plain-present provider norms: 2.2 ("Course design normally includes"), 2.3, 2.4, 2.11, 2.12, 3.1 ("It is anticipated that single honours degree courses ... address"), 3.13 ("Fieldwork is integral to all Geography courses"), 3.36, 3.38 ("it is anticipated that some form of independent research work is supported").',
    'Obliging words outside the five: "need to" and "responsibility and duty" (1.5, recorded will from "will need to"); "responsible for" and "need to" (2.6, recorded should); "require access" (2.6, 3.14, 3.16, 3.29: needs of resources, not cut); "requires" (3.8 "A geographical education requires that learners examine their own place in the world"; 3.38 "learning requires critical reflection": not cut, for Abbott); "required" (3.15, recorded must); "need to" (3.6, "needs to be an integral part", not cut); "is essential" (2.20, 3.29).',
    '3.21 holds should (resourcing) and must (employers recognising staff capacity) in one paragraph; recorded must, both kept in the versions.',
    '2.21 ("external examiners will be asked to comment") describes typical practice ("Typically"); not cut.',
    'Themes: the front matter names "employability, entrepreneurship and enterprise education" as one cross-cutting theme; recorded under theme:enterprise with 2.14 (employability) in carriedIn. A separate theme:employability id would be new: for Abbott.',
    'Frameworks: FHEQ and FQHEIS (SCQF) cited at 2.10 and 4.2. No CQFW citation; the front matter names the Quality Assessment Framework for Wales and the Quality Enhancement Framework in Scotland, quality regimes not qualification frameworks.',
    'Bodies and organisations: RGS-IBG (2.18; section 5). Advance HE appears only as co-author of the ESD guidance (1.10). Office for Students and the Disabled Students\' Commission appear only in excluded matter. The PSRBs and learned societies named generically in the front matter are not bodies.',
    'Inferred: subjects codes hecos 100409 geography and cah CAH26-01-01 (the text names the subject, not the codes); statedSubjects physical and human geography codes 100410 and 100478. P3 to confirm.',
    'Inferred: spine:6 and the fheq:6 to spine:6 crosswalk, from std:ref:uk-framework R2.',
    'Framework pointers in each author-agent-written instruction (qaa/fheq-2024/4.15.*, Annex D bands) are our reading of the nearest descriptor; typical cells are set beside both the 2.2 and 2.1 bands. P3 to check.',
    'Educational aside: the issuer cites Walkington and others (2018) on geocapabilities (back matter): pedagogy named for theory ingest.',
    'Unknown: S9 commentary not researched.',
]
