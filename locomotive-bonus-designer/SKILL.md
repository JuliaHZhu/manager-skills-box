# Locomotive Bonus Designer

Design and calibrate organizational bonus packages inspired by Huawei's "locomotive bonus" (火车头奖金) methodology. Covers three-step bonus pool generation, manager locomotive bonuses, individual allocation principles, and cross-unit smoothing mechanisms.

## When to Use

- When designing how bonus pools flow from company → business unit → department → individual
- When you need to align executive/manager bonuses with strategic goals (growth + budget + strategy)
- When resolving structural incentives across organizations (e.g., mature vs. emerging markets)
- When balancing organizational equity with individual differentiation

## How It Works

### Step 1: Three-Layer Bonus Pool Generation

Generate the bonus pool at each organizational level through three actions:

1. **Calculate**: Derive from financial results (revenue, profit, cash collection) using a get-share formula. Each unit's bonus is computed directly from its operational numbers.
2. **Aggregate/Exchange**: Roll up to the parent unit to enforce a **total cap** (总额约束). The sum of all sub-unit generated bonuses must not exceed the parent-level pool.
3. **Adjust**: Apply top-down smoothing (削峰填谷) to protect long-cycle investments and team stability. Subsidize low-performing strategic units, but ensure their per-capita bonus remains below normal units.

> Principle: Wood-business (木本生意), not grass-business (草本生意). To B markets need 3–5 years to mature; one bad year must not destroy the team.

### Step 2: Locomotive Bonus for Department Heads

For each department head, design a **locomotive bonus formula**:

- **Target Bonus**: Based on position responsibility, historical bonus level, and internal fairness across same-level roles.
- **Performance Coefficient**: Weighted 4:3:3 across three dimensions:
  - **Growth traction** (牵引增长): Revenue/profit/cash collection growth rate
  - **Budget traction** (牵引预算): Achievement against financial targets (revenue, profit, cash)
  - **Strategic goals** (牵引战略目标): 5–10 strategic tasks from the annual plan that build "soil fertility" (土地肥力)
- **Coefficient range**: Typically 0.5–1.5
- **Manager adjustment**: Direct supervisor retains 10–30% discretionary adjustment authority.

Formula: `Bonus = Target Bonus × Performance Coefficient × (1 + Supervisor Adjustment)`

### Step 3: Individual Employee Bonus Allocation

At the individual level, the company does **not** prescribe rigid rules. Instead, it sets principles and delegates to the AT (Administrative Team):

- Allocate based on **individual responsibility and contribution** (责任贡献)
- Link to performance rating:
  - A (excellent): 2–3× the B-level bonus (target: 3–5×)
  - B+ / B: standard allocation
  - C: principle is zero bonus (though units may grant a small amount)
  - D: no bonus
- Process: Direct supervisor proposes → AT reviews and approves
- Key cadres: Additional horizontal alignment by functional line (e.g., all HRBPs in a region are calibrated together)

### Step 4: Cross-Unit Balance and Individual Incentive Controls

**Organizational balance**: Keep inter-department per-capita bonus gaps within ~2×. Huawei describes this as "socialism at the organizational level."

**Individual differentiation**: Within a department, aggressively differentiate ("capitalism at the individual level").

**Timely incentives**: Project awards and personal commissions are allowed but capped at ~30% of the total incentive pool. They are drawn from the annual pool and deducted at year-end settlement.

**Linear bonus curve**: Unlike industry practice of accelerating incremental commissions, Huawei uses a **linear formula** (same rate for base and increment). Rationale: mature businesses suffer under steep incremental schemes; fairness requires consistent marginal rates.

## Output Format

Provide:
1. Recommended target bonus levels by role tier (with calibration logic)
2. 4:3:3 locomotive coefficient worksheet
3. Individual allocation guidelines and performance multiplier table
4. Cross-unit smoothing rules and exceptions list
5. Timely incentive cap and settlement mechanism

## Test Prompts

See `test-prompts.json` for validation scenarios.
