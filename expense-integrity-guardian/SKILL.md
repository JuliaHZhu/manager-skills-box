# expense-integrity-guardian

## Metadata
- **Version**: 1.0.0
- **Author**: Cangjie distillation from Huawei Finance & Accounting System Handbook (5th Ed, 2023)
- **Trigger**: 费用报销 / 差旅费 / 内审 / 费用合规 / 诚信档案 / 报销流程 / expense reimbursement / travel expense / audit / compliance
- **Category**: Finance & Internal Control

## Purpose
Build a lightweight but high-integrity employee expense management system that minimizes administrative overhead while maintaining strong fraud deterrence. Based on Huawei's SSE system and integrity-score mechanism, this skill helps organizations replace heavy pre-approval with trust-based automation and data-driven post-audit surveillance.

## When to Use
- When employee expense fraud or careless errors are draining resources
- When the finance team is drowning in manual invoice verification
- When expense approval delays frustrate employees and slow down business
- When designing a shared-service center for expense processing
- When balancing employee convenience with control requirements
- When setting up integrity-based monitoring instead of 100% inspection

## When NOT to Use
- For procurement or supplier payment processes (use procurement-strategy-designer)
- For statutory tax audit defense (use tax-specific tools)
- When regulatory requirements mandate 100% physical inspection
- For executive or board-level expense policies (may need additional governance)

## Core Framework: Trust-But-Verify Expense System

### Principle 1: Supervisor Ownership of Truth
The employee's direct supervisor — not finance — is the first line of defense for expense authenticity.

**Why**: Supervisors know the business context. Finance cannot judge whether a dinner was genuinely client-entertainment or personal indulgence.

**Implementation**:
- Supervisor approves expense electronically via workflow.
- Finance does NOT perform substantive audit on every invoice.
- Exception: integrity-score-triggered audits (see Principle 3).

### Principle 2: Automation Replaces Bureaucracy
Huawei's SSE (Self-Service Expense) system demonstrates four automation levers:

| Lever | Before | After |
|-------|--------|-------|
| Approval | Face-to-face signature chase | Electronic workflow routing |
| Document flow | Employee walks invoices to finance | Centralized courier to shared service center |
| Payment | Cashier processes one-by-one | System batch-transfer via bank integration |
| Accounting | Manual voucher entry per transaction | System auto-generates accounting entries |

**Result**: ~1.2 million expense transactions/year processed with minimal human touch.

### Principle 3: Integrity Score Drives Risk-Based Audit
Instead of auditing everyone equally, build an employee integrity profile.

**Scoring Mechanics**:
- **Initial score**: 80 (Grade B)
- **Increment**: +1 per clean reimbursement, up to 120 max
- **Decrement**: -X per error or violation found

**Audit Frequency by Score**:

| Score Range | Audit Rate | Treatment |
|-------------|------------|-----------|
| 100+ | 5% | Post-audit, fast-track |
| 90–99 | 10% | Post-audit, standard |
| 80–89 | 20% | Post-audit, enhanced |
| 70–79 | 100% | Pre-audit by finance before payment |
| < 70 | 100% + mandatory pre-approval | Extended processing time; coaching required |

**Psychological Effect**: Employees self-regulate because the score is personal and transparent. It gamifies compliance without punitive framing.

### Principle 4: Supervisor Accountability
If a supervisor approves improper expenses, the supervisor bears joint liability.

**Consequences for Supervisor Negligence**:
1. **Financial**: Joint reimbursement of improper amounts (if employee has left, supervisor pays).
2. **Authority**: Suspension of expense approval rights for 3 years.
3. **Reinstatement condition**: Supervisor must hire two CPAs at personal expense to audit all expenses approved in the past 3 years.

**Why it works**: Supervisors take approval seriously because their own money and authority are at stake.

## Policy Design Toolkit

### Toolkit 1: Time Limits
- **Standard**: Reimburse within 3 months of expense occurrence.
- **Late (3–6 months)**: Requires special justification memo.
- **Expired (> 6 months)**: No reimbursement permitted.

### Toolkit 2: Lost Invoice Rule
- If invoice is lost but expense is proven genuine (e.g., via alternative evidence): reimburse 50%.
- **Rationale**: 
  - 25% = company's tax loss (non-deductible)
  - 25% = penalty for carelessness

### Toolkit 3: Approval Deadline Enforcement
- If approver does not act within N days, system auto-escalates to next level AND records the delay.
- Delayed approvals are published periodically. Approvers are accountable for delays.

### Toolkit 4: Substantive Documentation Requirements
A single invoice is NEVER sufficient. The following evidence must accompany each major expense category:

| Category | Required Evidence |
|----------|-------------------|
| Physical assets | Purchase order, receipt, warehouse entry slip, quality acceptance |
| Rent | Lease contract, approval record, match between contract and invoice |
| Entertainment | Approver name, department manager sign-off, itemized receipt for large amounts |
| Travel | Trip purpose, destination match on tickets, accommodation match, attendee list |
| Conference | Meeting notice, agenda, attendee list, sign-in sheet, no unrelated expenses |

## Internal Audit Posture

### Audit Scope
- Audit does NOT inspect every transaction.
- Audit performs risk-based sampling, weighted by integrity scores and transaction profiles.
- Audit covers ALL levels including the CEO and board members (no sacred cows).

### Example: Board-Level Audit
Huawei's internal audit once found that CEO Ren Zhengfei had improperly claimed laundry expenses during a business trip. The amount was refunded and a self-criticism was issued. This publicized case reinforced the cultural norm: rules apply to everyone.

## STOP Checkpoints
Before rolling out an expense integrity system, verify:
1. [ ] Have we shifted substantive authenticity review to supervisors rather than finance?
2. [ ] Is the integrity-score algorithm transparent to employees?
3. [ ] Do supervisors face real consequences (financial + authority) for negligent approvals?
4. [ ] Have we automated at least 3 of the 4 process steps (approval, document flow, payment, accounting)?
5. [ ] Is there a clear "lost invoice" penalty that covers both tax loss and behavior correction?
6. [ ] Does audit have explicit authority and cultural license to inspect board/CEO expenses?

## Output Format
When invoked, provide:
1. **Current State Diagnosis**: Map of today's expense process pain points.
2. **Target Design**: Supervisor-first approval + integrity-score audit matrix.
3. **Automation Roadmap**: Which steps to automate and in what sequence.
4. **Policy Package**: Time limits, lost-invoice rule, documentation checklist, approval SLAs.
5. **Supervisor Accountability Contract**: Joint liability terms and reinstatement conditions.
6. **Implementation Risk List**: Top 3 likely adoption barriers and mitigations.

## Related Skills
- `finance-digital-transformer` — for building the IT backbone of expense automation.
- `procurement-ethics-guardian` — for supplier-side ethics and anti-corruption.
- `lean-process-reformer` — for simplifying expense workflows end-to-end.
