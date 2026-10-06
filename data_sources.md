# Data Sources

## 1. Purpose

This document defines the data sources used in the Korea Semiconductor Fund Flow Analysis project.

The project prioritizes official and reliable financial data sources to improve data accuracy, reproducibility, and traceability.

---

## 2. Primary Data Sources

| Data Category            | Source                                 | Purpose                                                               |
| ------------------------ | -------------------------------------- | --------------------------------------------------------------------- |
| Korean stock market data | Korea Investment & Securities Open API | Stock prices, trading volume, trading value                           |
| ETF market data          | Korea Exchange / Asset Manager data    | ETF prices, NAV, AUM and related information                          |
| ETF composition          | Official ETF asset manager websites    | ETF holdings and sector classification                                |
| Company financial data   | OpenDART                               | Revenue, operating profit and other financial information             |
| Company information      | KRX / OpenDART                         | Company name, ticker, market classification and corporate information |

---

## 3. Korean Stock Market Data

### Source

Korea Investment & Securities (KIS) Open API

### Data to Collect

* Trading date
* Ticker
* Open price
* High price
* Low price
* Closing price
* Trading volume
* Trading value

Where available, investor trading information will also be collected.

### Purpose

The market data will be used to measure:

* Stock returns
* Relative performance
* Trading activity
* Volatility
* Market breadth
* Sector-level performance

---

## 4. ETF Data

### Source

Official ETF data from Korean asset managers and related market data sources.

Initial ETF candidates include:

* KODEX Semiconductor
* KODEX AI Semiconductor Core Equipment
* SOL AI Semiconductor Equipment, Materials & Components
* SOL Semiconductor Front-end Process
* SOL Semiconductor Back-end Process

The final ETF list will be confirmed after reviewing the latest ETF composition and investment objectives.

### Data to Collect

* ETF ticker
* ETF name
* Trading date
* Closing price
* NAV
* Trading volume
* Trading value
* AUM
* Number of shares
* Holdings / constituent information

### Purpose

ETF data will be used as market proxies for different segments of the semiconductor value chain.

ETF data will not be treated as direct proof of capital movement by itself.

---

## 5. Company Financial Data

### Source

OpenDART

### Data to Collect

* Company name
* Stock code
* Fiscal period
* Revenue
* Operating profit
* Net income
* Total assets
* Total liabilities
* Equity

Additional financial indicators may be added depending on data availability.

### Purpose

Financial data will be used to compare market performance with company fundamentals.

This helps distinguish market momentum from fundamental improvement.

---

## 6. Company Classification

Companies will be classified into semiconductor value-chain categories.

### Initial Categories

* Memory
* Equipment
* Materials
* Components

### Market Classification

Companies will also be classified by:

* KOSPI
* KOSDAQ

The classification methodology will be documented separately to improve transparency and reproducibility.

---

## 7. Data Quality Principles

The project will apply the following data quality checks:

### Completeness

Check for missing trading dates, prices, volumes, and company identifiers.

### Accuracy

Check values against official or reliable source data where possible.

### Consistency

Ensure consistent ticker formats, date formats, company names, and market classifications.

### Timeliness

Record the latest available date for each dataset.

### Uniqueness

Check for duplicate records based on appropriate business keys.

### Val
