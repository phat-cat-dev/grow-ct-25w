# Judgement for run 0121, QAA Subject Benchmark Statement: Music (April 2025). std run agent.
# Built by tools/bm_build.py music-2025 --check. Brief BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft.
HON = "bachelor's with honours"
MA = "master's"
CITE = 'QAA, 2025, Music Subject Benchmark Statement, para '

META = dict(
    run='0121', p1='2026-10-03 18:00',
    title='Subject Benchmark Statement Music',
    heading='Subject Benchmark Statement: Music (QAA, April 2025)',
    edition='April 2025 (fifth edition)', published='2025-04',
    status='current',
    supersedes='the 2019 minor update (and the 2016, 2008 and 2002 editions), named in the membership section (section 6)',
    subjects=[
        dict(scheme='hecos', code='100070', label='music', basis='stated'),
        dict(scheme='cah', code='CAH25-02-02', label='music', basis='stated'),
        dict(scheme='hecos', code='100223', label='music production', basis='stated'),
        dict(scheme='hecos', code='101241', label='music therapy', basis='stated'),
        dict(scheme='hecos', code='100035', label='musical theatre', basis='stated'),
        dict(scheme='hecos', code='100674', label='ethnomusicology and world music', basis='stated'),
        dict(scheme='hecos', code='100667', label='musicology', basis='stated'),
        dict(scheme='hecos', code='100695', label='music composition', basis='stated'),
        dict(scheme='hecos', code='100841', label='popular music', basis='stated'),
        dict(scheme='hecos', code='100221', label='music technology', basis='stated'),
        dict(scheme='hecos', code='100427', label='acoustics', basis='stated'),
        dict(scheme='hecos', code='100637', label='musicianship and performance studies', basis='inferred'),
        dict(scheme='hecos', code='100643', label='music and arts management', basis='inferred'),
    ],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in music should know, understand and be able to do, set out for the "
                     "honours degree as a two-column table (a minimum threshold and a typical level) under three headings, knowledge and "
                     "understanding, technical skills and professional skills, with a short list added for master's study. Reach for it "
                     "when designing, approving, reviewing or describing a music course, its outcomes or its marking. It is not a "
                     "curriculum and not a regulatory requirement; in England it is not a sector-recognised standard."),
    summary=("Published by QAA in April 2025 as the fifth edition, the statement covers undergraduate and taught postgraduate degrees "
             "in music, including cognate and specialised degrees such as music production, music therapy, musical theatre, "
             "ethnomusicology and performance. It sets out the subject's context and purposes, five cross-cutting themes (equity, "
             "diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and "
             "entrepreneurship education; generative AI), the distinctive features of a music degree (design, progression, "
             "flexibility, partnership, monitoring and review), its content, teaching, learning and assessment, and benchmark "
             "standards for the honours degree at two rungs, threshold (22 items) and typical (22 items), paired row by row, with "
             "excellence described only in prose, plus five master's outcomes at FHEQ level 7. It points to Annex D for the degree "
             "classes and names three accrediting bodies (JAMES, CDMT, HCPC) and the Equality and Human Rights Commission."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a "
               "sector-recognised standard under the OfS framework; part of the current quality arrangements in Scotland, Wales "
               "and Northern Ireland (D1, front matter: Relationship to legislation)"))

