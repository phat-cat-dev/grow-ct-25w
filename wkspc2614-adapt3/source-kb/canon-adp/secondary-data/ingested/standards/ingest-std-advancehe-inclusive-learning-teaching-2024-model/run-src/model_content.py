# Content for ingest-std-advancehe-inclusive-learning-teaching-2024-model (std, 4 October 2026; D-std-0018).
# Read by model_build.py. `label` and every `source` must be found verbatim in the held text; everything else is ours.
# `anchor` names text that comes before a label which occurs more than once (the span is found after it).

NAME = 'advance-he-2024-inclusive-learning-teaching-framework-standard'   # library name: pdf/, txt/, records/
DOC = 'ingest-std-advancehe-inclusive-learning-teaching-2024-model'
ID = 'std:doc:advancehe-inclusive-learning-teaching-2024-model'
PFX = 'advancehe/inclusive-2024'
TITLE = 'Inclusive learning and teaching framework'
SERIES = 'advancehe-student-success-frameworks-2024'
PDF_SHA = 'd4f6264fdcdc88431b9f2e8d9d892c88bfd6073b8452712e57ebc300c57fff18'
THEORY = 'ing:doc:inclusive-learning-teaching-framework-advance-he-2024'

AXES = [
    dict(id='perspective:institution', label='Institution', page=7),
    dict(id='perspective:educators', label='Educators and related staff', page=9,
         note='labelled "Educators" in the structure figure (p. 5) and "Educators and related staff" on pp. 8 and 12'),
    dict(id='perspective:students', label='Students', page=11),
]
GROUPS = []
EDITION = 'digital edition, 2024'
DATES_OTHER = ['PDF created 25 June 2024', 'PDF modified 8 July 2024']
MODEL_KIND = 'condition-model'
FIGURE = dict(form='dial', pages=[7, 9, 11], readFrom='figure image')
USE = 'to place inclusion at the core of learning and teaching and to move from fixed rules to compassion in everyday choices; each perspective has three uses (S4 use.*) (D1, p. 12)'

