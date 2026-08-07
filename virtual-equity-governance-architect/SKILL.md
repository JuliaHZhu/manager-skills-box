# virtual-equity-governance-architect

## Description

Design a virtual equity governance architecture that separates dividend rights and appreciation rights from voting rights, ownership, and transfer rights. Based on Huawei's virtual restricted stock (虚拟受限股) and union-trustee holding platform (工会持股), this skill helps founders retain control while sharing long-term economic benefits with employees.

Applicable when:
- The user wants to design an employee stock ownership plan without losing control
- The user needs a holding platform structure for a non-listed company
- The user is considering virtual stock, ESOP, or phantom stock for internal financing + motivation
- The user asks about "工会持股", "虚拟股权", "任正非1%控制", "持股平台设计", or "防火墙架构"

Not applicable when the company is already publicly listed (different regulatory constraints) or when the founder is unwilling to share any economic rights.

## Activation

Trigger immediately when the user mentions any of the following:
- 虚拟股权 / virtual equity / phantom stock
- 工会持股 / employee stock ownership platform
- 任正非 1% / founder control with minority stake
- 持股平台 / holding platform / LP structure
- 五权分离 / separation of rights
- 顶层架构 / top-level equity architecture
- 防火墙设计 / firewall design

## Workflow

### Step 1: Clarify the control objectives
Ask the user:
1. What percentage of voting control must the founder retain? (e.g., 51%, 67%, or veto-only)
2. Is the company planning to go public within 5-10 years? (affects reversibility)
3. What is the current shareholder structure? (natural persons vs. existing entities)
4. How many employees are expected to participate? (affects platform choice: LLP vs. Ltd.)

### Step 2: Choose the holding platform type

| Platform Type | Control Mechanism | Best For | Tax Note |
|--------------|-------------------|----------|----------|
| Limited Partnership (LP) | GP holds 1%+ voting; LP holds economic rights | 10-50 key employees | Pass-through taxation; GP bears unlimited liability |
| Limited Company (Ltd.) | Founder controls board; employees hold shares | 50+ employees; easier perception | Double taxation risk |
| Union/Collective (工会) | Founder acts as union proxy; historical model | Very large workforce (Huawei model) | Requires union legal person status; rare today |
| Contractual (virtual) | Pure contract rights; no registry change | Fastest implementation; lowest legal friction | Employment-law relationship; not true equity |

Recommendation: For most private companies, use a **Limited Partnership** as the primary holding platform, with the founder or a trusted entity as the GP.

### Step 3: Separate the five rights (五权分离)

Huawei's key insight: decompose equity into five rights and assign them differently.

1. **Dividend right (分红权)** → Grant to employees via virtual shares / LP interests
2. **Appreciation right (增值权)** → Grant to employees; linked to net asset growth per share
3. **Voting right (表决权)** → Retained by founder / GP / core control entity
4. **Ownership right (所有权)** → Retained by founder or top holding company
5. **Transfer/sale right (出售权)** → Retained by company; employees cannot sell externally

Operational rule: Employees sign a "Virtual Stock Subscription Agreement" with the holding platform, not with the operating company. The agreement explicitly states that upon resignation, the platform will repurchase shares at the net asset value of the most recent audited year.

### Step 4: Design the top-level architecture (顶层架构)

Standard Huawei-inspired three-layer model:

```
Layer 1: Founder (自然人)
         |
         v
Layer 2: Holding Platform (控股平台)
         |-- Founder as GP (1% voting control)
         |-- Employee LP pool (99% economic rights)
         |
         v
Layer 3: Operating Company (运营公司) <-- 100% owned by Holding Platform
         |-- Business operations
         |-- IP / contracts / revenue
```

Firewall rule: Keep the operating company free of direct employee shareholders. All employee equity sits in Layer 2. This protects the operating company from shareholder disputes and simplifies future M&A or IPO restructuring.

### Step 5: Define repurchase mechanics

