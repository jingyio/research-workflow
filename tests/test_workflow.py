from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PY=sys.executable

def run(*args, cwd=ROOT):
    return subprocess.run([PY,*map(str,args)],cwd=cwd,text=True,capture_output=True,check=True)

def test_build_search_plan():
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'queries.md'
        run(ROOT/'scripts'/'build_search_plan.py','--out',out)
        text=out.read_text(encoding='utf-8')
        assert 'R1-direct-neighbor' in text
        assert 'R6-failure-negative' in text
        assert 'binding' in text.lower()

def test_ingest_chatgpt_export():
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        sample=[{"title":"AIDD idea","create_time":1,"mapping":{"a":{"message":{"author":{"role":"user"},"create_time":1,"content":{"parts":["interface state for binding affinity"]}}},"b":{"message":{"author":{"role":"assistant"},"create_time":2,"content":{"parts":["consider structure"]}}}}}]
        src=td/'conversations.json'; src.write_text(json.dumps(sample),encoding='utf-8')
        out=td/'digest.md'
        run(ROOT/'scripts'/'ingest_chatgpt_export.py',src,'--out',out,'--keywords','affinity')
        text=out.read_text(encoding='utf-8')
        assert 'AIDD idea' in text and 'interface state' in text

def test_init_project_is_idempotent():
    with tempfile.TemporaryDirectory() as td:
        dest=Path(td)/'project'
        run(ROOT/'scripts'/'init_project.py',dest)
        target=dest/'research'/'idea'/'current.md'
        assert target.exists()
        marker='\nPRIVATE EDIT\n'
        target.write_text(target.read_text(encoding='utf-8')+marker,encoding='utf-8')
        run(ROOT/'scripts'/'init_project.py',dest)
        assert marker in target.read_text(encoding='utf-8')


def test_private_seed_and_bootstrap_packet():
    seed=ROOT/'research'/'private'/'idea_seed'/'03_current_private_seed.md'
    assert seed.exists()
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'bootstrap.md'
        run(ROOT/'scripts'/'build_bootstrap_packet.py','--out',out)
        body=out.read_text(encoding='utf-8')
        assert 'North-star question' in body or 'north-star question' in body.lower()
        assert 'World model' in body or 'world model' in body.lower()


def test_reconciliation_packet():
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        digest=td/'digest.md'; digest.write_text('# Digest\n\nAIDD binding affinity interface state',encoding='utf-8')
        out=td/'reconcile.md'
        run(ROOT/'scripts'/'make_reconciliation_packet.py',digest,'--out',out)
        body=out.read_text(encoding='utf-8')
        assert 'confirm' in body and 'NORMALIZED CHATGPT HISTORY' in body


def test_bootstrap_from_chatgpt_uses_seed_keywords():
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        sample=[
          {"title":"Unrelated","create_time":1,"mapping":{"a":{"message":{"author":{"role":"user"},"create_time":1,"content":{"parts":["hello world"]}}}}},
          {"title":"AIDD","create_time":2,"mapping":{"a":{"message":{"author":{"role":"user"},"create_time":2,"content":{"parts":["antibody antigen binding interface mutation"]}}}}}
        ]
        src=td/'conversations.json'; src.write_text(json.dumps(sample),encoding='utf-8')
        digest=td/'digest.md'; packet=td/'packet.md'
        run(ROOT/'scripts'/'bootstrap_from_chatgpt.py',src,'--digest',digest,'--packet',packet)
        body=digest.read_text(encoding='utf-8')
        assert 'Selected conversations: 1 / 2' in body
        assert packet.exists()


def test_prompt_router_and_chinese_language_policy():
    required=[
        '00_session_bootstrap.md','01_plan_cycle.md','02_execute_cycle.md',
        '03_close_cycle.md','04_deep_read_paper.md','05_weekly_synthesis.md'
    ]
    for name in required:
        path=ROOT/'.workflow'/'prompts'/name
        assert path.exists(), name
        body=path.read_text(encoding='utf-8')
        assert any(ch in body for ch in '中文研究轮调证据问题')
    agents=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
    assert '启动下一轮文献调研' in agents
    assert '执行本轮调研' in agents
    profile=json.loads((ROOT/'.workflow'/'config'/'research_profile.json').read_text(encoding='utf-8'))
    assert profile['language_policy']['default_output_language']=='zh-CN'