# ---------------------------------------------------------------- M2 components, clockwise from the top of each dial
COMPONENTS = [
 # Institution (p. 7): kindness at the top; the open segment top left
 dict(slug='kindness', axis='perspective:institution', label='Fostering a culture of kindness', page=7,
   explained=[('It empowers readers to take a dynamic approach that moves away from static rules, processes and policies to those of compassion and kindness, acknowledging the impact of the everyday choices we make.', 'stated', 12)],
   ctype='culture', actor='institution', about='kindness as the institution\'s culture',
   para='The institution builds a culture in which care for people shapes everyday decisions, ahead of fixed rules and procedure.',
   conds=['theme:compassion'],
   prac='Make kindness part of how the institution runs: in policy, in how decisions are explained and in how staff are treated, so that care is the norm and not a favour.',
   ben='You can expect the people and systems around your study to treat you with care, and to explain decisions that affect you.',
   aaw='Describe this as a cultural condition set by the institution, not a teaching technique. Do not present kindness as softness or lowered expectations; present it as how rules are applied. Set it beside the compassionate, relational pedagogies component, which is its classroom form.',
   aad='Raise it when a person describes a rule applied without regard to circumstance. Ask: "Where does a rule here get in the way of treating someone fairly?" and "Who could you ask to apply it with more discretion?" Avoid moralising about individual staff.',
   holds='Decisions about students are made and explained with regard to the person affected, and discretion is used where a rule would cause needless harm.',
   signs=['policies include a route for exceptions and say who decides', 'decisions are explained in plain terms to the student affected', 'staff speak of students\' circumstances without blame'],
   absent='Rules are applied the same way regardless of circumstance, and students learn to expect refusal.',
   steer='Write with warmth and without blame: acknowledge that circumstances differ, and show where help or discretion can be sought.'),
 dict(slug='contextual-adaptation', axis='perspective:institution', label='Creating conditions for contextual adaptation', page=7,
   explained=[('Rather than expecting students to adapt to unsuitable environments, inclusive cultures of learning and teaching anticipate difference and adapt based on the context.', 'stated', 3),
              ('It is important that institutions consider and implement policies and practices which are culturally aligned yet able to recognise the fluidity of evolving contexts.', 'stated', 6)],
   ctype='structure', actor='institution', about='room to adapt practice to the setting',
   para='Policy and practice leave room for staff to adjust to the setting and the students present, so that the environment changes rather than the student.',
   conds=['theme:contextual-adaptation'],
   prac='Write policies that set a purpose and leave staff room to adapt how it is met, and review them as the student body and setting change.',
   ben='You can expect your course to adjust how things are done when the usual way does not work for the people taking it.',
   aaw='Present this as the institutional permission that makes local adaptation possible. Do not imply that any adaptation is allowed: the purpose of a policy stays; the means can flex. Link it to anticipating difference, which is what staff do with that permission.',
   aad='Raise it when staff say "the system will not let me". Ask: "What is the purpose of this rule, and is there more than one way to meet it?" Avoid promising flexibility the institution has not granted.',
   holds='Staff can change how a requirement is met for a group or a person without seeking exceptional approval, provided its purpose is kept.',
   signs=['course teams change formats or timings within a term without escalation', 'policies state their purpose as well as their procedure', 'reviews ask whether a rule still fits the current students'],
   absent='Every variation needs special approval, so practice stays fixed and students are asked to fit it.',
   steer='Offer more than one way to reach the same aim, and make clear which parts are fixed and which can change.'),
 dict(slug='challenge-structures', axis='perspective:institution', label='Empowering all to challenge the legitimacy of existing structures', page=7,
   explained=[('Inclusion is often unintentionally gatekept by those upholding existing policies, practices and processes.', 'inferred', 2),
              ('The biggest opportunities for meaningful inclusion and organisational success come from understanding what isn’t working.', 'inferred', 6)],
   ctype='culture', actor='all', about='permission to question existing structures',
   para='Staff and students are able, and encouraged, to ask whether existing policies and processes are justified, above all where they keep some students out.',
   conds=['theme:structural-challenge'],
   prac='Make it safe and expected for anyone to ask why a process exists and whom it excludes, and act on what the questions reveal.',
   ben='You are entitled to ask why things are done the way they are, especially if a rule seems to work against some students.',
   aaw='Describe this as legitimate questioning, not as rule-breaking. Do not encourage ignoring requirements; encourage asking whether they are justified and raising it through a route that can change them.',
   aad='Raise it when a person accepts an excluding practice as fixed. Ask: "Who does this arrangement suit, and who does it leave out?" and "Where could you raise that?" Avoid turning it into blame of named people.',
   holds='Questions about whether a policy or practice is fair are raised openly, answered, and sometimes lead to change.',
   signs=['students and staff raise concerns about processes in open forums', 'responses give reasons and say what will change', 'some policies change because of such questions'],
   absent='Existing arrangements are treated as given, and questioning them is seen as disloyal or naive.',
   steer='Invite the learner to ask why a convention exists and whom it serves, and treat that question as part of the learning.'),
 dict(slug='reconfigure-structures', axis='perspective:institution', label='Being prepared to reconfigure institutional structures', page=7,
   explained=[('Develop leadership and structures to prioritise cultures of inclusion in learning and teaching.', 'stated', 12),
              ('Institutional leaders that deliberately seek out heterogeneous views are equipped to drive effective cohesion between inclusive practices, leadership and policies.', 'inferred', 6)],
   ctype='structure', actor='institution', about='willingness to change institutional structures',
   para='Leaders are ready to change how the institution is organised when its structures stand in the way of inclusion.',
   conds=['theme:structural-challenge'],
   prac='Treat structures (committees, timetables, assessment regulations, roles) as open to redesign when evidence shows they exclude, and give leaders the remit to redesign them.',
   ben='You can expect your university to change how it is organised, not only to ask you to cope, when the way it works shuts some students out.',
   aaw='Present this as the institution\'s side of the bargain: questioning (the challenge component) leads somewhere only if structures can change. Do not overstate it as a promise of any particular change.',
   aad='Raise it when a fix is being sought from individuals for a structural problem. Ask: "Is this a problem one tutor can solve, or one the structure creates?" Avoid suggesting that staff alone should absorb structural failings.',
   holds='When a structure is shown to exclude, someone with authority owns its redesign and the change is made within a stated time.',
   signs=['reviews of regulations name inclusion as a test', 'structural changes cite the evidence that prompted them', 'leaders report on changes made, not only on plans'],
   absent='Structural problems are handed back to individual staff and students to work around.',
   steer='Where a barrier is structural, say so plainly rather than presenting it as the learner\'s problem to solve.'),
 dict(slug='diversity-of-voice', axis='perspective:institution', label='Fostering diversity of voice to centre inclusivity', page=7,
   explained=[('Welcome diverse perspectives, and be accountable for ensuring critical, divergent, or marginalised perspectives are not dismissed.', 'stated', 12),
              ('Institutional leaders that deliberately seek out heterogeneous views', 'stated', 6)],
   ctype='practice', actor='institution', about='many voices heard in decisions',
   para='Decisions draw on a wide range of voices, and dissenting or marginalised views are sought out and acted on rather than set aside.',
   conds=['theme:student-voice-partnership'],
   prac='Seek out views that differ from the majority, students\' included, before deciding; record how they shaped the decision, and answer for any that were set aside.',
   ben='Your view counts, including when it differs from most people\'s, and you can expect to hear what was done with it.',
   aaw='Describe voice as something sought and answered for, not merely allowed. Do not equate it with surveys alone. Link it to partnership and co-creation with students.',
   aad='Raise it when a decision is described with no mention of who was consulted. Ask: "Whose view is missing here?" and "How would they hear what happened to their input?" Avoid tokenism, such as one student speaking for all.',
   holds='Decisions record whose views were sought, include views from groups usually unheard, and report back what was done with them.',
   signs=['consultation reaches beyond the usual representatives', 'minority or critical views appear in decision records', 'people who gave views are told the outcome'],
   absent='The same few voices shape decisions, and critical or minority views are thanked and ignored.',
   steer='Bring in more than one perspective on the topic, including views from outside the mainstream, and ask the learner whose view is missing.'),

 # Educators and related staff (p. 9): compassionate pedagogies at the top; the open segment top left
 dict(slug='compassionate-relational', axis='perspective:educators', label='Compassionate, relational pedagogies', page=9,
   explained=[('Make decisions in your own context with compassion, understanding that policies, processes and notions of evidence may reinforce barriers to inclusion.', 'stated', 13),
              ('the framework gives principles to support facilitators of learning and teaching to both anticipate and respond compassionately to student need.', 'stated', 3)],
   ctype='relationship', actor='educator', about='teaching built on care and relationship',
   para='Teaching rests on relationships of care: staff respond to what students need with compassion and judge each case in its setting.',
   conds=['theme:compassion'],
   prac='Build working relationships with students, learn enough about their circumstances to respond well, and use your discretion with care where a rule or a habit would harm.',
   ben='You can expect the people who teach you to know you as a person and to respond to what you need with care.',
   aaw='Present this as a pedagogy (how teaching is done), grounded in relationship. Do not reduce it to pastoral support or to being nice; it includes holding high expectations with care.',
   aad='Raise it when a teacher describes a student only by performance. Ask: "What do you know about what is going on for this student?" and "What would a caring response look like that still keeps the standard?" Avoid implying staff must solve every personal difficulty.',
   holds='Staff know their students well enough to notice need, and respond to it with care while keeping expectations clear.',
   signs=['staff use students\' names and refer to what they know of them', 'responses to difficulty open with a question, not a sanction', 'students say they would approach staff with a problem'],
   absent='Contact is transactional, and students meet procedure before they meet a person.',
   steer='Address the learner directly and warmly, acknowledge that circumstances differ, and keep the standard clear.'),
 dict(slug='self-actualisation', axis='perspective:educators', label='Self-actualisation', page=9, anchor='Recognising students and selves as authentic learners',
   explained=[('this framework positions the facilitation of student and staff self-actualisation as key to promoting inclusive cultures.', 'stated', 2),
              ('We can do this by supporting staff and students to develop and believe in their own judgements.', 'stated', 2)],
   ctype='disposition', actor='all', about='staff and students growing into their own judgement',
   para='Staff and students are helped to develop, and to trust, their own judgement, as the way to an inclusive culture.',
   conds=['theme:agency-self-actualisation'], same='students.self-actualisation',
   prac='Give staff and students the room and the support to make judgements of their own, and back them when they do.',
   ben='You are supported to grow into your own judgement and to trust it.',
   aaw='Use the issuer\'s term, self-actualisation, and gloss it as growing into and trusting one\'s own judgement; note that it applies to staff as well as students here. Do not attribute the term to Maslow without saying the source does not.',
   aad='Raise it when a person defers every judgement to a rule or an authority. Ask: "What do you think is right here, and why?" Avoid pushing confidence where the person needs information first.',
   holds='Staff and students make and defend their own judgements, and are supported rather than overruled when they do so reasonably.',
   signs=['staff adapt practice on their own judgement and explain why', 'students are asked for their reasoning, not only their answer', 'reasonable judgements are backed even when another choice was possible'],
   absent='People wait to be told, and judgement is exercised only by those with authority.',
   steer='Ask the learner to make and justify a judgement of their own, and treat a reasoned answer as valuable even where others are possible.'),
 dict(slug='critical-thinkers', axis='perspective:educators', label='Empowering students to be critical thinkers', page=9,
   explained=[('This includes using all learning episodes to promote students’ critical thinking, agency and power to influence.', 'stated', 11),
              ('Rather than an end goal, inclusion is a mindset which promotes critical thinking and cultural transformation.', 'stated', 2)],
   ctype='practice', actor='educator', about='developing students\' critical thinking',
   para='Staff use every learning activity to build students\' critical thinking and their sense that they can influence what happens.',
   conds=['theme:critical-thinking'],
   prac='Design each activity so students question claims, weigh evidence and form a view, and show them that their reasoning can change things.',
   ben='You will be asked to question, weigh evidence and form your own view, and that view can make a difference.',
   aaw='Tie critical thinking to agency, as the source does: thinking critically includes the power to act on it. Do not present it only as an academic skill.',
   aad='Raise it when a task asks only for recall. Ask: "Where in this task does the student question or judge something?" Avoid treating criticism as negativity.',
   holds='Learning activities regularly require students to question, evaluate and decide, and their conclusions are taken seriously.',
   signs=['tasks ask for a judgement with reasons', 'students challenge sources or the tutor without penalty', 'student conclusions lead to changes in the session or course'],
   absent='Students receive and reproduce content, and questioning is reserved for later study.',
   steer='Include at least one point where the learner questions a claim, weighs evidence and states a reasoned view.'),
 dict(slug='authentic-learners', axis='perspective:educators', label='Recognising students and selves as authentic learners', page=9,
   explained=[('work in ways that are authentic to them.', 'stated', 3),
              ('Be supported to develop in authentic, meaningful ways, rather than expected to fit into unsuitable environments.', 'stated', 13)],
   ctype='disposition', actor='educator', about='learning as one\'s genuine self',
   para='Staff treat students, and themselves, as learners who bring who they are to their study, rather than people who must fit one mould.',
   conds=['theme:authenticity'],
   prac='Recognise the experience, identity and ways of working that students and colleagues bring, and let them show in how learning is done.',
   ben='You can bring who you are and what you know to your learning; you do not have to become someone else to succeed.',
   aaw='Note that the component names staff too ("selves"): educators are learners. Do not confuse it with authentic assessment, which is a different idea; link to it only as a related practice.',
   aad='Raise it when a person feels they must hide their background or way of working to fit in. Ask: "What do you bring that this task could use?" Avoid assuming what anyone\'s identity is.',
   holds='Students and staff can draw on their own experience and ways of working in learning, and these are treated as assets.',
   signs=['tasks invite students to draw on their own experience', 'more than one way of working is accepted', 'staff talk about their own learning'],
   absent='One way of being a student is rewarded, and others are corrected.',
   steer='Invite the learner to draw on their own experience and ways of working, and value what they bring.'),
 dict(slug='anticipating-difference', axis='perspective:educators', label='Anticipating difference without judgment', page=9,
   explained=[('inclusive cultures of learning and teaching anticipate difference and adapt based on the context.', 'stated', 3),
              ('Notice how your practices might impact students, and question your assumptions around what excellence and appropriate behaviour might look like.', 'inferred', 13),
              ('One aspect of this may be the hidden curriculum, namely the unspoken rules we have around what it means to succeed in higher education.', 'inferred', 8)],
   ctype='practice', actor='educator', about='planning for difference in advance',
   para='Staff expect students to differ, plan for that from the start, and do not measure students against an assumed typical student.',
   conds=['theme:anticipating-difference', 'theme:hidden-curriculum'],
   prac='Design for the range of students you will have, not for an imagined typical one; make unwritten expectations explicit, and check your own assumptions about what good looks like.',
   ben='You can expect your course to be designed with different students in mind, and the unwritten rules of study to be explained.',
   aaw='Describe this as design in advance, not reaction after a problem. Link it to the hidden curriculum, which the source raises in the same section. Do not equate difference with deficit.',
   aad='Raise it when a teacher plans for "the average student". Ask: "Who might find this harder for reasons that have nothing to do with ability?" and "What unwritten rule does this task rely on?" Avoid listing groups as problems.',
   holds='Teaching is planned for the range of students expected, and the unwritten expectations of study are made explicit.',
   signs=['materials and tasks offer more than one route in', 'expectations such as how to use feedback or office hours are spelled out', 'staff check assumptions about what excellent work looks like'],
   absent='Teaching assumes one kind of student, and those who differ discover the rules by failing them.',
   steer='Make unspoken expectations explicit, offer more than one way in, and avoid assuming what the learner already knows.'),

 # Students (p. 11): mattering at the top right; the open segment top left
 dict(slug='mattering', axis='perspective:students', label='Mattering', page=11,
   explained=[('Treating students like they matter means seeing their experiences and needs as legitimate, and an important factor in decision-making.', 'stated', 10),
              ('it is the process and mindset we use to make decisions in which we show students whether they matter.', 'stated', 10)],
   ctype='relationship', actor='all', about='students knowing they count',
   para='Students\' experiences and needs are taken as legitimate and weigh in decisions, so that each student can see they count.',
   conds=['theme:belonging-mattering'],
   prac='Treat what students tell you about their experience as evidence, let it weigh in decisions, and show them that it did.',
   ben='You matter: your experience and needs are taken seriously and count when decisions are made.',
   aaw='Present mattering as shown through how decisions are made, as the source does, not as a feeling staff should induce. Link it to belonging, which it underpins.',
   aad='Raise it when a student doubts they are noticed. Ask: "When did someone here act on something you told them?" Avoid reassurance with no evidence behind it.',
   holds='Students\' accounts of their experience are taken as legitimate, affect decisions, and students are shown that they did.',
   signs=['students are asked about their experience and told what changed', 'individual students are noticed when absent or struggling', 'students say staff know who they are'],
   absent='Students feel anonymous, and their accounts are discounted as anecdote.',
   steer='Address the learner as someone whose experience counts, and invite them to bring it into the task.'),
 dict(slug='self-actualisation', axis='perspective:students', label='Self-actualisation', page=11, anchor='Psychologically safe environments',
   explained=[('highlights that all students matter, if they are to build confidence and enhance their self-actualisation.', 'stated', 11),
              ('Be empowered to explore what enables them to thrive, and support them in trusting their judgement.', 'stated', 13)],
   ctype='disposition', actor='student', about='students growing into their own judgement',
   para='Students build the confidence to work out what helps them thrive and to trust their own judgement.',
   conds=['theme:agency-self-actualisation'], same='educators.self-actualisation',
   prac='Help students find out what helps them learn and thrive, and build their confidence to act on their own judgement.',
   ben='You are supported to find out what helps you thrive and to trust your own judgement.',
   aaw='Gloss the issuer\'s term as growing in confidence and trusting one\'s own judgement; note the source ties it to mattering. Do not present it as an endpoint students reach.',
   aad='Raise it when a student asks to be told the right way. Ask: "What has worked for you before?" and "What would you choose, and why?" Avoid withholding guidance the student needs.',
   holds='Students choose how to approach their learning, reflect on what works for them, and act on their own judgement with support.',
   signs=['students make choices about how they learn or are assessed', 'reflection asks what helped and why', 'students explain their own decisions'],
   absent='Students wait to be told what to do and doubt their own judgement.',
   steer='Give the learner a real choice and ask them to explain it, building confidence in their own judgement.'),
 dict(slug='critical-thinking', axis='perspective:students', label='Recognising the value of critical thinking', page=11,
   explained=[('This includes using all learning episodes to promote students’ critical thinking, agency and power to influence.', 'stated', 11)],
   ctype='disposition', actor='student', about='students valuing critical thinking',
   para='Students come to see critical thinking as worth doing and as a way to have a say in their learning.',
   conds=['theme:critical-thinking'],
   prac='Show students what critical thinking achieves, in their subject and beyond it, so they value it rather than seeing it as an exercise.',
   ben='Questioning and weighing things up is worth your effort: it is how you have a say in what you learn and what happens around you.',
   aaw='Distinguish this from the educators\' component: here the condition is that students value critical thinking, not only that staff promote it.',
   aad='Raise it when a student sees critical work as box-ticking. Ask: "Where has questioning something made a difference for you?" Avoid lecturing on its importance.',
   holds='Students choose to question and evaluate without being prompted, and can say why it matters to them.',
   signs=['students raise questions unprompted', 'students can say what critical thinking changed in their work', 'students apply it outside set tasks'],
   absent='Students treat critical thinking as a requirement to satisfy rather than a habit worth having.',
   steer='Show the learner what questioning achieves in a real case before asking them to do it.'),
 dict(slug='psychological-safety', axis='perspective:students', label='Psychologically safe environments', page=11, anchor='Mattering',
   explained=[('Through everyday actions we can create psychological safety by listening receptively, valuing feelings and understanding the importance of context.', 'stated', 10),
              ('Creating psychologically safe environments enables students to work effectively and safely with people from different and diverse backgrounds.', 'stated', 11),
              ('This enables psychologically safe environments that allow truly dialogic conversations that embed lived experience as a crucial form of evidence.', 'stated', 5)],
   ctype='environment', actor='all', about='safety to speak and to err',
   para='Students and staff can speak up, ask, disagree and get things wrong without fear of being judged or penalised.',
   conds=['theme:psychological-safety'],
   prac='Listen properly, take feelings seriously and respond to mistakes as part of learning, so that students can speak, ask and disagree without risk.',
   ben='You can ask questions, disagree and make mistakes without being judged for it; that is part of how you learn.',
   aaw='Use the term as the source does: an environment for open dialogue in which lived experience counts as evidence. Do not confuse safety with comfort or with avoiding challenge.',
   aad='Raise it when a student is reluctant to speak or ask. Ask: "What would make it easier to say that in the group?" Avoid promising that nothing will ever feel uncomfortable.',
   holds='Students speak, ask, disagree and admit mistakes in learning settings, and doing so carries no penalty.',
   signs=['students ask questions that reveal what they do not know', 'disagreement with peers or staff is heard respectfully', 'mistakes are discussed openly as part of learning'],
   absent='Students stay silent to avoid judgement, and mistakes are hidden.',
   steer='Frame mistakes and questions as expected, invite the learner\'s own experience, and allow for disagreement.'),
]