S2 = dict(
    governs="what a graduate in music is expected to know, understand and be able to do at honours, at threshold and typical levels, and the added outcomes for master's study",
    awards=[HON, "master's (taught postgraduate and integrated master's)"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"This Subject Benchmark Statement is relevant to all kinds of undergraduate and taught postgraduate degrees in Music, including broad-ranging Music degrees, cognate degrees such as Sound Studies and Music Production, degrees that intersect closely with other fields, such as Music Therapy and Musical Theatre, and specialised degrees within Music such as Ethnomusicology and Music Performance." (D1, 1.10)',
    statedSubjects=[
        dict(name='Music', locator='(D1, title; 1.1; 1.10)', kind='subject',
             codes=[dict(scheme='hecos', code='100070', label='music'), dict(scheme='cah', code='CAH25-02-02', label='music')]),
        dict(name='Sound Studies', locator='(D1, 1.10; 1.24)', kind='programme title', codes=[]),
        dict(name='Music Production', locator='(D1, 1.10; 2.5; 2.14)', kind='programme title', codes=[dict(scheme='hecos', code='100223', label='music production')]),
        dict(name='Music Therapy', locator='(D1, 1.10; 2.5; 2.14; 3.4)', kind='programme title', codes=[dict(scheme='hecos', code='101241', label='music therapy')]),
        dict(name='Musical Theatre', locator='(D1, 1.10; 2.14)', kind='programme title', codes=[dict(scheme='hecos', code='100035', label='musical theatre')]),
        dict(name='Ethnomusicology', locator='(D1, 1.10; 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100674', label='ethnomusicology and world music')]),
        dict(name='Music Performance', locator='(D1, 1.10; 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100637', label='musicianship and performance studies')]),
        dict(name='Musicology', locator='(D1, 1.16; 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100667', label='musicology')]),
        dict(name='Composition', locator='(D1, 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100695', label='music composition')]),
        dict(name='Popular Music studies', locator='(D1, 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100841', label='popular music')]),
        dict(name='Music Technology', locator='(D1, 1.24)', kind='specialism', codes=[dict(scheme='hecos', code='100221', label='music technology')]),
        dict(name='Acoustics', locator='(D1, 1.24)', kind='specialism', codes=[dict(scheme='hecos', code='100427', label='acoustics')]),
        dict(name='Music Business', locator='(D1, 2.4; 3.4)', kind='programme title', codes=[dict(scheme='hecos', code='100643', label='music and arts management')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Music degree', '2': 'Distinctive features of a Music degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.2', '1.11', 'Purposes and characteristics of a Music degree'), ('1.12', '1.17', 'Equity, diversity and inclusion'),
       ('1.18', '1.22', 'Accessibility and the needs of disabled students'), ('1.23', '1.26', 'Education for sustainable development'),
       ('1.27', '1.36', 'Employability, enterprise and entrepreneurship education'), ('1.37', '1.41', 'Generative artificial intelligence (GenAI)'),
       ('2.1', '2.5', 'Design'), ('2.6', '2.9', 'Progression'), ('2.10', '2.11', 'Flexibility'), ('2.12', '2.15', 'Partnership'),
       ('2.16', '2.20', 'Monitoring and review'), ('3.2', '3.5', 'Content'), ('3.6', '3.14', 'Teaching and learning'),
       ('3.15', '3.18', 'Assessment and feedback'), ('3.19', '3.20', 'Assessment methods'), ('3.21', '3.25', 'Feedback'),
       ('4.1', '4.6', 'Introduction'), ('4.7', '4.7', 'Knowledge and understanding'), ('4.8', '4.8', 'Technical skills'),
       ('4.9', '4.9', 'Professional skills'), ('4.10', '4.11', "Master's level")]

G = {
    '1.1': "the field's breadth and the value of its graduates to society",
    '1.2': 'degrees vary widely; the key elements are listed in 2.2',
    '1.3': 'the subject keeps changing with the needs of its users',
    '1.4': 'the range of traditions reflects a diverse society',
    '1.5': 'branches studied alone, combined or beside other disciplines',
    '1.6': 'distinctive elements of the subject and the resources they need',
    '1.7': 'a range of providers, conservatoires among them',
    '1.8': 'learners arrive by academic, vocational and self-taught routes',
    '1.9': 'where graduates work; self-employment and portfolio careers',
    '1.10': 'the degrees the statement covers',
    '1.11': 'examples are illustrative, not complete',
    '1.12': 'inclusive curricula and the critique of privilege',
    '1.13': 'problems in inherited scholarship; inclusive perspectives',
    '1.14': 'gatekeeping in admission and unequal access to resources',
    '1.15': 'choice, self-direction and identity in creative work',
    '1.16': 'global musics, collaboration and overlooked material',
    '1.17': 'decolonising history and redressing unequal representation',
    '1.18': 'the Equality Act duty and disabilities that bear on music study',
    '1.19': 'specialist support and examples of reasonable adjustments',
    '1.20': 'accessible, flexible design of teaching and assessment',
    '1.21': 'access to music-specific activities, with alternatives',
    '1.22': 'accessible synchronous and online provision',
    '1.23': "sustainability as part of understanding music's value",
    '1.24': 'the role of ESD; an interdisciplinary lens; the SDGs',
    '1.25': 'teaching for sustainability, with SDG-linked examples',
    '1.26': 'the environmental impact of music-making and responses to it',
    '1.27': 'what enterprise education supports; links with employers',
    '1.28': 'entrepreneurship beyond paid employment',
    '1.29': 'roles across the music ecosystem; portfolio careers',
    '1.30': 'resilience and adaptability; careers started before study',
    '1.31': 'professional readiness at graduation',
    '1.32': 'enterprise built into curriculum and assessment',
    '1.33': 'teaching and assessing enterprise directly',
    '1.34': 'industry involvement in enterprise education',
    '1.35': 'learning from staff who are practitioners',
    '1.36': 'transferable qualities; support for freelance and business careers',
    '1.37': 'what generative AI offers music',
    '1.38': 'staff understanding; critical and ethical student use of AI',
    '1.39': 'adapting teaching to use generative AI',
    '1.40': 'adapting assessment to use generative AI',
    '1.41': 'ethical, legal and environmental guidance on generative AI',
    '2.1': 'the variety of programme designs',
    '2.2': 'connected activities that shape every programme',
    '2.3': 'interdisciplinary, global and multicultural by nature',
    '2.4': 'single honours or part of another degree',
    '2.5': 'the variety of taught postgraduate provision',
    '2.6': 'progression across levels towards the threshold',
    '2.7': 'readiness for postgraduate study',
    '2.8': 'joint and combined degrees',
    '2.9': 'exit awards below honours',
    '2.10': 'course length across the UK nations',
    '2.11': 'modes of delivery and ways of gaining credit',
    '2.12': "partnership delivery and the statement's part in it",
    '2.13': 'partnerships that build employability',
    '2.14': 'accreditation by professional bodies',
    '2.15': 'partnerships with schools and colleges; the national plans',
    '2.16': 'monitoring and periodic course review',
    '2.17': 'external reviewers in periodic review',
    '2.18': 'the external examining system',
    '2.19': 'external examiners, live and recorded assessment, annual reports',
    '2.20': 'accreditation of professional and vocational courses',
    '3.1': 'how content shapes teaching and assessment',
    '3.2': 'key content points back to 2.2',
    '3.3': 'diversity of design, focus and approach',
    '3.4': 'interdisciplinary and music-adjacent study',
    '3.5': 'skills and attributes common to graduates',
    '3.6': 'a range of teaching styles; inclusive and practical',
    '3.7': 'lectures and seminars',
    '3.8': 'learning environments, equipment and collections',
    '3.9': 'individual tuition in performance or composition',
    '3.10': 'ensemble tuition',
    '3.11': 'teaching across levels with differentiated criteria',
    '3.12': 'formal and extracurricular performing activity',
    '3.13': 'industry-related teaching and placements',
    '3.14': 'links with support services',
    '3.15': 'the purpose of assessment and feedback',
    '3.16': 'assessment across practice and theory; process and product',
    '3.17': 'authentic assessment',
    '3.18': 'choice of assessment and submission methods',
    '3.19': 'indicative assessment methods',
    '3.20': 'projects and portfolios',
    '3.21': 'clarity about assessment and marking',
    '3.22': 'formats of feedback',
    '3.23': 'continuous feedback and feed forward',
    '3.24': 'discussing and using feedback',
    '3.25': 'peer feedback networks',
    '4.1': 'the two rungs set: minimum threshold and typical',
    '4.2': 'most students exceed the threshold; Annex D',
    '4.3': 'not competence standards; Equality Act guidance',
    '4.4': 'how excellence may be shown',
    '4.5': 'no common curriculum implied',
    '4.6': 'the standards are shown together',
    '4.7': 'knowledge and understanding: threshold and typical columns',
    '4.8': 'technical skills: threshold and typical columns',
    '4.9': 'professional skills: threshold and typical columns',
    '4.10': "outcomes added for master's study",
    '4.11': "master's as a route to doctoral work",
}
CTYPE = {'2.2': 'area', '3.3': 'area', '3.4': 'area', '3.5': 'area',
         '3.6': 'practice', '3.7': 'practice', '3.9': 'practice', '3.10': 'practice', '3.12': 'practice', '3.13': 'practice',
         '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.23': 'practice', '3.25': 'practice',
         '4.7': 'stem', '4.8': 'stem', '4.9': 'stem'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section headings (1 to 4)', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: membership, read for S7 (earlier editions 2019, 2016, 2008, 2002)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------- obliging and outcome paragraphs (sections 1 to 4)
s('1.18', type='requirement', rung='none', force='describes', level='none', appliesTo='music courses and course teams',
  addressee='provider', verbs=['consider', 'take', 'ensure'], about='the Equality Act duty towards disabled students', domain='none', award='none',
  para="Every music course carries a responsibility under the Equality Act 2010 to weigh the needs of disabled students and act ahead of time so they meet no discrimination, harassment or victimisation; the paragraph lists conditions that bear on music study and says teams make spaces and equipment reachable for all.",
  prac="Plan for disabled students before anyone asks: consider the conditions that matter in music (strain injuries, hearing and sight, performance anxiety, neurodiversity, long-term illness), admit flexibly and make sure every student can reach studios, rooms, performance spaces and equipment.",
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=("Describe this as a duty the statement places on music courses through the Equality Act 2010, worded as a responsibility rather than with must or should; it holds at every level and is not an outcome for students. "
       "Cite it as (" + CITE + "1.18) and set it beside paras 1.19 to 1.22 and the caution on competence standards in para 4.3. "
       "Do not claim the statement itself creates the legal duty; the duty comes from the Act."),
  aad=("Raise it with a programme team reviewing access to practical teaching, studios or ensembles, or with staff planning admissions. "
       "Frame it for staff as a planning duty, never as something a student must do. Ask: which practical activities on this course could a disabled student not yet reach, and what is in place before they arrive? "
       "Avoid quoting the list of conditions at length or speaking of a student's condition for them."))
s('1.31', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students at the point of graduating', addressee='learner',
  verbs=['support', 'started', 'begun', 'solved', 'built'], about='professional readiness at graduation', domain='generic-skill', award=HON,
  para="Courses back students on their way into professional life; by graduation students will have begun professional networks and a personal brand, met hard problems in testing settings and grown resilient.",
  prac="Design the course so that, by graduation, students will have begun a professional network and a personal brand, tackled complex problems under pressure and built resilience; transferable skills and preparation for working life sit behind this.",
  ben="By the time you graduate, you will have started a professional network and your own personal brand, worked through hard problems in demanding situations and grown more resilient.",
  aaw=("Present this as an expected outcome (will) for students graduating with honours in music, at FHEQ level 6, placed in the statement's employability, enterprise and entrepreneurship section rather than in the benchmark table. "
       "Cite it as (" + CITE + "1.31) and set it beside the professional-skills rows 4.9.b4 and 4.9.b11, the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6. "
       "Do not claim it is a threshold standard; the table in para 4.9 holds those."),
  aad=("Raise it when a student asks what they should have in place for work by the end of the degree, or a team plans careers provision. "
       "Put it in the second person for a student. Ask: who is in your professional network now, and how do you describe your work to someone who might hire you? "
       "Avoid making it sound like a marked requirement."))
s('2.6', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on honours and integrated master\'s courses in music', addressee='learner',
  verbs=['progress', 'expected', 'builds'], about='progression across levels towards the threshold', domain='none', award=[HON, "integrated master's"],
  para="On an honours degree (FHEQ 6; FQHEIS 10) or integrated master's (FHEQ 7; FQHEIS 11) a student will move up level by level under the institution's rules, each level adding knowledge, expertise and experience towards at least the threshold in subject and generic skills; much of this builds cumulatively.",
  prac="Map each level so that it adds knowledge, expertise and experience that lead towards at least the threshold standards at the end, for example longer and more complex performance or composition, or deeper critical and contextual work.",
  ben="Each year of your course will build on the last, adding knowledge, skill and experience, so that by the end you reach at least the minimum standard for the degree; expect your work to grow longer, more complex or more searching as you go.",
  aaw=("Describe this as the statement's account of progression (will, with an expectation) through an honours degree at FHEQ level 6 or an integrated master's at FHEQ level 7, building towards the threshold standards in paras 4.7 to 4.9. "
       "Cite it as (" + CITE + "2.6). Set it beside the level-by-level progression the FHEQ describes (qaa/fheq-2024/4.10, 4.12 and 4.15 descriptors; spine:4 to spine:6). "
       "Do not claim it fixes what each level must contain; it leaves the rules to each institution."),
  aad=("Raise it when a student asks how the years of a course fit together, or a team designs level outcomes. "
       "Put it plainly; for staff, frame it as the build towards the final threshold. Ask: what in this level's work is longer, harder or deeper than the level before? "
       "Avoid treating earlier levels as if they had to meet the final threshold already."))
s('2.7', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='honours graduates with a second-class degree or higher', addressee='learner',
  verbs=['expected', 'achieved', 'determined'], about='readiness for postgraduate study', domain='none', award=HON,
  para="A music graduate with at least a second-class degree is expected to be able and ready to take on postgraduate study in music or a related field, though each provider sets its own entry requirements.",
  prac="Treat a second-class honours result or better as the point at which graduates are expected to be ready for postgraduate study; note that postgraduate entry rules are each provider's own and may ask for particular skills or marks.",
  ben="If you finish with a second-class degree or higher, you can expect to be ready for postgraduate study in music or a related subject, though each course sets its own entry rules.",
  aaw=("Describe this as an expectation (worded as expected and would, not as a requirement) about honours graduates in music at FHEQ level 6 with a second-class result or above. "
       "Cite it as (" + CITE + "2.7) and set it beside the master's outcomes 4.10.b1.masters to 4.10.b5.masters and the Annex D classes (qaa/fheq-2024/annex-d/summary/r1/2.2). "
       "Do not claim it entitles anyone to a postgraduate place; entry is set by each provider."),
  aad=("Raise it when a student asks whether their degree result opens the way to a master's. "
       "Put it in the second person and plainly. Ask: what result are you working towards, and which skills would the course you have in mind ask for? "
       "Avoid promising admission."))
s('2.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='undergraduates studying music in a joint or combined degree', addressee='learner',
  verbs=['achieve', 'add'], about='joint and combined degrees', domain='none', award=HON,
  para="Students taking music within a joint or combined degree, including major and minor routes, will reach the core of the subject and generic skills set out here and gain others from their other subject.",
  prac="In a joint or combined degree, make sure the music part delivers the core subject-specific and generic skills, while the partner subject adds its own; look for interdisciplinary openings where the two meet.",
  ben="If you study music alongside another subject, you will reach the core music and general skills, and pick up further skills from your other subject.",
  aaw=("Present this as an expected outcome (will) for joint and combined honours students at FHEQ level 6: they meet core elements, not every item, of the standards in paras 4.7 to 4.9. "
       "Cite it as (" + CITE + "2.8). Set it beside para 2.4 on music within other degrees and the honours descriptor qaa/fheq-2024/4.15.b1. "
       "Do not claim the statement says which elements are core; it leaves that open."),
  aad=("Raise it when a joint-honours student or a combined-degree team asks how much of the music standards applies to them. "
       "Ask: which of the music outcomes does your half of the degree cover in full, and which does the other subject supply instead? "
       "Avoid suggesting a joint student must meet every single-honours item."))
s('2.16', type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies and their partners', addressee='provider',
  verbs=['collect', 'analyse', 'undertake', 'form', 'draw'], about='monitoring, review and the student voice', domain='none', award='none',
  para="Degree-awarding bodies and their partners gather and study information and review courses on their own cycle; the student voice will be part of this, and they use external reference points, this statement among them, to check alignment with sector norms.",
  prac="Build the student voice into routine monitoring and periodic review, and use external reference points such as this statement to check that provision sits within sector norms.",
  ben=('n/a', 'a duty on the provider about review; the student meets its effect, not a standard to reach'),
  aaw=("Describe this as a provider expectation (will) for monitoring and review: the student voice forms part of course review. It holds for the course as a whole, not for a level. "
       "Cite it as (" + CITE + "2.16) and set it beside the external review and examining paragraphs 2.17 and 2.19. "
       "Do not claim it prescribes a review cycle; it leaves the cycle to each body."),
  aad=("Raise it with a programme team preparing a periodic review or an annual monitoring report. "
       "Ask: how have students' views shaped the last round of changes, and where is that recorded? "
       "Do not put it to a student as something they must do."))
s('2.17', type='expectation', rung='none', force='will', level='none', appliesTo='providers conducting periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para="External scrutiny is a core part of UK quality assurance; providers will bring in reviewers from other institutions, professional bodies or employers during periodic review to gain an outside view and confirm that threshold standards are met and content suits the subject.",
  prac="Include external reviewers, from other universities, professional bodies or employers, in periodic review to give an independent view on proposed changes and to confirm the threshold standards and the subject content.",
  ben=('n/a', 'a duty on the provider; the student meets its effect, not a standard to reach'),
  aaw=("Describe this as a provider expectation (will) on periodic review, holding for the course as a whole. "
       "Cite it as (" + CITE + "2.17) and set it beside paras 2.16, 2.18 and 2.19 and the threshold columns of paras 4.7 to 4.9 that reviewers check against. "
       "Do not claim it is a regulatory rule; the statement is a reference point."),
  aad=("Raise it with a programme team choosing reviewers or planning a review panel. "
       "Ask: who outside the institution will look at the proposed changes, and does the panel include someone from practice or industry? "
       "Do not present it to students as their concern."))
s('2.19', type='requirement', rung='none', force='must', level='none', appliesTo='external examiners', addressee='provider',
  verbs=['required', 'produce', 'make'], about="external examiners' annual report", domain='none', award='none',
  find='External examiners are required to produce a report each year and make recommendations for changes to modules and assessments (where appropriate).',
  para="External examiners must write a report every year and suggest changes to modules and assessments where they see a need.",
  prac="Expect an annual report from each external examiner, with recommendations on modules and assessment where needed; arrange live attendance or recordings of recitals and event-based assessment so they can judge.",
  ben=('n/a', 'a duty on external examiners and the provider; not a standard for the student'),
  aaw=("Describe this as a requirement (required) on external examiners: one report a year, with recommendations where needed. "
       "Cite it as (" + CITE + "2.19), and set it beside the rest of para 2.19 on attending or reviewing recorded performances and para 2.18 on the examining system. "
       "Do not claim the statement sets the report's content beyond recommendations on modules and assessment."),
  aad=("Raise it with a programme team or a new external examiner planning the year's work. "
       "Ask: how will the examiner see live or recorded performances, and how will their recommendations be answered? "
       "Do not raise it with students as a duty of theirs."))
s('3.21', type='requirement', rung='none', force='describes', level='none', appliesTo='assessment and feedback practice in music courses', addressee='provider',
  verbs=['provided', 'enable'], about='clarity about assessment and marking', domain='none', award='none',
  para="Because assessment is central to learning and professional skill, students are to be told clearly how assessment works and how marks are reached; criteria tied to outcomes and curriculum let them read their mark and see how to improve.",
  prac="Tell students plainly how each assessment runs and how the mark is worked out, and publish criteria aligned to the learning outcomes and curriculum so they can place their mark and see how to do better next time.",
  ben="You can expect to be told clearly how each assessment works and how your mark is worked out, with criteria that show you how to improve your next piece of work.",
  aaw=("Describe this as an obligation on assessment practice, worded as essential rather than with must or should, holding at every level. "
       "Cite it as (" + CITE + "3.21) and set it beside the feedback paragraphs 3.22 to 3.25 and the reference assessment criteria (std:ref:uk-assesscriteria). "
       "Do not claim it prescribes a marking scheme; it asks for clarity and alignment."),
  aad=("Raise it when a student is unsure how a mark was reached, or a team reviews its assessment briefs. "
       "For a student, put it as what they can expect to be told; for staff, as what each brief must make plain. Ask: could a student explain from the brief alone how this work will be marked? "
       "Avoid turning it into a complaint about a particular marker."))
s('3.24', type='expectation', rung='none', force='will', level='none', appliesTo='students receiving feedback on creative and performance work', addressee='both',
  verbs=['include', 'have', 'discuss', 'seek', 'interpret', 'use'], about='discussing and using feedback', domain='none', award='none',
  para="Since creative and performance assessment can turn on personal artistic expression, students will typically be able to talk through and query their feedback and be given ways to read and act on it, a skill the creative industries need.",
  prac="Give students room to talk through and question feedback on creative and performance work, and teach them how to interpret and act on it, as preparation for the creative industries.",
  ben="Because creative and performance work is personal, you will usually get the chance to talk through your feedback, ask what it means and learn how to use it, which is a skill you will need at work.",
  aaw=("Describe this as a typical expectation (will) on feedback for creative and performance work, holding at every level. "
       "Cite it as (" + CITE + "3.24) and set it beside paras 3.21 to 3.23 and 3.25 on feedback and peer feedback. "
       "Do not claim it guarantees a meeting for every assessment; the statement says typically."),
  aad=("Raise it when a student is puzzled or upset by feedback on a performance or composition. "
       "Put it in the second person: they can ask what the feedback means. Ask: which comment do you least understand, and what would you try differently next time? "
       "Avoid defending or overturning the mark yourself."))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers awarding honours degrees in music', addressee='provider',
  verbs=['perform', 'refer'], about='going beyond the threshold; Annex D', domain='none', award=HON,
  para="Most students will do well above the minimum threshold; each provider decides what evidence shows such achievement and should consult Annex D of the national qualifications Frameworks, which describes the four main honours classes.",
  prac="When deciding what evidence shows achievement above the threshold, you should consult Annex D of the UK qualifications Frameworks, which describes the first, upper second, lower second and third classes.",
  ben=('n/a', 'addressed to the provider about how it sets evidence for degree classes'),
  aaw=("Describe this as an expectation (should) on providers awarding honours in music at FHEQ level 6: they refer to Annex D when judging achievement above the threshold. "
       "Cite it as (" + CITE + "4.2) and set it beside the threshold and typical columns of paras 4.7 to 4.9 and the Annex D classes in std:doc:qaa-fheq-2024-framework (qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st). "
       "Do not claim the statement maps its typical level onto a particular class."),
  aad=("Raise it with a programme team writing marking criteria or classification rules. "
       "Ask: where do your criteria for the upper bands come from, and do they match the Annex D descriptions? "
       "Do not put it to a student as a duty; for a student, talk about the class descriptions instead."))
s('4.3', type='expectation', rung='none', force='should', level='none', appliesTo='providers developing competence standards', addressee='provider',
  verbs=['note', 'intended', 'develop', 'informed', 'follow'], about='competence standards and the Equality Act', domain='none', award='none',
  para="The threshold and typical standards are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 in a programme specification may draw on the statement and any PSRB requirements and should follow the latest guidance from the Equality and Human Rights Commission.",
  prac="Do not treat the benchmark table as a list of competence standards; if you set competence standards in a programme specification, base them on this statement and any PSRB requirements and follow the Equality and Human Rights Commission's current guidance.",
  ben=('n/a', 'addressed to the provider about competence standards; not a standard for the student'),
  aaw=("Describe this as an expectation (should) on providers that write competence standards in the Equality Act 2010 sense, holding for the programme as a whole. "
       "Cite it as (" + CITE + "4.3) and set it beside the accessibility paragraphs 1.18 to 1.22 and the bodies in para 2.14. "
       "Do not claim that the threshold or typical items are competence standards; the statement says they are not."),
  aad=("Raise it with a programme team writing a programme specification for an accredited or practice-based course. "
       "Ask: does the specification set any competence standards, and has the current Equality and Human Rights Commission guidance been checked against them? "
       "Do not put it to a student."))

# ------------------------------------------------------------- 4.7 to 4.9: the two-column rung table (threshold | typical), paired by row
FT_T = "a threshold standard: the minimum every student shows for a bachelor's degree with honours in music"
FT_Y = "a typical standard (will): what most honours graduates in music show, above the minimum"
HEAD = {'4.7': 'knowledge and understanding', '4.8': 'technical skills', '4.9': 'professional skills'}

def row(tid, dom, fheq, ad, vt, at, pt, rt, bt, ft, vy, ay, py, ry, by, fy, qt, qy):
    n = tid.rsplit('.b', 1)[0]; k = tid.rsplit('.b', 1)[1]
    yid = tid + '.typical'
    base = dict(level='fheq:6', addressee='learner', award=HON, domain=dom, forceFrom=n)
    P[tid] = dict(type='threshold', rung='threshold', force='threshold', appliesTo='honours graduates in music at the threshold',
                  verbs=vt, about=at, para=pt, prac=rt, ben='At the minimum for your honours degree, ' + bt, find=ft, **base,
                  aaw=("Treat this as " + FT_T + ", at FHEQ level 6 (FQHEIS level 10), in the " + HEAD[n] + " table. "
                       "Cite it as (" + CITE + n + ", threshold column, row " + k + "). "
                       "Do not claim it is a regulatory requirement or that it describes master's study. "
                       "Set it beside its typical partner " + yid + ", the honours descriptor " + fheq + " with spine:6, and the third-class cell " + ad + "/3rd."),
                  aad=("Raise it when a student asks what they must be able to do to pass the degree, or a team checks a module against the minimum. "
                       "Put it plainly: second person for a student, and for staff as what assessment lets every student show. "
                       "Ask: " + qt + " Avoid reading the issuer's wording aloud, and do not treat the typical column as the minimum."))
    P[yid] = dict(type='typical', rung='typical', force='will', appliesTo='honours graduates in music at the typical level',
                  verbs=vy, about=ay, para=py, prac=ry, ben='Going beyond the minimum, as most students do, ' + by, find=fy, **base,
                  aaw=("Treat this as " + FT_Y + ", at FHEQ level 6 (FQHEIS level 10), in the " + HEAD[n] + " table. "
                       "Cite it as (" + CITE + n + ", typical column, row " + k + "). "
                       "Do not present it as the pass requirement, and do not invent an excellent rung: the statement describes excellence only in prose (para 4.4). "
                       "Set it beside the threshold item " + tid + ", the honours descriptor " + fheq + " with spine:6, and the Annex D cells " + ad + "/2.2 and " + ad + "/2.1."),
                  aad=("Raise it when a student wants to know what doing well beyond a pass looks like, or a team writes criteria for the upper bands. "
                       "Put it in plain words: second person for a student, and for staff as what most of a cohort will reach. "
                       "Ask: " + qy + " Avoid presenting it as the minimum; the threshold item " + tid + " is the floor."))
    GRADE[yid] = tid + '|stated'
    OUT.append(dict(outcome=at, threshold=tid, typical=yid, excellent='none', basis='stated', domain=dom, award=HON))

GRADE = {}
OUT = []

# 4.7 knowledge and understanding
row('4.7.b1', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r1',
    ['demonstrate'], 'a body of music and its materials',
    "Will at least know and understand a body of music, together with the materials, texts, discourses and concepts that go with it in their discipline.",
    "Make sure every student can show what they know and understand of a body of music and of the artefacts, texts, resources and ideas attached to it in their field.",
    "you will be able to show that you know and understand a body of music and the materials, texts and ideas that go with it in your area.",
    'demonstrate knowledge and understanding of a body of music and of musical materials, artefacts, texts, discourses, resources and concepts associated with it appropriate to their discipline',
    ['show', 'explore', 'evaluate', 'apply', 'challenge'], 'engaging in depth with scholarship on musical materials',
    "Will typically also be able to explore, assess, use or contest the scholarship and research on musical materials in depth.",
    "Expect most students to go further and engage in depth with the scholarship and research on their musical materials, exploring, testing, applying or challenging it.",
    "you will be able to explore, weigh up, use or argue against the research and scholarship on the music you study, in depth.",
    'in addition, show the ability to explore, evaluate, apply or challenge associated scholarship and research relating to musical materials in depth',
    "Which body of music could you talk about with confidence, and what materials and ideas come with it?",
    "Which piece of scholarship on your music have you questioned or put to work in your own writing or practice?")
row('4.7.b2', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2',
    ['demonstrate'], 'musical contexts',
    "Will at least show knowledge and understanding of the contexts of music, including how it relates to historical, philosophical, cultural, educational and social practice.",
    "Make sure every student can show knowledge of the contexts music sits in: history, philosophy, culture, education and society.",
    "you will be able to show that you understand the settings music belongs to, such as its history, culture, philosophy, education and social life.",
    "demonstrate knowledge and understanding of musical contexts, including the relationship of Music to historical, philosophical, cultural, educational and social practices and phenomena",
    ['demonstrate'], 'critical debates about music in its contexts',
    "Will typically also be aware of the critical debates that arise when music is set in wider contexts.",
    "Expect most students to also know the critical arguments that arise when music is read within its wider contexts.",
    "you will also know the critical arguments that come up when music is placed in its wider setting.",
    'in addition, demonstrate awareness of the critical debates arising from the placing of Music in wider contexts',
    "Which historical, cultural or social setting helps you explain the music you work on?",
    "Which debate about music and its setting could you outline both sides of?")
row('4.7.b3', 'understanding', 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2',
    ['demonstrate'], 'music and other disciplines',
    "Will at least show knowledge and understanding of how music connects with other fields in the arts, humanities and the social and physical sciences, where relevant.",
    "Make sure every student can show how music links with other disciplines across the arts, humanities and the social and physical sciences, as suits their course.",
    "you will be able to show how music connects with other subjects, such as other arts, the humanities and the social or physical sciences.",
    'demonstrate knowledge and understanding of how Music interconnects with other disciplines in the arts, humanities, and social and physical sciences, as appropriate',
    ['show'], 'what interdisciplinary work means for creation and research',
    "Will typically also be aware of what an interdisciplinary approach to music implies for making, innovating and researching.",
    "Expect most students to also see what working across disciplines means for creative work, innovation and research in music.",
    "you will also see what working across subjects means for how music is made, renewed and researched.",
    'in addition, show an awareness of the implications of an interdisciplinary approach to Music for creation, innovation and research',
    "Which other subject has changed how you think about music, and how?",
    "How did drawing on another discipline change a piece of your creative or research work?")
row('4.7.b4', 'subject-skill', 'qaa/fheq-2024/4.15.b3.1', 'qaa/fheq-2024/annex-d/cognitive/r1',
    ['analyse', 'interrogate', 'communicate'], 'analysing musical materials and reporting findings',
    "Will at least be able to analyse and question musical materials and artefacts in their discipline and report what they find coherently.",
    "Make sure every student can analyse and probe the musical materials and artefacts of their field and present the results in a coherent form.",
    "you will be able to analyse and question musical materials in your area and explain what you find clearly.",
    'analyse and interrogate musical materials and artefacts appropriate to their discipline and communicate the findings in a coherent form',
    ['show', 'raised', 'analysing'], 'debate and uncertainty raised by analysis',
    "Will typically also be critically aware of the questions of debate or uncertainty that analysing musical materials raises.",
    "Expect most students to also recognise, critically, where analysis of musical materials leaves matters open or contested.",
    "you will also be critically aware of where analysing music leaves questions open or in dispute.",
    'in addition, show critical awareness of issues of debate or uncertainty raised from analysing musical materials and artefacts',
    "Can you walk through an analysis you have done and say what it showed?",
    "Where did your analysis leave a question open, and how did you deal with that?")
row('4.7.b5', 'understanding', 'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/knowledge/r2',
    ['demonstrate'], 'practice and theory in music',
    "Will at least show an understanding of how artistic practice relates to the theory of music, as it applies to their area.",
    "Make sure every student can show how artistic practice and theoretical thinking in music relate, in the area they study.",
    "you will be able to show how making music and thinking about it in theory relate to each other in your area.",
    'demonstrate an understanding of relationships between artistic practice and theoretical aspects of Music, as applicable to the particular area studied',
    ['critique'], 'critiquing theoretical constructs',
    "Will typically also critique the nature, relevance, purpose and effects of theoretical constructs in music.",
    "Expect most students to also critique the theories and frameworks used in music: what they are, why they matter, what they do and what follows from them.",
    "you will also be able to critique the theories used in music: what they are, what they are for and what they lead to.",
    'in addition, critique the nature, relevance, purpose and consequences of theoretical constructs in Music',
    "How does a theory you have learned show up in the music you make or study?",
    "Which theoretical idea in music would you challenge, and on what grounds?")
row('4.7.b6', 'understanding', 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2',
    ['demonstrate'], 'music and technology',
    "Will at least show an understanding of how music and technology relate.",
    "Make sure every student can show how music and technology shape each other.",
    "you will be able to show how music and technology are connected.",
    'demonstrate an understanding of the relationships between Music and technology.',
    ['show'], 'current discourse on music technologies',
    "Will typically also show deep awareness of current discussion in and about music technologies, shown through critical writing or research through practice.",
    "Expect most students to also show in-depth awareness of present debate on music technologies, through critical writing or practice-as-research.",
    "you will also show a deep awareness of current thinking about music technology, through critical work or research through practice.",
    'in addition, show in-depth awareness of current discourse in and on Music technologies through critical work or practice-as-research.',
    "How has technology changed the music you work with?",
    "Which current debate about music technology have you engaged with in your own work?")

# 4.8 technical skills
row('4.8.b1', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r3',
    ['convey', 'employing'], 'personal expression in practical music-making',
    "Will at least convey personal expression and imagination when making music, using suitable technical and interpretative means.",
    "Make sure every student can bring personal expression and imagination to practical music-making through apt technique and interpretation.",
    "you will be able to put your own expression and imagination into making music, using the right technique and interpretation.",
    'convey personal expression and imagination in practical music-making through employing appropriate technical and interpretative means',
    ['demonstrate'], "an individual musical voice",
    "Will typically show an individual musical personality or voice, through advanced technique and deeper interpretative insight.",
    "Expect most students to show a distinct musical personality, with advanced technique and deeper interpretative insight.",
    "you will show a musical voice of your own, backed by advanced technique and deeper insight into interpretation.",
    'demonstrate an individual musical personality or ‘voice’, through advanced technical skills and deeper levels of interpretative insight',
    "In your last performance or piece, what was yours rather than copied?",
    "What would a listener recognise as your own voice in your music?")
row('4.8.b2', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r1',
    ['recognise', 'use'], 'the components of musical language',
    "Will at least recognise and use the essential components of musical language suited to their discipline and practice.",
    "Make sure every student can recognise and use the core elements of musical language that their field and practice need.",
    "you will be able to recognise and use the basic building blocks of musical language in your area.",
    'recognise and use essential components of musical language appropriate to the discipline and practice',
    ['interrogate'], 'musical language across cultures and genres',
    "Will typically also question how musical language is used in different cultural or genre settings.",
    "Expect most students to also examine how musical language works differently across cultures and genres.",
    "you will also be able to question how musical language works in different cultures or genres.",
    'in addition, interrogate the use of musical language within different cultural or genre-specific settings',
    "Which elements of musical language do you rely on most in your practice?",
    "How does the same musical device work differently in two genres or traditions you know?")
row('4.8.b3', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r1',
    ['recognise', 'respond'], 'musical organisation',
    "Will at least recognise and respond to how music is organised, as their discipline requires.",
    "Make sure every student can recognise and respond to the organisation of music in the ways their field needs.",
    "you will be able to recognise how music is put together and respond to it, as your area needs.",
    'recognise and respond to aspects of musical organisation as appropriate to the discipline',
    ['internalise', 'reconstruct'], 'internalising and rebuilding musical materials',
    "Will typically also internalise musical materials and rebuild them, as suits the discipline.",
    "Expect most students to also absorb musical materials and reconstruct them, in the way their field calls for.",
    "you will also be able to take music in so fully that you can rebuild it yourself.",
    'in addition, internalise and reconstruct musical materials as appropriate to the discipline',
    "Can you hear or read how a piece is organised and say what you noticed?",
    "Could you reconstruct a passage you have learned from memory or by ear?")
row('4.8.b4', 'subject-skill', 'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r2',
    ['collaborate'], 'collaborative music-making',
    "Will at least collaborate in making music, through ensembles, co-creation, improvisation or similar work.",
    "Make sure every student can make music with others, whether in ensembles, joint creation, improvisation or comparable activity.",
    "you will be able to make music with other people, in ensembles, by creating together, improvising or in similar ways.",
    'collaborate in music-making, whether through ensemble performance, co-creation, improvisatory work, or analogous activities',
    ['demonstrate'], 'leadership in a creative team',
    "Will typically also show leadership within a creative team.",
    "Expect most students to also lead within a creative team.",
    "you will also show that you can lead within a creative team.",
    'in addition, demonstrate qualities of leadership within a creative team',
    "What was your part in the last group you made music with?",
    "When have you led a group of musicians, and what did you do to make it work?")
row('4.8.b5', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r3',
    ['employ', 'include'], 'using music technologies',
    "Will at least use music technologies as the discipline needs, from recording and production to composition, sound design, instrument making, live events or generative tools.",
    "Make sure every student can work with the music technologies their field needs, such as recording, production, composition, sound design, instrument building, live events or generative tools.",
    "you will be able to use the music technology your area needs, such as recording, production, sound design, live events or generative tools.",
    'employ music technologies as appropriate to the discipline; this could include recording, producing, composition, sound design, instrument creation, live events, or use of generative technologies.',
    ['demonstrate'], 'nuance and flair with technology',
    "Will typically also use the technology with nuance, creative flair and professionalism, in a way that suits the style.",
    "Expect most students to also handle technology with nuance, creative flair and professional polish, in keeping with the style.",
    "you will also use technology with subtlety, flair and professional polish, in a way that suits the style of the music.",
    'in addition, demonstrate nuance, creative flair and professionalism with the technology in a stylistically appropriate way.',
    "Which music technology do you use, and what do you use it for?",
    "Where in your recent work did your use of technology show style and polish rather than only function?")

# 4.9 professional skills
row('4.9.b1', 'generic-skill', 'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/transferable/r3',
    ['demonstrate'], 'independent research and creative growth',
    "Will at least show independent research skills and the potential to keep developing artistically and creatively.",
    "Make sure every student can show research skills of their own and promise of continued artistic and creative growth.",
    "you will be able to show that you can research on your own and that you can keep growing as an artist.",
    'demonstrate independent research skills and the potential for continuing artistic and creative development',
    ['demonstrate'], 'potential for creative leadership and innovation',
    "Will typically also show the potential to lead and innovate artistically and creatively.",
    "Expect most students to also show promise as artistic and creative leaders and innovators.",
    "you will also show that you have it in you to lead and break new ground creatively.",
    'in addition, demonstrate the potential for artistic and creative leadership and innovation',
    "What have you found out through your own research recently?",
    "Where have you tried something new that others could follow?")
row('4.9.b2', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r3',
    ['work', 'show'], 'independent work, self-motivation and self-awareness',
    "Will at least work on their own and show self-motivation and critical awareness of themselves.",
    "Make sure every student can work independently and shows drive and critical self-awareness.",
    "you will be able to work on your own, keep yourself going and look critically at your own work.",
    'work independently, and show self- motivation and critical self-awareness',
    ['produce'], 'high-quality independent work',
    "Will typically also produce strong work on their own that is rigorous, defensible, robust and imaginative.",
    "Expect most students to also produce independent work of a high standard that is rigorous, defensible, robust and imaginative.",
    "you will also produce strong work of your own that is careful, well argued, sturdy and imaginative.",
    'in addition, produce independent work of high quality (rigorous, defensible, robust, imaginative)',
    "How do you keep a long project moving when no one is checking on you?",
    "Which piece of your own work would you defend as rigorous and imaginative, and why?")
row('4.9.b3', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r2',
    ['work', 'addressing'], 'working in diverse teams',
    "Will at least work with others in diverse teams on shared projects or activities.",
    "Make sure every student can work with others in mixed teams on joint projects or activities.",
    "you will be able to work with a mix of people in teams on shared projects.",
    'work with others in diverse teams addressing joint projects or activities',
    ['demonstrate'], 'teamwork, negotiation and decision-making',
    "Will typically also show advanced teamwork, negotiation, organisation and decision-making.",
    "Expect most students to also show advanced skill in teamwork, negotiating, organising and making decisions.",
    "you will also show advanced skill in working in a team, negotiating, organising and deciding.",
    'in addition, demonstrate advanced skills of teamwork, negotiation, organisation and decision-making',
    "What did you contribute to the last team project you were part of?",
    "When did you help a team reach a decision it was stuck on?")
row('4.9.b4', 'generic-skill', 'qaa/fheq-2024/4.15.b9.2', 'qaa/fheq-2024/annex-d/transferable/r3',
    ['organise', 'manage'], 'scheduling and managing a project',
    "Will at least plan and manage a schedule of work well when carrying out a project.",
    "Make sure every student can organise and run a work schedule effectively while delivering a project.",
    "you will be able to plan and keep to a schedule of work when you carry out a project.",
    'organise and manage a schedule of work effectively in the execution of a project',
    ['demonstrate'], 'confident, adaptable project planning',
    "Will typically also plan and manage projects with confidence and adaptability.",
    "Expect most students to also plan and manage projects confidently and adapt when things change.",
    "you will also plan and run projects with confidence and adjust when plans change.",
    'in addition, demonstrate confidence and adaptability in project planning and management',
    "How did you plan the time for your last project, and did it hold?",
    "When a project plan went wrong, how did you change it?")
row('4.9.b5', 'generic-skill', 'qaa/fheq-2024/4.15.b9.2', 'qaa/fheq-2024/annex-d/transferable/r4',
    ['demonstrate'], 'respect for professional and cultural contexts',
    "Will at least show awareness of, and respect for, different professional and cultural contexts.",
    "Make sure every student can show awareness of and respect for varied professional and cultural settings.",
    "you will be able to show that you know about, and respect, different professional and cultural settings.",
    'demonstrate awareness and respect of different professional and cultural contexts',
    ['adapt', 'respond', 'articulate'], 'adapting to settings and voicing the value of music skills',
    "Will typically also adjust creatively to varied professional and cultural environments and explain the value of musical, intellectual and creative skills there.",
    "Expect most students to also adapt creatively to different professional and cultural environments and make the case for musical, intellectual and creative skills within them.",
    "you will also adapt creatively to different working and cultural settings and explain what musical and creative skills bring to them.",
    'in addition, adapt and respond creatively to different professional and cultural environments, and articulate the value of musical, intellectual and creative skills and associated practices within such contexts',
    "Which professional or cultural setting outside your usual one have you worked in?",
    "How would you explain the value of your musical skills to an employer outside music?")
row('4.9.b6', 'generic-skill', 'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1',
    ['present'], 'presenting work to expert and general audiences',
    "Will at least present work accessibly, so that expert and non-expert audiences alike can follow it, in sound, speech or writing.",
    "Make sure every student can present work in a form both specialists and non-specialists can follow, through sound, speech or writing.",
    "you will be able to present your work so that both experts and people new to it can follow, in sound, speech or writing.",
    'present work in accessible form, intelligible to both expert and non-expert audiences (readers, listeners, consumers) through sonic, verbal and/or written forms of presentation',
    ['demonstrate', 'articulate'], 'imaginative, persuasive presentation',
    "Will typically also show imaginative and persuasive presentation.",
    "Expect most students to also present imaginatively and persuasively.",
    "you will also present your work in imaginative and persuasive ways.",
    'in addition, demonstrate and articulate imaginative and persuasive powers of presentation',
    "Could someone with no music training follow your last presentation or programme note?",
    "What did you do in a recent presentation to win the audience over?")
row('4.9.b7', 'generic-skill', 'qaa/fheq-2024/4.15.b9.3', 'qaa/fheq-2024/annex-d/practical/r1',
    ['demonstrate'], 'awareness of technical and technological skills',
    "Will at least show awareness of the technological and technical skills that suit their work.",
    "Make sure every student can show awareness of the technical and technological skills their work calls for.",
    "you will be able to show that you know which technical and technological skills your work needs.",
    'demonstrate awareness of appropriate technological and technical skills',
    ['demonstrate'], 'applying technical skills, advanced',
    "Will typically show advanced knowledge of how technical and technological skills are applied in their area.",
    "Expect most students to show advanced knowledge of applying technical and technological skills in the area they study.",
    "you will show advanced knowledge of how to apply technical and technological skills in your area.",
    'demonstrate advanced knowledge of the application of technical and technological skills relative to the area studied',
    "Which technical skills does your kind of music work depend on?",
    "Where have you applied a technical skill in a way a beginner would not?")
row('4.9.b8', 'generic-skill', 'qaa/fheq-2024/4.15.b4', 'qaa/fheq-2024/annex-d/professional/r2',
    ['demonstrate'], 'legal and ethical frameworks in music',
    "Will at least show awareness of the legal and ethical frameworks that apply to music practice and procedure.",
    "Make sure every student can show awareness of the legal and ethical rules that govern music practice and procedure, such as rights and consent.",
    "you will be able to show that you know the legal and ethical rules that apply to working in music.",
    'demonstrate an awareness of the legal and ethical frameworks relating to Music practices and procedures',
    ['identify', 'take', 'ensure'], 'ethical and political challenges and ethical practice',
    "Will typically identify ethical and political challenges in music and act to make sure practice is ethical.",
    "Expect most students to spot ethical and political challenges in music and take steps so that practice stays ethical.",
    "you will spot ethical and political problems in music and take action so that the work is done ethically.",
    'identify ethical and political challenges within Music and take steps to ensure ethical practices are undertaken',
    "Which legal or ethical rules have applied to music you have made, recorded or shared?",
    "When did you notice an ethical problem in a music project, and what did you do?")
row('4.9.b9', 'generic-skill', 'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1',
    ['communicate'], 'communicating ideas in a creative team',
    "Will at least communicate musical and creative ideas well to others in a creative team.",
    "Make sure every student can get musical and creative ideas across to others in a creative team.",
    "you will be able to get your musical and creative ideas across to others in a creative team.",
    'communicate musical and creative ideas effectively with others within a creative team',
    ['adapt', 'communicating'], 'adapting language for different stakeholders',
    "Will typically also adjust language and terms when communicating with a range of stakeholders.",
    "Expect most students to also adjust their language and terms for the different people they deal with.",
    "you will also change your language and terms to suit the different people you work with.",
    'in addition, adapt language and terminology when communicating with a variety of stakeholders',
    "How do you explain a musical idea to the rest of a band or team?",
    "How would you describe the same project to a fellow musician, a funder and an audience?")
row('4.9.b10', 'generic-skill', 'qaa/fheq-2024/4.15.b4', 'qaa/fheq-2024/annex-d/transferable/r5',
    ['demonstrate', 'relates'], 'music and wider societal concerns',
    "Will at least show awareness of how music bears on wider concerns in society.",
    "Make sure every student can show awareness of how music connects with wider questions in society.",
    "you will be able to show that you understand how music connects with wider issues in society.",
    'demonstrate an awareness of how Music relates to wider societal concerns',
    ['identify', 'contribute'], 'music and global and societal challenges',
    "Will typically also identify ways music can help to address global and societal challenges.",
    "Expect most students to also identify ways music can help meet global and social challenges.",
    "you will also be able to name ways music can help with global and social challenges.",
    'in addition, identify ways in which Music can contribute to solving global and societal challenges',
    "Which issue in society does the music you study speak to?",
    "How could music help with a problem in your community or beyond?")
row('4.9.b11', 'generic-skill', 'qaa/fheq-2024/4.15.b9.3', 'qaa/fheq-2024/annex-d/transferable/r3',
    ['demonstrate', 'adapt', 'continue'], 'adapting and continuing to learn',
    "Will at least show they can adapt and go on learning.",
    "Make sure every student can show adaptability and the capacity to keep learning.",
    "you will be able to show that you can adapt and keep learning.",
    'demonstrate the ability to adapt and continue to learn.',
    ['demonstrate', 'contribute', 'shaping'], 'shaping the future of music',
    "Will typically also show they can help shape the future of music.",
    "Expect most students to also show they can contribute to where music goes next.",
    "you will also show that you can help shape where music goes next.",
    'in addition, demonstrate an ability to contribute to shaping the future of Music.',
    "What have you had to learn quickly or change how you work recently?",
    "What change in music would you like to be part of, and what are you doing towards it?")

# ------------------------------------------------------------- 4.10 master's list: another award, recorded at the threshold rung (brief convention)
def m(i, dom, verbs, about, para, prac, ben, fw, link, q, find):
    s(i, type='threshold', rung='threshold', force='will', level='fheq:7', appliesTo="students completing a master's degree in music", addressee='learner',
      verbs=verbs, about=about, domain=dom, award=MA, para=para, prac=prac, ben='By the end of your master\'s degree, ' + ben, find=find, forceFrom='4.10',
      aaw=("Treat this as a master's outcome (will) at FHEQ level 7 (FQHEIS level 11), recorded at the threshold rung, which adds to the honours standards in paras 4.7 to 4.9 for master's study in music. "
           "Cite it as (" + CITE + "4.10). Set it beside the honours item " + link + " and the master's descriptor " + fw + " with spine:7. "
           "Do not claim it applies to honours graduates or that the statement grades master's work into threshold and typical levels."),
      aad=("Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. "
           "Ask: " + q + " Avoid presenting it as an honours expectation."))

m('4.10.b1.masters', 'knowledge', ['demonstrate'], 'systematic, critical grasp of current and emerging trends',
  "Will be able to show a systematic, comprehensive and critically aware grasp of current and emerging directions in music research or practice.",
  "Expect master's students to show a systematic and thorough understanding of current and emerging directions in music research or practice, with critical awareness.",
  "you will be able to show a systematic, thorough and critical grasp of where music research or practice is now and where it is heading.",
  'qaa/fheq-2024/4.17.b1', '4.7.b1.typical', "Which current development in your area of music could you explain and critique to a specialist?",
  'demonstrate both a systematic and comprehensive understanding and a critical awareness of current and emerging trends in Music research and/or practice')
m('4.10.b2.masters', 'understanding', ['evaluate', 'apply'], 'evaluating research to apply knowledge originally',
  "Will be able to assess current research and advanced scholarship and use knowledge in original ways in a field of music study or practice.",
  "Expect master's students to evaluate current research and advanced scholarship and apply what they know with originality.",
  "you will be able to judge current research and advanced scholarship and use what you know in original ways.",
  'qaa/fheq-2024/4.17.b3', '4.7.b1.typical', "Where has your reading of recent research changed what you made or argued?",
  'evaluate current research and advanced scholarship to apply knowledge in original ways in an area of Music studies or practice')
m('4.10.b3.masters', 'generic-skill', ['evaluate', 'demonstrate', 'dealing'], 'method, self-direction and originality with complex problems',
  "Will be able to weigh suitable methodologies and show self-direction and originality in handling complex problems in practice or research.",
  "Expect master's students to choose and justify methods and to tackle complex problems with self-direction and originality.",
  "you will be able to weigh up methods and tackle complex problems in practice or research on your own initiative and in original ways.",
  'qaa/fheq-2024/4.17.b6', '4.9.b2.typical', "Which method did you choose for your current project, and what made it the right one?",
  'evaluate appropriate methodologies and demonstrate self-direction and originality in dealing with complex problems in practice and/or research')
m('4.10.b4.masters', 'subject-skill', ['create', 'communicate'], 'new insight, communicated to specialists and others',
  "Will be able to generate new insight in their field and convey conclusions clearly to specialist and general audiences.",
  "Expect master's students to produce new insight in their field and communicate their conclusions clearly to both specialists and non-specialists.",
  "you will be able to come up with new insight in your field and explain your conclusions clearly to experts and to people outside it.",
  'qaa/fheq-2024/4.17.b5', '4.9.b6.typical', "What new insight has your work produced, and how would you explain it to someone outside music?",
  'create new insight in their field of study, and communicate conclusions clearly to specialist and non-specialist audiences')
m('4.10.b5.masters', 'subject-skill', ['complete', 'informed'], 'a major practice project or substantial research project',
  "Will be able to complete a major practice project or a substantial research project grounded in a thorough understanding of the discipline.",
  "Expect master's students to carry through a major practice-based project or a sizeable research project, grounded in thorough understanding of the discipline.",
  "you will be able to complete a major practical project or a substantial piece of research, built on a thorough understanding of your field.",
  'qaa/fheq-2024/4.17.b2', '4.9.b4.typical', "What is your major project, and how does it draw on your understanding of the field?",
  'complete a major piece of practice, or a substantial research project, informed by thorough understandings of the discipline.')

TH = {'1.18': 'theme:accessibility', '1.31': 'theme:enterprise'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.6 (honours: FHEQ Level 6)'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.6 (honours: FQHEIS Level 10)'),
            dict(id='fheq:7', role='cites', locator="D1, 2.6 (integrated master's: FHEQ Level 7); 4.10 (master's list, level inferred)"),
            dict(id='fqheis:11', role='cites', locator="D1, 2.6 (integrated master's: FQHEIS Level 11)"),
            dict(id='fheq:4', role='cites', locator='D1, 2.9 (CertHE)'),
            dict(id='fqheis:8', role='cites', locator='D1, 2.9 (CertHE, as the statement gives it)'),
            dict(id='fheq:5', role='cites', locator='D1, 2.9 (DipHE)'),
            dict(id='fqheis:9', role='cites', locator='D1, 2.9 (DipHE, as the statement gives it)'),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 (inferred)'),
            dict(id='spine:7', role='refers', locator='std:ref:uk-framework R2 (inferred)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.6); agrees with std:doc:qaa-fheq-2024-framework Table 1'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.6); agrees with std:doc:qaa-fheq-2024-framework Table 1'),
                dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.9) for the CertHE; differs from std:doc:qaa-fheq-2024-framework Table 1 (CertHE at fqheis:7): Part E'),
                dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.9) for the DipHE; differs from std:doc:qaa-fheq-2024-framework Table 1 (DipHE at fqheis:8): Part E')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '2.3', '3.6', '3.18']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.18', '1.19', '1.20', '1.21', '1.22', '3.6', '3.14', '4.3']),
      dict(id='theme:esd', role='carries', carriedIn=['1.23', '1.24', '1.25', '1.26', '1.41']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '2.2', '2.13', '3.5', '3.13']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.37', '1.38', '1.39', '1.40', '1.41', '4.8'])]

