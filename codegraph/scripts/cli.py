#!/usr/bin/env python3
"""CodeGraph CLI entry."""

import sys
import json
from schema import ensure_codegraph_schema
from indexer import index_project
from blast_radius import blast_radius
from search import search_code

def main():
    if len(sys.argv) < 2:
        print("""CodeGraph CLI
Commands:
  init                           Ensure schema
  index <src_dir>                Index project code
  blast <node_name> [max_nodes]  Impact analysis
  search <query> [limit]         Search code nodes
""")
        return
    cmd = sys.argv[1]
    if cmd == "init":
        ensure_codegraph_schema()
        print("Schema ready.")
    elif cmd == "index":
        src = sys.argv[2] if len(sys.argv) > 2 else "workspace/src"
        index_project(src)
    elif cmd == "blast":
        name = sys.argv[2]
        max_n = int(sys.argv[3]) if len(sys.argv) > 3 else 500
        print(json.dumps(blast_radius(name, max_n), indent=2, ensure_ascii=False))
    elif cmd == "search":
        q = sys.argv[2]
        lim = int(sys.argv[3]) if len(sys.argv) > 3 else 50
        print(json.dumps(search_code(q, lim), indent=2, ensure_ascii=False))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
