# Talent Inventory Nine-Box Operator

Run structured talent reviews using the nine-box and supporting matrices inspired by Huawei's annual talent inventory (年终人才盘点). Combines performance-potential matrices, learning-agility scoring, workload analysis, and position-matching dashboards.

## When to Use

- When conducting annual or quarterly organization-wide talent reviews
- When deciding who to promote, rotate, develop, or exit
- When assessing bench strength and succession readiness by department
- When a new manager needs a rapid, flat view of all team members' status

## How It Works

### Tool 1: Performance-Potential Matrix (绩效潜能矩阵)

Two axes:
- **Vertical**: Performance / KPI results (quantitative outcomes)
- **Horizontal**: Behavior / competency / potential (qualitative process)

Map personnel into a grid. Use these standard Huawei tiers:

| Potential \ Performance | S (Superior) | A (Excellent) | B (Good) | C (Needs Improvement) |
|---|---|---|---|---|
| **S (High)** | Star — promote now | Strong performer — fast-track | Develop — stretch assignment | Warning — misaligned? |
| **A (Medium)** | Solid — broader role in 2 years | Core — steady development | Maintain — targeted training | Risk — coach or move |
| **B (Low)** | Lucky/leader-assisted — verify | Contributor — specialist track | Average — efficiency focus | Exit candidate |
| **None** | Do not promote | Do not promote | Do not promote | Exit |

**Application rules**:
- Do not allow excessive clustering in any single cell; healthy organizations show dispersion.
- If one cell is overloaded, initiate cross-department rotation.
- Contrast inventory results against business requirements to identify critical gaps.

### Tool 2: Learning-Agility / Potential Scorecard (学习力评价表)

Score 1–5 on four dimensions (five items each, total max 25):

1. **Thinking agility** (思维心智): domain expertise, problem-solving, ambiguity tolerance, clarity of communication, error-as-opportunity mindset
2. **Interpersonal agility** (人际情商): relationship sensitivity, persuasive communication, emotional acceptance, self-awareness, coordination
3. **Change agility** (变革创新): continuous improvement, challenge acceptance, novel ideas, experimentation, driving transformation
4. **Results agility** (结果导向): self-drive, resilience, high standards, potential activation, outcome focus

- **20–25**: High potential (晋升优先)
- **14–19**: Medium potential (2-year development path)
- **8–13**: Low potential (3–5 year horizon)
- **≤7**: Weak potential (no promotion track)

### Tool 3: Workload Quantification & Efficiency Table (工作定量分析)

For any role, list:
- Frequency (daily/weekly/monthly)
- Nature (fixed vs. variable)
- Task description
- Time spent (actual vs. target)
- % of daily workload
- Efficiency improvement method
- Adjusted time target

Use this to:
- Identify low-value tasks consuming disproportionate time
- Reallocate effort toward critical-path activities
- Set realistic headcount and capacity plans

### Tool 4: Position-Matching Matrix (岗位匹配度矩阵)

A flat, single-page dashboard per department head showing:
- Total headcount vs. approved headcount
- Reporting structure (supervisor → subordinates)
- Historical performance ratings (e.g., 2A2B over past 4 cycles)
- Tenure / company age
- Compensation level vs. band
- Mobility frequency (transfers / loans)
- Potential rating

Update at least quarterly. Purpose: give new or promoted managers an instant, comprehensive view of their team for deployment decisions.

### Tool 5: Nine-Box Dynamic Assessment (九宫格动态评估)

Core principles:
1. **Dual-axis evaluation**: Results alone are insufficient. ~20% of results are luck; ~20% are heavily leader-assisted; ~20% stem from role risk. Use competency/potential to filter noise before promotion.
2. **Three-way split**:
   - Top-right (high-high): Priority promotion and development
   - Bottom-left (low-low): Targeted exit or remediation
   - Middle band: Maintain with targeted improvement
3. **Mismatch diagnosis**:
   - High results + low competency: Likely luck/leader-driven; continue using but invest in training
   - High competency + low results: Likely wrong role; reassess job fit before penalizing

> Rule: Results determine bonuses; competency/potential (plus root-cause analysis) determine promotions.

## Output Format

For each review cycle, produce:
1. Performance-Potential grid with headcount per cell and gap analysis vs. business needs
2. Learning-Agility scorecard for high-potential candidates
3. Workload analysis for roles with efficiency concerns
4. Position-Matching matrix for the organization/department
5. Action list (promote / develop / rotate / exit) with timeline

## Test Prompts

See `test-prompts.json` for validation scenarios.