OPEN = [
 dict(axis='perspective:institution', page=7), dict(axis='perspective:educators', page=9), dict(axis='perspective:students', page=11),
]
OPEN_REASON_PAGE = 12
OPEN_REASON = 'One segment in each dial is left intentionally blank to represent the many unknown unknowns – complex factors that we may not realise we are missing – and the importance of not assuming we know enough to make judgements about a student’s needs and circumstances.'
OPEN_INSTR = {
 'perspective:institution': 'Do not fill this segment. When the institution\'s side is in play, ask what else in this institution bears on inclusion that the five named components miss, and hold the answer as context, not as part of the model.',
 'perspective:educators': 'Do not fill this segment. When the educators\' side is in play, ask what else in this teaching setting bears on these students that the five named components miss, and hold the answer as context.',
 'perspective:students': 'Do not fill this segment. When the students\' side is in play, ask the person what else matters for these students that the four named components miss, and do not assume you know their needs.',
}

# ---------------------------------------------------------------- S4 statements
# (id suffix, source, stem, perspective, mood, force, forceNote, statementType, addressee, verbs, about, paraphrase, page,
#  prac, ben, aaw, aad)
STEMS = {'requires': 'Inclusive learning and teaching requires:'}
STATEMENTS = [
 dict(heading='Inclusive learning and teaching requires:', n='requires.b1', src='understanding that the status quo is not a level playing field', stem='requires', axis=None, mood='gerund',
   force='must', fnote='D-std-0016: "requires" (lead-in) read as must', stype='requirement', addr='provider',
   verbs=['understanding'], about='unequal starting points', page=3,
   para='Requires recognising that existing arrangements do not give every student an equal start.',
   prac='Start from the recognition that current arrangements do not put all students on equal terms; this is required, not optional.',
   ben='not-applicable: a stance required of staff and the institution, not of the student',
   aaw='State this as the first requirement the issuer sets for inclusive learning and teaching, with must force from "requires". Do not restate it as a claim about any one group.',
   aad='Raise it when someone assumes fairness means treating everyone identically. Ask: "Does everyone start this from the same place?" Avoid lecturing.'),
 dict(heading='Inclusive learning and teaching requires:', n='requires.b2', src='actively seeking to know the unexpected impacts we might have on our students', stem='requires', axis=None, mood='gerund',
   force='must', fnote='D-std-0016: "requires" (lead-in) read as must', stype='requirement', addr='provider',
   verbs=['seeking', 'know', 'have'], about='finding out unintended effects on students', page=3,
   para='Requires going out of one\'s way to discover the effects one has on students that were not intended.',
   prac='Find out, actively, how your practice affects students in ways you did not intend; waiting for complaints does not meet this requirement.',
   ben='not-applicable: a requirement on staff and the institution',
   aaw='Present this as an active duty to look for unintended effects, with must force. Link it to the hidden curriculum and to the anticipating-difference component.',
   aad='Raise it when a practice is defended because no one has complained. Ask: "How would you know if this affected some students badly?" Avoid implying bad intent.'),
 dict(heading='Inclusive learning and teaching requires:', n='requires.b3', src='welcome different ways of working for all students without needing “evidence” or “proof”', stem='requires', axis=None, mood='infinitive',
   force='must', fnote='D-std-0016: "requires" (lead-in) read as must', stype='requirement', addr='provider',
   verbs=['welcome', 'working', 'needing'], about='accepting other ways of working without demanding proof', page=3,
   para='Requires accepting that students may work in different ways without asking them to justify or prove why.',
   prac='Accept different ways of working from any student without first asking for documentation or proof of need.',
   ben='You should not have to prove a need before you are allowed to work in a way that suits you.',
   aaw='Note the issuer puts "evidence" and "proof" in quotation marks, signalling a critique of evidence demands; keep that nuance. The force is must, from the lead-in. Do not present it as removing formal adjustment processes.',
   aad='Raise it when a student is asked to justify a reasonable preference. Ask: "What would it cost to allow this for anyone who asks?" Avoid contradicting formal disability processes; this is about everyday flexibility.'),
 dict(heading='Inclusive learning and teaching requires:', n='requires.b4', src='reviewing our practices, processes and curricula by critically examining what is truly “non-negotiable”, and designing flexibly around this.', stem='requires', axis=None, mood='gerund',
   force='must', fnote='D-std-0016: "requires" (lead-in) read as must', stype='requirement', addr='provider',
   verbs=['reviewing', 'examining', 'designing'], about='separating the fixed from the flexible in design', page=3,
   para='Requires reviewing practice, process and curriculum to find what genuinely cannot change, and building flexibility around it.',
   prac='Review your course to separate what genuinely cannot change from what is habit, then design flexibly around the fixed core.',
   ben='not-applicable: a requirement on course design, met by staff',
   aaw='Present this as a design method: identify the truly fixed requirements, then flex the rest. Keep the quotation marks\' implication that much called fixed is not.',
   aad='Raise it during course design or review. Ask: "Which of these requirements would the subject itself fail without, and which are habit?" Avoid treating every requirement as negotiable.'),
 dict(heading='Institution', n='frame.institution', src='It is important that institutions consider and implement policies and practices which are culturally aligned yet able to recognise the fluidity of evolving contexts.', stem=None, axis='perspective:institution', mood='declarative',
   force='should', fnote='"it is important that" read as should: not in D-std-0016\'s list; proposed (Part E)', stype='expectation', addr='provider',
   verbs=['consider', 'implement', 'recognise'], about='policy that fits culture and adapts to change', page=6,
   para='Institutions should adopt policies and practices that fit their culture while staying able to respond as circumstances change.',
   prac='Set policies that fit the institution\'s culture and still respond to changing circumstances; review them for both.',
   ben='not-applicable: addressed to institutions',
   aaw='Present as the framing expectation of the institution perspective, force should (our reading of "it is important that"). Link it to the contextual adaptation component.',
   aad='Raise it in discussion of policy review. Ask: "Does this policy still fit the students we now have?" Avoid detail the institution has not stated.'),
 dict(heading='Educators and related staff', n='frame.educators', src='It is important that staff continually seek to change practices which are within their personal sphere of control, and actively use successes as leverage for challenging existing structures when appropriate.', stem=None, axis='perspective:educators', mood='declarative',
   force='should', fnote='"it is important that" read as should: not in D-std-0016\'s list; proposed (Part E)', stype='expectation', addr='provider',
   verbs=['seek', 'change', 'use', 'challenging'], about='changing what is in one\'s control, then structures', page=9,
   para='Staff should keep changing the practices they control, and use what works as grounds to question wider structures where that is right.',
   prac='Change what is within your own control first and keep doing so; then use what worked as evidence to argue for wider structural change.',
   ben='not-applicable: addressed to staff',
   aaw='Present as the framing expectation of the educators\' perspective, force should (our reading). Note its two steps: local change, then leverage. Link it to the challenge-structures component.',
   aad='Raise it when a teacher feels powerless. Ask: "What here is within your control?" and later "What has worked that you could use to argue for more?" Avoid urging confrontation.'),
 dict(heading='How can you use the framework?', n='use.institution.1', src='Develop leadership and structures to prioritise cultures of inclusion in learning and teaching.', axis='perspective:institution', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E)', stype='guidance', addr='provider',
   verbs=['Develop', 'prioritise'], about='leadership and structures for inclusion', page=12,
   para='Institutions should build leadership and structures that put inclusive cultures of learning and teaching first.',
   prac='Use the model to shape leadership roles and structures so that inclusion in learning and teaching is a priority, not an add-on.',
   ben='not-applicable: addressed to institutions',
   aaw='One of three uses the issuer gives for institutions; force should (imperative, our reading). Link to the reconfigure-structures component.',
   aad='Raise it with leaders. Ask: "Who owns inclusion in learning and teaching here, and with what authority?" Avoid assuming a structure exists.'),
 dict(heading='How can you use the framework?', n='use.institution.2', src='Inform and enhance strategic priorities, mapping how inclusive learning and teaching aligns with these priorities.', axis='perspective:institution', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E)', stype='guidance', addr='provider',
   verbs=['Inform', 'enhance', 'mapping', 'aligns'], about='linking inclusion to strategy', page=12,
   para='Institutions should use the model to shape strategy and show where inclusive learning and teaching fits it.',
   prac='Map inclusive learning and teaching against the institution\'s strategic priorities and use the model to improve them.',
   ben='not-applicable: addressed to institutions',
   aaw='A use of the model for strategy; force should (our reading). Do not overstate it as a requirement.',
   aad='Raise it in strategy work. Ask: "Where does inclusive teaching appear in our priorities, and where is it missing?"'),
 dict(heading='How can you use the framework?', n='use.institution.3', src='Welcome diverse perspectives, and be accountable for ensuring critical, divergent, or marginalised perspectives are not dismissed.', axis='perspective:institution', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E)', stype='guidance', addr='provider',
   verbs=['Welcome', 'ensuring', 'dismissed'], about='accountability for unheard views', page=12,
   para='Institutions should seek a range of views and answer for making sure that critical and marginalised ones are not brushed aside.',
   prac='Seek a range of views, and be answerable for making sure that critical, minority and marginalised views are acted on rather than brushed aside.',
   ben='not-applicable: addressed to institutions',
   aaw='Force should (imperative, our reading). Stress accountability, which goes beyond welcoming. Link to the diversity-of-voice component.',
   aad='Raise it when consultation is described. Ask: "Which critical views were heard, and what happened to them?"'),
 dict(heading='How can you use the framework?', n='use.educators.1', src='Notice how your practices might impact students, and question your assumptions around what excellence and appropriate behaviour might look like.', axis='perspective:educators', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E)', stype='guidance', addr='provider',
   verbs=['Notice', 'impact', 'question', 'look'], about='checking one\'s assumptions about excellence', page=13,
   para='Staff should watch for the effects of their practice on students and test their assumptions about what excellent work and proper conduct are.',
   prac='Watch for how your practice affects different students, and test your own picture of what excellent work and proper conduct look like.',
   ben='not-applicable: addressed to staff',
   aaw='Force should (imperative, our reading). Note the reflexive turn: the assumptions examined are the educator\'s own. Link to anticipating difference and the hidden curriculum.',
   aad='Raise it in reflection on marking or conduct expectations. Ask: "Where did your idea of excellent work come from, and who does it suit?"'),
 dict(heading='How can you use the framework?', n='use.educators.2', src='Make decisions in your own context with compassion, understanding that policies, processes and notions of evidence may reinforce barriers to inclusion.', axis='perspective:educators', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E); "may" here is possibility, not permission', stype='guidance', addr='provider',
   verbs=['Make', 'understanding', 'reinforce'], about='compassionate local decisions', page=13,
   para='Staff should decide with compassion in their own setting, aware that rules, processes and evidence demands can themselves create barriers.',
   prac='Decide with compassion in your own setting, aware that rules, procedures and demands for evidence can themselves be barriers.',
   ben='not-applicable: addressed to staff',
   aaw='Force should (imperative, our reading). Note the claim that notions of evidence can be a barrier, which links to requirement b3. Link to the compassionate pedagogies component.',
   aad='Raise it when a decision is being made by the book. Ask: "Could the rule itself be the barrier here?"'),
 dict(heading='How can you use the framework?', n='use.educators.3', src='Be empowered – and empower students – to explore what enables them to thrive, and support them in trusting their judgement.', axis='perspective:educators', mood='imperative',
   force='should', fnote='imperative read as should (proposed; Part E)', stype='guidance', addr='both',
   verbs=['empowered', 'empower', 'explore', 'enables', 'thrive', 'support', 'trusting'], about='mutual empowerment and trust in judgement', page=13,
   para='Staff should take up their own agency, extend it to students, help them find what lets them thrive and back their judgement.',
   prac='Take up your own agency and extend it to students: help them find out what lets them thrive, and back their judgement.',
   ben='You are encouraged to find out what helps you thrive and to trust your own judgement.',
   aaw='Force should (imperative, our reading). It addresses staff and students at once. Link to both self-actualisation components.',
   aad='Raise it when a student defers to staff on how they learn best. Ask: "What have you found works for you?"'),
 dict(heading='How can you use the framework?', n='use.students.1', src='Be supported to develop in authentic, meaningful ways, rather than expected to fit into unsuitable environments.', axis='perspective:students', mood='entitlement',
   force='should', fnote='entitlement read as should (proposed; Part E)', stype='guidance', addr='learner',
   verbs=['supported', 'develop', 'expected', 'fit'], about='developing as oneself, not fitting in', page=13,
   para='Students should be helped to develop in ways that are genuine and meaningful to them, not made to fit settings that do not suit them.',
   prac='Support students to develop in ways that are genuine and meaningful to them, and change unsuitable settings rather than asking students to fit them.',
   ben='You should be helped to grow in ways that are real and meaningful to you, not expected to squeeze into a setting that does not suit you.',
   aaw='An entitlement: what students should receive; force should (our reading). Link to the authentic-learners component.',
   aad='Raise it when a student is struggling to fit a format. Ask: "What would let you do this in a way that works for you?"'),
 dict(heading='How can you use the framework?', n='use.students.2', src='Be treated like they matter, and with compassion.', axis='perspective:students', mood='entitlement',
   force='should', fnote='entitlement read as should (proposed; Part E)', stype='guidance', addr='learner',
   verbs=['treated', 'matter'], about='being treated as mattering', page=13,
   para='Students should be treated as people who count, and with compassion.',
   prac='Treat every student as someone who counts, and with compassion, in every contact.',
   ben='You should be treated as someone who counts, and with compassion.',
   aaw='An entitlement; force should (our reading). Link to the mattering component.',
   aad='Raise it when a student reports being dismissed. Ask: "What happened, and who could you raise it with?"'),
 dict(heading='How can you use the framework?', n='use.students.3', src='Be empowered to explore what enables them to thrive, and support them in trusting their judgement.', axis='perspective:students', mood='entitlement',
   force='should', fnote='entitlement read as should (proposed; Part E)', stype='guidance', addr='learner',
   verbs=['empowered', 'explore', 'enables', 'thrive', 'support', 'trusting'], about='finding what helps one thrive', page=13,
   para='Students should be enabled to find out what helps them thrive and be supported to trust their own judgement.',
   prac='Enable students to find out what helps them thrive, and support them to trust their own judgement.',
   ben='You should have the chance to find out what helps you thrive and support to trust your own judgement.',
   aaw='An entitlement; force should (our reading). Note the second clause shifts to the supporter ("support them"). Link to the students\' self-actualisation component.',
   aad='Raise it in tutorials on study approaches. Ask: "What conditions help you do your best work?"'),
]

