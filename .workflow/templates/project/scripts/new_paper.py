#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--key',required=True)
    ap.add_argument('--title',required=True)
    ap.add_argument('--year',default='')
    ap.add_argument('--root',type=Path,default=ROOT)
    args=ap.parse_args()
    key=''.join(c for c in args.key.lower() if c.isalnum() or c in '-_').strip('-_')
    if not key: raise SystemExit('Invalid key')
    outdir=args.root/'research'/'literature'/'papers'/key
    outdir.mkdir(parents=True,exist_ok=True)
    out=outdir/'card.md'
    if out.exists(): raise SystemExit(f'Card already exists: {out}')
    tmpl=(args.root/'research'/'literature'/'papers'/'_template'/'card.md').read_text(encoding='utf-8')
    text=tmpl.replace('{{TITLE}}',args.title).replace('{{KEY}}',key).replace('{{YEAR}}',str(args.year))
    out.write_text(text,encoding='utf-8')
    print(out)
if __name__=='__main__': main()
