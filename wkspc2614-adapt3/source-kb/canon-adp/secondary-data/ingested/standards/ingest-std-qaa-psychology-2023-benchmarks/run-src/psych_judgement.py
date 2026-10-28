# Judgement fields for run 0043, QAA Psychology 2023 (std). Keys are S4 ids under qaa/psychology-2023/.
# Each: type, rung, force, level, appliesTo, addressee, verbs, about, domain, award, paraphrase, prac, ben (text or ('n/a', reason)), gradeOf
HON = "bachelor's with honours"
CONV = "master's conversion"
BOTH = [HON, CONV]

P = {}
def s(i, **k): P[i] = k

# ---- obliging or outcome paragraphs (sections 1 to 4)
s('1.6', type='requirement', rung='none', force='must', level='none', appliesTo='anyone seeking to practise as a psychologist',
  addressee='learner', verbs=['registered', 'completed'], about='protected practitioner psychologist titles', domain='none', award='none',
  para="Practising as a psychologist needs postgraduate study and supervised training beyond the degree; by law anyone using one of the nine protected practitioner titles must be on the HCPC register and have finished an HCPC-approved training course.",
  prac="An undergraduate or conversion degree does not by itself lead to a protected title: anyone using one of the nine practitioner psychologist titles (Health Professions Order 2001) must be an HCPC registrant who has completed approved training.",
  ben="If you want to work as a practitioner psychologist (clinical, forensic, educational and others), you must first complete further postgraduate study and supervised training and register with the professional regulator: the titles are protected by law.")
s('1.18', type='expectation', rung='none', force='will', level='none', appliesTo='graduates of the subject',
  addressee='learner', verbs=['value', 'incorporate'], about='equality, diversity and inclusion in personal and professional life', domain='generic-skill', award='none',
  para="Equality is advanced by learning, teaching and assessment that widen opportunity, remove discrimination and question inaccurate accounts of people; graduates are expected to value equality, diversity and inclusion and carry them into their lives and work.",
  prac="Learning, teaching and assessment that widen opportunity and challenge biased narratives in the discipline are the means; the expected result is that graduates will value equality, diversity and inclusion and act on them in their personal and professional lives.",
  ben="You will come to value equality, diversity and inclusion and build them into how you live and work, helping to make society fairer.")
s('1.24', type='requirement', rung='none', force='must', level='none', appliesTo='course design and the wider student experience',
  addressee='provider', verbs=['considered', 'anticipated'], about='anticipating accessibility for disabled students', domain='none', award='none',
  para="The Equality Act 2010 requires providers to anticipate the accessibility needs of disabled students across teaching, learning, assessment and student life, and accessibility must be considered when courses are designed.",
  prac="Build accessibility in from the start: under the Equality Act 2010 you must consider disabled students' needs when designing the course and planning the wider student experience, not only when an adjustment is asked for.",
  ben=('n/a', 'a duty on the provider; the student meets its effect, not a standard to reach'))
s('2.5', type='outcome', rung='none', force='will', level='none', appliesTo='students of the subject',
  addressee='learner', verbs=['apply', 'evaluating'], about='ethical understanding and behaviour', domain='subject-skill', award='none',
  para="Ethics sits at the core of the discipline and of course design, with activities that apply it to research, practice and daily conduct; students will be able to apply ethics to their own behaviour and judge the ethical conduct of others critically.",
  prac="Ethics is often at the heart of course design, with activities that bring it into research, practice and daily life; students will be able to act ethically themselves and critically judge the ethics of others.",
  ben="You will be able to apply ethical principles to how you behave in research, in practice and day to day, and to judge critically how ethically others act.")
