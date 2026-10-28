# Judgement for run 0132, QAA Theology and Religious Studies (March 2022, fifth edition). std run agent.
# Keys are S4 ids under qaa/theology-and-religious-studies-2022/. Built by tools/bm_build.py (BM-BRIEF 0.2.3).
HON = "bachelor's with honours"
MA = "master's"
CITE = 'QAA, 2022, Theology and Religious Studies Subject Benchmark Statement'
F = 'qaa/fheq-2024/'
AD = 'qaa/fheq-2024/annex-d/'

META = dict(
    run='0132', p1='2026-10-03 18:40',
    title='Subject Benchmark Statement Theology and Religious Studies',
    heading='Subject Benchmark Statement: Theology and Religious Studies (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current',
    supersedes='the fourth edition, 2019 (named in the advisory group section, which also names editions of 2014, 2007 and 2000)',
    subjects=[
        dict(scheme='hecos', code='100794', label='theology and religious studies', basis='stated'),
        dict(scheme='cah', code='CAH20-02-02', label='theology and religious studies', basis='stated'),
        dict(scheme='hecos', code='100340', label='theology', basis='stated'),
        dict(scheme='hecos', code='100339', label='religious studies', basis='stated'),
        dict(scheme='hecos', code='100799', label='divinity', basis='stated'),
        dict(scheme='hecos', code='100801', label='biblical studies', basis='stated'),
        dict(scheme='hecos', code='100796', label='Islamic studies', basis='stated'),
        dict(scheme='hecos', code='100798', label='buddhism', basis='inferred'),
        dict(scheme='hecos', code='100797', label='Judaism', basis='inferred'),
        dict(scheme='hecos', code='100802', label='pastoral studies', basis='inferred'),
        dict(scheme='cah', code='CAH20-02', label='philosophy and religious studies', basis='inferred'),
    ],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition (2022 revision with cross-cutting themes)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=(
        "QAA's UK reference point for what an honours graduate in theology and religious studies can be expected to know, "
        "understand and do, set as threshold (third-class) outcomes in three lists: knowledge and understanding, subject-specific "
        "and intellectual skills and generic skills; an appendix adds what a taught master's in the field shows on top of them. "
        "Use it when designing, reviewing or describing a theology, religious studies or divinity course and its outcomes. "
        "It is not a curriculum, not a checklist and not a regulatory requirement in England; it states no typical or excellent lists: "
        "above the threshold it hands over to the degree classification descriptions (Annex D)."),
    summary=(
        "Published by QAA in March 2022 as the fifth edition, the statement covers theology and religious studies (TRS) as one "
        "contested field taught in secular and faith-based settings, under many course titles. It describes the subject's context "
        "and purposes, its distinctive features (breadth and depth designs, access, progression, partnership with religious "
        "communities, review), its content, approaches, teaching and assessment; and benchmark standards at the threshold rung "
        "only, for bachelor's degrees with honours (FHEQ level 6, FQHEIS level 10): 24 outcomes. Appendix A adds eight outcomes "
        "for taught master's degrees. It carries the cross-cutting themes of equality, diversity and inclusion (with a decolonising "
        "approach), accessibility, education for sustainable development (with the eight UNESCO competencies) and employability "
        "with enterprise and entrepreneurship education. It points to Annex D for performance above the threshold and names "
        "PSRBs in general, faith bodies, the Institute for Apprenticeships and Technical Education (a Church Minister standard) "
        "and the subject association's Framework of Professional Practice."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a "
               "sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the "
               "quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)"),
)

S2 = dict(
    governs=("what an honours graduate in theology and religious studies can be expected to know, do and understand, and what "
             "a taught master's graduate shows in addition; the nature and characteristics of awards in the subject "
             "(D1, front matter: About this Statement; 4.1; Appendix A6)"),
    awards=["bachelor's degrees with honours (single, joint, combined, major-minor)", "taught master's degrees (Appendix A)",
            "integrated master's (described, 2.17)"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope=('"This document is a QAA Subject Benchmark Statement for Theology and Religious Studies that defines what can '
                 'be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of '
                 'their studies." (D1, front matter: About this Statement)'),
    statedSubjects=[
        dict(name='Theology and Religious Studies (TRS)', locator='(D1, title; 1.1; 1.7)', kind='subject',
             codes=[dict(scheme='hecos', code='100794', label='theology and religious studies'),
                    dict(scheme='cah', code='CAH20-02-02', label='theology and religious studies')]),
        dict(name='Theology', locator='(D1, 1.7)', kind='programme title', codes=[dict(scheme='hecos', code='100340', label='theology')]),
        dict(name='Religious Studies; Study of Religion(s)', locator='(D1, 1.7)', kind='programme title',
             codes=[dict(scheme='hecos', code='100339', label='religious studies')]),
        dict(name='Divinity', locator='(D1, 1.7)', kind='programme title', codes=[dict(scheme='hecos', code='100799', label='divinity')]),
        dict(name='Religion, Philosophy and Ethics', locator='(D1, 1.8)', kind='programme title', codes=[]),
        dict(name='Biblical Studies', locator='(D1, 1.8)', kind='specialism', codes=[dict(scheme='hecos', code='100801', label='biblical studies')]),
        dict(name='Buddhist Studies', locator='(D1, 1.8)', kind='specialism', codes=[dict(scheme='hecos', code='100798', label='buddhism')]),
        dict(name='Islamic Studies', locator='(D1, 1.8)', kind='specialism', codes=[dict(scheme='hecos', code='100796', label='Islamic studies')]),
        dict(name='Jewish Studies', locator='(D1, 1.8)', kind='specialism', codes=[dict(scheme='hecos', code='100797', label='Judaism')]),
        dict(name='Theology, Ministry and Mission; Practical Theology', locator='(D1, 1.8)', kind='programme title',
             codes=[dict(scheme='hecos', code='100802', label='pastoral studies')]),
        dict(name='Religious Education', locator='(D1, 1.8)', kind='programme title', codes=[]),
        dict(name='MTh, MDiv, MMin, MA, MSt', locator='(D1, Appendix A2)', kind='programme title', codes=[]),
    ],
)

SECTIONS = {
    '1': 'Context and purposes of a Theology and Religious Studies degree',
    '2': 'Distinctive features of a Theology and Religious Studies degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
    'A1': "Appendix A: Taught master's degrees; A1 The nature and extent of taught master's degrees",
    'A2': "Appendix A: Taught master's degrees; A2 The naming of master's degrees",
    'A3': "Appendix A: Taught master's degrees; A3 Intended entrants",
    'A4': "Appendix A: Taught master's degrees; A4 Teaching and learning",
    'A5': "Appendix A: Taught master's degrees; A5 Assessment",
    'A6': "Appendix A: Taught master's degrees; A6 Benchmark standards",
}
SUB = [
    ('1.1', '1.10', 'Context'),
    ('1.11', '1.12', 'Purposes of a Theology and Religious Studies degree: Reasons for studying TRS'),
    ('1.13', '1.16', 'Purposes of a Theology and Religious Studies degree: Broader social purpose'),
    ('1.17', '1.21', 'Employability'),
    ('1.22', '1.25', 'Equality, diversity and inclusion'),
    ('1.26', '1.29', 'Education for sustainable development'),
    ('1.30', '1.33', 'Entrepreneurship and enterprise education'),
    ('2.1', '2.3', 'Design'),
    ('2.4', '2.11', 'Accessibility'),
    ('2.12', '2.18', 'Progression'),
    ('2.19', '2.20', 'Partnership'),
    ('2.21', '2.25', 'Monitoring and review'),
    ('3.1', '3.5', 'Content: Subject matter'),
    ('3.6', '3.6', 'Content: Approaches'),
    ('3.7', '3.7', 'Content: Interdisciplinary connections'),
    ('3.8', '3.9', 'Teaching and learning: Overview'),
    ('3.10', '3.17', 'Teaching and learning: Specific modes of teaching and learning'),
    ('3.18', '3.18', 'Assessment: Purpose'),
    ('3.19', '3.19', 'Assessment: Relation to learning outcomes'),
    ('3.20', '3.20', 'Assessment: Formative and summative'),
    ('3.21', '3.21', 'Assessment: Feedback'),
    ('3.22', '3.22', 'Assessment: Criteria'),
    ('3.23', '3.25', 'Assessment methods'),
    ('4.1', '4.5', 'Introduction'),
    ('4.6', '4.6', 'Threshold level (3rd class): Knowledge and understanding'),
    ('4.7', '4.7', 'Threshold level (3rd class): Subject-specific and intellectual skills'),
    ('4.8', '4.8', 'Threshold level (3rd class): Generic skills'),
]

G = {
    '1.1': 'the field studies religion critically in a global setting and helps people live in a world religion shapes',
    '1.2': 'courses let students examine and take part in religious life and meet views unlike their own',
    '1.3': 'the name and unity of the field are debated: one discipline or two linked ones',
    '1.4': 'the debates cross over with insider and outsider stances, views on truth claims and institutional settings',
    '1.5': 'many kinds of provider teach the field, and parts of it sit inside wider humanities units',
    '1.6': 'secular providers and providers with a religious stance, the latter often training for ministry or chaplaincy',
    '1.7': 'where the field sits in an institution and the many names its departments use',
    '1.8': 'course titles vary widely, from combined titles to tradition-specific and vocational ones',
    '1.9': 'single, joint, combined, major-minor and general study; modules open to other students',
    '1.10': 'overlaps with many other subjects because religion runs through culture and society',
    '1.11': 'seven benefits of studying the field, from curiosity and method to careers and public debate',
    '1.12': 'study can change a student personally, widening horizons and challenging prejudice',
    '1.13': 'the social purpose: informed public debate grounded in religious literacy',
    '1.14': 'graduates across careers bring an informed grasp of religion to many public questions',
    '1.15': 'demand for religious literacy training from public bodies and others, given the Equality Act',
    '1.16': 'the field also serves religious communities, prompting reflection and innovation',
    '1.17': 'the habits of mind and general skills the field builds serve both work and further study',
    '1.18': 'graduates are employable for their cross-disciplinary skills and critical range',
    '1.19': 'graduates able to engage with empathy across familiar and unfamiliar views (S4)',
    '1.20': 'employment sectors and public-facing vocations graduates enter',
    '1.21': 'employment in religious bodies; the Church Minister integrated degree apprenticeship',
    '1.22': 'courses aim at success for every kind of student; a religious stance is declared and open to challenge (S4)',
    '1.23': 'courses recognise the identities students and staff bring and encourage learning from each other',
    '1.24': 'a decolonising approach to content and teaching as part of the commitment to equality',
    '1.25': 'critical awareness of the part the field itself has played in categorising religions',
    '1.26': 'what education for sustainable development means in this field',
    '1.27': 'sustainability knowledge applied to fairer, greener societies; the role of religious actors',
    '1.28': 'sustainability promoted through the eight UNESCO competencies, each given a religious angle',
    '1.29': 'the link between sustainability and the decolonising approach',
    '1.30': 'what enterprise and entrepreneurship education does and its overlap with sustainability',
    '1.31': 'enterprise-relevant skills and attitudes the field can foster',
    '1.32': 'five ways to bring enterprise education into courses, from placements to practitioner teaching',
    '1.33': 'some courses prepare for religious roles with an innovation emphasis',
    '2.1': 'breadth courses and depth courses, which can be combined',
    '2.2': 'both designs assume students of varied belief and prior knowledge',
    '2.3': 'overlaps with other disciplines may lead to strategic partnerships',
    '2.4': 'students arrive from many educational backgrounds',
    '2.5': 'entry does not depend on school religious studies; support for those new to the field',
    '2.6': 'many take the field as a second bachelor-level course for religious leadership roles',
    '2.7': 'part-time, online and blended study widens access, with broad parity across modes',
    '2.8': 'ancient and classical languages, usually optional, with accessible materials',
    '2.9': 'courses designed for disabled students and those with specific learning differences; inclusive design (S4)',
    '2.10': 'fieldwork, placements and discussion made accessible, including for autistic and anxious students (S4)',
    '2.11': 'sensitivity to how prior exposure and identity affect students; religion as a protected characteristic',
    '2.12': 'progression year by year towards the threshold skills; honours at FHEQ 6 and FQHEIS 10',
    '2.13': 'what progression involves: facility, depth, maturity, writing and research skills (S4)',
    '2.14': 'multiple entry points and care over prerequisites',
    '2.15': 'a graduate is expected to be ready for postgraduate study',
    '2.16': 'joint honours students reach part of the subject skills and add others (S4)',
    '2.17': 'integrated master\'s at FHEQ 7 and FQHEIS 11; exit awards; four-year Scottish honours',
    '2.18': 'exit points matter most for professional and vocational training',
    '2.19': 'the many ties between courses and religious communities, including validation',
    '2.20': 'critical study can unsettle convictions; engagement with communities is respectful (S4)',
    '2.21': 'monitoring and periodic review against external reference points, employability among them (S4)',
    '2.22': 'what monitoring and evaluation are and what they inform',
    '2.23': 'external reviewers in periodic review check threshold standards and content (S4)',
    '2.24': 'external examining and its role; accreditation of vocational courses by professional bodies',
    '2.25': 'partner bodies\' own monitoring is taken into account in design',
    '3.1': 'the two clusters of subject matter: religions in general and particular traditions',
    '3.2': 'seventeen topics the field covers in more detail',
    '3.3': 'engagement with contemporary issues and critical studies of identity and power',
    '3.4': 'some courses teach classical and scriptural languages',
    '3.5': 'courses mix the elements differently; sustainability and inclusion questions in all of them (S4)',
    '3.6': 'nineteen approaches or methods for studying religion',
    '3.7': 'thirty-four neighbouring subjects the field draws on and feeds',
    '3.8': 'eighteen teaching and learning methods',
    '3.9': 'other learning opportunities, each with clearly stated aims and outcomes',
    '3.10': 'lectures and presentations and what they offer',
    '3.11': 'seminars and tutorials for dialogue among differing views',
    '3.12': 'study visits and fieldwork with living religion; adjustments for disabled students',
    '3.13': 'observing practice beside the study of texts and history',
    '3.14': 'group and peer learning',
    '3.15': 'work-based learning and placements',
    '3.16': 'reading primary and secondary literature from diverse authors; finding sources with discernment',
    '3.17': 'online materials and online learning',
    '3.18': 'every course assesses; varied tasks, feedback, growing independence, clear guidance',
    '3.19': 'assessment checks that stated outcomes are met',
    '3.20': 'summative and formative work, and what formative work gives students (S4)',
    '3.21': 'forms and purposes of feedback',
    '3.22': 'clear criteria for all assessment, especially group and peer work',
    '3.23': 'twenty-three assessment methods; adjustments for disabled students',
    '3.24': 'negotiating assessment for self-chosen research topics',
    '3.25': 'oral examination of reports and dissertations; recording presentations',
    '4.1': 'the standards are the minimum for an honours award (the threshold rung defined)',
    '4.2': 'most students exceed the threshold; providers should use Annex D for the classes above it (S4)',
    '4.3': 'excellent students go beyond the threshold with originality and insight (no list)',
    '4.4': 'the outcomes are indicative, not a curriculum or checklist',
    '4.5': 'personal development is hard to assess; spiritual development is not an award criterion',
    '4.6': 'threshold knowledge and understanding: nine outcomes',
    '4.7': 'threshold subject-specific and intellectual skills: six outcomes',
    '4.8': 'threshold generic skills: nine outcomes',
}

CTYPE = {
    '3.1': 'area', '3.2': 'area', '3.3': 'area', '3.4': 'area', '3.6': 'area', '3.7': 'area',
    '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice',
    '3.14': 'practice', '3.15': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice',
    '3.20': 'practice', '3.21': 'practice', '3.22': 'practice', '3.23': 'practice', '3.24': 'practice', '3.25': 'practice',
}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points',
         kind='other: front matter, read for S1, S2, S6 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for S7, SB5 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Theology and Religious Studies',
         kind='other: membership, read for S8 (editions of 2000, 2007, 2014 and 2019)'),
    dict(number='Appendix A (inside the skeleton\'s back-matter-2)', heading="Appendix A: Taught master's degrees, A1 to A6",
         kind='not excluded: read in full; recorded as sections A1 to A6 and its statements cut by find (Part E)'),
    dict(number='none', heading='Fifth edition; Published - 30 March 2022; copyright notice', kind='other: colophon, read for S1 and S8'),
]

