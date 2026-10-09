# Autoformalization Helper

## When to Use

当你想把自然语言描述的数学定义、定理或证明步骤转化为机器可验证的形式化语言（Lean 4 / Coq / Isabelle）时激活。适用于：
- 将论文中的数学段落翻译成 Lean code
- 验证自然语言证明是否有隐藏 gap
- 把算法正确性论证形式化
- 学习形式化语言的惯用写法

不适用：纯自然语言讨论（无需形式化）、没有明确数学结构的定性论证、大规模软件验证（超出单次交互范围）。

## Trigger
- "把这个形式化一下"
- "翻译成 Lean"
- "形式化证明"
- "autoformalize"
- "formalize this"
- "Lean code"

## Workflow

### Step 1: 目标语言确认
确认用户想要的形式化语言：
- **Lean 4**（默认）：数学库最丰富，社区活跃，OpenAI 722 篇手稿使用的语言
- **Coq**：软件验证传统更强，SSReflect 风格适合组合数学
- **Isabelle/HOL**：自动化程度最高，适合快速验证

如果用户不确定，默认推荐 Lean 4。

### Step 2: 概念映射
将自然语言中的每个数学概念映射到形式化库中的对应构造：

| 自然语言 | Lean 4 (mathlib4) | Coq (mathcomp) |
|---------|-------------------|----------------|
| 实数 ℝ | `Real` | `R` |
| 连续函数 | `Continuous` | `continuous` |
| 集合 | `Set α` | `{pred T}` |
| 度量空间 | `MetricSpace` | `Type` + `ball` |
| 群 | `Group` | `fingroup` |

如果概念在库中不存在，给出自定义定义模板。

### Step 3: 形式化翻译
按模块输出代码：

```lean4
import Mathlib

-- 1. 定义/前提
variable {α : Type*} [MetricSpace α]

-- 2. 辅助引理（如果有）
lemma helper (x : α) : ... := by
  ...

-- 3. 主定理
theorem main_theorem (h1 : ...) (h2 : ...) : conclusion := by
  ...
```

每个 tactic 块附上注释说明对应自然语言的哪一步。

### Step 4: Gap 识别
标注形式化过程中发现的 gap：
- **已填充**：自然语言明确，直接翻译
- **需补充**：自然语言隐含了某个步骤，需要额外引理
- **需验证**：自然语言声称"显然"，但实际需要非平凡证明
- **不兼容**：自然语言依赖的数学结构与形式化库版本冲突

### Step 5: 可运行性检查
给出让这段代码跑起来的最小指令：
```bash
# Lean 4
lake new my_project math
# 复制代码到 MyProject/Basic.lean
lake build
```

## Output Format

```
=== 目标语言 ===
Lean 4 (mathlib4)

=== 概念映射 ===
- "实数序列收敛" → `Tendsto u atTop (𝓝 L)`
- "ε-δ 定义" → `Metric.continuous_iff` + `dist x y < δ`
- ...

=== 形式化代码 ===
```lean4
import Mathlib

[代码]
```

=== Gap 分析 ===
| 步骤 | 自然语言 | 形式化状态 | 备注 |
|------|---------|-----------|------|
| 1 | 假设 f 连续 | 已填充 | `hf : Continuous f` |
| 2 | 显然 f 有界 | 需验证 | 需要 Compact + Continuous ↦ Bounded |
| 3 | ... | ... | ... |

=== 运行指令 ===
```bash
...
```

=== 下一步 ===
1. 先补哪个 gap
2. 需要查阅 mathlib 哪个文件
3. 是否有更简洁的形式化路径
```

## Example

用户："形式化：闭区间上的连续函数一定达到最大值。"

Agent：
- 概念映射：闭区间 → `Set.Icc a b`，连续 → `ContinuousOn`，最大值 → `IsMaxOn`
- 代码：用 `ContinuousOn.image_Icc` + `IsCompact.isMaxOn` 的组合
- Gap：自然语言说"显然"，但形式化需要显式构造紧致性证明
- 提供 lake 新建项目的命令

## Resources
- **Lean 4 在线验证**: https://live.lean-lang.org/
- **mathlib4 文档**: https://leanprover-community.github.io/mathlib4_docs/
- **OpenAI math repo**: https://github.com/openai/math （722 篇手稿的 Lean 形式化参考）
- **Coq 在线**: https://jscoq.github.io/

## Notes
- 不要求一次生成完整可编译的代码，重点是框架和 gap 识别
- 如果用户没有 Lean 环境，优先推荐在线验证器
- 与 `proof-outline-generator` 联动：大纲的每一步可以直接对应到 `by` block 的结构
- 与 `algorithm-sketch-agent` 联动：算法的正确性证明可以形式化为不变式验证