# ---------------------------------------------------------------- M6 conditions carried (provisional)
CONDS = {
 'theme:compassion': 'decisions and teaching shaped by care for the person affected',
 'theme:contextual-adaptation': 'practice adapts to the setting and its students, not the reverse',
 'theme:structural-challenge': 'structures that exclude can be questioned and are changed',
 'theme:student-voice-partnership': 'a range of voices, students\' included, shapes decisions and is answered',
 'theme:agency-self-actualisation': 'people grow into, use and trust their own judgement',
 'theme:critical-thinking': 'questioning and evaluating are practised and valued',
 'theme:authenticity': 'learners bring who they are, and that is treated as an asset',
 'theme:anticipating-difference': 'teaching is designed in advance for the range of students',
 'theme:hidden-curriculum': 'the unwritten rules of study are made explicit',
 'theme:belonging-mattering': 'students see that their experience and needs count',
 'theme:psychological-safety': 'speaking, asking, disagreeing and erring carry no penalty',
}

PSF = ['V1', 'V2', 'V3', 'V4', 'V5', 'A1', 'A2', 'A3', 'A4', 'A5', 'K1', 'K2', 'K3', 'K4', 'K5']
PSF_LEAD = 'Inclusive learning and teaching can be relevant to all dimensions of the framework:'
FELLOWSHIP = 'Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.'
SCOPE = 'This framework is relevant to anyone, in any role, that has input into student learning, student outcomes, and/or the student experience in any shape or form.'
OPEN_NOTE_LEAD = OPEN_REASON

