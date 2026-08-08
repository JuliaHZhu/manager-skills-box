---
name: book-card-git-manager
description: |
  管理 book-to-learn 知识卡片项目的 Git 策略：生成 .gitignore、区分源数据与生成物、提供重建命令、处理跨设备迁移。当用户问"知识卡片怎么git管理""卡片项目git策略""book-to-learn git"时激活。
version: 1.2.0
---

# book-card-git-manager — 知识卡片 Git 管理

## ⛔ 核心规则

1. **不 commit 生成物**：cards/ images/ full_text.txt 均可重建
2. **commit 源数据**：items.json 是唯一不可替代的核心资产
3. **commit 进度凭证**：progress.json / daily-progress.md 是学习状态唯一来源
4. **自包含重建**：丢了 cards/ 或 images/ 能通过单条命令秒级恢复

---

## Phase 0：输入验证

**输入**：用户提供的目录路径（可能缺失、错误或非 book-to-learn 项目）
**输出**：验证通过的合法路径，或明确报错

步骤：
1. `test -d <path>` 检查目录是否存在
2. `test -f <path>/items.json` 检查是否为 book-to-learn 项目（唯一必要条件）
3. 若通过 → 进入 Phase 1；若失败 → 按「输入验证失败分支」处理

**输入验证失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| 路径不存在 | `mkdir -p <path>` 创建目录后重试 | 让用户确认路径拼写 |
| 不是 book-to-learn 项目（无 items.json） | 提示"这不是一个已拆书的项目，请先运行 book_setup.py 拆书" | 引导用户到 book-to-learn skill |
| 路径是文件而非目录 | 报错"路径应为目录而非文件" | 让用户重新提供路径 |

---

## Phase 1：诊断当前状态

**输入**：已验证的书项目目录路径
**输出**：该目录下哪些文件该 commit、哪些该 ignore 的分级报告

步骤：
1. `ls -la <path>` 扫描目录，识别已存在文件
2. 对照「文件分级表」输出分级报告
3. **🔴 STOP**：展示报告给用户确认，再继续

### 文件分级表

| 路径 | 是否 commit | 理由 | 重建方式 |
|------|------------|------|---------|
| `items.json` | ✅ 必须 | 所有知识点数据源，丢了卡片全没 | 不可重建 |
| `config.json` | ✅ 必须 | 推送配置 | 不可重建 |
| `index.json` | ✅ 推荐 | 索引 | `gen-index` 重建 |
| `progress.json` | ✅ 必须 | 学习进度唯一凭证 | 不可重建 |
| `daily-progress.md` | ✅ 必须 | 学习日志 | 不可重建 |
| `cards/*.pdf` `cards/*.html` | ❌ ignore | 生成物 | `gen-cards` 重建 |
| `images/*.png` `images/*.jpg` | ❌ ignore | 配图 | `download-imgs` 重建 |
| `full_text.txt` | ❌ ignore | 原始文本，通常 5MB+ | 从原书重新提取 |

**✅ 验证检查点**：报告展示后，用户确认"是/否"，若否 → 询问用户特殊需求后调整

---

## Phase 2：初始化 Git 仓库（如未初始化）

**输入**：书项目目录路径
**输出**：已初始化的 git 仓库

步骤：
1. `git -C <path> rev-parse --git-dir 2>/dev/null` 检查是否已是 git 仓库
2. 若否 → `git init` 初始化
3. **🔴 STOP**：告知用户"已为该项目初始化 git 仓库"，确认后继续

**失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| `git` 命令不存在 | 检查 `which git`；建议 `apt install git` 或 `brew install git` | 告知用户手动安装 git 后继续 |
| 目录无写权限 | `ls -ld <path>` 检查权限；建议 `chmod 755 <path>` | 让用户手动授权 |
| 已是 git 仓库 | 跳过初始化，直接进入 Phase 3 | — |

---

## Phase 3：生成 .gitignore

**输入**：书项目目录路径
**输出**：写入 `.gitignore` 文件

