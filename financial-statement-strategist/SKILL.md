# financial-statement-strategist

## Metadata
- **Version**: 1.0.0
- **Author**: Cangjie distillation from Huawei Finance & Accounting System Handbook (5th Ed, 2023)
- **Trigger**: 三张表 / 财报分析 / 财报六看 / 利润表 / 现金流量表 / 资产负债表 / financial statement / 财务分析 / 利润兑现率 / 自由现金流
- **Category**: Finance & Analysis

## Purpose
Read and interpret corporate financial statements not as accounting exercises but as strategic narratives. Based on Huawei's "Six Views" framework, this skill teaches users to diagnose a company's strategic position, growth quality, operational efficiency, asset health, and risk exposure through the lens of the three core financial statements.

## When to Use
- When evaluating a company's true health beyond headline profit numbers
- When preparing for investor presentations or board reviews
- When diagnosing whether reported profits are backed by cash
- When assessing a competitor's strategic direction through their financials
- When coaching non-finance managers to read financial statements
- When conducting due diligence or credit analysis

## When NOT to Use
- For detailed tax planning or audit procedures
- For valuation modeling requiring DCF or comparables
- When only raw transaction-level data is available (need consolidated statements)
- For personal investment advice (this is a framework, not a recommendation engine)

## Core Framework: The Three Statements as Strategic Narrative

### Statement 1 — Profit & Loss (Income Statement)
**Role**: The "makeup" — shows face value performance.

**Reading Protocol**:
1. **Revenue & Growth**: Size and trajectory. Validate against cash received from customers.
2. **Gross Margin & Trend**: Product competitiveness and pricing power. A declining margin may signal commoditization or loss of differentiation.
3. **Operating Expenses**: 
   - Sales/Marketing = customer-interface investment strategy
   - R&D = future-oriented innovation bet
   - Admin = internal operational efficiency ("卓越运营")
4. **Asset Impairment**: Watch for judgment-driven write-downs that may smooth or manipulate earnings.
5. **Non-Recurring Items**: One-time gains/losses that distort the true operating picture.
6. **Net Profit**: The bottom line, but remember — "profit is the source of all evil" (万恶"盈"为首) because it can be engineered.

### Statement 2 — Cash Flow Statement
**Role**: The "mirror of truth" — reveals whether profit is real or illusion.

**Reading Protocol**:
1. **Operating Cash Flow**: The lifeblood. If OCF is consistently below net profit, investigate receivables, inventory buildup, or aggressive revenue recognition.
2. **Investing Cash Flow**: Negative is often good (growth investment); positive may signal asset sales or contraction.
3. **Financing Cash Flow**: Source of capital. High debt inflows = leverage risk; equity inflows = dilution or growth confidence.
4. **Free Cash Flow (FCF)**: OCF minus capital expenditures. The true distributable surplus.
5. **Profit Realization Ratio**: OCF / Net Profit. Huawei uses this to test profit quality. < 1 = caution.

**Key Insight**: Cash flow recognizes nothing until cash moves. It overrides accrual accounting illusions.

### Statement 3 — Balance Sheet
**Role**: The "territory" — shows accumulated strategic choices.

**Reading Protocol**:
1. **Asset Composition**: Tangible vs. intangible. In tech, intangible value (R&D, brand, customer relationships) often exceeds book assets.
2. **Debt Structure**: Short-term vs. long-term. Match against cash conversion cycle.
3. **Working Capital**: Receivables + Inventory — Payables. Long cycles drain cash.
4. **Equity Growth**: Retained earnings trajectory signals sustainable value creation.

## The Six Views (财报六看)

A synthesized framework for holistic financial statement analysis:

