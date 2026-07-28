#!/usr/bin/env python3
"""Multi-word code search via FTS5 + exact match fallback."""

import os
import sqlite3
import json
from schema import DB_PATH

def search_code(query: str, limit: int = 50):
    """Search code nodes by name/signature/body."""
    conn = sqlite3.connect(DB_PATH)
    try:
        words = query.strip().split()
        if not words:
            return []
        # FTS5 query
        fts_query = " AND ".join(words)
        rows = conn.execute(
            "SELECT rowid, rank FROM code_fts WHERE code_fts MATCH ? ORDER BY rank LIMIT ?",
            (fts_query, limit)
        ).fetchall()
        ids = [r[0] for r in rows]
        if not ids and len(words) == 1:
            # Fallback exact/like match
            rows = conn.execute(
                "SELECT id FROM code_nodes WHERE name LIKE ? LIMIT ?",
                (f"%{words[0]}%", limit)
            ).fetchall()
            ids = [r[0] for r in rows]
        if not ids:
            return []
        placeholders = ",".join("?" * len(ids))
        details = conn.execute(
            f"SELECT id, file_id, kind, name, start_line, end_line, signature, language FROM code_nodes WHERE id IN ({placeholders})",
            ids
        ).fetchall()
        return [
            {"id": d[0], "file_id": d[1], "kind": d[2], "name": d[3],
             "start_line": d[4], "end_line": d[5], "signature": d[6], "language": d[7]}
            for d in details
        ]
    finally:
        conn.close()

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: search.py <query> [limit]")
        return
    q = sys.argv[1]
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    print(json.dumps(search_code(q, lim), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
