#!/usr/bin/env python3
"""FileStates SQLite index manager — shared by all skills."""

import os
import sqlite3
import hashlib
from pathlib import Path
from datetime import datetime

DB_PATH = Path(os.environ.get("FILESTATES_DB", "workspace/.filestates/index.db"))

def ensure_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE NOT NULL,
        hash TEXT,
        size INTEGER,
        mtime REAL,
        role TEXT DEFAULT 'source',
        created_at TEXT,
        updated_at TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_files_path ON files(path);
    CREATE INDEX IF NOT EXISTS idx_files_role ON files(role);
    CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY,
        file_id INTEGER REFERENCES files(id),
        hash TEXT NOT NULL,
        snap_path TEXT NOT NULL,
        created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS plans (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        goal_kind TEXT,
        objective TEXT,
        acceptance_criteria TEXT,
        non_goals TEXT,
        assumed_scope TEXT,
        verification_plan TEXT,
        status TEXT DEFAULT 'active',
        created_at TEXT,
        updated_at TEXT
    );
    """)
    conn.commit()
    conn.close()

def file_hash(path: str) -> str:
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    except Exception:
        return ""
    return h.hexdigest()

def upsert_file(path: str, role: str = None):
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        st = os.stat(path)
        h = file_hash(path)
        now = datetime.now().isoformat()
        if role:
            conn.execute("""
            INSERT INTO files(path, hash, size, mtime, role, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                hash=excluded.hash, size=excluded.size, mtime=excluded.mtime,
                role=excluded.role, updated_at=excluded.updated_at
            """, (path, h, st.st_size, st.st_mtime, role, now, now))
        else:
            conn.execute("""
            INSERT INTO files(path, hash, size, mtime, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                hash=excluded.hash, size=excluded.size, mtime=excluded.mtime,
                updated_at=excluded.updated_at
            """, (path, h, st.st_size, st.st_mtime, now, now))
        conn.commit()
        row = conn.execute("SELECT id FROM files WHERE path=?", (path,)).fetchone()
        return row[0] if row else None
    finally:
        conn.close()

def get_file(path: str):
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute("SELECT * FROM files WHERE path=?", (path,)).fetchone()
        if row:
            cols = [d[0] for d in conn.execute("SELECT * FROM files LIMIT 0").description]
            return dict(zip(cols, row))
        return None
    finally:
        conn.close()

def list_files(role: str = None):
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        if role:
            rows = conn.execute("SELECT * FROM files WHERE role=?", (role,)).fetchall()
        else:
            rows = conn.execute("SELECT * FROM files").fetchall()
        cols = [d[0] for d in conn.execute("SELECT * FROM files LIMIT 0").description]
        return [dict(zip(cols, r)) for r in rows]
    finally:
        conn.close()
