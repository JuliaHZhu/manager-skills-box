#!/usr/bin/env python3
"""NeatFreak scanner — aggregate issues from CodeGraph + WikiBrain + FileStates."""

import os
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path("workspace/.filestates/index.db")
WIKI_DIR = Path("workspace/knowledge/wiki")
SRC_DIR = Path("workspace/src")
ARCHIVE_THRESHOLD_DAYS = 180

def _ensure_tables(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS wiki_pages (
        id INTEGER PRIMARY KEY, path TEXT UNIQUE NOT NULL, title TEXT,
        category TEXT, tags TEXT, created_at TEXT, updated_at TEXT, frontmatter TEXT
    );
    CREATE TABLE IF NOT EXISTS wiki_links (
        id INTEGER PRIMARY KEY, src_path TEXT, dst_title TEXT
    );
    CREATE TABLE IF NOT EXISTS code_nodes (
        id INTEGER PRIMARY KEY, file_id INTEGER, kind TEXT, name TEXT,
        start_line INTEGER, end_line INTEGER, signature TEXT, body TEXT, language TEXT
    );
    CREATE TABLE IF NOT EXISTS code_edges (
        id INTEGER PRIMARY KEY, src_id INTEGER, dst_id INTEGER, kind TEXT
    );
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY, path TEXT UNIQUE NOT NULL, hash TEXT,
        size INTEGER, mtime REAL, role TEXT DEFAULT 'source', created_at TEXT, updated_at TEXT
    );
    """)
    conn.commit()

def scan_all() -> list:
    issues = []
    if not DB_PATH.exists():
        return issues
    conn = sqlite3.connect(DB_PATH)
    _ensure_tables(conn)
    try:
        # Wiki orphans (no links at all)
        rows = conn.execute("""
        SELECT path, title FROM wiki_pages
        WHERE path NOT IN (SELECT DISTINCT src_path FROM wiki_links)
          AND path NOT IN (SELECT DISTINCT dst_title FROM wiki_links)
        """).fetchall()
        for path, title in rows:
            issues.append({"type": "wiki-orphan", "path": path, "title": title,
                           "severity": "info", "message": "Wiki page has no links"})
        # Wiki dead links
        rows = conn.execute("""
        SELECT DISTINCT l.src_path, l.dst_title
        FROM wiki_links l
        LEFT JOIN wiki_pages p ON l.dst_title = p.title
        WHERE p.title IS NULL
        """).fetchall()
        for src, dst in rows:
            issues.append({"type": "dead-link", "path": src, "target": dst,
                           "severity": "warn", "message": f"Dead wiki link: [[{dst}]]"})
        # Code orphans (nodes with zero edges)
        rows = conn.execute("""
        SELECT n.id, n.name, n.kind, n.file_id, f.path
        FROM code_nodes n
        JOIN files f ON n.file_id = f.id
        WHERE n.id NOT IN (SELECT src_id FROM code_edges)
          AND n.id NOT IN (SELECT dst_id FROM code_edges)
        """).fetchall()
        for nid, name, kind, fid, fpath in rows:
            issues.append({"type": "code-orphan", "node_id": nid, "name": name,
                           "kind": kind, "file": fpath,
                           "severity": "info", "message": f"{kind} '{name}' has no references"})
        # Stale files (not modified in N days)
        threshold = (datetime.now() - timedelta(days=ARCHIVE_THRESHOLD_DAYS)).timestamp()
        rows = conn.execute(
            "SELECT path, mtime, role FROM files WHERE mtime < ? AND role IN ('doc','generated','artifact')",
            (threshold,)
        ).fetchall()
        for fpath, mtime, role in rows:
            issues.append({"type": "stale", "path": fpath, "role": role,
                           "last_modified": datetime.fromtimestamp(mtime).isoformat(),
                           "severity": "info", "message": f"Not modified in {ARCHIVE_THRESHOLD_DAYS}+ days"})
        # Missing wiki frontmatter
        rows = conn.execute("SELECT path, title FROM wiki_pages WHERE frontmatter='{}' OR frontmatter=''").fetchall()
        for path, title in rows:
            issues.append({"type": "missing-meta", "path": path, "title": title,
                           "severity": "info", "message": "Missing YAML frontmatter"})
    finally:
        conn.close()
    return issues

def main():
    import json
    issues = scan_all()
    print(json.dumps(issues, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
