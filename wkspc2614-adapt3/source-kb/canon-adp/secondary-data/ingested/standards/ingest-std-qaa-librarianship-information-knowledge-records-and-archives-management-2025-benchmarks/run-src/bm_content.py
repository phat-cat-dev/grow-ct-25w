# bm_content.py: judgement for run 0117, QAA Subject Benchmark Statement Librarianship, Information, Knowledge,
# Records and Archives Management (April 2025). std run agent. Read by tools/bm_build.py.
# Keys of P are S4 ids under qaa/librarianship-information-knowledge-records-and-archives-management-2025/.
# All text below except `find` spans is ours.

HON = "bachelor's with honours"
MAS = ["master's", 'postgraduate diploma', 'postgraduate certificate']
ALLA = [HON] + MAS
NA = ('n/a', 'a duty on the provider and the people who run the course, not a standard the student reaches')

CITE = '(QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, %s)'
LEVELNAME = {'fheq:6': 'FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16)', 'fheq:7': 'FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text)'}
SPINE = {'fheq:6': 'spine:6 in the reference framework (std:ref:uk-framework, R8)', 'fheq:7': 'spine:7 in the reference framework (std:ref:uk-framework, R8)'}
FWD = {('fheq:6', 'knowledge'): 'qaa/fheq-2024/4.15.b1', ('fheq:6', 'understanding'): 'qaa/fheq-2024/4.15.b1',
       ('fheq:6', 'subject-skill'): 'qaa/fheq-2024/4.15.b6', ('fheq:6', 'generic-skill'): 'qaa/fheq-2024/4.15.b7',
       ('fheq:6', 'none'): 'qaa/fheq-2024/4.15.b1',
       ('fheq:7', 'knowledge'): 'qaa/fheq-2024/4.17.b1', ('fheq:7', 'understanding'): 'qaa/fheq-2024/4.17.b1',
       ('fheq:7', 'subject-skill'): 'qaa/fheq-2024/4.17.b5', ('fheq:7', 'generic-skill'): 'qaa/fheq-2024/4.17.b6',
       ('fheq:7', 'none'): 'qaa/fheq-2024/4.17.b1'}

P = {}
EXTRA = {}   # per record: fw (framework id), pair (S4 id at the other award), q (a question for dialogue), when (dialogue trigger)


def s(i, extra=None, **k):
    P[i] = k
    EXTRA[i] = extra or {}


def ordn(n):
    return ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
            'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
            'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth'][n - 1]


def loc(i):
    if '.b' in i:
        p, b = i.split('.b')
        return 'para %s, %s item' % (p, ordn(int(b)))
    if '.s' in i:
        p, n = i.split('.s')
        return 'para %s, %s sentence' % (p, ordn(int(n)))
    return 'para %s' % i


# =============================================================== section 2: obliging sentences and provider duties
s('2.3.s1', find='As such, students are required to reflect on their own experiences and ethical priorities as information users, when information is itself the subject of study.',
  type='requirement', rung='none', force='must', level='none', appliesTo='students of the subject at any award', addressee='learner',
  verbs=['required', 'reflect'], about='reflecting on their own information use and ethics', domain='subject-skill', award=ALLA,
  para='Since information is the very thing the subject studies, students must look back on their own experience and ethical priorities as people who use information.',
  prac='Give students structured occasions to examine their own habits and ethical priorities as information users: the subject requires it, because information is what they study.',
  ben='You must reflect on how you yourself use information and on the ethical priorities you bring to it, because information is the thing you are studying.',
  extra=dict(q='What does your own way of finding and judging information say about the priorities you would bring to a service?',
             when='a student or team discusses reflective tasks, ethics teaching or why the course asks students to examine their own information habits'))
s('2.3.s2', find='Students should be able to develop and demonstrate an understanding of the fluidity of information, impact of use and need for appraisal amid societal and technological evolution.',
  type='outcome', rung='none', force='should', level='none', appliesTo='students of the subject at any award', addressee='learner',
  verbs=['develop', 'demonstrate'], about='how information shifts and why it needs appraising', domain='understanding', award=ALLA,
  para='Students should be able to build, and show, an understanding that information keeps changing, that how it is used has effects, and that it has to be judged afresh as society and technology move on.',
  prac='Students should come to understand, and be able to show, that information is fluid, that its use has consequences and that appraisal must keep pace with social and technical change.',
  ben='You should be able to show that you understand how information changes over time, how its use affects people, and why it needs judging again as society and technology change.',
  extra=dict(q='Can you think of a source whose value or meaning has changed since it was made, and how you would appraise it now?'))
s('2.6', find='Undergraduates studying Librarianship, Information, Knowledge, Records and Archives Management courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement, and will add others according to the areas covered in the other subject(s) of their degree.',
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint and combined honours students', addressee='learner',
  verbs=['achieve', 'add'], about='core skills for joint and combined honours students', domain='none', award=HON,
  para='Undergraduates taking the subject within a joint or combined degree, including major and minor routes, will attain the central subject-specific and generic skills set out here and gain others from their second subject.',
  prac='In a joint or combined honours course, students will reach the core of the subject-specific and generic skills set out here; the other subject adds further skills, so map which core items each route covers.',
  ben='If you study this field as part of a joint or combined degree, you will gain its core subject and general skills, plus further skills from the other subject you take.',
  extra=dict(q='Which of the core skills does your half of the course cover, and which come from your other subject?',
             when='a joint or combined honours student, or the team designing such a route, asks how much of the subject it must cover'))
s('2.17', find='The student voice is paramount in monitoring and review, and degree-awarding bodies will have in place a system for student input into the monitoring and evaluation process.',
  type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies', addressee='provider',
  verbs=['have'], about='a system for student input to course monitoring', domain='none', award=ALLA,
  para='Students\' views come first in monitoring and review, and the awarding body will run a system through which students feed into monitoring and evaluation.',
  prac='The awarding body will have a working route, such as a staff and student liaison forum, for students to contribute to course monitoring and evaluation.',
  ben=NA,
  extra=dict(q='How do students on this course currently feed into monitoring, and what changed last year as a result?',
             when='a programme team or quality office plans monitoring, annual review or student representation'))
s('2.18', find='Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.',
  type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=ALLA,
  para='In periodic review the institution will bring in external reviewers, for an outside view of planned changes and to confirm that threshold standards are met and content suits the subject.',
  prac='Plan periodic review with external reviewers who will give an independent view of proposed changes and confirm that threshold standards are met and the content fits the subject.',
  ben=NA,
  extra=dict(q='Who will act as the external reviewer at the next periodic review, and which proposed changes most need their view?',
             when='a programme team prepares for periodic review or revalidation'))

# =============================================================== 3.10: what assessment will include (lead-in "These will include assessments which:")
A310 = dict(type='expectation', rung='none', force='will', level='none', appliesTo='assessment in courses of the subject', addressee='both',
            domain='none', award=ALLA)
s('3.10.b1', verbs=['allow', 'develop', 'demonstrate'], about='assessment of professional competencies', **A310,
  para='Assessment will include tasks, such as portfolios, synoptic work and self-reflection, through which students build and show professional competence.',
  prac='Include assessment, for instance a portfolio, a synoptic task or a self-reflective piece, in which students grow and evidence professional competencies.',
  ben='You will be assessed through tasks such as portfolios, synoptic work and self-reflection, which let you build and show your professional skills.',
  extra=dict(q='Which piece of your portfolio best shows a professional skill, and what does it show?'))
s('3.10.b2', verbs=['provide'], about='reflexive evaluation of professional identity', **A310,
  para='Assessment will include chances to evaluate, reflexively and critically, professional and sector identity, professional growth and the student\'s own learning, through reflections, presentations or case studies.',
  prac='Include assessment, such as critical reflections, presentations or case studies, where students evaluate their professional and sector identity, their development and their learning journey.',
  ben='You will have assessments, such as reflective writing, presentations or case studies, where you look critically at your professional identity, your development and how your learning has gone.',
  extra=dict(q='How has your sense of yourself as an information professional changed since you started?'))
s('3.10.b3', verbs=['enable', 'engage', 'apply'], about='authentic assessment in real settings', **A310,
  para='Assessment will include authentic tasks in which students apply their learning to make a real contribution in a workplace, sector or community setting, through projects, placements or project documents.',
  prac='Include authentic assessment, such as practical projects, placements or project documentation, where students apply learning and make a genuine contribution in a sector, workplace or community setting.',
  ben='You will have assessments set in real workplaces, the sector or the community, such as projects or placements, where what you do makes a genuine contribution.',
  extra=dict(q='What did your placement or project change for the people it served?'))
s('3.10.b4', verbs=['demonstrate', 'work'], about='assessed group work', **A310,
  para='Assessment will include tasks, such as group projects, presentations or portfolios, that show students can work well with others in a team.',
  prac='Include assessed group work, such as joint projects, presentations or portfolios, through which students show they can collaborate effectively.',
  ben='You will be assessed on how well you work in a group, for example through team projects, joint presentations or shared portfolios.',
  extra=dict(q='What did you contribute to your last group task, and how did the group decide who did what?'))
s('3.10.b5', verbs=['demonstrate', 'use'], about='assessed use of digital technologies', **A310,
  para='Assessment will include tasks showing that students can use digital technologies, generative AI among them, to make websites, databases, catalogues, presentations, posters, social media outputs or other digital content.',
  prac='Include assessment in which students produce digital content (websites, databases, online catalogues, posters, social media outputs and the like) and may use generative AI in doing so.',
  ben='You will have assessments where you make digital content, such as a website, a database, an online catalogue or social media posts, and you may use generative AI tools to help.',
  extra=dict(q='Which digital tool did you use for your last piece of work, and how did you check what it produced?'))
s('3.10.b6', verbs=['enable', 'conduct'], about='assessed research', **A310,
  para='Assessment will include research tasks, gathering primary data or interrogating and synthesising secondary data at length, analysing it and presenting the findings.',
  prac='Include an assessed research task in which students collect primary data or work extensively with secondary data, analyse it and present what they find.',
  ben='You will carry out assessed research, collecting your own data or working closely with existing data, analysing it and presenting what you found.',
  extra=dict(q='What question would your research project answer, and where would your data come from?'))

