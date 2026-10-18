# 2026-korea-semiconductor-fund-flow-analysis
An end-to-end financial data analytics project tracking capital rotation from memory semiconductors to semiconductor equipment and materials in Korea.
한국 내 메모리 반도체에서 반도체 장비 및 소재로의 자본 이동을 추적하는 엔드투엔드(end-to-end) 금융 데이터 분석 프로젝트

# Korea Semiconductor Fund Flow Analysis

## Project Overview
This project investigates whether capital and market momentum
have rotated from memory semiconductors toward semiconductor
equipment, materials, and components in Korea since July 2026.
이 프로젝트는 2026년 7월 이후 한국 시장에서 자본과 시장 모멘텀이 
메모리 반도체에서 반도체 장비, 소재 및 부품 분야로 이동했는지 여부를 분석하는 포괄적인 금융 데이터 분석 프로젝트입니다.

## Objective

The project combines financial market data, ETF data,
investor flows, and company fundamentals to analyze
semiconductor sector rotation.
이 프로젝트는 금융 시장 데이터, ETF 데이터, 투자자 자금 흐름, 그리고 기업 펀더멘털을 결합하여 반도체 섹터 로테이션을 분석을 목표합니다.

## Tech Stack

- Python
- Pandas
- SQL Server
- Power BI
- Git / GitHub

## Current Status

🚧 Project in progress

STEP 01 Business Question             ✅  (Day-1)  
STEP 02 Data Source Design            ✅
STEP 03 GitHub Setup                  ✅  (Day-2)
STEP 04 Python Environment            ✅
STEP 05 API Authentication            ✅  (Day-3)
STEP 06 Samsung Daily Price API TEST  ✅  (Day-4)
STEP 07 Pandas Transformation         ✅  (Day-5 / 9)
STEP 08 Data Validation               ✅  (Day-6 / 7)
STEP 09 SQL Server                    ✅  (Day-8 / 9)
STEP 10 SQL Analysis                  ✅  (Day-8 / 9)
STEP 11 Power BI                      ⬜
STEP 12 Investment Insight            ⬜


### Day 01 — Project Planning

**Completed**
- Defined the core business question for the project.
- Established the research focus on semiconductor sector rotation in Korea.
- Defined the hypothesis that market momentum may have expanded from memory semiconductors toward semiconductor equipment, materials, and components since July 2026.
- Defined the initial analysis scope, including KOSPI, KOSDAQ, individual semiconductor companies, investor flows, and ETF data.
- Designed the overall end-to-end data pipeline from data collection to Power BI analysis.

**Key Learning**
- Learned how to define a financial data project around a business question rather than starting with a visualization.
- Learned how to separate a research hypothesis from an analytical conclusion.

**Next Step**
- Identify reliable financial data sources and define how each source will be used.


### Day 02 — Data Source & GitHub Setup

**Completed**
- Selected KIS Open API as the primary source for Korean stock market data.
- Reviewed OpenDART as a potential source for company financial fundamentals.
- Defined the initial data categories required for the analysis, including stock prices, trading activity, investor flows, ETF data, and company fundamentals.
- Created the GitHub repository for the project.
- Created the initial project documentation structure.
- Added project planning, data source, data dictionary, data model, and methodology documentation.

**Key Learning**
- Learned how to select financial data sources based on data availability, reliability, and analytical requirements.
- Learned how GitHub can be used to document both the development process and the final analytical result.
- Learned the importance of defining data structure before starting data collection.

**Next Step**
- Set up the Python environment and prepare the API authentication process.

### Day 03 — Python Environment & KIS API Authentication

**Completed**
- Created a Python virtual environment for the project.
- Installed the required Python packages, including `requests`, `python-dotenv`, and `pandas`.
- Created a `.env` file for storing API credentials locally.
- Configured the KIS API App Key and App Secret as environment variables.
- Implemented the KIS Open API access token request.
- Successfully received an access token from the KIS production API.
- Added the API authentication test script to the GitHub repository.

**Key Learning**
- Learned how to create and manage an isolated Python environment using `venv`.
- Learned how to use environment variables to keep API credentials separate from source code.
- Learned the basic authentication flow required to access a financial REST API.
- Learned why API credentials should not be hard-coded or committed to GitHub.

**Next Step**
- Use the authenticated API connection to retrieve actual Korean stock market data.

### Day 04 — KIS API Connectivity Test

**Completed**
- Connected Python to the KIS Open API using the issued access token.
- Selected Samsung Electronics (005930) as the first test stock.
- Configured the KIS daily stock price API endpoint.
- Sent the required API headers and query parameters from Python.
- Successfully retrieved Samsung Electronics daily price data.
- Received and parsed the API response as JSON.
- Verified the API response code and message.
- Confirmed that the API returned daily market data successfully.
- Verified the end-to-end connection from Python to the KIS market data API.

**Key Learning**
- Learned how to send authenticated REST API requests using Python.
- Learned how API endpoints, headers, query parameters, and response data work together.
- Learned how to inspect and validate JSON responses from a financial data API.
- Confirmed that the KIS API connection is ready for the next ETL stage.

**Next Step**
- Transform the KIS API JSON response into a standardized Pandas DataFrame.
- Standardize column names and data types.
- Prepare the data for cleaning and validation.

### Day 05 — Pandas Data Transformation

**Completed**
- Created a dedicated Python script for collecting market data.
- Loaded API credentials and configuration from environment variables.
- Retrieved Samsung Electronics daily stock price data through the KIS Open API.
- Converted the JSON response into a Pandas DataFrame.
- Renamed API fields to standardized English column names.
- Converted the trading date and numeric fields to appropriate data types.
- Selected the required analytical columns.
- Sorted records by trading date in ascending order.
- Added the stock ticker to identify the company in the dataset.
- Verified the resulting DataFrame and its data types.

