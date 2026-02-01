# Electric Vehicle Population Analysis

## 1. Context & Motivation

Electric Vehicles (EVs) are often discussed in terms of innovation, sustainability, and future mobility. However, beyond high-level narratives, meaningful decisions around EV adoption require a grounded understanding of how EVs are actually distributed, how they perform, and how policy mechanisms interact with real-world adoption patterns.

This project focuses on analyzing EV population data to move beyond surface-level trends and answer practical, analytics-driven questions:
- Where is EV adoption concentrated?
- How do different EV types compare in real-world performance?
- How aligned is EV adoption with clean energy policy eligibility?

Rather than treating this as a modeling or prediction problem, the project approaches EV data as an **analytics and decision-support problem**, emphasizing exploration, synthesis, and communication of insights.


## 2. Problem Framing & Analytical Objective

At its core, this project aims to analyze **EV adoption trends, performance variations, and clean energy policy eligibility**, and to communicate these insights clearly through structured visual storytelling.

The primary analytical objective is:

> To understand how EV adoption, performance, and policy eligibility interact, so that data-driven decisions can be informed around planning, prioritization, and future direction within the EV ecosystem.

This project does **not** attempt to:
- predict future EV adoption
- build production-grade models
- establish causal relationships

Instead, it focuses on **descriptive and exploratory analytics** that help translate raw population data into actionable understanding.


## 3. Data Overview & Constraints

The dataset used in this project contains **Electric Vehicle Population Data** with approximately **247k records**, including information on:
- EV make and model
- model year
- electric vehicle type (BEV vs PHEV)
- electric range
- geographic attributes (county, city)
- Clean Alternative Fuel Vehicle (CAFV) eligibility

From the outset, the dataset presented practical constraints:
- large row count
- mixed data quality
- memory considerations for in-memory analysis tools

These constraints directly influenced how the analytical workflow was designed.


## 4. Analytical Workflow Design

Rather than selecting tools arbitrarily, the workflow was intentionally structured based on **data scale, analytical purpose, and cost of exploration**.

The pipeline follows a clear progression:

**SQL → Python → Power BI**

Each tool serves a distinct analytical role:
- **SQL** handles scale-efficient filtering and structural cleaning.
- **Python** enables deeper exploration, validation, and refinement.
- **Power BI** focuses on insight communication and synthesis.

This design ensures that computationally expensive exploration is performed only after the dataset has been reduced to a manageable and analytically meaningful size.


## 5. Stage 1: SQL (Scaling Down the Problem)

Given the size of the raw dataset, SQL was used as the first analytical tool to:
- enforce appropriate data types
- remove invalid or incomplete records
- perform basic exploration and preprocessing

The goal at this stage was **not deep analysis**, but **problem reduction**.

Through SQL-based filtering and cleanup, the dataset was reduced from approximately **247k records to 97k records**.  
This step significantly lowered the cost of downstream analysis while preserving analytically relevant information.

SQL acted as a **structural gatekeeper**, ensuring that only usable data entered the in-memory analytics phase.


## 6. Stage 2: Python (Understanding the Data)

Once the dataset was reduced and stabilized, it was loaded into Python for deeper exploration.

A key analytical decision at this stage was to treat **Exploratory Data Analysis (EDA) as a first-class task**, rather than a quick preliminary step.

### Automated EDA as a Strategic Move

An automated EDA report was generated using **Pandas Profiling (YData Profiling)** to quickly surface:
- data distributions
- missing value patterns
- potential anomalies
- variable relationships

This provided a fast, global understanding of the dataset and helped avoid premature conclusions.

### Manual Exploration for Validation

Despite the automated report, manual exploration was still performed:
- to validate automated findings
- to build intuition around key variables
- to confirm assumptions before visualization

This intentional redundancy improved confidence in the insights rather than introducing inefficiency.

Following additional refinement, the dataset was further reduced from **97k to ~70k records**, forming the finalized dataset for visualization and storytelling.


## 7. Stage 3: Power BI (From Analysis to Insight)

The refined dataset was then used to build a **three-page Power BI report**, designed explicitly for analytical storytelling rather than exploratory analysis.

Each page serves a distinct purpose:

### Page 1: EV Population Overview
- Establishes scale and context
- Introduces EV type distribution
- Highlights geographic concentration
- Surfaces early policy signals

### Page 2: EV Trends & Performance Insights
- Compares adoption vs performance
- Highlights differences between popularity and electric range
- Examines manufacturer and model-level dynamics

### Page 3: EV Policy Impact & Clean Energy Eligibility
- Connects EV types and performance to CAFV eligibility
- Quantifies policy alignment
- Identifies manufacturers most aligned with clean energy incentives

Only insights that survived earlier exploration stages were visualized, ensuring clarity and focus.


## 8. Key Insights & Implications

Several consistent patterns emerged across the analysis:

- EV adoption is **geographically concentrated**, not evenly distributed.
- BEVs dominate both adoption and electric range performance.
- Popular models are not always the highest-performing in terms of range.
- Approximately **73% of EVs are CAFV eligible**, indicating strong, but not complete, policy alignment.
- Certain manufacturers consistently align better with clean energy eligibility and performance benchmarks.

These insights can inform decisions related to:
- infrastructure planning
- policy focus areas
- manufacturer positioning
- future adoption strategies


## 9. Limitations & Trade-offs

This analysis has important limitations:
- The data represents a specific geographic scope and may not generalize universally.
- Results are descriptive, not causal.
- Policy eligibility rules are treated as static, despite evolving regulations.

Acknowledging these constraints is essential to avoid overinterpretation of results.

----

This project demonstrates an end-to-end analytics workflow where **tool choices are driven by analytical intent**, not habit. By prioritizing data understanding, structured reduction, and clear communication, the analysis bridges raw population data and meaningful decision-oriented insights.


View the Complete Project Repository: **[Electric Vehicle Population Analysis](https://github.com/nibeditans/Electric-Vehicle-Population-Analysis)**