# ------------------------------------------------------------------ statements
P = {}
def s(i, **k):
    P[i] = k

def aaw_thr(n, k, what, fw, ad, nb):
    return (f"Treat this as a threshold outcome for a bachelor's degree with honours in theology and religious studies (FHEQ level 6, "
            f"FQHEIS level 10): the least an honours graduate will be able to show, here {what}. "
            f"Cite it as {CITE}, para {n}, bullet {k}. "
            f"Do not claim it is a regulatory requirement, a complete checklist (para 4.4 calls the outcomes indicative) or a standard for other levels. "
            f"Set it beside {nb}, the level 6 descriptor {F}{fw} and Annex D's third-class cell {AD}{ad}.")

def aad_thr(topic, q, staff):
    return (f"Raise this when a student, teacher or programme team asks about {topic}. "
            f"With a student, say in plain words and the second person that this is the floor for an honours award, not the mark of a good degree; "
            f"with staff, frame it as {staff}. "
            f"Ask: {q} Do not read the issuer's list aloud or treat this minimum as the target.")

def aaw_ma(k, what, fw, nb):
    return (f"Treat this as part of the master's standard: a taught master's in the field is awarded to students who have shown many, "
            f"not necessarily all, of the eight items on top of the honours outcomes, here {what}. "
            f"Cite it as {CITE}, Appendix A6, bullet {k}, at FHEQ level 7 or FQHEIS level 11 (our reading of the frameworks; the appendix states no level). "
            f"Do not present any single item as required, or the list as applying to honours study. "
            f"Set it beside {nb}, the master's descriptor {F}{fw} and spine:7 in the reference framework.")

def aad_ma(topic, q):
    return (f"Bring this up when a master's student or course team talks about {topic}. "
            f"Put it to a student as one of several things a master's typically adds beyond honours work, in plain words and the second person; "
            f"to staff, as an outcome the course should make room for. "
            f"Ask: {q} Avoid reciting the appendix or implying every item must be met.")

# ---- threshold, 4.6 knowledge and understanding (lead-in 4.6; rung defined as the minimum in 4.1)
L = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6',
         appliesTo='honours graduates in the subject, at the threshold', addressee='learner', award=HON)
TB = 'At the minimum for an honours award, '

s('4.6.b1', **L, verbs=['demonstrate'], about='religions and worldviews, general and particular', domain='knowledge',
  para='Will show that they understand and engage critically with religion and worldviews in general, with specific religious traditions and their communities and institutions or with both.',
  prac='At threshold, graduates will show understanding of, and critical engagement with, religions and worldviews broadly, particular traditions with their communities and institutions or both.',
  ben=TB + 'you will show that you understand, and can think critically about, religion and worldviews as a whole, specific traditions and their communities or both.',
  aaw=aaw_thr('4.6', 1, 'critical understanding of religions and worldviews, broadly or in particular traditions', '4.15.b1', 'knowledge/r1/3rd', 'the other knowledge items 4.6.b2 to 4.6.b7'),
  aad=aad_thr('what a theology or religious studies graduate should know', 'Which traditions or broad questions about religion could you explain and question with confidence, and which feel thin?',
              'an outcome every student needs a fair chance to evidence, whether the course is broad or deep'))
s('4.6.b2', **L, verbs=['demonstrate'], about='non-religion, atheism and the secular', domain='knowledge',
  para='Will show understanding of, and critical engagement with, non-religion and atheism and with how religions relate to secular culture.',
  prac='At threshold, graduates will understand and critically engage with non-religion, atheism and the relations between religions and the secular.',
  ben=TB + 'you will understand, and think critically about, non-belief and atheism and how religion and secular society relate.',
  aaw=aaw_thr('4.6', 2, 'critical understanding of non-religion, atheism and the secular', '4.15.b1', 'knowledge/r1/3rd', '4.6.b1 and the subject matter in para 3.2'),
  aad=aad_thr('whether the subject covers unbelief and secular society', 'Where in your study have you looked at atheism or secular culture, and how did it change your view of religion?',
              'content the course should include, not an optional extra'))
s('4.6.b3', **L, verbs=['demonstrate'], about='lived religion and its links to wider society', domain='knowledge',
  para='Will show understanding of, and critical engagement with, a selection of the lived aspects of the traditions studied (practice, belief, ethics, text, material culture, art, history and more) and how these connect with wider social and cultural patterns.',
  prac='At threshold, graduates will critically understand some of the practical, material, textual and historical dimensions of the traditions they studied and relate them to wider social and cultural structures.',
  ben=TB + 'you will understand and think critically about some of the ways the traditions you study are lived (practices, beliefs, texts, objects, art, history) and how they connect with the wider society around them.',
  aaw=aaw_thr('4.6', 3, 'critical understanding of some dimensions of lived religion and their social connections', '4.15.b1', 'knowledge/r2/3rd', '4.6.b1 and 4.6.b5'),
  aad=aad_thr('how deep or wide study of a tradition needs to go', 'Pick one tradition you studied: which of its practices, texts or institutions can you connect to the society around it?',
              'an outcome that asks for some, not all, of the listed dimensions'))
s('4.6.b4', **L, verbs=['demonstrate'], about='changing religious identities and hybridity', domain='understanding',
  para='Will show a sophisticated grasp of how religious identities and cultures are continually renegotiated, change, meet and clash, and of hybrid and multiple belonging.',
  prac='At threshold, graduates will understand in a sophisticated way the ongoing renegotiation of religious identities and cultures, including hybridity and multiple belonging.',
  ben=TB + 'you will have a sophisticated grasp of how religious identities keep shifting, meet and clash, and how people can belong to more than one tradition.',
  aaw=aaw_thr('4.6', 4, 'a sophisticated understanding of shifting religious identity, hybridity and multiple belonging', '4.15.b4', 'knowledge/r2/3rd', '4.6.b1 and 4.7.b3'),
  aad=aad_thr('identity, belonging and change in religious life', 'Can you describe a case where someone belongs to more than one tradition, and what that shows about identity?',
              'the one knowledge outcome the issuer qualifies as sophisticated even at threshold'))
