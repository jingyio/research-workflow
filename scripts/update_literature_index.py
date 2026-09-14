#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]

def field(text,label):
    m=re.search(rf'^- {re.escape(label)}:\s*(.*)$',text,re.M)
    return m.group(1).strip() if m else ''

def main():
    pdir=ROOT/'research'/'literature'/'papers'
    rows=[]
    for card in sorted(pdir.glob('*/card.md')):
        if card.parent.name.startswith('_'): continue
        t=card.read_text(encoding='utf-8')
        title=re.search(r'^# Paper Card — (.+)$',t,re.M)
        rows.append((card.parent.name, title.group(1).strip() if title else card.parent.name, field(t,'Year'), field(t,'DOI / arXiv'), field(t,'Primary URL'), field(t,'Code')))
    out=ROOT/'research'/'literature'/'papers'/'INDEX.md'
    lines=['# Paper Index','', '| Key | Title | Year | DOI/arXiv | URL | Code |','|---|---|---:|---|---|---|']
    for r in rows: lines.append('| '+' | '.join(x.replace('|','\\|') for x in r)+' |')
    out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'{out}: {len(rows)} papers')
if __name__=='__main__': main()