# ---------------------------------------------------------------- document-level parts
AGENTDEF = ('A practice model from Advance HE\'s Student Success Frameworks: fourteen components of inclusive learning and teaching, '
            'seen from the institution, educators and students, each held here as a practice theme that can qualify the context of '
            'a lesson or a piece of material. Reach for it to set or check the conditions under which students learn. It sets no '
            'levels and no outcomes: pair it with a framework or benchmark for what students achieve.')
SUMMARY = ('Advance HE (2024) sets out inclusive learning and teaching as the deliberate shaping of approaches so that every student '
           'can thrive, and as the foundation of quality rather than a competing priority. It draws three dials, one for each of '
           'the institution, educators and related staff, and students, with five, five and four named segments and one segment '
           'in each left blank for what is not yet known. Four requirements frame it, and a short list of uses is given for each '
           'perspective. It states that it bears on every dimension of the Professional Standards Framework 2023 and invites its '
           'use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.')

# S3: (number, order, componentType, parent, heading, gloss, pages, readFrom)
S3 = [
 ('what-is', 1, 'section', 'none', 'What is inclusive learning and teaching in higher education?', 'definition, the mindset and the four requirements', '2-3', 'text layer'),
 ('requires', 2, 'stem', 'what-is', 'Inclusive learning and teaching requires:', 'the lead-in to the four requirements', '3', 'text layer'),
 ('who-for', 3, 'section', 'none', 'Who is the framework for?', 'audiences: academic developers, module and course leaders, facilitators, decision makers, students\' unions', '2-3', 'text layer'),
 ('why', 4, 'section', 'none', 'Why is inclusive learning and teaching important?', 'rationale: rethinking practice; psychological safety and lived experience', '4', 'text layer'),
 ('structure', 5, 'figure', 'none', 'How is the framework structured?', 'the three perspectives shared by the series', '5', 'figure image'),
 ('institution', 6, 'perspective', 'none', 'Institution', 'framing prose for the institution', '6', 'text layer'),
 ('institution.dial', 7, 'figure', 'institution', '(dial)', 'five segments and one open segment', '7', 'figure image'),
 ('educators', 8, 'perspective', 'none', 'Educators and related staff', 'framing prose for educators; the hidden curriculum', '8-9', 'text layer'),
 ('educators.dial', 9, 'figure', 'educators', '(dial)', 'five segments and one open segment', '9', 'figure image'),
 ('students', 10, 'perspective', 'none', 'Students', 'framing prose for students: mattering, psychological safety', '10-11', 'text layer'),
 ('students.dial', 11, 'figure', 'students', '(dial)', 'four segments and one open segment', '11', 'figure image'),
 ('use', 12, 'use-list', 'none', 'How can you use the framework?', 'purpose, the open segments, three uses for each perspective', '12-13', 'figure image'),
 ('psf', 13, 'section', 'none', 'How does this framework align with the Professional Standards Framework (PSF) 2023?', 'the PSF crosswalk table and the Fellowship invitation', '14', 'text layer'),
]
EXCLUDED = [('back-cover', 'We help higher education organisations be the best they can be ...', 'other: the issuer\'s promotional back cover', '15')]