s('4.6.b5', **L, verbs=['demonstrate'], about='key sources and how they have been read', domain='knowledge',
  para='Will show understanding of, and critical engagement with, the central sources of the traditions or worldviews studied and how they have been interpreted across periods and settings.',
  prac='At threshold, graduates will critically understand the key sources of the religions or worldviews studied and their interpretation across history and social or geographical settings.',
  ben=TB + 'you will understand and think critically about the main sources of the traditions you study and how people have read them in different times and places.',
  aaw=aaw_thr('4.6', 5, 'critical understanding of key sources and their reception', '4.15.b5', 'knowledge/r3/3rd', '4.6.b3 and 4.7.b2'),
  aad=aad_thr('sacred texts, scriptures or founding sources', 'Which source have you studied closely, and can you show two different ways it has been read?',
              'an outcome about reception as well as content'))
s('4.6.b6', **L, verbs=['demonstrate'], about='claims about the transcendent, the world, ethics and flourishing', domain='knowledge',
  para='Will show understanding of, and critical engagement with, the beliefs and arguments circulating in particular religious settings about transcendent reality, the divine, the world, ethics and human flourishing.',
  prac='At threshold, graduates will critically understand the beliefs and arguments about the divine or transcendent, the world, ethics and flourishing current in specified religious contexts.',
  ben=TB + 'you will understand and think critically about what particular religious groups believe and argue about God or the divine, the world, ethics and living well.',
  aaw=aaw_thr('4.6', 6, 'critical understanding of doctrinal and ethical claims in specified contexts', '4.15.b1', 'knowledge/r2/3rd', '4.6.b5 and 4.7.b4'),
  aad=aad_thr('doctrine, belief and ethics', 'Can you set out one argument about the divine or about living well from a tradition you studied, and then question it?',
              'critical engagement with claims, not assent to them'))
s('4.6.b7', **L, verbs=['demonstrate'], about='themes, debates and methods of the field', domain='knowledge',
  para='Will show understanding of, and critical engagement with, a range of the themes, debates and methods that make up theology and religious studies.',
  prac='At threshold, graduates will critically understand a range of the field\'s themes, debates and methods.',
  ben=TB + 'you will understand and think critically about a range of the topics, debates and methods in the study of theology and religion.',
  aaw=aaw_thr('4.6', 7, "critical understanding of a range of the field's themes, debates and methods", '4.15.b2', 'knowledge/r2/3rd', '4.7.b1 and the approaches in para 3.6'),
  aad=aad_thr('the debates and methods of the field', 'Which debate in the field could you summarise for someone new to it, and which method would you choose to study it?',
              'breadth of the discipline, not one school'))
s('4.6.b8', **L, verbs=['make'], about='applying the field to interdisciplinary discussion', domain='subject-skill',
  para='Will bring the field\'s ideas, themes and debates to bear, appropriately, on discussions shared with other disciplines in the humanities, social sciences, law or the sciences.',
  prac='At threshold, graduates will apply the insights and debates of the field appropriately to interdisciplinary conversations, for example with law, the social sciences or the sciences.',
  ben=TB + 'you will be able to use ideas and debates from theology and religious studies sensibly in conversations with other subjects, such as law, social science or medicine.',
  aaw=aaw_thr('4.6', 8, 'appropriate application of the field to interdisciplinary discussion', '4.15.b6', 'cognitive/r3/3rd', 'para 3.7 on neighbouring subjects and 4.6.b9'),
  aad=aad_thr('how the subject connects with other disciplines', 'Name a question in another subject where what you know about religion changes the answer: how would you make that case?',
              'an application outcome that suits joint and combined courses'))
s('4.6.b9', **L, verbs=['demonstrate'], about="religion's contributions to public debate", domain='understanding',
  para='Will show awareness of, and assess critically, what religions contribute to public debate on matters such as justice, identity, diversity, inclusion, poverty, race, sustainability and truth.',
  prac='At threshold, graduates will be aware of and critically assess religious contributions to public debate on topics such as diversity, inclusion, justice, poverty, race and sustainability.',
  ben=TB + 'you will be aware of how religious voices take part in public debates (on justice, identity, race, poverty, sustainability and more) and be able to assess them critically.',
  aaw=aaw_thr('4.6', 9, 'critical assessment of religious contributions to public debate', '4.15.b7', 'cognitive/r2/3rd', 'para 1.13 on the social purpose and 4.6.b8'),
  aad=aad_thr('religion in public life and current debates', 'Choose a public debate you follow: what do religious voices add to it, and where would you challenge them?',
              'an outcome linking the subject to public debate and the cross-cutting themes'))

# ---- threshold, 4.7 subject-specific and intellectual skills
s('4.7.b1', **L, verbs=['Demonstrate'], about='intellectual flexibility across methods of study', domain='subject-skill',
  para='Will show flexibility of mind by working with a variety of methods of study, from anthropological, historical and textual to feminist, postcolonial, queer, theological and others.',
  prac='At threshold, graduates will show intellectual flexibility by practising varied methods of study (for example exegetical, empirical, feminist, postcolonial, systematic or theological).',
  ben=TB + 'you will show flexible thinking by using several different methods to study religion, such as historical, textual, social scientific, feminist or theological approaches.',
  aaw=aaw_thr('4.7', 1, 'intellectual flexibility through several methods of study', '4.15.b2', 'practical/r1/3rd', '4.6.b7 and the approaches in para 3.6'),
  aad=aad_thr('which methods a student should be able to use', 'Which two methods have you used on the same topic, and what did each let you see?',
              'a call for more than one method in the curriculum'))
s('4.7.b2', **L, verbs=['evaluate', 'analyse'], about='evaluating primary and secondary sources', domain='subject-skill',
  para='Will judge and analyse critically many original and secondary sources by varied authors and from varied settings, from the field and, where relevant, from related subjects.',
  prac='At threshold, graduates will critically evaluate and analyse a wide range of primary and secondary material from diverse authors and contexts, within and beyond the field.',
  ben=TB + 'you will be able to judge and analyse critically a wide range of original and secondary sources by varied authors, including some from related subjects.',
  aaw=aaw_thr('4.7', 2, 'critical evaluation of a wide range of primary and secondary sources', '4.15.b7', 'cognitive/r1/3rd', '4.6.b5 and 4.8.b7'),
  aad=aad_thr('reading, sources and critical analysis', 'How do you decide whether a source is reliable, and how varied are the authors you draw on?',
              'a source-handling outcome tied to diverse reading lists (para 3.16)'))
s('4.7.b3', **L, verbs=['demonstrate'], about='how religion shapes identity and motivation', domain='subject-skill',
  para='Will show a sophisticated grasp of how religion forms personal and shared identities and motives, of the good and harm this can do and of why such identities matter.',
  prac='At threshold, graduates will show sophisticated understanding of how religion shapes personal and communal identity and motivation for good and ill and how much it matters.',
  ben=TB + 'you will show a sophisticated understanding of how religion shapes who people are and what drives them for better and worse and why that matters.',
  aaw=aaw_thr('4.7', 3, 'sophisticated understanding of religion in identity and motivation', '4.15.b1', 'knowledge/r2/3rd', '4.6.b4 and 4.7.b4'),
  aad=aad_thr('religion, identity and motivation', 'Can you give an example where religious identity drove action, and weigh both its positive and harmful effects?',
              'an intellectual skill the issuer pitches as sophisticated at threshold'))
s('4.7.b4', **L, verbs=['demonstrate'], about='conviction and certainty and their effects', domain='subject-skill',
  para='Will show a sensitive awareness of strong conviction and claimed certainty found in religious and non-religious groups and institutions, with their good and bad effects.',
  prac='At threshold, graduates will show sensitive awareness of conviction and claims to certainty in religious and non-religious settings, and their positive and negative effects.',
  ben=TB + 'you will show a sensitive awareness of strong conviction and certainty, in religious and non-religious groups alike, and of the good and harm they can do.',
  aaw=aaw_thr('4.7', 4, 'sensitive awareness of conviction and certainty and their effects', '4.15.b4', 'summary/r3/3rd', '4.7.b3 and 4.8.b4'),
  aad=aad_thr('handling strong convictions, including their own', 'When you meet a view held with certainty, how do you take it seriously and still assess its effects?',
              'a skill to build through discussion, not a test of belief (para 4.5)'))
s('4.7.b5', **L, verbs=['demonstrate'], about='marginalised voices and the causes of marginalisation', domain='subject-skill',
  para='Will show awareness of, and sensitivity to, voices pushed to the margins in religious communities, in public talk about religion and in the field itself, and awareness of what causes this.',
  prac='At threshold, graduates will show awareness of and sensitivity to marginalised voices in communities, public discourse and the discipline, and understand where marginalisation comes from.',
  ben=TB + 'you will notice and respond with care to voices that get pushed aside, in religious groups, in public debate and in this subject itself, and understand why that happens.',
  aaw=aaw_thr('4.7', 5, 'awareness of marginalised voices and the sources of marginalisation', '4.15.b7', 'cognitive/r2/3rd', 'paras 1.24 and 1.25 on decolonising and A6.b6.masters'),
  aad=aad_thr('whose voices the subject hears and whose it leaves out', 'Whose perspective is missing from a topic you studied, and what explains its absence?',
              'an outcome that the course content and reading lists must make possible'))
s('4.7.b6', **L, verbs=['demonstrate'], about='critically informed practice in vocational courses', domain='subject-skill',
  para='On professional, vocational and ministerial courses, will show they can practise with sophistication, creativity and critical insight in complex settings that cannot be predicted.',
  prac='At threshold, graduates of professional, vocational and ministerial courses will show they can practise in a sophisticated, creative and critically informed way in complex, unpredictable contexts.',
  ben=TB + 'if your course is professional, vocational or ministerial, you will show you can practise thoughtfully, creatively and critically in complex and unpredictable situations.',
  aaw=aaw_thr('4.7', 6, 'critically informed practice, for professional, vocational and ministerial courses only', '4.15.b9.2', 'practical/r1/3rd', 'para 4.5 on vocational outcomes and para 2.18'),
  aad=aad_thr('ministry, chaplaincy or other vocational training', 'Describe a complex situation in practice: what did you do, and how did study shape your judgement?',
              'an outcome that applies only to vocational courses'))

# ---- threshold, 4.8 generic skills
LG = dict(L, domain='generic-skill')
s('4.8.b1', **LG, verbs=['communicate'], about='communicating to an audience in varied forms',
  find=('communicate information, ideas, arguments, principles and theories to an intended audience by a variety of means - for '
        'example, by appropriate oral and visual\n\n18\nmeans, by written work of various kinds and lengths, and by dissertations or '
        'extended projects that are clearly and effectively organised and presented'),
  para='Will convey information, ideas, arguments and theories to a chosen audience in several forms, spoken, visual and written, including a well organised dissertation or extended project.',
  prac='At threshold, graduates will communicate ideas and arguments to a defined audience orally, visually and in writing of varied lengths, including a clearly organised dissertation or extended project.',
  ben=TB + 'you will be able to get ideas and arguments across to a particular audience by speaking, visuals and writing, including a long, well organised project or dissertation.',
  aaw=aaw_thr('4.8', 1, 'communication to an intended audience by varied means', '4.15.b8', 'transferable/r1/3rd', 'para 3.23 on assessment methods and 4.8.b3'),
  aad=aad_thr('presentations, essays, dissertations and audience', 'Who is the audience for your next piece of work, and how will you change the form to suit them?',
              'a generic skill the assessment mix should let students show'))
