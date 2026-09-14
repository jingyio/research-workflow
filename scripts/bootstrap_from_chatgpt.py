#!/usr/bin/env python3
"""One-command local bootstrap from an official ChatGPT conversations.json export.

Pipeline:
1) derive topic anchors from the private seed metadata and research profile;
2) normalize/filter the export;
3) build a reconciliation packet for an LLM/agent.

No network access. Raw export is never copied into tracked files.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def collect_keywords():
    terms = []
    meta = ROOT / "research/private/idea_seed/00_seed_metadata.json"
    if meta.exists():
        data = json.loads(meta.read_text(encoding="utf-8"))
        terms += data.get("topic_anchors", [])
    profile = ROOT / ".workflow/config/research_profile.json"
    if profile.exists():
        data = json.loads(profile.read_text(encoding="utf-8"))
        for k in ("core_terms", "mechanism_terms", "domain_terms"):
            terms += data.get(k, [])
    # stable de-duplication, case-insensitive
    seen, out = set(), []
    for x in terms:
        x = str(x).strip()
        key = x.lower()
        if x and key not in seen:
            seen.add(key); out.append(x)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export", type=Path, help="official ChatGPT conversations.json")
    ap.add_argument("--digest", type=Path, default=ROOT / "research/imports/chatgpt/latest_digest.md")
    ap.add_argument("--packet", type=Path, default=ROOT / "research/private/reconciliation_packet.md")
    ap.add_argument("--extra-keywords", default="")
    args = ap.parse_args()

    kws = collect_keywords()
    kws += [x.strip() for x in args.extra_keywords.split(",") if x.strip()]
    cmd = [PY, str(ROOT / "scripts/ingest_chatgpt_export.py"), str(args.export), "--out", str(args.digest), "--keywords", ",".join(kws)]
    subprocess.run(cmd, check=True, cwd=ROOT)
    subprocess.run([PY, str(ROOT / "scripts/make_reconciliation_packet.py"), str(args.digest), "--out", str(args.packet)], check=True, cwd=ROOT)
    print("\nNext: give the reconciliation packet to your research agent and apply only reviewed changes.")

if __name__ == "__main__":
    main()
