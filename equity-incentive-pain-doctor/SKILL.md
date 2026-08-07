# equity-incentive-pain-doctor

## Description

Diagnose and treat the fourteen most common equity incentive failures, from "equity becomes equity reward" to "shareholders turn into passengers." Based on Huawei's own painful lessons and the "14 pain points + 14 key points" framework distilled from three decades of ESOP and TUP practice.

Applicable when:
- A previous equity plan backfired (entitlement, laziness, disputes, or exodus)
- The user is designing a new plan and wants to avoid known landmines
- The user asks "what can go wrong with股权激励?" or "why did our ESOP fail?"
- The user needs to match shareholder types (capital / resource / management / tech / advisor) to entry instruments

Not applicable when the company has no historical equity data to diagnose or when the failure is purely due to business model collapse unrelated to incentive design.

## Activation

Trigger immediately when the user mentions any of the following:
- 股权激励痛点 / equity pain points
- 股权变福利 / equity became welfare
- 持股不干活 / shareholders don't work
- 股权纠纷 / equity dispute
- 股权激励失败 / failed ESOP
- 五类股东 / five types of shareholders
- 股权设计踩坑 / equity design pitfalls

## Workflow

### Step 1: Run the 14-point diagnostic scan

Ask the user to indicate which of the following symptoms are present (Yes / No / Unclear):

| # | Pain Point | Symptom | Root Cause |
|---|------------|---------|------------|
| 1 | **Founder control loss** | Early employees team up against founder decisions | Gave registered shares with voting rights |
| 2 | **Equity became reward** | Gave shares purely for past loyalty, not future contribution | No dynamic adjustment; no sustained-contribution filter |
| 3 | **Scope too narrow** | Only top 5% got equity; middle layer feels excluded | Fear of dilution; legal complexity of registered shares |
| 4 | **Platform hijacks control** | Employee holding platform demands board seats | Wrong platform structure (Ltd. instead of LP) |
| 5 | **Top architecture ignored** | Equity decisions made ad hoc without 10-year view | No holding-company layer; no firewall |
| 6 | **Tool mismatch** | Used registered stock for 200+ employees | Registry limit; tax nightmare; irreversibility |
| 7 | **Organization not activated** | After getting shares, employees work less, not more | No expiration; no re-qualification; no clawback |
| 8 | **Resource integration failed** | Promised equity to suppliers/agents but they didn't perform | No quantified algorithm; no performance gate |
| 9 | **No external reach** | Could not attract ecosystem partners with equity | Used internal ESOP instead of ATUP for outsiders |
| 10 | **No trial period** | Gave permanent registered shares to new hires who left in 6 months | No TUP/option trial before registered stock |
| 11 | **Wrong philosophy** | CEO copied a competitor's plan without understanding cultural fit | No alignment with company values or stage |
| 12 | **Unsustainable drain** | Dividend payouts strangle R&D investment | No labor:capital ratio control |
| 13 | **No system support** | Equity plan exists only on paper; HR cannot administer it | Missing process, IT tools, and committee governance |
| 14 | **Backward-looking only** | Equity rewards yesterday's heroes, not tomorrow's growth | No link to 3-5 year strategic value creation |

Scoring: Count "Yes" answers. 0-3 = healthy; 4-7 = warning; 8+ = critical redesign needed.

### Step 2: Map the five shareholder types to entry instruments

Not everyone should receive the same equity instrument. Use this entry matrix:

| Shareholder Type | Startup Stage | Growth Stage | Maturity Stage | Entry Rule |
|-----------------|---------------|--------------|----------------|------------|
| **Capital (资金型)** | Registered stock | Registered stock | Registered stock (<20%) | Premium pricing; pay for value |
| **Resource (资源型)** | ATUP | TUP | TUP + registered stock | Quantified contribution; phased conversion |
| **Management (管理型)** | TUP | TUP + options | TUP + registered stock | Full-time commitment; performance gate |
| **Technology (技术型)** | ATUP | TUP + options | TUP + registered stock | Assessable output; IP transfer check |
| **Advisor (顾问型)** | ATUP | Options | Registered stock (<5%) | Result-based; milestone-triggered |

Golden rule: **Never give registered stock on day one to non-capital contributors.** Always start with ATUP (external) or TUP (internal), then convert to options, then finally to registered stock after 3-5 years of proven contribution.

### Step 3: Apply the matching antidote

For each "Yes" in Step 1, apply the corresponding key point:

