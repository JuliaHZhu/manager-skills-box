---
name: training-effect-measurer
description: Measure training effectiveness using Kirkpatrick's four-level model adapted for enterprise context, plus Huawei's training conversion rate methodology. Covers reaction, learning, behavior, and result-level evaluation, with focus on linking training investment to business outcomes. Use when the user needs to prove training ROI, redesign evaluation systems, or stop measuring the wrong things.
---

# training-effect-measurer

## When to Activate

Trigger when the user mentions:
- 培训效果评估 / training effectiveness evaluation
- 培训ROI / training return on investment
- 柯氏四级评估 / Kirkpatrick four levels
- 培训转化率 / training conversion rate
- 怎么证明培训有用 / how to prove training works
- 培训满意度 vs 培训效果 / satisfaction vs effectiveness
- 培训评估怎么做 / how to evaluate training

## Core Framework: Four-Level Evaluation (四级评估)

华为采用的培训效果评估体系，从感性反应到业务结果逐层深入：

| Level | Name | Question | Method | Common Trap |
|---|---|---|---|---|
| **L1** | 反应层 Reaction | 学员喜欢这次培训吗？ | 满意度问卷 | ❌ 把满意度当唯一指标 |
| **L2** | 学习层 Learning | 学员学到了什么？ | 考试、答辩、案例分析 | ❌ 考过了=学会了 |
| **L3** | 行为层 Behavior | 学员回到岗位后行为改变了吗？ | 上级观察、360度评估、行为举证 | ❌ 短期观察，无持续跟踪 |
| **L4** | 结果层 Result | 培训对业务指标产生了什么影响？ | 绩效数据对比、项目成果、ROI计算 | ❌  attribution gap（无法区分是培训还是其他因素） |

## Huawei's Key Metric: Training Conversion Rate (培训转化率)

> "成功不是知不知，而是用不用。"

华为关注的终极指标不是考试分数，而是**培训后行为改变产生的业务价值**。

### Conversion Rate Formula

```
培训转化率 = 培训后产生可衡量业务价值的人数 / 参加培训的总人数

或者：
培训投资回报率 = (培训后业务收益增量 - 培训成本) / 培训成本
```

### Measurement Chain

```
培训投入
    ↓
学员参与（出勤率）
    ↓
学习通过（考试/答辩通过率）
    ↓
行为改变（上级评估：是否在用新方法）
    ↓
业务结果（销售额↑、故障率↓、周期↓、客户满意度↑）
    ↓
ROI计算
```

## Level-by-Level Implementation

### L1: Reaction — Make It Useful, Not Just Happy

- **不要只问“满意吗”**，要问：
  - 内容与实际工作相关度？（1-5分）
  - 讲师实战经验丰富度？
  - 你会向同事推荐这个培训吗？（NPS式问题）
- **淘汰阈值**：相关性评分 < 3分的课程，强制复盘或下架

### L2: Learning — Test Application, Not Memory

- **拒绝死记硬背**：考试题目必须是案例分析和场景判断
- **答辩制**：学员输出真实案例应用分析，专家组评审
- **华为实践**：新员工必须通过编程基础考试（100分满分）和编程规范考试（90分及格），三次机会，不过淘汰

### L3: Behavior — The Hardest and Most Important

- **3个月跟踪**：培训结束后1个月、3个月、6个月分别评估
- **上级举证**：学员上级需在述职中明确说明“该员工培训后哪些行为改变了”
- **述职捆绑**：华为要求导师在述职中汇报培养成果；培训管理者也要汇报培训转化情况

### L4: Result — Link to Business Metrics

| Training Type | Result Metric Example |
|---|---|
| 销售技巧培训 | 培训组 vs 对照组：成单率、客单价、回款周期 |
| 项目管理培训 | 项目按时交付率、预算偏差率 |
| 技术培训 | 故障解决时间、客户投诉率 |
| 领导力培训 | 团队绩效提升、关键人才保留率 |

## Attribution Challenge: How to Isolate Training Impact

培训效果很难100%归因，华为采用以下方法：

1. **对照组**：培训组 vs 未培训组的同期绩效对比
2. **时间序列**：培训前6个月 vs 培训后6个月的趋势变化
3. **多源验证**：绩效数据 + 上级评估 + 客户反馈 + 自我报告交叉印证
4. **保守估算**：只计算可明确归因的部分，不夸大

## Implementation Checklist

- [ ] 为每个培训项目定义L4结果指标（培训前就定好）
- [ ] 设计L2评估方式（案例考试、答辩、实操演练）
- [ ] 建立L3跟踪机制（3个月、6个月行为评估）
- [ ] 设计满意度问卷（聚焦相关性、实用性，而非泛泛的“满意”）
- [ ] 建立培训档案（谁参加了什么培训、考试成绩、行为跟踪、业务结果）
- [ ] 要求业务部门参与评估（上级评估、绩效数据提供）
- [ ] 定期输出培训ROI报告（给管理层看，争取资源）
- [ ] 建立课程淘汰机制（连续两期转化率低的课程下架）

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| 只测满意度 | 学员满意的课不一定有用， challenging 的课满意度低但价值高 |
| 考完就算 | 考过了不代表工作中会用 |
| 无对照组 | 无法区分是培训效果还是市场/管理变化 |
| 让培训部自己评估自己 | 利益相关，数据可信度低 |
| 追求100%归因 | 过度精确导致无法行动；接受近似估算 |

## Example Interaction

**User**: 老板总说培训花钱没效果，我怎么证明培训有价值？

**Skill Response**:
> 你需要把评估从L1（满意度）拉到L4（业务结果），并且**在培训前就约定好指标**。
>
> **第一步：选一个能打赢的仗**
> - 不要试图证明“所有培训都有价值”，选一个业务痛点最清晰的培训项目
> - 例如：销售成单率低 → 销售技巧培训
>
> **第二步：培训前定指标**
> - 与业务部门共识：培训后3个月，成单率从X%提升到Y%
> - 定义对照组：同期未参加培训的销售团队
>
> **第三步：改造评估方式**
> - L2：不用选择题，用真实客户案例模拟谈判，录像评审
> - L3：培训后1个月、3个月，销售主管评估“是否在用新方法”
> - L4：追踪培训组 vs 对照组的成单率、客单价
>
> **第四步：输出报告**
> - 培训投入：讲师费X + 学员工时成本Y = 总成本Z
> - 培训产出：培训组成单率提升A% → 增量收入B
> - ROI = (B - Z) / Z
>
> **关键原则**：哪怕只做一个项目，只要有清晰的ROI，老板就会相信培训可以创造价值。从0到1比从1到100难。