BCONCEPTS = [
 dict(slug='inclusive-learning-and-teaching', form='inclusive learning and teaching', defn='deliberately shaping teaching and its setting so that every student can thrive, treated as the basis of quality', scope='covers culture, policy and practice as well as the curriculum; not limited to any protected group', cat='approach'),
 dict(slug='hidden-curriculum', form='hidden curriculum', defn='the unwritten expectations about how to succeed in study that students must pick up without being told', scope='the source raises it under educators; the practice theme theme:hidden-curriculum', cat='concept'),
 dict(slug='mattering', form='mattering', defn='a student\'s sense, borne out by how decisions are made, that their experience and needs count', scope='named a student segment; linked to belonging', cat='concept'),
 dict(slug='psychological-safety', form='psychological safety', defn='a setting in which people can speak, ask, disagree and make mistakes without fear of judgement or penalty', scope='named a student segment; the source links it to dialogue and lived experience as evidence', cat='concept'),
 dict(slug='self-actualisation', form='self-actualisation', defn='growing into and trusting one\'s own judgement; here applied to staff and students alike', scope='the source does not cite Maslow or define the term further', cat='concept'),
 dict(slug='unknown-unknowns', form='unknown unknowns', defn='factors that bear on a student which those designing or teaching have not recognised', scope='represented by the open segment in each dial', cat='concept'),
]

