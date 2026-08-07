---
name: strategic-sourcing-tco
description: Shift from transactional purchasing to strategic sourcing by evaluating total cost of ownership (TCO) including transportation, inventory, risk, quality, and sustainability rather than just unit price. Use when the user discusses reducing procurement cost, evaluating supplier bids, choosing between bulk discount vs. flexibility, or moving from price-based to value-based procurement.
---

# strategic-sourcing-tco

Shift from transactional purchasing to strategic sourcing by evaluating total cost of ownership (TCO) rather than just unit price.

## When to Use

- The user asks how to reduce procurement costs beyond simple price negotiation
- The user faces a trade-off between bulk discounts and inventory/flexibility costs
- The user needs to evaluate whether a lower-priced supplier is actually cheaper after considering hidden costs
- The user wants to implement strategic sourcing or total cost of ownership analysis
- The user describes procurement decisions that saved on purchase price but increased logistics, inventory, or quality costs

## The Problem with Traditional Purchasing Tactics

Four common tactics and their hidden side effects:

1. **Bulk ordering for volume discounts**
   - Side effect: higher inventory, more working capital tied up, obsolescence risk

2. **Annual supply agreements for price stability**
   - Side effect: locked into supplier, reduced flexibility to switch if market changes

3. **Competitive bidding for lowest transport price**
   - Side effect: may sacrifice reliability, visibility, or service level

4. **Switching to lowest-cost supplier or demanding price cuts**
   - Side effect: quality degradation, supply instability, damaged supplier relationship

## Strategic Sourcing: The TCO Lens

Strategic sourcing evaluates the **total impact** of a procurement decision on the entire supply chain:

| Cost Category | What to Include |
|--------------|-----------------|
| **Purchase price** | Unit price, volume discounts, payment terms |
| **Transportation** | Inbound freight, handling, customs, duties |
| **Inventory** | Carrying cost, warehouse space, working capital, obsolescence |
| **Risk** | Supply disruption probability, single-source exposure, geopolitical risk |
| **Quality** | Defect rate, inspection cost, rework, warranty, brand damage |
| **Sustainability** | Compliance cost, carbon footprint, ESG requirements |

Decision rule: the lowest unit price is rarely the lowest total cost.

## Implementation Steps

### Step 1 — Segment Spend

Classify procurement categories by value and complexity:
- **Strategic**: high value, high risk, few sources (e.g., key chips, specialized components)
- **Leverage**: high value, low risk, many sources (e.g., standard raw materials)
- **Bottleneck**: low value, high risk, few sources (e.g., specialized tooling)
- **Non-critical**: low value, low risk, many sources (e.g., office supplies, MRO)

Different segments get different sourcing strategies.

### Step 2 — Build TCO Model per Category

For strategic and leverage categories, build a quantified TCO model:
1. List all cost drivers (not just price)
2. Assign weights based on business impact
3. Collect data from internal systems and supplier input
4. Run scenario analysis: e.g., Supplier A (low price, high MOQ) vs. Supplier B (higher price, lower MOQ, better quality)

### Step 3 — Supplier Relationship Strategy

| Supplier Type | Relationship Approach |
|--------------|----------------------|
| Strategic partner | Long-term collaboration, joint improvement, information sharing, mutual investment |
| Competitive leverage | Maintain multiple sources, use competition to keep market pricing |
| Transactional | Efficient processing, low touch, standard terms |
| Monitor/exit | Performance improvement plan or phase-out |

### Step 4 — Contract Design Beyond Price

Include条款 that protect TCO:
- Quality guarantees and penalty clauses
- Flexibility clauses (volume ramps, reductions, expedites)
- Information sharing requirements (inventory visibility, forecast sharing)
- Continuous improvement commitments
- Sustainability and compliance obligations

### Step 5 — Performance Monitoring

Track TCO KPIs, not just purchase price variance:
- Total landed cost per unit
- Supplier quality ppm (parts per million)
- On-time delivery rate
- Inventory turns by supplier/Material
- Supply risk incidents per year

## Strategic Principle: Supply Chain Competition

Ren Zhengfei: "Future competition is not between individual enterprises, but between supply chains. If our procurement staff only know how to haggle mechanically instead of building long-term supplier partnerships, they will ruin the company's tomorrow."

- 60% of a product's final cost often comes from suppliers
- Supply chain cost is the enterprise's primary cost
- A supply chain ecosystem cannot be bought with money in the short term
- Technology leadership is temporary (products last 9 months to 2 years); service and integration capability is the sustained competitive advantage

## Boundaries & Anti-Patterns

- **Not for**: pure spot-buying of commoditized goods where price is the only meaningful variable; emergency purchases where speed dominates cost
- TCO analysis requires data infrastructure; attempting it without basic cost visibility will produce garbage results
- Do not apply identical TCO depth to all categories; focus analytical effort on strategic and leverage spend
- Avoid "partnering" with every supplier; partnership is resource-intensive and should be reserved for truly strategic relationships
- Beware of internal resistance: procurement teams measured on purchase price savings will resist TCO metrics unless incentives change

## Related Skills

- `procurement-strategy-designer` — for selecting procurement methods (tendering, direct purchase,框架协议)
- `tqrdc-supplier-evaluation` — for multi-dimensional supplier scoring (Technology, Quality, Response, Delivery, Cost + Environment/Social)
- `supplier-lifecycle-manager` — for end-to-end supplier relationship management from sourcing to exit
- `vmi-inventory-designer` — for vendor-managed inventory as a strategic sourcing mechanism
