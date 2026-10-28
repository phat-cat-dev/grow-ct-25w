# bm_content.py: run 0111, QAA Subject Benchmark Statement: History of Art, Architecture and Design (April 2026). std.
# Judgement file for tools/bm_build.py (BM-BRIEF 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Written fresh from the held text alone; no consuming project's files read (benchmark rule 6).

HON = "bachelor's with honours"
MAS = "master's"
CITE = '(QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para %s)'

META = dict(
    run='0111', p1='2026-10-03 17:29',
    title='Subject Benchmark Statement: History of Art, Architecture and Design',
    heading='Subject Benchmark Statement: History of Art, Architecture and Design (QAA, April 2026)',
    edition='April 2026 (fifth edition)', published='2026-04',
    status='current', supersedes='the fourth edition, 2019 (minor update), as the back matter records',
    subjects=[
        dict(scheme='hecos', code='100306', label='history of art', basis='stated'),
        dict(scheme='hecos', code='100782', label='history of architecture', basis='stated'),
        dict(scheme='hecos', code='100783', label='history of design', basis='stated'),
        dict(scheme='cah', code='CAH20-01-02', label='history of art, architecture and design', basis='stated'),
    ],
    awards=[HON, MAS], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2026 revision (fifth edition for this subject)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate in the history of art, architecture and design (HAAD) "
                     "can be expected to know and do at the end of an honours degree, with a short list for master's graduates. "
                     "It holds a two-rung table (threshold and typical) across subject knowledge, subject-specific skills and "
                     "generic intellectual skills, a list of transferable skills and a master's list. Reach for it when designing, "
                     "reviewing or describing a HAAD course or its outcomes. It is not a curriculum and not a regulatory requirement "
                     "in England."),
    summary=("Published by QAA in April 2026 as the fifth edition, the statement describes the subject's purposes and "
             "characteristics (the study of artefacts as visual and material culture, in every medium and period), the "
             "distinctive features of courses (design, progression, flexibility, partnerships, monitoring), content, teaching "
             "and assessment, and benchmark standards for the bachelor's degree with honours at two rungs, threshold "
             "(equivalent to a third) and typical (equivalent to a second), plus transferable skills and a master's list. "
             "It carries five cross-cutting themes: equity, diversity and inclusion; accessibility and the needs of disabled "
             "students; education for sustainable development; employability, entrepreneurship and enterprise education; and "
             "generative AI. It points to Annex D of the Frameworks for the four honours classes, cites the FHEQ and the "
             "FQHEIS (SCQF) for levels, and names PSRBs and the Equality and Human Rights Commission without naming a "
             "subject body."),
    authority=('reference: a sector-owned reference point; in England not a sector-recognised standard under the OfS '
               'regulatory framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland '
               '(D1, front matter: Relationship to legislation)'),
)

S2 = dict(
    governs=("what a HAAD graduate can be expected to know, do and understand at the end of an honours degree, with "
             "postgraduate standards for the master's degree, and the nature of awards in the subject "
             "(D1, front matter: About this Statement; 4.1; 4.4; 4.6)"),
    awards=["bachelor's degree with honours", "integrated master's (described, 2.6, 2.12)", "master's degree (4.4, 4.6)",
            "joint and combined honours (2.8)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This QAA Subject Benchmark Statement for History of Art, Architecture and Design defines what can be '
                 'expected of a graduate in terms of what they might know, do and understand at the end of their studies." '
                 '(D1, front matter: About this Statement)'),
    doesNot=('it does not prescribe approaches to teaching, learning or assessment; it does not interpret legislation or carry '
             'statutory or regulatory requirements; its threshold standards are not universal competence standards '
             '(D1, front matter; 4.3)'),
    statedSubjects=[
        dict(name='History of Art, Architecture and Design (HAAD)', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100306', label='history of art'),
                    dict(scheme='hecos', code='100782', label='history of architecture'),
                    dict(scheme='hecos', code='100783', label='history of design'),
                    dict(scheme='cah', code='CAH20-01-02', label='history of art, architecture and design')]),
        dict(name='Fine Art', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100059', label='fine art')]),
        dict(name='Design', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100048', label='design')]),
        dict(name='Architecture', locator='(D1, 1.2; 1.15)', kind='programme title',
             codes=[dict(scheme='hecos', code='100122', label='architecture')]),
        dict(name='History, Museum and Heritage Studies', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100302', label='history'), dict(scheme='hecos', code='100918', label='museum studies'),
                    dict(scheme='hecos', code='100805', label='heritage studies')]),
        dict(name='Curatorial Practice', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100914', label='curatorial studies')]),
        dict(name='Photography, Film and Media Studies', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100063', label='photography'), dict(scheme='hecos', code='100058', label='film studies'),
                    dict(scheme='hecos', code='100444', label='media and communication studies')]),
        dict(name='Area Studies, Social Sciences and Humanities', locator='(D1, 1.2)', kind='programme title', codes=[]),
        dict(name='combined or joint degree (including major and minor options)', locator='(D1, 2.8)', kind='programme title',
             codes=[dict(scheme='cah', code='CAH20-01-02', label='history of art, architecture and design')]),
    ],
)

SECTIONS = {
    '1': 'Context and purposes of a History of Art, Architecture and Design degree',
    '2': 'Distinctive features of HAAD courses',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.3', '1.9', 'Purposes and characteristics of a History of Art, Architecture and Design degree'),
    ('1.10', '1.12', 'Equity, diversity and inclusion'),
    ('1.13', '1.15', 'Accessibility and the needs of disabled students'),
    ('1.16', '1.18', 'Education for sustainable development'),
    ('1.19', '1.21', 'Employability, entrepreneurship and enterprise education'),
    ('1.22', '1.26', 'Generative artificial intelligence'),
    ('2.1', '2.5', 'Design'),
    ('2.6', '2.9', 'Progression'),
    ('2.10', '2.14', 'Flexibility'),
    ('2.15', '2.17', 'Partnerships'),
    ('2.18', '2.21', 'Monitoring and review'),
    ('3.2', '3.5', 'Content'),
    ('3.6', '3.8', 'Teaching and learning'),
    ('3.9', '3.13', 'Assessment'),
    ('4.1', '4.4', 'Introduction'),
    ('4.5', '4.5', 'Transferable skills'),
    ('4.6', '4.6', "Master's level"),
]

G = {
    '1.1': 'the subject studies how images, objects and buildings shape societies',
    '1.2': 'an established field taught alone and inside many other degrees',
    '1.3': 'artefacts named by medium, from painting to games',
    '1.4': 'art and design read as historical constructs; global scope',
    '1.5': 'descriptive methods for the visual and material',
    '1.6': 'context, sources and the making and use of artefacts',
    '1.7': 'power, inequality and marginalised histories; sustainability',
    '1.8': 'display, institutions and digital access',
    '1.9': 'varied entrants; skills and careers of graduates',
    '1.10': 'a safe environment beyond equality law',
    '1.11': 'inclusive, object-centred learning and provenance',
    '1.12': 'communities shaping the subject; wellbeing benefits',
    '1.13': 'accessible methods and reasonable adjustment',
    '1.14': 'varied delivery, off-campus study and digital tools',
    '1.15': 'no prerequisites; portfolios; widening participation',
    '1.16': 'artefacts and the UN goals',
    '1.17': 'global links, resource use and sensitive artefacts',
    '1.18': 'environmental cost of travel and digital technology',
    '1.19': 'what enterprise education does for students',
    '1.20': 'cultural economy and the museum and heritage sectors',
    '1.21': 'experiential tasks, placements and graduate destinations',
    '1.22': 'guidance to students on generative AI',
    '1.23': 'generative AI and questions of authorship and creativity',
    '1.24': 'critical engagement with and disclosure of AI use',
    '1.25': 'AI fluency and informed choices about use',
    '1.26': 'AI in assessment: openings and concerns',
    '2.1': 'range of periods, places, media and issues in design',
    '2.2': 'visual literacy, interdisciplinarity and transferable skills',
    '2.3': 'course design for year-on-year progression',
    '2.4': 'digital resources and site-based learning',
    '2.5': 'balanced, aligned assessment portfolio',
    '2.6': 'progression through levels to the threshold',
    '2.7': 'readiness for postgraduate study',
    '2.8': 'joint and combined degrees',
    '2.9': 'early exit awards',
    '2.10': 'bachelor\'s length outside Scotland',
    '2.11': 'Scottish degree structure and the MA title',
    '2.12': 'integrated master\'s length and level',
    '2.13': 'part-time credit',
    '2.14': 'modes of study and credit accumulation',
    '2.15': 'formal and informal partnerships',
    '2.16': 'inclusive, safe, contracted partnership learning',
    '2.17': 'partnerships for employability and hosts',
    '2.18': 'monitoring, evaluation and the student voice',
    '2.19': 'external reviewers in periodic review',
    '2.20': 'the external examining system',
    '2.21': 'professional accreditation of vocational courses',
    '3.1': 'what the section covers',
    '3.2': 'diverse content set by local circumstance',
    '3.3': 'from core skills to a final-year project',
    '3.4': 'research-informed teaching and collections partnerships',
    '3.5': 'historiography, physical properties and current contexts',
    '3.6': 'competences built through varied formats',
    '3.7': 'inclusive design and study visits',
    '3.8': 'indicative teaching methods and approaches',
    '3.9': 'assessment within learning; handbooks',
    '3.10': 'effective, flexible, aligned assessment',
    '3.11': 'self- and peer assessment',
    '3.12': 'generative AI and the assessment portfolio',
    '3.13': 'indicative assessment methods; inclusive by design',
    '4.1': 'what the standards set out',
    '4.2': 'performance above threshold; Annex D',
    '4.3': 'not competence standards; EHRC guidance',
    '4.4': 'two rungs defined; the threshold and typical table',
    '4.5': 'transferable skills on graduating with honours',
    '4.6': 'outcomes on graduating with a master\'s',
}