S7 = [dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='4.2: providers refer to the degree classification descriptions'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='2.6, 2.9: FHEQ levels 4 to 7 named'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='2.6, 2.9: FQHEIS levels 8 to 11 named'),
      dict(rel='refersTo', target='Equality and Human Rights Commission guidance on competence standards (not yet ingested)', note='4.3; Part E'),
      dict(rel='refersTo', target='Equality Act 2010 (legislation; not a standards document)', note='1.18, 4.3'),
      dict(rel='refersTo', target='National Plans for Music Education, England and Wales (2022; not yet ingested)', note='2.15'),
      dict(rel='refersTo', target='United Nations Sustainable Development Goals (not yet ingested)', note='1.24, 1.25'),
      dict(rel='refersTo', target='JAMES, CDMT and HCPC accreditation requirements (not yet ingested)', note='2.14; Part E'),
      dict(rel='overlaps', target='std:doc:qaa-dance-drama-and-performance-2024-benchmarks', note='inferred: musical theatre and performance (1.10, 2.14); Part E'),
      dict(rel='relatedTo', target='other Subject Benchmark Statements for music-adjacent subjects', note='3.4 says Music Business and Music Therapy may reference other statements; inferred, not named')]

S8 = dict(published='2025-04', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='none-stated; an advisory group of academics, students and sector members (D1, section 6)', replacedBy='none')

