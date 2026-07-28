#!/usr/bin/env python3
"""FileStates CLI entry — unified commands."""

import sys
from fs_proxy import fs_write, fs_append, fs_rewind, fs_status, fs_role_set, fs_role_get
from plan_manager import new_plan, get_plan, list_plans, update_plan

def main():
    if len(sys.argv) < 2:
        print("""FileStates CLI
Commands:
  fs_write <path> <content> [role]     Write file with snapshot
  fs_append <path> <content>           Append to file with snapshot
  fs_rewind <path> [steps]             Rewind file N snapshots
  fs_status [path]                     Show tracked files
  fs_role set|get <path> [role]        Manage file roles
  plan new <name> [--key=value ...]    Create/update plan
  plan show <name>                     Show plan details
  plan list [active|done]              List plans
  plan update <name> --status=done     Update plan
""")
        return
    cmd = sys.argv[1]
    if cmd == "fs_write":
        path, content = sys.argv[2], sys.argv[3]
        role = sys.argv[4] if len(sys.argv) > 4 else "source"
        print(fs_write(path, content, role))
    elif cmd == "fs_append":
        print(fs_append(sys.argv[2], sys.argv[3]))
    elif cmd == "fs_rewind":
        print(fs_rewind(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1))
    elif cmd == "fs_status":
        print(fs_status(sys.argv[2] if len(sys.argv) > 2 else "."))
    elif cmd == "fs_role":
        sub = sys.argv[2]
        if sub == "set":
            print(fs_role_set(sys.argv[3], sys.argv[4]))
        else:
            print(fs_role_get(sys.argv[3]))
    elif cmd == "plan":
        sub = sys.argv[2]
        if sub == "new":
            name = sys.argv[3]
            kwargs = {}
            for arg in sys.argv[4:]:
                if arg.startswith("--") and "=" in arg:
                    k, v = arg[2:].split("=", 1)
                    kwargs[k.replace("-", "_")] = v
            print(new_plan(name, **kwargs))
        elif sub == "show":
            print(get_plan(sys.argv[3]))
        elif sub == "list":
            print(list_plans(sys.argv[3] if len(sys.argv) > 3 else None))
        elif sub == "update":
            name = sys.argv[3]
            kwargs = {}
            for arg in sys.argv[4:]:
                if arg.startswith("--") and "=" in arg:
                    k, v = arg[2:].split("=", 1)
                    kwargs[k.replace("-", "_")] = v
            print(update_plan(name, **kwargs))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