CTYPE = {
    '1.3': 'area', '1.5': 'area', '3.2': 'area', '3.5': 'area',
    '1.14': 'practice', '2.4': 'practice', '2.5': 'practice', '3.4': 'practice', '3.6': 'practice', '3.7': 'practice',
    '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice',
}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='Membership of the Advisory Group (2026, 2019, 2016, 2007, 2002)', kind='other: back matter, read for S7 and S8'),
    dict(number='none', heading='Fifth Edition; Published 16 April 2026; copyright notice', kind='other: colophon, read for S1 and S8'),
]

P = {}


def s(i, **k):
    P[i] = k


# ------------------------------------------------------------------ agent instructions
FWLABEL = {'threshold': 'the threshold standard, the minimum an honours graduate must show (equivalent to a third)',
           'typical': 'the typical standard, which most honours graduates will reach (equivalent to a second)'}


def aaw_rung(n, rung, about, pair, fw):
    tail = '' if rung == 'threshold' else ', and do not present it as the pass standard'
    return ("Present this as %s for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): %s. "
            "Cite it as %s, naming the %s column. "
            "Do not call it a regulatory requirement or apply it to another award or level%s. "
            "Set it beside %s, %s and the reference framework's spine:6." % (FWLABEL[rung], about, CITE % n, rung, tail, pair, fw))


def aad_rung(rung, when, ask):
    if rung == 'threshold':
        avoid = 'and do not suggest the threshold is what most students aim for'
        plain = 'the least you need to show to pass the honours degree'
    else:
        avoid = 'and never present this typical standard as the minimum for a pass'
        plain = 'what most students reach, above the pass line'
    return ("Raise this when %s. With a student, put it in plain second-person words as %s; with staff, frame it as what modules "
            "must give students the chance to show. Ask: \"%s\" Avoid reading the issuer's wording aloud %s." % (when, plain, ask, avoid))


def row(k, dom, t, y, when):
    """one row of the 4.4 table: threshold cell 4.4.b<k>, typical cell 4.4.b<k>.typical (gradeOf stated: same row)."""
    ti, yi = '4.4.b%d' % k, '4.4.b%d.typical' % k
    s(ti, find=t['find'], type='threshold', rung='threshold', force='threshold', forceFrom='4.4', level='fheq:6',
      appliesTo='honours graduates at the threshold', addressee='learner', verbs=t['verbs'], about=t['about'], domain=dom, award=HON,
      para=t['para'], prac=t['prac'], ben=t['ben'],
      aaw=aaw_rung('4.4', 'threshold', t['about'], 'its typical cell (%s)' % yi, t['fw']),
      aad=aad_rung('threshold', when, t['ask']))
    s(yi, find=y['find'], type='typical', rung='typical', force='will', forceFrom='4.1', level='fheq:6',
      appliesTo='honours graduates at the typical level', addressee='learner', verbs=y['verbs'], about=y['about'], domain=dom, award=HON,
      para=y['para'], prac=y['prac'], ben=y['ben'],
      aaw=aaw_rung('4.4', 'typical', y['about'], 'its threshold cell (%s)' % ti, y['fw']),
      aad=aad_rung('typical', when, y['ask']))
    GRADE[yi] = ti + '|stated'
    OUT.append(dict(outcome=t['out'], threshold=ti, typical=yi, excellent='none', basis='stated', domain=dom, award=HON))


GRADE = {}
OUT = []
T = 'To reach the minimum standard, '
Y = 'At the typical standard, '