s('2.8', type='requirement', rung='none', force='must', level='none', appliesTo='students seeking Graduate Basis for Chartered Membership',
  addressee='learner', verbs=['gain', 'pass'], about='the professional body route to chartered membership', domain='none', award=HON,
  para="A second-class degree or above usually fits a graduate for postgraduate study; to gain the professional body's Graduate Basis for Chartered Membership, a student must achieve at least a second-class degree and pass the empirical project, or pass an accredited conversion course at 50% or equivalent.",
  prac="For the BPS Graduate Basis for Chartered Membership, students must gain at least a second-class degree and pass the empirical project, or pass an accredited conversion course at 50% (a merit or equivalent).",
  ben="If you want the first step towards chartered membership of the professional body, you must achieve at least a second-class degree and pass your empirical project on an accredited course, or pass an accredited conversion course with 50% or more.")
s('3.11', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
  addressee='learner', verbs=['completed', 'culminating', 'reporting'], about='research reports and the empirical project', domain='subject-skill', award=HON,
  para="Graduates will have written a series of research reports through the course, ending in an empirical project (or equivalent) that reports a substantial piece of research collecting original data or using an accepted alternative such as modelling or secondary analysis.",
  prac="Graduates will have completed a sequence of research reports leading to a substantial empirical project in which each collects original quantitative, qualitative or mixed data, or uses an accepted alternative such as computational modelling or secondary data analysis.",
  ben="You will write a series of research reports during your studies, leading up to a substantial project of your own in which you gather and report original data, or work with an accepted alternative such as existing datasets or computer models.")

# ---- 3.16 subject-specific skills (lead-in: on graduating with honours or a conversion course, students are able to)
L316 = dict(rung='none', force='will', level='fheq:6', appliesTo='honours and conversion graduates', addressee='learner', award=BOTH)
def k316(i, **k): s('3.16.b%d' % i, type='outcome', **L316, **k)
k316(1, verbs=['understand'], about='conceptual and historical foundations', domain='understanding',
  para="Understand the ideas and history on which psychology as a discipline rests.",
  prac="Graduates understand the conceptual and historical foundations of psychology as a discipline.",
  ben="You will understand the ideas and history that psychology is built on.")
k316(2, verbs=['apply', 'recognising'], about='multiple perspectives on psychological issues', domain='subject-skill',
  para="Bring several perspectives to bear on psychological questions, aware that the discipline uses many methods, theories, kinds of evidence, readings and applications.",
  prac="Graduates apply more than one perspective to psychological issues and recognise the range of methods, theories, evidence, interpretations and applications the discipline uses.",
  ben="You will be able to look at psychological questions from several angles, knowing that psychology uses many methods, theories, kinds of evidence and ways of applying them.")
k316(3, verbs=['integrate', 'apply'], about='integrating findings and applying knowledge ethically', domain='subject-skill',
  para="Bring together ideas and findings from different approaches, and use psychological knowledge on real problems in ways that are ethical, professional and safe.",
  prac="Graduates integrate ideas and findings across approaches and apply psychological knowledge to real-world problems ethically, professionally and safely.",
  ben="You will be able to combine ideas and findings from different approaches and use what you know about psychology on real problems, ethically, professionally and safely.")
k316(4, verbs=['identify', 'contextualise', 'evaluate'], about='patterns in behaviour and experience', domain='subject-skill',
  para="Recognise, place in context and judge the varied patterns found in behaviour, mental functioning and experience.",
  prac="Graduates identify, contextualise and evaluate the diversity of patterns in behaviour, psychological functioning and experience.",
  ben="You will be able to spot, put in context and assess the many patterns in how people behave, think and experience the world.")
k316(5, verbs=['apply', 'address', 'identifying'], about='critical thinking for complex problems', domain='subject-skill',
  para="Use critical thinking on complex problems to find creative and innovative answers.",
  prac="Graduates apply critical thinking to complex problems and reach creative, innovative solutions.",
  ben="You will be able to think critically about complex problems and come up with creative, new solutions.")
k316(6, verbs=['generate', 'explore', 'design', 'collect'], about='hypotheses, research questions and original data', domain='subject-skill',
  para="Form and examine suitable hypotheses and research questions grounded in theory, research and practice, then design studies and gather original data.",
  prac="Graduates generate and explore hypotheses and research questions grounded in existing theory, studies and practice, then design their own studies and gather new data.",
  ben="You will be able to form your own hypotheses and research questions from theory, research and practice, then design studies and gather new data.")
