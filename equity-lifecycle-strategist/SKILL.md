# equity-lifecycle-strategist

## Description

Map equity incentive tools to the company's growth stage and crisis context. Based on Huawei's seven historical equity adjustments — each triggered by a specific crisis — this skill helps leaders choose the right instrument (real stock, virtual stock, options, TUP, or ATUP) at the right time, rather than copying a single template.

Applicable when:
- The user asks "what equity tool fits our stage?" or "should we use real shares, virtual shares, or options?"
- The company faces a crisis (cash crunch, market freeze, talent exodus) and needs emergency equity measures
- The user wants to evolve equity design as the company matures
- The user mentions "华为股权激励历程", "危机时期开股", or "不同阶段股权激励"

Not applicable when the company has no clarity on its 3-year strategic direction or when the founder is unwilling to dilute any economic interest.

## Activation

Trigger immediately when the user mentions any of the following:
- 股权激励阶段 / equity stage
- 危机股权 / crisis equity
- 初创期/成长期/成熟期股权 / startup/growth/maturity equity
- 华为七次股权调整 / Huawei seven equity adjustments
- 股权降本 / equity cost reduction
- 内部融资 / internal financing
- 不同阶段用什么股权工具 / which tool at which stage

## Workflow

### Step 1: Diagnose company stage and pressure

Use the following matrix to classify the company:

| Stage | Revenue Trend | Cash Position | Talent Pressure | Primary Equity Goal |
|-------|--------------|---------------|-----------------|---------------------|
| **Startup** | Unpredictable | Tight / negative | High (need co-founders) | Retain core team, conserve cash |
| **Growth** | Rapid growth | Break-even or positive | Moderate (need scale) | Fund expansion, reward strivers |
| **Maturity** | Stable / slow growth | Strong | Low (but veterans complacent) | Prevent bureaucracy, refresh culture |
| **Crisis** | Declining / frozen | Critical | Extreme (flight risk) | Emergency retention, cash substitution |

### Step 2: Select the instrument by stage

| Stage | Primary Instrument | Secondary Instrument | Rationale |
|-------|-------------------|----------------------|-----------|
| **Startup** | Real stock (registered) or founding partnership | IOU-to-stock conversion (like Huawei 1990) | Tiny team, high trust, need skin in the game; legal registry is feasible |
| **Growth** | Virtual restricted stock (ESOP) | TUP for new tiers | Too many employees for direct registry; need internal financing; veterans accumulating |
| **Maturity** | TUP (dominant) + ESOP (shrinking new grants) | ATUP for ecosystem | Prevent "shareholder retiree" syndrome; reallocate to active contributors |
| **Crisis** | Emergency TUP or salary-to-stock swap | Zero-bonus commitment with symbolic equity | Substitute cash outflow; bind survivors to turnaround; avoid external fire-sale |

