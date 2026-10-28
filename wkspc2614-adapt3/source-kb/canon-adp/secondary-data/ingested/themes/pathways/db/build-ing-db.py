#!/usr/bin/env python3
"""Compile the pathway cores' terminology and cards into one SQLite database.

A working compilation for ing (ing N-0118), never a record: rebuild it from the
cores whenever they change. Reads every `pathways/ingest-path-*.md` and the card
vocabulary; writes `ing-pathways.sqlite` beside this script.

Usage: python3 build-ing-db.py
"""
import json, os, re, sqlite3, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ING = os.path.dirname(HERE)
CORES = os.path.join(ING, 'pathways')
VOCAB = os.path.join(ING, 'integrations', 'cards', 'ing-card-vocabulary.json')
VIC = os.path.join(ING, 'integrations', 'cards', 'verbs-in-context.json')
DB = os.path.join(HERE, 'ing-pathways.sqlite')

SCHEMA = """
CREATE TABLE pathway (id TEXT PRIMARY KEY, doc_id TEXT, title TEXT, version TEXT, file TEXT);
CREATE TABLE concept (pathway TEXT, slug TEXT, kind TEXT, parent TEXT, ord TEXT, name TEXT, definition TEXT, category TEXT, section TEXT,
  PRIMARY KEY (pathway, slug));
CREATE TABLE term (pathway TEXT, concept TEXT, form TEXT, list TEXT, term_status TEXT, part_of_speech TEXT, register TEXT, status TEXT);
CREATE TABLE term_block (pathway TEXT, concept TEXT, form TEXT, component TEXT, sources TEXT, weight TEXT);
CREATE TABLE framework_block (pathway TEXT, concept TEXT, component TEXT, definition_here TEXT, use_here TEXT);
CREATE TABLE relation (pathway TEXT, rel TEXT, from_slug TEXT, to_slug TEXT, note TEXT, section TEXT);
CREATE TABLE theory_relation (pathway TEXT, rel TEXT, target TEXT, note TEXT);
CREATE TABLE search_term (pathway TEXT, term TEXT, kind TEXT);
CREATE TABLE card (id TEXT PRIMARY KEY, pathway TEXT, tier TEXT, statement TEXT, origin TEXT, benchmark_hits TEXT);
CREATE TABLE card_word (card TEXT, word TEXT, kind TEXT);
CREATE TABLE card_theory (card TEXT, theory TEXT);
CREATE TABLE card_process (card TEXT, process TEXT);
CREATE TABLE card_framework (card TEXT, framework TEXT, equivalence TEXT);
CREATE TABLE verb_in_context (verb TEXT, statement TEXT, statement_type TEXT, source TEXT, subject TEXT, hecos TEXT, pathway TEXT, card TEXT, read_as TEXT, relation TEXT);
CREATE VIEW concept_hierarchy AS
  SELECT pathway, slug AS child, parent, 'part-of (A3)' AS how FROM concept WHERE parent IS NOT NULL AND parent <> 'none'
  UNION ALL
  SELECT pathway, from_slug, to_slug, rel FROM relation WHERE rel IN ('narrower', 'part-of');
CREATE VIEW term_across_pathways AS
  SELECT lower(form) AS form, count(DISTINCT pathway) AS pathways, group_concat(DISTINCT pathway) AS which
  FROM (SELECT pathway, form FROM term UNION SELECT pathway, term FROM search_term)
  GROUP BY lower(form) HAVING count(DISTINCT pathway) > 1;
"""


def sections(text):
    """Map each '## ' or '### ' heading (first token, e.g. 'A3', 'B2a') to its body."""
    out = {}
    parts = re.split(r'\n(?=#{2,3} )', text)
    for p in parts:
        m = re.match(r'#{2,3} (\S+)', p)
        if m:
            out[m.group(1)] = p
    return out


def yaml_blocks(body):
    return [yaml.safe_load(b) for b in re.findall(r'```yaml\n(.*?)```', body, re.S)]