SB1 = [
    'Music in higher education is a wide field of intellectual and creative activity that builds specialist and general skills and opens many careers inside and outside music (D1, 1.1)',
    'Degrees differ greatly in content, method and approach; some keep to one tradition while others are plural, reflecting cultural diversity (D1, 1.2, 1.4)',
    'Its distinctive elements are practice, creative invention, sensory skill, collaboration and special literacies such as notation and programming, which need space, instruments, technology, collections and practitioner staff (D1, 1.6)',
    'It can be arts- or science-based and meets many other subjects, from the humanities and business to engineering, physics, psychology, medicine and education (D1, 1.5, 2.3)',
    'Every programme draws on linked activities: reading musical texts, creative and re-creative practice, analysis and criticism, repertories and their contexts, the social value of music, teaching music, aesthetics and reception, theory and practice, and vocational skills (D1, 2.2)',
    'It is offered by universities and specialist conservatoires, each with its own mission, to learners who arrive by academic, vocational or self-taught routes (D1, 1.7, 1.8)',
    'Graduates often work for themselves in portfolio careers across music, education, broadcasting, healthcare and the wider cultural sector (D1, 1.9, 1.29)',
]

SB2 = [
    dict(theme='theme:edi', inThisSubject='music study questions inherited canons and privilege, opens to global, decolonial, disability-centred and gender-focused perspectives, and tackles unequal access to instruments, tuition and admission (D1, 1.12 to 1.17)', statements=[]),
    dict(theme='theme:accessibility', inThisSubject='courses plan for disabilities that bear on music study (strain injuries, hearing and sight, performance anxiety, neurodiversity) and make lessons, ensembles, studios, placements and online material reachable (D1, 1.18 to 1.22)', statements=['1.18', '4.3']),
    dict(theme='theme:esd', inThisSubject='students weigh the environmental and social footprint of music-making, from instrument materials and touring to the global music economy, and music is framed against the UN goals (D1, 1.23 to 1.26)', statements=[]),
    dict(theme='theme:enterprise', inThisSubject='enterprise is built into the curriculum through events, commissions, briefs, microbusinesses, placements and practitioner staff, preparing students for freelance portfolio careers (D1, 1.27 to 1.36)', statements=['1.31']),
    dict(theme='theme:generative-ai', inThisSubject='generative AI is used in teaching and assessed projects as a creative collaborator, with guidance on rights, plagiarism, labour, environmental cost and bias (D1, 1.37 to 1.41; 4.8)', statements=['4.8.b5']),
]

