# bm_content.py: judgement for run 0103, QAA Subject Benchmark Statement Education Studies (April 2025). std run agent.
# Read by tools/bm_build.py. Keys of P are S4 ids under qaa/education-studies-2025/. All text below except `find` spans is ours.
import json as _json, re as _re

_ST = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_NORM = open('/home/claude/wkspc2601-library/txt/qaa-2025-education-studies-subject-benchmark-statement-standard.norm.txt', encoding='utf-8').read()
_SK = _json.load(open(_ST + '/ingest-std-qaa-education-studies-2025-benchmarks/run-src/bm-skel.json', encoding='utf-8'))
_CS = {c['number']: (c['start'], c['end']) for c in _SK['components']}
_HEADS = ['Purposes and characteristics of an Education Studies degree', 'Equity, diversity and inclusion Vision',
          'Education for s ustainable d evelopment Vision', 'Employability, entrepreneurship and enterprise education Vision',
          'Artificial i ntelligence Vision', 'Accessibility and the needs of disabled students', 'Defining principles',
          'Progression', 'Flexibility', 'Partnership', 'Monitoring and review', 'Subject-specific curriculum',
          'Practice-based curriculum', 'Transversal curriculum', 'Teaching and learning', 'Assessment', 'Vision']

def _tidy(t):
    t = t.rstrip()
    t = _re.sub(r'\s*\n\n\d+\s*$', '', t)
    return t.rstrip()

def _para(n):
    """the paragraph's own text: the skeleton span without trailing sub-headings or a page number"""
    a, b = _CS[n]
    t = _tidy(_NORM[a:b])
    changed = True
    while changed:
        changed = False
        for h in _HEADS:
            if t.endswith(' ' + h) or t.endswith('\n' + h):
                t = _tidy(t[:-len(h)]); changed = True
                break
    return t, a

HON = "bachelor's with honours"
MAS = "master's"
INT = "integrated master's"
NA = ('n/a', 'a duty on the course team or the institution, not a standard the student reaches')
SID = 'qaa/education-studies-2025/'
CITE = 'QAA, 2025, Education Studies Subject Benchmark Statement, %s'

P = {}
def s(i, find=None, after=None, **k):
    if find is None and i in _CS:
        find, after = _para(i)
    if find is not None:
        k['find'] = find; k['after'] = after if after is not None else 0
    P[i] = k

def prov(i, **k):
    d = dict(type='requirement', rung='none', force='should', level='none', appliesTo='Education Studies courses and their teams',
             addressee='provider', domain='none', award='none', ben=NA)
    d.update(k); s(i, **d)

def both(i, **k):
    d = dict(type='expectation', rung='none', force='should', level='fheq:6', appliesTo='Education Studies courses and their students',
             addressee='both', domain='none', award=HON)
    d.update(k); s(i, **d)

def learner(i, **k):
    d = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of Education Studies',
             addressee='learner', award=HON)
    d.update(k); s(i, **d)

# =============================================================== section 1: context and purposes
learner('1.6', verbs=['participate', 'construct', 'contest', 'develop', 'position'], domain='understanding',
  about='taking a reasoned position in educational debate',
  para="Students take part in, build and challenge debates about values, engagement, educational practice and community; by choosing, analysing and combining viewpoints they grow critical capability and so can hold a reasoned stance in a world that keeps changing, ready for many careers and for learning across working life.",
  prac="Give students room to join, shape and contest debates on values and practice, and to choose, analyse and combine viewpoints until they can hold and defend a reasoned stance; tie this to their future careers and continued learning.",
  ben="You can take part in, shape and question debates about values, practice and communities, and you learn to choose, analyse and combine viewpoints so that you can argue for a reasoned stance of your own.",
  q="Which debate in education have you taken a stance on, and which viewpoints brought you there?")
learner('1.9', verbs=['interrogate', 'acknowledging'], domain='understanding',
  about='questioning entrenched language, knowledge and thought',
  para="Students can question core concepts and terms, recognising how dominant ways of speaking, knowing and thinking have become fixed, in the past and now, across formal, informal and hidden curricula.",
  prac="Build in tasks where students question the key terms and concepts of education and trace how dominant language and knowledge have taken hold in formal, informal and hidden curricula.",
  ben="You can question the key ideas and terms you meet, and see how dominant ways of speaking, knowing and thinking have taken hold in what is taught openly, informally and in the hidden curriculum.",
  q="Which taken-for-granted term in education would you question first, and why?")
learner('1.11', verbs=['engage', 'appreciating', 'recognising', 'defining'], domain='understanding',
  about='engaging with EDI and taking a position on justice',
  para="Students can work with questions of equity, diversity and inclusion, seeing what helping to build a just society involves, recognising differing standpoints and setting out where they stand, both in terms of rights, duties, responsibilities and law and beyond them.",
  prac="Ask students to work through EDI questions, weigh different standpoints and state their own position with reference to rights, duties, responsibilities and the law, and also beyond those frames.",
  ben="You can work with questions of equity, diversity and inclusion, see what it takes to help build a fairer society, recognise other people's standpoints and say clearly where you stand.",
  q="Where do you stand on one EDI question in education, and how does the law shape or fail to shape your view?")
both('1.13', force='will', type='outcome', verbs=['reflect', 'question', 'engage', 'understand', 'demonstrating'], domain='generic-skill',
  appliesTo='Education Studies courses and their students', about='reflection, self-understanding and respect for divergent views',
  para="Courses give students the agency to reflect, question and take part; students are practised in reflection and can see what is distinctive about themselves while showing proper respect for views that differ from or oppose their own.",
  prac="Give students real scope to reflect, question and take part, and assess reflection that pairs self-understanding with respect for views far from their own.",
  ben="Your course gives you room to reflect, question and take part, and you can become skilled at reflection, understanding what is distinctive about you while respecting views that differ sharply from yours.",
  q="When did a view you disagreed with change how you see your own position?")
prov('1.15', force='describes', verbs=['places', 'adopt', 'anticipated'], about='the Equality Act duty to anticipate accessibility issues',
  para="The Equality Act 2010 puts a legal duty on education providers to act ahead of need rather than after it, foreseeing accessibility issues in teaching, learning and assessment.",
  prac="Treat accessibility in teaching, learning and assessment as something to plan for in advance, as the Equality Act 2010 requires of the institution, not something to fix once a problem appears.",
  q="Which accessibility barriers in the current design were found only after a student raised them?")
prov('1.16', force='must', verbs=['considered'], about='accessibility in course design and the wider student experience',
  para="The subject is inclusive and open to everyone, including students from varied social and economic backgrounds, with specific learning needs, neurodivergent students and those who need particular access arrangements; it treats accessibility as both a moral and a legal imperative that must be considered in course design and in planning the wider student experience.",
  prac="Build accessibility into the course design itself and into planning the wider student experience, for students with specific learning needs, access requirements or neurodivergence and from every background: this is a must, not an option.",
  q="Where in the design and approval documents is accessibility shown to have been considered?")
prov('1.20', verbs=['characterised'], about='accessible curriculum and clear assessment',
  para="Course curriculum, content and assessment need to be open to every learner, whatever their culture, disability, neurodivergence, identity or background, and every assessment should be clear about its purpose and what it expects.",
  prac="Check curriculum, content and assessment for access across cultures, disabilities, neurodivergence, identities and backgrounds, and make each assessment brief state its purpose and expectations clearly.",
  q="Could a student read each assessment brief and say what it is for and what a good answer looks like?")
prov('1.21', force='will', verbs=['anticipate'], about='anticipating barriers to learning',
  para="Course teams will need to foresee barriers learners might meet; delivery strategies can include support plans, close work with institutional support services and signposting to them.",
  prac="Map the barriers learners may meet before they arise, and plan responses such as support plans, joint work with institutional support and clear signposting to services.",
  q="Which barriers has the team anticipated this year, and what is in place for each?")
prov('1.22', verbs=['make'], about='anticipatory reasonable adjustments',
  para="In line with the Equality Act 2010, every course should adjust its teaching, learning and assessment in advance and reasonably, so that all students can reach its intended learning outcomes.",
  prac="Plan reasonable adjustments to teaching, learning and assessment ahead of need, so that every student has a fair route to the intended learning outcomes.",
  q="Which adjustments are built into the course by default rather than arranged case by case?")
prov('1.23', verbs=['consider', 'ensuring'], about='accessibility in person and online, including assistive technology',
  para="Course teams should think about accessibility for every student, face to face and through digital delivery, so that all can reach the learning resources they need, assistive technology included.",
  prac="Review access to learning resources in person and online, including assistive technology, so that every student can use what they need for their own learning.",
  q="Can every student reach every learning resource, online and on campus, with the assistive technology they use?")
prov('1.24', verbs=['offered', 'considered'], about='accessibility and well-being on placements',
  para="Where a course offers a placement, it should consider good practice on accessibility and on students' well-being, which may mean alternative options, choice in assessment and careers guidance and openings that take account of every student's needs.",
  prac="For any placement element, plan for accessibility and well-being: offer alternatives where needed, allow a choice of assessment and make careers guidance and openings fit the needs of all students.",
  q="What does a student who cannot take the standard placement do instead, and is it assessed fairly?")
both('1.30', verbs=['understand', 'consider'], domain='understanding', about='education and a sustainable future',
  para="Students understand the distinctive and vital part education plays in a sustainable future, through learning across life and in many formal and informal settings; although some parts of a course may treat these themes on their own, course teams should consider teaching, content and assessment in a broader frame.",
  prac="Spread sustainability across teaching, content and assessment rather than leaving it to one module, and help students see how learning across life and settings serves a sustainable future.",
  ben="You will come to understand the part education plays in a sustainable future, through learning at every age and in many settings, and your course should weave sustainability through its teaching, content and assessment.",
  q="Where outside a sustainability module does your course ask you to think about a sustainable future?")
learner('1.31', verbs=['craft', 'working', 'monitor', 'manage'], domain='generic-skill',
  about='personal sustainability and well-being',
  para="Students can build a personal sustainability of their own, both ecological and psychological, keeping watch over and looking after their own well-being and the well-being of people around them, reflectively.",
  prac="Help students develop habits of personal sustainability, ecological and psychological, and reflective ways of tracking and caring for their own and others' well-being.",
  ben="You can build your own personal sustainability, ecological and psychological, by reflecting on and looking after your own well-being and the well-being of people around you.",
  q="What do you do to keep track of your own well-being, and how do you notice when others around you need support?")
