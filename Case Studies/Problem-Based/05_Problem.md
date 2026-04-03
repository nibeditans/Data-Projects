# When the Average Hides the Real Customer Experience

## Context

An e-commerce company monitors delivery performance through a dashboard used by leadership and operations teams. One of the key headline metrics on the dashboard is **average delivery time**.

The current dashboard reports:

> **Average delivery time = 3 days**

Based on this metric, leadership assumes that delivery performance is strong and customers are generally receiving their orders quickly.

However, averages can sometimes conceal important patterns in the underlying data. Before accepting the dashboard metric as an accurate reflection of delivery performance, it is necessary to examine how delivery times are distributed across different customer segments.

The goal of this analysis is to evaluate whether the reported average truly reflects the customer experience and to identify any operational risks hidden behind the headline metric.

## Problem Statement

Delivery performance for the past month is summarized by order type as follows:

| Order Type | Number of Orders | Delivery Time (days) |
| ---------- | ---------------- | -------------------- |
| Local      | 800              | 2                    |
| Regional   | 150              | 5                    |
| Remote     | 50               | 12                   |

The company wants to understand:
* Whether the reported **3-day average delivery time** accurately reflects customer experience.
* Whether any important delivery risks are hidden within the aggregated metric.
* Which metrics would provide a clearer picture of delivery performance.

## Verifying the Dashboard Metric

To verify the calculation programmatically, we can represent the delivery data in Python.

```py
import pandas as pd

df = pd.DataFrame({
    "order_type": ["Local", "Regional", "Remote"],
    "no_of_orders": [800, 150, 50],
    "delivery_time": [2, 5, 12]
})

df
```

The first step is to verify whether the dashboard metric is mathematically correct.

Because each delivery time applies to a different number of orders, the correct calculation uses a **weighted average**, where each delivery time is weighted by the number of orders in that segment.

$$
\text{Average Delivery Time} =
\frac{\sum (Orders_i \times DeliveryTime_i)}{\sum Orders_i}
$$

Substituting the available data:

$$
\frac{(800 \times 2) + (150 \times 5) + (50 \times 12)}{800 + 150 + 50}
= \frac{1600 + 750 + 600}{1000}
= 2.95 \text{ days}
$$

```py
avg_delivery_time = (
    df["no_of_orders"] * df["delivery_time"]
).sum() / df["no_of_orders"].sum()

avg_delivery_time # 2.95
```

Rounded to the nearest whole number, this equals **3 days**, which matches the value shown on the dashboard.

This confirms that the dashboard metric is **technically correct**. The issue is therefore not a calculation error but rather how well the average represents the underlying customer experience.

## Distribution of Customer Experiences

To understand the delivery experience more clearly, it is helpful to examine how orders are distributed across segments.

```py
order_share = (
    df[["order_type"]]
    .assign(
        share_pct=lambda x: df["no_of_orders"] /
        df["no_of_orders"].sum() * 100
    )
)

order_share
```

| Order Type | Orders | Share of Orders |
| ---------- | ------ | --------------- |
| Local      | 800    | 80%             |
| Regional   | 150    | 15%             |
| Remote     | 50     | 5%              |

Several important observations emerge:
* **80% of customers receive deliveries in approximately 2 days.**
* **15% of customers wait about 5 days.**
* **5% of customers wait as long as 12 days.**

While most customers receive fast deliveries, a meaningful portion of customers experience significantly slower service.

From the perspective of these customers, the system does not feel like a **3-day delivery service**.

For example:
* Regional customers wait **2.5 times longer** than Local customers.
* Remote customers wait **6 times longer** than Local customers.

This variation highlights a large gap between the headline metric and the actual experience of certain customer groups.

## Why the Average Becomes Misleading?

The average delivery time is heavily influenced by the largest segment of orders. Because **Local deliveries account for 80% of all orders**, their relatively fast delivery time strongly pulls the average downward.

As a result, the overall mean reflects the performance of the majority group rather than the full range of customer experiences.