s('4.8.b2', **LG, verbs=['show'], about='independent thought and critical self-awareness',
  para='Will think independently and be critically aware of their own outlooks, commitments and prejudices.',
  prac='At threshold, graduates will show independent thought and critical self-awareness of their own outlooks, commitments and biases.',
  ben=TB + 'you will think for yourself and be critically aware of your own views, commitments and biases.',
  aaw=aaw_thr('4.8', 2, 'independent thought and critical self-awareness', '4.15.b9.1', 'summary/r3/3rd', '4.7.b4 and 4.8.b6'),
  aad=aad_thr('self-awareness and personal standpoint', 'Which of your own commitments most shapes how you read religious material, and how do you keep it in check?',
              'a reflective skill, never an assessment of the student\'s faith (para 4.5)'))
s('4.8.b3', **LG, verbs=['present'], about='arguing a view while treating others fairly',
  para='Will argue for their own position while fairly acknowledging, representing and engaging with the positions of others.',
  prac='At threshold, graduates will argue their own views while fairly acknowledging, representing and engaging with others\' views.',
  ben=TB + 'you will be able to argue for your own view while setting out other people\'s views fairly and responding to them.',
  aaw=aaw_thr('4.8', 3, 'arguing one\'s own view while representing others fairly', '4.15.b3.1', 'cognitive/r2/3rd', '4.8.b4 and 4.8.b1'),
  aad=aad_thr('argument, debate and fairness to opponents', 'Could someone who disagrees with you recognise their view in how you described it?',
              'a skill built in seminars and assessed debates'))
s('4.8.b4', **LG, verbs=['engage'], about='empathetic, critical engagement with others',
  para='Will engage with the convictions and conduct of others with empathy and integrity while reflecting critically.',
  prac='At threshold, graduates will engage with other people\'s convictions and behaviour empathetically, with integrity and critical reflection.',
  ben=TB + 'you will engage with what other people believe and do with empathy and integrity, while still thinking critically.',
  aaw=aaw_thr('4.8', 4, 'empathetic, principled and critical engagement with others', '4.15.b9.1', 'summary/r3/3rd', '1.19 and 4.7.b4'),
  aad=aad_thr('working with people whose beliefs differ', 'Think of a belief you find hard to accept: how would you engage its holder with empathy and still question it?',
              'a generic skill central to fieldwork and placements'))
s('4.8.b5', **LG, verbs=['work'], about='teamwork',
  para='Will work with others in a team or group so that each member\'s strengths are used well.',
  prac='At threshold, graduates will work collaboratively in a team or group, making good use of each member\'s talents.',
  ben=TB + 'you will be able to work in a group so that everyone\'s strengths are put to good use.',
  aaw=aaw_thr('4.8', 5, 'collaborative work in a team or group', '4.15.b9.1', 'transferable/r2/3rd', 'para 3.14 on group learning and 3.22 on group assessment'),
  aad=aad_thr('group work', 'In your last group task, how were roles shared, and was everyone\'s strength used?',
              'a skill that needs group tasks with clear criteria'))
s('4.8.b6', **LG, verbs=['undertake', 'reflect'], about='self-directed study and reflection on learning',
  para='Will study independently or in a self-directed way while managing their time, and reflect on what they do well and less well as learners.',
  prac='At threshold, graduates will undertake self-directed study, manage their time and reflect on their own strengths and weaknesses as learners.',
  ben=TB + 'you will be able to organise your own study and time and reflect on what you do well and less well as a learner.',
  aaw=aaw_thr('4.8', 6, 'self-directed study, time management and reflection on learning', '4.15.b5', 'transferable/r3/3rd', '4.8.b2 and A6.b1.masters'),
  aad=aad_thr('study habits and independent learning', 'What is one strength and one weakness in how you study, and what will you change?',
              'a generic skill that dissertations and extended work develop (para 3.18)'))
s('4.8.b7', **LG, verbs=['identify', 'gather', 'analyse'], about='gathering and analysing primary material',
  para='Will find, collect and analyse primary data and source material, through work on texts or in the field.',
  prac='At threshold, graduates will identify, gather and analyse primary data and sources, whether textual or from fieldwork.',
  ben=TB + 'you will be able to find, collect and analyse original material yourself, from texts or from fieldwork.',
  aaw=aaw_thr('4.8', 7, 'identifying, gathering and analysing primary data and sources', '4.15.b6', 'knowledge/r3/3rd', '4.7.b2 and para 3.12 on fieldwork'),
  aad=aad_thr('research, fieldwork and working with primary texts', 'What primary material have you collected or worked from directly, and how did you analyse it?',
              'a research skill the course should give room to practise'))
s('4.8.b8', **LG, verbs=['make'], about='using resources to find material and compile bibliographies',
  para='Will use the full range of resources well to locate suitable material, build bibliographies, inform research and strengthen presentations.',
  prac='At threshold, graduates will use the whole range of resources well to find material, compile bibliographies, inform research and improve presentations.',
  ben=TB + 'you will use the whole range of resources to find good material, build reference lists, support your research and improve your presentations.',
  aaw=aaw_thr('4.8', 8, 'appropriate use of resources to find material and compile bibliographies', '4.15.b5', 'cognitive/r1/3rd', '4.8.b9 and para 3.16 on discernment in sourcing'),
  aad=aad_thr('finding sources and building a bibliography', 'Where do you look first for material, and what range of resources have you not yet tried?',
              'an information skill to plan with library and learning support'))
s('4.8.b9', **LG, verbs=['use'], about='technology for sources, research and presentation',
  para='Will use technology and computing skills suitably to find material and data, support research and improve presentations.',
  prac='At threshold, graduates will use technology and computer skills appropriately to locate sources and data, support research and enhance presentations.',
  ben=TB + 'you will use digital tools and computer skills sensibly to find material and data, support your research and improve your presentations.',
  aaw=aaw_thr('4.8', 9, 'appropriate use of technology for sources, research and presentation', '4.15.b2', 'transferable/r1/3rd', '4.8.b8 and A6.b8.masters'),
  aad=aad_thr('digital skills and tools', 'Which digital tools do you rely on for research, and which would you like to use better?',
              'a digital literacy outcome'))

# ---- master's, Appendix A6 (lead-in: awarded to students who have demonstrated many of the following, beyond section 4)
LM = dict(type='threshold', rung='threshold', force='threshold', forceFrom='A master\'s degree in the TRS area is awarded to students who',
          level='fheq:7', appliesTo="taught master's graduates in the subject", addressee='learner', award=MA)
MB = 'On a taught master\'s, you will typically show, among other things, '
s('A6.b1.masters', **LM, verbs=['taking', 'finding'], about='independence and self-direction in learning', domain='generic-skill',
  find='a high degree of independence and self-direction in learning, taking responsibility for their own learning experience, and finding many of their own learning resources',
  para='Has shown a large measure of independence and self-direction, owning their learning and locating much of their own material.',
  prac="Master's graduates have shown strong independence and self-direction, taking charge of their learning and sourcing much of their own material.",
  ben=MB + 'a high level of independence: you take charge of your own learning and find much of your own material.',
  aaw=aaw_ma(1, 'independence and self-direction in learning', '4.17.b6', '4.8.b6 at honours'),
  aad=aad_ma('working independently at master\'s level', 'How much of your reading and planning do you now set for yourself, and where do you still wait to be told?'))
s('A6.b2.masters', **LM, verbs=[], about='research methods and skills', domain='subject-skill',
  find='knowledge of appropriate research methods and employment of appropriate research skills',
  para='Has shown knowledge of suitable research methods and put suitable research skills to use.',
  prac="Master's graduates have shown they know fitting research methods and can apply the research skills those methods need.",
  ben=MB + 'that you know which research methods suit a question and can use the skills they need.',
  aaw=aaw_ma(2, 'knowledge and use of appropriate research methods', '4.17.b2', '4.7.b1 and 4.8.b7 at honours'),
  aad=aad_ma('research design and methods', 'Why is your chosen method the right one for your question, and what would another method show?'))
s('A6.b3.masters', **LM, verbs=[], about='sophisticated analysis of sources', domain='subject-skill',
  find='sophisticated analysis of relevant original/primary sources and secondary literature',
  para='Has analysed relevant primary sources and secondary scholarship in a sophisticated way.',
  prac="Master's graduates have analysed relevant primary sources and secondary literature with sophistication.",
  ben=MB + 'a sophisticated analysis of original sources and of what scholars have written about them.',
  aaw=aaw_ma(3, 'sophisticated analysis of primary sources and secondary literature', '4.17.b4.1', '4.7.b2 at honours'),
  aad=aad_ma('working with sources at an advanced level', 'What does your reading of a key source add that the secondary literature misses?'))
s('A6.b4.masters', **LM, verbs=['adopt', 'evaluate', 'reaching'], about='skills for original research and independent conclusions', domain='subject-skill',
  find=('the skills necessary for the production of original research (although the degree of originality appropriate to doctoral '
        'research is not expected at this level of study), with an ability to adopt a critical distance from their source material '
        'and to evaluate it critically, reaching their own independent conclusions'),
  para='Has shown the skills to produce original research (below doctoral originality), standing back from and critically evaluating their material and reaching their own conclusions.',
  prac="Master's graduates have shown they can produce original research short of doctoral originality, keep critical distance from their sources and reach independent conclusions.",
  ben=MB + 'that you can produce original research of your own (not yet doctoral in its originality), step back from your sources, judge them critically and reach your own conclusions.',
  aaw=aaw_ma(4, 'skills for original research, with critical distance and independent conclusions', '4.17.b3', 'para A5 on extended research'),
  aad=aad_ma('the dissertation or extended research project', 'Which conclusion in your project is yours rather than your sources\', and how did you test it?'))
s('A6.b5.masters', **LM, verbs=[], about='complexity of the subject and range of sources', domain='understanding',
  find='critical awareness of the complexity of the subject matter, and the range of sources that are appropriate to their work',
  para='Has shown critical awareness of how complex the subject matter is and of which sources fit their work.',
  prac="Master's graduates have shown critical awareness of the subject's complexity and of the range of sources suited to their work.",
  ben=MB + 'that you are critically aware of how complex your subject is and which kinds of source suit your work.',
  aaw=aaw_ma(5, 'critical awareness of complexity and of fitting sources', '4.17.b1', '4.6.b7 at honours'),
  aad=aad_ma('scoping a topic and choosing sources', 'What makes your topic more complicated than it first looked, and which sources helped you see that?'))