prov('1.43', verbs=['engage'], about='course teams applying the AI principles',
  para="Course teams should also work with the AI principles of 1.42 in curriculum design, assessment, recruitment and research; they may find value in engaging with AI across a whole programme rather than in particular modules or stages, recognising that AI brings both openings and problems and calls for critical engagement with its strengths and limits.",
  prac="Apply the AI principles of 1.42 to your own curriculum design, assessment, recruitment and research, and consider threading AI through the programme rather than confining it to one module or stage.",
  q="Where does AI appear across the programme, and is it confined to one module?")

# =============================================================== section 2: distinctive features
both('2.2', force='will', verbs=['progress', 'include'], award=[HON, INT], appliesTo='students on honours and integrated master\'s courses',
  about='progression through the levels to the threshold',
  para="Students on an honours degree (FHEQ Level 6; FQHEIS Level 10) or, where offered, an integrated master's (FHEQ Level 7; FQHEIS Level 11) will move through the levels under each institution's rules, each level adding knowledge, expertise and experience towards meeting the threshold skills of the statement (and any higher ones set); this will usually mean passing, and gaining credit for, all learning and assessment, practical parts included.",
  prac="Design each level so that it builds knowledge, expertise and experience towards the threshold standards, and make the credit rules clear: students will usually need to pass every element, practical ones included.",
  ben="You will move from one level of study to the next, each one building your knowledge, expertise and experience towards the standards for your degree, and you will usually need to pass every part, practical work included.",
  q="How does each year of the course build towards the final standards, and where is the practical work assessed?")
learner('2.3', force='describes', verbs=['undertaking', 'determined'], domain='none',
  about='readiness for postgraduate study',
  para="A graduate with a second-class degree or better would be expected to be ready and able to take on postgraduate study in education or a related field, though entry rules belong to each institution and may ask for set levels of undergraduate achievement.",
  prac="Prepare students so that those with a second-class degree or better are ready for postgraduate study in education or a related field, and advise them that each postgraduate course sets its own entry rules.",
  ben="If you graduate with at least a second-class degree, you would be expected to be ready for postgraduate study in education or a related subject, though each postgraduate course sets its own entry rules.",
  q="What would you need to show a postgraduate admissions tutor about your readiness for further study?")
learner('2.4', verbs=['achieve', 'add', 'explore'], domain='none', appliesTo='students of Education Studies in joint or combined degrees',
  about='core skills in joint and combined degrees',
  para="Students taking Education Studies within a joint or combined degree, major and minor routes included, will reach the core subject-specific and generic skills of the statement and add others from the rest of their degree, with the chance to explore where disciplines overlap.",
  prac="In a joint or combined design, secure the core subject-specific and generic skills of Education Studies, and use the partner subject to add skills and to open up interdisciplinary study.",
  ben="If you study Education Studies alongside another subject, you will gain its core subject and general skills, add others from your second subject and can explore where the two meet.",
  q="Which core Education Studies skills does the joint course secure, and where does the partner subject add to them?")
prov('2.9', force='will', verbs=['form', 'draw'], about='periodic review and the student voice',
  para="Degree-awarding bodies and their partners gather and analyse information and review courses periodically for their own needs; the student voice will form part of this, and they draw on external reference points, this statement among them, to keep provision in line with sector norms.",
  prac="Include the student voice in every periodic review, and use external reference points, this statement among them, to test the course against sector norms.",
  q="How did students' views shape the last periodic review, and which external reference points were used?")
prov('2.10', force='will', verbs=['use', 'ensure'], about='external reviewers in periodic review',
  para="Externality is essential to quality assurance in the UK: providers will use external reviewers in periodic review to gain an independent view of proposed changes and to make sure threshold standards are met and content suits the subject.",
  prac="Bring external reviewers into periodic review so that proposed changes get an independent view and the course is shown to meet threshold standards with content fit for the subject.",
  q="What did the external reviewer say about threshold standards and subject content at the last review?")

# =============================================================== section 3: content, structure and delivery
learner('3.9', verbs=['develop'], domain='generic-skill', about='transversal knowledge and skills',
  para="Transversal knowledge and skills need not belong to one job, task or discipline and serve across many situations and workplaces; because Education Studies is interdisciplinary, students will build a broad set of them that help them at work.",
  prac="Make the transversal knowledge and skills explicit in the course, since students will build a broad set of them that carry across jobs, tasks and settings.",
  ben="Because Education Studies draws on many disciplines, you will build a broad set of knowledge and skills that carry across jobs, tasks and workplaces.",
  q="Which of your skills from this course would you use in a job outside education?")

_T10 = [
  (['apply', 'work', 'interpreting', 'analysing'], 'numeracy and data', "handle numbers with confidence, and interpret and analyse data where it fits"),
  (['take'], 'accountability and honesty', "be honest and answerable, owning the results of their own actions"),
  (['communicate'], 'communicating for different purposes', "communicate for varied ends, such as describing, explaining, persuading, judging and summing up"),
  (['comprehend', 'evaluate', 'utilise'], 'understanding and using data', "understand, judge critically and use data in many settings"),
  (['evaluate', 'determine'], 'judging sources', "judge sources critically for how relevant and useful they are"),
  (['demonstrate'], 'global competence and intercultural understanding', "show global competence and intercultural understanding, alert to other people's needs, backgrounds and experiences"),
  (['demonstrate'], 'empathy and active listening', "show empathy by connecting with others and listening actively"),
  (['engage'], 'respectful debate and negotiation', "debate, negotiate and persuade in ways that are respectful, helpful and fitting"),
  (['engage', 'demonstrating'], 'skilled communication across modes', "communicate skilfully in spoken, non-verbal, visual and written forms, with an eye to audience and medium"),
  (['engage', 'demonstrate'], 'self-care and resilience', "practise self-care and resilience and look after their own well-being in a field bound up with wider society"),
  (['engage'], 'reflection and reflexivity', "reflect, be reflexive and build critical self-awareness"),
  (['facilitate'], 'inclusion and accessibility', "help bring about inclusion and accessibility"),
  (['identify', 'develop', 'leveraging'], 'creative problem-solving and enterprise', "spot problems and work out solutions using creative and enterprising thinking"),
  (['identify'], 'improving own learning', "raise their own learning performance by seeing what to develop and how to get there"),
  (['maintain', 'showing'], 'professional attitude', "keep a professional attitude and treat colleagues at work with respect"),
  (['organise', 'manage', 'arrange'], 'managing information', "organise and manage information so that files, notes and documents can be found again later"),
  (['take'], 'initiative and autonomy', "use initiative where it fits, knowing the limits of their role and their freedom to act"),
  (['take'], 'responsibility and leadership', "accept responsibility, answer for their actions and give a lead"),
  (['use', 'developing', 'make'], 'critical questioning in practice', "ask critical questions in practice, building their own line of enquiry to reach critical judgements"),
  (['use'], 'digital and social media', "use digital and social media where suitable"),
  (['use', 'develop'], 'evidence-informed views', "draw on evidence-informed practice to form a reasoned view"),
  (['utilise'], 'critical and ethical use of AI', "use AI critically and ethically"),
  (['work'], 'collaboration', "work with others collaboratively")]
_Q10 = ["Where have you had to make sense of numbers or data in your studies so far?",
        "When did you last have to own a mistake, and what did you do next?",
        "Which kind of writing or speaking do you find hardest: explaining, persuading or summing up?",
        "What data have you used in an assignment, and how did you judge whether to trust it?",
        "How do you decide whether a source is worth using?",
        "When has learning about another culture changed how you see education?",
        "How do you show someone you are really listening?",
        "When did you last change someone's mind, or have yours changed, in a respectful debate?",
        "How do you change the way you communicate for a different audience?",
        "What do you do to stay well and resilient when the work is heavy?",
        "What has reflection on your own learning shown you this year?",
        "What have you done to make a learning setting more inclusive or accessible?",
        "Which problem have you solved by thinking creatively rather than following a set method?",
        "Which area of your learning are you working to improve, and how?",
        "What does acting professionally mean for you on placement or in group work?",
        "Could you find your notes from last term's module in under a minute?",
        "When have you taken the initiative, and how did you know it was your call to make?",
        "When have you taken the lead and answered for the outcome?",
        "What question would you ask to test a practice you observed?",
        "How do you decide which digital or social media tools fit a task?",
        "What evidence lies behind a view you hold about education?",
        "When is it right to use AI in your work, and when not?",
        "What made your last piece of group work succeed or struggle?"]
def _you(t):
    return (t.replace('their own', 'your own').replace('their actions', 'your actions').replace('their role', 'your role')
             .replace('their freedom', 'your freedom'))
for _k, (_v, _a, _c) in enumerate(_T10, 1):
    _i = '3.10.b%d' % _k
    both(_i, type='expectation', verbs=_v, domain='generic-skill', about=_a,
         para="Course teams should consider giving students opportunities to %s." % _c,
         prac="Consider where the transversal curriculum lets students %s, and how that is taught and assessed." % _c,
         ben="Your course should give you chances to %s." % _you(_c),
         q=_Q10[_k - 1])
P['3.10.b6']['about'] = 'global competence and intercultural understanding'

prov('3.16', verbs=['aligned'], about='aligning assessment with outcomes',
  para="The assessment strategy mirrors the wide range of skills, knowledge and values the statement sets out, and assessment should line up clearly with the outcomes, objectives or competencies it tests.",
  prac="Map each assessment to the outcomes, objectives or competencies it tests, and check that the strategy as a whole covers the skills, knowledge and values the subject asks for.",
  q="For each assessment, which outcomes does it test, and is any outcome left untested?")