k316(7, verbs=['apply'], about='a range of methods of inquiry', domain='subject-skill',
  para="Use varied methods of inquiry, from experiments and observation to interviews and focus groups, questionnaires and psychometric testing, creative approaches or analysis of existing data.",
  prac="Graduates apply a range of inquiry methods, experimental and observational, survey and psychometric, interview and focus group, creative, and secondary analysis.",
  ben="You will be able to use many research methods, such as experiments, observation, questionnaires, tests, interviews, focus groups, creative methods or existing datasets.")
k316(8, verbs=['understand', 'appreciate'], about='participatory, action and peer research', domain='understanding',
  para="Understand and value participatory or action research, the involvement of users, and community and peer research.",
  prac="Graduates understand and value participatory and action research, user involvement, and community and peer research.",
  ben="You will understand why research done with people, not only on them, matters: participatory and action research, and research led by users, communities and peers.")
k316(9, verbs=['analyse', 'present', 'evaluate', 'critique'], about='analysing data and critiquing findings', domain='subject-skill',
  para="Analyse, present and assess quantitative, qualitative and mixed-methods data, and critique the findings of research.",
  prac="Graduates analyse, present and evaluate quantitative, qualitative and mixed-methods data and critique research findings.",
  ben="You will be able to analyse, present and assess numerical, qualitative and mixed data, and question what research findings show.")
k316(10, verbs=['manage', 'synthesise', 'evaluate'], about='handling conflicting sources', domain='subject-skill',
  para="Manage, combine and judge sources that may conflict, such as primary studies or rival theories.",
  prac="Graduates manage, synthesise and evaluate sources that may conflict, such as primary studies or competing theories.",
  ben="You will be able to handle, combine and weigh up sources that disagree, such as different studies or theories.")
k316(11, verbs=['employ', 'examine'], about='evidence-based reasoning and the issues of inquiry', domain='subject-skill',
  para="Reason from evidence and examine the practical, theoretical and ethical questions raised by methods of inquiry and other activities.",
  prac="Graduates reason from evidence and examine the practical, theoretical and ethical issues that methods of inquiry and related activities raise.",
  ben="You will be able to reason from evidence and think through the practical, theoretical and ethical questions your research methods raise.")
k316(12, verbs=['use', 'critique'], about='psychological tools and instruments', domain='subject-skill',
  para="Use and critically assess psychological tools, such as specialist software, laboratory equipment and psychometric instruments.",
  prac="Graduates use and critique the tools of the discipline: specialist software, lab equipment and psychometric instruments.",
  ben="You will be able to use, and judge the limits of, the tools of psychology, such as specialist software, lab equipment and psychometric tests.")
k316(13, verbs=['evaluate'], about='critical evaluation of theory and research', domain='subject-skill',
  para="Assess psychological theory and research critically and reflectively.",
  prac="Graduates evaluate psychological theory and research critically and reflectively.",
  ben="You will be able to assess psychological theories and research critically and reflectively.")
k316(14, verbs=['understand', 'apply', 'developing'], about='theory development', domain='subject-skill',
  para="Understand how theory is developed, apply that process, and frame psychological questions driven by theory.",
  prac="Graduates understand and use the process of theory development and can frame theory-driven psychological questions.",
  ben="You will understand how theories are built and be able to ask psychological questions that grow out of theory.")
k316(15, verbs=['carry', 'demonstrate', 'designing', 'planning', 'resolving'], about='the independent empirical project', domain='subject-skill',
  para="Complete a substantial independent empirical study that shows, for each student, research skills from design and planning, through ethical questions, to analysis and dissemination.",
  prac="Each graduate completes an extensive independent empirical project demonstrating research skills across design, planning, ethics, analysis and dissemination.",
  ben="You will carry out a substantial research project of your own, showing that you can plan and design it, deal with its ethical questions, analyse the results and share what you found.")

