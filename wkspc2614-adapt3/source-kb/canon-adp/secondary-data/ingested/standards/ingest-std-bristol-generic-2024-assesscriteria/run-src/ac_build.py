#!/usr/bin/env python3
"""Generic builder for `standards/assessment-criteria` documents (profile 0.1.6-draft P5a). std. Used by runs 0050 (Bristol) and 0051 (Cardiff Met)."""
import json, re, collections, hashlib
import ac_terms as A
q = lambda s: json.dumps(s, ensure_ascii=False)
FH = '/home/claude/wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt'
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'

def fheq_echoes():
    """FHEQ statements (descriptor items and Annex D cells) with their spans, for echo detection."""
    norm = open(FH, encoding='utf-8').read()
    out = []
    sk = json.load(open(S + '/fheq-skel.json'))
    for x in sk['items']:
        if not x.get('stem'): out.append(('qaa/fheq-2024/' + x['id'], norm[x['span']['start']:x['span']['end']]))
    for c in json.load(open(S + '/fheq2-annexd.json'))['cells']:
        out.append(('qaa/fheq-2024/' + c['id'], norm[c['span'][0]:c['span'][1]]))
    cq = open('/home/claude/wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.norm.txt', encoding='utf-8').read()
    for x in json.load(open(S + '/cqfw-skel.json'))['statements']:
        if x['column'] != 'summary': out.append(('welsh-government/cqfw-2009/' + x['id'], cq[x['span']['start']:x['span']['end']]))
    return out

W = lambda s: re.findall(r"[a-z0-9']+", s.lower().replace('‐', '-').replace('’', "'").replace('- ', '-'))
def echo(text, FE, n=7):
    """longest run of >= n words shared with an FHEQ statement; returns (id, run) or None."""
    w = W(text); best = None
    for sid, st in FE:
        sw = W(st); G = {tuple(sw[i:i + n]) for i in range(len(sw) - n + 1)}
        hit = [i for i in range(len(w) - n + 1) if tuple(w[i:i + n]) in G]
        if hit:
            # extend the first hit greedily
            i = hit[0]; j = i + n; s = ' '.join(sw)
            while j < len(w) and ' '.join(w[i:j + 1]) in s: j += 1
            if not best or j - i > best[2]: best = (sid, ' '.join(w[i:j]), j - i)
    return best

def terms(text, T):
    vb = []
    for lem, form in A.verbs(text):
        tx = T.get(lem) or T.get(lem.replace('ise', 'ize')) or []
        vb.append({'lemma': lem, 'form': form, 'taxonomy': [f'{s}:{"/".join(c)}' for s, c in tx] or ['none']})
    return {'verbs': vb, 'objects': A.find(text, A.OBJECTS), 'degree': A.find(text, A.DEGREE, 'degree'), 'independence': A.find(text, A.INDEP), 'scope': A.find(text, A.SCOPE), 'deficits': A.find(text, A.DEFICIT, 'deficits')}

def lexicon(cells):
    L = {k: collections.defaultdict(lambda: {'n': 0, 'levels': set(), 'bands': collections.Counter()}) for k in ('verbs', 'degree', 'independence', 'scope', 'deficits', 'objects')}
    for c in cells:
        for k in L:
            items = [v['lemma'] for v in c['terms'][k]] if k == 'verbs' else c['terms'][k]
            for it in items:
                e = L[k][it]; e['n'] += 1; e['levels'].add(c['level']); e['bands'][c['bandpos']] += 1
    return L

def ladder(cells, bandorder, kinds=('degree', 'independence')):
    """each term's mean band position (0 = lowest band) over the cells it appears in; n >= 3."""
    out = []
    for k in kinds:
        acc = collections.defaultdict(list)
        for c in cells:
            for t in c['terms'][k]: acc[t].append(bandorder(c))
        for t, xs in acc.items():
            if len(xs) >= 3: out.append((sum(xs) / len(xs), t, k, len(xs)))
    return sorted(out)