s('A6.b6.masters', **LM, verbs=['employ'], about='reflecting on paradigms to reduce marginalisation', domain='understanding',
  find='critical reflection on the paradigms and perspectives that they employ, with a view to ameliorating the forms of marginalisation and exclusion implicated in them',
  para='Has reflected critically on the frameworks and perspectives they use, aiming to lessen the marginalisation and exclusion those frameworks carry.',
  prac="Master's graduates have reflected critically on their own paradigms and perspectives, aiming to reduce the marginalisation and exclusion built into them.",
  ben=MB + 'critical reflection on the frameworks you use, so that you can lessen the ways they push some people or views aside.',
  aaw=aaw_ma(6, 'critical reflection on paradigms to reduce marginalisation and exclusion', '4.17.b4.2', '4.7.b5 at honours and para 1.24'),
  aad=aad_ma('the assumptions behind a method or framework', 'Whose experience does your framework leave out, and how could you change your approach to include it?'))
s('A6.b7.masters', **LM, verbs=['raised'], about='research ethics and codes of practice', domain='understanding',
  find='an understanding of the ethical issues raised by their research, and compliance with relevant codes of practice',
  para='Has understood the ethical questions their research raises and kept to the relevant codes of practice.',
  prac="Master's graduates have understood the ethics of their own research and complied with relevant codes of practice.",
  ben=MB + 'that you understand the ethical questions your research raises and follow the codes of practice that apply.',
  aaw=aaw_ma(7, 'understanding research ethics and complying with codes of practice', '4.17.b8.1', 'A4.s1 and the subject association\'s Framework of Professional Practice (para A4)'),
  aad=aad_ma('research ethics and fieldwork with communities', 'What ethical risk does your research carry, and which code of practice guides how you handle it?'))
s('A6.b8.masters', **LM, verbs=['evaluate', 'employ'], about='online resources and tools', domain='generic-skill',
  find='an ability to evaluate critically and employ online resources and tools for study and research',
  para='Has shown they can judge critically and use online resources and tools for study and research.',
  prac="Master's graduates have shown they can critically evaluate and use online resources and tools for study and research.",
  ben=MB + 'that you can judge critically and use online resources and tools for study and research.',
  aaw=aaw_ma(8, 'critical evaluation and use of online resources and tools', '4.17.b2', '4.8.b9 at honours'),
  aad=aad_ma('digital research tools', 'How do you check that an online resource is trustworthy before you rely on it?'))

# ---- obliging or outcome paragraphs (body and Appendix A)
def aaw_body(n, what, force_txt, level_txt, nb, extra='Do not claim it is a regulatory requirement.'):
    return (f"Treat this as {force_txt}: {what}. It holds for {level_txt}. Cite it as {CITE}, para {n}. "
            f"{extra} Set it beside {nb}.")

s('1.19', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  find=('Graduates will be equipped with the knowledge, understanding and practical skills to foster empathetic engagement with both '
        'familiar and unfamiliar viewpoints - crucial skills in a diverse society.'),
  verbs=['equipped', 'foster'], about='empathetic engagement with familiar and unfamiliar views', domain='generic-skill', award=HON,
  para='Graduates will have the knowledge, understanding and practical skill to engage with empathy with views both familiar and strange to them, which a diverse society needs.',
  prac='Graduates will be equipped to engage empathetically with familiar and unfamiliar viewpoints, a skill set the issuer ties to employability in a diverse society.',
  ben='You will gain the knowledge and practical skill to engage with empathy with views you know and views new to you, which matters in a diverse society.',
  aaw=aaw_body('1.19', 'an expected outcome, in "will", for graduates, empathetic engagement with familiar and unfamiliar views, stated in the employability paragraphs',
               'an expected outcome', 'honours graduates (FHEQ level 6; our reading, as the paragraph names no level)',
               '4.8.b4, the level 6 descriptor qaa/fheq-2024/4.15.b9.1 and spine:6',
               'Do not count it as one of the threshold lists in section 4 or claim it is regulatory.'),
  aad=('Raise this when a student asks how the subject helps with work or with living among people who believe differently. '
       'Put it to a student in the second person as something the degree will build; to staff, as an employability outcome to make visible. '
       'Ask: When did you last engage seriously with a view very unlike yours, and what did you do to understand it? '
       'Avoid treating it as a separate minimum standard.'))
s('1.22', type='requirement', rung='none', force='will', level='none', appliesTo='institutions or courses with a religious identity or stance', addressee='provider',
  find=('Where an institution or course has a specific religious identity or stance, that will be made clear to all students, and '
        'students will have opportunities to examine, question and challenge that stance, and to consider alternative perspectives.'),
  verbs=['made', 'examine', 'question', 'challenge', 'consider'], about='declaring and opening to challenge a religious stance', domain='none', award='none',
  para='Where an institution or course holds a particular religious identity or stance, it will tell all students so, and students will be able to examine, question and challenge it and weigh other perspectives.',
  prac='If your institution or course has a religious identity or stance, make it clear to every student, and build in real chances for students to examine, question and challenge it and to explore alternatives.',
  ben=('n/a', 'a duty on the institution or course; the student meets its effect (being told and free to challenge), not a standard to reach'),
  aaw=aaw_body('1.22', 'a provider duty in "will" for institutions or courses with a religious stance: declare it to all students and let them question and challenge it',
               'a provider duty', 'any award the statement covers; Appendix A3 repeats it for master\'s courses that train for religious bodies',
               'A3.s3 and the equality, diversity and inclusion paragraphs 1.22 to 1.25',
               'Do not present it as an outcome students must show, or as a legal requirement.'),
  aad=('Raise this with a programme team at a confessional or faith-based provider, or with a teacher designing a module there. '
       'Frame it for staff as a duty of openness and of space to dissent; with a student, explain only that they should be told the stance and may challenge it, without making it their task. '
       'Ask staff: Where do students learn the course\'s stance, and where do they get to argue with it? '
       'Avoid giving the duty to the student as a standard.'))
s('2.9', type='requirement', rung='none', force='will', level='none', appliesTo='all courses in the field', addressee='provider',
  find='All courses within TRS will be designed with a view to the needs of disabled students and with specific learning differences.',
  verbs=['designed'], about='designing for disabled students and learning differences', domain='none', award='none',
  para='Every course in the field will be designed with the needs of disabled students and students with specific learning differences in mind.',
  prac='Design every course with disabled students and students with specific learning differences in mind from the start: varied formats, varied forms of engagement and assessment and accessible materials.',
  ben=('n/a', 'a duty on course design; the student meets its effect, not a standard to reach'),
  aaw=aaw_body('2.9', 'a provider duty in "will": every course is designed around the needs of disabled students and those with specific learning differences',
               'a provider duty', 'all awards in the field', '2.10, the accessibility paragraphs 2.4 to 2.11 and inclusive curriculum design as the paragraph describes it',
               'Do not present it as a student outcome or as the statement\'s reading of the Equality Act, which it does not cite here.'),
  aad=('Raise this with a programme team or module leader planning materials, assessment or delivery. '
       'Frame it for staff as anticipatory design, not adjustment after the event. '
       'Ask: Which parts of your module would a disabled student or one with a specific learning difference find hardest, and what is already in place? '
       'Avoid putting this duty to a student.'))
s('2.10', type='requirement', rung='none', force='will', level='none', appliesTo='courses using discussion and interpersonal activities', addressee='provider',
  find=('Courses within TRS also often require discussion activities and other forms of interpersonal engagement, and these will be '
        'provided in a manner mindful of the needs of those on the autism spectrum or with social anxiety.'),
  verbs=['provided'], about='accessible discussion for autistic and socially anxious students', domain='none', award='none',
  para='Where courses rely on discussion and other interpersonal work, these will be run with attention to the needs of autistic students and those with social anxiety.',
  prac='Run discussion and other interpersonal activities with the needs of autistic students and students with social anxiety in mind.',
  ben=('n/a', 'a duty on how teaching is delivered; not a standard for the student'),
  aaw=aaw_body('2.10', 'a provider duty in "will": discussion and interpersonal activities are delivered with autistic and socially anxious students in mind',
               'a provider duty', 'all awards in the field', '2.9 and the accessibility paragraphs 2.4 to 2.11',
               'Do not extend it to the fieldwork sentence before it, which is in the plain present (Part E).'),
  aad=('Raise this with a teacher planning seminars, assessed debates or group work. '
       'Frame it for staff as a design choice about how discussion runs. '
       'Ask: What alternatives to speaking up in a live group can a student use to take part fully? '
       'Avoid turning it into a demand on the student.'))
s('2.13', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students progressing through an honours course', addressee='both',
  find=('It will also involve the acquisition of academic writing and research skills, enabling students to become increasingly '
        'independent learners and researchers. Single honours courses in the TRS area will generally provide the opportunity for a major '
        'project or dissertation as one way of ensuring that independence and intellectual maturity are attained.'),
  verbs=['involve', 'enabling', 'provide'], about='writing and research skills; the major project', domain='generic-skill', award=HON,
  para='Progression will include gaining academic writing and research skills so that students learn and research more and more independently; single honours courses will generally offer a major project or dissertation to secure that independence.',
  prac='Plan progression so that students build academic writing and research skills towards independence; in single honours, generally offer a major project or dissertation as one route to it.',
  ben='As you progress you will build academic writing and research skills and become a more independent learner and researcher, usually with a major project or dissertation in a single honours course.',
  aaw=aaw_body('2.13', 'an expected outcome of progression in "will", with a soft provider norm ("will generally provide") for a major project in single honours',
               'an expectation, partly for the learner and partly for the course', 'honours study (FHEQ level 6, FQHEIS level 10 per para 2.12)',
               '4.8.b6, 4.8.b7, the level 6 descriptor qaa/fheq-2024/4.15.b5 and spine:6',
               'Do not claim a dissertation is required: the text says generally and calls it one way.'),
  aad=('Raise this when a student asks how the years build up, or a team plans the final-year project. '
       'Tell a student in the second person that writing and research skills are meant to grow towards independence; to staff, frame it as a progression design. '
       'Ask: What could you do on your own this year that you could not do last year? '
       'Avoid stating the dissertation as compulsory.'))
s('2.16', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint honours undergraduates', addressee='learner',
  find=('Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others '
        'according to the subjects covered in a joint course.'),
  verbs=['achieve', 'add'], about='skills reached on joint honours courses', domain='none', award=HON,
  para='Joint honours students will reach part of the subject-specific and generic skills, adding further skills from the other subjects in their course.',
  prac='On joint honours, expect students to reach elements of this subject\'s specific and generic skills, complemented by skills from the partner subject.',
  ben='On a joint honours course you will gain some of this subject\'s specific and general skills and add others from your other subject.',
  aaw=aaw_body('2.16', 'an expected outcome in "will" that limits the threshold lists for joint honours students to elements of them',
               'an expected outcome', 'joint honours (FHEQ level 6)', 'the threshold lists 4.6, 4.7 and 4.8 and para 1.9',
               'Do not claim joint honours students must meet every threshold item.'),
  aad=('Raise this when a joint honours student or course team asks which outcomes apply. '
       'Explain to a student in the second person that they will cover part of this subject\'s skills plus those of the other subject; to staff, frame it as a mapping task across the two subjects. '
       'Ask: Which of this subject\'s skills does your joint course cover, and which come from your other subject? '
       'Avoid holding a joint student to the full single honours list.'))