# ---- 3.17 transferable skills (lead-in: on graduating with a degree, students are able to)
L317 = dict(rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=BOTH, domain='generic-skill')
def k317(i, **k): s('3.17.b%d' % i, type='outcome', **L317, **k)
k317(1, verbs=['communicate'], about='effective communication',
  para="Communicate well by verbal and non-verbal means.", prac="Graduates communicate effectively through a range of verbal and non-verbal means.",
  ben="You will be able to communicate well, in speech and in other ways.")
k317(2, verbs=['interact', 'respond'], about='professional and inclusive interaction',
  para="Deal with others professionally and respond inclusively, attentive to the needs and expectations of varied audiences.",
  prac="Graduates interact professionally and respond inclusively, sensitive to the needs and expectations of diverse audiences.",
  ben="You will be able to work with others professionally and respond inclusively to people with different needs and expectations.")
k317(3, verbs=['demonstrate'], about='numerical reasoning',
  para="Show numerical reasoning, including analysing, presenting and interpreting quantitative data.",
  prac="Graduates demonstrate numerical reasoning: analysing, presenting and interpreting quantitative data.",
  ben="You will be able to reason with numbers and analyse, present and interpret numerical data.")
k317(4, verbs=['demonstrate', 'analyse', 'interpret', 'present'], about='qualitative data skills',
  para="Show that one can analyse, interpret and present qualitative data.",
  prac="Graduates demonstrate that they can analyse, interpret and present qualitative data.",
  ben="You will be able to analyse, interpret and present qualitative data, such as interviews or text.")
k317(5, verbs=['demonstrate'], about='digital literacy',
  para="Show digital literacy by using online databases, analysis software and digital tools for personal and professional development.",
  prac="Graduates demonstrate digital literacy: online databases, analysis software and digital tools for their own personal and professional growth.",
  ben="You will be confident with digital tools: online databases, analysis software and digital ways of developing yourself personally and professionally.")
k317(6, verbs=['understand'], about='artificial intelligence in learning and work',
  para="Understand what artificial intelligence does and its role in learning, teaching, problem-solving and working practice.",
  prac="Graduates understand what artificial intelligence does and where it fits in learning and teaching, problem-solving and working practice.",
  ben="You will understand what artificial intelligence does and how it is used in learning, solving problems and at work.")
k317(7, verbs=['understand'], about='information ethics and handling',
  para="Understand the ethical, practical and legal questions in collecting, managing, storing, processing, sharing and presenting information, digital information included.",
  prac="Graduates understand the ethical, practical and legal issues across the life of information, from collection to presentation, including in digital formats.",
  ben="You will understand the ethical, practical and legal rules for collecting, storing, using and sharing information, including digital information.")
k317(8, verbs=['retrieve', 'organise', 'recognising'], about='finding information and recognising whose knowledge counts',
  para="Find and organise information from varied sources, academic and non-academic, while recognising the perspectives and influences that raise up or push aside some kinds of knowledge and evidence.",
  prac="Graduates retrieve and organise information from academic, policy and non-academic sources and recognise the influences that amplify or marginalise particular knowledge and evidence.",
  ben="You will be able to find and organise information from many kinds of sources and notice whose knowledge and evidence gets heard and whose gets left out.")
k317(9, verbs=['demonstrate', 'reflect'], about='inclusive collaboration and consensus',
  para="Work inclusively and collaboratively, and reflect on the worth of engaging with differing views when reaching agreed solutions.",
  prac="Graduates work inclusively and collaboratively and reflect on the value of engaging varied views when reaching consensus on solutions.",
  ben="You will be able to work inclusively with others and reflect on why hearing different views helps a group agree on solutions.")
k317(10, verbs=['reflect', 'articulate', 'identify'], about='self-assessment and development',
  para="Reflect on and explain one's own strengths and areas to develop, and how to address them.",
  prac="Graduates reflect on and articulate their strengths and development needs and identify how to address them.",
  ben="You will be able to reflect on and explain your own strengths and what you need to develop, and work out how to do it.")