PART_E = [
 'Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF\'s creation date (25 June 2024; modified 8 July 2024), as ing\'s run 0137 does. `copyrightNotice: none-stated`.',
 'Held text: held by Abbott\'s permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.',
 'M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11); the text layer gives the labels in a different order. Each label is still found verbatim in the held text, so MD-2 holds.',
 'M2 explainedBy: links marked `inferred` are std\'s reading; the source does not tie its prose to its segments.',
 'S4 force: "it is important that" (frame.institution, frame.educators) and the imperative and entitlement use items are read as `should`, marked on each force line. Neither form is in D-std-0016. For Abbott: rule whether these read as should.',
 'S4 requires.b3: the issuer\'s grammar breaks the list ("welcome" after three gerunds); recorded as given, `mood: infinitive`.',
 'S6: the document never names EDI or accessibility as such (EDI appears only in the excluded back cover); theme:edi is carried, inferred.',
 'M6: every practice theme is provisional until the shared theme register exists (Abbott, 05:09: "we will call them themes").',
 'S7 siblingOf: the internationalising and access, retention, attainment and progression models are held (library) but not yet ingested under this variant; their ids are reserved.',
 'D3: Advance HE\'s web page for the series (current status, date, the full list of frameworks in the series) not reached; wanted.',
]


# ---------------------------------------------------------------- contract 0.2.0 additions (moved out of the builder)
S2 = dict(
  governs="the conditions for inclusive learning and teaching across an institution, its teaching and its students' experience (D1, pp. 2-3)",
  providers=['higher education institutions (as stated: "our institutions")'],
  whoMustUse="no one must; offered to anyone with input into student learning, outcomes or experience, and named as particularly useful to academic developers, module and course leaders, facilitators, decision makers and students' unions (D1, pp. 2-3)",
  howUsed=['design', 'review', 'other: strategy, staff development, Fellowship evidence'],
  statedScope=SCOPE, scopePage=3)
