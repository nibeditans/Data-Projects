# Growth Rate, Compounding & Forecast Illusion

## Problem Statement

A startup reports the following:
* Revenue is growing at **10% per month**
* Current monthly revenue: **₹10,00,000**
* Leadership makes the claim: "At this rate, we'll double our revenue in about 10 months."

As an analyst, you are asked to:
* Validate this claim
* Decide whether the forecast logic is sound or misleading
* Explain the risk of linear thinking in growth projections

## Context & Why This Question Matters

Growth statements like "10% per month" are common in startup updates and investor decks. While the number itself is clear, the **mental model used to interpret it often isn't**.

A claim like "we'll double in ~10 months" sounds intuitive because many people unconsciously apply **linear reasoning**: 

> 10% × 10 months ≈ 100% growth

This case study examines whether that intuition holds, and what goes wrong when linear logic is applied to a **compound growth process**.

## Solution

### Compound Growth Formula

Monthly revenue after **n** months:

$$
R_n = R_0 \times (1 + g)^n
$$

Where:
* $R_0$ = Starting revenue
* $g$ = Growth rate per month
* $n$ = Number of months
* $(1 + g) ^ n$ = Compounding

```python
curr_monthly_rev = 1_000_000
gr_per_month = 0.10

rev_after_10_months = curr_monthly_rev * (1 + gr_per_month) ** 10
rev_after_10_months # 2593742.460100002
```
After 10 months, revenue is approximately **₹25.9 lakh**, about **2.6×**, not merely double.

### 1. Simulation Approach (Intuitive & Realistic)

```python
revenue1 = 1_000_000
growth_rate = 0.10
target = revenue1 * 2
months = 0

while revenue1 < target:
    revenue1 *= (1 + growth_rate)
    months += 1

months # 8
```
Using a step-by-step simulation, revenue crosses the doubling mark in **8 months**.

### 2. Mathematical Approach (Precise & Fast)

```python
import math

months_to_double = math.log(2) / math.log(1 + growth_rate)
months_to_double  # 7.272540897341713
```
Mathematically, revenue doubles in approximately **7.3 months**.

### 3. Month-by-Month Revenue Trajectory

```python
revenue2 = 1_000_000
growth_rate = 0.10

for month in range(1, 11):
    revenue2 *= (1 + growth_rate)
    print(f"Month {month}: ₹{revenue2:,.0f}")
```

**Output:**

* Month 1: ₹1,100,000
* Month 2: ₹1,210,000
* Month 3: ₹1,331,000
* Month 4: ₹1,464,100
* Month 5: ₹1,610,510
* Month 6: ₹1,771,561
* Month 7: ₹1,948,717
* Month 8: ₹2,143,589
* Month 9: ₹2,357,948
* Month 10: ₹2,593,742

This progression makes the compounding effect visible: each month's absolute increase grows larger because it is applied on an expanding base.

## Validation of the Leadership Claim

* The statement "we'll double in about 10 months" is **numerically incorrect**.
* At 10% monthly compounding, revenue doubles in **7-8 months**, not 10.
* After 10 months, revenue significantly **exceeds** the doubling threshold.

More importantly, the issue is not just the final number, it's the **logic used to reach the conclusion**.

## Where the Forecast Logic Breaks?

The implicit reasoning behind the claim is: "10% growth per month × 10 months ≈ 100% growth"

This is **linear reasoning**, but monthly growth is a **multiplicative (compound) process**.

Key differences:

* **Linear thinking** assumes the same absolute increase each month
* **Compound growth** increases by a percentage of a growing base

As a result:

* Early intuition feels reasonable
* Short-term estimates seem conservative
* Long-term projections become misleading

## Business Risk of Linear Thinking

Applying linear intuition to compound processes can lead to:

* Underestimating near-term growth acceleration
* Overconfidence in simplistic forecasts
* Misaligned capacity, hiring, or infrastructure planning
* Poor expectation-setting with investors and stakeholders

In other contexts (costs, debt, churn, headcount), the same mistake can **silently compound risk** instead of revenue.

## Key Takeaways

* A **10% month-over-month growth rate is compound, not linear**
* At 10% monthly compounding, revenue doubles in **~7.3 months**, not 10
* After 10 months, revenue reaches **~₹25.9 lakh (~2.6×)**
* Linear shortcuts like "10% × 10 months" distort exponential realities
* Analysts must challenge intuitive narratives, not just compute outcomes

This case study illustrates how small reasoning shortcuts can materially alter business expectations. The analyst's role is not merely to calculate growth, but to **validate the mental models behind forecasts**.

### 📄 **Quick-read version available**

A condensed, visual PDF version of this case study is shared on my LinkedIn for a fast, high-level overview.

👉 View the PDF summaries on LinkedIn: **[Documents section](https://www.linkedin.com/in/ns-nibedita-sahu/recent-activity/documents/)**  