k317(11, verbs=['take'], about='ownership of learning and employability',
  para="Take charge of one's own learning, employability and development, including personal planning and project management.",
  prac="Graduates take ownership of their learning, employability and development, including personal planning and project management.",
  ben="You will take charge of your own learning, career readiness and development, planning your time and managing projects well.")

s('4.5', type='requirement', rung='none', force='must', level='fheq:7', appliesTo='conversion courses', addressee='provider',
  verbs=['align'], about='conversion course outcomes and framework levels', domain='none', award=CONV,
  para="Assessments matched to learning outcomes let students reach the standard; the base classification corresponds to framework level 6 (FHEQ, outside Scotland) or level 10 (FQHEIS, Scotland); the standards guide conversion courses at FHEQ level 7 or FQHEIS level 11, whose outcomes must ultimately align with the right framework levels.",
  prac="These standards are a reference point for conversion courses, but a conversion course's outcomes must ultimately align with FHEQ level 7 or FQHEIS level 11.",
  ben=('n/a', 'a duty on the provider in setting outcome levels'))
s('4.13', type='requirement', rung='none', force='must', level='none', appliesTo='postgraduate courses', addressee='provider',
  verbs=['ensure', 'registered'], about='award titles and protected titles', domain='none', award="postgraduate",
  para="It matters that postgraduate award titles reflect achievement and the field studied truthfully; the course provider must make sure students know that HCPC-regulated professions have titles protected by law that only registrants may use.",
  prac="It matters that postgraduate titles reflect the field and level honestly; and the provider must make sure students know that HCPC-regulated psychology professions carry legally protected titles open only to registrants.",
  ben=('n/a', 'a duty on the provider; the student-facing point is in 1.6'))

# ---- rungs 4.8 threshold, 4.9 typical, 4.10 excellent
RUNG = {'threshold': '4.8', 'typical': '4.9', 'excellent': '4.10'}
def kr(rung, i, **k):
    s('%s.b%d' % (RUNG[rung], i), type=rung, rung=rung, force='will', level='fheq:6', appliesTo="graduates at the %s level" % rung,
      addressee='learner', award=HON, **k)
BL = {'threshold': 'To reach the threshold standard, ', 'typical': 'To reach the typical standard, ', 'excellent': 'To reach the excellent standard, '}

kr('threshold', 1, verbs=['identified'], about='core areas and their applications', domain='knowledge',
  para="Has named the core areas of psychology and the settings where each can be applied.",
  prac="At threshold, graduates have named the discipline's core areas and the settings where each applies.",
  ben=BL['threshold'] + "you will have identified the main areas of psychology and where each can be used.")
kr('threshold', 2, verbs=['reviewed', 'evaluated'], about='reviewing the literature', domain='subject-skill',
  para="Has reviewed and assessed the key psychological literature systematically.",
  prac="At threshold, graduates have systematically reviewed and evaluated the key literature.",
  ben=BL['threshold'] + "you will have worked through and assessed the key research writing in psychology in a systematic way.")
kr('threshold', 3, verbs=['understood', 'compared'], about='links between areas and perspectives', domain='understanding',
  para="Has understood how the areas of psychology relate and compared the perspectives within it.",
  prac="At threshold, graduates have understood how areas of psychology interrelate and compared perspectives within the discipline.",
  ben=BL['threshold'] + "you will understand how the areas of psychology connect and be able to compare its different perspectives.")
kr('threshold', 4, verbs=['appreciated'], about='the role of evidence', domain='understanding',
  para="Has grasped the part evidence plays in reaching conclusions in psychology.",
  prac="At threshold, graduates have appreciated the role of evidence in reaching conclusions.",
  ben=BL['threshold'] + "you will understand why evidence matters when drawing conclusions in psychology.")
kr('threshold', 5, verbs=['understood', 'applied'], about='research principles, protocols and guidelines', domain='subject-skill',
  para="Has understood the principles and protocols of psychological investigation and followed the relevant legal, ethical and professional guidance.",
  prac="At threshold, graduates have understood the principles and protocols of psychological investigation and applied legal, ethical and professional guidelines.",
  ben=BL['threshold'] + "you will know the rules and procedures for psychological research and have followed the legal, ethical and professional guidance that applies.")
