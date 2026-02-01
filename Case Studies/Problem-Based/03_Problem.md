# Unit Economics & Margins (The Volume × Margin Illusion)

## Problem Context

A company sells a single product and is evaluating a marketing decision intended to increase sales volume.

Leadership's intuition is straightforward:

> "More sales means more profit."

This case study examines whether that intuition actually holds, **using unit economics and marginal analysis**, not headline revenue or total sales figures.


## Given Data & Assumptions

* **Selling price per unit:** ₹500
* **Variable cost per unit:** ₹300
* **Fixed monthly costs:** ₹10,00,000
* **Current monthly sales volume:** 5,000 units

Marketing proposes a campaign with the following impact:

* **Expected increase in volume:** +2,000 units
* **Additional marketing spend:** ₹2,00,000 per month
* **No change** in price or variable cost

Assumption:     
The campaign does not alter demand quality, pricing power, or unit-level costs beyond the stated marketing spend.


## Current State: Baseline Economics

At the current sales volume, the company is operating at **break-even**.

```python
selling_price = 500
variable_cost = 300
fixed_monthly_cost = 1_000_000
monthly_sales_vol = 5_000

current_total_cost = (variable_cost * monthly_sales_vol) + fixed_monthly_cost
current_revenue = selling_price * monthly_sales_vol
current_profit = current_revenue - current_total_cost

current_total_cost, current_revenue, current_profit
```

**Result:**

* Total Cost = ₹25,00,000
* Revenue = ₹25,00,000
* Profit = ₹0

The business is not losing money, but it has **no buffer**. Any drop in volume would immediately push it into losses.


## Marketing Proposal

Marketing suggests increasing monthly volume from 5,000 to 7,000 units at the cost of an additional ₹2,00,000 per month.

The proposal is framed as a growth opportunity:

* Higher sales
* Higher revenue
* Presumed higher profit

Before accepting this framing, the decision must be evaluated **incrementally**.


## Why Total Revenue is a Misleading Signal?

It is tempting to reason as follows:

* Revenue will increase
* Costs already exist
* Therefore, profit must improve

This logic is flawed because **total revenue does not determine profitability**.

Profit changes only when:

* Incremental revenue exceeds incremental costs

Everything else is noise.


## Unit Economics & Contribution Margin

At the unit level:

* Selling price = ₹500
* Variable cost = ₹300

**Contribution margin per unit = ₹200**

This ₹200 is what each additional unit contributes toward:

* covering fixed costs, and
* generating profit once fixed costs are covered

Since fixed costs are already fully covered at the current volume, **incremental units matter disproportionately**.


## Incremental (Marginal) Analysis

The marketing campaign adds 2,000 units.

Incremental contribution:

```python
additional_units = 2_000
contribution_per_unit = selling_price - variable_cost

incremental_contribution = additional_units * contribution_per_unit
incremental_contribution
```

**Incremental contribution = ₹4,00,000**

Incremental cost introduced by the decision:

```python
additional_marketing_spend = 200_000
```

Net incremental profit:

```python
incremental_profit = incremental_contribution - additional_marketing_spend
incremental_profit
```

**Net incremental profit = ₹2,00,000**

This is the **only number that matters** for the decision.


## Reconciliation with Full Profit View

For completeness, we can reconcile this with the full before-and-after profit view.

```python
new_volume = monthly_sales_vol + additional_units

new_total_cost = (
    variable_cost * new_volume
    + fixed_monthly_cost
    + additional_marketing_spend
)

new_revenue = selling_price * new_volume
new_profit = new_revenue - new_total_cost

new_profit
```

**Result:**

* Profit increases from ₹0 → ₹2,00,000

This matches the incremental analysis exactly, confirming internal consistency.


## Decision & Business Interpretation

The marketing campaign should be accepted.

However, **not for the reason leadership initially believed**.

Profit increases, not because revenue grows, but because **each additional unit carries positive contribution**, and the incremental contribution comfortably exceeds the incremental marketing spend.


## Key Takeaway: The Volume × Margin Illusion

"More sales" is not inherently good or bad.

Sales growth improves profitability **only when** unit contribution is positive, and incremental contribution exceeds incremental fixed or semi-fixed costs

In this case, volume growth works, **but only because unit economics are healthy**.

Revenue growth did not create profit.    
**Margins did.**


### 📄 **Quick-read version available**

A condensed, visual PDF version of this case study is shared on my LinkedIn for a fast, high-level overview.

👉 View the PDF summaries on LinkedIn: **[Documents section](https://www.linkedin.com/in/ns-nibedita-sahu/recent-activity/documents/)**