# =============================================================== section 4: benchmark standards, prose
prov('4.1', verbs=['defined', 'clarify', 'met'], level='fheq:6', award=[HON, MAS], about='who the standards apply to; joint degrees',
  para="The standards are set for students taking Education Studies as a single honours or master's degree; the subject is also studied in joint, major and minor and professionally focused courses, and no view is taken on how much subject knowledge a joint course needs; where Education Studies is one part of a degree, the institution makes clear how far the standards should be met.",
  prac="If Education Studies is one part of a degree, state in the course documents how far the standards should be met, since the statement leaves that to the institution.",
  q="Where do the course documents say how far a joint honours student should meet these standards?")
prov('4.3', verbs=['specify', 'demonstrate', 'refer', 'describe'], level='fheq:6', award=[HON, MAS], about='the threshold as minimum; evidence by Annex D',
  para="The threshold standards set the least every student completing an honours or master's course can show in each area, and most will do much better; each institution decides what evidence shows this and should refer to Annex D of the Frameworks for Higher Education Qualifications; the tables also describe typical and excellent undergraduate performance, and a student may reach the outcomes at different levels and to differing degrees.",
  prac="Treat the threshold column as the floor for every graduate, use the typical and excellent columns to describe performance above it, and refer to Annex D of the FHEQ when deciding what evidence shows each standard is met.",
  q="How do the course's marking criteria line up with the threshold, typical and excellent columns and with Annex D?")
prov('4.5', find=_NORM[_NORM.index('4.5 Please note'):_NORM.index('Human Rights Commission.', _NORM.index('4.5 Please note')) + len('Human Rights Commission.')],
  verbs=['follow', 'informed'], about='competence standards and the Equality Act',
  para="The minimum threshold, typical and excellent standards do not set universal competence standards for the discipline; a provider that writes competence standards (in the Equality Act 2010 sense) into a programme specification may draw on the statement and any PSRB requirements, and should then follow the latest Equality and Human Rights Commission guidance.",
  prac="Do not treat the standards as competence standards; if you write competence standards into a programme specification, draw on the statement and any PSRB requirements and follow current Equality and Human Rights Commission guidance.",
  q="Does the programme specification set any competence standards, and were they checked against current EHRC guidance?")
_s47 = _NORM.index('4.7 The specific professional')
both('4.7', find=_NORM[_s47:_NORM.index('does not meet them.', _s47) + len('does not meet them.')], force='will',
  verbs=['requires', 'made', 'meet'], domain='none', appliesTo='students on PSRB-accredited courses', type='requirement',
  about='professional competence as a condition of a PSRB-accredited award',
  para="This row covers the professional requirements and the learning ability needed for further professional training; where a degree calls for professional competencies to be assessed, the PSRB-accredited award will not be made unless the student meets them.",
  prac="Where the course carries PSRB accreditation that assesses professional competencies, make clear to students that the accredited award will not be made without them, and assess them separately from the academic standards.",
  ben="If your course leads to an award accredited by a professional body, you will not receive that accredited award unless you meet its professional competencies.",
  q="Does your course lead to a professionally accredited award, and do you know which competencies it assesses?")
_p1 = 'The student has demonstrated achievement of professional competence when assessed against the requirements of a PSRB.'
_p2 = 'The student has adhered to the appropriate rules and/or conventions set by regulators or the industry.'
s('4.7.b1', find=_p1, after=_s47, type='threshold', rung='threshold', force='threshold', forceFrom='4.7', level='fheq:6', award=HON,
  appliesTo='students on PSRB-accredited courses', addressee='learner', verbs=['demonstrated', 'assessed'], domain='subject-skill',
  about='professional competence met',
  para="To succeed, the student has shown professional competence when judged against what a professional, statutory or regulatory body asks for.",
  prac="On a PSRB-accredited course, record a pass on this row only where the student has been assessed against the body's requirements and met them.",
  ben="To succeed on a professionally accredited route, you need to have shown your professional competence when it is judged against the professional body's requirements.",
  q="Which professional body assesses your competence, and how will you be judged against its requirements?")
s('4.7.b2', find=_p2, after=_s47, type='threshold', rung='threshold', force='threshold', forceFrom='4.7', level='fheq:6', award=HON,
  appliesTo='students on PSRB-accredited courses', addressee='learner', verbs=['adhered', 'set'], domain='subject-skill',
  about='keeping to regulators\' and industry rules',
  para="To succeed, the student has kept to the rules or conventions that regulators or the industry lay down.",
  prac="On a PSRB-accredited course, check that the student has kept to the rules and conventions regulators or the sector set, and record failure to do so as not successful.",
  ben="To succeed on a professionally accredited route, you need to have kept to the rules and conventions that regulators or the sector set.",
  q="Which rules or conventions from regulators or the sector apply to your practice, and how do you show you keep them?")

# =============================================================== section 4: the standards table (after 4.5)
_ROWS = ['Knowledge', 'Critical awareness', 'Critical evaluation', 'Application', 'Ethical awareness', 'Evaluate own learning skills',
         'Study skills', 'Creativity', 'Planning for collaboration', 'Solution focus', 'Information retrieval and application',
         'Communication and presentation', 'Application of theory', 'Use of digital technologies, including AI',
         'Analytical and creative competence', 'Collaboration', 'Data access skills (analogue and digital)', 'Hybrid literacies',
         'Personal competences', 'Transformative competences']