s('2.20', type='requirement', rung='none', force='will', level='none', appliesTo='courses engaging with religious communities', addressee='provider',
  find='The engagement between TRS courses and religious communities will always be conducted respectfully.',
  verbs=['conducted'], about='respectful engagement with religious communities', domain='none', award='none',
  para='Courses will always engage with religious communities respectfully.',
  prac='Conduct every engagement between the course and religious communities respectfully, even where critical analysis unsettles convictions.',
  ben=('n/a', 'a duty on how courses deal with communities; students take part, but the standard is the course\'s'),
  aaw=aaw_body('2.20', 'a provider duty in "will" that engagement with religious communities is always respectful',
               'a provider duty', 'all courses in the field', 'the partnership paragraph 2.19 and 1.22',
               'Do not read it as limiting critical analysis, which the same paragraph defends.'),
  aad=('Raise this with a programme team planning placements, fieldwork or community partnerships. '
       'Frame it for staff as a standard of conduct alongside critical study. '
       'Ask: How do you prepare students and partners for critical work that may unsettle a community\'s convictions? '
       'Avoid assigning it to a student as their duty.'))
s('2.21', type='requirement', rung='none', force='will', level='none', appliesTo='degree-awarding bodies reviewing courses in the field', addressee='provider',
  find=('They will draw on a range of external reference points, including this Statement, to ensure that their provision aligns with '
        'sector norms. In TRS, periodic review will be conducted with reference to issues of employability; for example, alignment '
        'with standards for initial teacher training.'),
  verbs=['draw', 'ensure', 'conducted'], about='external reference points and employability in periodic review', domain='none', award='none',
  para='Awarding bodies will use external reference points, this statement among them, to keep provision in line with sector norms, and periodic review in the field will consider employability, for example fit with initial teacher training standards.',
  prac='In periodic review, use external reference points, this statement included, to check alignment with sector norms, and address employability, for example alignment with initial teacher training standards.',
  ben=('n/a', 'a duty on the awarding body\'s review process'),
  aaw=aaw_body('2.21', 'a provider duty in "will" on how degree-awarding bodies review provision in the field',
               'a provider duty', 'all awards in the field', '2.22, 2.23 and the employability paragraphs 1.17 to 1.21',
               'Do not name initial teacher training standards as required for every course; they are an example.'),
  aad=('Raise this with a programme team preparing for periodic review or revalidation. '
       'Frame it for staff as the evidence a review will look for. '
       'Ask: Which external reference points does your review document use, and how does it show employability? '
       'Avoid putting this to a student.'))
s('2.23', type='requirement', rung='none', force='will', level='none', appliesTo='higher education providers in periodic review', addressee='provider',
  find=('Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any '
        'proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.'),
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para='Providers will involve external reviewers in periodic review to get an outside view of planned changes and to check that threshold standards are met and content suits the subject.',
  prac='Include external reviewers in periodic review to test proposed changes and to confirm threshold standards are met and content fits the subject.',
  ben=('n/a', 'a duty on the provider\'s review process'),
  aaw=aaw_body('2.23', 'a provider duty in "will" to use external reviewers in periodic review',
               'a provider duty', 'all awards in the field', '2.21, 2.24 on external examining and the threshold lists 4.6 to 4.8',
               'Do not confuse external reviewers here with external examiners in 2.24.'),
  aad=('Raise this with a programme team planning review. '
       'Frame it for staff as a step that checks the threshold standards. '
       'Ask: Who is your external reviewer, and which threshold outcomes will you ask them to look at? '
       'Avoid raising it with students as their concern.'))
s('3.5', type='requirement', rung='none', force='describes', level='none', appliesTo='all courses in the field', addressee='provider',
  find=('In all courses, however, it is essential that the subject matter be investigated in relation to questions of sustainability, '
        'and questions of inclusion and identity such as questions of gender, race, class, sexuality and postcoloniality.'),
  verbs=['investigated'], about='sustainability, inclusion and identity in every course', domain='none', award='none',
  para='Whatever mix of content a course chooses, it is essential that every course examines its subject matter in the light of sustainability and of inclusion and identity (gender, race, class, sexuality, postcoloniality).',
  prac='Whatever content mix you choose, make sure the subject matter is examined in relation to sustainability and to inclusion and identity, including gender, race, class, sexuality and postcoloniality.',
  ben=('n/a', 'a requirement on course content; the student meets it through what is taught'),
  aaw=aaw_body('3.5', 'a content requirement worded "it is essential that", outside the five force words, recorded as describes and listed in Part E',
               'a provider expectation of strong weight', 'every course in the field',
               '3.2, 4.6.b9 and the theme paragraphs 1.22 to 1.29',
               'Do not render "essential" as "must" or "should" without saying the wording is the issuer\'s own.'),
  aad=('Raise this with a programme team reviewing content or a module leader writing a syllabus. '
       'Frame it for staff as a test every course should pass, whatever its focus. '
       'Ask: Where in the course does the subject matter meet sustainability, and where does it meet questions of gender, race, class, sexuality and postcoloniality? '
       'Avoid giving this to a student as a requirement on them.'))
s('3.20', type='expectation', rung='none', force='will', level='none', appliesTo='formative assessment in courses in the field', addressee='provider',
  find=('Formative assignments will provide students with opportunities to build the skills and understanding they will need in their '
        'summative assignments, and opportunities to receive feedback that will help them with that development.'),
  verbs=['provide', 'build', 'receive'], about='what formative work gives students', domain='none', award='none',
  para='Formative tasks will give students chances to build the skills and understanding their summative work needs, and to get feedback that helps them develop.',
  prac='Design formative tasks so that they build the skills and understanding summative tasks need, with feedback that supports that growth.',
  ben=('n/a', 'a duty on assessment design; the student benefits from it but is not judged on it'),
  aaw=aaw_body('3.20', 'a provider expectation in "will" about the purpose of formative assessment',
               'a provider expectation', 'all awards in the field', '3.18, 3.19 and 3.21 on feedback',
               'Do not present it as a rule about marks or weighting.'),
  aad=('Raise this with a teacher or programme team designing assessment. '
       'Frame it for staff as alignment between formative and summative tasks. '
       'Ask: Which skill does each formative task rehearse for the summative one, and when does feedback arrive? '
       'Avoid treating it as a student standard.'))
s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='higher education providers classifying honours degrees', addressee='provider',
  find=('Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and '
        'should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees.'),
  verbs=['refer'], about='using Annex D for performance above the threshold', domain='none', award=HON,
  para='Each provider decides how to evidence achievement above the threshold, and should consult the degree classification descriptions (Annex D) for level 6 and level 10 degrees.',
  prac='Decide your own method for evidencing achievement above threshold, and consult Annex D, the descriptions of degree classes at FHEQ level 6 and FQHEIS level 10, when you do.',
  ben=('n/a', 'a duty on the provider in classifying degrees'),
  aaw=aaw_body('4.2', 'a provider expectation in "should": refer to Annex D when deciding what evidences performance above the threshold',
               'a provider expectation', 'bachelor\'s degrees with honours, FHEQ level 6 and FQHEIS level 10',
               'the Annex D bands in std:doc:qaa-fheq-2024-framework (SL6; for example qaa/fheq-2024/annex-d/summary/r1/2.1), 4.1 and 4.3',
               'Do not claim the statement sets its own typical or excellent lists: it hands that to Annex D.'),
  aad=('Raise this with a programme team or external examiner discussing classification or marking criteria above a pass. '
       'Frame it for staff as the pointer from subject threshold to generic class descriptions. '
       'Ask: Which Annex D descriptions do your marking criteria for a 2.1 and a first draw on? '
       'Avoid presenting it to a student as a rule for them.'))
s('A3.s1', type='expectation', rung='none', force='will', level='fheq:7', appliesTo="applicants for master's degrees in the field", addressee='learner',
  find=("The undergraduate benchmark standards set out in section 4 above indicate the kinds of knowledge, understanding and skills likely "
        "to be required, but applicants for master's degrees will need to have demonstrated these at higher than threshold level."),
  verbs=['indicate', 'demonstrated'], about='entry above the honours threshold', domain='none', award=MA,
  para="The honours standards show the kind of knowledge and skill a master's will need, but applicants will need to have shown them above the threshold.",
  prac="When admitting to a master's, look for evidence of the honours outcomes at a level above the threshold, not merely at it.",
  ben="To start a master's in this field you will need to have shown the undergraduate knowledge and skills at more than the minimum level.",
  aaw=aaw_body('A3', 'an entry expectation, worded "will need to", outside the five force words and recorded as will (Part E): master\'s applicants show the honours outcomes above threshold',
               'an entry expectation', "taught master's admission (FHEQ level 7 by our reading)",
               'the threshold lists 4.6 to 4.8, para 4.2 on Annex D and A6',
               'Do not claim it sets a particular class of degree as the entry requirement; it names none.'),
  aad=("Raise this when a prospective master's student asks whether they are ready, or an admissions tutor asks what to look for. "
       "Tell a student in the second person that entry asks for more than the minimum pass in the undergraduate outcomes; to staff, frame it as an admissions judgement. "
       "Ask: Where have you gone beyond the minimum in your previous study, and can you show it? "
       "Avoid naming a degree class the text does not state."))
s('A3.s2', type='requirement', rung='none', force='should', level='none', appliesTo="master's degrees in the field", addressee='provider',
  find=("In general, master's degrees in the TRS area should be open to all students, irrespective of religious belief, gender, race, "
        "sexuality and disability."),
  verbs=['open'], about="open access to master's study", domain='none', award=MA,
  para="As a rule, master's degrees in the field should be open to every student, whatever their religious belief, gender, race, sexuality or disability.",
  prac="Keep master's admission open to all, regardless of religious belief, gender, race, sexuality or disability, save where A3 allows a genuine occupational requirement.",
  ben=('n/a', 'a duty on the provider in admissions'),
  aaw=aaw_body('A3', 'a provider expectation in "should" that master\'s study is open to all, with an exception for training for particular religious bodies where affiliation is a genuine occupational requirement',
               'a provider expectation', "taught master's degrees", 'A3.s3, 1.22 and the equality paragraphs 1.22 to 1.25',
               'Do not omit the stated exception, and do not describe it as the statement\'s reading of equality law.'),
  aad=("Raise this with an admissions or programme team setting entry criteria for a master's. "
       "Frame it for staff as an openness norm with one narrow exception. "
       "Ask: Does any entry criterion screen by belief, and if so, is the course training for work where affiliation is a genuine occupational requirement? "
       "Avoid presenting it to a student as their obligation."))
s('A3.s3', type='requirement', rung='none', force='will', level='none', appliesTo="master's courses training for work in particular religious bodies", addressee='provider',
  find=("Where this is the case, the nature of the programme will be made clear to all applicants, and students will still have "
        "opportunities to examine, question and challenge the stance of that religious body, and to consider alternative perspectives."),
  verbs=['made', 'examine', 'question', 'challenge', 'consider'], about='transparency and freedom to challenge in confessional training', domain='none', award=MA,
  para="Where affiliation is a genuine requirement, the course will tell all applicants its nature, and students will still be able to examine, question and challenge the religious body's stance and consider alternatives.",
  prac="Where religious affiliation is a genuine occupational requirement, make the course's nature clear to every applicant and keep room for students to question and challenge the sponsoring body's stance.",
  ben=('n/a', 'a duty on the provider; the student meets its effect'),
  aaw=aaw_body('A3', "a provider duty in \"will\" for master's courses that train for particular religious bodies: be transparent with applicants and keep the stance open to challenge",
               'a provider duty', "taught master's degrees", '1.22, which says the same for all courses, and A3.s2',
               'Do not treat it as permitting a closed curriculum.'),
  aad=("Raise this with a team running ministerial or confessional master's training. "
       "Frame it for staff as transparency plus freedom to dissent. "
       "Ask: How do applicants learn the course's religious basis, and where can students challenge it? "
       "Avoid making it the student's duty."))