# =============================================================== 4.2 and 4.4: provider duties
s('4.2', find='Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies.',
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer'], about='using Annex D to judge achievement above threshold', domain='none', award=HON,
  para='Each institution sets its own way of deciding what evidence shows achievement beyond the threshold, and should consult Annex D of the UK qualifications frameworks (the classification descriptions) in doing so.',
  prac='When deciding what evidence marks achievement above the threshold, use your own method but consult Annex D of the Frameworks (the classification descriptions for honours degrees).',
  ben=NA,
  extra=dict(fw='qaa/fheq-2024/annex-d (the classification bands, SL6 in std:doc:qaa-fheq-2024-framework)',
             q='How do your marking criteria for each class line up with the Annex D descriptions?',
             when='a programme team writes marking criteria or grade descriptors, or asks how classes above the threshold are judged'))
s('4.4', find='In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission.',
  type='expectation', rung='none', force='should', level='none', appliesTo='providers writing competence standards', addressee='provider',
  verbs=['follow'], about='competence standards and equality guidance', domain='none', award=ALLA,
  para='Where an institution writes competence standards under the Equality Act 2010 into a programme specification, it should follow the latest guidance of the Equality and Human Rights Commission.',
  prac='If you set competence standards (in the Equality Act 2010 sense) for a programme, follow the current Equality and Human Rights Commission guidance; the threshold standards here are not competence standards.',
  ben=NA,
  extra=dict(fw='4.4\'s own context: the threshold standards are not competence standards',
             q='Does the programme specification set any competence standards, and has the current equality guidance been checked for them?',
             when='a programme team considers competence standards, reasonable adjustments or a PSRB requirement'))

# =============================================================== 4.5 and 4.6: honours threshold lead-in
TH6 = dict(rung='threshold', level='fheq:6', appliesTo='honours graduates at the threshold', addressee='learner', award=HON)
s('4.5.s1', find='On graduating with an honours degree in Librarianship, Information, Knowledge, Records and Archive Management, students should be able to demonstrate a systematic understanding of the main body of knowledge for their course of study.',
  type='threshold', force='should', verbs=['demonstrate'], about='systematic grasp of the course\'s core knowledge', domain='knowledge', **TH6,
  para='At the honours threshold, students should be able to show a systematic grasp of the central knowledge their course covers.',
  prac='By the end of an honours course, students should be able to show ordered, systematic understanding of the course\'s core knowledge; teach and assess the whole of it, not isolated topics.',
  ben='By the end of your honours degree, you should be able to show a well-organised understanding of the main knowledge your course covers.',
  extra=dict(pair='4.10.s1', q='If you had to map the main areas of your course on one page, how would they connect?'))
s('4.5.s2', find='They should be able to understand and apply essential concepts, principles and practices of the subject in the context of well-defined scenarios, showing judgement in the selection and application of processes, materials and techniques.',
  type='threshold', force='should', verbs=['understand', 'apply', 'showing'], about='using core concepts in clearly bounded cases', domain='subject-skill', **TH6,
  para='They should be able to grasp and use the subject\'s key concepts, principles and practices in clearly bounded situations, choosing processes, materials and techniques with judgement.',
  prac='Honours students should apply the subject\'s key concepts, principles and practices to clearly framed cases, exercising judgement over which processes, materials and techniques to use.',
  ben='You should be able to understand and use the main ideas, principles and practices of your subject in clearly set-out situations, choosing sensibly which methods and materials to use.',
  extra=dict(pair='4.10.s2', q='In your last practical task, how did you decide which technique to use?'))
s('4.5.b1', type='threshold', force='should', verbs=['apply'], about='applying knowledge in structured, guided settings', domain='subject-skill', **TH6,
  para='Part of those concepts and practices: honours students should be able to use their knowledge where the setting is structured and guidance is given.',
  prac='Honours students should be able to put knowledge to work in structured contexts with guidance; at this level the setting is framed for them.',
  ben='You should be able to use what you know in tasks that are clearly structured and where you have guidance.',
  extra=dict(fw='qaa/fheq-2024/4.15.b6', q='Which task so far has asked you to apply what you know, and what guidance did you lean on?'))
s('4.5.b2', type='threshold', force='should', verbs=['analyse', 'evaluate'], about='analysing information within set frameworks', domain='subject-skill', **TH6,
  para='Honours students should be able to analyse and judge information inside frameworks already set for the task.',
  prac='Honours students should analyse and evaluate information within established frameworks, rather than devising their own.',
  ben='You should be able to analyse and judge information using frameworks that are already set out for you.',
  extra=dict(fw='qaa/fheq-2024/4.15.b7', q='Which framework did you use to judge a source recently, and what did it help you see?'))
s('4.5.b3', type='threshold', force='should', verbs=['use'], about='using tools and methods in practice', domain='subject-skill', **TH6,
  para='Honours students should be able to use the subject\'s tools, technologies and methods in practical settings.',
  prac='Honours students should use tools, technologies and methodologies of the field in practical settings, such as labs, projects or placements.',
  ben='You should be able to use the tools, technologies and methods of your field in practical work.',
  extra=dict(fw='qaa/fheq-2024/4.15.b2', q='Which tools or systems can you now use confidently, and which still feel new?'))
s('4.6', find='In this context, honours graduates at a threshold level of attainment (third class) will have demonstrated some degree of proficiency in the majority of the attributes listed in this Statement.',
  type='threshold', force='will', verbs=['demonstrated'], about='what the third-class threshold means', domain='none', **TH6,
  para='Honours graduates at the threshold, the third class, will have shown some proficiency in most, not all, of the attributes the statement lists.',
  prac='Read the honours lists as a profile: a third-class graduate will have shown some proficiency in most of the listed attributes, not every one of them.',
  ben='To reach the minimum level for an honours degree (a third), you will have shown some skill in most, though not all, of the abilities set out for your subject.',
  extra=dict(fw='qaa/fheq-2024/annex-d/summary/r1/3rd and the 3rd column of Annex D', pair='4.11.s1',
             q='Looking across the full list of abilities, which are your strongest and which have you not yet shown?'))

# =============================================================== 4.7 subject knowledge, understanding and skills (honours)
# 4.11 (master's) repeats most of these; each pair is set beside the other by id.
PAIR = {'4.7.b3': '4.11.b3', '4.7.b4': '4.11.b4', '4.7.b5': '4.11.b5', '4.7.b7': '4.11.b6', '4.7.b8': '4.11.b7', '4.7.b9': '4.11.b9',
        '4.7.b10': '4.11.b10', '4.7.b11': '4.11.b11', '4.7.b12': '4.11.b12', '4.7.b13': '4.11.b13', '4.7.b14': '4.11.b14',
        '4.7.b15': '4.11.b16', '4.7.b16': '4.11.b15', '4.7.b17': '4.11.b17', '4.7.b18': '4.11.b20', '4.7.b19': '4.11.b21',
        '4.7.b20': '4.11.b22', '4.7.b21': '4.11.b23', '4.5.s1': '4.10.s1', '4.5.s2': '4.10.s2', '4.6': '4.11.s1'}
RPAIR = {v: k for k, v in PAIR.items()}


def hon(i, verbs, about, domain, c, cb, find=None, after=None, fw=None, q=None, gen=False):
    """an honours threshold item: c is our verb phrase (third person), cb the student's (second person)"""
    k = dict(type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours graduates at the threshold',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON,
             para='At the honours threshold, graduates should be able to %s.' % c,
             prac=('By the end of an honours course, students should be able to %s; give them a task that lets them show it.' % c) if not gen else
                  ('Honours graduates should be able to %s; build it into teaching and assessment across the course, not one module.' % c),
             ben='By the end of your honours degree, you should be able to %s.' % cb)
    if find:
        k['find'] = find
        if after:
            k['after'] = after
    s(i, extra=dict(fw=fw, q=q, pair=PAIR.get(i)), **k)


hon('4.7.b1', ['develop', 'implement', 'identify', 'address'], 'tackling bias in collections, systems and services', 'subject-skill',
    'plan and carry out approaches that expose and reduce bias in collections, systems and services, so that people are fairly represented and obstacles to access come down',
    'plan and carry out ways of spotting and correcting bias in collections, catalogues and services, so that everyone is fairly represented and can reach what they need')
hon('4.7.b2', ['demonstrate', 'seek', 'remove'], 'a working commitment to access and equity', 'subject-skill',
    'show, across research, communication and teamwork, that they hold accessibility and fairness as commitments, and act to clear away what blocks access and participation',
    'show in all your work, research and teamwork included, that you care about access and fairness, and take steps to remove what stops people finding information or joining in')
hon('4.7.b3', ['create', 'cater'], 'inclusive physical and online spaces and collections', 'subject-skill',
    'shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs',
    'design library spaces and collections, physical and online, that work well for people with different abilities and needs')
hon('4.7.b4', ['partner', 'promote'], 'building literacies with community partners', 'subject-skill',
    'work with community groups and teachers to advance academic, data, digital, media and information literacies that serve scholarship and learning through life',
    'team up with community groups and teachers to help people build their academic, data, digital, media and information skills, for study and for learning through life')
hon('4.7.b5', ['engage', 'confronting', 'championing'], 'human rights, equality and fair access to information', 'understanding',
    'debate critically how information provision bears on human rights and equality, question structural inequality and bias (by race, gender or disability) in knowledge systems, and argue for fair access for groups once pushed aside',
    'discuss critically how information services affect human rights and equality, challenge bias built into knowledge systems, such as bias by race, gender or disability, and speak up for fair access for groups who have been left out')
hon('4.7.b6', ['advocate'], 'freedom of access and open access', 'subject-skill',
    'argue that free access to information is a basic human right, and make the case for open access to knowledge and for the skills and systems that make access possible',
    'argue that everyone has a right to reach information, and make the case for open access to knowledge and for the skills and systems that make it possible')
