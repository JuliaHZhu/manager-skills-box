# tup-incentive-architect

## Description

Design and implement a Time Unit Plan (TUP) — Huawei's signature 5-year deferred-incentive instrument that grants employees a calculable, escalating share of future value creation without requiring upfront capital. TUP is a "trial equity" and "stepping stone to real equity" that prevents veteran complacency while motivating new and mid-tier contributors.

Applicable when:
- The user wants an equity-like incentive that requires no employee purchase
- The user needs to balance labor income vs. capital income (target ratio 3:1 or 4:1)
- The user is troubled by "shareholder retirees" who collect dividends without contributing
- The user asks about "TUP", "时间单位计划", "奖励期权计划", "递延奖金", or "奋斗者分配"

Not applicable when the company has no predictable profit stream (TUP requires a bonus pool funded by value creation) or when the legal entity cannot support multi-year deferred compensation accruals.

## Activation

Trigger immediately when the user mentions any of the following:
- TUP / Time Unit Plan / 时间单位计划
- 奖励期权计划 / reward option plan
- 递延激励 / deferred incentive
- 劳动所得与资本所得 / labor income vs capital income ratio
- 新员工买不起股 / new employees cannot afford shares
- 老员工躺平 / veteran complacency / 食利阶层
- 九定流程 / nine fixed elements

## Workflow

### Step 1: Confirm TUP eligibility and pool source

Ask the user:
1. What is the annual value-creation metric? (revenue growth, profit, EVA, or specific project deliverables)
2. What percentage of incremental value will flow into the TUP pool? (Huawei uses ~18% of revenue for total compensation; TUP is a subset of that)
3. Who qualifies? (all employees above 1 year, or only certain levels/performance bands?)
4. What is the target labor-to-capital income ratio? (3:1 for growth stage, 4:1 for mature stage)

### Step 2: Run the "Nine Fixed" design flow (九定流程)

| # | Element | Decision Input |
|---|---------|---------------|
| 1 | **Purpose (定目的)** | 3-5 year strategic goal the TUP must serve |
| 2 | **Source (定来源)** | Incremental profit, revenue growth, or specific project surplus |
| 3 | **Cycle (定周期)** | Usually 5 years for tech/manufacturing; 3 years for fast-cycle industries |
| 4 | **Targets (定对象)** | Level + performance threshold; e.g., level 13+, 2 consecutive B+ ratings |
| 5 | **Units (定股数)** | Hay evaluation or job-grade coefficient × performance multiplier |
| 6 | **Assessment (定考核)** | Annual gate: performance rating + values compliance; failure suspends that year's accrual |
| 7 | **Annual dividend (定年度分红)** | Pool ÷ total outstanding TUP units × individual units × year-factor |
| 8 | **Terminal settlement (定期末分配)** | Year 5: full dividend + (exit NAV − entry NAV) × units, then units zeroed |
| 9 | **Mechanism (定机制)** | Transfer rules, forfeiture on departure, clawback for misconduct, rollover for top 30% |

### Step 3: Build the 5-year escalating schedule

TUP is a "deferred + incremental" (递延+递增) instrument.

Example with 10,000 units granted in Year 0 at NAV 5.42:

| Year | Dividend Entitlement | Calculation Example (if dividend = 1.0/unit) | Appreciation Settlement |
|------|---------------------|----------------------------------------------|------------------------|
| 1 | 0% | 0 | None |
| 2 | 33% | 3,333 | None |
| 3 | 67% | 6,667 | None |
| 4 | 100% | 10,000 | None |
| 5 | 100% | 10,000 | 10,000 × (NAV_year5 − 5.42) |

After Year 5, the 10,000 units are **zeroed**. The employee must re-qualify for a new TUP grant.

Key psychological effect: The employee always has "money on the table" in future years, increasing switching cost.

### Step 4: Calibrate the labor-capital ratio

Huawei's principle: **Labor income (salary + bonus + TUP) : Capital income (ESOP dividend) = 3:1 to 4:1**

Algorithm:
1. Calculate total compensation budget.
2. Pay salary and bonus first (short-term).
3. Allocate TUP from remaining pool (mid-term).
4. Whatever remains goes to ESOP dividend (long-term capital).

