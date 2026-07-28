#!/usr/bin/env python3
"""Blast Radius — bounded best-first search for impact analysis."""

import os
import sqlite3
from collections import deque
from schema import DB_PATH

def blast_radius(node_name: str, max_nodes: int = 500, edge_kinds=None):
    """Find all nodes reachable from node_name via code edges (call/import/inherits/uses)."""
    if edge_kinds is None:
        edge_kinds = {"calls", "imports", "inherits", "uses"}
    conn = sqlite3.connect(DB_PATH)
    try:
        # Find starting node id
        row = conn.execute(
            "SELECT id FROM code_nodes WHERE name=? LIMIT 1", (node_name,)
        ).fetchone()
        if not row:
            return {"error": f"Node '{node_name}' not found"}
        start_id = row[0]
        visited = set([start_id])
        queue = deque([(start_id, 0)])
        results = [{"id": start_id, "depth": 0}]
        while queue and len(results) < max_nodes:
            nid, depth = queue.popleft()
            rows = conn.execute(
                "SELECT dst_id, kind FROM code_edges WHERE src_id=? UNION SELECT src_id, kind FROM code_edges WHERE dst_id=?",
                (nid, nid)
            ).fetchall()
            for dst, kind in rows:
                if kind not in edge_kinds:
                    continue
                if dst not in visited:
                    visited.add(dst)
                    results.append({"id": dst, "depth": depth + 1})
                    queue.append((dst, depth + 1))
                    if len(results) >= max_nodes:
                        break
        # Fetch details
        ids = [r["id"] for r in results]
        placeholders = ",".join("?" * len(ids))
        details = conn.execute(
            f"SELECT id, file_id, kind, name, start_line, end_line, signature, language FROM code_nodes WHERE id IN ({placeholders})",
            ids
        ).fetchall()
        detail_map = {d[0]: d for d in details}
        enriched = []
        for r in results:
            d = detail_map.get(r["id"])
            if d:
                enriched.append({
                    "id": d[0], "file_id": d[1], "kind": d[2], "name": d[3],
                    "start_line": d[4], "end_line": d[5], "signature": d[6],
                    "language": d[7], "depth": r["depth"]
                })
        return {"start": node_name, "nodes_found": len(enriched), "nodes": enriched}
    finally:
        conn.close()

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: blast_radius.py <node_name> [max_nodes]")
        return
    name = sys.argv[1]
    max_n = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    import json
    print(json.dumps(blast_radius(name, max_n), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
