#!/usr/bin/env python3
"""Renovate memory tool (stdlib only). Run from anywhere: python3 tools/pm.py <command>

  check                 validate registers against registers/schema.json
  build                 regenerate index/ (catalog, links, digest), then check
  show ID               one item with its direct links (in and out)
  impact ID [depth]     everything linked to ID, grouped by type (default depth 2)
  find TEXT [PREFIX]    search titles, all cells and datapoint definitions
  open                  print index/digest.md (open items)
  next PREFIX           next free ID, e.g. next REQ
  add REGISTER k=v ...  add a row (ID auto, updated=today), then build
  set ID k=v ...        change cells of a row (updated=today), then build
"""
import collections, csv, datetime, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, 'registers')
IDX = os.path.join(ROOT, 'index')
S = json.load(open(os.path.join(REG, 'schema.json')))
PFX = sorted(S['prefixes'], key=len, reverse=True)
IDRE = re.compile(r'\b(?:%s)-\d{3,4}\b' % '|'.join(PFX))
TODAY = datetime.date.today().isoformat()
HUB = 25          # nodes with more links than this are listed but not expanded
CLOSED = {'done', 'cancelled', 'decided', 'superseded', 'met', 'missed', 'resolved',
          'answered', 'dropped', 'rejected', 'delivered', 'confirmed', 'invalidated'}


def load(name):
    with open(os.path.join(REG, name + '.csv'), newline='') as f:
        r = list(csv.reader(f))
    return r[0], [dict(zip(r[0], x)) for x in r[1:]]


def save(name, cols, rows):
    with open(os.path.join(REG, name + '.csv'), 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, '') for c in cols])


def reg_of(i):
    return S['prefixes'].get(i.split('-')[0])


def short(s, n=80):
    s = ' '.join(str(s).split())
    return s if len(s) <= n else s[:n - 1] + '…'


def title(reg, r):
    return ' | '.join(r[c] for c in S['registers'][reg]['title'] if r.get(c))


def items():
    out = {}
    for reg in S['registers']:
        for r in load(reg)[1]:
            out[r['id']] = (reg, r)
    return out


def defs():
    return {r['id']: r for r in load('datapoint_defs')[1]}


def edges(it):
    names = collections.defaultdict(list)
    for i, (reg, r) in it.items():
        if reg == 'datapoints':
            names[r['name'].lower()].append(i)
    E = set()
    for i, (reg, r) in it.items():
        for c, v in r.items():
            if c == 'id' or not v:
                continue
            for t in IDRE.findall(v):
                if t != i:
                    E.add((i, t, c))
        for c in S['registers'][reg].get('field_refs', []):
            for tok in re.split(r'[\s,;()`]+', r.get(c, '')):
                for t in names.get(tok.lower(), []):
                    E.add((i, t, c))
    return sorted(E)


def check(quiet=False):
    errs, it = [], {}
    for reg, spec in S['registers'].items():
        cols, rows = load(reg)
        if cols != spec['columns']:
            errs.append(f'{reg}: header differs from schema')
        en = dict(S['common_enums'], **spec.get('enums', {}))
        for r in rows:
            i = r.get('id', '')
            if reg_of(i) != reg or not IDRE.fullmatch(i):
                errs.append(f'{reg}: bad id {i!r}')
            if i in it:
                errs.append(f'duplicate id {i}')
            it[i] = (reg, r)
            for c, allowed in en.items():
                if c in r and r[c] and r[c] not in allowed:
                    errs.append(f'{i}.{c}={r[c]!r} not in {allowed}')
            for t in filter(None, map(str.strip, r.get('topic', '').split(';'))):
                if t not in S['topics']:
                    errs.append(f'{i}.topic {t!r} unknown')
            if 'src' in r:
                toks = [t.strip() for t in r['src'].split(';') if t.strip()]
                if not toks:
                    errs.append(f'{i}: no src')
                for t in toks:
                    if not re.fullmatch(r'SRC-\d{4}', t):
                        errs.append(f'{i}.src {t!r} is not a SRC id')
    dcols, drows = load('datapoint_defs')
    if dcols != S['aux']['datapoint_defs']['columns']:
        errs.append('datapoint_defs: header differs from schema')
    for r in drows:
        if r['id'] not in it:
            errs.append(f'datapoint_defs: {r["id"]} has no datapoint')
    for a, b, c in edges(it):
        if b not in it:
            errs.append(f'{a}.{c} -> {b} does not exist')
    if not quiet:
        print('\n'.join(errs) if errs else f'ok: {len(it)} items, schema valid, no dangling links')
    return errs


