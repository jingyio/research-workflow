from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load_profile(root: Path = ROOT) -> dict:
    path = root / ".workflow" / "config" / "research_profile.json"
    return json.loads(path.read_text(encoding="utf-8"))

def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