# ---- 4.4 Subject knowledge, understanding and skills
row(1, 'knowledge', dict(
    find='Analyse and interpret the visual and material culture of more than one geographical region and/or chronological period.',
    verbs=['analyse', 'interpret'], about='visual and material culture of more than one region or period', out='range of cultures studied',
    para='At threshold, can analyse and interpret the art and objects of at least two regions or periods.',
    prac='At threshold, graduates analyse and interpret artefacts from more than one region or period, so the curriculum spans at least two.',
    ben=T + 'you will analyse and interpret art, buildings and objects from at least two parts of the world or periods of history.',
    ask='Which regions or periods have you analysed so far, and could you interpret an artefact from each?',
    fw='qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd'),
    dict(find='Devise and sustain arguments relating to the knowledge and understanding of the visual and material culture of more than one geographical region and/or chronological period.',
         verbs=['devise', 'sustain'], about='arguments about the culture of more than one region or period',
         para='At the typical level, will build and hold arguments about the visual and material culture of at least two regions or periods.',
         prac='At the typical level, graduates will construct and sustain arguments grounded in knowledge of artefacts from more than one region or period.',
         ben=Y + 'you will build and keep up your own arguments about art and objects from at least two places or periods.',
         ask='Can you build an argument of your own about artefacts from two different regions or periods, not only describe them?',
         fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and 2.1'),
    'a student or team asks how wide the geographical or historical range of study needs to be')
row(2, 'knowledge', dict(
    find='Describe and comment upon the materials and techniques through which artefacts are constructed in the cultures studied.',
    verbs=['describe', 'comment'], about='materials and making techniques of artefacts', out='materials and techniques',
    para='At threshold, can describe and remark on the materials and making techniques of artefacts in the cultures studied.',
    prac='At threshold, graduates describe how artefacts in the cultures they study were made and from what, and comment on those materials and techniques.',
    ben=T + 'you will describe what artefacts were made from and how, and comment on those materials and methods.',
    ask='Pick an artefact you have studied: what is it made of, and how was it made?',
    fw='qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd'),
    dict(find='Devise and sustain arguments relating to the knowledge and understanding of the materials and techniques through which artefacts are constructed in the cultures studied.',
         verbs=['devise', 'sustain'], about='arguments from knowledge of materials and techniques',
         para='At the typical level, will build and hold arguments from knowledge of how and from what the artefacts of the cultures studied were made.',
         prac='At the typical level, graduates will argue from a grasp of materials and making processes, not only describe them.',
         ben=Y + 'you will use what you know about materials and making methods to build and sustain your own arguments.',
         ask='How does what an object is made of change the argument you make about it?',
         fw='qaa/fheq-2024/4.15.b3.1'),
    'a student is writing about how an object was made or a team plans material or technical study')
row(3, 'understanding', dict(
    find='Follow current debates and approaches to the discipline.',
    verbs=['follow'], about='current debates and approaches in the discipline', out='current debates',
    para="At threshold, can keep up with the discipline's present debates and approaches.",
    prac='At threshold, graduates keep track of current debates and approaches in the discipline.',
    ben=T + 'you will keep up with the current debates and ways of working in your subject.',
    ask='Which current debate in the discipline could you summarise for someone new to it?',
    fw='qaa/fheq-2024/4.15.b3.2'),
    dict(find='Demonstrate sound knowledge of current debates and approaches to the discipline and accurately deploy established techniques of interpretation.',
         verbs=['demonstrate', 'deploy'], about='sound knowledge of debates; accurate interpretive technique',
         para="At the typical level, will show secure knowledge of the discipline's present debates and approaches and use its recognised methods of interpretation accurately.",
         prac="At the typical level, graduates will know current debates and approaches soundly and apply the discipline's established interpretive techniques with accuracy.",
         ben=Y + "you will know the current debates well and use the subject's recognised ways of interpreting artefacts accurately.",
         ask='Which interpretive technique do you use most, and how do you check you are using it accurately?',
         fw='qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b3.2'),
    'a student asks how far they need to follow scholarship beyond the reading list')
row(4, 'knowledge', dict(
    find='Demonstrate some familiarity with professional practice in the arts and creative cultural industries, including museums, galleries and the heritage sector.',
    verbs=['demonstrate'], about='some acquaintance with how the arts and heritage sectors work', out='professional practice',
    para='At threshold, will show some acquaintance with professional practice in the arts and cultural industries, such as museums, galleries and heritage.',
    prac='At threshold, graduates have some familiarity with how museums, galleries, heritage bodies and the creative industries work.',
    ben=T + 'you will know something of how museums, galleries, heritage sites and the creative industries work.',
    ask='What have you seen of how a museum, gallery or heritage site actually works?',
    fw='qaa/fheq-2024/4.15.b9.1'),
    dict(find='Engage with professional practice in the arts and creative cultural industries, including museums, galleries and the heritage sector that can be used to devise arguments and solve problems.',
         verbs=['engage', 'devise', 'solve'], about='using professional practice to argue and solve problems',
         para='At the typical level, will engage with professional practice in museums, galleries, heritage and the creative industries and draw on it to argue and solve problems.',
         prac='At the typical level, graduates will engage with professional practice across the arts, heritage and creative sectors and use it to build arguments and tackle problems.',
         ben=Y + 'you will engage with how museums, galleries, heritage and creative organisations work and use that to make arguments and solve problems.',
         ask='Where have you used something from professional practice to answer a question or solve a problem in your work?',
         fw='qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/2.2'),
    'a student asks about placements, curatorial work or careers in the sector, or a team plans partnership learning')
row(5, 'understanding', dict(
    find='Analyse the ways art, design and architecture contribute to and reflect upon the formation of cultures and identities.',
    verbs=['analyse', 'contribute', 'reflect'], about='how art, design and architecture shape cultures and identities', out='cultures and identities',
    para='At threshold, can analyse how art, design and architecture help shape, and comment on, cultures and identities.',
    prac='At threshold, graduates analyse the part art, design and architecture play in forming cultures and identities, and how they mirror that formation.',
    ben=T + 'you will analyse how art, design and buildings help to shape cultures and identities and respond to them.',
    ask='Choose a building, design or artwork: how did it help shape who a community thought it was?',
    fw='qaa/fheq-2024/4.15.b7'),
    dict(find='Apply theories to the ways art, design and architecture contribute to and reflect upon the formation of cultures and identities.',
         verbs=['apply', 'contribute', 'reflect'], about='theory applied to art, culture and identity',
         para='At the typical level, will apply theory to how art, design and architecture shape and reflect cultures and identities.',
         prac='At the typical level, graduates will bring theory to bear on the role of art, design and architecture in forming and reflecting cultures and identities.',
         ben=Y + 'you will use theory to explain how art, design and buildings shape and mirror cultures and identities.',
         ask='Which theory would you use to explain that, and why that one?',
         fw='qaa/fheq-2024/4.15.b3.1'),
    'a student is working on identity, representation or the social role of art')

# ---- 4.4 Subject-specific skills and abilities
row(6, 'subject-skill', dict(
    find='Apply basic skills of observation and visual and material description in analysis.',
    verbs=['apply'], about='basic observation and description in analysis', out='observation and description',
    para='At threshold, can use basic observation and visual and material description when analysing.',
    prac="At threshold, graduates bring basic skills of close looking and of describing artefacts' visual and material qualities into their analysis.",
    ben=T + 'you will look closely at artefacts and describe what you see and what they are made of as part of your analysis.',
    ask='Describe this object to me as if I could not see it: what do you notice first?',
    fw='qaa/fheq-2024/4.15.b2 and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd'),
    dict(find='Deploy skills of observation and visual and material description to the interpretation of artefacts and the elaboration of arguments.',
         verbs=['deploy'], about='observation and description put to interpretation and argument',
         para='At the typical level, will use observation and description of visual and material qualities to interpret artefacts and develop arguments.',
         prac='At the typical level, graduates will deploy close observation and description to interpret artefacts and to elaborate arguments.',
         ben=Y + 'you will use close looking and careful description to interpret artefacts and develop your arguments.',
         ask='How does what you noticed in that description support the argument you are making?',
         fw='qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b7'),
    'a student is learning visual analysis or struggling to move from description to argument')
row(7, 'subject-skill', dict(
    find='Situate artefacts within appropriate environmental, historical and cultural contexts.',
    verbs=['situate'], about='placing artefacts in context, environmental included', out='context',
    para='At threshold, can place artefacts in fitting environmental, historical and cultural contexts.',
    prac='At threshold, graduates place artefacts in suitable environmental, historical and cultural contexts.',
    ben=T + 'you will place artefacts in the right environmental, historical and cultural settings.',
    ask='When and where was this artefact made, and what environment and culture shaped it?',
    fw='qaa/fheq-2024/4.15.b1'),
    dict(find='Situate artefacts within appropriate historical and cultural contexts to advance enquiry within the HAAD disciplines.',
         verbs=['situate', 'advance'], about='context used to advance enquiry',
         para='At the typical level, will place artefacts in fitting historical and cultural contexts so as to move enquiry in the discipline forward.',
         prac='At the typical level, graduates will use historical and cultural context to push enquiry in the discipline forward, not only to label artefacts.',
         ben=Y + 'you will use the historical and cultural setting of artefacts to open up new questions in your subject.',
         ask='What new question does that context open up for you?',
         fw='qaa/fheq-2024/4.15.b6'),
    'a student is contextualising an artefact in an essay or project')
row(8, 'subject-skill', dict(
    find='Use evidence from relevant interdisciplinary sources (visual, verbal, textual, technical, primary and secondary) in relation to current issues and enquiries in the HAAD disciplines.',
    verbs=['use'], about='interdisciplinary evidence on current issues', out='evidence from sources',
    para='At threshold, can use evidence of many kinds from across disciplines, such as images, texts, technical data and primary and secondary material, on current questions in the discipline.',
    prac='At threshold, graduates draw on evidence from several disciplines, visual, spoken, written and technical, original and secondary, in addressing current issues in the field.',
    ben=T + 'you will use evidence from different subjects and kinds of source, such as images, texts, technical data, original and secondary material, on current questions.',
    ask='What kinds of evidence did you use in your last piece of work, and from which subjects?',
    fw='qaa/fheq-2024/4.15.b5'),
    dict(find='Locate, use and evaluate evidence from relevant interdisciplinary sources (visual, verbal, textual, technical, primary and secondary) to advance inquiry within the HAAD disciplines.',
         verbs=['locate', 'use', 'evaluate', 'advance'], about='finding and weighing interdisciplinary evidence',
         para='At the typical level, will find, use and weigh evidence from many kinds of source across disciplines to advance enquiry in the discipline.',
         prac='At the typical level, graduates will locate and critically evaluate evidence from several disciplines themselves and use it to move enquiry forward.',
         ben=Y + 'you will find evidence for yourself across many kinds of source, judge how good it is and use it to move your enquiry on.',
         ask='How did you find that source, and how did you decide it was reliable?',
         fw='qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.2'),
    'a student is gathering sources or a team is designing a research-skills module')
row(9, 'subject-skill', dict(
    find='Demonstrate awareness of methodologies, theories and approaches established in the HAAD discipline areas.',
    verbs=['demonstrate'], about="awareness of the discipline's methods and theories", out='methods and theories',
    para="At threshold, will show awareness of the discipline's established methods, theories and approaches.",
    prac='At threshold, graduates are aware of the established methodologies, theories and approaches of the field.',
    ben=T + 'you will know the main methods, theories and approaches used in your subject.',
    ask='Which methods, such as iconography or formal analysis, could you name and explain?',
    fw='qaa/fheq-2024/4.15.b2'),
    dict(find='Deploy appropriate methodologies, theories and approaches established in the HAAD discipline areas.',
         verbs=['deploy'], about='choosing and using fitting methods and theories',
         para='At the typical level, will use suitable established methods, theories and approaches of the discipline.',
         prac='At the typical level, graduates will choose and deploy fitting methodologies, theories and approaches from the field.',
         ben=Y + 'you will choose and use the right methods, theories and approaches for the task.',
         ask='Which method did you choose for this project, and why does it suit the question?',
         fw='qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6'),
    'a student is choosing a method for an essay or dissertation')
row(10, 'subject-skill', dict(
    find='Show some ability to produce relevant arguments and concepts supported by visual, textual or other appropriate evidence.',
    verbs=['show', 'produce'], about='relevant arguments backed by evidence', out='evidenced argument',
    para='At threshold, will show some ability to make relevant arguments and concepts backed by visual, written or other fitting evidence.',
    prac='At threshold, graduates show some capacity to build relevant arguments and ideas supported by suitable evidence, visual, textual or other.',
    ben=T + 'you will show some ability to make relevant arguments backed by images, texts or other suitable evidence.',
    ask='What is the main claim in your essay, and what evidence supports it?',
    fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd'),
    dict(find='Consistently demonstrate an ability to produce cohesive, well-structured and relevant arguments supported by visual, textual or other appropriate evidence.',
         verbs=['demonstrate', 'produce'], about='consistent, well-built, evidenced argument',
         para='At the typical level, will consistently make coherent, well-organised, relevant arguments backed by fitting visual, written or other evidence.',
         prac='At the typical level, graduates will consistently write arguments that hang together, are well organised and relevant, with suitable supporting evidence.',
         ben=Y + 'you will consistently make clear, well-organised and relevant arguments backed by good evidence.',
         ask='Is every paragraph doing work for that claim, and is that so in all your recent pieces?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and 2.1'),
    'a student asks what makes an argument stronger or why a mark was held back')
row(11, 'subject-skill', dict(
    find='Discern the difference between alternative arguments and approaches.',
    verbs=['discern'], about='telling alternative arguments apart', out='alternative arguments',
    para='At threshold, can tell alternative arguments and approaches apart.',
    prac='At threshold, graduates distinguish between alternative arguments and approaches.',
    ben=T + 'you will be able to tell different arguments and approaches apart.',
    ask='What are two different ways scholars have read this artwork, and how do they differ?',
    fw='qaa/fheq-2024/4.15.b7'),
    dict(find='Demonstrate critical judgement and the ability to evaluate alternative arguments and to engage with competing approaches.',
         verbs=['demonstrate', 'evaluate', 'engage'], about='critical judgement between competing approaches',
         para='At the typical level, will show critical judgement, weighing alternative arguments and engaging with rival approaches.',
         prac='At the typical level, graduates will exercise critical judgement, evaluating alternative arguments and engaging with competing approaches.',
         ben=Y + 'you will judge competing arguments critically and engage with approaches that differ from your own.',
         ask='Which of those readings do you find stronger, and why?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.1'),
    'a student is reviewing scholarship or weighing interpretations')

# ---- 4.4 Generic intellectual skills
row(12, 'generic-skill', dict(
    find='Communicate comprehensibly in a variety of media, using visual aids where necessary.',
    verbs=['communicate', 'using'], about='understandable communication in varied media', out='communication',
    para='At threshold, can communicate understandably in various media, with visual aids where needed.',
    prac='At threshold, graduates communicate comprehensibly across different media, using visual aids when the task calls for them.',
    ben=T + 'you will communicate clearly enough to be understood in different media, using images or other visual aids where they help.',
    ask='In which formats have you presented your work, and did your audience follow it?',
    fw='qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd'),
    dict(find='Communicate effectively in a variety of media with specialist and non-specialist audiences, using visual aids where necessary.',
         verbs=['communicate', 'using'], about='effective communication to expert and lay audiences',
         para='At the typical level, will communicate effectively in various media to specialist and general audiences, with visual aids where needed.',
         prac='At the typical level, graduates will communicate effectively in a range of media for both expert and lay audiences, using visual aids as needed.',
         ben=Y + 'you will communicate well in different media to experts and non-experts alike, using visual aids where they help.',
         ask='How would you change this talk for a general audience rather than your tutors?',
         fw='qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2'),
    'a student is preparing a presentation, video essay or exhibition text')
row(13, 'generic-skill', dict(
    find='Undertake information gathering and basic research with guidance and support.',
    verbs=['undertake'], about='guided information gathering and basic research', out='research',
    para='At threshold, can gather information and carry out basic research with guidance and help.',
    prac='At threshold, graduates gather information and do basic research when guided and supported.',
    ben=T + 'you will gather information and do basic research with guidance and help.',
    ask='How did you find your sources for this piece, and who helped?',
    fw='qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd'),
    dict(find='Conduct self-directed research demonstrating a capacity for effective and verifiable information retrieval, critical review and organisation relevant to a given task.',
         verbs=['conduct', 'demonstrating'], about='self-directed, verifiable research',
         para='At the typical level, will carry out self-directed research, retrieving information effectively and verifiably, reviewing it critically and organising it for the task.',
         prac='At the typical level, graduates will direct their own research, finding information reliably and traceably, reviewing it critically and organising it to suit the task.',
         ben=Y + 'you will lead your own research, finding information in ways others can check, reviewing it critically and organising it for the task.',
         ask='Could someone else retrace how you found your sources?',
         fw='qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.1'),
    'a student is starting independent research or a dissertation')
row(14, 'generic-skill', dict(
    find='Display open-mindedness: be receptive to unfamiliar artefacts, issues, values and ideas.',
    verbs=['display'], about='open-mindedness to the unfamiliar', out='open-minded and inclusive interpretation',
    para='At threshold, will show open-mindedness, being open to artefacts, issues, values and ideas they have not met before.',
    prac='At threshold, graduates are open-minded: willing to take seriously artefacts, issues, values and ideas new to them.',
    ben=T + 'you will be open-minded about artefacts, issues, values and ideas you have not met before.',
    ask='What is an artefact or idea you met on the course that was new to you, and how did you approach it?',
    fw='qaa/fheq-2024/4.15.b4'),
    dict(find='Demonstrate the ability to take an inclusive approach to interpretation by taking into account the ideas, contexts and structures out of which various visual and material cultures have arisen.',
         verbs=['demonstrate', 'take', 'taking'], about='inclusive interpretation',
         para='At the typical level, will show they can interpret inclusively, allowing for the ideas, contexts and structures from which different visual and material cultures emerged.',
         prac='At the typical level, graduates will interpret inclusively, taking account of the ideas, settings and structures behind diverse visual and material cultures.',
         ben=Y + 'you will interpret artefacts inclusively, taking account of the ideas, settings and structures behind different cultures.',
         ask='Whose ideas and circumstances shaped this artefact, and have you allowed for them in your reading?',
         fw='qaa/fheq-2024/4.15.b7'),
    'a student meets unfamiliar cultures or contested artefacts')
row(15, 'generic-skill', dict(
    find='Identify underlying values and ethics within culture and society.',
    verbs=['identify'], about='values and ethics in culture and society', out='values and ethics',
    para='At threshold, can identify the values and ethics that underlie culture and society.',
    prac='At threshold, graduates identify the values and ethics underlying culture and society.',
    ben=T + 'you will spot the values and ethics that lie beneath culture and society.',
    ask='What values does this artefact take for granted?',
    fw='qaa/fheq-2024/4.15.b9.1'),
    dict(find='Identify and examine underlying values and ethics within culture and society.',
         verbs=['identify', 'examine'], about='examining values and ethics in culture and society',
         para='At the typical level, will identify and also examine the values and ethics that underlie culture and society.',
         prac='At the typical level, graduates will go beyond naming the values and ethics beneath culture and society to examine them.',
         ben=Y + 'you will not only spot the values and ethics beneath culture and society but examine them.',
         ask='How would you test or question those values?',
         fw='qaa/fheq-2024/4.15.b7'),
    'a student is discussing ethics, provenance or values in art')


# ------------------------------------------------------------------ 4.5 transferable skills (should, honours)
def aaw_45(n, about, fw):
    return ("Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours "
            "at FHEQ Level 6 (FQHEIS Level 10): %s; it is not one of the two rungs. Cite it as %s. "
            "Do not call it a regulatory requirement or a measure of degree class. "
            "Set it beside the generic cells 4.4.b12 to 4.4.b15, %s and spine:6." % (about, CITE % n, fw))


def aad_45(when, ask):
    return ("Raise this when %s. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a "
            "skill modules should build and assess. Ask: \"%s\" Avoid reading the list aloud or treating it as graded." % (when, ask))


def k45(b, find, verbs, about, para, prac, ben, when, ask, fw):
    s('4.5.b%d' % b, find=find, type='outcome', rung='none', force='should', forceFrom='4.5', level='fheq:6',
      appliesTo='honours graduates', addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON,
      para=para, prac=prac, ben=ben, aaw=aaw_45('4.5', about, fw), aad=aad_45(when, ask))


k45(1, 'present knowledge or an argument that is comprehensible to others while\n\n19\ndemonstrating a sound technical proficiency of written English',
    ['present', 'demonstrating'], 'clear presentation in sound written English',
    'Should be able to put knowledge or a case so others can follow it, with technically sound written English.',
    'Graduates should be able to put knowledge or a case across understandably, writing English with sound technical accuracy.',
    'You should be able to explain what you know or argue a case so others can follow it, writing English accurately.',
    'a student asks about writing standards or feedback on expression',
    'Could someone outside your subject follow your last essay, and where did the writing slip?',
    'qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd')
k45(2, 'work as part of a team as an effective collaborator', ['work'], 'effective teamwork',
    'Should be able to collaborate well as a member of a team.',
    'Graduates should be able to collaborate effectively as members of a team.',
    'You should be able to work well with others as part of a team.',
    'group work is set or a group is not working well',
    'What did you contribute to your last group task, and how did the group use it?',
    'Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd')
k45(3, 'research and study effectively in a guided and structured environment', ['research', 'study'],
    'effective study where learning is guided',
    'Should be able to research and study well in a guided, structured setting.',
    'Graduates should be able to research and study well where the learning is guided and structured.',
    'You should be able to research and study well when your learning is guided and structured.',
    'a student is adjusting to university study or planning independent work',
    'Where do you need more structure to study well, and where less?',
    'qaa/fheq-2024/4.15.b5')
k45(4, 'appreciate and engage in contemporary debates relating to culture and society, for example around inequality and sustainability',
    ['appreciate', 'engage'], 'current debates on culture and society',
    'Should be able to value and take part in current debates on culture and society, such as those on inequality and sustainability.',
    'Graduates should be able to appreciate and join contemporary debates about culture and society, for instance on inequality and sustainability.',
    'You should be able to understand and join today\'s debates about culture and society, such as those on inequality and sustainability.',
    'inequality, sustainability or current cultural controversies come up',
    'Which current debate about inequality or sustainability in the arts have you followed, and where do you stand?',
    'qaa/fheq-2024/4.15.b3.2')
k45(5, 'use digital technologies (including GenAI, used and applied ethically) to research, select and communicate information',
    ['use', 'research', 'select', 'communicate'], 'ethical use of digital tools and GenAI',
    'Should be able to use digital technologies, generative AI included and used ethically, to research, choose and convey information.',
    'Graduates should be able to use digital tools, including generative AI applied ethically, to research, select and share information.',
    'You should be able to use digital tools, including generative AI used ethically, to research, choose and share information.',
    'a student asks whether or how to use generative AI or other digital tools',
    'Which digital tools, generative AI included, did you use on your last assignment, and how did you declare that use?',
    'Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd')
k45(6, 'work diligently, to take appropriate decisions and meet assessment deadlines', ['work', 'take', 'meet'],
    'diligence, decisions and deadlines',
    'Should be able to work conscientiously, make sound decisions and keep to assessment deadlines.',
    'Graduates should be able to work diligently, decide appropriately and keep to assessment deadlines.',
    'You should be able to work steadily, make sensible decisions and hand in assessments on time.',
    'a student is struggling with workload or deadlines',
    'How do you plan your work so that you meet deadlines, and what happens when the plan slips?',
    'Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd and qaa/fheq-2024/4.15.b9.2')
k45(7, 'take responsibility for their own work, understanding questions of academic integrity', ['take', 'understanding'],
    'responsibility for own work; academic integrity',
    'Should be able to take responsibility for their work and understand what academic integrity asks of it.',
    'Graduates should be able to own their work and understand the questions of academic integrity it raises.',
    'You should be able to take responsibility for your own work and understand what academic integrity means for it.',
    'referencing, collusion or AI use come up',
    'How do you make sure the work you hand in is your own, and how do you credit what is not?',
    'Annex D qaa/fheq-2024/annex-d/transferable/r4/3rd')
k45(8, 'reflect on their own progress, making appropriate use of feedback to further intellectual development and improve performance',
    ['reflect', 'making'], 'reflection and use of feedback',
    'Should be able to reflect on their progress and use feedback well to develop intellectually and do better.',
    'Graduates should be able to reflect on their progress and use feedback to deepen their thinking and raise their performance.',
    'You should be able to reflect on how you are doing and use feedback to develop your thinking and improve your work.',
    'feedback has just been returned or a student is planning how to improve',
    'What did your last piece of feedback say, and what did you change because of it?',
    'Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd')
k45(9, 'identify and examine underlying values and ethics both within culture and society and on a personal level',
    ['identify', 'examine'], 'values and ethics, personal as well as social',
    'Should be able to identify and examine the values and ethics beneath culture and society and in their own lives.',
    'Graduates should be able to identify and examine the values and ethics in culture, in society and in themselves.',
    'You should be able to spot and question the values and ethics beneath culture, society and your own choices.',
    'a student is reflecting on their own position or on an ethical question in the subject',
    'Which of your own values shapes how you read artefacts?',
    'qaa/fheq-2024/4.15.b7')
k45(10, 'exhibit some awareness of the inherent uncertainty, ambiguities and the limits of knowledge', ['exhibit'],
    'awareness of uncertainty and the limits of knowledge',
    'Should be able to show some awareness that knowledge is uncertain, ambiguous and limited.',
    'Graduates should be able to show some awareness of the uncertainty, ambiguity and limits that come with any knowledge.',
    'You should be able to show some awareness that what we know is uncertain, open to more than one reading and limited.',
    'a student wants a single right answer or evidence runs out',
    'Where in your topic does the evidence run out, and how did you handle that?',
    'qaa/fheq-2024/4.15.b4')


# ------------------------------------------------------------------ 4.6 master's level (should typically)
def aaw_46(about, fw):
    return ("Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): %s. "
            "Cite it as %s. Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. "
            "Set it beside %s and spine:7." % (about, CITE % '4.6', fw))


def aad_46(when, ask):
    return ("Raise this when %s. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame "
            "it as what the course typically develops at Level 7. Ask: \"%s\" Avoid presenting this typical list as the minimum for the award." % (when, ask))


def k46(b, find, verbs, dom, about, para, prac, ben, when, ask, fw):
    s('4.6.b%d.masters' % b, find=find, type='typical', rung='typical', force='should', forceFrom='4.6', level='fheq:7',
      appliesTo="master's graduates", addressee='learner', verbs=verbs, about=about, domain=dom, award=MAS,
      para=para, prac=prac, ben=ben, aaw=aaw_46(about, fw), aad=aad_46(when, ask))


k46(1, 'demonstrate sophisticated and nuanced visual literacy', ['demonstrate'], 'subject-skill', 'refined visual literacy',
    'Should typically be able to show refined, subtle visual literacy.',
    "Master's graduates should typically show sophisticated, nuanced visual literacy.",
    'At master\'s level, you should usually be able to read images and objects with real subtlety and sophistication.',
    'a master\'s student is analysing images or objects in depth',
    'Take an image you know well: what can you now see in it that you missed as an undergraduate?',
    'qaa/fheq-2024/4.17.b1')
k46(2, 'systematically and critically engage with texts and artefacts, as well as theories and methods for examining visual and material culture',
    ['engage'], 'subject-skill', 'systematic, critical work with texts, artefacts and theory',
    'Should typically be able to engage systematically and critically with texts, artefacts and the theories and methods for studying visual and material culture.',
    "Master's graduates should typically work systematically and critically with texts and artefacts and with the theories and methods of the field.",
    "At master's level, you should usually work systematically and critically with texts, objects and the theories and methods used to study them.",
    'a master\'s student is planning a literature or object review',
    'How systematic was your approach to the sources in your last project?',
    'qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b4.2')
k46(3, 'demonstrate awareness of how methodologies and research trends in the discipline have challenged assumptions and interpretations of art, architecture or design',
    ['demonstrate', 'challenged'], 'understanding', 'how methods and research have unsettled received readings',
    "Should typically be able to show how the discipline's methods and research trends have unsettled earlier assumptions and readings of art, architecture or design.",
    "Master's graduates should typically understand how methodological change and research trends have overturned received views and readings in the field.",
    "At master's level, you should usually be able to explain how new methods and research have overturned older assumptions about art, architecture or design.",
    'a master\'s student is writing on historiography or the state of the field',
    'Which older reading in your field has been overturned, and by what kind of research?',
    'qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b4.2')
k46(4, 'use unfamiliar arguments and artefacts constructively, while engaging critically with prominent, familiar or established ideas within the discipline',
    ['use', 'engaging'], 'subject-skill', 'unfamiliar material set against established ideas',
    'Should typically be able to use unfamiliar arguments and artefacts productively while engaging critically with well-known or established ideas.',
    "Master's graduates should typically put unfamiliar arguments and artefacts to good use and question the field's established ideas.",
    "At master's level, you should usually be able to make good use of unfamiliar arguments and objects while questioning the field's established ideas.",
    'a master\'s student is testing a received view',
    'Which established idea in your field have you questioned, and what unfamiliar evidence did you bring?',
    'qaa/fheq-2024/4.17.b3')
k46(5, 'demonstrate advanced knowledge of the place of HAAD in relation to larger social and political contexts',
    ['demonstrate'], 'knowledge', 'the subject in its social and political setting',
    'Should typically be able to show advanced knowledge of how the discipline sits within wider social and political contexts.',
    "Master's graduates should typically show advanced knowledge of the subject's place in wider social and political contexts.",
    "At master's level, you should usually know in depth how your subject connects with wider social and political questions.",
    'a master\'s student asks why the subject matters beyond the academy',
    'How does your research topic connect with a current social or political question?',
    'qaa/fheq-2024/4.17.b1')
k46(6, 'form a systematic and critically engaged approach to the representation of art in museums, galleries and the heritage sector',
    ['form'], 'subject-skill', 'a critical approach to display and representation',
    'Should typically be able to develop a systematic, critical approach to how art is represented in museums, galleries and heritage.',
    "Master's graduates should typically form a systematic, critically engaged view of how museums, galleries and heritage bodies represent art.",
    "At master's level, you should usually have a systematic and critical way of looking at how museums, galleries and heritage sites present art.",
    'a master\'s student is studying exhibitions, curating or heritage interpretation',
    'What choices did the last exhibition you saw make about how to present its art, and what did they leave out?',
    'qaa/fheq-2024/4.17.b4.1')
k46(7, 'demonstrate comprehensive grounding in skills of analysis, argument and expression', ['demonstrate'], 'generic-skill',
    'grounding in analysis, argument and expression',
    'Should typically be able to show thorough grounding in analysis, argument and expression.',
    "Master's graduates should typically be comprehensively grounded in analysis, argument and expression.",
    "At master's level, you should usually be thoroughly skilled in analysing, arguing and expressing your ideas.",
    'a master\'s student asks how their writing should change from undergraduate work',
    'Which of analysis, argument or expression is your strongest, and which needs work?',
    'qaa/fheq-2024/4.17.b5')
k46(8, 'assemble data from a variety of relevant primary and secondary sources, and discern connections between them',
    ['assemble', 'discern'], 'generic-skill', 'assembling and connecting sources',
    'Should typically be able to gather data from varied relevant primary and secondary sources and see the links between them.',
    "Master's graduates should typically bring together data from a range of pertinent original and secondary sources and see how they connect.",
    "At master's level, you should usually gather information from many original and secondary sources and see how they connect.",
    'a master\'s student is building an evidence base for a dissertation',
    'How do your primary and secondary sources speak to each other in your project?',
    'qaa/fheq-2024/4.17.b2')
k46(9, 'recognise their own academic strengths and weaknesses, and reflect on their performance and progress',
    ['recognise', 'reflect'], 'generic-skill', 'self-knowledge and reflection',
    'Should typically be able to see where they are strong and weak academically and think about how they are performing and progressing.',
    "Master's graduates should typically know their academic strengths and weak points and review how well they are performing and progressing.",
    "At master's level, you should usually know where you are strong and weak academically and reflect on how you are getting on.",
    'a master\'s student is planning development or responding to feedback',
    'What is one academic weakness you are working on, and how will you know it has improved?',
    'qaa/fheq-2024/4.17.b8.3')
k46(10, 'identify the relationship between different intellectual approaches and choose those appropriate to a particular instance',
    ['identify', 'choose'], 'generic-skill', 'relating approaches and choosing one',
    'Should typically be able to see how different intellectual approaches relate and pick the right one for a given case.',
    "Master's graduates should typically identify how intellectual approaches relate and choose those suited to a particular case.",
    "At master's level, you should usually see how different ways of thinking relate and choose the right one for each case.",
    'a master\'s student is choosing a framework for a project',
    'Why did you choose this approach for your case rather than another?',
    'qaa/fheq-2024/4.17.b4.2')
k46(11, 'carry out a self-directed, original research project', ['carry'], 'subject-skill', 'an original, self-directed research project',
    'Should typically be able to complete an original research project that they direct themselves.',
    "Master's graduates should typically carry out an original, self-directed research project.",
    "At master's level, you should usually carry out an original research project that you lead yourself.",
    'a master\'s student is scoping a dissertation',
    'What is original about your research project, and which decisions in it were yours?',
    'qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6')
k46(12, 'communicate ideas and structured arguments effectively to specialist and non- specialist audiences',
    ['communicate'], 'generic-skill', 'communication to expert and lay audiences',
    'Should typically be able to convey ideas and structured arguments effectively to expert and general audiences.',
    "Master's graduates should typically put across ideas and well-built arguments effectively to both expert and lay audiences.",
    "At master's level, you should usually explain ideas and well-built arguments clearly to experts and non-experts.",
    'a master\'s student is presenting research or writing for the public',
    'How would you present your research to a museum visitor rather than an examiner?',
    'qaa/fheq-2024/4.17.b5')

# ------------------------------------------------------------------ obliging paragraphs (sections 2 to 4)
s('2.3', type='expectation', rung='none', force='will', level='none', appliesTo='course design teams', addressee='provider',
  verbs=['consider', 'provide', 'progress'], about='course design for progression across years', domain='none', award=HON,
  para=("Course design teams use institutional guidance and external reference points for specifications, outcomes, challenge and content; "
        "the design will consider how each year's content and teaching prepares every student to move on to harder problems."),
  prac=("Use institutional guidance and external reference points to set outcomes and challenge; the design will need to show how each year's "
        "content, learning and teaching equips all students for more complex work the next year."),
  ben=('n/a', 'a duty on course design teams; the student meets its effect in how the years build'),
  aaw=("Treat this as an expectation, in will, on course design teams rather than students: a HAAD honours course is designed so each year "
       "readies all students for harder problems. Cite it as " + CITE % '2.3' + " and read it with 3.3, which describes the move from core "
       "skills to a final-year project. Do not present it as a regulatory requirement. Set it beside the level descriptors "
       "qaa/fheq-2024/4.10, 4.12 and 4.15 and spine:4 to spine:6."),
  aad=("Raise this with a programme team planning or reviewing year-by-year structure. Frame it as a design check and ask \"Which skills "
       "does each year introduce, and where does the next year depend on them?\" and \"Could every student, whatever their route in, "
       "make the step up?\" Do not put it to a student as their own task; it describes the course's duty."))
s('2.6', type='expectation', rung='none', force='will', level='none', appliesTo='honours and integrated master\'s students', addressee='learner',
  verbs=['progress', 'include'], about='progression through the levels to the threshold', domain='none', award=[HON, "integrated master's"],
  para=("A student will move up through the levels as each institution's rules set out, each level expected to build knowledge, expertise and "
        "experience towards the threshold (and any higher) subject and generic skills; this will usually mean passing and gaining credit for "
        "all learning and assessment, practical work included."),
  prac=("Plan each level so that students will build towards the threshold skills listed for the award; progression usually depends on "
        "passing and earning credit for every part of the course, practical components included."),
  ben=("You will move up one level each year as your university's rules allow, building towards the skills your degree asks for; usually "
       "that means passing every part of the course, including practical work, and earning its credit."),
  aaw=("Describe this as the expected route, in will, by which an honours student (FHEQ Level 6; FQHEIS Level 10) or an integrated master's "
       "student (FHEQ Level 7; FQHEIS Level 11) progresses towards the threshold standards in 4.4 and 4.5. Cite it as " + CITE % '2.6' + ". "
       "Do not claim it sets progression rules, which stay with each institution. Set it beside the threshold cells 4.4.b1 to 4.4.b15, the "
       "descriptors qaa/fheq-2024/4.10, 4.12, 4.15 and 4.17, and spine:4 to spine:7."),
  aad=("Raise this when a student asks what moving from one year to the next involves, or a team maps credit to levels. Tell a student in "
       "plain words that each year builds towards the skills the degree asks for and that passing every part, practical work included, is "
       "usually needed; ask \"Which parts of this year are you less sure of passing?\" Avoid quoting the institution's regulations as if this "
       "statement set them."))
s('2.8', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students taking HAAD in joint or combined degrees', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint and combined degrees', domain='none', award=HON,
  para=("Students taking HAAD within a joint or combined degree, major and minor routes included, will reach the core of the subject and generic "
        "skills set out here and will add further skills from their other subject or subjects."),
  prac=("In joint, combined and major/minor routes, design the HAAD share so that students will achieve the core subject-specific and "
        "generic skills of this statement, while their other subject adds its own."),
  ben=("If you study HAAD as part of a joint or combined degree, you will gain the core subject and general skills of the field and add "
       "others from your second subject."),
  aaw=("Present this as the expected outcome, in will, for students taking HAAD in a joint, combined or major/minor honours degree at FHEQ "
       "Level 6 (FQHEIS Level 10): the core of the skills in 4.4 and 4.5, not every one of them. Cite it as " + CITE % '2.8' + ". Do not claim "
       "that a joint-honours student must meet every cell of 4.4, or that the statement says which elements are core. Set it beside 4.4, "
       "4.5 and qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a joint-honours student or a team designing a combined route asks how much of the HAAD standard applies. Explain "
       "plainly that the core subject skills still apply and the other subject adds its own; ask \"Which HAAD skills does your route give "
       "you the chance to show, and which come from your other subject?\" Avoid suggesting that joint honours is a lesser standard."))
s('2.18', find=('Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake '
                'periodic course review according to their own needs. Considering the student voice will form part of this.'),
  type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies and their partners', addressee='provider',
  verbs=['collect', 'analyse', 'undertake', 'form'], about='periodic review and the student voice', domain='none', award=HON,
  para=("Degree-awarding bodies and their partners routinely gather and analyse information and review courses periodically to suit their "
        "needs; the student voice will be considered as part of this."),
  prac=("Your periodic course review, alone or with partners, will take account of what students say, alongside the data you routinely "
        "gather and analyse."),
  ben=('n/a', 'a duty on the degree-awarding body in course review'),
  aaw=("Treat this as an expectation, in will, on degree-awarding bodies and their partners: periodic course review takes account of the "
       "student voice. Cite it as " + CITE % '2.18' + ". Do not present it as a student outcome or as a regulatory requirement. Set it beside "
       "2.19 (external reviewers) and the external examining system the statement describes in 2.20."),
  aad=("Raise this with a programme team preparing a periodic review or answering student feedback. Frame it in practitioner terms and ask "
       "\"How did students' views reach this review, and what changed because of them?\" Do not hand it to a student as a task; it is the "
       "institution's duty, though students can be told their views count."))
s('2.19', type='expectation', rung='none', force='will', level='none', appliesTo='providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para=("Externality is essential to UK quality assurance; providers will use external reviewers in periodic review for an independent view "
        "of proposed changes and to make sure threshold standards are met and content suits the subject."),
  prac=("In periodic review you will bring in external reviewers, for an independent view on proposed changes and a check that threshold "
        "standards are met and content fits the subject."),
  ben=('n/a', 'a duty on the provider in periodic review'),
  aaw=("Present this as an expectation, in will, on providers: external reviewers take part in periodic review to check that the threshold "
       "standards (4.4, 4.5) are achieved and content suits the subject. Cite it as " + CITE % '2.19' + ". Do not present it as a learner "
       "outcome. Set it beside 2.18, 2.20 and the threshold cells 4.4.b1 to 4.4.b15."),
  aad=("Raise this when a programme team plans a periodic review or asks who checks its standards. Frame it as practice the team will follow "
       "and ask \"Who is your external reviewer, and which threshold standards will they look at?\" Avoid presenting it to students as "
       "something they must meet."))
s('3.13', find='Assessment methods will be inclusive by design. Considerations for accessibility and inclusivity will determine forms of assessment.',
  type='expectation', rung='none', force='will', level='none', appliesTo='those who design assessment', addressee='provider',
  verbs=['determine'], about='inclusive, accessible assessment design', domain='none', award=HON,
  para='Assessment methods will be inclusive from the outset, and accessibility and inclusion will shape which forms of assessment are used.',
  prac=("Design assessment to be inclusive from the start: accessibility and inclusion will decide which forms of assessment you use, "
        "rather than being added afterwards."),
  ben=('n/a', 'a duty on those who design assessment; the student meets its effect'),
  aaw=("Treat this as an expectation, in will, on those who design assessment on a HAAD course: methods are inclusive by design and "
       "accessibility shapes their form. Cite it as " + CITE % '3.13' + " and read it with the accessibility paragraphs 1.13 to 1.15. Do not "
       "present the indicative list of methods in 3.13 as required. Set it beside 3.10, 3.11 and the Equality Act 2010 duties the statement "
       "cites in 1.13."),
  aad=("Raise this when a team is choosing or revising assessment, or a disabled student asks about adjustments. With staff, ask \"Was "
       "accessibility decided before this assessment was set, or added afterwards?\"; with a student, explain in plain words that assessment "
       "should be designed with their needs in mind and point them to the course's support. Avoid giving the student this as a duty of their own."))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers', addressee='provider',
  verbs=['perform', 'refer'], about='evidence above threshold; Annex D', domain='none', award=HON,
  para=("Most students will do far better than the minimum threshold; each provider decides how to evidence that achievement and should "
        "refer to Annex D of the Frameworks, which describes the four honours classes (1st, 2.1, 2.2, 3rd)."),
  prac=("To evidence achievement above threshold, you should use Annex D of the Frameworks, its descriptions of first, upper second, lower "
        "second and third-class honours, alongside your own method."),
  ben=('n/a', 'a duty on the provider in judging and classifying achievement; the student meets it through marks and class'),
  aaw=("Treat this as a duty, in should, on each provider: to judge achievement above threshold it refers to Annex D of the Frameworks "
       "(std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/summary/r1/3rd to 1st). Cite it as " + CITE % '4.2' + ". Do not claim the "
       "statement itself sets class boundaries or mark bands. Set it beside the threshold and typical cells of 4.4, the Annex D bands (SL6 of "
       "the FHEQ document) and the band axis of std:ref:uk-assesscriteria."),
  aad=("Raise this when a team writes marking criteria or asks how the threshold and typical rungs relate to degree classes. Frame it for "
       "staff: threshold sits at the third-class line and typical at second class, while Annex D describes all four classes; ask \"Do your criteria "
       "for a 2.1 and a first say more than the typical cells do?\" Avoid telling students that most of them will exceed the threshold as if it "
       "were a promise."))
