#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--label',default='idea-state')
    args=ap.parse_args()
    src=args.root/'research'/'idea'/'current.md'
    text=src.read_text(encoding='utf-8')
    digest=hashlib.sha256(text.encode()).hexdigest()[:8]
    stamp=datetime.now().strftime('%Y%m%d-%H%M%S')
    out=args.root/'research'/'idea'/'snapshots'/f'{stamp}-{args.label}-{digest}.md'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(text,encoding='utf-8')
    print(out)
if __name__=='__main__': main()
