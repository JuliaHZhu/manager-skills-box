# Successor Pipeline Architect

Build a succession planning and talent pipeline system that ensures every critical role has qualified backups at three readiness levels — eliminating vacancy risk, readiness risk, transition risk, and appointment risk.

## When to Use

When the user needs to:
- Ensure no critical role goes vacant without a ready successor
- Move from reactive backfilling to proactive succession planning
- Design a talent inventory (人才盘点) that identifies high potentials objectively
- Classify successors into readiness tiers (Ready Now / 1 job away / 2 jobs away)
- Reduce new-leader failure through structured 90-day turnarounds and annual appointment decisions

## Core Concepts

**Four Succession Risks**:
1. **Vacancy risk**: No one available when the role opens
2. **Readiness risk**: Successor exists but lacks capability or experience
3. **Transition risk**: Successor appointed but fails to adapt to new role
4. **Appointment risk**: Wrong person placed in wrong role at wrong time

**Three Readiness Levels** (borrowed from IBM, adapted by Huawei):
- **Ready Now**: Fully meets role standards; can assume role immediately
- **One job away**: 1–2 key gaps; needs 1–2 years targeted development
- **Two jobs away**: Multiple gaps; needs 3–5 years; potential-focused

**Performance-Potential Matrix**: Maps current performance (vertical) against future potential (horizontal) to identify stars, high potentials, core contributors, and underperformers.

**AAD (Annual Appointment Decision)**: A structured annual meeting where leadership reviews talent inventory and makes binding placement decisions for the coming year.

## Operating Procedure

### Step 1: Identify Critical Roles

Not all roles need succession plans. Focus on:
- Roles whose vacancy would significantly disrupt business continuity
- Roles that are hard to fill externally due to proprietary knowledge or relationships
- Roles that will face high turnover risk (retirement, market demand, burnout)

**Selection principles**:
1. Future-strategy driven: Which roles will matter most in 3–5 years?
2. Current-capability driven: Which roles are we weakest in today?
3. Vacancy-risk driven: Which roles have incumbents likely to leave soon?

Document role requirements in a living document updated every 2–3 years. Make it visible internally so employees can self-assess gaps.

### Step 2: Conduct Talent Inventory (人才盘点)

For each critical role, assess the bench using two dimensions:

**Dimension A — Performance**:
- S: Exemplary, role-model results
- A: Consistently exceeds expectations
- B: Meets expectations reliably
- C: Below expectations

**Dimension B — Potential** (four sub-dimensions, 1–5 scale each):
- Cognitive (strategic thinking, problem solving, learning agility)
- Interpersonal (influence, collaboration, emotional intelligence)
- Drive (ambition, resilience, initiative)
- Values alignment (culture fit, integrity, long-term commitment)

Total potential score: 20+ = high potential, 14–19 = medium, 8–13 = low, <8 = no potential.

Map all assessed employees onto the Performance-Potential matrix:

| | High Potential | Medium Potential | Low/No Potential |
|---|---|---|---|
| **S Performance** | Star — accelerate, retain at all costs | Solid performer — develop for broader roles | Expert track — deepen specialty |
| **A Performance** | High potential — fast-track development | Core contributor — maintain and gradually stretch | Stable performer — maintain in current role |
| **B Performance** | Rising potential — invest carefully | Average — monitor, provide coaching | At risk — performance improvement or exit |
| **C Performance** | Misplaced potential? — reassess fit | Underperformer — formal PIP | Remove — 3-month transition |

### Step 3: Build the Succession Table

For each critical role, maintain a table:

| Role | Incumbent | Ready Now | 1 Job Away | 2 Jobs Away |
|------|-----------|-----------|------------|-------------|
| Country GM — X | Zhang Wei | Li Na | Wang Tao, Chen Jie | Liu Hao |

**Quality checks**:
- Candidate pool should be ~3× the number of expected vacancies
- Include cross-functional candidates, not just direct reports
- Validate with multiple assessors (current manager, prior manager, skip-level, HRBP)
- Keep data confidential; access on strict need-to-know

### Step 4: Match Development to Readiness Level

| Level | Strategy | Typical Actions |
|-------|----------|----------------|
| **Ready Now** | Focused precision | Stretch assignments in current role; acting-up opportunities; board exposure |
| **One job away** | Focused development | 1–2 year IDP targeting specific gaps; cross-functional project; mentor assignment; 高研班 |
| **Two jobs away** | Focused potential | 3–5 year career pathing; rotation into adjacent functions; foundational skill building |

### Step 5: Manage the Four Risks

**Vacancy risk**: Maintain minimum 1 Ready Now or 1 Job Away candidate for every critical role. If a role has zero candidates, flag as red and launch emergency recruitment + development.

**Readiness risk**: Require at least one successful实践案例 for any Ready Now candidate. Classroom training alone is insufficient.

**Transition risk**: Implement a **90-day turnaround plan** for every new appointee:
- Days 1–30: Learn — map stakeholders, understand team dynamics, listen
- Days 31–60: Plan — define quick wins, align with boss on priorities, fix obvious problems
- Days 61–90: Act — deliver first visible result, gather feedback, adjust approach
- Assign a transition mentor (not the direct boss) who meets biweekly

**Appointment risk**: Hold an **Annual Appointment Decision (AAD)** meeting:
- Pre-meeting: HR prepares talent inventory, vacancy forecasts, and candidate packets
- Meeting: Leadership reviews each critical role, discusses candidates, makes placements
- Post-meeting: Document decisions, communicate to affected managers, schedule transitions
- Principle: "Right person, right role, right time" — not "who is available now"

### Step 6: Continuously Refresh

- Update succession tables quarterly
- Re-assess potential annually (or after major projects)
- Remove candidates who leave, underperform, or show declining motivation
- Add new high potentials identified through projects or rotations
- Track pipeline health: % critical roles with Ready Now backup, average time to readiness, diversity metrics

## Anti-Patterns

- **Paper successors**: Listing names without real assessment or development. The table becomes fiction.
- **Clone syndrome**: Selecting successors who are mini-versions of the incumbent, ignoring future role evolution.
- **Ignore hidden talent**: Only assessing direct reports. High potentials often sit two levels down or in adjacent functions.
- **Over-reliance on IQ**: Promoting the smartest person without checking interpersonal skills or values alignment.
- **Secrets without action**: Conducting talent review but never changing appointments based on it.

## Test Prompts

See `test-prompts.json`.