kr('threshold', 6, verbs=['constructed', 'tested', 'undertaken'], about='hypotheses and supervised research', domain='subject-skill',
  para="Has formed and tested hypotheses and carried out supervised research on defined questions, alone and in groups.",
  prac="At threshold, graduates have constructed and tested hypotheses and undertaken supervised research, individually and in groups.",
  ben=BL['threshold'] + "you will have built and tested hypotheses and carried out supervised research on set questions, on your own and with others.")
kr('threshold', 7, verbs=['summarised', 'understood'], about='summarising findings from quantitative and qualitative methods', domain='subject-skill',
  para="Has summarised findings from quantitative and qualitative methods and understood what they add to knowledge.",
  prac="At threshold, graduates have summarised quantitative and qualitative findings and understood their contribution to knowledge.",
  ben=BL['threshold'] + "you will have summed up results from numerical and qualitative research and understood what they add to what we know.")
kr('threshold', 8, verbs=['used'], about='hardware and software for learning and research', domain='generic-skill',
  para="Has used suitable hardware and software for study and research.",
  prac="At threshold, graduates have used suitable equipment and software in their study and research.",
  ben=BL['threshold'] + "you will have used the right equipment and software for your study and research.")
kr('threshold', 9, verbs=['communicated'], about='communicating knowledge and findings', domain='generic-skill',
  para="Has conveyed psychological knowledge and findings in several formats.",
  prac="At threshold, graduates have communicated psychological knowledge and findings in a range of formats.",
  ben=BL['threshold'] + "you will have shared psychological knowledge and research findings in different formats.")

kr('typical', 1, verbs=['understood'], about='breadth of the discipline and its impact', domain='knowledge',
  para="Has understood how wide psychology is and how it can make a difference to many real problems.",
  prac="At the typical level, graduates have grasped how broad psychology is and how it can bear on many real-world challenges.",
  ben=BL['typical'] + "you will understand how broad psychology is and how it can help with many real-world problems.")
kr('typical', 2, verbs=['conducted', 'reflected', 'explored'], about='in-depth literature review and history of ideas', domain='subject-skill',
  para="Has reviewed the literature in depth, reflected on historical concepts and theories, and traced what they mean for thinking now.",
  prac="At the typical level, graduates have conducted in-depth literature reviews, reflected on historical concepts and theories, and explored their bearing on current thinking.",
  ben=BL['typical'] + "you will have reviewed research in depth, thought about older ideas and theories, and worked out what they mean for today.")
kr('typical', 3, verbs=['adopted', 'analysed'], about='multiple perspectives and research paradigms', domain='subject-skill',
  para="Has taken several perspectives and analysed research paradigms, methods and measures systematically.",
  prac="At the typical level, graduates have adopted multiple perspectives and systematically analysed paradigms, methods of enquiry and measurement techniques.",
  ben=BL['typical'] + "you will have looked at psychology from several viewpoints and analysed its research approaches, methods and measures carefully.")
kr('typical', 4, verbs=['reflected'], about='evidence and scientific reasoning', domain='understanding',
  para="Has reflected on how evidence supports conclusions and on scientific reasoning in psychology.",
  prac="At the typical level, graduates have reflected on the role of evidence and on scientific reasoning.",
  ben=BL['typical'] + "you will have thought carefully about how evidence supports conclusions and how to reason scientifically in psychology.")
kr('typical', 5, verbs=['posed', 'critiqued'], about='research questions and competence across methods', domain='subject-skill',
  para="Has set and critiqued research questions in a way that shows competence in many quantitative and qualitative methods.",
  prac="At the typical level, graduates have posed and critiqued research questions and shown competence across a wide range of quantitative and qualitative methods.",
  ben=BL['typical'] + "you will have set and questioned research questions and shown you can use many numerical and qualitative methods well.")