步骤：
1. 检查 `.gitignore` 是否已存在
2. 若不存在 → 直接写入完整规则
3. 若已存在 → `grep "book-to-learn" .gitignore` 检查是否已有本 skill 的规则
4. 若没有 → 追加规则（不覆盖原有内容）；若有 → 提示"规则已存在，跳过"
5. **✅ 验证检查点**：`cat .gitignore` 展示内容，用户确认

```bash
# 在项目根目录执行
cat > .gitignore << 'EOF'
# book-to-learn 生成物（可重建）
cards/*.pdf
cards/*.html
cards/*.png
cards/*.jpg
images/*.png
images/*.jpg
images/*.jpeg
images/*.gif
full_text.txt

# 临时文件
*.tmp
*.log
.DS_Store
__pycache__/
EOF
```

**失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| `.gitignore` 已存在且包含冲突规则 | 展示冲突行，让用户选择保留/覆盖/合并 | 备份原文件为 `.gitignore.bak` 后写入新规则 |
| 无写权限 | 输出规则内容，让用户手动粘贴 | — |

---

## Phase 4：首次 commit 源数据

**输入**：书项目目录路径
**输出**：源数据已安全 commit

步骤：
1. `git add items.json config.json progress.json daily-progress.md index.json`
2. `git commit -m "init: book-to-learn source data"`
3. **✅ 验证检查点**：`git status --short` 确认无未跟踪的源数据、无生成物被意外提交
4. **🔴 STOP**：展示 `git log --oneline -1` 和 `git status`，用户确认后继续

**失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| `git add` 被拒绝（.gitignore 排除） | 检查文件路径是否正确；确认文件不在 .gitignore 中 | 强制 add：`git add -f <file>` |
| `git commit` 报错（未配置 user.name/email） | `git config user.name "Name" && git config user.email "email@example.com"` | 输出配置命令让用户执行 |
| 生成物被意外 `git add` | `git reset HEAD <file>` 取消暂存，检查 .gitignore 是否生效 | 重新生成 .gitignore 并确认规则正确 |

---

## Phase 5：重建命令

**触发条件**：cards/ 或 images/ 丢失、或换设备 clone 后
**输出**：恢复完整的 cards/ 和 images/

步骤：
1. 确认 `items.json` 存在
2. 依次执行重建命令
3. **✅ 验证检查点**：`ls cards/ | wc -l` 检查卡片数量是否与 `items.json` 中的条目数一致

```bash
cd skills/book-to-learn
python3 book_setup.py gen-cards --slug <book-slug>
python3 book_setup.py gen-index --slug <book-slug>
python3 book_setup.py download-imgs --slug <book-slug>
```

**失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| `book_setup.py` 找不到 | 检查 skill 安装路径；用 `find ~ -name book_setup.py` 定位 | 告知用户手动运行 `pip install` 重装 book-to-learn skill |
| `gen-cards` 报错 | 检查 `items.json` 是否存在且格式正确（`python3 -m json.tool items.json`） | 从 git 历史恢复 `items.json`：`git checkout HEAD -- items.json` |
| `download-imgs` 网络失败 | 重试 3 次 | 跳过配图，继续推送（PDF 不依赖图片也能生成） |
| 卡片数量不一致 | 对比 `jq '. | length' items.json` 和 `ls cards/ | wc -l` | 删除 cards/ 重新生成 |

---

## Phase 6：跨设备迁移

**场景**：换新电脑，clone 已有项目，恢复到可推送状态

步骤：
1. `git clone <repo-url>`
2. `cd books/<slug>/`
3. 运行 Phase 5 重建命令恢复 cards/ 和 images/
4. 检查 `progress.json` 确认断点（`jq '.current_index' progress.json`）
5. **✅ 验证检查点**：确认 cards/ 目录存在且非空、progress.json 可读
6. 继续从断点推送

**失败分支**：

| 症状 | 一线修复 | 兜底 |
|------|---------|------|
| `progress.json` 丢失 | `git checkout HEAD -- progress.json` 从 git 恢复 | git 中也没有 → 回到第一张重新推送 |
| `items.json` 丢失 | `git checkout HEAD -- items.json` 从 git 恢复 | git 中也没有 → **项目报废**，必须从原书重新拆书 |
| clone 后无 cards/ 且重建失败 | 检查 items.json 是否存在 → 进入 Phase 5 | items.json 也没有 → 项目报废 |
| `jq` 不可用 | `python3 -c "import json; print(json.load(open('progress.json'))['current_index'])"` | 让用户手动查看 progress.json |

