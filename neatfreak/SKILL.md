# Skill: NeatFreak

## Description

P2 治理层 — 知识库与代码库的质量巡检官。整合 FileStates、CodeGraph、WikiBrain 的索引，执行三档清理模式：Scan（只检测）、Fix（确定性修复）、Clean（深度清理需确认）。

## When to Use

- 定期巡检知识库/代码库质量时
- 发现 wiki 页面孤立、链接失效、元数据缺失时
- 怀疑存在死代码或无引用函数时
- 需要归档长期未修改的文件时
- 用户主动要求"整理/清理/巡检"时

## Dependencies

- **FileStates** (P0)
- **CodeGraph** (P1)
- **WikiBrain** (P1)

## Tools

### CLI Commands

```bash
# 扫描问题
python workspace/skills/neatfreak/scripts/cli.py scan

# 生成清理报告
python workspace/skills/neatfreak/scripts/cli.py report [output_path]

# 自动修复确定性问题（默认 dry-run）
python workspace/skills/neatfreak/scripts/cli.py fix [--apply]

# 归档建议
python workspace/skills/neatfreak/scripts/cli.py archive suggest [days]
python workspace/skills/neatfreak/scripts/cli.py archive move <file> [--apply]
```

## Three Modes

| Mode | Behavior | Safety | Typical Action |
|------|----------|--------|----------------|
| **Scan** | 只检测，不改任何东西 | 🟢 完全安全 | 找问题、列建议、按严重程度排序 |
| **Fix** | 只修确定性问题 | 🟡 低风险 | 补 frontmatter、修正格式 |
| **Clean** | 深度清理，需 agent 逐一确认 | 🔴 需监督 | 合并重复页、归档陈旧内容 |

## Safety Rules

1. **Never delete source/test/config files** without human confirmation
2. **Never auto-merge wiki pages** — only suggest
3. **Never auto-archive files < 30 days old**
4. Safe auto-fixes: missing frontmatter, markdown formatting, dead link correction

## Rules

1. 每次运行先 `scan` 生成完整问题清单
2. 按 severity 排序：warn 优先于 info
3. `fix --apply` 只能执行确定性修复
4. 所有删除/合并/归档操作必须经 agent 判断，脚本只提供候选清单
5. 参考 `references/safety_rules.md` 和 `references/cleanup_patterns.md`
