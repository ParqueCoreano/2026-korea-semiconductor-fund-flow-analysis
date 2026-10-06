# Data Dictionary

## 1. Purpose

This document defines the main fields used in the Korea Semiconductor Fund Flow Analysis project.

The purpose of the data dictionary is to maintain consistent definitions across Python, SQL Server, and Power BI.

---

# 2. Company Master

Table: `dim_company`

| Column           | Data Type    | Description                                     |
| ---------------- | ------------ | ----------------------------------------------- |
| `company_id`     | INT          | Unique internal company identifier              |
| `ticker`         | VARCHAR(20)  | Korean stock ticker                             |
| `company_name`   | VARCHAR(100) | Company name                                    |
| `market`         | VARCHAR(20)  | KOSPI or KOSDAQ                                 |
| `value_chain`    | VARCHAR(30)  | Memory, Equipment, Materials, or Components     |
| `is_active`      | BIT          | Whether the company is included in the analysis |
| `effective_date` | DATE         | Date from which the classification is valid     |

---

# 3. Stock Price Data

Table: `fact_stock_price`

| Column          | Data Type     | Description                              |
| --------------- | ------------- | ---------------------------------------- |
| `trade_date`    | DATE          | Trading date                             |
| `company_id`    | INT           | Reference to `dim_company`               |
| `open_price`    | DECIMAL(18,2) | Opening price                            |
| `high_price`    | DECIMAL(18,2) | Highest price during the trading session |
| `low_price`     | DECIMAL(18,2) | Lowest price during the trading session  |
| `close_price`   | DECIMAL(18,2) | Closing price                            |
| `volume`        | BIGINT        | Trading volume                           |
| `trading_value` | DECIMAL(20,2) | Total trading value                      |

### Derived Metrics

The following metrics may be calculated later rather than stored directly in the raw table:

* Daily return
* Cumulative return
* Rolling volatility
* Moving averages
* Relative performance

---

# 4. Investor Flow Data

Table: `fact_stock_flow`

| Column                  | Data Type     | Description                             |
| ----------------------- | ------------- | --------------------------------------- |
| `trade_date`            | DATE          | Trading date                            |
| `company_id`            | INT           | Reference to `dim_company`              |
| `foreign_net_value`     | DECIMAL(20,2) | Foreign investor net buying value       |
| `institution_net_value` | DECIMAL(20,2) | Institutional investor net buying value |
| `retail_net_value`      | DECIMAL(20,2) | Retail investor net buying value        |

### Notes

Investor flow fields will only be included if reliable source data is available.

---

# 5. ETF Master

Table: `dim_etf`

| Column          | Data Type    | Description                                  |
| --------------- | ------------ | -------------------------------------------- |
| `etf_id`        | INT          | Unique internal ETF identifier               |
| `ticker`        | VARCHAR(20)  | ETF ticker                                   |
| `etf_name`      | VARCHAR(100) | ETF name                                     |
| `asset_manager` | VARCHAR(100) | ETF asset manager                            |
| `value_chain`   | VARCHAR(50)  | Semiconductor segment represented by the ETF |
| `benchmark`     | VARCHAR(200) | Reference index or investment strategy       |
| `is_active`     | BIT          | Whether the ETF is included in the analysis  |

---

# 6. ETF Market Data

Table: `fact_etf_price`

| Column          | Data Type     | Description            |
| --------------- | ------------- | ---------------------- |
| `trade_date`    | DATE          | Trading date           |
| `etf_id`        | INT           | Reference to `dim_etf` |
| `open_price`    | DECIMAL(18,2) | Opening price          |
| `high_price`    | DECIMAL(18,2) | Highest price          |
| `low_price`     | DECIMAL(18,2) | Lowest price           |
| `close_price`   | DECIMAL(18,2) | Closing price          |
| `volume`        | BIGINT        | Trading volume         |
| `trading_value` | DECIMAL(20,2) | Trading value          |
| `nav`           | DECIMAL(18,4) | Net asset value        |

---

# 7. ETF Fund Data

Table: `fact_etf_flow`

| Column               | Data Type     | Description                             |
| -------------------- | ------------- | --------------------------------------- |
| `trade_date`         | DATE          | Reference date                          |
| `etf_id`             | INT           | Reference to `dim_etf`                  |
| `aum`                | DECIMAL(20,2) | Assets under management                 |
| `shares_outstanding` | BIGINT        | Number of ETF shares outstanding        |
| `premium_discount`   | DECIMAL(10,4) | Difference between market price and NAV |

### Important Note

ETF AUM changes should not automatically be interpreted as investor inflows.

AUM can change because of:

* Price movements
* Net subscriptions/redemptions
* Changes in holdings
* Other fund-level effects

Therefore, ETF flow analysis will consider multiple variables together.

---

# 8. Financial Data

Table: `fact_financials`

| Column       | Data Type | Description                |
| ------------ | --------- | -------------------------- |
| `company_id` | INT       | Reference to `dim_company` |
| `fis         |           |                            |
