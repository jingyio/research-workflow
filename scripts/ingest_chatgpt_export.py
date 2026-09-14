#!/usr/bin/env python3
"""Normalize ChatGPT exports into a research-focused Markdown digest.

Supports standard conversations.json and plain .md/.txt/.html files.
No network or third-party dependencies.
"""
from __future__ import annotations
import argparse, json, re, html
from pathlib import Path
from datetime import datetime, timezone


def text_from_content(content) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(text_from_content(x) for x in content)
    if isinstance(content, dict):
        if isinstance(content.get("parts"), list):
            return "\n".join(text_from_content(x) for x in content["parts"])
        if "text" in content:
            return text_from_content(content["text"])
        return "\n".join(text_from_content(v) for v in content.values() if isinstance(v, (str,list,dict)))
    return str(content)


def normalize_conversation(conv: dict) -> dict:
    title = conv.get("title") or "Untitled"
    mapping = conv.get("mapping") or {}
    msgs=[]
    for node in mapping.values():
        m = (node or {}).get("message")
        if not m: continue
        author = ((m.get("author") or {}).get("role") or "unknown")
        if author not in {"user","assistant"}: continue
        text = text_from_content(m.get("content")).strip()
        if not text: continue
        ts = m.get("create_time") or 0
        msgs.append((float(ts or 0), author, text))
    msgs.sort(key=lambda x:x[0])
    return {"title":title, "messages":msgs, "create_time":conv.get("create_time") or 0}


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<script.*?>.*?</script>", " ", s)
    s = re.sub(r"(?is)<style.*?>.*?</style>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", "\n", s)
    return html.unescape(re.sub(r"\n{3,}", "\n\n", s))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--keywords", default="", help="comma-separated; conversation kept if title/content matches any keyword")
    ap.add_argument("--titles", default="", help="optional comma-separated title substrings")
    ap.add_argument("--max-chars-per-message", type=int, default=12000)
    args=ap.parse_args()
    kws=[x.strip().lower() for x in args.keywords.split(',') if x.strip()]
    title_filters=[x.strip().lower() for x in args.titles.split(',') if x.strip()]
    raw=args.input.read_text(encoding='utf-8', errors='replace')
    conversations=[]
    if args.input.suffix.lower()=='.json':
        data=json.loads(raw)
        if isinstance(data, dict) and "conversations" in data:
            data=data["conversations"]
        if isinstance(data, list):
            conversations=[normalize_conversation(c) for c in data if isinstance(c,dict)]
        else:
            raise SystemExit("JSON format not recognized as a ChatGPT conversation export.")
    else:
        body=strip_html(raw) if args.input.suffix.lower() in {'.html','.htm'} else raw
        conversations=[{"title":args.input.stem,"messages":[(0,"unknown",body)],"create_time":0}]

    def keep(c):
        title=c['title'].lower()
        text='\n'.join(m[2] for m in c['messages']).lower()
        if title_filters and not any(x in title for x in title_filters):
            return False
        if kws and not any(x in title or x in text for x in kws):
            return False
        return True

    selected=[c for c in conversations if keep(c)]
    selected.sort(key=lambda c: float(c.get('create_time') or 0))
    lines=["# Normalized ChatGPT Research Digest", "", f"Source: `{args.input.name}`", f"Selected conversations: {len(selected)} / {len(conversations)}", "", "> This is historical context, not authoritative research truth. Compare it against the current Idea State.", ""]
    for c in selected:
        lines += [f"## {c['title']}", ""]
        for ts,role,text in c['messages']:
            if len(text)>args.max_chars_per_message:
                text=text[:args.max_chars_per_message]+"\n\n[truncated by normalizer]"
            stamp=""
            if ts:
                try: stamp=datetime.fromtimestamp(ts,tz=timezone.utc).isoformat()
                except Exception: pass
            lines += [f"### {role}" + (f" — {stamp}" if stamp else ""), "", text, ""]
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text("\n".join(lines),encoding='utf-8')
    print(f"Wrote {args.out} ({len(selected)} conversations).")

if __name__=='__main__': main()
