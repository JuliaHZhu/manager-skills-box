#!/usr/bin/env python3
"""WikiBrain lint — detect orphans, dead links, missing metadata."""

import os
import sqlite3
from pathlib import Path
from indexer import ensure_wiki_schema, DB_PATH, WIKI_DIR

def lint_wiki():
    ensure_wiki_schema()
    conn = sqlite3.connect(DB_PATH)
    try:
        issues = []
        # Orphan pages (no incoming wiki-links)
        rows = conn.execute("""
        SELECT path, title FROM wiki_pages
        WHERE path NOT IN (SELECT DISTINCT src_path FROM wiki_links)
          AND path NOT IN (SELECT DISTINCT dst_title FROM wiki_links)
        """).fetchall()
        for path, title in rows:
            issues.append({"type": "orphan", "path": path, "title": title,
                           "severity": "info", "message": "No wiki-links to or from this page"})
        # Dead links (dst_title not matching any page title)
        rows = conn.execute("""
        SELECT DISTINCT l.src_path, l.dst_title
        FROM wiki_links l
        LEFT JOIN wiki_pages p ON l.dst_title = p.title
        WHERE p.title IS NULL
        """).fetchall()
        for src, dst in rows:
            issues.append({"type": "dead-link", "path": src, "target": dst,
                           "severity": "warn", "message": f"Wiki-link target not found: [[{dst}]]"})
        # Missing frontmatter
        rows = conn.execute("SELECT path, title FROM wiki_pages WHERE frontmatter='{}' OR frontmatter=''").fetchall()
        for path, title in rows:
            issues.append({"type": "missing-meta", "path": path, "title": title,
                           "severity": "info", "message": "Missing YAML frontmatter"})
        return issues
    finally:
        conn.close()

def main():
    import json
    issues = lint_wiki()
    print(json.dumps(issues, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
