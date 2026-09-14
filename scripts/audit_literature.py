#!/usr/bin/env python3
"""Lightweight structural audit for paper cards and evidence ledgers."""
from __future__ import annotations
from pathlib import Path
import csv, sys
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_CARD_HEADINGS=['## Why this paper is in the project','## Task and scientific setup','## What is explicitly represented?','## Evidence from the paper','## Agent inference — keep separate','## Failure / limitation evidence','## Effect on current Idea State']

def main():
    issues=[]
    pdir=ROOT/'research'/'literature'/'papers'
    for card in pdir.glob('*/card.md'):
        if card.parent.name.startswith('_'): continue
        text=card.read_text(encoding='utf-8')
        for h in REQUIRED_CARD_HEADINGS:
            if h not in text: issues.append(f'{card}: missing heading {h}')
        if '- Decision question:' not in text: issues.append(f'{card}: missing decision question field')
    ledger=ROOT/'research'/'literature'/'evidence'/'claim_ledger.csv'
    with ledger.open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    valid={'supports','challenges','mixed','context','unknown',''}
    for i,row in enumerate(rows,2):
        if row.get('support_direction','') not in valid:
            issues.append(f'{ledger}:{i}: invalid support_direction={row.get("support_direction")}')
        if row.get('paper_key') and not (pdir/row['paper_key']/'card.md').exists():
            issues.append(f'{ledger}:{i}: unknown paper_key={row["paper_key"]}')
    if issues:
        print('AUDIT FAILED')
        for x in issues: print('-',x)
        sys.exit(1)
    print('AUDIT OK')
if __name__=='__main__': main()