s('4.3', type='requirement', rung='none', force='should', level='none', appliesTo='providers that develop competence standards', addressee='provider',
  verbs=['follow'], about='competence standards and EHRC guidance', domain='none', award=HON,
  para=("The minimum threshold standards do not set universal competence standards; a provider that develops competence standards under the "
        "Equality Act 2010 may draw on the statement and PSRB requirements, and should follow the latest Equality and Human Rights Commission guidance."),
  prac=("The threshold standards are not competence standards; if you set competence standards in a programme specification, inform them "
        "from this statement and any PSRB requirements, and you should follow the current Equality and Human Rights Commission guidance."),
  ben=('n/a', 'a duty on the provider in writing competence standards'),
  aaw=("Treat this as a duty, in should, on any provider that writes competence standards (in the Equality Act 2010 sense) for a HAAD "
       "programme: follow current Equality and Human Rights Commission guidance. Cite it as " + CITE % '4.3' + ". Do not describe the threshold "
       "cells of 4.4 as competence standards or as universal requirements. Set it beside 4.4, 4.2 and the accessibility paragraphs 1.13 to 1.15."),
  aad=("Raise this when a programme team is drafting competence standards or a disabled student's adjustment turns on what is truly "
       "required. Frame it for staff and ask \"Is this a genuine competence standard, and have you checked it against the Commission's "
       "current guidance?\" Avoid presenting threshold standards to a student as fixed competences that rule out adjustments."))