| View | What to Look For | Key Indicators |
|------|------------------|----------------|
| **1. Strategy** | How capital is allocated to strategic priorities | R&D intensity, CapEx direction, M&A activity, product mix |
| **2. Growth** | Top-line momentum and market position | Revenue growth rate, market share trends, customer concentration |
| **3. Efficiency** | Operational excellence and asset utilization | Asset turnover, inventory days, receivable days, admin expense ratio |
| **4. Profitability** | Value capture from operations | Gross margin, operating margin, ROE, ROA, EVA |
| **5. Asset Quality** | Risk hidden in the balance sheet | Impairment trends, receivables aging, inventory obsolescence, off-BS items |
| **6. Risk** | Sustainability and vulnerability | Debt/Equity, interest coverage, cash burn rate, covenant compliance, contingent liabilities |

**Rule**: Always look at trends, not single-period snapshots. A V-shaped profit reversal (loss → profit → loss) is a red flag for earnings management.

## Huawei's "Soft Assets" Lens
Traditional balance sheets understate tech companies. Evaluate five intangible value drivers:

1. **肚子里有货**: Differentiated products and solutions (R&D output)
2. **有地盘**: Market position and installed base (recurring revenue potential)
3. **资源整合力**: Global delivery and customer response capability
4. **客户信任**: Strategic partnership depth with key accounts
5. **品牌**: Brand equity and customer retention (repeat purchase rate)

These are not on the balance sheet but often represent >75% of market value.

## Cross-Statement Diagnostics

### Diagnostic 1: Is the Profit Real?
- P&L shows profit → Check CFO: is cash collected?
- If profit ↑ but CFO ↓ → investigate receivables buildup or channel stuffing.
- If profit ↑ and CFO ↑ → profit is likely genuine.

### Diagnostic 2: Where Is the Money Going?
- P&L profit → Retained earnings (BS) → Reinvested or distributed?
- If retained earnings grow but equity doesn't → check for write-downs or buybacks.
- If CapEx (CF) > Depreciation → growing asset base; if < → contraction or efficiency gain.

### Diagnostic 3: Can the Company Survive a Downturn?
- BS: Cash + undrawn credit facilities vs. short-term debt maturities.
- CF: FCF margin and volatility.
- P&L: Fixed cost structure (operating leverage).

### Diagnostic 4: Is Growth Profitable?
- Revenue growth vs. margin trend.
- If revenue grows but margins compress → scale without value capture (dangerous).
- If revenue grows and margins expand → strong competitive position.

## Capital Structure Life-Cycle Logic

| Stage | Capital Structure | Rationale |
|-------|-------------------|-----------|
| Startup | High equity, low debt | High operating risk; creditors unwilling |
| Growth | Moderate equity, rising debt | Cash flow improving; debt becomes accessible |
| Mature | Lower equity, higher debt | Stable cash flows support leverage; shareholders want dividends |
| Decline | Low equity, high debt | Shareholders exit; lenders hold until asset liquidation |

## STOP Checkpoints
Before presenting a financial analysis, verify:
1. [ ] Have I validated profit quality with operating cash flow?
2. [ ] Have I looked at 3+ years of trends, not just the latest period?
3. [ ] Have I assessed intangible/soft asset value beyond book numbers?
4. [ ] Have I identified non-recurring items that distort the operating picture?
5. [ ] Have I cross-checked revenue growth against cash collected from customers?
6. [ ] Have I flagged any V-shaped earnings patterns or near-zero profit volatility?

## Output Format
When invoked, provide:
1. **Executive Snapshot**: One-paragraph verdict on the company's financial health.
2. **Six-View Dashboard**: Score or color-code each view (Strategy/Growth/Efficiency/Profitability/Asset Quality/Risk).
3. **Three-Statement Narrative**: Story of how strategy → operations → cash → assets.
4. **Red Flags**: Top 3 warning signs requiring deeper investigation.
5. **Soft Asset Assessment**: Qualitative rating of the five intangible value drivers.
6. **Peer Context**: How the metrics compare to industry norms (if provided).

## Related Skills
- `finance-bp-operator` — for translating financial analysis into business action plans.
- `project-four-accounting` — for project-level financial statement analysis.
- `comprehensive-budget-manager` — for connecting financial analysis to budget planning.
- `business-model-five-elements` — for linking financial results to business model design.