hon('4.7.b7', ['develop', 'addressing', 'ensuring'], 'retention schedules and preservation plans', 'subject-skill',
    'draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration',
    'write retention schedules and preservation plans for physical and digital material that keep it usable for years, including moving it to new formats when needed')
hon('4.7.b8', ['understand', 'apply'], 'archival principles in arrangement and description', 'understanding',
    'understand archival principles such as provenance and original order and use them when arranging and describing collections',
    'understand archival principles such as provenance and original order and use them when you arrange and describe material')
hon('4.7.b9', ['adhere', 'ensuring'], 'storage standards for fragile or sensitive items', 'subject-skill',
    'follow the sector\'s standards for keeping fragile or sensitive items, with the right environmental conditions and security',
    'follow the industry\'s standards for storing fragile or sensitive material, keeping conditions and security right')
hon('4.7.b10', ['master', 'enhance'], 'cataloguing, classification and metadata', 'subject-skill',
    'command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find',
    'catalogue, classify and describe resources and create metadata skilfully, using controlled vocabularies and standards so that people can find things')
hon('4.7.b11', ['design', 'manage', 'adhering'], 'content systems, repositories and web platforms', 'subject-skill',
    'design and run content management systems, digital repositories and web platforms in line with good accessibility practice',
    'set up and run content management systems, digital repositories and websites that follow good accessibility practice')
hon('4.7.b12', ['implement', 'create'], 'user-centred, accessible interface design', 'subject-skill',
    'apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use',
    'use user-centred design and accessibility guidelines to make online resources and services easy for everyone to use')
hon('4.7.b13', ['evaluate', 'apply', 'considering'], 'judging new technologies ethically', 'subject-skill',
    'appraise new technologies for managing information critically and put them to use, weighing their ethical consequences',
    'weigh up new technologies for managing information, use them well and think through their ethical effects')
hon('4.7.b14', ['collaborate', 'develop'], 'information literacy and reader development programmes', 'subject-skill',
    'build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need',
    'work with teachers and community partners to build information literacy and reading programmes that suit people at different levels and with different needs')
hon('4.7.b15', ['design', 'foster'], 'teaching and outreach for critical thinking', 'subject-skill',
    'plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online',
    'plan teaching and outreach sessions that help people think critically, read the media well and take part safely and responsibly online')
hon('4.7.b16', ['adapt'], 'critical information literacy for varied audiences', 'subject-skill',
    'adjust critical information literacy teaching for different audiences, children, adults and lifelong learners among them',
    'adjust how you teach critical information literacy for different groups, such as children, adults and lifelong learners')
hon('4.7.b17', ['collect', 'analyse', 'inform'], 'user data and metrics for evidence-based improvement', 'subject-skill',
    'gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving',
    'gather and analyse data about users, how services perform and trends in the sector, and use it to make decisions and keep improving')
hon('4.7.b18', ['explore', 'ensuring'], 'AI tools for automated tasks, with ethical oversight', 'subject-skill',
    'try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place',
    'try out AI tools for automatic tasks, such as creating metadata or recommending resources, while keeping an ethical check on how they are used')
hon('4.7.b19', ['champion'], 'intellectual freedom, privacy and openness', 'subject-skill',
    'stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data',
    'stand up for people\'s freedom of thought and expression, for the privacy of their data, and for open access to information and data')
hon('4.7.b20', ['participate', 'address'], 'organisational policy on information ethics', 'subject-skill',
    'help shape organisational policy on ethical information practice, responsible data governance and the rights of users',
    'help write your organisation\'s policies on the ethical use of information, careful handling of data and the rights of its users')
hon('4.7.b21', ['engage', 'support'], 'advocacy for fair access and privacy law', 'subject-skill',
    'take part in local and national campaigning for laws that widen fair access to information and protect users\' privacy',
    'take part in local and national campaigns for laws that give people fair access to information and protect their privacy',
    find='engage in local and national advocacy efforts to support legislation that promotes equitable access to information and safeguards user privacy.')

# =============================================================== 4.8 generic skills (honours)
G8 = [
    ('4.8.b1', ['identify'], 'identifying issues, questions and problems', 'qaa/fheq-2024/4.15.b7',
     'recognise the issues, questions and problems a situation raises', 'spot the issues, questions and problems a situation raises'),
    ('4.8.b2', ['demonstrate', 'applying', 'adhering'], 'accurate use of referencing styles', 'qaa/fheq-2024/4.15.b5',
     'use a wide range of referencing styles accurately, following the detail each one asks for', 'use many referencing styles accurately, following the detailed rules of each'),
    ('4.8.b3', ['identify', 'acquire'], 'finding and filling gaps in their knowledge', 'qaa/fheq-2024/4.15.b9.3',
     'see where their own knowledge falls short and gain what is missing', 'see where your own knowledge falls short and learn what is missing'),
    ('4.8.b4', ['understand', 'analyse'], 'understanding and analysing information', 'qaa/fheq-2024/4.15.b7',
     'make sense of knowledge and information and analyse it', 'make sense of knowledge and information and analyse it'),
    ('4.8.b5', ['synthesise'], 'drawing together what is known on a topic', 'qaa/fheq-2024/4.15.b3.2',
     'pull together the current state of knowledge on a given topic', 'pull together what is currently known about a topic'),
    ('4.8.b6', ['apply', 'provide'], 'reaching conclusions backed by evidence', 'qaa/fheq-2024/4.15.b7',
     'use knowledge and understanding to reach conclusions supported by evidence', 'use what you know and understand to reach conclusions backed by evidence'),
    ('4.8.b7', ['communicate'], 'communicating effectively', 'qaa/fheq-2024/4.15.b8',
     'communicate well and fittingly, in speech and in other forms', 'communicate clearly and suitably, in speech and in other ways'),
    ('4.8.b8', ['present'], 'presenting knowledge or argument clearly', 'qaa/fheq-2024/4.15.b8',
     'set out knowledge or an argument so that others can follow it', 'set out what you know, or an argument, so that others can follow it'),
    ('4.8.b9', ['work'], 'working with qualitative and quantitative data', 'qaa/fheq-2024/annex-d/practical/r4/3rd',
     'handle varied data, empirical qualitative and quantitative data included', 'work with many kinds of data, including qualitative and quantitative data from research'),
    ('4.8.b10', ['engage', 'collate', 'analyse', 'select', 'present'], 'critical use of digital technology', 'qaa/fheq-2024/annex-d/transferable/r1/3rd',
     'use a range of digital technologies critically to gather, analyse, choose and present information', 'use digital tools critically to gather, analyse, choose and present information'),
    ('4.8.b11', ['assert', 'undertaking', 'conducting', 'demonstrating'], 'intellectual independence', 'qaa/fheq-2024/4.15.b9.1',
     'show intellectual independence: working on tasks alone with suitable support, running their own research and exercising critical judgement', 'think and work for yourself: take on tasks alone with the right support, run your own research and make critical judgements'),
    ('4.8.b12', ['work', 'undertaking', 'participating'], 'working with others', 'qaa/fheq-2024/annex-d/transferable/r2/3rd',
     'work with others, in a group or team or by taking part in discussion', 'work with others, in a group or team or by joining in discussion'),
    ('4.8.b13', ['reflect'], 'reflecting on progress and personal leadership', 'qaa/fheq-2024/annex-d/transferable/r5/3rd',
     'look back on their own progress, their personal leadership skills among it', 'look back on your own progress, including how you lead'),
    ('4.8.b14', ['identify', 'examine'], 'examining values and ethics', 'qaa/fheq-2024/4.15.b7',
     'recognise and examine the values and ethics beneath culture, society and their own conduct', 'recognise and examine the values and ethics behind culture, society and your own choices'),
    ('4.8.b15', ['understand'], 'well-being, emotion and learning', 'qaa/fheq-2024/4.15.b5',
     'understand why well-being, mental health and emotion matter and how they bear on learning', 'understand why well-being, mental health and emotions matter and how they affect your learning'),
    ('4.8.b16', ['make'], 'using feedback to develop', 'qaa/fheq-2024/4.15.b5',
     'use the feedback they receive well, to take their thinking further', 'use the feedback you get to take your thinking further'),
    ('4.8.b17', ['appreciate', 'engage'], 'current debates on culture and society', 'qaa/fheq-2024/4.15.b7',
     'value and join current debates on culture and society, such as those on inequality and sustainability', 'follow and join current debates about culture and society, such as inequality and sustainability'),
]
for _i, _v, _a, _fw, _c, _cb in G8:
    hon(_i, _v, _a, 'generic-skill', _c, _cb, fw=_fw, gen=True)

# =============================================================== 4.9 and 4.10: master's lead-in
TH7 = dict(rung='threshold', level='fheq:7', appliesTo="graduates of postgraduate certificates, diplomas and master's degrees", addressee='learner', award=MAS)
D49 = dict(type='threshold', force='describes', **TH7)
s('4.9.b1', verbs=['emphasise', 'engage'], about='deeper understanding and engagement with research', domain='understanding', **D49,
  para="Postgraduate study involves advanced ideas that call for a deeper grasp of complex issues and the ability to work with current research and scholarship.",
  prac="Postgraduate courses build mastery of advanced ideas that deepen students' grasp of complex issues and their engagement with current research and scholarship.",
  ben='At postgraduate level, you work with advanced ideas that deepen your understanding of complex issues and draw you into current research and scholarship.',
  extra=dict(fw='qaa/fheq-2024/4.17.b1'))
s('4.9.b2', verbs=['highlight', 'apply'], about='applying knowledge where problems are ill-defined', domain='subject-skill', **D49,
  para='Postgraduate study involves advanced ideas that bring out the ability to use knowledge in real situations that are loosely defined or need new solutions.',
  prac="Postgraduate courses develop students' ability to apply knowledge to real cases that are poorly defined or call for innovation.",
  ben='At postgraduate level, you learn to use what you know in real situations where the problem is unclear or a new solution is needed.',
  extra=dict(fw='qaa/fheq-2024/4.17.b5'))