_ta = _NORM.index('Threshold level Subject-specific'); _tb = _NORM.index('4.6 Professional competences')
_st = [_ta + m.start() for m in _re.finditer(r'(The|A) student (can|consistently|shows)', _NORM[_ta:_tb])]
_st = [p for p in _st if p not in (_NORM.index('The student can evaluate their own strengths'), _NORM.index('The student can demonstrate improvement resulting'))]
assert len(_st) == 80
_CELLS = []
for _k, _p in enumerate(_st):
    _e = _st[_k + 1] if _k + 1 < len(_st) else _tb
    _t = _NORM[_p:_e]
    _m = _re.search(r'\n\n(?=[A-Z0-9])', _t)
    if _m:
        _t = _t[:_m.start()]
    _t = _t.rstrip()
    _nx = _ROWS[(_k + 1) // 4] if (_k + 1) % 4 == 0 and _k + 1 < 80 else None
    if _nx and _t.endswith(' ' + _nx):
        _t = _t[:-len(_nx) - 1].rstrip()
    _CELLS.append((_t, _p))

COLS = ['threshold', 'typical', 'excellent', 'masters']
COLNAME = {'threshold': 'Threshold standard', 'typical': 'Typical standard', 'excellent': 'Excellent standard', 'masters': "Postgraduate master's"}
PLEAD = {'threshold': 'As the minimum for an honours degree in Education Studies, the student can',
         'typical': 'At the typical level of honours performance, the student can',
         'excellent': 'At the excellent level of honours performance, the student can',
         'masters': "For a master's degree in Education Studies, the student can"}
PRAC = {'threshold': 'Check that every student awarded honours can',
        'typical': 'Plan for students working at the typical honours level to be able to',
        'excellent': 'Recognise excellent honours work where students can',
        'masters': "On a master's course, plan for students to be able to"}
BLEAD = {'threshold': 'To meet the minimum for your honours degree, you can',
         'typical': 'At the typical level for an honours degree, you can',
         'excellent': 'At the excellent level for an honours degree, you can',
         'masters': "For a master's degree, you can"}
# rows: (domain, about, fheq6, fheq7, annex row, strand, q honours, q master's, [(verbs, core) x 4])
_TROWS = [
 ('knowledge', 'theories, concepts and ideas about education', '4.15.b1', '4.17.b1', 'knowledge/r2', 'strand:knowledge',
  "Which theory of education could you explain to a friend, and where would it struggle?",
  "Which ideas at the leading edge of education research shape your own work?",
  [(['demonstrate'], "show a coherent grasp of the major theories, concepts and ideas about education, taken in its broadest sense"),
   (['demonstrate'], "show a sound grasp of the major theories, concepts and ideas about education, taken in its broadest sense"),
   (['demonstrate'], "show a deep grasp of the major theories, concepts and ideas about education, taken in its broadest sense, drawing on the leading edge of the field"),
   (['demonstrate'], "show a systematic grasp of the major theories, concepts and ideas about education, taken in its broadest sense, much of it from the leading edge of the field")]),
 ('understanding', 'the uncertainty and limits of knowledge in education', '4.15.b4', '4.17.b1', 'knowledge/r2', 'strand:thinking',
  "Where does what we know about education run out, or rest on shaky ground?",
  "Which claim at the forefront of your field would you challenge, and on what grounds?",
  [(['demonstrate'], "show a coherent grasp of where knowledge and theory in education are uncertain, ambiguous or limited"),
   (['demonstrate'], "show a sound grasp of where knowledge and theory in education are uncertain, ambiguous or limited"),
   (['demonstrate'], "show a deep grasp of where knowledge and theory in education are uncertain, ambiguous or limited"),
   (['evaluate'], "judge critically the knowledge and theory at the leading edge of the field")]),
 ('subject-skill', 'critical questions and arguments about education', '4.15.b7', '4.17.b4.1', 'cognitive/r2', 'strand:thinking',
  "What is the strongest counter-argument to the case you made in your last essay?",
  "What new insight did bringing two bodies of evidence together give you?",
  [(['identify'], "pick out critical questions about education by drawing on knowledge and evidence"),
   (['devise'], "build critical arguments about education that draw in detail on several bodies of knowledge and evidence"),
   (['devise', 'sustain'], "build and keep up critical arguments about education that draw on several bodies of knowledge and evidence in complex ways"),
   (['synthesize'], "bring complex knowledge and evidence together to reach new insights")]),
 ('subject-skill', 'applying theory to real problems in education', '4.15.b3.1', '4.17.b3', 'cognitive/r3', 'strand:application',
  "Which real problem in education have you explained with a theory, and did the theory fit?",
  "Where have you applied a theory in a way others had not tried?",
  [(['apply'], "use major theories, concepts and ideas on real problems in education"),
   (['apply'], "use major theories, concepts and ideas on real problems in education, in detail"),
   (['apply'], "use major theories, concepts and ideas on real problems in education, in complex ways"),
   (['demonstrate'], "show originality in using major theories and ideas on complex real problems in education")]),
 ('understanding', 'ethical tensions in education', '4.15.b4', '4.17.b5', 'knowledge/r2', 'strand:thinking',
  "Which ethical dilemma in education do you find hardest to resolve, and why?",
  "How would you resolve an ethical dilemma you met in your own research or practice?",
  [(['demonstrate'], "show a coherent grasp of the ethical dilemmas, tensions and challenges in education"),
   (['demonstrate'], "show a sound grasp of the ethical dilemmas, tensions and challenges in education"),
   (['demonstrate'], "show a deep grasp of the ethical dilemmas, tensions and challenges in education"),
   (['demonstrate'], "show originality in analysing and resolving ethical dilemmas, tensions and challenges in education")]),
 ('subject-skill', 'evaluating own learning skills', '4.15.b5', '4.17.b8.3', 'transferable/r5', 'strand:autonomy',
  "What is one strength and one weakness in how you learn, and what will you do about the weakness?",
  "How do you decide what to learn next, without anyone setting it for you?",
  [(['recognise', 'assess', 'reflect'], "accept the value of weighing up their own skills and reflecting on them to guide later learning"),
   (['take', 'reflect', 'evaluate'], "take control of their own learning, reflecting on and judging their personal strengths and weaknesses to guide later learning"),
   (['taking', 'reflect'], "take control of their own learning with sophistication, reflecting on their strengths and weaknesses to guide later learning"),
   (['leading', 'evaluating'], "lead their own learning with sophistication, judging their strengths and weaknesses reflexively to guide later learning")]),
 ('subject-skill', 'methods for systematic study and research', '4.15.b2', '4.17.b2', 'knowledge/r3', 'strand:application',
  "Which research method could you use well today, and which would you need to learn?",
  "How would you defend your choice of method to a sceptical examiner?",
  [(['demonstrate', 'apply'], "know and use the methods that systematic study and research in education call for"),
   (['demonstrate', 'apply', 'evaluate'], "know and use, with a sound working grasp, the methods for systematic study and research in education, and judge their own strengths and weaknesses"),
   (['demonstrate', 'apply'], "know and use, with a deep working grasp, the methods for systematic study and research in education, and show that judging their own skills has improved them"),
   (['demonstrate', 'apply'], "judge in a critically reflexive way, and use, the methods for systematic study, research and application in education")]),
 ('subject-skill', 'creative approaches to studying education', '4.15.b6', '4.17.b6', 'cognitive/r4', 'strand:thinking',
  "Where have you taken a creative approach in your studies, and did it work?",
  "What is original about the approach you took in your recent work?",
  [(['demonstrate'], "take creative approaches to studying education"),
   (['demonstrate'], "take creative approaches to studying education, and to good effect"),
   (['demonstrate'], "take highly creative approaches to studying education"),
   (['demonstrate'], "take highly creative and original approaches to studying education")]),
 ('subject-skill', 'planning and carrying out collaborations', '4.15.b9.1', '4.17.b8.1', 'transferable/r2', 'strand:autonomy',
  "Who have you collaborated with on your course, and what did you plan together?",
  "Which partner outside your organisation have you worked with, and what made it work?",
  [(['demonstrate', 'plan', 'implement'], "plan and carry out suitable collaborations with fellow students, staff and wider stakeholders"),
   (['demonstrate', 'plan', 'implement'], "show a well-developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders"),
   (['demonstrate', 'plan', 'implement'], "show a highly developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders"),
   (['demonstrate', 'plan', 'implement'], "show an excellent ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders, within and beyond an organisation")]),
 ('subject-skill', 'identifying challenges and resolving them', '4.15.b7', '4.17.b5', 'cognitive/r3', 'strand:application',
  "Which challenge have you spotted on placement or in a project, and what did you suggest?",
  "What original way of resolving a problem have you proposed and tested?",
  [(['identify', 'resolve'], "spot challenges and find suitable ways to resolve them"),
   (['identify', 'suggest', 'apply', 'resolve'], "spot challenges, then propose and use suitable ways to resolve them"),
   (['identify', 'suggest', 'lead', 'resolve'], "spot challenges, then propose suitable ways to resolve them and lead their use"),
   (['demonstrate', 'suggest', 'apply', 'resolve'], "understand challenges deeply and propose and use original ways to resolve them")]),
 ('subject-skill', 'finding and using information', '4.15.b5', '4.17.b2', 'cognitive/r1', 'strand:knowledge',
  "How did you find the sources for your last assignment, and how did you judge them?",
  "Which advanced search technique has changed what you find?",
  [(['demonstrate', 'search', 'identify', 'use'], "search for, find and use a range of information, whether written, numerical, visual, spoken or non-verbal, from digital, analogue and empirical sources"),
   (['demonstrates', 'search', 'identify', 'use'], "consistently search critically for, find and use such a range of information from digital, analogue and empirical sources"),
   (['demonstrates', 'search', 'identify', 'use'], "consistently and with insight search critically for, find and use such a range of information from digital, analogue and empirical sources"),
   (['use', 'identify'], "apply advanced search techniques to locate a broad spread of information sources, of every kind, and use them critically and with insight")]),
 ('subject-skill', 'communicating and presenting', '4.15.b8', '4.17.b5', 'transferable/r1', 'strand:communication',
  "How do you choose the right words and format for a given audience?",
  "Why did you choose the form you used to present your last piece of work?",
  [(['organise', 'articulate'], "set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms"),
   (['organise', 'articulate'], "set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms consistently"),
   (['organise', 'articulate'], "set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms with sophistication"),
   (['organise', 'articulate', 'justify'], "set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms with sophisticated use of specialist terms, and justify critically why those forms were chosen")]),
 ('subject-skill', 'theoretical positions and educational practice', '4.15.b3.1', '4.17.b3', 'cognitive/r2', 'strand:application',
  "How might one theory you have studied change what happens in a classroom?",
  "What is original in your view of how theory should shape practice?",
  [(['present', 'demonstrate'], "set out a range of theoretical positions and show how each might bear on educational practice"),
   (['present', 'offer', 'justify'], "set out a wide range of theoretical positions and make and justify a well-informed case for how each might bear on educational practice"),
   (['present', 'offer', 'justify'], "set out a wide range of theoretical positions and make and justify a critically well-informed case for how each might bear on educational practice"),
   (['demonstrate', 'articulate', 'justify'], "show accurate and detailed knowledge of many theoretical positions and argue for and justify a critical, insightful and well-informed view that has some originality")]),
 ('subject-skill', 'digital technologies, including AI, in study', '4.15.b2', '4.17.b7', 'transferable/r1', 'strand:application',
  "Which digital tool, AI included, has improved how you study, and where did you draw the line?",
  "How do digital tools, AI included, support your critical and reflective study?",
  [(['use', 'enhance'], "use digital technologies well and ethically to strengthen a range of approaches to studying education"),
   (['demonstrate', 'enhance'], "use digital technologies with confidence, ethically and well, to strengthen in a systematic way a range of approaches to studying education"),
   (['demonstrate', 'enhance'], "use digital technologies in a sophisticated, ethical, critically informed and effective way to strengthen a range of approaches to studying education"),
   (['demonstrate', 'enhance'], "use digital technologies in a sophisticated, ethical, self-directed and critically informed way to strengthen critical and reflective study")]),
 ('generic-skill', 'building and justifying a position', '4.15.b7', '4.17.b5', 'cognitive/r2', 'strand:thinking',
  "What position have you argued for, and which perspectives did you draw on?",
  "Which new synthesis of sources did your last argument produce?",
  [(['demonstrate', 'process', 'organise', 'articulate'], "show how to process, order and express opinions and arguments so as to build, present and defend a chosen stance that draws on relevant perspectives"),
   (['demonstrate', 'process', 'synthesise', 'organise', 'articulate'], "show a sound grasp of how to process, synthesise, order and express opinions and arguments, drawing on varied sources, to argue for and defend a chosen stance grounded in theory"),
   (['demonstrate', 'process', 'synthesise', 'organise', 'articulate'], "show a deep grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance"),
   (['demonstrate', 'process', 'synthesise', 'organise', 'articulate'], "show a critical grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance")]),
 ('generic-skill', 'communicating and working in a team', '4.15.b9.1', '4.17.b8.1', 'transferable/r2', 'strand:communication',
  "What role did you take in your last team, and how did you build trust?",
  "How have you helped a diverse team to trust one another and deliver?",
  [(['demonstrate', 'communicate', 'plan'], "show how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities"),
   (['demonstrate', 'communicate', 'plan'], "show a sound grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities"),
   (['demonstrate', 'communicate', 'plan'], "show a deep grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities"),
   (['demonstrate', 'communicate', 'plan'], "show a critical grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities")]),
 ('generic-skill', 'accessing information safely and ethically', '4.15.b5', '4.17.b2', 'practical/r4', 'strand:knowledge',
  "How do you check that an online source is trustworthy, and how do you keep yourself safe online?",
  "How do you judge the reliability of the information systems your work depends on?",
  [(['demonstrate', 'access', 'use'], "show how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online"),
   (['demonstrate', 'access', 'use'], "show a sound grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online"),
   (['demonstrate', 'access', 'use'], "show a deep grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online"),
   (['demonstrate', 'access', 'use'], "show a systematic grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online")]),
 ('generic-skill', 'working with data across formats', '4.15.b8', '4.17.b5', 'practical/r4', 'strand:communication',
  "How did you present the data in your last project, and why that format?",
  "How do you make complex data clear and ethical for a given audience?",
  [(['demonstrate', 'collect', 'analyse', 'interpret', 'apply', 'present'], "show how to gather data, then analyse, interpret, apply and present it in varied verbal and non-verbal forms, suited to the task and audience and handled ethically"),
   (['demonstrate', 'analyse', 'interpret', 'apply', 'present'], "show a sound grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically"),
   (['demonstrate', 'analyse', 'interpret', 'apply', 'present'], "show a deep grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically"),
   (['demonstrate', 'analyse', 'interpret', 'apply', 'present'], "show a critical grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically")]),
 ('generic-skill', 'flexibility, self-reflection and lifelong learning', '4.15.b9.3', '4.17.b8.3', 'transferable/r3', 'strand:autonomy',
  "When did you have to adapt quickly, and what did you learn about yourself?",
  "How do you keep learning and reflecting in your professional life?",
  [(['demonstrate', 'engage'], "show flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter"),
   (['demonstrate', 'engage'], "show a sound grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter"),
   (['demonstrate', 'engage'], "show a deep grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter"),
   (['demonstrate', 'engage'], "show a systematic grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter")]),
 ('generic-skill', 'taking part in change; futures thinking', '4.15.b9.2', '4.17.b8.2', 'transferable/r4', 'strand:autonomy',
  "What change in education have you been part of, and what tensions did it raise?",
  "How would you use futures thinking to plan a change in your setting?",
  [(['demonstrate', 'anticipate', 'reconcile', 'understand'], "show engagement in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means"),
   (['demonstrate', 'engage', 'anticipate', 'reconcile', 'understand'], "show a sound grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means"),
   (['demonstrate', 'engage', 'anticipate', 'reconcile', 'understand'], "show a deep grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means"),
   (['demonstrate', 'engage', 'anticipate', 'reconcile', 'understand'], "show a systematic grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means")])]
assert len(_TROWS) == 20

def _cid(r, col):
    return '4.5.b%d' % r + ('' if col == 'threshold' else '.' + col)
GRADE = {}
ROW = {}
for _r, (_dom, _about, _f6, _f7, _ax, _strand, _qh, _qm, _cl) in enumerate(_TROWS, 1):
    for _c, _col in enumerate(COLS):
        _txt, _pos = _CELLS[(_r - 1) * 4 + _c]
        _v, _core = _cl[_c]
        _i = _cid(_r, _col)
        ROW[_i] = (_r, _col)
        _mas = _col == 'masters'
        s(_i, find=_txt, after=_pos, type='threshold' if _col in ('threshold', 'masters') else _col,
          rung='threshold' if _col in ('threshold', 'masters') else _col,
          force='threshold' if _col == 'threshold' else 'will', forceFrom='4.3',
          level='fheq:7' if _mas else 'fheq:6', award=MAS if _mas else HON,
          appliesTo=("students completing a master's degree in Education Studies" if _mas else 'honours students at the %s standard' % _col),
          addressee='learner', verbs=_v, domain=_dom, about=_about,
          para='%s %s.' % (PLEAD[_col], _core),
          prac='%s %s%s.' % (PRAC[_col], _core, ', treating the column as a guide, as 4.4 asks' if _mas else ''),
          ben='%s %s.' % (BLEAD[_col], _you(_core)),
          q=_qm if _mas else _qh)
    GRADE[_cid(_r, 'typical')] = _cid(_r, 'threshold') + '|stated'
    GRADE[_cid(_r, 'excellent')] = _cid(_r, 'typical') + '|stated'

# =============================================================== the two agent instructions
LEVELS = {'fheq:6': 'FHEQ Level 6 (FQHEIS Level 10, spine:6)', 'fheq:7': 'FHEQ Level 7 (FQHEIS Level 11, spine:7)'}
FW = {('fheq:6', 'knowledge'): 'qaa/fheq-2024/4.15.b1', ('fheq:6', 'understanding'): 'qaa/fheq-2024/4.15.b4 and 4.15.b7',
      ('fheq:6', 'subject-skill'): 'qaa/fheq-2024/4.15.b3.1', ('fheq:6', 'generic-skill'): 'qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3',
      ('fheq:6', 'none'): 'qaa/fheq-2024/4.15.b1 and 4.15.b9.3'}
FORCEW = {'should': 'an expectation worded with "should"', 'must': 'a requirement worded with "must"', 'will': 'an expected outcome or feature worded with "will" or "can"',
          'threshold': 'a minimum condition', 'describes': 'a statement without one of the five obliging words (force recorded as describes)'}
BAND = {'threshold': '3rd', 'typical': '2.2', 'excellent': '1st'}

def _order(i):
    base, _, b = i.partition('.b')
    try:
        return tuple(int(x) for x in base.split('.')) + ((int(b),) if b else (0,))
    except ValueError:
        return (9999, i)
_IDS = sorted(P, key=_order)

def _loc(i):
    if i in ROW:
        r, col = ROW[i]
        return 'section 4, the standards table after para 4.5, row "%s", %s column' % (_ROWS[r - 1], COLNAME[col])
    if i.startswith('3.10.b'):
        return 'para 3.10, bullet %s' % i.split('.b')[1]
    if i.startswith('4.7.b'):
        return 'para 4.7, the professional competences table, "Successful" column'
    return 'para ' + i

def _awd(r):
    aw = r['award']
    if isinstance(aw, list):
        return ' and '.join({HON: "the honours degree", MAS: "the master's degree", INT: "the integrated master's"}[a] for a in aw)
    return {'none': 'any Education Studies course the statement covers', HON: 'the honours degree', MAS: "the master's degree"}.get(aw, 'the ' + aw)

def _nb(i):
    plain = [x for x in _IDS if x not in ROW and not x.startswith('4.7.b')]
    if i not in plain:
        return "the statement's section " + i.split('.')[0]
    k = plain.index(i); sec = i.split('.')[0]
    near = [x for x in (plain[k - 1] if k else None, plain[k + 1] if k + 1 < len(plain) else None) if x and x.split('.')[0] == sec]
    return ' and '.join(SID + x for x in near) or "the statement's section %s" % sec

for _i in _IDS:
    r = P[_i]
    q = r.pop('q', 'Where does the course show this, and what evidence would you point to?')
    cite = CITE % _loc(_i)
    lv = LEVELS.get(r['level'], 'the level of the award it applies to')
    if _i in ROW:
        rn, col = ROW[_i]
        _dom, _about, _f6, _f7, _ax, _strand = _TROWS[rn - 1][:6]
        if col == 'masters':
            r['aaw'] = (f"Write about this as the master's standard for {_about} at {lv}, the postgraduate column the statement asks institutions to treat as a guide (4.4). "
                        f"Cite it as {cite}. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. "
                        f"Set it beside {SID}{_cid(rn, 'excellent')}, the honours cell it reaches past, and the descriptor qaa/fheq-2024/{_f7} at spine:7 ({_strand}).")
            r['aad'] = (f"Raise it when a master's student or course team asks what is expected for {_about}. "
                        f"Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. "
                        f"Ask: {q} Do not read the cell aloud at length or use an honours column for a master's student.")
        else:
            below = GRADE.get(_i, '').split('|')[0]
            above = next((x for x, y in GRADE.items() if y.split('|')[0] == _i), None)
            pair = ' and '.join(SID + x for x in (below, above) if x)
            what = {'threshold': 'the threshold, the least every honours graduate shows', 'typical': 'the typical standard, above the threshold',
                    'excellent': 'the excellent standard, the top of the honours range'}[col]
            band = (f"the Annex D band qaa/fheq-2024/annex-d/{_ax}/3rd (the threshold class)" if col == 'threshold'
                    else f"the Annex D row qaa/fheq-2024/annex-d/{_ax} (the statement ties no class to this column)")
            r['aaw'] = (f"Write about this as {what} for {_about}, in an honours degree in Education Studies at {lv}. "
                        f"Cite it as {cite}. Do not present it as a regulatory requirement or a mark scheme{', or as the minimum to pass' if col != 'threshold' else ''}, and do not apply it to master's awards. "
                        f"Set it beside {pair}, {band} and the descriptor qaa/fheq-2024/{_f6} at spine:6 ({_strand}).")
            avoid = ('Make clear that this is the floor every honours graduate reaches, not the target.' if col == 'threshold'
                     else 'Never present this column as what is needed simply to pass.')
            r['aad'] = (f"Raise it when a student asks what {col} work looks like for {_about}, or when markers compare work across the columns. "
                        f"Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. "
                        f"Ask: {q} {avoid}")
        continue
    if _i.startswith('4.7.b'):
        r['aaw'] = (f"Write about this as a pass condition on a professionally accredited honours route at {lv}: {r['about']}. "
                    f"Cite it as {cite}. Do not apply it to courses without PSRB accreditation or present it as an academic grade. "
                    f"Set it beside {SID}4.7, {SID}4.7.b1 and {SID}4.7.b2 together, and the Annex D row qaa/fheq-2024/annex-d/professional/r{_i[-1]}/3rd-1st it reproduces.")
        r['aad'] = (f"Raise it only with a student or team on a professionally accredited route, when they ask what the professional body needs. "
                    f"Put it plainly as pass or not, separate from the academic standards. Ask: {q} "
                    f"Do not suggest it applies to every Education Studies student.")
        continue
    fw = FW.get((r['level'], r['domain']), 'the honours and master\'s descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7')
    if r['addressee'] == 'provider':
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} on the course and its team, on {r['about']}, holding for {_awd(r)}. "
                    f"Cite it as {cite}. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. "
                    f"Set it beside {_nb(_i)}, and where it shapes outcomes beside {fw}.")
        r['aad'] = (f"Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to {r['about']}. "
                    f"Frame it for staff as {FORCEW[r['force']]}, and ask: {q} "
                    f"Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve.")
    else:
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} for {_awd(r)}, at {lv}, on {r['about']}. "
                    f"Cite it as {cite}. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. "
                    f"Set it beside {_nb(_i)} and the framework descriptor {fw}.")
        r['aad'] = (f"Bring it up when a student asks about {r['about']}, or when staff check a module or outcome against it. "
                    f"Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as {FORCEW[r['force']]}. "
                    f"Ask: {q} Avoid long quotation of the issuer's text.")

