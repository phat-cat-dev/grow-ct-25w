# AC6 terms analysis: lexicons and a parser shared by every assessment-criteria run. std.
import re, collections
RUNS = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/runs'
# 1 performance verbs: lemma -> surface forms (nominalisations included, recorded as such)
VERBS = {
 'demonstrate': ['demonstrate', 'demonstrates', 'demonstrated', 'demonstrating', 'demonstration'],
 'interpret': ['interpret', 'interprets', 'interpreted', 'interpreting', 'interpretation', 'interpretations'],
 'comment': ['comment', 'comments', 'commented', 'commenting'],
 'evaluate': ['evaluate', 'evaluates', 'evaluated', 'evaluating', 'evaluation', 'evaluations'],
 'use': ['use', 'uses', 'used', 'using'],
 'develop': ['develop', 'develops', 'developed', 'developing', 'development'],
 'make': ['make', 'makes', 'making'],
 'recognise': ['recognise', 'recognises', 'recognising', 'recognition'],
 'apply': ['apply', 'applies', 'applied', 'applying', 'application'],
 'collect': ['collect', 'collects', 'collecting'],
 'undertake': ['undertake', 'undertakes', 'undertaking'],
 'complete': ['complete', 'completes', 'completed', 'completing'],
 'identify': ['identify', 'identifies', 'identifying'],
 'isolate': ['isolate', 'isolates'],
 'deploy': ['deploy', 'deploys', 'deploying'],
 'draw on': ['draw on', 'draws on', 'drawing on'],
 'select': ['select', 'selects', 'selected', 'selecting', 'selection'],
 'consider': ['consider', 'considers', 'considering', 'consideration'],
 'synthesise': ['synthesise', 'synthesises', 'synthesising', 'synthesis'],
 'integrate': ['integrate', 'integrates', 'integrating'],
 'explain': ['explain', 'explains', 'explanation', 'explanations'],
 'devise': ['devise', 'devises'],
 'sustain': ['sustain', 'sustains', 'sustained'],
 'create': ['create', 'creates', 'creation'],
 'critique': ['critique', 'critiques'],
 'reflect': ['reflect', 'reflects', 'reflection', 'self-reflection', 'reflecting'],
 'assess': ['assess', 'assesses', 'assessing'],
 'plan': ['plan', 'plans', 'planning'],
 'implement': ['implement', 'implements'],
 'provide': ['provide', 'provides'],
 'work': ['works', 'working', 'work with', 'work within', 'work and lead', 'work without', 'work autonomously'],
 'contribute': ['contribute', 'contributes', 'contributions'],
 'lead': ['lead', 'leads', 'leading'],
 'organise': ['organise', 'organises'],
 'manage': ['manage', 'manages', 'managing'],
 'communicate': ['communicate', 'communicates', 'communicating'],
 'adapt': ['adapt', 'adapts', 'adapting', 'adapted'],
 'decide': ['decide', 'decides', 'decisions', 'decision-making'],
 'conduct': ['conduct', 'conducts', 'conducted'],
 'produce': ['produce', 'produces', 'produced'],
 'reproduce': ['reproduce', 'reproduces', 'reproducing'],
 'acknowledge': ['acknowledge', 'acknowledging'],
 'address': ['address', 'addressing'],
 'meet': ['meet', 'met'],
 'set': ['setting'],
 'express': ['express', 'expressing'],
 'present': ['present', 'presenting', 'presentation'],
 'argue': ['argue', 'argued', 'argues'],
 'solve': ['solve', 'solving', 'solution', 'solutions', 'problem-solving'],
 'understand': ['understand', 'understands'],
 'challenge': ['challenge', 'challenged'],
 'extend': ['extend', 'extends'],
 'transform': ['transform'],
 'describe': ['describe', 'describing', 'description', 'descriptive'],
 'report': ['report', 'reporting'],
 'review': ['review'],
}
# 2 objects
OBJECTS = ['knowledge and understanding', 'knowledge', 'understanding', 'directed and independent reading', 'directed reading', 'independent reading', 'reading', 'primary sources', 'set sources', 'sources', 'basic theories and concepts', 'theories', 'concepts', 'well-established principles', 'principles', 'knowledge base', 'introductory material', 'introductory knowledge', 'material', 'field of study', 'field', 'discipline', 'complex problems', 'problems', 'approaches', 'methods of enquiry', 'foundational skills', 'specialist skills', 'advanced techniques', 'techniques', 'data', 'information', 'research tasks', 'research literature', 'research', 'scholarship', 'academic conventions', 'academic skills', 'academic honesty', 'literature', 'lines of argument', 'arguments', 'alternative perspectives', 'perspectives', 'views', 'complex matters and ideas', 'ideas', 'team', 'conflict', 'strengths and weaknesses', 'self-development', 'goals', 'feedback', 'audiences', 'media', 'deadlines', 'tasks', 'circumstances', 'forefront', 'current problems', 'contemporary issues', 'limitations', 'set task', 'learning outcomes', 'assessment criteria', 'referencing', 'research processes', 'own practice', 'presentation', 'structure', 'qualitative and quantitative data', 'theory and practice']
# 3 degree, ordered low to high as a provisional ladder (the set's own order is read from the bands)
DEGREE = ['very inadequate', 'inadequate', 'very limited', 'very little', 'limited', 'little', 'minimal', 'poor', 'some', 'basic', 'sufficient', 'adequate', 'generally', 'sound', 'secure', 'satisfactory', 'clear', 'clearly', 'good', 'well', 'very good', 'consistent', 'consistently', 'effective', 'effectively', 'successfully', 'successful', 'capable', 'informed', 'strong', 'thorough', 'thoroughly', 'detailed', 'comprehensive', 'comprehensively', 'confident', 'confidently', 'confidence', 'high', 'highly', 'high-level', 'perceptive', 'perceptively', 'excellent', 'nuanced', 'assured', 'sophisticated', 'accomplished', 'innovative', 'authoritative', 'outstanding', 'exceptional', 'exceptionally', 'mastery']
# 4 independence and scope
INDEP = ['even with guidance', 'with external guidance', 'with limited external guidance', 'with limited guidance', 'with minimum guidance', 'with very limited guidance', 'without extensive guidance', 'without substantial guidance', 'with a degree of autonomy', 'with a significant degree of autonomy', 'with a high degree of autonomy', 'with autonomy', 'autonomously', 'autonomous', 'autonomy', 'initiative', 'independent thinking', 'independent', 'reliance on tutor support', 'setting own goals', 'tutor support']
SCOPE = ['introductory', 'foundational', 'basic', 'at this level', 'well-established', 'main', 'key', 'specialised', 'specialist', 'advanced', 'complex', 'unfamiliar', 'non-routine', 'well-defined', 'forefront', 'beyond what has been taught', 'beyond the set range', 'sometimes beyond the set range', 'usually beyond the set range', 'a range of', 'wide range', 'broad range', 'systematic', 'in-depth', 'straightforward', 'reasonably straightforward', 'current', 'contemporary', 'original', 'originality', 'beyond level']
# 5 negations and deficits
DEFICIT = ['no', 'not', 'none', 'lacking', 'lacks', 'lack', 'without', 'major gaps', 'gaps', 'deficiencies', 'inaccuracies', 'weakly', 'weak', 'weaknesses', 'flaws', 'lapses', 'ignored', 'over-reliance', 'reliance', 'superficial', 'inconsistencies', 'inconsistent', 'inconsistently', 'poorly', 'unsubstantiated', 'unsubstantiate d', 'irrelevant', 'flawed', 'insufficient', 'errors', 'misconceptions', 'unaddressed', 'negligible', 'absent', 'failure', 'naive', 'naïve', 'simplistic', 'unconvincing', 'clumsy', 'confused']
def norm(t): return ' ' + ' '.join(t.lower().replace('‐', '-').replace('’', "'").replace('- ', '-').split()) + ' '
MASK = {'deficits': ['strengths and weaknesses', 'strengths or weaknesses'], 'degree': ['basic theories and concepts', 'basic theories', 'basic concepts']}
def find(t, terms, kind=None):
    n = norm(t)
    for m in MASK.get(kind, []): n = n.replace(m, '#' * len(m))
    hits = []
    for term in sorted(terms, key=len, reverse=True):
        for m in re.finditer(r'(?<![a-z\-])' + re.escape(term) + r'(?![a-z\-])', n):
            if any(m.start() < e and s < m.end() for s, e, _ in hits): continue
            hits.append((m.start(), m.end(), term))
    return [h[2] for h in sorted(hits)]
def verbs(t):
    n = norm(t); out = []
    for lem, forms in VERBS.items():
        for f in forms:
            if re.search(r'(?<![a-z\-])' + re.escape(f) + r'(?![a-z\-])', n): out.append((lem, f)); break
    return out
def taxonomy():
    """verb -> placements from the INGEST theory documents (revised Bloom; SOLO)."""
    T = collections.defaultdict(list)
    for doc, short in (('ingest-theory-revised-bloom-taxonomy-anderson-krathwohl-2001.md', 'bloom-r'), ('ingest-theory-solo-biggs-collis-1982.md', 'solo')):
        for line in open(f'{RUNS}/{doc}', encoding='utf-8'):
            m = re.match(r'- \{ concept: ([^,]+), form: ([^,]+), frameworkBlocks: \[(.*)', line)
            if not m: continue
            comps = re.findall(r'component: ([a-z\-]+)', m.group(3))
            T[m.group(2).strip().lower()].append((short, sorted(set(comps))))
    return T