SECTOR_DEFAULT = ['theme:edi']
S6 = [dict(id='theme:edi', role='carries', carriedIn=['what-is', 'why', 'institution', 'educators', 'students', 'use'],
           basis='inferred: the document is about inclusion throughout but never names EDI (Part E)')]
S7 = [
 dict(rel='partOf', target=SERIES, note='Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)'),
 dict(rel='modelledAs', target=THEORY, note='the same source run as theory with a dialogue layer (ing run 0137); read for consistency, not used as a source'),
 dict(rel='alignsWith', target='std:doc:advancehe-psf-dimensions-2023-framework', note='stated: relevant to every PSF 2023 dimension (M5)'),
 dict(rel='partOf', target='std:doc:advancehe-enhancing-student-success-2024-model', note='the series overview names inclusive learning and teaching as one of its nine areas'),
]
PSF = dict(codes=['V1', 'V2', 'V3', 'V4', 'V5', 'A1', 'A2', 'A3', 'A4', 'A5', 'K1', 'K2', 'K3', 'K4', 'K5'],
           lead=PSF_LEAD, fellowship=FELLOWSHIP, page=14, codeNote='relevant, as stated for every dimension')
M5_INFERRED = [
 dict(**{'from': 'model', 'to': 'theme:edi', 'note': "inclusion is the model's whole subject"}),
 dict(**{'from': PFX + '/educators.anticipating-difference', 'to': 'theme:accessibility', 'note': 'designing in advance for difference includes disabled students; the model does not name disability'}),
 dict(**{'from': PFX + '/students.psychological-safety', 'to': 'theme:internationalisation', 'note': "safe work with people from diverse backgrounds (D1, p. 11) links to the internationalising model's intercultural components"}),
]
B4 = [
 dict(rel='related', **{'from': 'mattering'}, to='psychological-safety', note='both under students; the source links mattering to confidence and safety'),
 dict(rel='related', **{'from': 'hidden-curriculum'}, to='inclusive-learning-and-teaching', note='noticing it is named as a key opportunity'),
 dict(rel='related', **{'from': 'unknown-unknowns'}, to='inclusive-learning-and-teaching', note='the open segments'),
]
B5 = [
 "self-actualisation: gloss it on first use as growing into and trusting one's own judgement, because the source uses it without definition and readers may assume Maslow's sense.",
 'mattering: keep it distinct from belonging, because the source treats it as shown through decisions, not as a feeling.',
]
D3 = [dict(citation='Advance HE, Student Success Frameworks (series web page), current', settles=['S8', 'S7'])]
CHANGE = 'rebuilt on the generic builder; position.perspective becomes position.axis; S7 adds the series overview.'
CHANGES_PRIOR = ['0.1.0, 2026-10-04 05:15: first built (Abbott, 05:02 and 05:03; D-std-0018, D-std-0019), the worked example of the model template 0.1.0-draft: 14 components, 3 open segments, 15 statements, 11 practice themes (Abbott, 05:09: conditions are themes).']

# ---- practice theme working lines from the shared register (tools/practice_themes.json 0.1.0; D-std-0020)
CONDS = {k: {'theme:transition': 'students are prepared and supported as they move into, through and on from study', 'theme:evidence-informed-enhancement': 'practice is mapped, its effects are evaluated and it is improved on that evidence', 'theme:agency-self-actualisation': 'people grow into, use and trust their own judgement', 'theme:whole-institution': "the institution's strategy, quality processes, estate and staff pull together towards one aim", 'theme:collaboration': 'learning and problem-solving are done with others, across subjects, professions and sectors', 'theme:belonging-mattering': 'students see that their experience and needs count', 'theme:career-development': 'students learn to explore, decide and manage their own paths and professional identity', 'theme:anticipating-difference': 'teaching is designed in advance for the range of students', 'theme:student-voice-partnership': "a range of voices, students' included, shapes decisions and is answered", 'theme:feedback-dialogue': 'feedback is timely, usable, two-way and acted on', 'theme:authenticity': 'learners bring who they are, and that is treated as an asset', 'theme:interconnectivity': 'work in one area, discipline or place is linked to others', 'theme:real-world-learning': 'learning, assessment and settings are modelled on real practice', 'theme:enterprising-capability': 'learners build and practise the skills of turning ideas into value', 'theme:compassion': 'decisions and teaching shaped by care for the person affected', 'theme:contextual-adaptation': 'practice adapts to the setting and its students, not the reverse', 'theme:hidden-curriculum': 'the unwritten rules of study are made explicit', 'theme:targeted-support': 'help reaches the students who need it, early and before difficulty grows', 'theme:assessment-literacy': 'staff and students share an understanding of criteria, standards and how work is judged', 'theme:critical-thinking': 'questioning and evaluating are practised and valued', 'theme:intercultural-engagement': 'people from different cultures meet, work together and learn from each other', 'theme:consistent-judgement': 'assessment judgements are consistent, calibrated and fair across markers, modules and groups', 'theme:programmatic-assessment': 'assessment is planned across a whole programme so that tasks connect, balance and build', 'theme:structural-challenge': 'structures that exclude can be questioned and are changed', 'theme:global-citizenship': 'learners prepare to act responsibly on shared global challenges', 'theme:professional-learning': 'staff are given time, support and recognition to develop their practice', 'theme:systems-futures-thinking': 'problems are seen as connected systems and judged against possible futures', 'theme:graduate-attributes': 'personal qualities, values and interpersonal abilities are developed, shown and carried across settings', 'theme:entrepreneurial-mindset': 'learners come to see themselves as able to act on ideas, and learn from setbacks', 'theme:equitable-participation': 'every student, and member of staff, can take part fully and on fair terms', 'theme:psychological-safety': 'speaking, asking, disagreeing and erring carry no penalty', 'theme:community-engagement': 'learning connects with communities, employers and partners beyond the institution', 'theme:action-competence': 'learners turn understanding into action and judge its effects', 'theme:flexibility': 'learners choose how, what, when and where they learn, with tools, spaces and rules that allow it', 'theme:embedded-practice': 'an aim is built into curriculum, teaching and assessment, not added on', 'theme:values-reflection': 'learners examine how their values and experiences shape their judgements and actions', 'theme:shared-language': 'key terms are defined, agreed and used the same way by everyone involved', 'theme:entrepreneurial-pedagogy': 'teaching methods and assessment match whether learners study, prepare for or do enterprise', 'theme:assessment-for-learning': 'assessment and its feedback are designed so that students learn through them'}.get(k, v) for k, v in CONDS.items()}