kr('typical', 6, verbs=['initiated', 'completed', 'recognising'], about='self-started enquiries and their limits', domain='subject-skill',
  para="Has started and finished psychological enquiries while recognising their theoretical, practical and methodological limits.",
  prac="At the typical level, graduates have initiated and completed enquiries, recognising their theoretical, practical and methodological limitations.",
  ben=BL['typical'] + "you will have started and finished your own research, aware of its theoretical, practical and method limits.")
kr('typical', 7, verbs=['drawn', 'evaluating', 'accounting', 'making'], about='conclusions, significance and further research', domain='subject-skill',
  para="Has drawn conclusions from findings, judging their psychological importance, allowing for the diversity of individual experience and proposing further research.",
  prac="At the typical level, graduates have drawn conclusions from findings, weighed their significance with regard to diverse individual experience, and recommended further investigation.",
  ben=BL['typical'] + "you will have drawn conclusions from your findings, judged how much they matter, taken account of how differently people experience things, and suggested what to study next.")
kr('typical', 8, verbs=['understood'], about='consequences of tools and theoretical choices', domain='understanding',
  para="Has understood what follows from using different subject hardware and software and from taking different theoretical positions.",
  prac="At the typical level, graduates have understood the implications of choosing different subject-relevant hardware and software and different theoretical perspectives.",
  ben=BL['typical'] + "you will understand how your choice of equipment, software and theory shapes your work.")
kr('typical', 9, verbs=['disseminated', 'tailoring'], about='communicating findings to different audiences', domain='generic-skill',
  para="Has shared research findings with peers and supervisors, adapting communication to what each audience needs.",
  prac="At the typical level, graduates have disseminated findings to peers and supervisors, tailoring communication to each audience.",
  ben=BL['typical'] + "you will have shared your research with fellow students and supervisors, adjusting how you communicate to suit each audience.")

kr('excellent', 1, verbs=['demonstrated', 'engage', 'pointing'], about='precise technical discussion of the discipline', domain='knowledge',
  para="Has consistently shown precise technical discussion of the nature of psychology, picking out possible misreadings.",
  prac="At the excellent level, graduates have consistently discussed the nature of psychology with technical precision and identified likely misinterpretations.",
  ben=BL['excellent'] + "you will have consistently discussed what psychology is with technical precision, pointing out where it is often misunderstood.")
kr('excellent', 2, verbs=['engaged', 'identified', 'challenging', 'offering'], about='original reviews and the limits of understanding', domain='subject-skill',
  para="Has consistently produced original theoretical and practical reviews, found where psychological understanding runs out, challenged myths and offered other readings.",
  prac="At the excellent level, graduates have consistently produced original theoretical and practical reviews, identified the limits of current understanding, challenged myths and offered alternative interpretations.",
  ben=BL['excellent'] + "you will have consistently written original reviews of what psychology knows, shown where that knowledge stops, challenged myths and offered other explanations.")
kr('excellent', 3, verbs=['interpreted', 'making', 'showing'], about='interpreting evidence across sub-specialisms', domain='subject-skill',
  para="Has consistently interpreted a wide range of evidence within and beyond psychology's sub-specialisms, making significant connections and applying knowledge comprehensively.",
  prac="At the excellent level, graduates have consistently interpreted evidence across sub-specialisms and related disciplines, made significant connections and applied knowledge comprehensively.",
  ben=BL['excellent'] + "you will have consistently made sense of wide-ranging evidence across areas of psychology and beyond, linking it in significant ways and applying it thoroughly.")
kr('excellent', 4, verbs=['demonstrated', 'evaluate', 'forming'], about='critical evaluation of evidence for novel conclusions', domain='subject-skill',
  para="Has consistently shown critical thinking and judged the rigour and weight of evidence in reaching new conclusions.",
  prac="At the excellent level, graduates have consistently shown critical thinking and evaluated the rigour and significance of evidence when reaching novel conclusions.",
  ben=BL['excellent'] + "you will have consistently thought critically, judging how strong and important evidence is when reaching new conclusions of your own.")