def build():
    it = items()
    E = edges(it)
    os.makedirs(IDX, exist_ok=True)
    with open(os.path.join(IDX, 'catalog.csv'), 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['id', 'type', 'title', 'status', 'topic', 'owner', 'updated'])
        for i, (reg, r) in it.items():
            st = r.get('status') or r.get('canada_status') or r.get('canada', '')
            ow = r.get(S['registers'][reg]['owner'], '') if S['registers'][reg]['owner'] else ''
            w.writerow([i, reg, short(title(reg, r), 100), st, r.get('topic', ''), ow, r.get('updated', '')])
    with open(os.path.join(IDX, 'links.csv'), 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['from', 'to', 'via'])
        w.writerows(E)
    digest(it)
    errs = check(quiet=True)
    print(f'built index/: {len(it)} items, {len(E)} links' + (f'; {len(errs)} check errors (run check)' if errs else '; check ok'))
    return errs


def digest(it):
    by = collections.defaultdict(list)
    for i, (reg, r) in it.items():
        by[reg].append(r)
    is_open = lambda r: r.get('status', '') not in CLOSED
    L = [f'# Digest (generated {TODAY} by tools/pm.py build; do not edit)', '']
    try:
        last = [l for l in open(os.path.join(ROOT, 'logs', 'ingest-log.md')) if l[:2] == '20'][-1]
        L += ['Last ingest: ' + short(last, 140), '']
    except (OSError, IndexError):
        pass

    def sec(head, rows, fmt):
        L.append(f'## {head} ({len(rows)})')
        L.extend(fmt(r) for r in rows)
        L.append('')

    acts = [r for r in by['actions'] if is_open(r)]
    sec('Waiting on others', [r for r in acts if r['status'] == 'waiting'],
        lambda r: f"- {r['id']} {short(r['owner'], 20)}: {short(r['description'], 70)}")
    sec("Bastien's open actions", [r for r in acts if 'Bastien' in r['owner'] and r['status'] != 'waiting'],
        lambda r: f"- {r['id']} [{r['status']}] {short(r['description'], 70)}")
    sec('Other open actions', [r for r in acts if 'Bastien' not in r['owner'] and r['status'] != 'waiting'],
        lambda r: f"- {r['id']} {short(r['owner'], 20)} [{r['status']}]: {short(r['description'], 60)}")
    sec('Commitments open', [r for r in by['commitments'] if is_open(r)],
        lambda r: f"- {r['id']} {short(r['promised_by'], 20)}: {short(r['description'], 60)} (due {r['due'] or 'none'})")
    sec('Blockers open', [r for r in by['blockers'] if is_open(r)],
        lambda r: f"- {r['id']} {short(r['description'], 80)}")
    sec('Decisions open', [r for r in by['decisions'] if is_open(r)],
        lambda r: f"- {r['id']} [{r['topic']}] {short(r['decision'], 75)}")
    sec('Questions open', [r for r in by['questions'] if is_open(r)],
        lambda r: f"- {r['id']} ask {short(r['ask_who'], 18)}: {short(r['question'], 70)}")
    L.append('## Requirements by topic')
    c = collections.defaultdict(collections.Counter)
    for r in by['requirements']:
        c[r['topic'] or '-'][r['status']] += 1
    L.extend(f'- {t}: ' + ', '.join(f'{k} {v}' for k, v in sorted(s.items())) for t, s in sorted(c.items()))
    L.append('')
    dp = by['datapoints']
    cnt = lambda col: ', '.join(f'{k} {v}' for k, v in collections.Counter(r[col] for r in dp).most_common())
    L += ['## Datapoints', f'- USA: {cnt("usa")}', f'- Canada: {cnt("canada")}', f'- LATAM: {cnt("latam")}',
          '- KPIs (Canada reports vs SuperGold): ' + ', '.join(f'{k} {v}' for k, v in collections.Counter(r['canada_status'] for r in by['kpis']).most_common()), '']
    open(os.path.join(IDX, 'digest.md'), 'w').write('\n'.join(L))


def label(it, i):
    if i not in it:
        return f'{i} (missing)'
    reg, r = it[i]
    st = r.get('status') or r.get('canada_status') or ''
    return f"{i} {short(title(reg, r), 70)}" + (f' [{st}]' if st else '')