Huawei's historical path (simplified):
- 1990: Startup — IOU converted to real stock (internal financing + retention)
- 1997: Growth — Union-trustee restructuring (scale beyond 50 shareholders)
- 2001: Crisis (dot-com bust) — Virtual stock introduced (loss of confidence in real stock value)
- 2003: Crisis (SARS + Cisco lawsuit) — Large grant + 3-year lockup (retention under fire)
- 2008: Crisis (financial crisis) — Saturated granting (cap veteran accumulation, make room for new blood)
- 2013: Maturity — TUP introduced (new employees can't afford virtual stock; veterans too comfortable)
- 2018+: Ecosystem — ATUP / ESOP1 (global workforce, external partners)

### Step 3: Design crisis-specific equity plays

When the user is in crisis mode, deploy one of these three tactics:

**A. Equity for Cost Reduction (股权降本)**
- Offer three compensation packages:
  - High cash / low equity (for employees who need immediate survival)
  - Medium cash / medium equity (for balanced risk-takers)
  - Low cash / high equity (for believers with savings)
- Requires: credible equity value story; transparent financials; founder's own sacrifice visible

**B. Equity for Internal Financing (股权融资)**
- Convert a portion of unpaid bonuses or deferred salary into stock/TUP.
- Use company-guaranteed loans only if legally permissible (note: Huawei's bank-loan model was later ruled non-compliant).
- Better alternative: issue convertible bonds to employees — fixed interest + conversion option.

**C. Equity for Turnaround Retention (股权留人)**
- Grant TUP with accelerated vesting tied to turnaround milestones (e.g., "if Q3 cash flow turns positive, Year 2 dividend jumps to 67% immediately").
- For critical roles, offer "golden handcuff" ESOP with 3-year cliff and 10-year repurchase schedule.

### Step 4: Plan the transition between instruments

Equity design must evolve. Use this transition map:

```
Year 0-2:   Founding stock (real) → build trust
Year 3-5:   Virtual stock (ESOP) → scale + internal finance
Year 6-10:  ESOP + TUP dual track → balance veterans vs. new strivers
Year 11+:   TUP dominant + ESOP1 rollover → refresh culture
Year 15+:   ATUP ecosystem → extend sharing to partners/suppliers
```

Transition rule: Never revoke existing rights. Instead, **let old instruments atrophy by shrinking new grants** while expanding the new instrument.

### Step 5: Set the crisis-to-normal recovery trigger

Define explicit metrics to exit crisis mode and return to normal equity policy:

| Metric | Crisis Threshold | Recovery Threshold |
|--------|-----------------|-------------------|
| Cash runway | < 6 months | > 12 months |
| Revenue growth | Negative for 2 quarters | Positive for 2 quarters |
| Voluntary attrition | > 20% annualized | < 10% annualized |
| Employee confidence (survey) | < 50% trust leadership | > 70% trust leadership |

When recovery triggers hit, freeze crisis instruments and relaunch standard TUP/ESOP cycles.

## Example Prompts

### Prompt A: Seed-stage startup choosing first equity plan
> "We just raised angel funding. Should we give real shares, options, or virtual stock to our first 10 employees?"

Response outline:
1. For 10 employees at seed stage: real shares or options are best (registry manageable; high trust).
2. Reserve 10-15% option pool in founders' agreement.
3. Use 4-year vesting with 1-year cliff; include company repurchase at fair market value.
4. Avoid virtual stock now — it adds unnecessary complexity when the cap table is small.
5. Set a trigger: when headcount exceeds 50 or you hit Series B, switch to virtual stock or TUP.

### Prompt B: Mature company with lazy veterans
> "Our company is 12 years old. Early employees act like landlords collecting rent. How do we fix this without legal war?"

Response outline:
1. Do NOT try to confiscate or dilute existing shares — legally dangerous and culturally toxic.
2. Introduce TUP as the primary new incentive; fund it before ESOP dividends.
3. Cap new ESOP grants at current saturation limits by level.
4. Create exciting new business lines with separate TUP pools — veterans must opt-in and perform to earn.
5. Over 5 years, the income mix shifts from "dividend-heavy" to "TUP-heavy" for active contributors.

### Prompt C: COVID-like crisis, cash flow drying up
> "We may not make payroll in 3 months. Can we use equity to survive?"

Response outline:
1. Immediate: offer salary-to-TUP conversion for voluntary participants (e.g., 30% of salary deferred into TUP units).
2. For critical roles: retention ESOP with 2x upside if company survives 18 months.
3. For all: transparent weekly financial updates to maintain trust.
4. If legally viable, offer convertible notes (debt → equity) rather than direct share issuance to avoid valuation disputes.
5. Set recovery triggers: when cash runway exceeds 9 months, revert to normal compensation.

## Key Principles

1. **One size never fits all**: The equity tool that saved Huawei in 2001 (virtual stock) would have been wrong in 1990 (too complex) and wrong in 2013 (too permanent).
2. **Crisis is the catalyst for equity innovation**: Huawei's best equity reforms happened during its worst business winters.
3. **Preserve existing rights, redirect new value**: Never steal from veterans; simply allocate new value creation to new instruments favoring current strivers.
4. **Legal feasibility changes by era**: Huawei's union-trustee + bank-loan model was historically specific and partly non-compliant. Modern equivalents use LLPs and contractual virtual stock.
5. **Communicate the "why" with history**: Employees accept painful transitions (e.g., lower ESOP dividends) when they understand the long-term survival logic.

## Related Skills

- `virtual-equity-governance-architect` — For holding-platform and five-rights separation design
- `tup-incentive-architect` — For detailed TUP algorithm and 9-fixed process
- `equity-incentive-pain-doctor` — For diagnosing why previous equity plans created entitlement cultures
- `rd-incentive-architect` — For R&D-specific long-term incentives by project lifecycle
