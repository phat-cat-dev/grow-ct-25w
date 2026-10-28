import json,glob,collections,re,os
B='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/stan/core/qaa/benchmarks/'
exec(open('rb_analyse.py').read().split("docs={}")[0])
C={ # concept: (strand, regex)
 'subject knowledge and understanding':('K',r'knowledge|understand'),
 'theories, concepts and debates':('K',r'theor|concept|debate|paradigm'),
 'history, context and currency of the field':('K',r'histor|context|contemporary|current'),
 'critical evaluation of evidence and arguments':('C',r'critical|evaluat|assess (the|evidence|argument)|argument'),
 'analysis and problem-solving':('C',r'analys|problem'),
 'research and enquiry methods':('A',r'research|enquiry|inquiry|investigat|method'),
 'data, numbers and quantitative reasoning':('A',r'\bdata\b|quantitative|numer|statistic'),
 'applying knowledge to practice or problems':('A',r'\bappl(y|ication)|practi(c|s)e|practical'),
 'information and sources':('A',r'source|literature|information|retriev'),
 'digital skills':('A',r'digital|software|technolog|computational'),
 'written communication':('M',r'writ|written|report|essay'),
 'oral or other communication to audiences':('M',r'communicat|present|audience|oral'),
 'teamwork and collaboration':('M',r'team|collaborat|group work|others'),
 'independent and self-directed learning':('R',r'independen|self-direct|autonom|own learning'),
 'reflection and personal development':('R',r'reflect|personal development|self-aware'),
 'ethics, integrity and values':('R',r'ethic|integrity|values|responsib'),
 'professional practice and employability':('R',r'professional|employab|career|workplace|vocational'),
 'equality, diversity and inclusion':('R',r'diversity|inclusi|equalit|equity'),
 'sustainability':('R',r'sustainab|environmental'),
 'enterprise and creativity':('A',r'enterpris|entrepreneur|creativ|innovat'),
}
docs=collections.defaultdict(lambda: collections.defaultdict(set))
nd=collections.Counter()
for f in sorted(glob.glob(B+'*.chunks.json')):
    slug=os.path.basename(f).replace('.chunks.json',''); s=sec4(f); cur='threshold'; seen=set()
    for line in s.split('\n'):
        mm=list(re.finditer(r'(Threshold|Typical|Excellent|Very good)',line))
        if not line.startswith('•') and mm: cur=mm[-1].group(1).lower()
        if line.startswith('•'):
            seen.add(cur); l=line.lower()
            for k,(st,rx) in C.items():
                if re.search(rx,l): docs[cur][k].add(slug)
    for r in seen: nd[r]+=1
print(nd)
out={}
for r in ('threshold','typical','excellent'):
    out[r]={k:sorted(v) for k,v in docs[r].items()}
    print('==',r,nd[r]); 
    for k,(st,rx) in C.items(): print(f'  {st} {k}: {len(docs[r].get(k,()))}')
json.dump({'n':nd,'docs':out,'concepts':{k:v[0] for k,v in C.items()}},open('rb_concepts.json','w'),indent=0)
