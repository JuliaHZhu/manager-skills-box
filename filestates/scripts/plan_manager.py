#!/usr/bin/env python3
"""Plan mode manager — Grok Build style plan.md."""

import os
import sqlite3
from pathlib import Path
from datetime import datetime
from index_manager import ensure_db, DB_PATH

PLAN_MD = Path("workspace/.filestates/plan.md")

def ensure_plan_table():
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
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

def new_plan(name: str, goal_kind: str = "feature", objective: str = "",
             acceptance_criteria: str = "", non_goals: str = "",
             assumed_scope: str = "", verification_plan: str = ""):
    ensure_plan_table()
    now = datetime.now().isoformat()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("""
        INSERT INTO plans(name, goal_kind, objective, acceptance_criteria,
                          non_goals, assumed_scope, verification_plan, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            goal_kind=excluded.goal_kind, objective=excluded.objective,
            acceptance_criteria=excluded.acceptance_criteria, non_goals=excluded.non_goals,
            assumed_scope=excluded.assumed_scope, verification_plan=excluded.verification_plan,
            status=excluded.status, updated_at=excluded.updated_at
        """, (name, goal_kind, objective, acceptance_criteria, non_goals,
              assumed_scope, verification_plan, "active", now, now))
        conn.commit()
        sync_plan_md()
        return True
    finally:
        conn.close()

def get_plan(name: str):
    ensure_plan_table()
    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute("SELECT * FROM plans WHERE name=?", (name,)).fetchone()
        if row:
            cols = [d[0] for d in conn.execute("SELECT * FROM plans LIMIT 0").description]
            return dict(zip(cols, row))
        return None
    finally:
        conn.close()

def list_plans(status: str = None):
    ensure_plan_table()
    conn = sqlite3.connect(DB_PATH)
    try:
        if status:
            rows = conn.execute("SELECT * FROM plans WHERE status=? ORDER BY updated_at DESC", (status,)).fetchall()
        else:
            rows = conn.execute("SELECT * FROM plans ORDER BY updated_at DESC").fetchall()
        cols = [d[0] for d in conn.execute("SELECT * FROM plans LIMIT 0").description]
        return [dict(zip(cols, r)) for r in rows]
    finally:
        conn.close()

def update_plan(name: str, **kwargs):
    ensure_plan_table()
    allowed = {"goal_kind", "objective", "acceptance_criteria", "non_goals",
               "assumed_scope", "verification_plan", "status"}
    updates = {k: v for k, v in kwargs.items() if k in allowed}
    if not updates:
        return False
    conn = sqlite3.connect(DB_PATH)
    try:
        sets = ", ".join(f"{k}=?" for k in updates)
        vals = list(updates.values()) + [datetime.now().isoformat(), name]
        conn.execute(f"UPDATE plans SET {sets}, updated_at=? WHERE name=?", vals)
        conn.commit()
        sync_plan_md()
        return True
    finally:
        conn.close()

def sync_plan_md():
    plans = list_plans()
    lines = ["# FileStates Plans\n"]
    for p in plans:
        status_icon = "✅" if p.get("status") == "done" else "🟡" if p.get("status") == "active" else "⚪"
        lines.append(f"## {status_icon} {p['name']} ({p.get('goal_kind','')})\n")
        lines.append(f"**Objective:** {p.get('objective','')}\n")
        lines.append(f"**Status:** {p.get('status','')}\n")
        lines.append(f"**AC:** {p.get('acceptance_criteria','')}\n")
        lines.append(f"**Non-goals:** {p.get('non_goals','')}\n")
        lines.append(f"**Scope:** {p.get('assumed_scope','')}\n")
        lines.append(f"**Verify:** {p.get('verification_plan','')}\n")
        lines.append(f"_Updated: {p.get('updated_at','')}_\n")
    PLAN_MD.parent.mkdir(parents=True, exist_ok=True)
    PLAN_MD.write_text("\n".join(lines), encoding="utf-8")