This automatically shrinks veteran dividend share when TUP expands, reallocating value to active contributors.

### Step 5: Design the allocation algorithm

TUP unit allocation per employee =

```
Base Units = Job Grade Coefficient (from Hay evaluation) × Level Multiplier
Performance Modifier = 0.5 (C) / 1.0 (B) / 1.5 (A) / 2.0 (A+)
Strategic Weight = 1.0 (core business) / 1.2 (new venture) / 0.8 (support)
Final Units = Base Units × Performance Modifier × Strategic Weight
```

All final units are submitted to the Administration Team (AT) or compensation committee for collective ratification. No individual manager can unilaterally grant TUP.

### Step 6: Establish the rollover rule for top performers

To retain the best talent beyond the 5-year cycle:
- Top 30% performers at Year 5 may convert outstanding TUP value into ESOP purchase rights (transition to real equity).
- Bottom 20% receive no new TUP grant; their economic rights naturally expire.
- Middle 50% receive a new TUP grant if they continue to meet performance gates.

This creates a **meritocratic filter**: TUP is the "trial"; ESOP is the "reward for sustained excellence."

## Example Prompts

### Prompt A: Company wants to reduce veteran dividend burden
> "Our early employees hold too much stock and collect huge dividends without working. New hires feel it's unfair. How can TUP rebalance this?"

Response outline:
1. Freeze new ESOP grants for levels already at saturation.
2. Introduce TUP for all active contributors; fund TUP from operating profit before ESOP dividend.
3. Set labor:capital target to 3:1; as TUP grows, ESOP dividend pool shrinks proportionally.
4. Veterans keep existing shares but no new ones; their relative income share declines over time.
5. Communicate: "The pie grows, but active contributors get the new slices."

### Prompt B: Startup cannot afford to let employees buy real shares
> "We want to give equity-like upside, but our engineers can't afford to buy shares. We also don't want to give away registered equity yet."

Response outline:
1. TUP is ideal: zero employee cost, no registered equity dilution.
2. Grant TUP units tied to 3-year cycle (fast for startup).
3. Fund from revenue milestones, not profit (since startup may be pre-profit).
4. At Year 3, top performers may convert TUP accumulated value into option rights at a nominal strike price.
5. Use the 9-fixed design flow; keep legal structure as employment incentive contract, not securities offering.

### Prompt C: HR wants a calculable model for CFO approval
> "I need to show the CFO exactly how much TUP will cost us over 5 years and what ROI we get."

Response outline:
1. Build a spreadsheet model:
   - Column A: projected annual value creation (revenue or profit).
   - Column B: TUP pool % (e.g., 5% of incremental profit).
   - Column C: total units outstanding each year.
   - Column D: per-unit dividend and appreciation.
   - Row: each employee's accrual schedule.
2. Stress-test: what if revenue grows 10% vs. 30%? Show CFO the variable-cost nature of TUP.
3. ROI framing: TUP reduces cash bonus outflow in early years (deferral), improves retention of Year 3-4 employees (highest flight risk), and replaces fixed salary increases with performance-linked upside.

## Key Principles

1. **TUP is a cash-flow instrument dressed as equity**: It behaves like equity (units, NAV, dividend) but legally is deferred compensation.
2. **Expiration forces re-qualification**: The 5-year zeroing prevents "once granted, forever entitled" complacency.
3. **Algorithm eliminates bargaining**: Pre-defined formulas (Hay grade × performance × strategy weight) remove subjective negotiation and political favoritism.
4. **Labor:capital ratio is the lever**: Adjusting this ratio is the primary mechanism for generational rebalancing between veterans and new strivers.
5. **TUP feeds into ESOP, never replaces it**: TUP is the front gate; ESOP is the back gate. Together they form a dual-track ownership pipeline.

## Related Skills

- `virtual-equity-governance-architect` — For holding-platform and legal structure design
- `equity-lifecycle-strategist` — For choosing TUP vs. ESOP vs. options by company stage
- `equity-incentive-pain-doctor` — For diagnosing why previous equity plans failed
- `position-based-pay-architect` — For Hay job evaluation that feeds TUP unit allocation