SB3 = dict(
    areas=[dict(component='2.2', gloss='the linked activities every programme draws on, from musical texts and practice to aesthetics and vocational skills'),
           dict(component='3.3', gloss='specialist or generalist; arts or science; vocational or liberal'),
           dict(component='3.4', gloss='joint study and music-adjacent subjects such as music business and music therapy'),
           dict(component='3.5', gloss='the skills and attributes graduates share, set out further in section 4'),
           dict(component='1.6', gloss="the subject's distinctive elements and their resource needs")],
    practices=[dict(component='3.6', kind='teaching', gloss='varied, inclusive teaching with practical learning, in person, online or hybrid'),
               dict(component='3.7', kind='teaching', gloss='lectures and seminars for history, analysis and criticism'),
               dict(component='3.9', kind='teaching', gloss='one-to-one tuition in performance or composition'),
               dict(component='3.10', kind='teaching', gloss='ensemble tuition, workshops and masterclasses'),
               dict(component='3.12', kind='learning', gloss='formal and extracurricular performing, often student-led'),
               dict(component='3.13', kind='learning', gloss='industry-linked learning, placements and mentoring'),
               dict(component='1.39', kind='teaching', gloss='teaching adapted to use generative AI'),
               dict(component='1.40', kind='assessment', gloss='assessment adapted to use generative AI'),
               dict(component='3.19', kind='assessment', gloss='indicative methods: written, presented and performed work, and artefacts'),
               dict(component='3.20', kind='assessment', gloss='projects and portfolios, peer and self-assessment'),
               dict(component='3.21', kind='assessment', gloss='clear criteria and marking'),
               dict(component='3.23', kind='assessment', gloss='continuous feedback and feed forward'),
               dict(component='3.25', kind='assessment', gloss='peer feedback networks')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.7; 4.8; 4.9; 4.10', award=[HON, MA], items=27),
           dict(rung='typical', leadIn='4.7; 4.8; 4.9', award=HON, items=22),
           dict(rung='excellent', leadIn='none', award=HON, items=0)],
    rungBases=("4.1 names two rungs, the minimum threshold and the typical standard, for the honours degree; each of 4.7 to 4.9 is a "
               "two-column table (Threshold level, Typical level) under one lead-in, flattened in the held text and read row by row: "
               "22 rows, 22 threshold and 22 typical cells, each typical cell paired with the threshold cell in its row (gradeOf stated). "
               "The threshold count of 27 is 22 honours cells and 5 master's outcomes (4.10), recorded at the threshold rung with award "
               "master's by the brief's convention. Excellence is described only in prose (4.4), with no list, so the excellent rung has no items."),
    outcomeLists=[dict(leadIn='4.10', gloss="outcomes added for master's study, beyond the honours standards", items=5, award=[MA])],
    outcomes=OUT)