kr('excellent', 5, verbs=['articulated'], about='articulating complex arguments', domain='generic-skill',
  para="Has consistently expressed complex arguments and concepts clearly and even-handedly.",
  prac="At the excellent level, graduates have consistently articulated complex arguments and concepts coherently and in a balanced way.",
  ben=BL['excellent'] + "you will have consistently explained complex arguments and ideas clearly and fairly.")
kr('excellent', 6, verbs=['demonstrated', 'designing'], about='creative research design', domain='subject-skill',
  para="Has consistently designed research creatively, relevant to current psychological issues.",
  prac="At the excellent level, graduates have consistently shown creativity in designing research relevant to contemporary issues.",
  ben=BL['excellent'] + "you will have consistently designed creative research that speaks to current issues in psychology.")
kr('excellent', 7, verbs=['reflected', 'applied'], about='findings in social, political and ethical debate', domain='understanding',
  para="Has consistently reflected on what historical and current findings mean when brought to social, political and ethical debates and policy.",
  prac="At the excellent level, graduates have consistently weighed what past and present findings mean for social, political and ethical debate and policy.",
  ben=BL['excellent'] + "you will have consistently thought about what past and present findings mean for social, political and ethical debates and policies.")
kr('excellent', 8, verbs=['understood', 'gained'], about='personal, professional and employability skills', domain='generic-skill',
  para="Has consistently understood the value of personal and professional skills and acquired transferable employability skills, such as command of particular hardware and software and analytical ability.",
  prac="At the excellent level, graduates have consistently shown they value personal and professional skills and have built transferable employability skills, such as command of particular tools and strong analysis.",
  ben=BL['excellent'] + "you will have consistently shown that you value personal and professional skills and built skills employers want, such as mastery of particular tools and strong analysis.")
kr('excellent', 9, verbs=['imparted'], about='conveying a comprehensive grasp to varied audiences', domain='generic-skill',
  para="Has consistently conveyed to peers, tutors, supervisors and mixed audiences a full grasp of how psychology informs public debate and decisions.",
  prac="At the excellent level, graduates have consistently shown peers, staff and wider audiences a full command of how psychology informs public debate and decisions.",
  ben=BL['excellent'] + "you will have consistently shown fellow students, tutors and wider audiences a thorough grasp of how psychology shapes public debate and decisions.")

# gradeOf: same outcome at the rung below (inferred: the issuer lists each rung separately, by position)
GRADE = {}
for i in range(1, 10):
    GRADE['4.9.b%d' % i] = '4.8.b%d' % i
    GRADE['4.10.b%d' % i] = '4.9.b%d' % i
WEAK = {'4.9.b5', '4.10.b5', '4.10.b7', '4.10.b8'}  # content match less plain: listed in Part E
OUTCOMES = ['core areas and breadth', 'literature review', 'perspectives', 'evidence and reasoning', 'research questions and methods',
            'conducting research', 'findings and their significance', 'hardware, software and skills', 'communicating to audiences']


# ---- force-keeping pass (std, 03:35): outcome items keep "will" in paraphrase and practitioner version
import re as _re
for _i, _r in P.items():
    if _i.startswith(('3.16.', '3.17.')):
        _r['para'] = 'Will be able to ' + _r['para'][0].lower() + _r['para'][1:]
        _r['prac'] = _re.sub(r'^Graduates (?!will)', 'Graduates will ', _r['prac'])
        _r['prac'] = _r['prac'].replace('Each graduate completes', 'Each graduate will complete')
    if _r.get('rung') in ('threshold', 'typical', 'excellent'):
        _r['para'] = _re.sub(r'^Has consistently ', 'Will consistently have ', _r['para'])
        _r['para'] = _re.sub(r'^Has ', 'Will have ', _r['para'])
        _r['prac'] = _r['prac'].replace(', graduates have consistently ', ', graduates will consistently have ').replace(', graduates have ', ', graduates will have ')