**Key Learning**
- Learned how to transform API responses into structured tabular data.
- Learned how to standardize column names and data types using Pandas.
- Learned how sorting and selecting columns prepare data for downstream analysis.
- Completed the initial data collection and transformation workflow for a financial data pipeline.

**Why It Matters**
- A standardized dataset is easier to validate, store in SQL Server, and analyze in Power BI.
- This workflow establishes the foundation for expanding the pipeline to additional stocks and market data.

**Next Step**
- Validate the collected data for missing values, duplicate records, invalid prices, and other data quality issues.

### Day 06 — Data Validation: Basic Quality Checks 

**What I Did**
- Checked for missing values. (결측값 확인)
- Checked for duplicate trading dates. (중복 거래일 확인)
- Validated closing prices and trading volumes. (거래량이 0 이하인 종가 확인 / 음수 거래량 확인)
- Checked the relationship between high and low prices. (고가와 저가의 관계 확인)

**Techniques Used**
- Pandas `isnull()`
- Pandas `duplicated()`
- Boolean conditions and `sum()`

**Key Learning**
- Data validation helps identify missing, duplicated, and logically invalid records before analysis.
- A result of zero means no records matched the specific validation condition.

**Next Step**
- Complete data validation and prepare the cleaned data for SQL Server.

### Day 07 — Data Validation: Automated Quality Checks

**What I Did**
- Checked for missing values and duplicate trading dates.
- Validated closing prices, trading volumes, and high-low price relationships.
- Implemented conditional logic using `if` and `else` to automatically report missing values.
- Executed the validation checks and reviewed the results.

**Techniques Used**
- Pandas `isnull()` and `duplicated()`
- Boolean conditions and `sum()`
- Python conditional statements (`if` / `else`)

**Key Learning**
- Data validation helps identify missing, duplicated, and logically invalid records before analysis.
- Conditional statements allow Python to evaluate validation results automatically.
- Passing basic validation checks does not guarantee that all data is accurate.

**Validation Results**
- Missing values: None found
- Duplicate trading dates: 0
- Invalid closing prices: 0
- Negative trading volumes: 0
- Invalid high-low price relationships: 0

**Next Step**
- Set up SQL Server and prepare a database table for the cleaned market data.

---

### Day 08 — SQL Server Integration and SQL Analysis

**Objective**

Set up SQL Server, connect Python to the database, store cleaned stock market data, and begin analyzing stock price movements using SQL.

**Completed Tasks**

- Connected to SQL Server Express using Windows Authentication.
- Created the `Finance_dataflow` database and the `daily_stock_prices` table with appropriate column names, data types, and a composite primary key (`stock_code`, `trade_date`).
- Connected Python to SQL Server using `pyodbc` and inserted cleaned Samsung Electronics daily stock data from a Pandas DataFrame.
- Verified inserted records using `SELECT`, filtered data using `WHERE`, and sorted results by trading date using `ORDER BY`.
- Used `LAG()` with `OVER (ORDER BY trade_date)` to retrieve the previous trading day's closing price.
- Calculated daily price changes by subtracting the previous closing price from the current closing price.
- Calculated percentage returns using arithmetic expressions, `NULLIF()` to prevent division by zero, and `ROUND()` to round results to two decimal places.
- Used a Common Table Expression (CTE) with `WITH` to organize intermediate query results and reuse them in subsequent calculations.
- Practiced `CAST()` to convert numeric data types for average calculations and explored `DECIMAL` for controlled numeric precision.
- Used aggregate functions to summarize stock data: `COUNT(*)` for row counts, `AVG()` for average prices and volume, `MAX()` and `MIN()` for price extremes, and `SUM()` for total trading volume and trading value.
- Compared `COUNT(*)` with `COUNT(DISTINCT trade_date)` to understand the difference between counting rows and counting unique trading dates.

**Key Learnings**
- Connected a Python data collection pipeline to a relational database.
- Learned how to query and validate stored financial data.
- Used window functions to compare current and previous stock prices.
- Learned how aggregate functions summarize trading activity and price data.

**Outcome**

Successfully connected Python to SQL Server, stored cleaned stock market data, and began SQL-based analysis of stock prices and trading activity.

**Technologies**
- Python
- Pandas
- pyodbc
- Microsoft SQL Server Express
- SQL Server Management Studio (SSMS)
- SQL

**Status:** Completed

**Next Step:** Continue SQL analysis and prepare the dataset for Power BI visualization.

### Day 09 — Data Pipeline Automation & SQL Analysis

- Modified the data collection script to calculate the end date dynamically based on the system date.
- Compared two data update strategies: skipping existing trading dates and updating existing records.
- Selected the update strategy to refresh records for existing trading dates.
- Created and tested a Windows `.bat` file to automate Python script execution.
- Loaded collected and cleaned stock price data into SQL Server.
- Validated stored data and analyzed daily price changes, daily returns, trading volume changes, and the 5-trading-day moving average.
- Calculated the overall price return for the selected period.

**Initial Finding**

Samsung Electronics' closing price decreased from KRW 276,000 on October 1, 2026, to KRW 217,000 on October 16, 2026, resulting in a price return of -21.38%.

*This is a preliminary result based on 10 trading-day observations and does not establish the broader semiconductor sector rotation hypothesis.*

**Next Steps**
- Expand data collection to semiconductor equipment, materials, and components stocks.
- Analyze investor trading flows.
- Compare performance before and after July 2026.