SB4A_FULL = []

SB5 = [
    dict(body='Professional, statutory and regulatory bodies (PSRBs) in general', says='may use the statement in defining academic standards; accredit some music courses by reviewing curriculum, facilities, staffing, assessment and partnerships; their requirements may inform competence standards (D1, front matter; 2.14; 2.20; 4.3)', requirements='not yet ingested (Part E)'),
    dict(body='JAMES (Joint Audio Media Education Services)', says='named as an accreditor for areas such as music production (D1, 2.14)', requirements='not yet ingested (Part E)'),
    dict(body='CDMT (Council for Dance, Drama and Musical Theatre)', says='named as an accreditor for areas such as musical theatre (D1, 2.14)', requirements='not yet ingested (Part E)'),
    dict(body='HCPC (Health and Care Professions Council)', says='named as an accreditor for areas such as music therapy (D1, 2.14)', requirements='not yet ingested (Part E)'),
    dict(body='Equality and Human Rights Commission', says='its latest guidance is to be followed by providers that set competence standards (D1, 4.3)', requirements='not yet ingested (Part E)'),
]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, diversity and inclusion', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '2.3', '3.6', '3.18'], statements=[]),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=['1.18', '1.19', '1.20', '1.21', '1.22', '3.6', '3.14', '4.3'], statements=['1.18', '4.3']),
            dict(id='theme:esd', named='Education for sustainable development', carriedIn=['1.23', '1.24', '1.25', '1.26', '1.41'], statements=[]),
            dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education', carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '2.2', '2.13', '3.5', '3.13'], statements=['1.31']),
            dict(id='theme:generative-ai', named='Generative artificial intelligence (GenAI)', carriedIn=['1.37', '1.38', '1.39', '1.40', '1.41', '4.8'], statements=['4.8.b5'])],
    frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.6', '2.9', '4.2']),
                dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.6', '2.9'])],
    bodies=[dict(body='PSRBs (in general)', citedIn=['2.14', '2.20', '4.3']),
            dict(body='JAMES', citedIn=['2.14']), dict(body='CDMT', citedIn=['2.14']), dict(body='HCPC', citedIn=['2.14']),
            dict(body='Equality and Human Rights Commission', citedIn=['4.3'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='the common descriptions of the four honours classes, for judging achievement above the threshold'),
                     dict(document='not yet ingested: listed in Part E', named='Equality Act (2010)', citedIn=['1.18', '4.3'], role='the legal basis for duties to disabled students and for competence standards'),
                     dict(document='not yet ingested: listed in Part E', named='United Nations Sustainable Development Goals (SDGs)', citedIn=['1.24', '1.25'], role='a frame for sustainability in the curriculum'),
                     dict(document='not yet ingested: listed in Part E', named='National Plans for Music Education in Wales and England (both 2022)', citedIn=['2.15'], role='context for partnerships with schools and colleges')])

