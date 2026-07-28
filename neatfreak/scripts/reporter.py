#!/usr/bin/env python3
"""NeatFreak reporter — generate human-readable cleanup report."""

import json
from scanner import scan_all
from pathlib import Path

def generate_report(output_path: str = "workspace/knowledge/output/neatfreak_report.md") -> str:
    issues = scan_all()
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# NeatFreak Cleanup Report\n", f"**Total Issues:** {len(issues)}\n"]
    severity_order = {"warn": 0, "info": 1}
    issues.sort(key=lambda x: severity_order.get(x.get("severity"), 2))
    by_type = {}
    for i in issues:
        by_type.setdefault(i["type"], []).append(i)
    for t, items in by_type.items():
        lines.append(f"\n## {t} ({len(items)})\n")
        for i in items:
            icon = "⚠️" if i.get("severity") == "warn" else "ℹ️"
            path = i.get("path") or i.get("file") or i.get("name", "")
            lines.append(f"- {icon} `{path}` — {i.get('message','')}")
    out.write_text("\n".join(lines), encoding="utf-8")
    return str(out)

def main():
    out = generate_report()
    print(f"Report written to {out}")

if __name__ == "__main__":
    main()
