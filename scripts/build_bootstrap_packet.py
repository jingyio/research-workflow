#!/usr/bin/env python3
"""Build a local agent-readable bootstrap packet from public state + private seed."""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC = [
    ROOT / "research/idea/current.md",
    ROOT / "research/idea/rejected.md",
    ROOT / "research/idea/open_questions.md",
    ROOT / "research/idea/decision_log.md",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed-dir", type=Path, default=ROOT / "research/private/idea_seed")
    ap.add_argument("--out", type=Path, default=ROOT / "research/private/bootstrap_packet.md")
    args = ap.parse_args()

    if not args.seed_dir.exists():
        raise SystemExit(f"Private seed not found: {args.seed_dir}")

    chunks = [
        "# Research Bootstrap Packet",
        "",
        "> Local/generated file. Research memory is not scientific evidence.",
        "",
        "## Instructions",
        "",
        (ROOT / ".workflow/prompts/bootstrap_from_private_seed.md").read_text(encoding="utf-8"),
    ]
    for p in PUBLIC:
        if p.exists():
            chunks += ["", f"---\n\n# SOURCE: `{p.relative_to(ROOT)}`\n", p.read_text(encoding="utf-8")]
    for p in sorted(args.seed_dir.glob("*")):
        if p.is_file() and p.suffix.lower() in {".md", ".json", ".txt"}:
            chunks += ["", f"---\n\n# PRIVATE SOURCE: `{p.relative_to(ROOT)}`\n", p.read_text(encoding="utf-8")]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(chunks), encoding="utf-8")
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