# =============================================================== front matter and sections
META = dict(
    run='0103', p1='2026-10-03 17:11',
    title='Subject Benchmark Statement Education Studies', heading='Subject Benchmark Statement: Education Studies (QAA, April 2025)',
    edition='April 2025 (fifth edition)', published='2025-04',
    status='current', supersedes='the Education Studies statement of 2019 (a minor update of the 2015 edition; earlier editions 2007 and 2000; dates from the advisory group lists, back matter)',
    subjects=[dict(scheme='hecos', code='100459', label='education studies', basis='stated'),
              dict(scheme='cah', code='CAH22-01-01', label='education', basis='stated'),
              dict(scheme='cah', code='CAH22-01-02', label='teacher training', basis='inferred'),
              dict(scheme='hecos', code='101246', label='professional practice in education', basis='inferred')],
    awards=[HON, MAS, INT], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (published 10 April 2025)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what an Education Studies graduate should know, understand and be able to do, at honours and at master's level. "
                     "Reach for it when designing, approving, reviewing or describing an Education Studies course, its outcomes or its assessment. "
                     "Its standards are one table of twenty rows in three groups (subject-specific, practical and practice-based, transversal), each row at four columns: "
                     "threshold, typical and excellent for honours, and a postgraduate master's column the statement asks institutions to treat as a guide. "
                     "It is not a regulatory requirement, not a teacher training standard and not a mark scheme."),
    summary=("Published by QAA on 10 April 2025, the statement covers Education Studies as a subject, field or discipline concerned with how people learn across life, "
             "the nature of knowledge and the contexts of education, at honours and master's level. It sets five cross-cutting themes (equity, diversity and inclusion; "
             "accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; "
             "artificial intelligence), distinctive features of progression, flexibility, partnership and review, three curricula (subject-specific, practice-based and "
             "transversal) and its standards as one table at threshold, typical, excellent and master's, with a pass-or-not row for professional competence on "
             "PSRB-accredited routes. It names PSRBs, the Office for Students and the Equality and Human Rights Commission, and points to Annex D of the FHEQ."),
    authority='reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of quality arrangements in Scotland, Wales and Northern Ireland (D1, Relationship to legislation)')