s('A4.s1', type='expectation', rung='none', force='describes', level='fheq:7', appliesTo="master's students in the field", addressee='learner',
  find='Students are expected to demonstrate that they have considered the ethical issues raised by their study, and in particular by their research.',
  verbs=['demonstrate', 'considered', 'raised'], about='considering the ethics of study and research', domain='understanding', award=MA,
  para="Master's students are expected to show that they have thought about the ethical questions their study, and above all their research, raises.",
  prac="Expect master's students to show they have considered the ethics of their study and especially of their research, with reference to relevant standards such as the subject association's Framework of Professional Practice.",
  ben="On a master's you will be expected to show that you have thought through the ethical questions your study, and especially your research, raises.",
  aaw=aaw_body('A4', 'an expectation worded "are expected to", outside the five force words, recorded as describes (Part E): master\'s students show they have considered the ethics of their study and research',
               'a master\'s expectation', "taught master's degrees (FHEQ level 7 by our reading)",
               'A6.b7.masters, the master\'s descriptor qaa/fheq-2024/4.17.b8.1 and spine:7',
               'Do not claim it as a separate award condition beyond A6.'),
  aad=("Raise this when a master's student plans research or fieldwork. "
       "Put it to a student in the second person as something to show in their work; to staff, as an expectation to build into research training. "
       "Ask: What ethical question does your research raise, and where in your work do you show you have dealt with it? "
       "Avoid reading the appendix aloud."))

GRADE = {}   # threshold only: no rung above or below to link (Part E)
TH = {'1.19': 'theme:enterprise', '1.22': 'theme:edi', '2.9': 'theme:accessibility', '2.10': 'theme:accessibility'}

S5 = dict(
    levels=[
        dict(id='fheq:6', role='cites', locator='D1, 2.12; 4.2', note='honours; threshold lists 4.6 to 4.8 and the generic skills refine it'),
        dict(id='fqheis:10', role='cites', locator='D1, 2.12; 4.2'),
        dict(id='fheq:7', role='cites', locator='D1, 2.17', note="integrated master's; taught master's in Appendix A read at this level (inferred, Part E)"),
        dict(id='fqheis:11', role='cites', locator='D1, 2.17'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.12: 'a degree with honours (FHEQ Level 6; FQHEIS Level 10)'; 4.2 names both)"),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.17: integrated master's at FHEQ Level 7, FQHEIS Level 11); the FHEQ shares one descriptor for both (std:doc:qaa-fheq-2024-framework, S5)"),
    ],
)

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.15', '1.22', '1.23', '1.24', '1.25', '1.29', '2.11', '3.5', '4.6', 'A3']),
    dict(id='theme:accessibility', role='carries', carriedIn=['2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '3.12', '3.23']),
    dict(id='theme:esd', role='carries', carriedIn=['1.14', '1.26', '1.27', '1.28', '1.29', '1.30', '3.5', '4.6']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.30', '1.31', '1.32', '1.33', '2.21']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-theology-and-religious-studies-2019-benchmarks (fourth edition, 2019; not held)',
         note='the advisory group section names the 2019 fourth edition and earlier editions of 2014, 2007 and 2000; the front matter lists key changes'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
         note="4.2: 'Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', for performance above the threshold"),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.12, 2.17, 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.12, 2.17, 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.26 cites the QAA and Advance HE Education for Sustainable Development Guidance; the reference list gives its Executive Summary (std:doc:qaa-advancehe-esd-2021-execsummary)'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='1.30 cites Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers'),
    dict(rel='refersTo', target='Church Minister (integrated degree) apprenticeship standard, Institute for Apprenticeships and Technical Education, 2019 (not yet ingested)', note='1.21'),
    dict(rel='refersTo', target='Association of University Departments of Theology and Religious Studies, Framework of Professional Practice, 2005 (not yet ingested)', note='Appendix A4; reference list'),
    dict(rel='refersTo', target='UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives (not ingested)', note='1.26, 1.28: the eight sustainability competencies'),
    dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary (not yet ingested)', note='front matter'),
]

SB1 = [
    'A field that studies religion and religions critically and globally, including non-religion, atheism and the secular, so that people can understand and act in a world religion shapes (D1, 1.1, 1.11, 3.1, 3.2).',
    'Its identity is itself debated: one internally varied discipline, or theology and religious studies as two linked disciplines; insider and outsider stances and views on truth claims cut across the debate (D1, 1.3, 1.4).',
    'It is taught in secular providers open to any belief and in providers with a religious stance, some training for ministry or chaplaincy, under many course titles (D1, 1.5 to 1.8, 2.6).',
    'Courses are built for breadth (several traditions) or depth (one tradition, often with its languages) or a mix (D1, 2.1, 2.8, 3.4).',
    'It works through many approaches, textual, historical, social scientific, philosophical, theological, feminist, postcolonial and others, and draws on and feeds many neighbouring subjects (D1, 3.6, 3.7, 4.7).',
    'It engages directly with living religion through study visits, fieldwork, placements and partnership with religious communities, which calls for respect and handles unsettling critique (D1, 2.19, 2.20, 3.12, 3.13).',
    "It can change students personally, but a student's spiritual development and religious outlook are not award criteria (D1, 1.12, 4.5, A5).",
]

SB2 = [
    dict(theme='theme:edi', inThisSubject='belonging for students of every belief and background; a declared religious stance that students may challenge; a decolonising approach to content, pedagogy and assessment; critical awareness of the field\'s own role in categorising religions; religion as a protected characteristic; inclusion and identity questions in every course (D1, 1.15, 1.22 to 1.25, 2.11, 3.5, A3)',
         statements=['1.22', '3.5', '4.6.b9', 'A3.s2', 'A3.s3']),
    dict(theme='theme:accessibility', inThisSubject='entry without school religious studies; part-time, online and blended modes; accessible language materials; design for disabled students and specific learning differences; accessible fieldwork, placements and discussion, including for autistic and socially anxious students (D1, 2.4 to 2.11, 3.12, 3.23)',
         statements=['2.9', '2.10']),
    dict(theme='theme:esd', inThisSubject='where social, economic, cultural and environmental concerns meet religion and spirituality; the eight UNESCO competencies each given a religious angle; a stated link to the decolonising approach; sustainability questions in every course and in public debate (D1, 1.14, 1.26 to 1.29, 3.5, 4.6)',
         statements=['3.5', '4.6.b9']),
    dict(theme='theme:enterprise', inThisSubject='named with employability as one theme; graduates valued for cross-disciplinary skill and empathy; placements, workplace modules, community challenges and practitioner teaching; innovation in religious roles; review with employability in view (D1, 1.17 to 1.21, 1.30 to 1.33, 2.21)',
         statements=['1.19', '2.21']),
]

SB3 = dict(
    areas=[
        dict(component='3.1', gloss='religions and worldviews in general, and particular traditions'),
        dict(component='3.2', gloss='seventeen topics, from lived religion and doctrine to media, conflict, science and professional practice'),
        dict(component='3.3', gloss='contemporary issues; gender, feminist, queer, Black, disability, postcolonial and liberationist studies'),
        dict(component='3.4', gloss='classical and scriptural languages in some courses'),
        dict(component='3.6', gloss='nineteen approaches to the study of religion'),
        dict(component='3.7', gloss='thirty-four related subjects'),
    ],
    practices=[
        dict(component='3.8', kind='teaching', gloss='eighteen teaching and learning methods, from lectures to placements'),
        dict(component='3.10', kind='teaching', gloss='lectures and presentations'),
        dict(component='3.11', kind='teaching', gloss='seminars and tutorials for dialogue across differing views'),
        dict(component='3.12', kind='learning', gloss='study visits and fieldwork with living religion'),
        dict(component='3.13', kind='learning', gloss='observing practice beside texts and history'),
        dict(component='3.14', kind='learning', gloss='group and peer learning'),
        dict(component='3.15', kind='learning', gloss='work-based learning and placements'),
        dict(component='3.16', kind='learning', gloss='reading diverse primary and secondary literature'),
        dict(component='3.17', kind='learning', gloss='online materials and discussion'),
        dict(component='3.18', kind='assessment', gloss='varied tasks, feedback, growing independence'),
        dict(component='3.20', kind='assessment', gloss='formative and summative work'),
        dict(component='3.21', kind='assessment', gloss='feedback'),
        dict(component='3.22', kind='assessment', gloss='clear criteria'),
        dict(component='3.23', kind='assessment', gloss='twenty-three assessment methods'),
        dict(component='3.25', kind='assessment', gloss='oral examination of reports and dissertations'),
    ],
)

SB4 = dict(
    rungs=[
        dict(rung='threshold', leadIn="4.6; 4.7; 4.8 (under the heading 'Threshold level (3rd class)', which closes 4.5; the rung defined as the minimum in 4.1)", award=HON, items=24),
        dict(rung='threshold', leadIn='A6 (Appendix A: awarded to students who have shown many of the eight items, beyond section 4)', award=MA, items=8),
        dict(rung='typical', leadIn='none', award=HON, items=0),
        dict(rung='excellent', leadIn='none (4.3 describes excellent students in one sentence, with no list)', award=HON, items=0),
    ],
    rungBases=("4.1: the lists are the minimum for an honours award; 4.2: most students do significantly better, and each provider should "
               "use Annex D's classification descriptions (1st, 2:1, 2:2, 3rd) for that; 4.3: excellent students go beyond the threshold "
               "with originality, insight and readiness for postgraduate research; 4.4: the outcomes are indicative, not a checklist"),
    outcomeLists=[
        dict(leadIn='4.6', gloss='threshold knowledge and understanding', items=9, award=[HON]),
        dict(leadIn='4.7', gloss='threshold subject-specific and intellectual skills', items=6, award=[HON]),
        dict(leadIn='4.8', gloss='threshold generic skills', items=9, award=[HON]),
        dict(leadIn='A6', gloss="master's outcomes, many of which are shown, on top of the honours threshold", items=8, award=[MA]),
    ],
    outcomes=[],
)

SB4A_FULL = []

SB5 = [
    dict(body='Professional, statutory and regulatory bodies (PSRBs), unnamed',
         says='may use the statement for the academic standards expected of students and set their own requirements; vocational courses may need their evaluation and accreditation through visits and desk review (D1, front matter; 2.24)',
         requirements='not-applicable: no body named'),
    dict(body='Institute for Apprenticeships and Technical Education',
         says='approved a Church Minister (integrated degree) apprenticeship standard in 2019 for professional ministry in a Christian context, learning on the job while studying for a degree (D1, 1.21)',
         requirements='not yet ingested (Part E)'),
    dict(body='Association of University Departments of Theology and Religious Studies',
         says="its Framework of Professional Practice is one of the standards master's students are made aware of for research ethics (D1, A4; reference list)",
         requirements='not yet ingested (Part E)'),
    dict(body='Faith bodies and religious bodies (unnamed)',
         says="partners whose own monitoring is accounted for in course design; a religious body may accredit a successful master's student for a role; affiliation may be a genuine occupational requirement for training for its work (D1, 2.25, A1, A3)",
         requirements='not-applicable: no body named'),
]

SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.15', '1.22', '1.23', '1.24', '1.25', '1.29', '2.11', '3.5', '4.6', 'A3'],
             statements=['1.22', '3.5', '4.6.b9', 'A3.s2', 'A3.s3']),
        dict(id='theme:accessibility', named='Accessibility', carriedIn=['2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '3.12', '3.23'],
             statements=['2.9', '2.10']),
        dict(id='theme:esd', named='Education for sustainable development (ESD)', carriedIn=['1.14', '1.26', '1.27', '1.28', '1.29', '1.30', '3.5', '4.6'],
             statements=['3.5', '4.6.b9']),
        dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (EED); Employability (front matter: employability, entrepreneurship and enterprise education)',
             carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.30', '1.31', '1.32', '1.33', '2.21'], statements=['1.19', '2.21']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.12', '2.17', '4.2']),
        dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.12', '2.17', '4.2']),
    ],
    bodies=[
        dict(body='PSRBs (unnamed)', citedIn=['front matter', '2.24']),
        dict(body='Institute for Apprenticeships and Technical Education', citedIn=['1.21']),
        dict(body='Association of University Departments of Theology and Religious Studies', citedIn=['A4']),
        dict(body='faith and religious bodies (unnamed)', citedIn=['2.25', 'A1', 'A3']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees',
             citedIn=['4.2'], role='descriptions of the four honours classes, used for performance above the threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE, Education for Sustainable Development Guidance',
             citedIn=['1.26'], role='the ESD theme; the reference list gives the Executive Summary (std:doc:qaa-advancehe-esd-2021-execsummary)'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers',
             citedIn=['1.30'], role='the enterprise theme'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code',
             citedIn=['front matter'], role='course design, learning and teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
    ],
)