s('4.9.b3', verbs=['stress', 'conduct', 'evaluate', 'propose'], about='original research and new hypotheses', domain='generic-skill', **D49,
  para='Postgraduate study involves advanced ideas that put weight on doing original research, judging methods and putting forward new hypotheses.',
  prac='Postgraduate courses stress original research: students carry it out, evaluate methodologies and propose new hypotheses.',
  ben='At postgraduate level, you are expected to do original research, judge research methods and put forward new hypotheses of your own.',
  extra=dict(fw='qaa/fheq-2024/4.17.b4.2'))
s('4.9.b4', verbs=['focus', 'lead', 'influence', 'advocate', 'develop'], about='leading change and strategic solutions', domain='generic-skill', **D49,
  para='Postgraduate study involves advanced ideas centred on leading and shaping change, arguing for ethical practice and devising strategic answers to complex problems.',
  prac='Postgraduate courses centre on leadership: students learn to lead and influence change, advocate ethical practice and build strategic responses to complex challenges.',
  ben='At postgraduate level, you learn to lead and influence change, speak up for ethical practice and work out strategic answers to complex problems.',
  extra=dict(fw='qaa/fheq-2024/4.17.b8.1'))
s('4.10.s1', find='Given the diverse routes into this profession, including postgraduate qualification of those with undergraduate degrees in different disciplines, students should be expected to demonstrate a systematic and comprehensive understanding of the main body of knowledge for their course of study.',
  type='threshold', force='should', verbs=['demonstrate'], about='systematic and comprehensive core knowledge', domain='knowledge', **TH7,
  para="Because many enter the profession through postgraduate study after a first degree in another field, master's students should show a systematic and comprehensive grasp of their course's central knowledge.",
  prac="Postgraduate students, many with first degrees in other fields, should show systematic and comprehensive understanding of the course's core knowledge; plan induction for those new to the subject.",
  ben='By the end of your postgraduate course, you should be able to show a thorough, well-organised understanding of the main knowledge it covers, even if your first degree was in another subject.',
  extra=dict(pair='4.5.s1', q='Coming from your first degree, which parts of the core knowledge were new to you, and how secure do they feel now?'))
s('4.10.s2', find='They should be able to critically analyse and apply essential concepts, principles and practices of the subject in complex and diverse scenarios, demonstrating sound judgement in the selection and application of processes, materials and techniques.',
  type='threshold', force='should', verbs=['analyse', 'apply', 'demonstrating'], about='critical application in complex, varied cases', domain='subject-skill', **TH7,
  para="Master's students should be able to analyse critically and use the subject's key concepts, principles and practices in complex and varied situations, choosing methods and materials with sound judgement.",
  prac="At master's level, students should apply and critically analyse the subject's key concepts and practices in complex, varied cases, with sound judgement over processes, materials and techniques.",
  ben='You should be able to analyse critically and use the main ideas and practices of your subject in complex and varied situations, judging well which methods and materials to use.',
  extra=dict(pair='4.5.s2', q='Think of a messy, real case you worked on: what made it complex, and how did you choose your approach?'))
s('4.10.s3', find="At master's level, students may also be asked to demonstrate skills and understanding in relation to strategic thinking and leadership, as well as the ability to undertake original research to a higher academic standard.",
  type='expectation', rung='none', force='may', level='fheq:7', appliesTo="master's students", addressee='learner',
  verbs=['asked', 'demonstrate', 'undertake'], about='strategic thinking, leadership and original research', domain='generic-skill', award=MAS,
  para="Master's students may also have to show skill and understanding in strategic thinking and leadership, and the ability to carry out original research to a higher academic standard.",
  prac="A master's course may also ask students to show strategic thinking and leadership and to undertake original research at a higher academic standard; decide whether yours does and say so.",
  ben="On a master's course you may also be asked to show strategic thinking and leadership, and to carry out original research to a higher standard.",
  extra=dict(fw='qaa/fheq-2024/4.17.b6', q='Has your course asked you to lead anything or to plan research of your own, and how did it go?'))
s('4.11.s1', find="At master's level, graduates at a threshold level of attainment will have demonstrated some degree of proficiency in the majority of the attributes listed in this Statement.",
  type='threshold', force='will', verbs=['demonstrated'], about="what the master's threshold means", domain='none', **TH7,
  para="Master's graduates at the threshold will have shown some proficiency in most, not all, of the listed attributes.",
  prac="Read the master's lists as a profile: a threshold graduate will have shown some proficiency in most of the attributes, not every one.",
  ben='To reach the minimum level for your postgraduate award, you will have shown some skill in most, though not all, of the abilities set out for your subject.',
  extra=dict(pair='4.6', q='Looking across the full list of abilities, which can you already evidence, and which are still to come?'))


# =============================================================== 4.11 subject knowledge, understanding and skills (master's)
def mas(i, verbs, about, domain, c, cb, find=None, fw=None, q=None, gen=False, force='will', ff='4.11'):
    k = dict(type='threshold', rung='threshold', force=force, level='fheq:7', appliesTo="master's graduates at the threshold",
             addressee='learner', verbs=verbs, about=about, domain=domain, award=MAS,
             para=("At the master's threshold, graduates will have shown the ability to %s." % c) if force == 'will' else
                  ("Master's graduates should be able to show %s." % c),
             prac=("In postgraduate certificate, diploma and master's courses, give students room to show they can %s; at threshold they will have shown most such attributes to some degree." % c) if force == 'will' else
                  ("Postgraduate students should be able to show %s; build it into the research and project work of the course." % c),
             ben=("By the end of your postgraduate course, you will have shown that you can %s." % cb) if force == 'will' else
                 ("By the end of your master's course, you should be able to show %s." % cb))
    if ff:
        k['forceFrom'] = ff
    if find:
        k['find'] = find
    s(i, extra=dict(fw=fw, q=q, pair=RPAIR.get(i)), **k)


mas('4.11.b1', ['demonstrate'], 'information needs across disciplines and fields', 'understanding',
    'understand, with nuance, the particular information needs and sources of different disciplines and professions, such as STEM, law, business and the arts and humanities',
    'understand in detail what information different disciplines and professions need, such as science and engineering, law, business or the arts, and where it is found')
mas('4.11.b2', ['design', 'implement'], 'culturally responsive outreach and services', 'subject-skill',
    'design and deliver outreach, programmes and services that respond to culture and fit the needs of diverse communities',
    'design and run outreach, events and services that respect different cultures and meet the needs of diverse communities')
mas('4.11.b3', ['create', 'cater'], 'inclusive physical and online spaces and collections', 'subject-skill',
    'shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs',
    'design library spaces and collections, physical and online, that work well for people with different abilities and needs')
mas('4.11.b4', ['partner', 'promote'], 'building literacies for marginalised groups', 'subject-skill',
    'work with community groups and teachers to advance academic, data, digital, media and information literacies among marginalised groups',
    'team up with community groups and teachers to help marginalised groups build their academic, data, digital, media and information skills')
mas('4.11.b5', ['engage', 'confronting'], 'decolonising information practice', 'understanding',
    'debate critically the decolonising of information practice and challenge structural inequality in knowledge systems',
    'discuss critically how information practice can be decolonised and challenge the inequalities built into knowledge systems')
mas('4.11.b6', ['develop', 'addressing', 'ensuring'], 'retention schedules and preservation plans', 'subject-skill',
    'draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration',
    'write retention schedules and preservation plans for physical and digital material that keep it usable for years, including moving it to new formats')
mas('4.11.b7', ['understand', 'apply'], 'archival principles in arrangement and description', 'understanding',
    'understand archival principles such as provenance and original order and use them when arranging and describing collections',
    'understand archival principles such as provenance and original order and use them when you arrange and describe material')
mas('4.11.b8', ['implement'], 'disaster preparedness and recovery', 'subject-skill',
    'put in place disaster preparedness, with risk assessment, backup strategies and recovery plans',
    'put disaster plans in place, with risk assessments, backups and plans for recovery')
mas('4.11.b9', ['adhere', 'ensuring'], 'storage standards for fragile or sensitive items', 'subject-skill',
    'follow the sector\'s standards for keeping fragile or sensitive items, with the right environmental conditions and security',
    'follow the industry\'s standards for storing fragile or sensitive material, keeping conditions and security right')
mas('4.11.b10', ['master', 'enhance'], 'cataloguing, classification and metadata', 'subject-skill',
    'command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find',
    'catalogue, classify and describe resources and create metadata skilfully, using controlled vocabularies and standards so that people can find things')
mas('4.11.b11', ['design', 'manage', 'adhering'], 'content systems, repositories and web platforms', 'subject-skill',
    'design and run content management systems, digital repositories and web platforms in line with good accessibility practice',
    'set up and run content management systems, digital repositories and websites that follow good accessibility practice')
mas('4.11.b12', ['implement', 'create'], 'user-centred, accessible interface design', 'subject-skill',
    'apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use',
    'use user-centred design and accessibility guidelines to make online resources and services easy for everyone to use')
mas('4.11.b13', ['evaluate', 'apply', 'considering'], 'judging new technologies ethically', 'subject-skill',
    'appraise new technologies for managing information critically and put them to use, weighing their ethical consequences',
    'weigh up new technologies for managing information, use them well and think through their ethical effects')
mas('4.11.b14', ['collaborate', 'develop', 'address'], 'information literacy and reader development programmes', 'subject-skill',
    'build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need, children, adults and lifelong learners included',
    'work with teachers and community partners to build information literacy and reading programmes for people at different levels, from children to adults and lifelong learners')
mas('4.11.b15', ['adapt'], 'critical information literacy for varied audiences', 'subject-skill',
    'adjust critical information literacy teaching to what different audiences need, children, adults and lifelong learners among them',
    'adjust how you teach critical information literacy to what different groups need, such as children, adults and lifelong learners')
