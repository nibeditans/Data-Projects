# Averages and KPIs: When a Headline Metric Breaks Reality

## Problem Statement

You are analyzing customer revenue performance for a business.

A leadership dashboard highlights the following headline KPI:

**Average Revenue per Customer (ARPC) = ₹2,000**

Based on this number, leadership concludes:

"Our customers are spending well. Revenue quality looks strong."

Before accepting this interpretation, you request access to raw, customer-level data to validate how this KPI is computed and whether it truly reflects customer behavior.

The customer data provided is summarized below:

| Customer Segment | Number of Customers | Revenue per Customer (₹) |
| ---------------- | ------------------: | -----------------------: |
| Free Users       |                 900 |                        0 |
| Basic Plan       |                  80 |                    1,000 |
| Premium Plan     |                  20 |                   50,000 |

Your task is to evaluate whether the headline average metric reflects business reality.


## Initial Analytical Concern

Two immediate concerns arise when evaluating the dashboard metric:

1. **Is the reported ARPC even correct when recomputed from raw data?**
2. **Even if correct, does an average meaningfully represent customer revenue behavior in this business?**

Rather than accepting the dashboard number at face value, the analysis begins by recomputing the KPI directly from the underlying data.


## Data Breakdown & Computation

The following Python code is used to calculate ARPC and supporting metrics from the customer-level data:

```py
import pandas as pd

customer_data = {
    "customer_segment": ["free_users", "basic_plan", "premium_plan"],
    "customer_count": [900, 80, 20],
    "revenue_per_customer": [0, 1000, 50000]
}

df = pd.DataFrame(customer_data)

df["total_revenue"] = df["customer_count"] * df["revenue_per_customer"]

total_revenue = df["total_revenue"].sum()
total_customers = df["customer_count"].sum()

arpc = total_revenue / total_customers
print(f"Average Revenue per Customer = ₹{arpc:,.0f}")  # ₹1,080

df["revenue_percentage"] = round((df["total_revenue"] / total_revenue) * 100, 2)
df["customer_percentage"] = round((df["customer_count"] / total_customers) * 100, 2)

paying_customers = df.loc[df["revenue_per_customer"] > 0, "customer_count"].sum()
monetization_rate = paying_customers / total_customers
print(f"Monetization Rate = {(monetization_rate * 100):.0f}%")  # 10%
```

This computation produces an **actual ARPC of ₹1,080**, not ₹2,000 as reported on the dashboard.


## Solution

The leadership conclusion is **not supported by the data**, for two independent reasons:

1. **The headline KPI itself is incorrect**    
   Recomputing ARPC from raw customer data yields **₹1,080**, not ₹2,000. This immediately raises concerns about how the dashboard metric is defined, filtered, or reported.

2. **Even the correct ARPC misrepresents customer reality**    
   While ₹1,080 is numerically correct, it does not describe typical customer behavior. The average is driven almost entirely by a very small premium customer segment.

As a result, the claim that "customers are spending well" does not hold.


## Why ARPC Misrepresents Customer Reality?

Looking beyond the single average reveals a highly imbalanced customer base:

* **90% of customers generate ₹0 revenue**
* **Only 10% of customers are monetized**
* A tiny premium segment contributes the majority of total revenue

In effect:

* The "average customer" implied by ARPC does not exist
* The **typical customer is a non-paying user**
* Revenue is heavily concentrated in a small cohort

The average masks this structure and creates a misleading narrative of broad-based customer spending.


## Business Implications & Risk Exposure

This revenue profile introduces several material risks:

* **Revenue concentration risk**    
  A small number of premium customers financially sustain the business.

* **False confidence in revenue quality**    
  Customer growth may be driven by free users rather than revenue contributors.

* **High sensitivity to churn**    
  Losing even a few premium customers could significantly impact total revenue.

* **Misleading executive dashboards**    
  Single aggregated KPIs can obscure structural weaknesses in the customer base.


## What Should Be Tracked Instead?

To better assess revenue health, the business should complement ARPC with:

* Monetization rate
* Revenue contribution by customer segment
* Segment-level ARPC
* Changes in customer mix over time

These metrics reveal **who pays**, **how revenue is distributed**, and **how sustainable growth truly is**.


## Key Takeaway

**A KPI can be wrong, and even when corrected, still tell the wrong story.**

In this case:

* The reported ARPC was factually incorrect
* The corrected ARPC still hid extreme revenue concentration
* Leadership confidence was built on a misleading abstraction

Strong analysis doesn’t stop at reading dashboards.
It verifies numbers, questions averages, and exposes what metrics conceal.
