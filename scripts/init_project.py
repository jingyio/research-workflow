#!/usr/bin/env python3
"""Bootstrap a research project from the reusable templates in this repository.

Idempotent: existing files are never overwritten.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = HERE / ".workflow" / "templates" / "project"


def copy_missing(src: Path, dst: Path) -> tuple[int, int]:
    created = skipped = 0
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        out = dst / rel
        if p.is_dir():
            out.mkdir(parents=True, exist_ok=True)
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            skipped += 1
        else:
            shutil.copy2(p, out)
            created += 1
    return created, skipped


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("destination", type=Path)
    args = ap.parse_args()
    if not TEMPLATE_ROOT.exists():
        raise SystemExit(f"Template root missing: {TEMPLATE_ROOT}")
    args.destination.mkdir(parents=True, exist_ok=True)
    created, skipped = copy_missing(TEMPLATE_ROOT, args.destination)
    print(f"Initialized {args.destination}: {created} files created, {skipped} existing files preserved.")

if __name__ == "__main__":
    main()