def s(v):
    if v is None:
        return None
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def main():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    counts = {}
    for fn in sorted(os.listdir(CORES)):
        if not fn.startswith('ingest-path-') or not fn.endswith('.md'):
            continue
        text = open(os.path.join(CORES, fn), encoding='utf-8').read()
        fm = yaml.safe_load(text.split('---')[1])
        sec = sections(text)
        a10 = next((b for b in yaml_blocks(sec.get('A10', '')) if isinstance(b, dict) and 'pathway' in b), None)
        pid = a10['pathway']['id'].replace('path:', '') if a10 else fn[len('ingest-path-'):-3]
        con.execute('INSERT INTO pathway VALUES (?,?,?,?,?)', (pid, fm['id'], fm['title'], str(fm['version']), fn))
        # A3 components
        for b in yaml_blocks(sec.get('A3', '')):
            for c in (b or {}).get('components', []):
                con.execute('INSERT OR REPLACE INTO concept VALUES (?,?,?,?,?,?,?,?,?)',
                            (pid, c['slug'], c.get('componentType'), s(c.get('parent')), s(c.get('order')), c.get('name'),
                             c.get('gloss'), 'tier' if c.get('componentType') == 'level' else 'capability', 'A3'))
        # A4 concepts: '- slug: definition'
        for m in re.finditer(r'^- ([a-z0-9-]+): (.+)$', sec.get('A4', ''), re.M):
            con.execute('INSERT OR IGNORE INTO concept VALUES (?,?,?,?,?,?,?,?,?)',
                        (pid, m.group(1), 'concept', None, None, m.group(1), m.group(2), 'concept', 'A4'))
        # B1 exceptions
        for b in yaml_blocks(sec.get('B1', '')):
            for c in b or []:
                con.execute('INSERT OR REPLACE INTO concept VALUES (?,?,?,?,?,?,?,?,?)',
                            (pid, c['slug'], 'concept', None, None, c['slug'], c.get('definition'), c.get('category'), 'B1'))
        # B2a named terms
        for b in yaml_blocks(sec.get('B2a', '')):
            for t in b or []:
                con.execute('INSERT INTO term VALUES (?,?,?,?,?,?,?,?)',
                            (pid, t.get('concept'), s(t.get('form')), 'B2a', t.get('termStatus'), t.get('partOfSpeech'), t.get('register'), 'named'))
        # B2b associated vocabulary
        for b in yaml_blocks(sec.get('B2b', '')):
            for t in b or []:
                con.execute('INSERT INTO term VALUES (?,?,?,?,?,?,?,?)',
                            (pid, t.get('concept'), s(t.get('form')), 'B2b', None, None, None, t.get('status')))
                for fb in t.get('frameworkBlocks', []) or []:
                    con.execute('INSERT INTO term_block VALUES (?,?,?,?,?,?)',
                                (pid, t.get('concept'), s(t.get('form')), fb.get('component'), s(fb.get('sources')), s(fb.get('weight'))))
        # B3 framework blocks
        for b in yaml_blocks(sec.get('B3', '')):
            for f in b or []:
                con.execute('INSERT INTO framework_block VALUES (?,?,?,?,?)',
                            (pid, f.get('concept'), f.get('component'), f.get('definitionHere'), f.get('useHere')))
        # B4 relations
        for b in yaml_blocks(sec.get('B4', '')):
            for r in b or []:
                con.execute('INSERT INTO relation VALUES (?,?,?,?,?,?)',
                            (pid, r.get('rel'), r.get('from'), r.get('to'), r.get('note'), 'B4'))
        # A9 theory relations
        for b in yaml_blocks(sec.get('A9', '')):
            for r in b or []:
                con.execute('INSERT INTO theory_relation VALUES (?,?,?,?)', (pid, r.get('rel'), s(r.get('target')), r.get('note')))
        # A10 terms and cards
        if a10:
            terms = a10['pathway'].get('terms', {}) or {}
            for kind in ('direct', 'associated'):
                for t in terms.get(kind, []) or []:
                    con.execute('INSERT INTO search_term VALUES (?,?,?)', (pid, s(t), kind))
            for c in a10['pathway'].get('competencies', []) or []:
                con.execute('INSERT OR REPLACE INTO card (id, pathway, tier, statement, origin) VALUES (?,?,?,?,?)',
                            (c['id'], pid, s(c.get('tierNote')), c.get('statement'), 'core A10'))
                for th in c.get('theory', []) or []:
                    con.execute('INSERT INTO card_theory VALUES (?,?)', (c['id'], s(th)))
                for pr in c.get('process', []) or []:
                    con.execute('INSERT INTO card_process VALUES (?,?)', (c['id'], s(pr)))
                for pf in c.get('professional', []) or []:
                    for fw in pf.get('frameworks', []) or []:
                        con.execute('INSERT INTO card_framework VALUES (?,?,?)', (c['id'], fw, pf.get('equivalence')))
    # card vocabulary (all 88 cards, including the three pathways drafted after it)
    if os.path.exists(VOCAB):
        v = json.load(open(VOCAB, encoding='utf-8'))
        for c in v['cards']:
            con.execute('INSERT OR IGNORE INTO card (id, pathway, tier, statement, origin) VALUES (?,?,?,?,?)',
                        (c['id'], c['pathway'], s(c['tier']), c['statement'], 'card vocabulary'))
            con.execute('UPDATE card SET benchmark_hits = ? WHERE id = ?', (c.get('benchmarkHits'), c['id']))
            for kind, key in (('verb', 'verbs'), ('measure', 'measures'), ('keyword', 'keywords')):
                for w in c.get(key, []):
                    con.execute('INSERT INTO card_word VALUES (?,?,?)', (c['id'], w, kind))
            # D-ing-0058: every verb with the statement it is used in
            for w in c.get('verbs', []):
                con.execute('INSERT INTO verb_in_context VALUES (?,?,?,?,?,?,?,?,?,?)',
                            (w, c['statement'], 'capability statement', c['id'], 'any (generic pathway model)', None, c['pathway'], c['id'], 'skill', 'the card itself'))
    if os.path.exists(VIC):
        for r in json.load(open(VIC, encoding='utf-8'))['records']:
            for w in r['verbs']:
                con.execute('INSERT INTO verb_in_context VALUES (?,?,?,?,?,?,?,?,?,?)',
                            (w, r['statement'], r['statementType'], r['source'], r['subject'], r.get('hecos'), r['pathway'], r.get('card'), r.get('readAs'), r.get('relation')))
    con.commit()
    for t in ('pathway', 'concept', 'term', 'term_block', 'framework_block', 'relation', 'theory_relation',
              'search_term', 'card', 'card_word', 'card_theory', 'card_process', 'card_framework', 'verb_in_context'):
        counts[t] = con.execute(f'SELECT count(*) FROM {t}').fetchone()[0]
    con.close()
    for t, n in counts.items():
        print(f'{t}\t{n}')
    if counts['pathway'] == 0 or counts['term'] == 0:
        print('FAIL: no subjects reached', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