S2 = dict(
    governs="what can be expected of a graduate in Education Studies at honours and master's level, and the nature of awards in the subject (D1, front matter; 4.1)",
    awards=["bachelor's degrees with honours, including joint and combined degrees and professionally focused courses (2.4, 4.1, 4.2)", MAS, "integrated master's (2.2)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining (front matter, 2.12); PSRBs (front matter); prospective students and employers (front matter)'],
    doesNot="it does not prescribe teaching, learning or assessment, interpret legislation or carry statutory or regulatory requirements; its standards are not universal competence standards (D1, front matter; 4.5)",
    statedScope='"This QAA Subject Benchmark Statement for Education Studies defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies." (D1, front matter); "The following benchmark standards are defined for students studying a single honours or master\'s degree in Education Studies." (D1, 4.1)',
    statedSubjects=[
        dict(name='Education Studies', locator='(D1, title; 1.1; 4.1)', kind='subject', codes=[dict(scheme='hecos', code='100459', label='education studies'), dict(scheme='cah', code='CAH22-01-01', label='education')]),
        dict(name='allied areas including teacher training', locator='(D1, front matter)', kind='subject', codes=[dict(scheme='cah', code='CAH22-01-02', label='teacher training')]),
        dict(name='teaching studies; programmes that offer qualified teacher status', locator='(D1, 3.3; 3.7)', kind='programme title', codes=[dict(scheme='hecos', code='101246', label='professional practice in education')]),
        dict(name='mathematics education, inclusive education, lifelong learning', locator='(D1, 4.2)', kind='specialism', codes=[])])

SECTIONS = {'1': 'Context and purposes of an Education Studies degree', '2': 'Distinctive features of the Education Studies course',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context and purposes of an Education Studies degree'), ('1.2', '1.6', 'Purposes and characteristics of an Education Studies degree'),
       ('1.7', '1.14', 'Equity, diversity and inclusion'), ('1.15', '1.24', 'Accessibility and the needs of disabled students'),
       ('1.25', '1.31', 'Education for sustainable development'), ('1.32', '1.40', 'Employability, entrepreneurship and enterprise education'),
       ('1.41', '1.43', 'Artificial intelligence'), ('2.1', '2.1', 'Distinctive features of the Education Studies course'), ('2.2', '2.5', 'Progression'),
       ('2.6', '2.7', 'Flexibility'), ('2.8', '2.8', 'Partnership'), ('2.9', '2.12', 'Monitoring and review'), ('3.1', '3.1', 'Content, structure and delivery'),
       ('3.2', '3.4', 'Content'), ('3.5', '3.6', 'Subject-specific curriculum'), ('3.7', '3.8', 'Practice-based curriculum'), ('3.9', '3.10', 'Transversal curriculum'),
       ('3.11', '3.15', 'Teaching and learning'), ('3.16', '3.24', 'Assessment'), ('4.1', '4.5', 'Introduction'), ('4.6', '4.7', 'Threshold level')]

G = {
 '1.1': 'what the subject studies; its contexts', '1.2': 'transformative purpose; praxis', '1.3': 'subject, field or discipline',
 '1.4': 'ethics throughout; a changing subject', '1.5': 'diverse perspectives; reciprocal learning', '1.6': 'debate, critical capability and careers',
 '1.7': 'EDI vision', '1.8': 'co-constructing equitable curricula', '1.9': 'questioning dominant language and knowledge', '1.10': 'learning across the lifespan',
 '1.11': 'EDI and a just society', '1.12': 'unique contributions; ideologies and communities', '1.13': 'agency, reflection, respect',
 '1.14': 'digital technologies and AI through an EDI lens', '1.15': 'Equality Act duty to anticipate', '1.16': 'open to all; accessibility a must',
 '1.17': 'design fits mode of delivery', '1.18': 'non-standard routes; equal access', '1.19': 'professional advice and student voice',
 '1.20': 'accessible curriculum; clear assessment', '1.21': 'anticipating barriers', '1.22': 'anticipatory reasonable adjustments',
 '1.23': 'access in person and online', '1.24': 'accessible placements', '1.25': 'ESD vision', '1.26': 'UN SDGs and ESD guidance',
 '1.27': 'competences for sustainable practice', '1.28': 'interdisciplinary basis of sustainability', '1.29': 'complexities of sustainability',
 '1.30': 'education for a sustainable future', '1.31': 'personal sustainability and well-being', '1.32': 'employability and enterprise vision',
 '1.33': 'entrepreneurship beyond employment', '1.34': 'qualities the subject fosters', '1.35': 'education in its widest sense',
 '1.36': 'graduate destinations', '1.37': 'enterprise embedded, not added', '1.38': 'innovation and adaptability', '1.39': 'ethical entrepreneurial disposition',
 '1.40': 'four aims of the subject', '1.41': 'AI vision', '1.42': 'eleven principles for understanding AI', '1.43': 'course teams and the AI principles',
 '2.1': 'eleven common features of courses', '2.2': 'progression through levels', '2.3': 'readiness for postgraduate study', '2.4': 'joint and combined degrees',
 '2.5': 'exit awards', '2.6': 'course length by nation; part-time', '2.7': 'modes, formats and credit', '2.8': 'partnership delivery',
 '2.9': 'periodic review; student voice', '2.10': 'externality', '2.11': 'professional accreditation', '2.12': 'external examining',
 '3.1': 'how content shapes teaching and assessment', '3.2': 'skills for study and employment', '3.3': 'three curricular areas; Figure 1',
 '3.4': 'fluid boundaries between the areas', '3.5': 'programmes choose their focus', '3.6': 'twenty subject-specific knowledge areas',
 '3.7': 'placements and practice', '3.8': 'fourteen practice-based opportunities', '3.9': 'transversal knowledge and skills',
 '3.10': 'twenty-three transversal areas', '3.11': 'inclusive, interactive, reflective teaching', '3.12': 'seven ways courses support success',
 '3.13': 'modelling effective practice', '3.14': 'alignment with professional bodies', '3.15': 'contemporary issues and the themes',
 '3.16': 'assessment aligned to outcomes', '3.17': 'twenty-three assessment methods', '3.18': 'academic integrity and AI',
 '3.19': 'accessible, inclusive assessment', '3.20': 'staff workload and sustainable courses', '3.21': 'authentic assessment',
 '3.22': 'assessed placements', '3.23': 'a varied assessment diet', '3.24': 'forward-facing feedback',
 '4.1': 'who the standards are for', '4.2': 'professional training contexts', '4.3': 'threshold, typical and excellent defined; Annex D',
 '4.4': "master's standards as a guide", '4.5': 'not competence standards; the standards table follows', '4.6': 'professional competences row',
 '4.7': 'professional competence for accredited awards; back matter follows'}
CTYPE = {'3.6': 'area', '3.8': 'area', '3.10': 'area', '3.3': 'area', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice',
         '3.17': 'practice', '3.18': 'practice', '3.19': 'practice', '3.21': 'practice', '3.22': 'practice', '3.24': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='none', heading='Figure 1: The knowledge areas of education studies', kind='other: figure labels held inside 3.3, read for SB3'),
    dict(number='none', heading='Membership of the Advisory Group', kind="other: back matter held inside the skeleton's 4.7 span, read for S7 and S8 (editions 2019 minor update, 2015, 2007, 2000)")]

TH = {}
for _i in ('1.9', '1.11', '1.13'): TH[_i] = 'theme:edi'
for _i in ('1.15', '1.16', '1.20', '1.21', '1.22', '1.23', '1.24'): TH[_i] = 'theme:accessibility'
for _i in ('1.30', '1.31'): TH[_i] = 'theme:esd'
TH['1.43'] = 'theme:generative-ai'

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.2 (honours); the honours columns of the table (4.3)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.2'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.2 (integrated master's); 4.4 (Level 7, framework not named)"),
                  dict(id='fqheis:11', role='cites', locator="D1, 2.2; 4.4 (Level 11 in Scotland)"),
                  dict(id='fheq:4', role='cites', locator='D1, 2.5 (CertHE exit award)'),
                  dict(id='fqheis:8', role='cites', locator='D1, 2.5 (given for the CertHE; Part E)'),
                  dict(id='fheq:5', role='cites', locator='D1, 2.5 (DipHE exit award)'),
                  dict(id='fqheis:9', role='cites', locator='D1, 2.5 (given for the DipHE; Part E)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.2: honours at FHEQ Level 6, FQHEIS Level 10)"),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.2: integrated master's at FHEQ Level 7, FQHEIS Level 11; 4.4: Level 7 and Level 11)"),
                      dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.5, CertHE); the FHEQ document\'s Table 1 gives the CertHE at fqheis:7 (Part E)'),
                      dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.5, DipHE); the FHEQ document\'s Table 1 gives the DipHE at fqheis:8 (Part E)'),
                      dict(**{'from': 'threshold column'}, to='Annex D 3rd (threshold)', relation='thresholdAt', basis='inferred: 4.3 sends institutions to Annex D for evidence; the statement ties no class to typical or excellent')])