mas('4.11.b16', ['design', 'foster'], 'teaching and outreach for critical thinking', 'subject-skill',
    'plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online',
    'plan teaching and outreach sessions that help people think critically, read the media well and take part safely and responsibly online')
mas('4.11.b17', ['collect', 'analyse', 'inform'], 'user data and metrics for evidence-based improvement', 'subject-skill',
    'gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving',
    'gather and analyse data about users, how services perform and trends in the sector, and use it to make decisions and keep improving')
mas('4.11.b18', ['foster', 'exploring', 'enhance'], 'a culture of experiment in services', 'subject-skill',
    'build a habit of experiment, testing how new technologies and approaches could improve information services',
    'encourage a habit of trying things out, testing how new technologies and ideas could improve information services')
mas('4.11.b19', ['identify', 'developing'], 'spotting openings for enterprise', 'subject-skill',
    'look actively for chances to be entrepreneurial, creating new information products, services or ventures',
    'look out for chances to be enterprising and create new information products, services or businesses')
mas('4.11.b20', ['explore', 'ensuring'], 'AI tools for automated tasks, with ethical oversight', 'subject-skill',
    'try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place',
    'try out AI tools for automatic tasks, such as creating metadata or recommending resources, while keeping an ethical check on how they are used')
mas('4.11.b21', ['champion'], 'intellectual freedom, privacy and openness', 'subject-skill',
    'stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data',
    'stand up for people\'s freedom of thought and expression, for the privacy of their data, and for open access to information and data')
mas('4.11.b22', ['participate', 'address'], 'organisational policy on information ethics', 'subject-skill',
    'help shape organisational policy on ethical information practice, responsible data governance and the rights of users',
    'help write your organisation\'s policies on the ethical use of information, careful handling of data and the rights of its users')
mas('4.11.b23', ['engage', 'support'], 'advocacy for fair access and privacy law', 'subject-skill',
    'take part in local and national campaigning for laws that widen fair access to information and protect users\' privacy',
    'take part in local and national campaigns for laws that give people fair access to information and protect their privacy')
mas('4.11.b24', ['employ', 'implement', 'monitor', 'evaluate', 'understand'], 'strategic leadership of initiatives', 'subject-skill',
    'use strategic analysis and leadership to deliver, track and judge initiatives and grasp their effect on the communities or users concerned',
    'use strategic thinking and leadership to run, track and judge projects, and understand what they mean for the people they serve')
mas('4.11.b25', ['use', 'inform'], 'using results to plan future services', 'subject-skill',
    'draw on results to shape future services and outreach',
    'use what your projects achieved to shape future services and outreach',
    find='use outcomes to inform the development of future services and outreach.')

# =============================================================== 4.12 generic skills (master's): "students should be able to demonstrate:"
G12 = [
    ('4.12.b1', ['demonstrate'], 'research techniques and philosophies', 'qaa/fheq-2024/4.17.b2',
     'a full grasp of the research techniques their own research or advanced study needs, and a sound use of fitting research philosophies and methods',
     'a full understanding of the research techniques your own research needs, and that you can use suitable research philosophies and methods'),
    ('4.12.b2', [], 'originality in applying knowledge', 'qaa/fheq-2024/4.17.b3',
     'originality in the way they put knowledge to use', 'originality in how you put your knowledge to use'),
    ('4.12.b3', ['used', 'create', 'evaluate'], 'research as evidence for professional practice', 'qaa/fheq-2024/4.17.b3',
     'a working grasp of how established research and enquiry produce and test evidence that improves professional practice',
     'that you understand in practice how research methods produce and test evidence that improves professional work'),
    ('4.12.b4', ['complete'], 'an independent substantial project', 'qaa/fheq-2024/4.17.b6',
     'that they can carry through, by independent study, a substantial critical piece of empirical research, a work-based project, a major review or a case study, which may add to research or solve a workplace problem',
     'that you can complete on your own a substantial piece of critical research, a work-based project, a major review or a case study, which might add to research or solve a problem at work'),
    ('4.12.b6', ['evaluate'], 'evaluating current research critically', 'qaa/fheq-2024/4.17.b4.1',
     'a conceptual grasp that lets them judge current research and advanced scholarship in the field critically',
     'an understanding of ideas deep enough to judge current research and advanced study in your field critically'),
    ('4.12.b7', ['evaluate', 'develop', 'propose'], 'critiquing methods and proposing hypotheses', 'qaa/fheq-2024/4.17.b4.2',
     'a conceptual grasp that lets them assess and critique research methods and, where fitting, put forward new hypotheses, which may mean knowing methods from neighbouring fields',
     'an understanding of ideas deep enough to assess and critique research methods and, where it fits, suggest new hypotheses, perhaps drawing on methods from related subjects'),
    ('4.12.b8', ['deal', 'make', 'communicate'], 'complex issues, judgement and clear communication', 'qaa/fheq-2024/4.17.b5',
     'that they can handle complex issues both methodically and inventively, judge soundly when data are incomplete, and explain their conclusions plainly to expert and general audiences',
     'that you can handle complex issues methodically and creatively, judge well when you lack some of the data, and explain your conclusions clearly to experts and non-experts'),
    ('4.12.b9', [], 'self-direction and originality', 'qaa/fheq-2024/4.17.b6',
     'that they direct themselves and work with creativity and originality', 'that you direct your own work and bring creativity and originality to it'),
    ('4.12.b10', [], 'leadership and advocacy', 'qaa/fheq-2024/4.17.b8.1',
     'skill in leading and advocating, aware of the shifting internal and external factors that bear on both', 'that you can lead and speak up for a cause, aware of the changing pressures inside and outside an organisation that affect both'),
    ('4.12.b11', ['exploit'], 'networking globally', 'qaa/fheq-2024/4.17.b8.3',
     'that they can use tools and processes to network effectively across the world', 'that you can use tools and processes to build useful professional networks worldwide'),
    ('4.12.b12', ['challenge', 'justify'], 'challenging practice and justifying change', 'qaa/fheq-2024/4.17.b5',
     'that they can question current practice and make the case for the changes they propose', 'that you can question how things are done now and make the case for the changes you propose'),
]
for _i, _v, _a, _fw, _c, _cb in G12:
    mas(_i, _v, _a, 'generic-skill', _c, _cb, fw=_fw, gen=True, force='should', ff=None)

# =============================================================== agent instructions (aaw, aad): our words, composed per record
for _i, _r in P.items():
    _x = EXTRA[_i]
    _cite = CITE % loc(_i)
    _lv = _r['level']
    _fw = _x.get('fw') or FWD.get((_lv, _r['domain']))
    _pair = _x.get('pair')
    _q = _x.get('q') or ('Which piece of your work so far best shows what you can do on %s, and what would make it stronger?' % _r['about'])
    if _r['addressee'] == 'provider':
        _r['aaw'] = ('Treat this as a duty on the institution, worded with "%s": %s, for %s. Cite it as %s. '
                     'Do not present it as something a student must achieve, or as a regulatory requirement in England. '
                     'Set it beside %s.') % (_r['force'], _r['about'], 'honours courses' if _r['award'] == HON else 'every award the statement covers', _cite,
                                            _fw if _x.get('fw') else 'the threshold definitions at 4.6 and 4.11.s1 and the review duties at 2.17 and 2.18')
        _r['aad'] = ('Raise this when %s. Put it in practitioner terms, as something the course or institution does. '
                     'Ask, for example: "%s" Do not put it to a student as a standard they have to reach.') % (_x['when'], _q)
    elif _i.startswith('3.10'):
        _r['aaw'] = ('Treat this as an expected feature of assessment design, worded with "will", for every award the statement covers: %s. '
                     'Cite it as %s, and do not claim it fixes a method or a weighting. '
                     'Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12.') % (_r['about'], _cite)
        _r['aad'] = ('Raise this when a team designs assessment, or when a student asks how and why they will be assessed. '
                     'With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. '
                     'Ask, for example: "%s" Avoid reading the list out at length.') % _q
    elif _r['rung'] == 'none':
        _scope = 'at any award the statement covers' if _r['award'] == ALLA else ('for %s' % (_r['award'] if isinstance(_r['award'], str) else "master's and other postgraduate awards"))
        _r['aaw'] = ('Treat this as %s worded with "%s", %s: %s. Cite it as %s. '
                     'Do not claim it is a regulatory requirement or a rung of its own; set it beside %s.') % (
            'an expectation' if _r['force'] != 'must' else 'a requirement', _r['force'], _scope, _r['about'], _cite,
            ('the framework descriptor %s' % _fw) if _fw else 'the threshold lists in section 4 (4.7, 4.8, 4.11, 4.12)')
        _r['aad'] = ('Raise this when %s. Put it plainly, in the second person for a student and as a course design question for staff. '
                     'Ask, for example: "%s" Do not read the issuer\'s wording aloud at length.') % (
            _x.get('when') or 'a student or team asks what the course expects about %s' % _r['about'], _q)
    else:
        _hon = _r['award'] == HON
        _kind = ('an honours threshold standard worded with "should", of which a third-class graduate shows most items to some degree (4.6)' if _hon else
                 ("a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"%s\"%s" %
                  (_r['force'], '' if _r['force'] == 'describes' else ', of which a threshold graduate will have shown most to some degree (4.11)'
                   if _r['force'] == 'will' else '')))
        if _r['force'] == 'describes':
            _kind = "a description, with no modal of its own, of what postgraduate certificate, diploma and master's study involves (the lead-in at 4.9 says \"expected\")"
        if _r['domain'] == 'generic-skill':
            _kind = 'a generic skill: ' + _kind
        _set = []
        if _pair:
            _set.append('its counterpart %s at the other award' % _pair)
        _set.append('the framework descriptor %s' % _fw)
        _set.append(SPINE[_lv])
        _r['aaw'] = ('Treat this as %s. It holds at %s and concerns %s. Cite it as %s. '
                     'Do not present it as a regulatory requirement or as a standard for %s, and set it beside %s.') % (
            _kind, LEVELNAME[_lv], _r['about'], _cite, "master's awards" if _hon else 'honours degrees', ', '.join(_set[:-1]) + ' and ' + _set[-1])
        _r['aad'] = ('Raise this when %s asks what the course should leave them able to do about %s, or plans work that draws on it. '
                     'With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. '
                     'Ask, for example: "%s" Avoid reading the issuer\'s list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown.') % (
            'an honours student' if _hon else 'a postgraduate student', _r['about'], _q)