This creates a situation where:
* The average appears healthy.
* Significant delivery delays experienced by smaller segments remain hidden.

In statistical terms, the mean alone does not describe the **distribution of outcomes**. When variability is large, relying on the mean can obscure important operational realities.

One way to quantify how spread out delivery times are is to measure variance or standard deviation. A high standard deviation indicates that delivery experiences vary widely across customers rather than clustering around the mean.

```py
import numpy as np

# Expand the dataset so each order is represented
expanded_delivery_times = np.repeat(
    df["delivery_time"],
    df["no_of_orders"]
)

# Standard deviation of delivery times
delivery_std = expanded_delivery_times.std()

delivery_std # 2.34
```

In this case, the delivery system exhibits **high variability**, with delivery times ranging from **2 days to 12 days**.

## Hidden Operational Risk

If leadership relies only on the average delivery time, several risks may remain unnoticed.

### Uneven customer experience

Customers in Regional and Remote areas consistently experience slower deliveries. These customers may perceive the service as unreliable or inefficient compared to the majority of customers receiving faster deliveries.

### Silent churn risk

Customers facing longer delivery times may gradually reduce purchases or shift to competitors offering more consistent delivery performance.

Because the overall average still appears healthy, these problems may develop without being immediately visible in leadership dashboards.

### Operational blind spots

A single average metric may prevent teams from identifying structural issues in logistics operations, such as:

* limited regional distribution capacity
* longer shipping routes to remote areas
* supply chain delays affecting specific regions

Without additional metrics, operational inefficiencies affecting smaller customer groups can remain hidden.

## Metrics That Better Represent Delivery Performance

To provide a more accurate picture of delivery performance, the dashboard should include metrics that capture both the average and the variability of delivery experiences.

### Segment-level delivery metrics

Reporting delivery times separately for each segment provides immediate visibility into differences across customer groups.

For example:
* Local customers: **2 days**
* Regional customers: **5 days**
* Remote customers: **12 days**

Segment-level metrics allow operational teams to quickly identify where delays occur.

### Tail performance metrics

Metrics that capture the experience of slower deliveries are particularly useful for identifying service issues.

Examples include:
* **P90 delivery time**, representing the delivery time experienced by the slowest 10% of orders
* Percentage of orders taking **more than 7 days**

These metrics highlight the performance of the system under less favorable conditions.

### On-time delivery rate

Customers are less concerned with averages than with whether their orders arrive within the promised delivery window.

A useful metric is the **on-time delivery rate**:

$$
\text{On-Time Delivery Rate} =
\frac{\text{Orders delivered within promised window}}{\text{Total Orders}}
$$

This directly reflects the reliability of the delivery system from the customer’s perspective.

## Key Insight

The reported **3-day average delivery time** is mathematically accurate but operationally incomplete.

While the majority of customers receive fast deliveries, a significant minority experiences much longer wait times. The large volume of fast deliveries masks slower deliveries in smaller segments, making the average appear more favorable than the full distribution of delivery times would suggest.

This case illustrates an important principle in data analysis:

**Averages alone rarely capture the full story.**

Understanding the distribution of outcomes is essential for accurately evaluating customer experience and operational performance.

## Conclusion

The company’s headline metric of **average delivery time = 3 days** correctly summarizes the weighted mean delivery time but fails to fully represent the variability in customer experiences.

A substantial share of customers waits significantly longer than the headline metric suggests, particularly those in Regional and Remote locations.

To better monitor delivery performance, the company should complement the average with additional metrics, including:

* segment-level delivery times
* tail performance indicators such as P90 delivery time
* on-time delivery rate

Together, these metrics provide a more complete view of delivery performance and help ensure that operational issues affecting smaller customer groups are not overlooked.

### 📄 **Quick-read version available**

A condensed, visual PDF version of this case study is shared on my LinkedIn for a fast, high-level overview.

👉 View the PDF summaries on LinkedIn: **[Documents section](https://www.linkedin.com/in/ns-nibedita-sahu/recent-activity/documents/)**