_EDI_C = ['front matter', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.13', '1.14', '1.20', '3.10', '3.12', '3.15', '3.19']
_ACC_C = ['front matter', '1.7', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.42', '3.10', '3.12', '3.19', '4.5']
_ESD_C = ['front matter', '1.4', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.42', '3.6', '3.15']
_ENT_C = ['front matter', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '2.1', '3.10', '3.12', '3.15']
_AI_C = ['front matter', '1.14', '1.41', '1.42', '1.43', '3.8', '3.10', '3.15', '3.18', 'section 4 table, row "Use of digital technologies, including AI"']
S6 = [dict(id='theme:edi', role='carries', carriedIn=_EDI_C), dict(id='theme:accessibility', role='carries', carriedIn=_ACC_C),
      dict(id='theme:esd', role='carries', carriedIn=_ESD_C), dict(id='theme:enterprise', role='carries', carriedIn=_ENT_C),
      dict(id='theme:generative-ai', role='carries', carriedIn=_AI_C)]

S7 = [dict(rel='supersedes', target='std:doc:qaa-education-studies-2019-benchmarks (not held)', note='the front matter lists key changes from the previous statement; advisory groups are named for 2019 (minor update), 2015, 2007 and 2000 (back matter)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='4.3: institutions should refer to Annex D when deciding what evidence shows the standards are met'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 4 to 7 (2.2, 2.5, 4.4)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 8 to 11 (2.2, 2.5, 4.4)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.26: named as a resource for shaping the offer (the QAA and Advance HE Education for Sustainable Development Guidance)'),
      dict(rel='refersTo', target='QAA Quality Code (2024) (not ingested)', note='front matter'),
      dict(rel='refersTo', target='Equality Act 2010 (law; not a standards document)', note='1.15, 1.22, 4.5'),
      dict(rel='refersTo', target='PSRB requirements (not yet ingested)', note='front matter, 2.8, 2.11, 3.14, 3.17, 3.22, 4.5, 4.7')]
S8 = dict(published='2025-04', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='none-stated; an advisory group and a student focus group are listed (back matter)', replacedBy='none')

SB1 = ['Education Studies studies how people develop and learn across their lives, the nature of knowledge and ways of knowing and educational processes and systems in their cultural, social, technological, political, philosophical, environmental, historical and economic settings, always with critique of policy and practice (D1, 1.1).',
       'It joins theory and scholarly practice (praxis) and aims to change lives and society for the better, preparing students to act as agents of change (D1, 1.2).',
       'It can be read as a subject defined by content, a field drawing on psychology, sociology, philosophy, history, language, politics and economics, or a discipline with its own discourses and methods (D1, 1.3).',
       'Ethics runs through all of it, and it is always changing (D1, 1.4).',
       'Learning is reciprocal: students bring diverse perspectives that feed critical debate (D1, 1.5).',
       'It treats education in its widest sense, well beyond schools, colleges and universities, and its graduates go into many sectors, not only teaching (D1, 1.35, 1.36).',
       'Its curriculum spans three overlapping areas, subject-specific, practice-based and transversal, where transformative learning happens at their meeting point (D1, 3.3, 3.4, Figure 1).']

SB2 = [dict(theme='theme:edi', inThisSubject='EDI as a founding tenet of the field: co-constructed equitable curricula, questioning dominant language and knowledge, defining a position on justice, reflection with respect for others and EDI in the use of digital technologies (D1, 1.7 to 1.14, 3.12)',
            statements=['1.9', '1.11', '1.13', '3.10.b6', '3.10.b12']),
       dict(theme='theme:accessibility', inThisSubject='an inclusive discipline open to all: the Equality Act duty to anticipate, accessibility a must in design, anticipatory adjustments, digital access and assistive technology, accessible placements and competence standards under the Equality Act (D1, 1.15 to 1.24, 3.19, 4.5)',
            statements=['1.15', '1.16', '1.20', '1.21', '1.22', '1.23', '1.24', '3.10.b12', '4.5']),
       dict(theme='theme:esd', inThisSubject="education as a driver of sustainable practice, the UN SDGs (SDG 4 in particular), interdisciplinary knowledge of sustainability and students' personal sustainability and well-being (D1, 1.25 to 1.31, 3.6)",
            statements=['1.30', '1.31']),
       dict(theme='theme:enterprise', inThisSubject='employability, entrepreneurship and enterprise embedded rather than added, for destinations far beyond teaching, with an ethical entrepreneurial disposition (D1, 1.32 to 1.40, 2.1, 3.12)',
            statements=['3.10.b13']),
       dict(theme='theme:generative-ai', inThisSubject='artificial intelligence as its own theme: eleven principles for critical, ethical and transparent use, applied by course teams across the programme, academic integrity in assessment and a standards row on digital technologies including AI (D1, 1.41 to 1.43, 3.18; the standards table)',
            statements=['1.43', '3.10.b22', '4.5.b14', '4.5.b14.typical', '4.5.b14.excellent', '4.5.b14.masters'])]

SB3 = dict(areas=[dict(component='3.3', gloss='three curricular areas: subject-specific, practice-based and transversal, shown in Figure 1'),
                  dict(component='3.6', gloss='twenty subject-specific knowledge areas, from research methods and curriculum design to safeguarding, SEND, social justice and educational technologies'),
                  dict(component='3.8', gloss='fourteen practice-based opportunities: adapting practice, reasonable adjustments, ethics, safeguarding, student voice, technology, reflection, observation'),
                  dict(component='3.10', gloss='twenty-three transversal areas, from numeracy and communication to self-care, AI and collaboration')],
           practices=[dict(component='3.11', kind='teaching', gloss='inclusive, interactive and reflective methods drawing on practice, theory and evidence'),
                      dict(component='3.12', kind='learning', gloss='independent learning, self-assessment, accessibility, support services, employability, inclusive environment, scaffolding'),
                      dict(component='3.13', kind='teaching', gloss='programmes modelling effective teaching practice'),
                      dict(component='3.17', kind='assessment', gloss='twenty-three methods, from posters and podcasts to game-based outputs, portfolios and vivas'),
                      dict(component='3.18', kind='assessment', gloss='academic integrity, especially with GenAI'),
                      dict(component='3.19', kind='assessment', gloss='accessible and inclusive assessment; student well-being'),
                      dict(component='3.21', kind='assessment', gloss='authentic assessment in real-world settings'),
                      dict(component='3.22', kind='assessment', gloss='assessed placements and work-based practice with reflection'),
                      dict(component='3.24', kind='assessment', gloss='formative and summative feedback that looks forward')])

_outs = []
for _r, _t in enumerate(_TROWS, 1):
    _outs.append(dict(outcome=_ROWS[_r - 1] + ': ' + _t[1], threshold=_cid(_r, 'threshold'), typical=_cid(_r, 'typical'),
                      excellent=_cid(_r, 'excellent'), masters=SID + _cid(_r, 'masters'), basis='stated', domain=_t[0], award=HON))
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3', award=HON, items=20, label='Threshold standard'),
           dict(rung='typical', leadIn='4.3', award=HON, items=20, label='Typical standard'),
           dict(rung='excellent', leadIn='4.3', award=HON, items=20, label='Excellent standard'),
           dict(rung='threshold', leadIn='4.4', award=MAS, items=20, label="Postgraduate master's (read as the master's threshold: 4.3, 4.4)"),
           dict(rung='threshold', leadIn='4.7', award=HON, items=2, label='Professional competences, Successful (PSRB-accredited routes only)')],
    rungBases=("4.3: the threshold standards set the minimum every student completing an honours or master's course can show; most perform well above it; the tables also describe "
               "typical and excellent undergraduate performance, and institutions refer to Annex D for evidence. 4.4: the postgraduate column is for a master's at Level 7 "
               "(Level 11 in Scotland), to be used as a guide only. One table after 4.5 lists twenty rows in three groups (Subject-specific skills: Knowledge and understanding, "
               "10 rows; Practical and practice-based skills, 4 rows; Transversal skills: Transferable competences, 6 rows), each across the four columns; the issuer pairs "
               "the cells by row. 4.6 and 4.7 add a pass-or-not row for professional competence that reproduces Annex D's professional rows."),
    outcomeLists=[dict(leadIn='3.10', gloss='twenty-three transversal areas course teams should consider', items=23, award=[HON])],
    outcomes=_outs)
SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs)',
            says='the statement can support their definitions of academic standards; courses may be delivered with them, may need their evaluation and accreditation, may align to their requirements; a PSRB-accredited award is not made without the professional competencies they assess (D1, front matter, 2.8, 2.11, 3.14, 3.17, 3.22, 4.5, 4.7)',
            requirements='not yet ingested (Part E)'),
       dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not-applicable-by-design'),
       dict(body='Equality and Human Rights Commission', says='providers writing competence standards should follow its latest guidance (D1, 4.5)', requirements='not-applicable-by-design: guidance, not course requirements')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, diversity and inclusion (EDI)', carriedIn=_EDI_C, statements=[SID + x for x in SB2[0]['statements']]),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=_ACC_C, statements=[SID + x for x in SB2[1]['statements']]),
            dict(id='theme:esd', named='Education for sustainable development', carriedIn=_ESD_C, statements=[SID + x for x in SB2[2]['statements']]),
            dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education', carriedIn=_ENT_C, statements=[SID + x for x in SB2[3]['statements']]),
            dict(id='theme:generative-ai', named='Artificial intelligence (front matter: generative artificial intelligence)', carriedIn=_AI_C, statements=[SID + x for x in SB2[4]['statements']])],
    frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.2', '2.5', '4.3', '4.4']),
                dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.2', '2.5', '4.4'])],
    bodies=[dict(body='PSRBs (generic)', citedIn=['front matter', '2.8', '2.11', '3.14', '3.17', '3.22', '4.5', '4.7']),
            dict(body='Office for Students', citedIn=['front matter']),
            dict(body='Equality and Human Rights Commission', citedIn=['4.5'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.3', '4.6', '4.7'], role='evidence of achievement against the standards (4.3); the professional competence rows reproduced in 4.6 and 4.7'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE Education for Sustainable Development Guidance', citedIn=['1.26'], role='a resource for the sustainability theme'),
        dict(document='QAA Quality Code 2024 (not ingested)', named='the Quality Code (2024 update)', citedIn=['front matter'], role='sector reference point read with the statement'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='std:doc:qaa-education-studies-2019-benchmarks (not held)', named='the previous Subject Benchmark Statement', citedIn=['front matter'], role='the edition this one revises'),
        dict(document='UN Sustainable Development Goals (external)', named='the current United Nations Sustainable Development Goals (SDG 4 Quality Education)', citedIn=['1.26'], role='frame for the sustainability theme'),
        dict(document='Equality Act 2010 (law)', named='The Equality Act 2010', citedIn=['1.15', '1.22', '4.5'], role='the anticipatory duty, reasonable adjustments and competence standards')])

