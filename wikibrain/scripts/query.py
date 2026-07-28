#!/usr/bin/env python3
"""WikiBrain query — fast wiki page lookup via index + FTS5."""

import os
import sqlite3
from pathlib import Path
from indexer import ensure_wiki_schema, DB_PATH

def query_wiki(q: str, limit: int = 20):
    ensure_wiki_schema()
    conn = sqlite3.connect(DB_PATH)
    try:
        words = q.strip().split()
        if not words:
            return []
        fts_q = " AND ".join(words)
        rows = conn.execute(
            "SELECT rowid, rank FROM wiki_fts WHERE wiki_fts MATCH ? ORDER BY rank LIMIT ?",
            (fts_q, limit)
        ).fetchall()
        ids = [r[0] for r in rows]
        if not ids:
            # Fallback LIKE
            pattern = f"%{q}%"
            rows = conn.execute(
                "SELECT id FROM wiki_pages WHERE title LIKE ? OR path LIKE ? LIMIT ?",
                (pattern, pattern, limit)
            ).fetchall()
            ids = [r[0] for r in rows]
        if not ids:
            return []
        placeholders = ",".join("?" * len(ids))
        details = conn.execute(
            f"SELECT id, path, title, category, tags FROM wiki_pages WHERE id IN ({placeholders})",
            ids
        ).fetchall()
        return [
            {"id": d[0], "path": d[1], "title": d[2], "category": d[3], "tags": d[4]}
            for d in details
        ]
    finally:
        conn.close()

def main():
    import sys, json
    if len(sys.argv) < 2:
        print("Usage: query.py <query> [limit]")
        return
    q = sys.argv[1]
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    print(json.dumps(query_wiki(q, lim), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
