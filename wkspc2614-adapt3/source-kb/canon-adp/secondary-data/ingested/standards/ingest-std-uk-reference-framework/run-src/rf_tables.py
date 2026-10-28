import json,re,collections
R=json.load(open('rf_recs.json'))
DUB={'knowledge-and-understanding':'K','applying-knowledge':'A','making-judgements':'C','communication':'M','learning-skills':'R'}
for r in R:
    if r['src']=='dublin' and r['dim'] in DUB: r['strand']=DUB[r['dim']]
STEPS=['entry-2','entry-3','1','2','3','4','5','6','7','8']
SRC=['cqfw','fheq','fqheis','dublin']; AB={'cqfw':'C','fheq':'F','fqheis':'Q','dublin':'D'}
ST={'K':'Knowledge and understanding','C':'Thinking and judgement','A':'Application and enquiry','M':'Communication','R':'Autonomy, responsibility and learning'}
LEX={
 'context':['simple','familiar','routine','well-defined','straightforward','non-routine','complex','unfamiliar','unpredictable','specialised','abstract','ill-defined','undefined','new'],
 'depth':['basic','underlying','well-established','established','coherent','detailed','systematic','comprehensive','critical','critically','in-depth','advanced','forefront','current','original','originality','new knowledge'],
 'independence':['guidance','direction','supervision','autonomy','autonomously','independent','independently','initiative','personal responsibility','self-direction','leadership','lead'],
}
def has(t,w): return re.search(r'\b'+re.escape(w)+r'\b',t.lower()) is not None
out={}
# lexicon presence: term -> step -> set(src)
lex={g:{w:{s:set() for s in STEPS} for w in ws} for g,ws in LEX.items()}
for r in R:
    for g,ws in LEX.items():
        for w in ws:
            if has(r['text'],w): lex[g][w][r['step']].add(AB[r['src']])
out['lex']={g:{w:{s:''.join(sorted(v)) for s,v in d.items()} for w,d in ws.items()} for g,ws in lex.items()}
# verbs by step x strand: per source
vb={}
for r in R:
    for v in r['verbs']:
        vb.setdefault((r['step'],r['strand']),collections.defaultdict(set))[v].add(AB[r['src']])
out['verbs']={f'{k[0]}|{k[1]}':{v:''.join(sorted(s)) for v,s in d.items()} for k,d in vb.items()}
# counts
out['counts']={f'{s}|{st}':{src:sum(1 for r in R if r['step']==s and r['strand']==st and r['src']==src) for src in SRC} for s in STEPS for st in ST}
# first verb ladder across steps per strand: verbs in >=2 sources
json.dump(out,open('rf_tables.json','w'),indent=0)
# print summaries
for st in ST:
    print('==',ST[st])
    for s in STEPS:
        d=vb.get((s,st),{})
        common=[v for v,ss in d.items() if len(ss)>=2]
        print(f' {s}: n={sum(out["counts"][f"{s}|{st}"].values())} common={common} all={len(d)}')
for g in LEX:
    print('##',g)
    for w,d in out['lex'][g].items():
        row=[f'{s}:{d[s]}' for s in STEPS if d[s]]
        if row: print(' ',w,' '.join(row))