def show(i):
    it = items()
    if i not in it:
        sys.exit(f'{i} not found')
    reg, r = it[i]
    print(f'{i} ({reg})')
    row = dict(r, **{k: v for k, v in defs().get(i, {}).items() if k != 'id'}) if reg == 'datapoints' else r
    for c, v in row.items():
        if v and c != 'id':
            print(f'  {c}: {short(v, 400)}')
    E = edges(it)
    out = [(b, c) for a, b, c in E if a == i]
    inc = [(a, c) for a, b, c in E if b == i]
    for head, lst in (('out', out), ('in', inc)):
        if not lst:
            continue
        print(f'{head} ({len(lst)}):')
        if len(lst) > HUB:
            print('  ' + ', '.join(f'{k} {v}' for k, v in collections.Counter(reg_of(x) for x, _ in lst).most_common()))
            lst = lst[:8]
        for x, c in lst:
            print(f'  {c}: {label(it, x)}')


def impact(i, depth=2):
    it = items()
    if i not in it:
        sys.exit(f'{i} not found')
    adj = collections.defaultdict(set)
    for a, b, c in edges(it):
        adj[a].add(b)
        adj[b].add(a)
    seen, frontier, via, hubs = {i: 0}, [i], {}, []
    for d in range(1, depth + 1):
        nxt = []
        for n in frontier:
            if n != i and (reg_of(n) in ('sources',) or len(adj[n]) > HUB):
                hubs.append(n)
                continue
            for m in adj[n]:
                if m not in seen:
                    seen[m], via[m] = d, n
                    nxt.append(m)
        frontier = nxt
    grp = collections.defaultdict(list)
    for m, d in seen.items():
        if m != i:
            grp[reg_of(m)].append((d, m))
    print(f'impact of {label(it, i)} (depth {depth})')
    for reg in sorted(grp, key=lambda g: min(d for d, _ in grp[g])):
        lst = sorted(grp[reg])
        print(f'{reg} ({len(lst)}):')
        for d, m in lst[:15]:
            print(f'  {label(it, m)}' + (f'  via {via[m]}' if d > 1 else ''))
        if len(lst) > 15:
            print(f'  +{len(lst) - 15} more')
    if hubs:
        print('not expanded (hubs): ' + ', '.join(sorted(set(hubs))))


def find(text, pfx=None):
    it, df, q, n = items(), defs(), text.lower(), 0
    for i, (reg, r) in it.items():
        if pfx and not i.startswith(pfx + '-'):
            continue
        blob = ' '.join(r.values()) + ' ' + ' '.join(df.get(i, {}).values())
        if q in blob.lower():
            print(label(it, i))
            n += 1
            if n >= 30:
                print('… (more, refine the search)')
                return
    if not n:
        print('no match')


def next_id(p):
    reg = S['prefixes'][p]
    nums = [int(r['id'].split('-')[1]) for r in load(reg)[1]]
    width = 3 if p == 'CAKPI' else 4
    return f'{p}-{(max(nums) + 1 if nums else 1):0{width}d}'


def kv(args):
    out = {}
    for a in args:
        k, _, v = a.partition('=')
        out[k] = v
    return out


def write(reg, i, vals, new=False):
    cols, rows = load(reg)
    bad = [k for k in vals if k not in cols]
    if bad:
        sys.exit(f'unknown column(s) for {reg}: {bad}; columns: {cols}')
    if new:
        rows.append(dict({c: '' for c in cols}, id=i))
    r = next((x for x in rows if x['id'] == i), None)
    if r is None:
        sys.exit(f'{i} not found')
    r.update(vals)
    if 'updated' in cols:
        r['updated'] = TODAY
    save(reg, cols, rows)
    errs = build()
    mine = [e for e in errs if i in e]
    if mine:
        print('WARNING:\n' + '\n'.join(mine))
    print(('added ' if new else 'updated ') + label(items(), i))


def main(a):
    if not a or a[0] in ('-h', '--help', 'help'):
        print(__doc__)
    elif a[0] == 'check':
        sys.exit(1 if check() else 0)
    elif a[0] == 'build':
        build()
    elif a[0] == 'show':
        show(a[1])
    elif a[0] == 'impact':
        impact(a[1], int(a[2]) if len(a) > 2 else 2)
    elif a[0] == 'find':
        find(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == 'open':
        print(open(os.path.join(IDX, 'digest.md')).read())
    elif a[0] == 'next':
        print(next_id(a[1]))
    elif a[0] == 'add':
        reg = a[1]
        p = [k for k, v in S['prefixes'].items() if v == reg][0]
        write(reg, next_id(p), kv(a[2:]), new=True)
    elif a[0] == 'set':
        write(reg_of(a[1]), a[1], kv(a[2:]))
    else:
        print(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