GRADE = {}
TH = {}

# =============================================================== front matter, S1, S2
META = dict(
    run='0117', p1='2026-10-03 17:45',
    title='Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management',
    heading='Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management (QAA, April 2025)',
    edition='Fifth edition, April 2025', published='2025-04',
    status='current',
    supersedes='the previous Subject Benchmark Statement, named only as such in the front matter; the advisory group list names a 2019 minor update, a 2015 and a 2007 revision and the 2000 original (D1, section 6)',
    subjects=[dict(scheme='hecos', code='100913', label='librarianship', basis='stated'),
              dict(scheme='hecos', code='100915', label='archives and records management', basis='stated'),
              dict(scheme='hecos', code='100370', label='information management', basis='inferred'),
              dict(scheme='hecos', code='100916', label='information services', basis='inferred'),
              dict(scheme='cah', code='CAH24-01-01', label='information services', basis='inferred')],
    awards=[HON, "master's", 'postgraduate diploma', 'postgraduate certificate'],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2025 revisions with cross-cutting themes (fifth edition of this statement)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=('A reference record of the QAA statement for librarianship, information, knowledge, records and archives management, 2025. '
                     'It holds the statement\'s standards as 101 records: honours threshold lists for subject skills and generic skills, master\'s threshold lists for the same, '
                     'and the few obliging sentences elsewhere, each with its span, our paraphrase, a practitioner and a student version and two instructions for AI agents. '
                     'Use it to write or check course outcomes in this field at FHEQ levels 6 and 7, never as a regulatory text.'),
    summary=('The statement covers honours degrees, postgraduate certificates and diplomas and master\'s degrees in librarianship, information, knowledge, records and archives management, '
             'noting that the field is mostly studied at postgraduate level. It states one rung only, the threshold, twice: for honours (4.5 to 4.8, with 4.6 defining a third as some proficiency in most attributes) '
             'and for master\'s and other postgraduate awards (4.9 to 4.12); it names typical standards in 1.1 but lists none, and leaves classes above the threshold to Annex D (4.2). '
             'Its five cross-cutting themes are equality, diversity and inclusion; accessibility; education for sustainable development (with the UN goals); employability, enterprise and entrepreneurship; and generative AI. '
             'It names CILIP, the Archives and Records Association, IFLA, the Information and Records Management Society and the Equality and Human Rights Commission, '
             'and cites the FHEQ and FQHEIS levels in 2.4 and 2.7.'),
    authority='reference: a sector-owned reference point, not a regulatory requirement; not a sector-recognised standard in England, part of quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter)')

S2 = dict(governs='what graduates in librarianship, information, knowledge, records and archives management know, understand and can do at the end of honours and postgraduate study, and the nature of courses in the field',
          awards=[HON, "master's", 'postgraduate diploma', 'postgraduate certificate'],
          levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
          statedScope='"The Subject Benchmark Statement for Librarianship, Information, Knowledge, Records and Archives Management sets out threshold and typical standards for bachelor\'s degrees with honours, postgraduate certificates, postgraduate diplomas and master\'s degrees." (D1, 1.1)',
          statedSubjects=[dict(name='Librarianship, Information, Knowledge, Records and Archives Management', locator='(D1, title; 1.1)', kind='subject',
                               codes=[dict(scheme='hecos', code='100913', label='librarianship'),
                                      dict(scheme='hecos', code='100915', label='archives and records management'),
                                      dict(scheme='hecos', code='100370', label='information management'),
                                      dict(scheme='hecos', code='100916', label='information services')])])

# =============================================================== S3
SECTIONS = {'1': 'Context and purposes of a Librarianship, Information, Knowledge, Records and Archives Management degree',
            '2': 'Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context'),
       ('1.2', '1.3', 'Purposes of a Librarianship, Information, Knowledge, Records and Archives Management degree'),
       ('1.4', '1.6', 'Characteristics of a Librarianship, Information, Knowledge, Records and Archives Management degree'),
       ('1.7', '1.10', 'Equality, diversity and inclusion'), ('1.11', '1.11', 'Accessibility and the needs of disabled students'),
       ('1.12', '1.14', 'Education for sustainable development'), ('1.15', '1.19', 'Employability, enterprise and entrepreneurship education'),
       ('1.20', '1.21', 'Generative artificial intelligence'),
       ('2.1', '2.3', 'Design'), ('2.4', '2.8', 'Progression'), ('2.9', '2.12', 'Flexibility'), ('2.13', '2.15', 'Partnership'),
       ('2.16', '2.20', 'Monitoring and review'),
       ('3.1', '3.2', 'Content'), ('3.3', '3.8', 'Teaching and learning'), ('3.9', '3.11', 'Assessment'),
       ('4.1', '4.4', 'Introduction'), ('4.5', '4.6', 'Threshold level'), ('4.7', '4.7', 'Subject knowledge, understanding and skills'),
       ('4.8', '4.8', 'Generic skills'), ('4.9', '4.10', "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"),
       ('4.11', '4.11', "Subject knowledge, understanding and skills (master's)"), ('4.12', '4.12', "Generic skills (master's)")]
G = {
    '1.1': 'what the statement covers; awards; joint courses vary',
    '1.2': 'aim: preparing students for information careers',
    '1.3': 'areas courses are likely to address, under seven headings',
    '1.4': 'usual features of degrees in the field',
    '1.5': 'varied teaching; courses set their own outcomes',
    '1.6': 'varied assessment; clear policies; formative and summative',
    '1.7': 'the disciplines and equitable access to information',
    '1.8': 'information services, needs and information architecture',
    '1.9': 'cultural competence and care for historic material',
    '1.10': 'fair access at the heart of professional ethics',
    '1.11': 'accessible courses and attention to varied student needs',
    '1.12': 'the field and the UN sustainable development goals',
    '1.13': 'recorded knowledge and heritage as sustainability',
    '1.14': 'sustainable management of information; sector initiatives',
    '1.15': 'employability education and career destinations',
    '1.16': 'entrepreneurship education beyond employment',
    '1.17': 'practice-based courses and authentic assessment',
    '1.18': 'enterprise skills and the professional skills base',
    '1.19': 'enterprise at the core of the subject',
    '1.20': 'generative AI: ethical questions and literacies',
    '1.21': 'preparing students to use AI ethically in services',
    '2.1': 'ethical, theoretical and legal foundations; careers',
    '2.2': 'vocational and academic; many routes in',
    '2.3': 'information as the object of study; reflection',
    '2.4': 'progression through the levels to the threshold',
    '2.5': 'readiness for postgraduate study',
    '2.6': 'joint and combined honours routes',
    '2.7': 'exit awards below honours',
    '2.8': 'continuing development and professional recognition',
    '2.9': 'flexible teaching; part-time and mature students',
    '2.10': 'modes of study, credit and micro-credentials',
    '2.11': 'course lengths across the UK nations',
    '2.12': 'part-time credit in proportion to study',
    '2.13': 'varied careers; learning tied to society',
    '2.14': 'placements and workplace projects',
    '2.15': 'accreditation and engaging with professional bodies',
    '2.16': 'monitoring and periodic review',
    '2.17': 'the student voice in monitoring',
    '2.18': 'external reviewers in periodic review',
    '2.19': 'external examiners and threshold standards',
    '2.20': 'professional accreditation of courses',
    '3.1': 'a broad, interdisciplinary subject',
    '3.2': 'content gives a broad, relevant base',
    '3.3': 'modes of teaching; theory and practice',
    '3.4': 'forms of teaching to suit learners',
    '3.5': 'partnership with professional practice',
    '3.6': 'support for independent learning',
    '3.7': 'evidence-based practice and research training',
    '3.8': 'continuing development and lifelong learning',
    '3.9': 'why varied assessment matters',
    '3.10': 'authentic assignments; what assessment will include',
    '3.11': 'feedback and self-directed learning',
    '4.1': 'threshold standards for honours defined',
    '4.2': 'most exceed threshold; Annex D for classes',
    '4.3': 'published criteria and feedback',
    '4.4': 'not competence standards; equality guidance',
    '4.5': 'honours threshold: core knowledge and application',
    '4.6': 'third class: some proficiency in most attributes',
    '4.7': 'honours subject knowledge and skills list',
    '4.8': 'honours generic skills list',
    '4.9': "the postgraduate standard: advanced concepts",
    '4.10': "master's knowledge, application and options",
    '4.11': "master's threshold and subject skills list",
    '4.12': "master's generic skills list",
}
CTYPE = {'1.3': 'area', '1.4': 'area', '3.1': 'area', '3.2': 'area',
         '1.5': 'practice', '1.6': 'practice', '1.17': 'practice', '3.3': 'practice', '3.4': 'practice', '3.5': 'practice', '3.6': 'practice',
         '3.7': 'practice', '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice',
         '4.5': 'stem', '4.7': 'stem', '4.8': 'stem', '4.9': 'stem', '4.11': 'stem', '4.12': 'stem'}
EXCLUDED = [dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
                 kind='other: front matter, read for S1 and S2'),
            dict(number='none', heading='section heading lines (sections 1 to 4)', kind='other: headings, recorded in S3 as sections'),
            dict(number='5', heading='List of references and further resources', kind='other: references, read for SB5, SB6 and D3'),
            dict(number='6', heading='Membership of the Advisory Group', kind='other: membership lists, read for S8 and supersedes')]

