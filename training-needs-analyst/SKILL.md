---
name: training-needs-analyst
description: Analyze organizational training needs using Huawei's "Three Hard + Three Soft" framework. Identifies gaps between current and required capabilities, aligns training investment with business strategy, and prioritizes training projects by ROI. Use when the user needs to determine what training is truly needed, avoid training waste, or design a training curriculum tied to business outcomes.
---

# training-needs-analyst

## When to Activate

Trigger when the user mentions:
- 培训需求分析 / training needs analysis (TNA)
- 三硬三软 / capability gaps
- 培训预算怎么花 / training budget allocation
- 培训与业务脱节 / training not aligned with business
- 训什么、不训什么 / what to train, what to skip
- 培训项目立项 / training project justification

## Core Framework: Three Hard + Three Soft (三硬三软)

华为培训需求分析的六维框架，从组织战略到个人差距逐层分解：

### 三硬 (Hard Dimensions — Measurable)

| Dimension | Question | Data Sources |
|---|---|---|
| **战略硬需求** | 未来1-3年业务战略需要什么新能力？ | 战略规划、BLM输出、SP/BP |
| **岗位硬标准** | 关键岗位的任职资格标准是什么？ | 任职资格体系、岗位说明书 |
| **绩效硬差距** | 当前绩效与目标的量化差距有多大？ | 绩效考核数据、项目复盘 |

### 三软 (Soft Dimensions — Observable)

| Dimension | Question | Data Sources |
|---|---|---|
| **文化软渗透** | 员工价值观和行为是否符合公司文化？ | 360度评估、文化审计、离职访谈 |
| **士气软信号** | 团队氛围、敬业度、流失率有何异常？ | 敬业度调研、流失率分析 |
| **潜力软观察** | 高潜人才的能力短板在哪里？ | 人才盘点、IDP反馈、上级观察 |

## The Training Needs Analysis Process

```
Step 1: 组织层面分析
    └─ 公司战略 → 关键成功要素 → 组织能力缺口

Step 2: 任务/岗位层面分析
    └─ 岗位职责 → 任职资格 → 知识/技能/素质要求

Step 3: 人员层面分析
    └─ 现任者能力测评 → 与标准差距 → 培训优先级排序

Step 4: 培训项目确认
    └─ 差距可否通过培训解决？ → 是：立项 / 否：转HR/组织干预
```

### Critical Filter: Is This Really a Training Problem?

> 培训能解决的只是“能力缺口”；如果是“意愿问题”“组织设计问题”“流程问题”，培训无效。

| Problem Type | Symptom | Solution |
|---|---|---|
| **知识缺口** | 员工不知道怎么做 | ✅ 培训 |
| **技能缺口** | 员工知道但做不对 | ✅ 训战结合 |
| **态度/意愿** | 员工不愿做 | ❌ 培训无效 → 激励/文化/淘汰 |
| **资源限制** | 想做但没资源 | ❌ 培训无效 → 资源调配 |
| **流程障碍** | 流程不允许做 | ❌ 培训无效 → 流程变革 |
| **标准模糊** | 不知道做到什么程度算好 | ❌ 培训无效 → 标准化/任职资格 |

## Training Project ROI Estimation

华为将培训视为投资，每个项目需要估算投入产出：

```
培训转化率 = 培训后行为改变产生的业务价值 / 培训总投入

关键测算点：
1. 不参与培训的现状成本（错误率、低效率、流失、客户投诉）
2. 培训后的预期改善（量化指标：销售额↑、故障率↓、周期↓）
3. 培训直接成本（讲师、场地、学员时间机会成本）
```

### Priority Matrix

| 高业务影响 + 高能力缺口 | → 立即投入，重点保障 |
| 高业务影响 + 低能力缺口 | → 少量投入，维持即可 |
| 低业务影响 + 高能力缺口 | → 选择性投入，或缓行 |
| 低业务影响 + 低能力缺口 | → 不投入 |

## Implementation Checklist

- [ ] 获取未来1-3年业务战略和关键举措
- [ ] 识别支撑战略的关键岗位群（20%岗位创造80%价值）
- [ ] 梳理关键岗位的任职资格标准
- [ ] 对现任者进行能力测评（考试、述职、360度）
- [ ] 量化差距：人数×差距程度×影响权重
- [ ] 过滤非培训问题（意愿/资源/流程/标准）
- [ ] 按优先级矩阵排序培训项目
- [ ] 为每个项目估算ROI（现状成本 vs 预期收益 vs 培训投入）
- [ ] 形成年度培训计划，与业务部门确认

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| 培训需求由培训部门“拍脑袋” | 脱离业务，学非所用 |
| 全员覆盖式培训 | 资源稀释，关键岗位得不到充分培养 |
| 只问“想学什么”不问“该学什么” | 员工倾向舒适区，回避真正短板 |
| 把培训当成福利 | 学员无压力，学习效果差 |
| 不做差距分析直接买课程 | 课程与真实需求错配 |

## Example Interaction

**User**: 明年培训预算砍了一半，怎么决定哪些培训保留、哪些砍掉？

**Skill Response**:
> 预算压缩时，用“三硬三软”框架做硬性筛选：
>
> **第一步：战略对齐过滤**
> - 列出公司明年TOP 3战略举措
> - 只保留直接支撑这3项举措的培训项目，其余全部暂停
>
> **第二步：ROI排序**
> 对每个保留项目估算：
> - 不参与培训的现状代价（量化：流失率、故障率、项目延期）
> - 培训投入（讲师费+场地+学员工时）
> - 预期改善收益
> - 计算：预期收益 / 投入 → 按比值从高到低排序
>
> **第三步：砍掉底线**
> - ROI < 1 的项目：砍
> - 非关键岗位全员通识培训：砍
> - 外部采购的通用管理课程：砍，改为内部经验分享
>
> **第四步：保重点**
> - 高ROI + 关键岗位 + 战略直接相关 = 保
> - 考虑用训战结合替代传统培训，缩短周期、降低成本
>
> 结果应该是：砍掉80%的面，保住20%的点——但这些点能产生80%的价值。