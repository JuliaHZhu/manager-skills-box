# Skill: FileStates

## Description

P0 基础层 — 文件状态追踪与写操作代理。所有对 workspace 内文件的修改都应优先走 FileStates 代理工具，自动留下快照与索引，支持回滚与计划模式。

## When to Use

- 每次写入/修改 workspace 内的 source / doc / config / test 类文件时
- 需要为任务建立 plan.md 时
- 需要回滚文件到之前版本时
- 需要标注文件角色（source/test/doc/config/generated/artifact）时

## Tools

### CLI 命令（通过 workspace/skills/filestates/scripts/cli.py）

```bash
# 写文件（自动快照 + 索引）
python workspace/skills/filestates/scripts/cli.py fs_write <path> "<content>" [role]

# 追加写（自动快照）
python workspace/skills/filestates/scripts/cli.py fs_append <path> "<content>"

# 回滚文件 N 个版本
python workspace/skills/filestates/scripts/cli.py fs_rewind <path> [steps]

# 查看追踪状态
python workspace/skills/filestates/scripts/cli.py fs_status [path]

# 设置/查看文件角色
python workspace/skills/filestates/scripts/cli.py fs_role set <path> <role>
python workspace/skills/filestates/scripts/cli.py fs_role get <path>

# 计划管理
python workspace/skills/filestates/scripts/cli.py plan new <name> --objective="..." --goal-kind=feature
python workspace/skills/filestates/scripts/cli.py plan show <name>
python workspace/skills/filestates/scripts/cli.py plan list [active|done]
python workspace/skills/filestates/scripts/cli.py plan update <name> --status=done
```

## Plan Mode Format

创建计划时写入 `.filestates/plan.md`：

```markdown
# Plan: [目标名称]

**Goal Kind:** feature / refactor / research / bugfix
**Objective:** 一句话描述要达成什么
**Acceptance Criteria:**
- [ ] AC1: ...
- [ ] AC2: ...
**Non-goals:** 明确不做什么
**Assumed Scope:** 默认包含/假设的范围
**Verification Plan:** 怎么验证完成了
```

## Rules

1. **优先使用代理工具**：对 source/doc/config/test 文件的修改，优先调用 fs_write/fs_append，而非直接 write_file
2. **自动快照**：fs_write 在覆盖已有文件前自动保存快照到 `.filestates/snapshots/`
3. **角色标注**：新建文件时标注角色，帮助后续 skill 识别文件用途
4. **计划先行**：复杂任务先创建 plan，完成后再标记 status=done
5. **不删文件**：FileStates 只追踪、快照、回滚，不执行删除
