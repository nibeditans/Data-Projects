# Pricing, Percentages & Revenue Illusion

## Problem Statement

You’re an analyst at a subscription-based company.

Last month:

* Price per subscription: ₹1,000
* Active subscribers: 1,000

This month, the business team implemented a pricing change:

* Subscription price increased by **20%**
* Active subscribers dropped by **15%** after the change

During a leadership review, a stakeholder claims: "Revenue must have gone up. The price increase is larger than the drop in users."

You are asked to:
1. Verify whether total revenue actually increased or decreased.
2. Evaluate whether this pricing decision can be considered successful based on the information available.
3. Identify assumptions, risks, or missing context in the leadership’s conclusion.

## Business Context & Leadership Claim

At a glance, the claim sounds intuitive:
* Price ↑ by 20%
* Users ↓ by 15%

The implicit mental model is: "If price grows faster than volume shrinks, revenue should increase."

This kind of reasoning is common in pricing discussions and often dangerous, because it relies on **directional intuition**, not verified magnitude.

## Analytical Reasoning

Revenue is a multiplicative outcome:

$$
\text{Revenue} = \text{Price} \times \text{Subscribers}
$$

This means small percentage changes can interact in **non‑intuitive ways**. To validate the claim, we must translate percentages into absolute numbers and compare total revenue **before vs after**.

## Solution (Python Verification)

```python
# Given values
price_last_month = 1000
subscribers_last_month = 1000

price_increase_pct = 0.20
subscriber_drop_pct = 0.15

# Calculations
price_this_month = price_last_month * (1 + price_increase_pct)
subscribers_this_month = subscribers_last_month * (1 - subscriber_drop_pct)

revenue_last_month = price_last_month * subscribers_last_month
revenue_this_month = price_this_month * subscribers_this_month

absolute_change =  revenue_this_month - revenue_last_month
percentage_change = (absolute_change/revenue_last_month) * 100

print(f"Total Revenue last month: ₹{revenue_last_month:,.0f}")
print(f"Total Revenue this month: ₹{revenue_this_month:,.0f}")
print(f"Absolute Change b/w last month and this month: ₹{absolute_change:,.0f}")
print(f"Percentage Change b/w last month and this month: {percentage_change:.0f}%")
```

**Output:**
```yaml
Total Revenue last month: ₹1,000,000
Total Revenue this month: ₹1,020,000
Absolute Change b/w last month and this month: ₹20,000
Percentage Change b/w last month and this month: 2%
```

## Insight

Yes, **revenue increased**, but only by **₹20,000**, which is a **2% increase**.

This immediately exposes the illusion:

* A 20% price increase does not translate to a comparable revenue gain
* The 15% subscriber loss absorbs most of the upside

Large percentage changes in inputs do not imply large changes in outcomes.

## Business Interpretation

### Was the pricing decision successful?

**Numerically:**
* Revenue increased marginally ✅

**Strategically:**
* Success is **not guaranteed**

Why?
* We only observed **one month** of impact
* We don’t know if churn will continue
* We don’t know customer lifetime value (LTV)
* We don’t know cost structure or margin sensitivity

A small revenue bump does not automatically justify:
* customer dissatisfaction
* brand damage
* long‑term churn risk

## Decision & Recommendation

### What to tell leadership?

* The claim "revenue must have gone up" is numerically correct, but strategically incomplete.
* The revenue gain is modest relative to the price increase.
* The decision should not be judged successful without observing:
  * retention over multiple periods
  * impact on customer quality and LTV

### Recommended next steps

* Monitor churn trends over the next few cycles
* Segment churned vs retained users
* Evaluate whether higher prices attract or repel high‑value customers

## Key Takeaway

**Percentage intuition is unreliable in multiplicative systems.**

Pricing decisions must be validated with:
* numbers
* context
* and time

Not gut feel.

### 📄 **Quick-read version available**

A condensed, visual PDF version of this case study is shared on my LinkedIn for a fast, high-level overview.

👉 View the PDF summaries on LinkedIn: **[Documents section](https://www.linkedin.com/in/ns-nibedita-sahu/recent-activity/documents/)**  
