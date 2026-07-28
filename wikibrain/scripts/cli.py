#!/usr/bin/env python3
"""WikiBrain CLI entry."""

import sys
import json
from ingest import ingest_file, ensure_dirs
from indexer import index_wiki
from lint import lint_wiki
from query import query_wiki
from session_extract import extract_feedback, write_feedback_wiki
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("""WikiBrain CLI
Commands:
  init                          Ensure directories
  ingest <file> [category]      Stage raw material
  index                         Index wiki pages
  query <query> [limit]         Search wiki
  lint                          Quality audit
  extract-feedback              Distill session feedback
""")
        return
    cmd = sys.argv[1]
    if cmd == "init":
        ensure_dirs()
        print("WikiBrain directories ready.")
    elif cmd == "ingest":
        f = sys.argv[2]
        cat = sys.argv[3] if len(sys.argv) > 3 else "notes"
        print(ingest_file(f, cat))
    elif cmd == "index":
        index_wiki()
    elif cmd == "query":
        q = sys.argv[2]
        lim = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        print(json.dumps(query_wiki(q, lim), indent=2, ensure_ascii=False))
    elif cmd == "lint":
        print(json.dumps(lint_wiki(), indent=2, ensure_ascii=False))
    elif cmd == "extract-feedback":
        items = []
        for sf in Path("workspace/.sessions").glob("*.json"):
            items.extend(extract_feedback(str(sf)))
        if items:
            out = write_feedback_wiki(items)
            print(f"Extracted {len(items)} items to {out}")
        else:
            print("No feedback found.")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