TH = {}

S5 = dict(
    levels=[
        dict(id='fheq:4', role='cites', locator='D1, 2.9 (Certificate of Higher Education)'),
        dict(id='fheq:5', role='cites', locator='D1, 2.9 (Diploma of Higher Education)'),
        dict(id='fheq:6', role='cites', locator='D1, 2.6; 2.10; 2.12; 2.15'),
        dict(id='fheq:7', role='cites', locator='D1, 2.6; 2.12; 2.15; 4.4'),
        dict(id='fqheis:8', role='cites', locator='D1, 2.9 (as the statement gives it for the CertHE: Part E)'),
        dict(id='fqheis:9', role='cites', locator='D1, 2.9 (DipHE, as stated: Part E); 2.11 (ordinary degree and MA)'),
        dict(id='fqheis:10', role='cites', locator='D1, 2.6; 2.11; 2.12'),
        dict(id='fqheis:11', role='cites', locator='D1, 2.6; 2.12; 4.4'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
             basis='stated (D1, 2.6; 2.12: the honours degree at FHEQ Level 6 and FQHEIS Level 10); agrees with FHEQ Table 1'),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent',
             basis="stated (D1, 2.6; 2.12; 4.4: master's at Level 7 in England, Wales and Northern Ireland and Level 11 in Scotland); agrees with FHEQ 4.17"),
        dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent',
             basis='stated (D1, 2.9: CertHE at FHEQ Level 4, FQHEIS Level 8); differs from FHEQ Table 1, which puts the CertHE at FQHEIS 7 (Part E)'),
        dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent',
             basis='stated (D1, 2.9: DipHE at FHEQ Level 5, FQHEIS Level 9); differs from FHEQ Table 1, which puts the DipHE at FQHEIS 8 (Part E)'),
    ],
)

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.7', '1.10', '1.11', '1.12', '1.13', '2.16', '3.7', '3.13', '4.3', '4.4', '4.5']),
    dict(id='theme:accessibility', role='carries', carriedIn=['1.13', '1.14', '1.15', '2.16', '3.8', '3.13']),
    dict(id='theme:esd', role='carries', carriedIn=['1.7', '1.8', '1.16', '1.17', '1.18', '1.23', '1.26', '4.4', '4.5']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.19', '1.20', '1.21', '1.25', '2.2', '2.17']),
    dict(id='theme:generative-ai', role='carries', carriedIn=['1.14', '1.18', '1.22', '1.23', '1.24', '1.25', '1.26', '3.6', '3.8', '3.12', '4.5']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-history-of-art-architecture-and-design-2019-benchmarks (not ingested)',
         note='the fourth edition, 2019 minor update; earlier editions 2016, 2007 and 2002 (back matter)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
         note='the degree classification descriptions for bachelor\'s degrees with honours (4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Levels 4 to 7 (2.6, 2.9, 2.10, 2.12, 2.15)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS (SCQF) Levels 8 to 11 (2.6, 2.9, 2.11, 2.12; 4.4 by level number)'),
    dict(rel='refersTo', target='QAA Quality Code, 2024 update (not ingested)', note='front matter'),
    dict(rel='refersTo', target='Equality and Human Rights Commission guidance on competence standards (not ingested)', note='4.3'),
]

