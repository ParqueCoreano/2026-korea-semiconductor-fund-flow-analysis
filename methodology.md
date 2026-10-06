# Analysis Methodology

## 1. Purpose

This document defines the analytical methodology used to evaluate semiconductor sector rotation in the Korean equity market.

The analysis focuses on whether market momentum and capital allocation have expanded from memory semiconductors toward semiconductor equipment, materials, and components since July 2026.

---

# 2. Research Question

> Is Korea's semiconductor rally rotating beyond memory into semiconductor equipment, materials, and components, particularly KOSDAQ-listed companies, since July 2026?

---

# 3. Hypothesis

The initial hypothesis is:

> Market momentum may have expanded from major memory semiconductor companies toward semiconductor equipment, materials, and components since July 2026.

This hypothesis will not be accepted based on stock price performance alone.

Multiple indicators will be evaluated together.

---

# 4. Analysis Framework

The analysis consists of three major dimensions.

### 4.1 Performance

Measure whether semiconductor equipment, materials, and components have outperformed memory semiconductor companies.

### 4.2 Capital Flow

Evaluate whether investor and ETF-related activity is consistent with increased capital allocation toward these segments.

### 4.3 Market Breadth

Determine whether the potential rotation is broad-based or driven by a small number of companies.

---

# 5. Analysis Period

## Baseline Period

January 2026 – Present

The baseline period provides sufficient historical context before the core analysis window.

## Core Period

July 2026 – Present

July 2026 is treated as a hypothesis-driven potential regime-change point.

The analysis will test whether market behavior changed meaningfully after this date.

---

# 6. Performance Analysis

## 6.1 Stock Return

Daily return will be calculated as:

```text
Daily Return = (Close Price / Previous Close Price) - 1
```

Cumulative return will be calculated as:

```text
Cumulative Return = (Current Price / Starting Price) - 1
```

---

## 6.2 Segment Performance

Stocks will be grouped into semiconductor value-chain categories:

* Memory
* Equipment
* Materials
* Components

Segment-level performance will be calculated using appropriate aggregation methods.

Where possible, equal-weighted and market-capitalization-weighted approaches will be compared.

---

## 6.3 Relative Performance

Relative performance will compare the return of a semiconductor segment against a reference segment.

Example:

```text
Relative Performance =
Equipment Return - Memory Return
```

A positive value indicates that the equipment segment outperformed memory during the selected period.

---

# 7. Trading Activity

Trading activity will be measured using:

* Trading value
* Trading volume
* Average daily trading value
* Change in trading activity

The analysis will compare activity before and after July 2026.

Example:

```text
Trading Activity Change =
Post-July Average Trading Value
/
Pre-July Average Trading Value
- 1
```

Higher activity may indicate increased market attention but does not by itself prove capital inflow.

---

# 8. Investor Flow Analysis

Where reliable investor-flow data is available, the analysis will consider:

* Foreign investor net buying
* Institutional investor net buying
* Retail investor net buying

The analysis will compare investor behavior across semiconductor value-chain categories.

Example:

```text
Cumulative Net Buying =
Σ Daily Net Buying
```

Investor flow will be analyzed together with price performance rather than independently.

---

# 9. ETF Analysis

ETFs will be used as market proxies for semiconductor segments.

Potential ETF groups include:

* Memory
* Equipment
* Materials
* Components
* Front-end process
* Back-end process

The analysis may include:

* ETF return
* Trading value
* NAV
* AUM
* Shares outstanding
* Premium / discount

---

# 10. ETF Flow Interpretation

ETF AUM changes will not automatically be interpreted as investor inflows.

AUM can change due to:

* Market price movements
* Net subscriptions or redemptions
* Portfolio changes
* Other fund-level effects

Therefore, ETF flow conclusions will require supporting evidence from multiple variables where available.

---

# 11. Market Breadth

Market breadth measures how widely a movement is distributed across companies.

Potential breadth indicators include:

### Positive Return Ratio

```text
Positive Return Ratio =
Number of stocks with positive return
/
Total stocks
```

### Moving Average Breadth

```text
MA20 Breadth =
Number of stocks above 20-day moving average
/
Total stocks
```

These metrics help distinguish broad sector rotation from performance concentrated in a small number of stocks.

---

# 12. KOSDAQ Analysis

A specific focus will be placed on KOSDAQ-listed semiconductor companies.

The analysis will compare:

* KOSPI semiconductor companies
* KOSDAQ semiconductor companies
* Equipment companies
* Materials companies
* Components companies

The objective is to determine whether market participation has broadened toward smaller semiconductor-related companies.

---

# 13. Fundamental Analysis

Market performance will be compared with company fundamentals where data availability permits.

Potential indicators include:

* Revenue growth
* Operating profit growth
* Net income growth
* Profit margin
* Asset growth

The purpose is not to determine whether a stock is fundamentally attractive, but to identify whether market performance is supported by improving business fundamentals.

---

# 14. Rotation Score

A composite rotation score may be developed to summarize evidence of sector rotation.

A potential framework is:

```text
Rotation Score =
Performance Score
+ Flow Score
+ Breadth Score
```

The exact weights will be determined after reviewing data availability and statistical behavior.

The methodology and weights will be explicitly documented before final conclusions are presented.

The score will be treated as an analytical framework rather than an objective measure of actual capital movement.

---

# 15. Pre- and Post-July Comparison

The analysis will compare market behavior before and after July 2026.

Potential comparison metrics include:

| Metric                   | Pre-July | Post-July |
| ------------------------ | -------: | --------: |
| Cumulative Return        |          |           |
| Average Trading Value    |          |           |
| Foreign Net Buying       |          |           |
| Institutional Net Buying |          |           |
| Positive Return Ratio    |          |           |
| MA20 Breadth             |          |           |
| Volatility               |          |           |

This comparison will help identify whether market behavior changed after the proposed regime-change point.

---

# 16. Statistical Validation

Where appropriate, the analysis may include:

* Correlation analysis
* Rolling correlation
* Volatility comparison
* Relative performance analysis
* Simple regression
* Event-window analysis

Statistical methods will be selected based on data availability and the specific analytical question.

---

# 17. Data Quality Validation

Before analysis, the following checks will be performed:

### Completeness

Check for missing trading dates and missing observations.

### Uniqueness

Check for duplicate company-date or ETF-date records.

### Validity

Check for invalid prices, negative values, and unexpected records.

### Consistency

Ensure consistent ticker, company, date, and market classifications.

### Timeliness

Record the latest available data date.

---

# 18. Avoiding Overinterpretation

The project will distinguish between:

### What the data can show

* Relative performance
* Trading activity
* Investor net buying
* ETF activity
* Market breadth
* Fundamental changes

### What the data cannot directly prove

* The exact intention of investors
* The exact source of capital
* Direct causality between events and stock performance
* Future stock returns

Therefore, conclusions will use evidence-based language such as:

* "The data suggests..."
* "The evidence is consistent with..."
* "Relative performance indicates..."
* "Investor flows show..."

rather than making unsupported causal claims.

---

# 19. Reproducibility

The analysis should be reproducible through:

* Documented data sources
* Python ETL scripts
* SQL queries
* Defined transformation rules
* Documented assumptions
* Version-controlled project files

The GitHub repository will serve as the project record.

---

# 20. Final Analytical Output

The final analysis will answer three main questions:

### Q1

Did equipment, materials, and components outperform memory after July 2026?

### Q2

Is there evidence of increased capital allocation toward these segments?

### Q3

Was the movement broad-based across KOSDAQ semiconductor companies?

The final conclusion will combine performance, flow, breadth, and fundamental evidence.
