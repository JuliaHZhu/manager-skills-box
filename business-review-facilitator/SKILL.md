# business-review-facilitator

## Metadata

- **Source**: Huawei Management Handbook (5th Ed) — Business Management, Chapters 13-17
- **Domain**: Operations management / Business execution
- **Confidence**: High (derived from documented Huawei practice)
- **Revision**: 1.0

## When to Activate

Use when the user needs to run a business review meeting (经营分析会), operations review, monthly business review (MBR), or quarterly business review (QBR). Also triggers when the user complains that review meetings are "going through the motions" (走过场), "showing off results instead of facing gaps" (晒成绩不直面差距), or "jumping to actions without root cause analysis".

**Key triggers**: 经营分析会 / business review / MBR / QBR / 经营例会 / 经营复盘 / 差距分析 / 根因分析 / 经营会议流于形式 / 晒成绩 / 不找根因

**Not for**: pure strategic planning (use BLM/DSTE skills), routine status updates with no financial/operational targets, or personal productivity retrospectives.

## Core Methodology

Huawei's business review meeting is designed as a "gap → root cause → process" loop, not a "result → excuse → action" loop. The facilitator enforces three disciplines.

### Discipline 1: Start with Gaps (差距开头)

Rule: 80% of meeting time must be spent on gaps, not achievements.

1. **Define the battle standard** — A "win" is not "met target." It is:
   - vs. target (目标)
   - vs. same period last year (同比)
   - vs. competitor (与对手比)
   If all three are not addressed, the achievement is not validated.

2. **Open-classify-quantify** (打开-分类-数据量化):
   - Open by business line, product line, region, customer segment.
   - Classify into revenue gap, profit gap, market-share gap, efficiency gap.
   - Quantify with exact numbers. No "大概"/"差不多" allowed.

3. **Anatomy the sparrow** (解剖麻雀):
   - For each category, identify top-5 performers and bottom-20% performers.
   - Compare: what does the top do differently? What does the bottom miss?
   - Extract transferable practices, not just blame.

### Discipline 2: Find Root Causes (根因分析)

Rule: Only math problems allowed; no literature essays (只准做数学题，不准做语文题).

1. **Five-whys with data** — Each "why" must be backed by a number.
2. **Attribute internally first** (归因于内) — Each department must explain its own contribution to the gap before citing external factors.
3. **Open three layers deep**:
   - Layer 1: surface symptom (e.g., revenue dropped 10%).
   - Layer 2: structural split (e.g., which products/regions dropped?).
   - Layer 3: behavioral/mechanism root (e.g., pricing process missing competitor monitoring).

4. **Use the 33% rule** — If 33% of customers do not repurchase, open it:
   - 13% due to quality → which component? charger 7%, accessories 3%.
   - 11% due to service → which touchpoint?
   - The remaining 9% → unknowns become next month's research priority.

### Discipline 3: Build Process (建流程)

Rule: Firing a person closes a case; building a process prevents recurrence.

1. **Exception-to-routine** (例外例行化) — Every problem solved must become a standard operating procedure.
   - Example: Flight delays in rainy season → secretary handbook updated with "rainy season: book dominant local airline first."

2. **Mechanism over hero** — The value of a manager is measured by the processes they leave behind, not the fires they personally extinguish.
   - Reference: Li Bing's Dujiangyan irrigation system still operates 2,000 years later without Li Bing.

3. **Close the loop checklist**:
   - [ ] Problem defined with data
   - [ ] Root cause identified with evidence
   - [ ] Action owner assigned with deadline
   - [ ] Process/rule updated
   - [ ] Similar problems across other units checked
   - [ ] Next review will verify if the process worked

### Meeting Structure (Recommended)

| Phase | Time | Owner | Output |
|-------|------|-------|--------|
| Gap presentation | 40% | Business unit | Data-backed gap list |
| Root-cause drill | 40% | Cross-functional team | 3-layer cause map |
| Process/action | 15% | Process owner | Updated SOP + action tracker |
| Leadership summary | 5% | Chair | Decision log + next review focus |

## STOP Checkpoints

- **STOP if** the meeting starts with success stories for more than 5 minutes. Redirect to gaps immediately.
- **STOP if** someone says "the market is bad" or "competitors are too aggressive" without internal attribution first.
- **STOP if** an action item names a person to "try harder" instead of naming a process to change.
- **STOP if** the meeting ends without at least one SOP update or rule change.

## Anti-Patterns (Blacklist)

| Anti-Pattern | Why It Fails | Correct Practice |
|--------------|--------------|------------------|
| Private pre-negotiation | Problems are hidden from the formal forum | All gaps discussed in open meeting |
| Blame external factors | No organizational learning happens | Internal attribution first |
| Jump to action without root cause | Actions address symptoms, not disease | 5-whys with data |
| Fire the person, keep the system | Same problem recurs with new hire | Build process, update rule |
| Review only past, no prediction | Meeting becomes post-mortem, not steering | Include forecast +必胜计划 |

## Test Prompts

See `test-prompts.json` for validation scenarios.