SB1 = [
    'Studies artefacts as visual and material culture in every medium, from painting, sculpture and buildings to applied arts, performance, photography, film, social media and games, past and present (D1, 1.3, 1.5).',
    'Joins close description (formal, iconographic, semiotic, material, spatial or functional analysis) with critical study of context, making, patronage and use (D1, 1.5, 1.6).',
    'Reads "art" and "design" as historical categories shaped by colonialism, the Enlightenment and modern institutions, and examines inequalities of power and histories pushed to the margins (D1, 1.4, 1.7, 1.11).',
    'Interdisciplinary by nature, drawing on archives, literary texts and scientific analysis across the arts, humanities and sciences (D1, 1.6, 2.2).',
    'Display is part of the subject: museums, galleries, heritage sites and digital display shape how artefacts are received, and many partner with courses (D1, 1.8, 3.4).',
    'Object-based learning and visual and material literacy are its signature skills, built through study visits, collections and handling (D1, 2.2, 3.5, 3.8).',
    'Taught as single honours and as a component of many other degrees, among them fine art, design, architecture, heritage, curating and media (D1, 1.2).',
]

SB2 = [
    dict(theme='theme:edi', inThisSubject=("the subject examines power, class, race, gender, sexuality and health in artefacts, recentres marginalised voices, "
                                           "questions Eurocentric narratives and object provenance, and ties inclusive environments to the Equality Act and "
                                           "partnership practice (D1, 1.7, 1.10 to 1.12, 2.16); inclusive interpretation is a typical generic skill (4.4)"),
         statements=['3.13', '4.3', '4.4.b14.typical', '4.5.b4']),
    dict(theme='theme:accessibility', inThisSubject=("accessible teaching and assessment, hybrid delivery and reasonable adjustment under equality law; no "
                                                     "prerequisites and portfolio entry; assessment inclusive by design (D1, 1.13 to 1.15, 3.13)"),
         statements=['3.13']),
    dict(theme='theme:esd', inThisSubject=("artefacts as vehicles for the UN goals; the environmental cost of making, conserving, travelling to and digitising "
                                           "artefacts; environmental context is part of the threshold skill of situating artefacts (D1, 1.16 to 1.18; 4.4)"),
         statements=['4.4.b7', '4.5.b4']),
    dict(theme='theme:enterprise', inThisSubject=("the cultural economy and art markets, experiential and partnership learning, curatorial and public "
                                                  "programming tasks, and graduate routes into museums, heritage and creative industries (D1, 1.19 to 1.21, 2.17)"),
         statements=[]),
    dict(theme='theme:generative-ai', inThisSubject=("guidance and disclosure of use, questions of authorship and creativity, critical AI fluency, new "
                                                     "assessment forms and concerns over bias and energy use (D1, 1.22 to 1.26, 3.12); ethical use is a "
                                                     "transferable skill (4.5)"),
         statements=['4.5.b5']),
]

