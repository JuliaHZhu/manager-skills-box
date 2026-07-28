#!/usr/bin/env python3
"""NeatFreak CLI entry."""

import sys
import json
from scanner import scan_all
from reporter import generate_report
from fixer import apply_safe_fixes
from archiver import suggest_archive, archive_file

def main():
    if len(sys.argv) < 2:
        print("""NeatFreak CLI
Commands:
  scan                    Detect issues across wiki/code/files
  report [output_path]    Generate cleanup report
  fix [--apply]           Auto-fix deterministic issues (default dry-run)
  archive suggest [days]  List stale file suggestions
  archive move <file> [--apply]  Move file to .archive/
""")
        return
    cmd = sys.argv[1]
    if cmd == "scan":
        print(json.dumps(scan_all(), indent=2, ensure_ascii=False))
    elif cmd == "report":
        out = sys.argv[2] if len(sys.argv) > 2 else "workspace/knowledge/output/neatfreak_report.md"
        print(generate_report(out))
    elif cmd == "fix":
        dry = "--apply" not in sys.argv
        print(json.dumps(apply_safe_fixes(dry_run=dry), indent=2, ensure_ascii=False))
    elif cmd == "archive":
        sub = sys.argv[2] if len(sys.argv) > 2 else "suggest"
        if sub == "suggest":
            days = int(sys.argv[3]) if len(sys.argv) > 3 else 180
            print(json.dumps(suggest_archive(days), indent=2, ensure_ascii=False))
        elif sub == "move":
            f = sys.argv[3]
            dry = "--apply" not in sys.argv
            print(json.dumps(archive_file(f, dry), indent=2, ensure_ascii=False))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
