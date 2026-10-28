import json,glob,collections,re,os
B='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/stan/core/qaa/benchmarks/'
src=open('rb_analyse.py').read()
exec(src.split("docs={}")[0])
Q=['basic','some','sound','good','very good','excellent','exceptional','outstanding','critical','critically','sophisticated','independent','independently','originality','original','creative','extensive','in-depth','deep','detailed','comprehensive','systematic','coherent','advanced','complex','confident','reflective','ethical','professional','sustainable','sustainability','employability','enterprise','digital','inclusive','diversity']
qr=collections.defaultdict(collections.Counter); ir=collections.Counter()
themes=collections.Counter(); sec1=collections.Counter()
TH={'edi':r'equality, diversity and inclusion','accessibility':r'^accessibility','sustainability':r'^(education for )?sustainab','enterprise':r'^enterprise and entrepreneurship'}
for f in sorted(glob.glob(B+'*.chunks.json')):
    s=sec4(f); cur='threshold'
    t=open(f.replace('.chunks.json','.norm.txt')).read()
    for k,p in TH.items():
        if re.search(p,t,re.I|re.M): themes[k]+=1
    for line in s.split('\n'):
        mm=list(re.finditer(r'(Threshold|Typical|Excellent|Very good)',line))
        if not line.startswith('•') and mm: cur=mm[-1].group(1).lower()
        if line.startswith('•'):
            ir[cur]+=1; l=line.lower()
            for q in Q:
                if re.search(r'\b'+re.escape(q)+r'\b',l): qr[cur][q]+=1
print('themes',themes)
for r in ('threshold','typical','excellent'):
    n=ir[r]; print(r,n,[(q,qr[r][q],round(100*qr[r][q]/n,1)) for q in Q if qr[r][q]])
json.dump({'themes':themes,'items':ir,'qual':{r:dict(qr[r]) for r in qr}},open('rb_more.json','w'))