SB3 = dict(
    areas=[
        dict(component='1.3', gloss='artefacts by medium: painting, sculpture, architecture, applied arts, lens and screen media, performance'),
        dict(component='1.5', gloss='descriptive methods: formalism, iconography, semiotics, materiality, spatial and functional analysis'),
        dict(component='3.2', gloss='many periods, places and cultures, studied in depth and comparatively; content varies by provider'),
        dict(component='3.5', gloss='historiography of the discipline, physical properties of artefacts, contemporary professional contexts'),
    ],
    practices=[
        dict(component='1.14', kind='teaching', gloss='lectures, seminars, tutorials, peer learning and off-campus visits'),
        dict(component='2.4', kind='learning', gloss='digital reproductions, databases and archives; fieldwork and site-based learning'),
        dict(component='2.5', kind='assessment', gloss='independent and group tasks; formative and summative balance'),
        dict(component='3.4', kind='teaching', gloss='research-informed teaching; collections partnerships'),
        dict(component='3.6', kind='teaching', gloss='varied output formats; visual literacy and communication'),
        dict(component='3.7', kind='learning', gloss='inclusive design; study visits; placements on some courses'),
        dict(component='3.8', kind='teaching', gloss='indicative methods and approaches: object-based, experiential, collaborative, problem-based, authentic, creative, digital'),
        dict(component='3.9', kind='assessment', gloss='feedback points; criteria in handbooks'),
        dict(component='3.10', kind='assessment', gloss='flexible, aligned, formative and summative'),
        dict(component='3.11', kind='assessment', gloss='self- and peer assessment for independence'),
        dict(component='3.12', kind='assessment', gloss='a broader portfolio in response to generative AI'),
        dict(component='3.13', kind='assessment', gloss='indicative methods: tests, written and spoken, creative and digital, industry-based'),
    ],
)

SB4 = dict(
    rungs=[
        dict(rung='threshold', leadIn='4.4', award=HON, items=15),
        dict(rung='typical', leadIn='4.4', award=HON, items=15),
        dict(rung='typical', leadIn='4.6', award=MAS, items=12),
    ],
    rungBases=("4.4: threshold is the minimum acceptable standard of an honours graduate, equivalent to a third; typical is the standard most "
               "honours graduates attain, equivalent to a second; no excellent rung (4.2 leaves performance above threshold to Annex D). 4.6's "
               "master's list says 'should typically', recorded as a typical rung for the master's award"),
    outcomeLists=[dict(leadIn='4.5', gloss='transferable skills on graduating with honours', items=10, award=['honours'])],
    outcomes=OUT,
)

SB4A_FULL = []

