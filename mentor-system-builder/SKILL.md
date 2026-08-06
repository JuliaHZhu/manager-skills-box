---
name: mentor-system-builder
description: Design and operate a full-cycle mentor system for employee development. Covers mentor selection, mentee matching, mentoring agreements, progress tracking, and incentive mechanisms. Based on Huawei's "Great leaders lead leaders" philosophy. Use when the user needs to build a structured mentorship program for onboarding, skill transfer, or leadership pipeline development.
---

# mentor-system-builder

## When to Activate

Trigger when the user mentions:
- 导师制 / mentor system / mentorship program
- 传帮带 / knowledge transfer / apprenticeship
- 新员工培养 / new employee onboarding
- 老员工带新人 / veteran-to-newcomer pairing
- 经验传承 / experience inheritance
- 导师选拔与激励 / mentor selection & incentives

## Core Philosophy

> "用最优秀的人培养更优秀的人" — Great leaders lead leaders.

华为导师制的本质是**将人才培养与组织利益深度绑定**，通过制度设计解决“导师不愿教、学员学不深”两大痛点。

## The 7 Roles of a Mentor

导师不是简单的“老师”，而是在员工整个职业生涯中持续发挥作用的复合角色：

1. **教师、教练、辅导员** — 传授技能，纠正动作
2. **榜样** — 以身作则，示范华为人的行为标准
3. **能力与潜质开发者** — 识别并放大被辅导者的优势
4. **值得信赖的保护人** — 在关键时刻提供庇护和指导
5. **技术带头人、提携者** — 用自身资源为被辅导者创造机会
6. **提供机会和纠正错误者** — 敢于让被辅导者试错，并及时纠偏
7. **思想引导者** — 传递价值观，塑造职业态度

## The 3 Operating Elements

### 1. 选拔与匹配 (Selection & Matching)

| Dimension | Rule |
|---|---|
| **导师资格** | 入职1年以上、绩效B+以上、有实际业务成果的老员工或退休专家 |
| **匹配方式** | 按业务领域精准匹配；新员工入职后1周内确定导师 |
| **双向确认** | 不是行政指派，而是导师与被辅导者双向认可 |

### 2. 协议与过程 (Agreement & Process)

- **签订导师协议**：明确辅导周期（通常6-12个月）、辅导目标、双方权责
- **定期述职**：导师在定期绩效述职中必须汇报“如何帮助员工成长、培养员工”
- **被辅导者输出**：定期（双周或月度）输出学习汇报，在项目组中公开汇报

### 3. 考核与激励 (Assessment & Incentive)

**核心绑定机制**：
> 员工没有进步或没有得到提拔，导师相应地很难获得提拔。

| Incentive Type | Mechanism |
|---|---|
| **晋升绑定** | 导师的晋升评审中，必须举证培养成果；被辅导者的成长是导师晋升的硬指标 |
| **荣誉激励** | 优秀导师评选、导师勋章、内部宣传 |
| **物质激励** | 导师津贴、培养奖金；任正非提出“先有鸡”——先给激励，再提要求 |
| **反向约束** | 被辅导者被淘汰或长期无成长，导师当年绩效降级 |

## Mentor System Lifecycle

```
新员工入职 → 1周内匹配导师 → 签订辅导协议 → 
定期辅导（技术+业务+文化） → 双周学习汇报 → 
试用期答辩 → 转正定级 → 持续跟踪（整个职业生涯）
```

## Special Mechanisms

### 退休专家返聘制度
- 聘用到退休年龄的老专家、老员工
- 职责：将工作经验和技术传递给更多新人
- 优势：解决“老员工人数有限、不能因培训耽误工作”的矛盾

### 资源池分类培养
- 按人才类型分类：研发特长 → 研发培训池；市场营销倾向 → 营销培训池
- 每个新人进入基层实践，在岗位上实现理论与实践精确结合

## Implementation Checklist

- [ ] 明确导师资格标准（绩效、年限、业务能力）
- [ ] 设计导师-被辅导者匹配规则（按领域、按层级）
- [ ] 制定导师协议模板（目标、周期、双方权责）
- [ ] 将导师培养成果纳入导师本人的绩效考核/晋升评审
- [ ] 建立被辅导者的定期输出机制（学习汇报、答辩）
- [ ] 设计导师激励方案（荣誉+物质+晋升绑定）
- [ ] 建立导师资源池循环（退休专家、业务骨干轮值）

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| 导师行政指派、被辅导者无选择权 | 关系不对等，辅导流于形式 |
| 只给导师加任务、不给激励 | 导师敷衍了事，不愿倾囊相授 |
| 导师资格只看资历不看能力 | 庸师误人，传递错误经验 |
| 辅导周期不明确、无过程跟踪 | 虎头蛇尾，头一个月热情后消失 |
| 考核只看被辅导者、不看导师 | 导师无压力，培养质量无保障 |

## Example Interaction

**User**: 我们导师制推行两年了，老员工不愿意带新人，怎么破？

**Skill Response**:
> 这是典型的“激励缺位”问题。华为解决这个问题的核心逻辑是**利益绑定**。
>
> 诊断一下你目前的机制：
> 1. 导师的晋升/加薪是否与被辅导者的成长挂钩？
> 2. 被辅导者长期无进步，导师是否承担任何后果？
> 3. 导师带人有没有明确的物质或荣誉回报？
>
> 如果以上都是“没有”，按以下顺序整改：
> - **第一步：晋升绑定** — 在管理者晋升评审中增加“人才培养举证”环节，必须列出培养过的员工及成果
> - **第二步：反向约束** — 被辅导者试用期未通过，导师当年绩效不得为A
> - **第三步：正向激励** — 设立“导师津贴”，优秀导师额外奖金；每年评选“金牌导师”
> - **第四步：仪式感** — 拜师仪式、导师授牌、被辅导者转正时导师同台受奖
>
> 关键原则：让导师感受到“培养人是自己的事”，而不是“公司派的任务”。