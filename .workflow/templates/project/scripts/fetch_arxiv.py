#!/usr/bin/env python3
"""Optionally download an arXiv PDF/source archive into a local paper folder.
Downloaded artifacts are ignored by git by default.
"""
from __future__ import annotations
import argparse, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def download(url: str, dest: Path):
    dest.parent.mkdir(parents=True,exist_ok=True)
    req=urllib.request.Request(url,headers={'User-Agent':'idea-driven-research-workflow/0.1'})
    with urllib.request.urlopen(req,timeout=60) as r, dest.open('wb') as f:
        f.write(r.read())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('arxiv_id')
    ap.add_argument('paper_key')
    ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--source',action='store_true')
    args=ap.parse_args()
    out=args.root/'research'/'literature'/'papers'/args.paper_key
    if not out.exists(): raise SystemExit('Create the paper card first with new_paper.py')
    aid=args.arxiv_id.replace('arXiv:','').strip()
    download(f'https://arxiv.org/pdf/{aid}',out/'paper.pdf')
    print(out/'paper.pdf')
    if args.source:
        download(f'https://export.arxiv.org/e-print/{aid}',out/'source.tar.gz')
        print(out/'source.tar.gz')
if __name__=='__main__': main()