# =============================================================== S5 to S7
S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.4 (undergraduate degree with honours)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.4'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.4 (integrated master's); the level of 4.9 to 4.12 is inferred from the awards named (Part E)"),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.4'),
                  dict(id='fheq:4', role='cites', locator='D1, 2.7 (Certificate of Higher Education)'),
                  dict(id='fheq:5', role='cites', locator='D1, 2.7 (Diploma of Higher Education)'),
                  dict(id='fqheis:8', role='cites', locator='D1, 2.7, set beside the CertHE (Part E)'),
                  dict(id='fqheis:9', role='cites', locator='D1, 2.7, set beside the DipHE (Part E)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.4); agrees with FHEQ Table 1'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.4); agrees with FHEQ Table 1'),
                      dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.7); conflicts with FHEQ Table 1, which places the CertHE at fqheis:7 (Part E)'),
                      dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.7); conflicts with FHEQ Table 1, which places the DipHE at fqheis:8 (Part E)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.3', '1.4', '1.7', '1.8', '1.9', '1.10', '2.2']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.3', '1.4', '1.11', '2.9', '3.9']),
      dict(id='theme:esd', role='carries', carriedIn=['1.3', '1.4', '1.12', '1.13', '1.14', '1.20']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.3', '1.15', '1.16', '1.17', '1.18', '1.19', '3.10']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.3', '1.20', '1.21', '3.10'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-librarianship-information-knowledge-records-and-archives-management-<previous year>-benchmarks (not yet ingested)',
           note='the front matter names key changes from the previous statement; section 6 names a 2019 minor update (Part E)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree outcome classification descriptions for bachelor\'s degrees with honours (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 4 to 7 (2.4, 2.7)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 8 to 11 (2.4, 2.7)'),
      dict(rel='refersTo', target='QAA guidance on inclusive subject learning communities (not yet ingested)', note='1.11'),
      dict(rel='refersTo', target='CILIP Professional Knowledge and Skills Base (not yet ingested)', note='1.18, 2.15'),
      dict(rel='refersTo', target='CILIP Ethical Framework; ARA Code of Ethics (not yet ingested)', note='1.21, 2.1'),
      dict(rel='refersTo', target='ARA Competency Framework (not yet ingested)', note='2.15'),
      dict(rel='themeReference', target='theme:esd', note='the UN Sustainable Development Goals, six named (1.12)')]

# =============================================================== SB1 to SB6
SB1 = ['A family of related disciplines concerned with representing, organising and communicating knowledge so that anyone can find, use, judge and share the information they need (D1, 1.7)',
       'Practice-based and vocational as well as academic, with many entering through postgraduate study; the field is mostly studied at postgraduate level (D1, front matter; 1.17; 2.2)',
       'Information itself is the object of study, so students turn a critical eye on their own use of it and on how sources change (D1, 2.3)',
       'Rests on distinctive ethical foundations set out by the professional bodies and on long-standing law, such as copyright, equalities, data protection and freedom of information (D1, 2.1)',
       'Social justice runs through it: tackling bias in collections and systems, decolonising practice and working for fair access for groups once marginalised (D1, 1.4; 1.9; 1.10)',
       'Combines theory with practice through case studies, problem-based learning, placements and partnerships with the profession (D1, 1.4; 2.14; 3.5)',
       'Technologically fluent: metadata, repositories, user experience, data and, increasingly, AI tools, always with ethical oversight (D1, 1.3; 1.4; 1.21)',
       'Careers span libraries in many sectors, archives and records work, curation, information governance and knowledge management (D1, 2.1; 2.13)']
SB2 = [dict(theme='theme:edi', inThisSubject='Fair, unbiased access is the ethical core of the field: graduates work against bias in collections and knowledge systems, decolonise practice and serve marginalised groups (D1, 1.7 to 1.10)',
            statements=['4.7.b1', '4.7.b2', '4.7.b3', '4.7.b4', '4.7.b5', '4.11.b2', '4.11.b3', '4.11.b4', '4.11.b5']),
       dict(theme='theme:accessibility', inThisSubject='Accessibility is both how courses are run (varied, flexible, inclusive methods) and what graduates build (accessible systems, spaces and interfaces) (D1, 1.11; 2.9; 3.9)',
            statements=['4.7.b2', '4.7.b3', '4.7.b11', '4.7.b12', '4.11.b3', '4.11.b11', '4.11.b12']),
       dict(theme='theme:esd', inThisSubject='Preserving and giving access to recorded knowledge and heritage is itself a contribution to sustainability, with the UN goals and sector initiatives named (D1, 1.12 to 1.14)',
            statements=['4.8.b17', '4.7.b7', '4.11.b6', '4.11.b8']),
       dict(theme='theme:enterprise', inThisSubject='Enterprise is treated as core: service design, innovation and practical action, with authentic assessment and the professional skills base behind it (D1, 1.15 to 1.19)',
            statements=['4.11.b18', '4.11.b19', '3.10.b3']),
       dict(theme='theme:generative-ai', inThisSubject='AI is both a subject of critical, ethical study and a set of tools for metadata, discovery and services; students learn to use it and to teach others about it (D1, 1.20; 1.21)',
            statements=['4.7.b18', '4.11.b20', '3.10.b5'])]
SB3 = dict(areas=[dict(component='1.3', gloss='seven areas courses are likely to address: safeguarding knowledge and records; the digital landscape; literacies; information equity; innovation; information rights; strategic thinking'),
                  dict(component='1.4', gloss='usual characteristics: interdisciplinarity, law and ethics, data ethics, theory with practice, user experience, social justice, technical fluency, lifelong learning'),
                  dict(component='3.1', gloss='breadth and depth vary by course and specialism'),
                  dict(component='3.2', gloss='the content gives every graduate a broad, relevant base')],
           practices=[dict(component='1.5', kind='teaching', gloss='varied teaching; each course sets its own outcomes'),
                      dict(component='3.3', kind='teaching', gloss='face-to-face, distance, hybrid and blended teaching'),
                      dict(component='3.4', kind='teaching', gloss='lectures, seminars, case studies, projects and workplace learning'),
                      dict(component='3.5', kind='teaching', gloss='engagement with the profession: visits, guest lectures, work experience'),
                      dict(component='3.6', kind='learning', gloss='independent learning and self-development'),
                      dict(component='3.7', kind='learning', gloss='research training towards a research project'),
                      dict(component='3.8', kind='learning', gloss='continuing professional development and lifelong learning'),
                      dict(component='1.6', kind='assessment', gloss='clear assessment policies; formative and summative assessment'),
                      dict(component='1.17', kind='assessment', gloss='authentic tasks: reports, policy, projects, reflective practice'),
                      dict(component='3.9', kind='assessment', gloss='varied, inclusive and accessible assessment'),
                      dict(component='3.10', kind='assessment', gloss='authentic assignments and the six kinds assessment will include'),
                      dict(component='3.11', kind='assessment', gloss='tutor and peer feedback; giving and receiving feedback')])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=44),
                  dict(rung='threshold', leadIn='4.11', award="master's (with postgraduate certificate and diploma)", items=43),
                  dict(rung='typical', leadIn='none', award=HON, items=0)],
           rungBases=('Threshold only, stated twice: honours (4.5, 4.6, 4.7, 4.8; 4.6 defines the third class as some proficiency in most attributes) '
                      'and postgraduate (4.9, 4.10, 4.11, 4.12; 4.11 repeats the definition at master\'s). 1.1 says typical standards are set out and 4.1 that the threshold, shown over time, '
                      'shows typical achievement, but no typical or excellent list is given; classes above the threshold are left to Annex D (4.2). '
                      'Rung counts: honours 44 (4.5.s1, 4.5.s2, 4.5.b1 to b3, 4.6, 4.7.b1 to b21, 4.8.b1 to b17); postgraduate 43 (4.9.b1 to b4, 4.10.s1, 4.10.s2, 4.11.s1, 4.11.b1 to b25, 4.12.b1 to b4 and b6 to b12).'),
           outcomeLists=[dict(leadIn='3.10', gloss='what assessment will include', items=6, award=['honours', 'postgraduate'])],
           outcomes=[])
SB4A_FULL = []
SB5 = [dict(body='Chartered Institute of Library and Information Professionals (CILIP)',
            says='its diversity and inclusion principles, Green Libraries Manifesto, Ethical Framework, AI Hub and Professional Knowledge and Skills Base are named; it accredits courses, with professional registration and Chartership as later recognition (D1, 1.10; 1.14; 1.18; 1.21; 2.1; 2.8; 2.15)',
            requirements='not yet ingested (Part E)'),
       dict(body='Archives and Records Association (ARA)',
            says='its diversity principles, Environmental Sustainability Group, Code of Ethics, Professional Development Programme and Competency Framework are named; it accredits courses and offers professional registration (D1, 1.10; 1.14; 2.1; 2.8; 2.15)',
            requirements='not yet ingested (Part E)'),
       dict(body="International Federation of Library Associations and Institutions (IFLA)",
            says='its Environment, Sustainability and Libraries Section shows sustainability as a professional concern (D1, 1.14)',
            requirements='not-applicable-by-design: named as evidence of a concern, not for requirements'),
       dict(body='The Information and Records Management Society (IRMS)',
            says='its accreditation programme is one route to vocational recognition (D1, 2.8)',
            requirements='not yet ingested (Part E)'),
       dict(body='Equality and Human Rights Commission',
            says='providers setting competence standards should follow its latest guidance (D1, 4.4)',
            requirements='not-applicable-by-design: guidance, not course requirements'),
       dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed',
            says='courses with professional outcomes may need their accreditation, usually through site visits and desk review every few years; competence standards may draw on their requirements (D1, 2.20; 4.4)',
            requirements='not-applicable-by-design: generic reference')]
SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (the front matter says "equity, diversity, and inclusion")', carriedIn=['1.3', '1.4', '1.7', '1.8', '1.9', '1.10', '2.2'],
                        statements=['4.7.b1', '4.7.b2', '4.7.b3', '4.7.b4', '4.7.b5', '4.11.b2', '4.11.b3', '4.11.b4', '4.11.b5']),
                   dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=['1.3', '1.4', '1.11', '2.9', '3.9'],
                        statements=['4.7.b2', '4.7.b3', '4.7.b11', '4.7.b12', '4.11.b3', '4.11.b11', '4.11.b12']),
                   dict(id='theme:esd', named='Education for sustainable development', carriedIn=['1.3', '1.4', '1.12', '1.13', '1.14', '1.20'],
                        statements=['4.8.b17']),
                   dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education', carriedIn=['1.3', '1.15', '1.16', '1.17', '1.18', '1.19', '3.10'],
                        statements=['4.11.b18', '4.11.b19', '3.10.b3']),
                   dict(id='theme:generative-ai', named='Generative artificial intelligence', carriedIn=['1.3', '1.20', '1.21', '3.10'],
                        statements=['4.7.b18', '4.11.b20', '3.10.b5'])],
           frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.4', '2.7', '4.2']),
                       dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.4', '2.7'])],
           bodies=[dict(body='CILIP', citedIn=['1.10', '1.14', '1.18', '1.21', '2.1', '2.8', '2.15']),
                   dict(body='Archives and Records Association (ARA)', citedIn=['1.10', '1.14', '2.1', '2.8', '2.15']),
                   dict(body='IFLA', citedIn=['1.14']),
                   dict(body='Information and Records Management Society (IRMS)', citedIn=['2.8']),
                   dict(body='Equality and Human Rights Commission', citedIn=['4.4']),
                   dict(body='PSRBs (unnamed)', citedIn=['2.20', '4.4'])],
           sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies',
                                 citedIn=['4.2'], role='how classes above the threshold are described'),
                            dict(document='not yet ingested: listed in Part E', named='QAA guidance on the creation of inclusive subject learning communities',
                                 citedIn=['1.11'], role='a reference for inclusive course development'),
                            dict(document='this statement (as a Subject Benchmark Statement)', named='Subject Benchmark Statements',
                                 citedIn=['2.16', '2.19'], role='an external reference point for review and for external examiners')])

# =============================================================== Part B
B1 = [dict(slug='formative-and-summative-assessment', definition='assessment given as feedback on progress, set against assessment mainly for credit, progression and classification (D1, 1.6)',
           beneficiaryDefinition='tasks that help you improve, and tasks that count towards your marks', scopeNote='departments explain the relation between the two (1.6)', category='unknown', practices=['education']),
      dict(slug='information-architecture', definition='the framework and standards within which information products, services and systems are made, analysed and judged for their users (D1, 1.8)',
           beneficiaryDefinition='how information and systems are organised so people can use them', scopeNote='set within effective information provision (1.8)', category='unknown', practices=['information-management']),
      dict(slug='monitoring-and-evaluation', definition='periodic assessment of a course, internal or external, using current and past monitoring data (D1, 2.16)',
           beneficiaryDefinition='how your course is checked and improved over time', scopeNote='with the student voice central (2.17)', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the standard a student will have shown when awarded the degree; at honours a third, with some proficiency in most attributes (D1, 4.1; 4.6; 4.11)',
           beneficiaryDefinition='the minimum you need to show for your award', scopeNote='not a competence standard (4.4)', category='unknown', practices=['education'])]
B2A = [dict(concept='formative-and-summative-assessment', form='formative and summative assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='information-architecture', form='information architecture', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='monitoring-and-evaluation', form='monitoring and evaluation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold level of attainment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []
B5 = []

D3 = [dict(citation='CILIP, The Professional Knowledge and Skills Base', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation="CILIP's Ethical Framework", settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='Archives and Records Association, Professional Registration Programme: Competency Framework', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA, Creating Inclusive Subject Communities', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted')]

E = [
    'S4, rungs: one rung only, the threshold, stated for two awards (honours 4.5 to 4.8; postgraduate 4.9 to 4.12). 1.1 says the statement sets out "threshold and typical standards" but no typical list exists; SB4 records typical with no lead-in and 0 items. No excellent rung. Unlike Psychology.',
    "S4, master's: a separate master's section (4.9 to 4.12) covering postgraduate certificates, diplomas and master's degrees, with its own paragraph numbers, so no `.masters` id suffix was needed; level fheq:7 is inferred from the awards, not stated in section 4 (2.4 names FHEQ 7 only for the integrated master's).",
    'S4, threshold reading: 4.6 and 4.11 define threshold as "some degree of proficiency in the majority of the attributes", so no single list item is a pass condition; every aad says so. For Abbott: whether list items should carry force `threshold` instead of the lead-in modal.',
    'S4, force: the honours lists take "should be able to" (4.5, 4.7, 4.8); the master\'s subject list takes "will have demonstrated" from 4.11\'s first sentence (forceFrom 4.11), while its lead-in also says the attributes "may be understood as some or all of the ability to"; 4.12 takes "should".',
    'S4, force: 4.9\'s lead-in has no modal ("the standard of achievement expected of all students"); its four items are recorded with force `describes`. For Abbott: does "expected" read as `should`?',
    'S4, 4.10.s3 ("students may also be asked to demonstrate" strategic thinking, leadership and original research) is recorded as an expectation with force `may`, rung none: an option, not a threshold item.',
    'S4, cuts: 2.3, 4.5, 4.10 and 4.11 are cut into sentence records (.s1, .s2, .s3) where a stem or paragraph carries its own obligation; 4.12.b5 ("a conceptual understanding that enables them to:") is a stem, not a record, and its two sub-items are 4.12.b6 and 4.12.b7 (skeleton ids kept).',
    'S4, skeleton correction: 4.7.b21 and 4.11.b25 ran on into the next sub-heading ("Generic skills"); both are recut with `find` to end at the item.',
    'S4, not taken: 1.3\'s 26 bullets ("degrees ... are likely to address the following areas") are content areas, recorded in S3 and SB3, though 4.7 and 4.11 repeat most of them nearly word for word as outcomes.',
    'S4, not taken (plain-present provider norms, template open point 5): 1.4\'s eight characteristics ("typically include"), 1.5, 1.6 ("departments ... develop clear assessment policies"), 1.11 (accessible courses), 1.21, 3.5 to 3.8, 4.3 ("Published criteria and grade descriptors are available").',
    'S4, not taken (obliging words outside the five, or descriptive "will"): 2.4 ("it is expected that each level would see ..."), 2.5 ("it would be expected that a student ... would be capable of" postgraduate study), 2.8, 2.14, 2.15 ("encouraged"), 2.19 (external examiners "will be asked", introduced by "Typically"), 1.9 (practitioners "are able to"), 1.19 ("Graduates are reflective, proactive and positive"). For Abbott at P3.',
    'S4, 2.7 ("may exit earlier and be eligible for" a CertHE or DipHE) is a permission, not taken as a statement; its level citations are recorded in S5 and SB6.',
    'S4, 3.10: the six assessment items are recorded as expectations (force will, from "These will include assessments which:") with addressee both, since the student meets them as tasks; for Abbott whether they are provider duties (student version not applicable).',
    'S5, crosswalk conflict: 2.7 places the CertHE at "FHEQ Level 4; FQHEIS Level 8" and the DipHE at "FHEQ Level 5; FQHEIS Level 9"; FHEQ Table 1 (std:doc:qaa-fheq-2024-framework, S5) places them at fqheis:7 and fqheis:8. Recorded as stated; for P3.',
    "SB4, cross-award pairs (not gradeOf: a different award, not a rung): 18 honours items in 4.7 recur in 4.11 almost unchanged (4.7.b3 to b5 and b7 to b21 with 4.11.b3 to b5, b6, b7, b9 to b17 and b20 to b23); each aaw sets the pair beside each other. 4.11 adds disaster preparedness (b8), experimentation (b18), entrepreneurship (b19) and strategic leadership (b24, b25), all drawn from 1.3.",
    "S4, 4.12: its items restate the FHEQ's master's descriptor closely (4.12.b1 with qaa/fheq-2024/4.17.b2; b2 and b3 with 4.17.b3; b6 and b7 with 4.17.b4; b8 with 4.17.b5; b9 with 4.17.b6). Recorded as the benchmark's own statements; each aaw points to the FHEQ item.",
    'S4, verbs: 4.12.b2, b9 and b10 are noun phrases with no verb of their own (their lead-in verb "demonstrate" is outside the span); verbs left empty.',
    'Subjects: no HESA code is stated. 100913 librarianship and 100915 archives and records management are recorded as stated because the title names them; 100370 information management, 100916 information services and CAH24-01-01 are inferred. Knowledge management has no HECoS code of its own. For P3.',
    'Title: the issuer writes "Archives Management" in the title and sections 1 and 3 but "Archive Management" in sections 2 and 4 and the advisory group lists; 2.13 also says "Library, Information ...". Recorded as given; the document title follows the cover.',
    'SB6: the front matter calls the first theme "equity, diversity, and inclusion"; the section heading says "Equality, diversity and inclusion". One theme id, theme:edi.',
    'SB6, not recorded as bodies: the UN Sustainable Development Goals (1.12; carried under theme:esd and S7), the Lifelong Learning Entitlement (2.10) and the Equality Act 2010 (4.4: legislation, not a body). The QAA Quality Code and Glossary are named only in the excluded front matter; QAA Enterprise and Entrepreneurship Education only in the references list.',
    'SB6, sharedDocuments: QAA guidance on inclusive subject learning communities (1.11) is not yet ingested (D3).',
    'Pattern: section 4\'s honours threshold lead-in (4.5) is followed by a separate paragraph (4.6) defining the third class, and the subject list (4.7) repeats 1.3\'s content areas as outcomes; Psychology had no such duplication.',
    'Frameworks consulted: std:doc:qaa-fheq-2024-framework (S5, SL1 to SL7, 4.15, 4.17, Annex D), std:doc:qaa-fqheis-2024-framework (S5), std:doc:welsh-government-cqfw-2009-framework (S5; not cited by the statement) and std:ref:uk-framework (R2, R3, R8). The framework ids in each aaw are our readings (inferred).',
]