| Pain Point | Antidote (Key Point) |
|------------|---------------------|
| 1 | Use LP structure: GP retains voting; LPs get economic rights only |
| 2 | Add "sustained contribution" clause; shares vest over time; TUP trial first |
| 3 | Use TUP/ATUP to broaden coverage to 80%+ of workforce without registry burden |
| 4 | Never let employee platform hold >34% voting in OpCo; use contractual control |
| 5 | Design 3-layer architecture (founder -> holding platform -> OpCo) before first grant |
| 6 | Switch to virtual stock or TUP when headcount >50 |
| 7 | Set expiration (5-year TUP), annual re-qualification, and performance clawback |
| 8 | Bind resource providers with ATUP tied to measurable KPIs (sales, procurement savings) |
| 9 | Create ATUP pool for external partners; keep internal ESOP separate |
| 10 | Mandatory TUP trial period (1-2 years) before any registered stock eligibility |
| 11 | Anchor equity design in company values; run a 1-day workshop with founder + HR + legal |
| 12 | Enforce labor:capital income ratio (3:1 or 4:1); cap total dividend payout |
| 13 | Build equity administration committee + IT tool + annual audit before launch |
| 14 | Tie new grants to 3-5 year strategic milestones, not historical tenure |

### Step 4: Build the recovery roadmap

If the diagnosis is critical (8+ Yes), follow this 90-day recovery plan:

**Week 1-2: Stop the bleeding**
- Freeze all new registered stock grants immediately.
- Announce a "performance review window" for all existing shareholders.

**Week 3-4: Legal triage**
- Review all shareholder agreements for repurchase triggers.
- Identify shareholders who are legally terminable (cause, non-compete breach).

**Week 5-8: Structural redesign**
- Introduce holding-company layer if missing.
- Launch TUP for all new value creation; redirect future grants to TUP.

**Week 9-12: Communication and relaunch**
- Founder town hall: explain "why" with transparent financials.
- New grantees start on TUP; top 20% of TUP holders may graduate to ESOP after 2 years.

## Example Prompts

### Prompt A: Post-ESOP failure diagnosis
> "We gave 20% real equity to 8 co-founders. Now 3 have left and won't return shares. The remaining 5 argue in every board meeting. What should we have done differently?"

Response outline:
1. Diagnosis: Pain points #1 (control loss), #5 (no top architecture), #6 (wrong tool for group).
2. Ideal design: Use a holding LP from day one; founder as GP with voting; 8 co-founders as LPs with economic rights only.
3. Recovery now: Negotiate voting trust or unified action pact; for future roles, switch to virtual stock with 4-year vesting.
4. Hard truth: Recovering shares from departed co-founders without pre-signed agreements is expensive; budget for buyout or litigation.

### Prompt B: Preventing equity entitlement
> "How do we make sure employees don't treat their shares as a pension and stop working hard?"

Response outline:
1. Diagnosis: Pain point #7 (organization not activated).
2. Design TUP with 5-year expiration so economic rights expire unless re-earned.
3. For ESOP: introduce "saturation granting" — caps by level; no new grants once cap reached.
4. Annual performance gate: shareholders rated C for 2 consecutive years lose dividend rights for that year.
5. Cultural reinforcement: "Equity is earned annually, not owned forever."

### Prompt C: Choosing the right instrument for a supplier
> "A key supplier wants equity instead of cash payment for a strategic component. How should we structure this?"

Response outline:
1. Diagnosis: Risk of pain point #8 (resource integration failed) if done wrong.
2. Rule: Supplier is "Resource type" → start with ATUP, not registered stock.
3. Structure: Grant ATUP units tied to delivery quality, cost reduction, and exclusivity metrics.
4. After 2 years of meeting KPIs, allow conversion to options in a subsidiary JV, not the parent.
5. Firewall: Keep supplier equity in a separate JV to avoid parent-level control disputes.

## Key Principles

1. **Diagnose before designing**: Running the 14-point scan takes 30 minutes and prevents years of pain.
2. **Type-matching beats equality**: Capital, resource, management, tech, and advisor shareholders need different entry instruments.
3. **Trial before permanence**: TUP is the trial; registered stock is the graduation. Never skip the trial.
4. **Architecture is destiny**: The top holding structure determines whether equity unites or fractures the company.
5. **Recovery is possible but costly**: Failed equity plans can be redesigned, but expect to pay a "change tax" in buyouts, legal fees, and trust rebuilding.

## Related Skills

- `virtual-equity-governance-architect` — For holding-platform and five-rights separation
- `tup-incentive-architect` — For detailed TUP algorithm design
- `equity-lifecycle-strategist` — For stage-matching and crisis-specific equity plays
- `atup-ecosystem-integrator` — For external partner equity design
