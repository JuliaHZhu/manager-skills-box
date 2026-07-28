#!/usr/bin/env python3
"""CodeGraph database schema — extends FileStates shared index.db."""

import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("FILESTATES_DB", "workspace/.filestates/index.db"))

def ensure_codegraph_schema():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS code_nodes (
        id INTEGER PRIMARY KEY,
        file_id INTEGER REFERENCES files(id),
        kind TEXT NOT NULL,
        name TEXT NOT NULL,
        start_line INTEGER,
        end_line INTEGER,
        signature TEXT,
        body TEXT,
        language TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_nodes_file ON code_nodes(file_id);
    CREATE INDEX IF NOT EXISTS idx_nodes_kind ON code_nodes(kind);
    CREATE INDEX IF NOT EXISTS idx_nodes_name ON code_nodes(name);

    CREATE TABLE IF NOT EXISTS code_edges (
        id INTEGER PRIMARY KEY,
        src_id INTEGER REFERENCES code_nodes(id),
        dst_id INTEGER REFERENCES code_nodes(id),
        kind TEXT NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_edges_src ON code_edges(src_id);
    CREATE INDEX IF NOT EXISTS idx_edges_dst ON code_edges(dst_id);

    CREATE VIRTUAL TABLE IF NOT EXISTS code_fts USING fts5(
        name, signature, body,
        content='code_nodes',
        content_rowid='id'
    );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    ensure_codegraph_schema()
    print("CodeGraph schema ready.")