---

## Phase 7：仓库健康检查

**场景**：用户想确认现有仓库是否符合最佳实践
**输出**：诊断报告

步骤：
1. `git status --short` —— 检查是否有未 commit 的源数据或已 track 的生成物
2. `du -sh cards/ images/ 2>/dev/null` —— 检查生成物是否意外被 track（尺寸异常大）
3. `git ls-files | grep -E "\.(pdf|png|jpg|gif)$"` —— 检查是否有生成物在 git 中
4. **✅ 验证检查点**：输出健康检查报告

**健康检查判定**：

| 检查项 | 通过标准 | 失败处理 |
|--------|---------|---------|
| 无未 commit 源数据 | `git status --short` 不显示 items.json/config.json/progress.json | `git add` 并 commit |
| 无生成物被 track | `git ls-files | grep "cards/\|images/"` 为空 | 从 git 移除并加入 .gitignore：`git rm --cached -r cards/ images/` |
| repo 体积合理 | `du -sh .git/` < 10MB（纯文本源数据） | 查找并清理被误 track 的大文件 |

---

## 反例黑名单（不要做的事）

| # | 反模式 | 后果 | 正确做法 |
|---|--------|------|---------|
| 1 | 把 `cards/*.pdf` commit 进 git | repo 体积爆炸，100 张 PDF = 50MB+ | 写 .gitignore 排除，靠脚本重建 |
| 2 | 不 commit `progress.json` | 换电脑后不知道推到第几张，会重复推送 | 必须 commit |
| 3 | 不 commit `items.json` | 项目核心资产丢失，卡片内容永久消失 | 必须 commit |
| 4 | 把 `full_text.txt` commit 进 git | 单文件 5MB+，拖慢 clone | 写 .gitignore 排除 |
| 5 | 直接 `rm -rf cards/` 不保留 items.json | 所有卡片内容永久丢失 | 先确认 items.json 已备份/已 commit 再清理 |
| 6 | 重建时覆盖未 commit 的 progress.json | 学习进度回滚 | 重建前先 `git add progress.json daily-progress.md && git commit` |
| 7 | `git add .` 一键提交全部 | 把生成物也 add 进去 | 明确指定源数据文件：`git add items.json config.json progress.json daily-progress.md` |
| 8 | 忽略 `.gitignore` 本身 | 队友 clone 后生成物又被 track | `.gitignore` 必须 commit |

---

## 速查：一句话判断

> 问：这个文件能不能通过 `items.json` + `book_setup.py` 重建？
> 能 → ignore。不能 → commit。

---

## 快速启动模板（新项目一键设置）

用户说"新建了一本书，帮我设置好 git"时，按以下顺序执行：

```bash
cd books/<slug>/
# Phase 0: 输入验证（确认 items.json 存在）
test -f items.json || echo "ERROR: not a book-to-learn project"
# Phase 2: 初始化 git
git init
# Phase 3: 生成 .gitignore
cat > .gitignore << 'EOF'
# book-to-learn 生成物（可重建）
cards/*.pdf
cards/*.html
cards/*.png
cards/*.jpg
images/*.png
images/*.jpg
images/*.jpeg
images/*.gif
full_text.txt
*.tmp
*.log
.DS_Store
__pycache__/
EOF
# Phase 4: 首次 commit 源数据
git add items.json config.json progress.json daily-progress.md index.json .gitignore
git commit -m "init: book-to-learn source data"
# Phase 5: 重建生成物
python3 ../../book_setup.py gen-cards --slug <slug>
python3 ../../book_setup.py gen-index --slug <slug>
python3 ../../book_setup.py download-imgs --slug <slug>
# Phase 7: 健康检查
git status --short
git ls-files | grep -E "\.(pdf|png|jpg)$" && echo "WARNING: tracked artifacts found" || echo "OK"
```
