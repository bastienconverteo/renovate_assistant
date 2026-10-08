#!/usr/bin/env python3
"""One-shot migration of registers to schema v0.2 (2026-10-08). Kept for traceability; do not rerun.
- source paths -> SRC ids (new registers/sources.csv); evidence/status normalised to enums
- date_added + last_confirmed -> updated; topic + links columns added
- datapoints split: slim datapoints.csv + datapoint_defs.csv (definitions, quality rules)
- new registers: sources, questions, meetings"""
import csv, json, re, sys, collections
S = json.load(open('registers/schema.json'))


def load(n):
    r = list(csv.reader(open(f'registers/{n}.csv', newline='')))
    return [dict(zip(r[0], x)) for x in r[1:]]


def save(n, cols, rows):
    with open(f'registers/{n}.csv', 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(cols)
        for r in rows: w.writerow([r.get(c, '') for c in cols])


SOURCES = [
    ('SRC-0001', 'DDX Elevate deck (March 2026), context only', 'deck', '2026-03', 'raw/2026-10-08_deck_DDX-Elevate-latest.pdf', 'extracts/2026-10-08_deck_ddx-elevate.md', 'Budgets not relevant'),
    ('SRC-0002', 'US workbook Gold Layer Domain Data Requirements (SuperGold, KPI catalog, backlog)', 'workbook', '2026-10-08', 'raw/2026-10-08_workbook_Gold-Layer-Domain-Data-Requirements.xlsx', 'extracts/2026-10-08_workbook_gold-layer-domain-data-requirements.md', 'US-specific baseline; 479 SuperGold rows'),
    ('SRC-0003', 'Genie analysis: Canada reports vs SuperGold', 'analysis', '2026-10-08', 'raw/2026-10-08_genie-analysis_canada-kpi-cross-reference.md', 'extracts/2026-10-08_genie-analysis_canada-kpi-cross-reference.md', 'Design-level; field existence verified by Claude'),
    ('SRC-0004', 'KPI workshop 1 recap, version 1', 'meeting_summary', 'unknown', 'raw/2026-10-08_workshop-summary_kpi-workshop-1.md', 'extracts/2026-10-08_workshop_kpi-workshop-1-summary.md', 'MTG-0001'),
    ('SRC-0005', 'KPI workshop 1 summary, version 2 (with roles)', 'meeting_summary', 'unknown', 'raw/2026-10-08_workshop-summary_kpi-workshop-1_version-2.md', 'extracts/2026-10-08_workshop_kpi-workshop-1-summary-v2.md', 'MTG-0001; attributes-first speaker conflicts with version 1 (QST-0001)'),
    ('SRC-0006', "Damien's reply on LiveRamp data elements (relayed by Bastien)", 'email', '2026-10-08', 'raw/2026-10-08_message_damien-liveramp-reply.md', 'extracts/2026-10-08_message_damien-liveramp-reply.md', ''),
    ('SRC-0007', 'LiveRamp weekly file sample "LR for RENOVATE.xlsx" (51 columns)', 'file', '2026-10-08', 'raw/2026-10-08_schema_liveramp-weekly-file-columns.md', 'extracts/2026-10-08_schema_liveramp-weekly-file.md', 'Original in inbox/ only (personal data, git-ignored)'),
    ('SRC-0008', "Bastien's chat messages and draft email to the data teams", 'chat', '2026-10-08', '', 'CONTEXT.md', 'Includes 20:57 UTC clarification (12-36 one flag; no follow-up)'),
    ('SRC-0009', 'Assistant suggestion (not a project source)', 'assistant', '2026-10-08', '', '', 'Evidence is always inferred'),
    ('SRC-0010', 'Databricks Genie prompts A-C (Canada coverage)', 'prompt', '2026-10-08', '', 'prompts/databricks-genie-canada-coverage.md', 'Not yet run'),
]


def src_ids(text):
    out = []
    for t in [x.strip() for x in text.split(';') if x.strip()]:
        tl = t.lower()
        if 'summary-v2' in tl or 'version-2' in tl: s = 'SRC-0005'
        elif 'kpi-workshop-1' in tl: s = 'SRC-0004'
        elif 'genie-analysis' in tl: s = 'SRC-0003'
        elif 'damien-liveramp' in tl: s = 'SRC-0006'
        elif 'schema_liveramp' in tl: s = 'SRC-0007'
        elif 'workbook' in tl or 'gold-layer-domain' in tl: s = 'SRC-0002'
        elif 'deck' in tl: s = 'SRC-0001'
        elif 'bastien message' in tl or 'chat message' in tl: s = 'SRC-0008'
        elif 'assistant' in tl: s = 'SRC-0009'
        elif 'prompts/' in tl: s = 'SRC-0010'
        else: sys.exit(f'unmapped source: {t}')
        if s not in out: out.append(s)
    return ';'.join(out)


def ev(t):
    t = t.lower()
    if 'proposed by assistant' in t: return 'inferred'
    for k in ('documented', 'verbal', 'analysis', 'inferred'):
        if t.startswith(k): return k
    sys.exit(f'unmapped evidence: {t}')


def upd(r): return r.get('last_confirmed') or r.get('date_added') or '2026-10-08'


TOPIC = {
    'REQ-0001': 'gold-datapoints', 'REQ-0002': 'kpi-catalog', 'REQ-0003': 'reporting-coverage', 'REQ-0004': 'reporting-coverage',
    'REQ-0005': 'reporting-coverage', 'REQ-0006': 'reporting-coverage', 'REQ-0007': 'churn-engagement', 'REQ-0008': 'churn-engagement',
    'REQ-0009': 'identity-ids', 'REQ-0010': 'canada-specific', 'REQ-0011': 'kpi-catalog', 'REQ-0012': 'gold-datapoints',
    'REQ-0013': 'gold-datapoints', 'REQ-0014': 'churn-engagement',
    'DEC-0001': 'reporting-coverage', 'DEC-0002': 'reporting-coverage', 'DEC-0003': 'identity-ids', 'DEC-0004': 'kpi-catalog',
    'DEC-0005': 'churn-engagement', 'DEC-0006': 'kpi-catalog', 'DEC-0007': 'churn-engagement', 'DEC-0008': 'canada-specific',
    'DEC-0009': 'reporting-coverage', 'DEC-0010': 'governance-scope', 'DEC-0011': 'kpi-catalog', 'DEC-0012': 'kpi-catalog',
    'DEC-0013': 'kpi-catalog', 'DEC-0014': 'governance-scope', 'DEC-0015': 'governance-scope', 'DEC-0016': 'gold-datapoints',
    'DEC-0017': 'delivery-timeline', 'DEC-0018': 'churn-engagement',
    'COM-0001': 'kpi-catalog', 'COM-0002': 'delivery-timeline', 'COM-0003': 'kpi-catalog',
    'ASM-0001': 'governance-scope', 'ASM-0002': 'reporting-coverage',
}
ACT_TOPIC = {'Data team requirements': 'data-team-asks', 'KPI catalog': 'kpi-catalog', 'Canada coverage': 'reporting-coverage',
             'Gold attributes': 'gold-datapoints', 'Gold requirements': 'gold-datapoints', 'Delivery dates': 'delivery-timeline'}
WORKSHOP = ('SRC-0004', 'SRC-0005')


def common(r, cols):
    r['src'] = src_ids(r.get('source', ''))
    if 'evidence' in cols: r['evidence'] = ev(r.get('evidence_status', 'documented'))
    r['updated'] = upd(r)
    if 'topic' in cols and r['id'] in TOPIC: r['topic'] = TOPIC[r['id']]
    if 'links' in cols and any(s in r['src'] for s in WORKSHOP) and r['id'][:3] in ('ACT', 'DEC', 'COM', 'REQ'):
        r['links'] = 'MTG-0001'
    return r


def run():
    C = {k: v['columns'] for k, v in S['registers'].items()}
    # actions
    rows = load('actions')
    for r in rows:
        r['topic'] = ACT_TOPIC[r['topic']]
        r['status'] = {'pending': 'waiting', 'draft': 'proposed'}.get(r['status'], r['status'])
        common(r, C['actions'])
    save('actions', C['actions'], rows)
    # assumptions
    rows = load('assumptions')
    for r in rows:
        r['status'] = 'partly_confirmed' if 'partly' in r['status'] else 'open'
        common(r, C['assumptions'])
    save('assumptions', C['assumptions'], rows)
    # blockers
    rows = load('blockers')
    for r in rows: r['links'] = r.get('linked_ids', ''); common(r, C['blockers'])
    save('blockers', C['blockers'], rows)
    # commitments, decisions, requirements, kpis
    for n in ('commitments', 'decisions', 'requirements', 'kpis'):
        rows = load(n)
        for r in rows:
            if n == 'decisions': r['status'] = {'explicit': 'decided'}.get(r['status'], r['status'])
            if n == 'kpis': r['topic'] = 'reporting-coverage'
            common(r, C[n])
        save(n, C[n], rows)
    # stakeholders
    rows = load('stakeholders')
    for r in rows:
        r['links'] = r.get('open_topics', '')
        if r.get('preferred_channel'): r['notes'] = (r['notes'] + '. ' if r['notes'] else '') + 'Preferred channel: ' + r['preferred_channel']
        assert not r.get('interest') and not r.get('stance')
        common(r, C['stakeholders'])
    save('stakeholders', C['stakeholders'], rows)
    # stories (empty)
    save('stories', C['stories'], [common(r, C['stories']) for r in load('stories')])
    # datapoints split
    rows, slim, dfs = load('datapoints'), [], []
    for r in rows:
        d = r['definition']
        lab, _, rest = d.partition(' | ') if ' | ' in d else ('', '', d)
        loc = r['source'].split(' > ')
        domain = loc[2].strip() if len(loc) > 2 else ''
        st = {'existing (US)': 'existing_us'}.get(r['status'], 'requested' if r['status'].startswith('requested') else r['status'])
        slim.append({'id': r['id'], 'name': r['name'], 'label': lab.strip(), 'view': r['source_tables'], 'domain': domain,
                     'usa': r['usa'], 'canada': r['canada'], 'latam': r['latam'], 'status': st,
                     'requirement_ids': r['requirement_ids'], 'evidence': ev(r['evidence_status']),
                     'src': src_ids(r['source'].split(' > ')[0]), 'updated': upd(r)})
        dfs.append({'id': r['id'], 'definition': rest.strip(), 'quality_rules': r['quality_rules'], 'owner': r['owner']})
    save('datapoints', C['datapoints'], slim)
    save('datapoint_defs', S['aux']['datapoint_defs']['columns'], dfs)
    # new registers
    save('sources', C['sources'], [dict(zip(C['sources'], s + ('2026-10-08',))) for s in SOURCES])
    save('meetings', C['meetings'], [{
        'id': 'MTG-0001', 'title': 'Canada KPI workshop 1', 'date': 'unknown (before 2026-10-08)',
        'attendees': 'Bastien; STK-0005 Deepti; STK-0006 Andres; STK-0008 Ajantha; STK-0009 Mezyan; STK-0007 Fatima (per version 1)',
        'summary': 'US KPI catalog is the baseline (Match / Gap / New); Canada KPI catalog to create; Gold is the primary consumption layer; attributes vs KPIs order open; no firm deadline',
        'topic': 'kpi-catalog', 'links': 'DEC-0011;DEC-0012;DEC-0013;DEC-0014;DEC-0015;DEC-0016;DEC-0017', 'src': 'SRC-0004;SRC-0005', 'updated': '2026-10-08'}])
    Q = [
        ('Who said "start with attributes first" in workshop 1: Fatima (version 1) or Mezyan (version 2)?', 'STK-0007;STK-0009;MTG-0001', 'Bastien', 'open', '', 'kpi-catalog', 'SRC-0004;SRC-0005'),
        ('Workshop 1 date, and date of workshop 2', 'MTG-0001;ACT-0016', 'Bastien', 'open', '', 'kpi-catalog', 'SRC-0004'),
        ('Surnames and entities of Sandra, Damien, Thomas, Oli, Deepti, Andres, Ajantha, Fatima, Mezyan', 'STK-0001;STK-0002;STK-0003;STK-0004', 'Bastien', 'open', '', 'system', 'SRC-0008'),
        ('Are SHUUS, BIOUS, DER, BO the brands Canada excludes?', 'REQ-0010', 'Bastien', 'open', '', 'canada-specific', 'SRC-0003'),
        ('Is the "T2C KPI catalog Canada" the D2C KPI catalog?', 'ACT-0009;DEC-0013', 'Deepti', 'open', '', 'kpi-catalog', 'SRC-0005'),
        ('Which brand-specific local definitions (e.g. "active customer") does Canada need?', 'DEC-0014', 'Bastien', 'open', '', 'governance-scope', 'SRC-0005'),
        ('Who decides the open Genie questions DEC-0001 to DEC-0010?', 'DEC-0001;DEC-0010', 'Deepti', 'open', '', 'governance-scope', 'SRC-0003'),
        ('Value format of subcategories and Is_Churn_12M_36M in the LiveRamp file (empty in sample)', 'DP-0480;DP-0481', 'Damien', 'open', '', 'churn-engagement', 'SRC-0007'),
        ('Will the weekly LiveRamp file be sourced from Gold once it exists?', 'REQ-0001;SRC-0007', 'Damien', 'open', '', 'governance-scope', 'SRC-0007'),
        ('What does Is_Churn_12M_36M mean: one flag or two?', 'DP-0481;REQ-0014', 'Bastien', 'answered', 'One flag for the 12-36 month window (Bastien 2026-10-08)', 'churn-engagement', 'SRC-0008'),
    ]
    save('questions', C['questions'], [dict(zip(C['questions'], (f'QST-{n:04d}',) + q + ('2026-10-08',))) for n, q in enumerate(Q, 1)])
    print('migrated')


run()
