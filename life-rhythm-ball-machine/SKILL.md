# life-rhythm-ball-machine

🎱 生活节律球机 —— 比例化作息、每日三球、不可修改的执行系统

## 触发条件

当用户提到以下任一关键词时激活：
- 生活节律 / 作息管理 / 比例化日程
- 每日三球 / 踩一脚 / 球机
- 不可修改的执行 / 信任契约
- 比例装填 / 装填周期
- 生活管理工具 / 日程系统 / 自律工具
- life rhythm / ball machine / daily schedule

## 核心概念

- **球 (Ball)**：一个最小可执行任务，例如「读 20 页书」「午睡 30 分钟」。
- **球库 (Ball Library)**：用户自建的任务池，按类别（读书、休息、社交等）组织。
- **周期 (Cycle)**：一次装填产生 N 天的完整球池，期间不可修改。
- **每日三球**：早场 (08:00-11:00)、午场 (13:00-17:00)、晚场 (19:00-23:00)，每天固定三个时段各执行一球。
- **信任契约**：装填完成后，当前周期的球池和日程锁定，只能「完成」或「跳过」，不能修改。

## 使用方式

### 方式一：通过 nanobot 对话使用（推荐）

用户发送自然语言指令，AI 调用底层 CLI/核心引擎完成操作。

### 方式二：直接 CLI

```bash
cd skills/life-rhythm-ball-machine/scripts

# 角色管理
python3 cli.py profile create lei --name 雷管 --emoji 🐧
python3 cli.py profile list
python3 cli.py profile switch lei

# 球库管理
python3 cli.py library add 读书 "读《黑天鹅》20页" --energy medium
python3 cli.py library list
python3 cli.py library import 读书 /path/to/books.txt --tag #书单

# 装填周期（10天，比例：读书30% 休息30% 探索20% 社交20%）
python3 cli.py fill --days 10 --proportion 读书:30,休息:30,探索:20,社交:20 \
                    --min-energy low --fun-balls 5

# 每日操作
python3 cli.py draw          # 踩一脚，生成今日三球
python3 cli.py today         # 查看今日三球状态
python3 cli.py complete morning    # 完成早场
python3 cli.py skip evening        # 跳过晚场

# 统计与报告
python3 cli.py status        # 周期进度
python3 cli.py stats         # 生涯统计
python3 cli.py report        # 综合报告
python3 cli.py cron          # 早报生成
```

## CLI 命令速查表

| 命令 | 说明 |
|------|------|
| `profile create <id>` | 创建角色 |
| `profile list` | 列出角色 |
| `profile switch <id>` | 切换角色 |
| `library add <cat> <content>` | 添加球到球库 |
| `library list [--category <cat>]` | 查看球库 |
| `library remove <cat> <ball_id>` | 删除球 |
| `library import <cat> <file>` | 导入收藏夹（txt/json/md） |
| `fill --days N --proportion A:a,B:b...` | 装填周期 |
| `draw` | 抽取/查看今日三球 |
| `today` | 查看今日三球状态 |
| `complete <morning/afternoon/evening>` | 完成场次 |
| `skip <morning/afternoon/evening>` | 跳过场次 |
| `status` | 周期状态与进度 |
| `stats` | 生涯统计 |
| `report` | 综合报告 |
| `cron` | 生成早报 |

## 数据持久化

- 单文件 JSON 数据库：`workspace/data/life-rhythm-state.json`
- 可通过环境变量 `LIFE_RHYTHM_DB` 覆盖路径
- 多角色隔离：每个角色拥有独立的球库、周期、历史

## 文件结构

```
skills/life-rhythm-ball-machine/
├── SKILL.md                    # 本文件
├── PRD.md                      # 产品需求文档
├── scripts/
│   ├── cli.py                  # CLI 入口
│   ├── core.py                 # 核心引擎（球池生成、抽取、统计）
│   ├── db.py                   # JSON 数据库层
│   ├── fun_balls.json          # 内置趣味球库
│   └── test_prd.py             # PRD 逐行对照测试
└── references/                 # 参考文档（可选）
```

## 技术依赖

- Python 3.10+
- 无外部依赖（纯标准库）

## 内置趣味球库

`scripts/fun_balls.json` 包含以下类别的趣味球：
- 读书（4 个）
- 休息（4 个）
- 自由探索（6 个）
- 社交（5 个）
- 运动（4 个）
- 创作（4 个）

装填时通过 `--fun-balls N` 混入 N 个趣味球。

## 能量分级

- **high**：高能量活动（深度工作、高强度运动）
- **medium**：中等能量活动（阅读、轻度社交）
- **low**：低能量活动（休息、散步、冥想）

装填时 `--min-energy low` 可保证每天至少有一个低能量球。
