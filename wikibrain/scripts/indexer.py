#!/usr/bin/env python3
"""WikiBrain indexer — extract YAML frontmatter + wiki-links, build SQLite index."""

import os
import re
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("FILESTATES_DB", "workspace/.filestates/index.db"))
WIKI_DIR = Path("workspace/knowledge/wiki")

LINK_RE = re.compile(r"\[\[(.*?)\]\]")
FRONT_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def ensure_wiki_schema():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS wiki_pages (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE NOT NULL,
        title TEXT,
        category TEXT,
        tags TEXT,
        created_at TEXT,
        updated_at TEXT,
        frontmatter TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_wiki_title ON wiki_pages(title);
    CREATE INDEX IF NOT EXISTS idx_wiki_cat ON wiki_pages(category);
    CREATE TABLE IF NOT EXISTS wiki_links (
        id INTEGER PRIMARY KEY,
        src_path TEXT,
        dst_title TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_wiki_links_dst ON wiki_links(dst_title);
    CREATE VIRTUAL TABLE IF NOT EXISTS wiki_fts USING fts5(
        title, body,
        content='wiki_pages',
        content_rowid='id'
    );
    """)
    conn.commit()
    conn.close()

def parse_page(path: str):
    text = Path(path).read_text(encoding="utf-8")
    fm = {}
    m = FRONT_RE.search(text)
    if m:
        import yaml
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            pass
    links = LINK_RE.findall(text)
    body = text
    if m:
        body = text[m.end():]
    return fm, links, body

def index_wiki():
    ensure_wiki_schema()
    conn = sqlite3.connect(DB_PATH)
    try:
        total = 0
        for page in WIKI_DIR.rglob("*.md"):
            path = str(page)
            try:
                fm, links, body = parse_page(path)
            except Exception:
                continue
            title = fm.get("title", page.stem)
            category = fm.get("category", "")
            tags = ",".join(fm.get("tags", []))
            now = __import__("datetime").datetime.now().isoformat()
            conn.execute("""
            INSERT INTO wiki_pages(path, title, category, tags, created_at, updated_at, frontmatter)
            VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(path) DO UPDATE SET
                title=excluded.title, category=excluded.category, tags=excluded.tags,
                updated_at=excluded.updated_at, frontmatter=excluded.frontmatter
            """, (path, title, category, tags, now, now, str(fm)))
            conn.execute("DELETE FROM wiki_links WHERE src_path=?", (path,))
            for dst in links:
                conn.execute("INSERT INTO wiki_links(src_path, dst_title) VALUES (?,?)", (path, dst))
            total += 1
        conn.commit()
        print(f"Indexed {total} wiki pages.")
    finally:
        conn.close()

def main():
    index_wiki()

if __name__ == "__main__":
    main()
