#!/usr/bin/env python3
"""Generate a first-pass complementary query pack from research_profile.json.

This is deterministic scaffolding, not a substitute for scholarly search judgment.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ROUTES={
"R1-direct-neighbor":[
    '"{core}" review benchmark',
    '({domain}) ({core_terms}) mutation affinity prediction structure'
],
"R2-representation-state":[
    'binding interface representation mutation affinity pair representation',
    'explicit interaction representation local structural change affinity',
    'interface-aware geometric model affinity change mutation'
],
"R3-mechanism-architecture":[
    'local update equivariant graph neural network protein complex mutation',
    'cross-interface attention pair features affinity prediction structure'
],
"R4-domain-physics":[
    'mutation binding affinity conformational change induced fit interface',
    'binding free energy mutation structural rearrangement interface'
],
"R5-data-generalization":[
    'binding affinity change dataset mutation split generalization leakage',
    'DeltaDeltaG benchmark family split complex split out-of-distribution',
    'antibody antigen affinity mutation dataset generalization'
],
"R6-failure-negative":[
    'binding affinity prediction structure model limitations split sensitivity',
    'DeltaDeltaG prediction overfitting data scarcity generalization negative results'
],
"R7-adjacent-analogy":[
    'dynamic local representation update geometric deep learning edit',
    'change detection explicit relation state local update graph neural network'
],
"R8-novelty-collision":[
    '"interaction state" mutation binding affinity',
    '"interface state" protein mutation affinity',
    'dynamic interface representation affinity change'
],
"R9-executable-baseline":[
    'binding affinity mutation prediction github dataset structure model',
    'DeltaDeltaG geometric neural network code dataset'
]
}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    profile=json.loads((args.root/'.workflow'/'config'/'research_profile.json').read_text(encoding='utf-8'))
    core=profile['core_question'].replace('"','')
    domain=profile.get('domain','')
    core_terms=' OR '.join(profile.get('core_terms',[])[:5])
    lines=['# Generated Search Query Pack','', '> Deterministic first pass. Refine queries and log actual searches in `search_log.csv`.','',f'Core question: {profile["core_question"]}','']
    for route,qs in ROUTES.items():
        lines += [f'## {route}','']
        for q in qs:
            try: q=q.format(core=core,domain=domain,core_terms=core_terms)
            except Exception: pass
            lines.append(f'- `{q}`')
        lines.append('')
    lines += ['## Priority questions from profile','']
    for q in profile.get('priority_questions',[]): lines.append(f'- {q}')
    out=args.out or (args.root/'research'/'literature'/'generated_query_pack.md')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(out)
if __name__=='__main__': main()