| Scenario | Repurchase Price | Payment Schedule |
|----------|-----------------|------------------|
| Normal resignation | Current year net asset per share | 4 years, 1/4 annually (general staff) |
| Core staff resignation | Current year net asset per share | 10 years, 1/10 annually |
| Termination for cause | Original purchase price or 1 yuan/share | Immediate |
| Retirement | Current year net asset per share | Negotiated installment |

Critical clause: Include a 6-month post-departure review period during which the company may withhold repurchase if the employee violates non-compete or confidentiality obligations.

### Step 6: Legal compliance checklist

- [ ] Union/collective platform: Confirm local policy allows union legal-person status (note: many jurisdictions now restrict this)
- [ ] LP platform: Ensure GP has sufficient assets to cover potential unlimited liability, or use a Ltd. as GP
- [ ] Virtual stock: Structure as performance-based deferred compensation contract to avoid securities regulation
- [ ] Financing check: If employee funds are used, avoid illegal fundraising by ensuring (a) no public solicitation, (b) funds used for real operations, (c) no guaranteed fixed returns
- [ ] Tax: Plan for individual income tax on dividends and capital gains; consider whether virtual stock is taxed as salary or investment income in local jurisdiction

## Example Prompts

### Prompt A: Startup wants to retain control while giving equity to 15 early employees
> "We are a pre-Series A tech startup with 15 employees. The founder wants to keep 60% voting control but share economic upside. Design a holding platform."

Response outline:
1. Recommend a Limited Partnership with founder as GP (1% LP interest + GP control).
2. 15 employees as LPs; total economic pool starts at 15-20% of operating company, held via LP.
3. Virtual stock agreement: employees get dividend + appreciation rights; no voting, no transfer.
4. Repurchase at net asset value upon departure; 4-year installment for general staff.
5. Add a "drag-along" clause so if founder sells the company, employee LPs must co-sell at the same price.

### Prompt B: Manufacturing company with 200 employees wants internal financing
> "Our factory needs 5M RMB for expansion. We prefer employee investment over bank loans. How to structure it legally?"

Response outline:
1. Establish an Employee Holding Ltd. (or LP) as Layer 2.
2. Employees subscribe to virtual shares at 1x net asset value; funds flow to operating company via capital increase.
3. Issue "virtual stock" contracts, not registered shares, to stay below securities thresholds.
4. Promise dividend rights (e.g., 15% of after-tax profit) but no guaranteed principal return.
5. Set annual redemption cap (e.g., 10% of pool) to prevent liquidity runs.

### Prompt C: Founder worried about losing control after giving out equity
> "I gave 30% real shares to early employees. Now I feel I might lose control if they team up. How to fix this?"

Response outline:
1. Diagnose: Real shares with voting rights are hard to reclaim without consent.
2. Short-term: Sign a voting trust agreement or unified action agreement among existing shareholders to consolidate voting with founder.
3. Medium-term: Create a top holding company; swap employee operating-company shares for holding-platform LP interests (economic only), giving founder GP control.
4. Long-term: For new grants, switch to virtual stock or LP structure; never give registered shares with voting rights to operational employees again.

## Key Principles

1. **Control first, then sharing**: Economic rights can be generous; voting rights must be centralized.
2. **Contract over registry**: Virtual stock contracts are more flexible and reversible than registered equity.
3. **Platform as firewall**: Never let employee equity touch the operating company directly.
4. **Repurchase is the safety valve**: A well-designed exit price and schedule prevent deadlocks and hostage-taking.
5. **Legality varies by jurisdiction**: Union-trustee models (Huawei 2003) are historically specific; modern equivalents use LLPs or contractual virtual stock.

## Related Skills

- `tup-incentive-architect` — For the algorithmic allocation and 5-year cycle design of TUP
- `equity-lifecycle-strategist` — For matching equity tools to company growth stage
- `equity-incentive-pain-doctor` — For diagnosing common equity incentive failures
- `rd-incentive-architect` — For R&D-specific long-term incentive design