B1 = [
    dict(slug='continuous-feedback', definition='information given to students throughout a course in order to improve their learning and attainment (D1, 3.23)', beneficiaryDefinition='ongoing comments on your work meant to help you improve', scopeNote='said to be a strength of many music courses', category='unknown', practices=['education']),
    dict(slug='feed-forward', definition='feedback framed so that students can carry what they learned into later projects (D1, 3.23)', beneficiaryDefinition='feedback that tells you what to do next time', scopeNote='given in quotation marks in the text', category='unknown', practices=['education']),
    dict(slug='enterprise-and-entrepreneurship-education', definition='education that builds the behaviours, attributes and competencies that shape career choice and success, abbreviated EEE (D1, 1.27)', beneficiaryDefinition='learning that prepares you to make your own opportunities and work', scopeNote='paired with employability in the section heading', category='unknown', practices=['education']),
    dict(slug='education-for-sustainable-development', definition='a holistic approach across the curriculum to linked questions of climate change, social justice and global inequality, abbreviated ESD (D1, 1.23)', beneficiaryDefinition='learning that helps you act for a sustainable future', scopeNote='framed with the UN SDGs', category='unknown', practices=['education']),
    dict(slug='threshold-and-typical', definition='the two rungs of benchmark standards: the minimum shown at award and what most students show (D1, 4.1, 4.2)', beneficiaryDefinition='the minimum and the usual standard for your honours degree', scopeNote='excellence is described in prose only (4.4)', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='continuous-feedback', form='continuous feedback', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='feed-forward', form='feed forward', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education (EEE)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-and-typical', form='minimum threshold and typical standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [
    dict(source='QAA Subject Benchmark Statement: Music (2019, minor update)', why='the edition this one supersedes, for the change comparison'),
    dict(source='Equality and Human Rights Commission guidance on competence standards', why='cited in 4.3 for providers setting competence standards'),
    dict(source='Accreditation requirements of JAMES, CDMT and HCPC', why='the bodies named in 2.14; their requirements are their own standards documents'),
    dict(source='National Plans for Music Education, England (HM Government, 2022) and Wales (Welsh Government, 2022)', why='cited in 2.15 and in section 5'),
]

E = [
    "Rungs: two, threshold and typical, set as one two-column table (Threshold level | Typical level) in each of 4.7, 4.8 and 4.9 under the lead-in 'students are able to'; 6, 5 and 11 rows. Psychology has a separate list per rung. The table is flattened in the held text and was read row by row: each typical cell normally opens 'in addition,', which marks the row boundary.",
    "Placements to confirm at P3 (no 'in addition' marker): 4.8.b1.typical (the individual 'voice' cell), 4.9.b7.typical (advanced technical knowledge) and 4.9.b8.typical (ethical and political challenges). Each sits between two threshold cells in the text and is read as its row's typical cell.",
    "gradeOf is recorded as stated for all 22 typical cells: the issuer pairs the columns by row, and most typical cells say 'in addition' to their threshold partner. The three rows above rest on the row reading alone; if P3 treats them as inferred, change GRADE for those three ids.",
    "No excellent rung: 4.4 describes excellence in prose (professionalism in presentation; innovative scholarly or creative approaches) with 'may', and gives no list. SB4 records the excellent rung with leadIn none and 0 items.",
    "Master's: 4.10 lists five outcomes under 'Through completing a master's degree, students are able to', after a stem saying master's study 'requires' critical and conceptual understanding beyond the honours standards. Recorded at the threshold rung with award master's, level fheq:7 (inferred: 4.10 names no level; 2.6 names FHEQ 7 only for the integrated master's) and ids 4.10.b<k>.masters, per the brief. The stem's 'requires' is read as the lead-in, not a statement of its own.",
    "Force words outside the five: 1.18 'have a responsibility to' (force describes); 2.7 'it is expected that ... would be capable of' (describes); 3.21 'it is essential ... that students are provided with clarity' (describes); 2.6 'it is expected that each level sees' sits beside 'will progress' (force will, from the latter). For Abbott.",
    "Threshold cells take force threshold: 4.1 calls them the 'minimum threshold' standards for the honours award. Typical cells take the lead-in's 'are able to' (will), via forceFrom on the table's paragraph.",
    "Plain-present provider norms, not statements (template open point 5): 1.19 to 1.22 (course teams ensure access, adjustments and accessible materials), 1.32 ('will often involve' organising events), 1.38 and 1.41 (students work to build a critical understanding of AI; students are provided with guidance), 2.18 (external examiners will typically be asked), 2.20 (courses may require accreditation), 3.6 to 3.14 and 3.22 to 3.23 (teaching and feedback norms).",
    "Not statements by judgement: 4.1 (the rung definition, kept as the lead-in component); 2.5 ('some programmes will allow' is descriptive); 3.17 ('skills that will be used' is descriptive); 4.11 ('may equip').",
    "2.19 is cut to its obliging sentence ('External examiners are required to produce a report each year ...'); the rest of the paragraph is descriptive (may).",
    "2.9 states the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9, where std:doc:qaa-fheq-2024-framework Table 1 and std:doc:qaa-fqheis-2024-framework S5 put them at fqheis:7 and fqheis:8. Recorded as the statement states it in S5; the conflict is for Abbott at P3.",
    "2.14 expands PSRB as 'professional, statutory or professional body'; the front matter has 'professional, statutory and regulatory bodies'. Recorded as PSRBs; the expansion in 2.14 looks like an issuer slip.",
    "Inferred subject codes: hecos 100637 musicianship and performance studies (for 'Music Performance', 1.10) and hecos 100643 music and arts management (for 'Music Business', 2.4 and 3.4). 'Sound Studies' (1.10) has no HECoS term; left uncoded. Acoustics (100427) sits in CAH07 physics though the statement names it within music (1.24).",
    "Inferred relations: overlaps with std:doc:qaa-dance-drama-and-performance-2024-benchmarks (musical theatre, performance); music-adjacent statements in 3.4 are unnamed.",
    "SB6 bodies and documents not yet ingested: JAMES, CDMT, HCPC requirements; Equality and Human Rights Commission guidance; Equality Act 2010; UN SDGs; National Plans for Music Education (England and Wales, 2022); the Quality Code (front matter only, excluded matter).",
    "Cross-cutting themes are five, all with their own sub-headings in section 1, including generative AI (1.37 to 1.41) and employability joined with enterprise. The front matter's list of key changes names them too (excluded matter).",
    "Section 5 (references) names the EDIMS report, ISM's Dignity at Work 2, the Keychange manifesto and the UK Parliament inquiry on misogyny in music: EDI sources, not cited by paragraph; not recorded in SB6.",
    "Pattern differences from Psychology: one two-column table per heading instead of lists per rung; no excellent rung; three headings (knowledge and understanding, technical skills, professional skills); a separate master's list; generative AI as a theme; four 'will' and 'should' provider paragraphs in sections 2 to 4.",
    "CQFW is not named in the text; Wales is named only for course length (2.10) and the Welsh national plan (2.15). No CQFW level recorded.",
]
