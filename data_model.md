# Data Model

## 1. Purpose

This document defines the logical data model for the Korea Semiconductor Fund Flow Analysis project.

The model is designed to support financial market analysis, investor flow analysis, ETF analysis, company fundamentals, and Power BI reporting.

The database will follow a dimensional modeling approach using fact and dimension tables.

---

# 2. Modeling Approach

The project uses a simplified star schema.

### Dimension Tables

Dimension tables provide descriptive information used to analyze financial data.

* `dim_date`
* `dim_company`
* `dim_etf`

### Fact Tables

Fact tables contain measurable financial and market observations.

* `fact_stock_price`
* `fact_stock_flow`
* `fact_etf_price`
* `fact_etf_flow`
* `fact_financials`
* `fact_data_quality`

---

# 3. High-Level Data Model

```text
                         dim_date
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
     fact_stock_price  fact_stock_flow  fact_etf_price
             │              │              │
             │              │              │
             ▼              ▼              ▼
       dim_company     dim_company       dim_etf
             │                             │
             │                             │
             ▼                             ▼
     fact_financials                 fact_etf_flow
```

The date dimension provides a common time reference for market and financial analysis.

---

# 4. Company Dimension

Table: `dim_company`

The company dimension contains the master information used to identify and classify Korean listed companies.

### Key Fields

* `company_id`
* `ticker`
* `company_name`
* `market`
* `value_chain`
* `is_active`

### Value Chain Categories

Companies will initially be classified into:

* Memory
* Equipment
* Materials
* Components

### Market Categories

* KOSPI
* KOSDAQ

---

# 5. Stock Price Fact

Table: `fact_stock_price`

This table stores daily market observations for individual companies.

### Grain

One row represents:

> One company on one trading date.

### Business Key

```text
trade_date + company_id
```

### Main Measures

* Open price
* High price
* Low price
* Close price
* Trading volume
* Trading value

### Derived Measures

* Daily return
* Cumulative return
* Rolling volatility
* Moving averages
* Relative performance

---

# 6. Stock Investor Flow Fact

Table: `fact_stock_flow`

This table stores investor trading information where reliable source data is available.

### Grain

One row represents:

> One company on one trading date.

### Main Measures

* Foreign investor net buying
* Institutional investor net buying
* Retail investor net buying

### Analytical Purpose

This table helps evaluate whether observed price movements are accompanied by changes in investor participation.

---

# 7. ETF Dimension

Table: `dim_etf`

This table contains ETF master information.

### Main Fields

* ETF ticker
* ETF name
* Asset manager
* Value chain
* Benchmark or investment strategy

### Initial ETF Groups
