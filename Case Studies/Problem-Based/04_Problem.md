# CAC, LTV & the "Profitable Growth" Illusion

## Problem Statement

A subscription-based company reports the following unit economics:

* **Monthly subscription price:** ₹1,000
* **Gross margin:** 70%
* **Average customer lifetime:** 10 months

Marketing proposes scaling paid acquisition with:

* **Customer Acquisition Cost (CAC):** ₹6,000 per customer

Leadership's conclusion:

> "LTV is much higher than CAC, so scaling ads is profitable."

The task is to evaluate whether this logic is valid or **dangerously incomplete**, and decide whether the company should **scale aggressively**.


## Why This Problem Matters?

"**LTV > CAC**" is one of the most commonly cited rules of thumb in growth discussions. It sounds financially responsible, data-driven, and intuitive. But this case study examines why that statement, by itself, can lead companies to scale into losses, even when the Math appears to work.


## Step 1: Numerical Verification (Baseline)

We first verify the leadership’s claim numerically.

### Customer Lifetime Value (LTV)

LTV is calculated as gross contribution earned over the average customer lifetime:

$$
\text{LTV} = \text{Monthly Price} \times \text{Gross Margin} \times \text{Lifetime}
$$

$$
\text{LTV} = 1000 \times 0.70 \times 10 = ₹7{,}000
$$

### Python Verification

```py
monthly_subs_price = 1000
gross_margin = 0.70
avg_cust_lt = 10  # months
cac = 6000

ltv = monthly_subs_price * gross_margin * avg_cust_lt
ratio = ltv / cac

print(f"LTV: ₹{ltv:,.0f}")
print(f"LTV/CAC Ratio: {ratio:.2f}")
```

**Output:**

* LTV = ₹7,000
* LTV/CAC ≈ **1.17**


## Step 2: The First Illusion: "Much Higher"

Leadership claims that LTV is **much higher** than CAC.

Numerically:

* LTV = ₹7,000
* CAC = ₹6,000

This is **only ₹1,000 higher** which already signals fragility:

* Small forecasting errors can wipe out the entire surplus
* "Greater than" is not the same as "safely greater than"

At scale, **thin margins amplify risk**, not profitability.


## Step 3: Why LTV > CAC Is Not Sufficient?

The logic "as long as LTV exceeds CAC, scaling is profitable" silently assumes:

* Customers live exactly as long as the average
* Revenue is earned quickly
* No additional costs matter
* Cash flow timing is irrelevant

None of these assumptions hold in real subscription businesses.

To see this clearly, we need to examine **payback time**.


## Step 4: CAC Payback Analysis

### Monthly Gross Contribution

Monthly gross contribution per customer:

$$
\text{Monthly Gross Profit} = 1000 \times 0.70 = ₹700
$$

This ₹700 is **not net profit**. It is the amount available each month to:

* Recover CAC
* Cover overhead
* Eventually generate profit

### CAC Payback Period

$$
\text{Payback Period} = \frac{\text{CAC}}{\text{Monthly Gross Contribution}}
$$

$$
\text{Payback} = \frac{6000}{700} \approx 8.6 \text{ months}
$$

### Python Verification

```py
monthly_gross_profit = monthly_subs_price * gross_margin
cac_payback = cac / monthly_gross_profit

print(f"Monthly Gross Profit: ₹{monthly_gross_profit}")
print(f"CAC Payback Period: {cac_payback:.1f} months")
```

**Output:**

* Monthly gross contribution = ₹700
* CAC payback ≈ **8.6 months**


## Step 5: The Real Risk

Now compare:

* **Average customer lifetime:** 10 months
* **CAC payback time:** 8.6 months

This means:

* The company recovers CAC **very late** in the customer's life
* Only ~1.4 months remain to generate surplus
* Any deviation breaks the model

This unit economics profile is **extremely fragile**.


## Step 6: Why Scaling Makes This Worse, Not Better?

This model only works if reality matches the spreadsheet exactly.

Consider small, realistic deviations:

* Lifetime drops from 10 → 9 months
* CAC increases slightly due to auction pressure
* Customers churn earlier than average
* Cash collections are slower than expected

Because CAC is paid **upfront** and LTV is earned **gradually**, scaling amplifies:

* Cash burn
* Downside risk
* Sensitivity to variance

This is how companies **grow into bankruptcy** while believing they are profitable.


## Step 7: Interpreting LTV Correctly

LTV is:

* An **average**
* A **long-term expectation**
* Earned **over time**

It is **not**:

* Cash in hand
* Guaranteed
* Symmetric around the mean

Basing aggressive scaling decisions on thin LTV/CAC margins ignores this asymmetry.


## Final Decision: Should the Company Scale Aggressively?

**No. The company should not scale aggressively.**

Although LTV exceeds CAC on paper:

* LTV/CAC ≈ **1.17**
* Payback ≈ **8.6 months** on a **10-month lifetime**

This leaves:

* No buffer for error
* No room for overhead
* No resilience under scale

Scaling ads under these conditions is more likely to **destroy value than create it**.


## What Should Be Fixed Before Scaling?

Scaling should only be considered after improving unit economics by:

* **Reducing CAC** (better channels, referrals, conversion efficiency)
* **Increasing customer lifetime** (churn reduction, retention, annual plans)
* **Improving margins or pricing** (pricing power, cost optimization)


## Core Insight

> **LTV > CAC is a necessary condition for profitability, not a sufficient one.**

* **LTV/CAC ≥ 3**
* **Payback ≤ 6 months**

These are not laws, but they exist to ensure **margin for error**, not perfection.

Ignoring payback timing and fragility turns "profitable growth" into an illusion that only collapses faster as the company scales.


### 📄 **Quick-read version available**

A condensed, visual PDF version of this case study is shared on my LinkedIn for a fast, high-level overview.

👉 View the PDF summaries on LinkedIn: **[Documents section](https://www.linkedin.com/in/ns-nibedita-sahu/recent-activity/documents/)**
