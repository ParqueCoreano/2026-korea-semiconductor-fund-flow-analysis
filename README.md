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
STEP 07 Pandas Transformation         ⬜ 
STEP 08 Data Validation               ⬜
STEP 09 SQL Server                    ⬜
STEP 10 SQL Analysis                  ⬜
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

