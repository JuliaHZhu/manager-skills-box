# 分析笔记制作流程

将五工具流水线分析结果做成独立HTML分析笔记，挂在原文lesson页面上。

## 触发条件

- 用户读完某章节后说"这个有意思，用直觉泵分析"
- 用户对某主张/论述提出质疑或展开讨论
- 用户说"把这个分析写下来"

## 文件结构

```
~/wiki/lessons/<book>/notes-chXX.html
```

与原文lesson同目录，命名 `notes-chXX.html`（XX为章节号）。

## HTML模板要点

- 与原文页一致的配色（米黄底 #fdfbf7，棕色系 #2c2416/#3d2715/#8b6d45）
- 使用 `.callout`（黄色左边框）、`.key-point`（绿色边框）、`.scroll`（居中容器）
- 每节一个 `h2`，工具间用明显分界
- 表格宽度 `width:100%`，`border-collapse:collapse`
- 底部导航：`← 回到原文 | ↑ 返回目录`

## 链接规则

在原文lesson.html的导航栏插入 `📝 分析笔记` 链接：
```html
<div class="nav">
<a href="ch09.html">← 上一章</a>
<a href="notes-ch10.html" style="color:#b45309">📝 分析笔记</a>
<a href="ch11.html">下一章 →</a>
</div>
```

## 内容结构

依次使用五工具（不需要全用，选最相关的）：

### 第一步：故意堆积检测
- 拆开多层主张（A/B/C表）
- 标注哪个主张最脆弱

### 第二步：假设猎手
- 层层回溯，找出隐藏假设
- 标注"承重墙"（最底层的脆弱假设）

### 第三步：旋钮检测
- 用表格：旋钮 | 原文设定 | 拧回 | 直觉变化
- 至少拧4个旋钮

### 第四步：归谬法
- 接受全部前提，推三层
- 找到矛盾后溯源到具体前提

### 第五步：三视角
- 物理/制度/博弈三列表格
- 找立场错配

## 用户追加判断

分析完成后用户经常会补充自己的判断。这些应该作为"第六步"或"更好的比喻"加入笔记——用callout或key-point包装，标注为用户的独立洞见而非工具链产出。

## 实战案例

- `~/wiki/lessons/fooled-by-randomness/notes-ch10.html` — 赢家通吃分析
- `~/wiki/lessons/fooled-by-randomness/notes-ch12.html` — 鸽子vs麻将玩家