B1 = [
    dict(slug='threshold-standard', definition='the minimum outcomes a student will have shown on being awarded an honours degree in the field (D1, 4.1)',
         beneficiaryDefinition='the least you need to show to earn the honours award', scopeNote='the only rung the statement lists; called third class in the heading before 4.6', category='unknown', practices=['education']),
    dict(slug='breadth-and-depth-courses', definition='two course designs: depth courses centre on one tradition or textual community, often with its languages; breadth courses cover several (D1, 2.1)',
         beneficiaryDefinition='whether your course goes deep into one tradition or covers several', scopeNote='the two may be combined', category='unknown', practices=['education']),
    dict(slug='decolonising-approach', definition='diversifying content, readings, teaching and assessment so marginalised voices count, and questioning Eurocentric framings of the discipline (D1, 1.24)',
         beneficiaryDefinition='making sure the course hears voices and traditions often left out, and questions Western-centred ways of framing religion', scopeNote='linked to sustainability in 1.29', category='unknown', practices=['education']),
    dict(slug='education-for-sustainable-development', definition='in this field, attending to how interdependent social, economic, cultural and environmental concerns meet religion and spirituality (D1, 1.26)',
         beneficiaryDefinition='looking at how religion connects with environmental, social and economic sustainability', scopeNote='abbreviated ESD; the eight UNESCO competencies in 1.28', category='unknown', practices=['education']),
    dict(slug='enterprise-and-entrepreneurship-education', definition='education that builds behaviours, attributes and competencies for employment, contribution to society and a fulfilling life (D1, 1.30)',
         beneficiaryDefinition='learning that builds skills and attitudes for work, society and your own life', scopeNote='abbreviated EED; overlaps with ESD', category='unknown', practices=['education']),
    dict(slug='formative-and-summative-assignments', definition='summative assignments count towards the module mark; formative ones do not (D1, 3.20)',
         beneficiaryDefinition='work that counts towards your mark, and practice work that does not', scopeNote='', category='unknown', practices=['education']),
    dict(slug='challenge-modules', definition="elements of a master's offered to undergraduates to introduce postgraduate study (D1, A4)",
         beneficiaryDefinition="master's-level modules you might try as an undergraduate", scopeNote='', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='Threshold level (3rd class)', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
    dict(concept='breadth-and-depth-courses', form='courses focused on breadth and courses focused on depth', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='decolonising-approach', form='decolonising approach', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education (EED)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='formative-and-summative-assignments', form='formative assignments; summative assignments', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='challenge-modules', form='challenge modules', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [
    dict(citation='Institute for Apprenticeships and Technical Education (2019) Church Minister (Integrated Degree) apprenticeship standard', settles=['SB5', 'S7'], state='wanted'),
    dict(citation='Association of University Departments of Theology and Religious Studies (2005) Framework of Professional Practice', settles=['SB5', 'S7'], state='wanted'),
]

E = [
    'Rungs: threshold only. The three lists 4.6 (knowledge and understanding, 9), 4.7 (subject-specific and intellectual skills, 6) and 4.8 (generic skills, 9) sit under one heading, "Threshold level (3rd class)", which the held text runs onto the end of 4.5. No typical or excellent lists: 4.2 hands performance above the threshold to Annex D and 4.3 describes excellent students in one sentence. Recorded as rungs typical and excellent with no lead-in and no items; no gradeOf links.',
    'Pattern (differs from Psychology): one rung, not three; a master\'s list in Appendix A6 recorded as rung threshold, award master\'s, level fheq:7, id suffix .masters (batch 1 convention). Its lead-in says "many of the following", so no single item is required; every A6 aaw says so.',
    'Force: threshold items take force threshold from 4.1, which defines the lists as the minimum for the award (forceFrom 4.1); the lead-ins themselves say "will be able to". A6 items take threshold from their award-condition lead-in (forceFrom gives its text).',
    'Levels: the taught master\'s in Appendix A states no level; fheq:7 (and fqheis:11) read from the FHEQ\'s Table 1 (std:doc:qaa-fheq-2024-framework, S5): inferred. 2.17 states level 7 and 11 for integrated master\'s only. 1.19, 2.13 and 2.16 name no level; fheq:6 read from their honours context (2.12): inferred.',
    'Skeleton: back-matter-2 swallowed Appendix A (A1 to A6) as excluded matter. Appendix A was read in full; its sections are recorded in SECTIONS (componentType section) and its statements cut with find (A3.s1 to A3.s3, A4.s1, A6.b1 to A6.b8). The skeleton counted no rungs (0).',
    'Skeleton: 4.8.b1 was cut at a page break ("visual\\n\\n18\\nmeans"); re-cut with find to the end of the item, so its source carries the page number 18 from the held text.',
    'Skeleton: theme hits were offset by the run-on sub-headings (the hit on 1.21 is the EDI heading, on 1.25 the ESD heading, on 2.3 the Accessibility heading); confirmed by reading and corrected in S6 and SB6.',
    'Statements cut from paragraphs: one record per obliging or outcome sentence, keyed by the paragraph number and cut with find (1.19, 1.22, 2.9, 2.10, 2.13, 2.16, 2.20, 2.21, 2.23, 3.5, 3.20, 4.2), so `source` holds the sentence, not the whole paragraph. For Abbott at P3: whether 2.13, 2.21, 2.23 and 3.20 (descriptive "will" about courses and review) should count as statements.',
    'Force outside the five: 3.5 "it is essential that" (all courses must examine subject matter for sustainability, inclusion and identity), recorded as describes; for Abbott: should it read as must?',
    'Force outside the five: A3 "will need to have demonstrated" (master\'s entry above threshold), recorded as will; A4 "are expected to demonstrate" (master\'s ethics), recorded as describes; 2.12 "It is expected that each year will see" and 2.15 "it would be expected that" (readiness for postgraduate study), not taken as statements. For Abbott.',
    'Plain-present provider norms, not statements (template open point 5): 2.7 and 2.8 "care is taken"; 2.9 "materials are provided in an accessible manner"; 2.10 fieldwork and placements "are made available"; 2.14 "caution is exercised"; 2.25 "care is taken"; 3.12 and 3.23 reasonable adjustments "are arranged"; 3.18 guidance "is provided"; 3.22 criteria "are provided"; A3 "Providers ensure"; A5 "Assessment does not involve evaluating students\' confessional stances".',
    'Not statements: 2.24 ("external examiners will be asked", "They will consider") describes the sector\'s external examining, hedged by "Typically"; 1.12 and 3.18 "will" are predictive; A5 "Generally, this will be a major project" is a common expectation, not an award condition.',
    'Exclusion of note: 4.5 and A5 say a student\'s personal spiritual development and religious outlook are not award criteria (plain present). Not a statement; carried in SB1 and the aaw and aad of 4.7.b4 and 4.8.b2.',
    'DPN-1: 1.29 refers to "paragraphs 1.19-1.24" for the decolonising approach, which is in 1.24 (the EDI paragraphs are 1.22 to 1.25): an issuer misreference, probably left from renumbering. 1.19 is taken as a statement on its own text, not from this reference. A4 "paragraph 3.1" and A5 "paragraph 3.23" are references, not statements.',
    'Themes: employability is grouped with enterprise and entrepreneurship as one cross-cutting theme in the front matter, so 1.17 to 1.21 are recorded under theme:enterprise; a separate theme:employability id would be new (for std). 4.6.b9 and 3.5 name diversity, inclusion and sustainability as content, tagged in SB2 and SB6 but not in TH (outside the theme paragraphs).',
    'Themes not tagged: 4.7.b5 and A6.b6 (marginalised voices, exclusion) touch EDI without naming it; 3.3 (environmental change; gender, queer, disability studies) touches ESD and EDI as content; left for a consumer to map.',
    'Domain: the issuer files 4.7.b3 to b5 (understanding of identity, conviction, marginalised voices) under subject-specific and intellectual skills; recorded as subject-skill to keep the issuer\'s grouping.',
    'Verbs: A6.b2, A6.b3 and A6.b5 are noun phrases with no verb in the span ("knowledge of", "sophisticated analysis of", "critical awareness of"); verbs left empty. The lead-in verb "demonstrated" is outside the spans.',
    'Codes: buddhism (100798), Judaism (100797) and pastoral studies (100802) are inferred for the course titles Buddhist Studies, Jewish Studies and Practical Theology or Theology, Ministry and Mission; CAH20-02 inferred as the parent. No HECoS code chosen for Religion, Philosophy and Ethics or Religious Education.',
    'Bodies: the PSRBs are not named; faith and religious bodies are unnamed. The Church Minister apprenticeship standard and the subject association\'s Framework of Professional Practice are not yet ingested (D3).',
    'Annex D: cited at 4.2 by its 2019 title; now in std:doc:qaa-fheq-2024-framework (Frameworks 2024). Every threshold aaw points to its third-class cells (qaa/fheq-2024/annex-d/.../3rd).',
    'Frameworks: no CQFW citation in the text; the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework are named in the front matter as quality regimes, not qualification frameworks, and are not recorded in SB6 frameworks.',
    'Licence: the text gives a copyright notice and no re-use terms; held privately, never published.',
    'S9: not researched in P1.',
]