B1 = [dict(slug='praxis', definition='theory joined with scholarly practice in the study of education (D1, 1.2)', beneficiaryDefinition='putting theory and practice together', scopeNote='the route to varied professional futures', category='unknown', practices=['education']),
      dict(slug='transversal-curriculum', definition='abilities learned for use in almost any work, crossing fields and industries rather than tied to one subject (D1, 3.3, 3.9)', beneficiaryDefinition='skills that carry across jobs and settings', scopeNote='one of three curricular areas with subject-specific and practice-based', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum every student completing an honours or master\'s course can show in each area of the standards table (D1, 4.3)', beneficiaryDefinition='the least you need to show for your degree', scopeNote='typical and excellent describe undergraduate performance above it', category='unknown', practices=['education']),
      dict(slug='artificial-intelligence', definition='technology that produces human-like outputs and responses, including large language models, chatbots and generative AI (D1, 1.41)', beneficiaryDefinition='tools that answer, write or make things in a human-like way', scopeNote='the fifth cross-cutting theme', category='unknown', practices=['education']),
      dict(slug='monitoring-and-evaluation', definition='periodic assessment of a course, internal or external, drawing on current and past monitoring to understand achievement and plan ahead (D1, 2.9)', beneficiaryDefinition='checking how well a course works and improving it', scopeNote='read with externality (2.10)', category='unknown', practices=['education'])]
B2A = [dict(concept='praxis', form='praxis', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
       dict(concept='transversal-curriculum', form='transversal curricula', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='artificial-intelligence', form='Artificial intelligence (AI)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='monitoring-and-evaluation', form='Monitoring and evaluation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []
D3 = [dict(citation="QAA (2019) Subject Benchmark Statement: Education Studies", settles=['S7', 'S8'], asked='2026-10-03', state='wanted: to confirm supersedes')]

E = [
 "SB4, shape: the standards are one untitled, unnumbered table after 4.5, of twenty rows in three groups (Subject-specific skills: Knowledge and understanding, 10; Practical and practice-based skills, 4; Transversal skills: Transferable competences, 6) across four columns: threshold, typical and excellent for honours, and postgraduate master's. Recorded as 80 S4 records, 4.5.b1 to 4.5.b20 for the threshold cells in reading order, with `.typical`, `.excellent` and `.masters` on the same row; the ids follow batch 1's convention and are ours, not the issuer's.",
 "SB4, master's column: recorded as `rung: threshold`, award master's, level fheq:7, read with 4.3 (the threshold standards cover honours and master's) and 4.4 (the postgraduate standards, to be used \"as a guideline only\"). Force recorded as `will` from the cells' \"can\", not `threshold`, since 4.4 softens it. `.masters` is a new id suffix: for a ruling. No gradeOf: there is no master's rung below it; each master's cell reads as going past the excellent honours cell in the same row (inferred, not recorded).",
 "SB4, gradeOf: the issuer pairs the cells by row, so each typical cell names the threshold cell and each excellent cell the typical cell, `basis: stated` (40 links).",
 "S4, force: threshold cells take `threshold` (4.3 defines them as the minimum for all students); typical, excellent and master's cells take `will` from their own \"can\"; every cell carries forceFrom 4.3. The cells headed \"The student consistently demonstrates\" (row 11) and \"The student shows sophistication\" (row 6) have no modal of their own.",
 "S4, domains: rows 1 to 14 sit under the issuer's Subject-specific and Practical headings and are recorded as knowledge, understanding or subject-skill; rows 15 to 20 (Transversal skills) are generic-skill. Rows 6 (Evaluate own learning skills), 9 (Planning for collaboration) and 14 (Use of digital technologies, including AI) read as generic but follow the issuer's grouping: for P3.",
 "S4, held text: the typical cell of row 15 reads \"theory- relevant perspectives\" where the other columns have \"relevant perspectives\"; row 6 excellent has \"reflect\" where \"reflecting\" is meant; row 11's excellent column head is \"Excellent\" without \"standard\" on pages 21 and 22. Kept as held.",
 "S4, 4.6 and 4.7: they reproduce Annex D's professional competence rows (qaa/fheq-2024/annex-d/professional/r1 and r2). 4.7's lead sentence is one record (force will: the accredited award \"will not be made\"); the two Successful cells are 4.7.b1 and 4.7.b2, threshold, PSRB-accredited routes only, recorded as a fifth SB4 rung entry; the two Not successful cells are failure descriptions, not statements. 4.6 is a row label only.",
 "S4, outcome paragraphs in sections 1 to 3 taken as statements: 1.6 (\"can\" and \"are able therefore to\"), 1.9 and 1.11 (\"are able to\"), 1.13 (\"able to\"), 1.31 (\"can\"), 2.4 and 3.9 (\"will\"); recorded force `will`. For Abbott: whether \"can\" in a narrative paragraph counts as an outcome statement.",
 "S4, force outside the five: 1.15 (\"a legal duty\", the Equality Act's) is recorded as `describes`; 2.3 (\"it would be expected that\") is recorded as `describes`; 1.21 (\"will need to\") as `will`. 4.7 (\"requires\", \"will not be made\") as `will`.",
 "S4, not taken: obliging words outside the five in 1.38 and 1.41 (\"there is a need\"), 4.4 (\"It is important ... as a guideline only\") and 2.10's \"essential\" (2.10 is taken for its \"will\").",
 "S4, plain-present provider norms, not statements (template open point 5): 1.1 (\"Courses include\"), 1.8, 1.12, 1.17, 1.18, 1.19, 1.26, 1.39, 2.1 (\"Courses ... commonly\", 11 bullets), 2.7, 3.12 (\"Courses are designed to\", 7 bullets), 3.18, 3.19, 3.20, 3.24, 4.2.",
 "S4, lists not taken: 1.40 (four aims of the subject, no modal); 1.42 (eleven AI principles under \"Programme teams consider\", a plain-present lead-in, though 1.43 then says course teams \"should also engage with the above principles\"; 1.43 is the record, and the skeleton's 1.42 candidates are not); 3.6 (\"consider and may incorporate\") and 3.8 (\"consider\"; \"typically provide\"), permissive; 3.17 (\"may include\"). 3.10's lead-in obliges (\"should consider\"), so its 23 bullets are records 3.10.b1 to b23; its stem is not a record.",
 "S4, permissive or descriptive and not taken: 1.3, 1.14, 2.5, 2.8, 2.11 (\"may also require\"), 2.12 (describes the external examining system), 3.7, 3.11 (\"will vary\"), 3.14, 3.22 (\"may be required\"), 3.23.",
 "S4, 4.1: \"providers clarify the extent to which the benchmark standards should be met\" is recorded as a provider statement with force `should`; the clarifying itself is plain present.",
 "S4, spans: the skeleton's paragraph spans run on into sub-headings and page numbers, and 4.5's runs on through the whole table, 4.7's through the back matter; records use `find` with the paragraph text alone. Page numbers inside a span (2.2, 2.9) stay in `source`.",
 "S5, crosswalk: 2.5 gives the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9; the FHEQ document's Table 1 (std:doc:qaa-fheq-2024-framework, S5) gives them at SCQF 7 and SCQF 8. Recorded as stated; the issuer's text looks one level out. For Abbott.",
 "S5: 4.4 names \"Level 7\" and \"Level 11\" without naming the frameworks; read as FHEQ and FQHEIS (inferred). CQFW is not named; Wales appears for course length (2.6) and the quality arrangements (front matter).",
 "S6, SB6: the AI theme is headed \"Artificial intelligence\" in section 1 and \"generative artificial intelligence\" in the front matter; recorded under the one shared id theme:generative-ai (batch 1 convention). The front matter and section 1 both name the EDI theme \"Equity\", not \"Equality\".",
 "S6, SB2: theme:enterprise is carried by no obliging statement in its own paragraphs (1.32 to 1.40 are descriptive); its only statement is 3.10.b13.",
 "S2, subjects: HECoS 100459 education studies and CAH22-01-01 are named by the statement (its subject); CAH22-01-02 teacher training (front matter: \"allied areas including teacher training\") and HECoS 101246 professional practice in education (3.3 teaching studies; 3.7 qualified teacher status) are inferred and wait for P3.",
 "SB5: no PSRB is named; the statement speaks of PSRBs in general. None of their requirements is ingested.",
 "S7, S8: the previous statement's date is not given in the body; the back matter names advisory groups for 2019 (minor update), 2015, 2007 and 2000, and the cover note says \"Fifth Edition Published - 10 April 2025\". supersedes points to a 2019 statement not held.",
 "S4, levels: learner and both statements in sections 1 to 3 are recorded at fheq:6 for the honours degree; they also bear on master's students. Provider duties carry level none, except 4.1 and 4.3, which set the scope of the standards (fheq:6, with master's in award).",
 "Patterns against Psychology: the standards are one four-column table, not lists; the honours rungs share one lead-in (4.3) and are paired by row; a master's column sits beside the honours columns as a guide; a pass-or-not professional competence row copied from Annex D; cells open \"The student can\" or \"A student can\"; a fifth theme (artificial intelligence); most obliging paragraphs in sections 1 to 3 are provider duties (student version not applicable); three curricula (subject-specific, practice-based, transversal) with a figure.",
]
