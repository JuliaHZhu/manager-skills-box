#!/usr/bin/env python3
"""WikiBrain session extract — distill session feedback into wiki notes."""

import os
import json
import re
from pathlib import Path
from datetime import datetime

SESSIONS_DIR = Path("workspace/.sessions")
WIKI_DIR = Path("workspace/knowledge/wiki")

def extract_feedback(session_file: str) -> list:
    """Parse a session JSONL for user corrections, preferences, key facts."""
    path = Path(session_file)
    if not path.exists():
        return []
    feedback = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                content = obj.get("content", "")
                # Heuristics: user corrections often contain "不对", "错了", "应该", "prefer"
                if any(k in content for k in ("不对", "错了", "应该", "prefer", "不要", "instead", "correction")):
                    feedback.append({
                        "timestamp": obj.get("timestamp", ""),
                        "content": content[:500],
                        "source": str(path)
                    })
    except Exception as e:
        return [{"error": str(e)}]
    return feedback

def write_feedback_wiki(feedback_items: list):
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    out = WIKI_DIR / "feedback_notes.md"
    lines = ["---", "title: Session Feedback Notes", "category: meta", f"updated: {datetime.now().isoformat()}", "---", "\n"]
    for item in feedback_items:
        lines.append(f"- **{item.get('timestamp','')}**: {item.get('content','')} _(from {item.get('source','')})_")
    out.write_text("\n".join(lines), encoding="utf-8")
    return str(out)

def main():
    import sys
    items = []
    for sf in SESSIONS_DIR.glob("*.json"):
        items.extend(extract_feedback(str(sf)))
    if items:
        out = write_feedback_wiki(items)
        print(f"Extracted {len(items)} feedback items to {out}")
    else:
        print("No feedback found.")

if __name__ == "__main__":
    main()