SB5 = [
    dict(body='Professional, statutory and regulatory bodies (PSRBs), none named',
         says=("architecture courses with HAAD modules may be subject to PSRB requirements; courses with professional outcomes may need their "
               "accreditation; competence standards may draw on PSRB requirements (D1, 1.15, 2.21, 4.3; front matter)"),
         requirements='not yet ingested (Part E)'),
    dict(body='Equality and Human Rights Commission',
         says='providers developing competence standards should follow its most recent guidance (D1, 4.3)',
         requirements='not yet ingested (Part E)'),
    dict(body='Office for Students',
         says="in England benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)",
         requirements='not-applicable-by-design: named for status only (Part E)'),
]

SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equity, diversity and inclusion', carriedIn=S6[0]['carriedIn'], statements=['3.13', '4.3', '4.4.b14.typical', '4.5.b4']),
        dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=S6[1]['carriedIn'], statements=['3.13']),
        dict(id='theme:esd', named='Education for sustainable development', carriedIn=S6[2]['carriedIn'], statements=['4.4.b7', '4.5.b4']),
        dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education', carriedIn=S6[3]['carriedIn'], statements=[]),
        dict(id='theme:generative-ai', named='Generative artificial intelligence', carriedIn=S6[4]['carriedIn'], statements=['4.5.b5']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.6', '2.9', '2.10', '2.12', '2.15', '4.4']),
        dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.6', '2.9', '2.11', '2.12', '4.4']),
    ],
    bodies=[
        dict(body='PSRBs (none named)', citedIn=['front matter', '1.15', '2.21', '4.3']),
        dict(body='Equality and Human Rights Commission', citedIn=['4.3']),
        dict(body='Office for Students', citedIn=['front matter']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies',
             citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) for evidence above threshold'),
        dict(document='QAA Quality Code, 2024 update (not yet ingested)', named='an update to the Quality Code', citedIn=['front matter'], role='a further reference point'),
        dict(document="QAA Glossary (not ingested)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development goals (2015)', citedIn=['1.16'],
             role='the frame of the sustainability theme, goals 3, 5, 9 to 16 named'),
        dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['1.10', '1.13', '4.3'], role='EDI duties, reasonable adjustment, competence standards'),
        dict(document='Disability Discrimination Act 1995 (law, Northern Ireland)', named='Disability Discrimination Act 1995', citedIn=['1.13'], role='reasonable adjustment in Northern Ireland'),
        dict(document='SEND legislation and guidance (law)', named='Special Educational Needs and Disability (SEND) legislation and guidance', citedIn=['1.13'], role='inclusion of disabled learners'),
    ],
)

B1 = [
    dict(slug='artefact', definition='any entity the subject studies, in any medium, from painting and buildings to screen media and performance (D1, 1.3)',
         beneficiaryDefinition='any object, image, building, design or performance you study', scopeNote='the statement\'s own umbrella term', category='unknown', practices=['education']),
    dict(slug='visual-and-material-culture', definition='the subject\'s object of study across all regions and periods, wider than "art" and "design" (D1, 1.4)',
         beneficiaryDefinition='everything people have made to be seen or used', scopeNote='replaces a focus on intrinsic artistic quality', category='unknown', practices=['education']),
    dict(slug='threshold-standard', definition='the minimum acceptable standard of an honours graduate, equivalent to a third-class degree (D1, 4.4)',
         beneficiaryDefinition='the least you need to show to gain the honours degree', scopeNote='paired with typical in the 4.4 table', category='unknown', practices=['education']),
    dict(slug='typical-standard', definition='the standard most honours graduates reach, equivalent to a second-class degree (D1, 4.4)',
         beneficiaryDefinition='the level most students reach', scopeNote='used for the master\'s list too ("should typically", 4.6)', category='unknown', practices=['education']),
    dict(slug='haad', definition='the abbreviation the statement uses for the subject (D1, 1.1)', scopeNote='used throughout', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='artefact', form='artefacts', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='visual-and-material-culture', form='visual and material culture', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='threshold-standard', form='threshold', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='typical-standard', form='typical', lang='en', partOfSpeech='adjective', termStatus='preferred', register='formal'),
    dict(concept='haad', form='HAAD', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
]
B4 = [dict(rel='contrasts-with', **{'from': 'threshold-standard'}, to='typical-standard', note='4.4: the two rungs of the table')]
B5 = []

D3 = [
    dict(citation='QAA (2019) Subject Benchmark Statement: History of Art, Architecture and Design, fourth edition (minor update)',
         settles=['S7'], asked='2026-10-03', state='wanted'),
]

E = [
    'SB4, pattern (differs from Psychology): two rungs only, threshold and typical, in one table of 15 rows across three blocks (subject knowledge, subject-specific skills, generic intellectual skills); no excellent rung. Each cell has its own text, so each is its own record with its own span; the typical cell is `<id>.typical`, and `gradeOf` is stated, the issuer pairing the cells in one row.',
    'SB4, flattened table (P3): the table is flattened in the held text, cells running threshold then typical, row by row. Placement read from the order and the plain pairing of content. The generic intellectual skills block has no column headings in the held text; its four rows were placed by the same alternation (threshold first). Least sure: row 14 (open-mindedness to inclusive interpretation), where the pairing is by theme, not by shared wording.',
    'SB4, row 7: the threshold cell names environmental context; the typical cell drops "environmental". Kept as the issuer has it; ESD tagged on the threshold cell only.',
    "SB4, master's: 4.6's lead-in reads 'should typically be able to'. Recorded as rung typical, award master's, level fheq:7, ids `.masters`, per the batch 1 convention ('the rung its heading names'; here the lead-in's word). For P3: threshold may be the intended reading.",
    'S4, force: the table cells take force from distant lead-ins: threshold cells `threshold` (4.4 defines it as the minimum for the award; forceFrom 4.4); typical cells `will` from 4.1 ("a student will have demonstrated"; forceFrom 4.1). 4.5 and 4.6 take `should` from their lead-ins.',
    'S4, 4.5 list: transferable skills on graduating with honours in "should be able to", not tied to a rung; recorded as an outcome list (rung none). The lead-in sits under the 4.4 heading run and 4.5 has no rung of its own: for P3.',
    'S4, 4.5.b1 and 4.5.b2: the held text runs two bullets together across a page break ("... written English work as part of a team ..."). Split into two records; 4.5.b1\'s span crosses the page number 19, so its `source` carries that page number. Skeleton ids 4.5.b2 to 4.5.b9 renumbered 4.5.b3 to 4.5.b10 by `find`.',
    'S4, skeleton correction: candidates 3.8.b1 to b42 and 3.13.b1 to b18 are indicative lists of teaching and assessment methods ("not exhaustive", "indicative rather than prescriptive"), not standards; recorded as practice components (SB3). The skeleton found no rungs: the rungs were judged by hand.',
    'S4, statements taken from prose: 2.3, 2.6, 2.8, 2.18 (sentence), 2.19 and 3.13 (sentence) in will; 4.2 and 4.3 in should. 2.6 and 2.8 are learner outcomes; the rest provider duties with no student version. Domain `none` for these paragraph statements, as in Psychology.',
    'S4, obliging words outside the five, not taken as statements, for Abbott: 2.7 "it would be expected that" (readiness for postgraduate study); 2.17 "are also expected to be beneficial" (partnerships for hosts); 2.6 "it is expected that" sits inside a statement taken on its "will".',
    'S4, plain-present provider norms, not statements (template open point 5): 1.13 (access proactively considered), 1.22 and 1.24 (students given guidance on GenAI), 2.12 (integrated master\'s designed to meet descriptors), 2.15 (formal partnerships aligned and reviewed), 2.16 (providers ensure equal opportunity; formal contracts), 3.9 (criteria communicated via handbooks), 3.11 and 3.12 (designers consider methods).',
    'S4, predictive "will" not taken: 1.25 ("Critical GenAI fluency will also enhance graduates\' employability skills"), 2.20 (external examiners will be asked and will consider), 3.2 (content will vary).',
    'S5, levels (doubt for P3): 2.9 places the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9. The FHEQ document (Table 1) places them at SCQF 7 and 8. Recorded as stated with the difference noted in S5; the issuer\'s text may be in error.',
    'S5, levels: 4.4 cites "Level 7 (in England, Northern Ireland and Wales) and Level 11 (in Scotland)" without naming a framework; read as fheq:7 and fqheis:11 and listed in SB6 under both frameworks.',
    'S5, generic skills: every generic-skill record carries fheq:6 (honours) or fheq:7 (master\'s), both in S5; the framework descriptors each instruction sets them beside are 4.15 and 4.17 of std:doc:qaa-fheq-2024-framework (inferred pairings, ours).',
    'SB6: the cross-cutting themes are named as five in the front matter (EDI; accessibility; ESD; EEE; GenAI) and each has its own heading in section 1. GenAI uses theme:generative-ai. 2.15\'s "sustainability and resilience of delivery" means continuity, not ESD, and is not tagged.',
    'SB6: CQFW is not cited. No subject association is named outside the back matter (the Association for Art History appears only in the advisory group list, excluded matter).',
    'SB5: the PSRBs are named only as a class; none is identified, so no requirements document can be linked. The EHRC\'s guidance is not yet ingested. The Office for Students is named for status only.',
    'S2, subjects: HECoS 100306, 100782 and 100783 and CAH20-01-02 are taken as stated: the title names history of art, architecture and design, and CAH20-01-02 carries the same label. The 1.2 programme codes are for degrees that include HAAD components, not the benchmark\'s own scope.',
    'S7: the previous edition (2019, fourth edition, minor update) is named in the back matter; earlier advisory groups 2016, 2007 and 2002 also listed. Not ingested (D3).',
    'S1, licence: the text gives a copyright notice and no re-use terms.',
    'S9: not researched in P1.',
    'Pattern (differs from Psychology): no professional body; a two-rung table rather than three separate lists; a master\'s list beside the honours standards; a generative AI theme section; the theme sections come before the distinctive features, as in the 2026 revision.',
]
