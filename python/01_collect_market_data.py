##기존의 연결 테스트 코드와 실제 데이터 수집 코드를 분리

import os
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime       #오늘 날짜를 자동으로 가져오는 데 사용

# Load environment variables from .env
load_dotenv()

# Read KIS API credentials
APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")

print("APP_KEY loaded:", bool(APP_KEY))
print("APP_SECRET loaded:", bool(APP_SECRET))
print(
    "APP_KEY has surrounding whitespace:",
    APP_KEY != APP_KEY.strip() if APP_KEY else "empty"
)
print(
    "APP_SECRET has surrounding whitespace:",
    APP_SECRET != APP_SECRET.strip() if APP_SECRET else "empty"
)

# Read the API base URL
BASE_URL = os.getenv(
    "KIS_BASE_URL",
    "https://openapi.koreainvestment.com:9443"
)

# Check whether required settings exist
if not APP_KEY:
    raise ValueError("KIS_APP_KEY is missing from .env")

if not APP_SECRET:
    raise ValueError("KIS_APP_SECRET is missing from .env")

print("Environment variables loaded successfully.")


# Request an access token
token_url = BASE_URL + "/oauth2/tokenP"

token_response = requests.post(
    token_url,
    headers={"content-type": "application/json"},
    json={
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    },
    timeout=10
)

print("Token HTTP Status:", token_response.status_code)
print("Token response received.")

token_response.raise_for_status()
token_data = token_response.json()
access_token = token_data["access_token"]

print("Access token received.")

# Request Samsung Electronics daily price data
stock_code = "005930"

url = (
    BASE_URL
    + "/uapi/domestic-stock/v1/quotations/"
    + "inquire-daily-itemchartprice"
)

headers = {
    "content-type": "application/json",
    "authorization": f"Bearer {access_token}",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "FHKST03010100"
}

params = {
    "FID_COND_MRKT_DIV_CODE": "J",
    "FID_INPUT_ISCD": stock_code,
    "FID_INPUT_DATE_1": "20261001",     
    "FID_INPUT_DATE_2": datetime.now().strftime("%Y%m%d"),    
    "FID_PERIOD_DIV_CODE": "D",
    "FID_ORG_ADJ_PRC": "1"
}

#시작날짜
 #종료날짜 : 컴퓨터의 현재 날짜와 시간을 가져와서 YYYYMMDD 형식으로 변환

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=10
)

response.raise_for_status()
data = response.json()

# Check the API's business-level response
if data.get("rt_cd") != "0":
    raise RuntimeError(
        f"KIS API error: {data.get('msg1', 'Unknown error')}"
    )

daily_data = data.get("output2", [])

print("Stock data received.")
print("Number of records:", len(daily_data))


# Convert JSON records into a Pandas DataFrame
df = pd.DataFrame(daily_data)

if df.empty:
    raise ValueError(
        "No stock data returned. Check the date range and API response."
    )

# Rename API column names to readable English names
column_mapping = {
    "stck_bsop_date": "trade_date",
    "stck_oprc": "open_price",
    "stck_hgpr": "high_price",
    "stck_lwpr": "low_price",
    "stck_clpr": "close_price",
    "acml_vol": "volume",
    "acml_tr_pbmn": "trading_value"
}

df = df.rename(columns=column_mapping)

# Convert the date column to a proper date type
if "trade_date" in df.columns:
    df["trade_date"] = pd.to_datetime(
        df["trade_date"],
        format="%Y%m%d",
        errors="coerce"
    )

# Convert numeric columns from text to numbers
numeric_columns = [
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "volume",
    "trading_value"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

# Show the result

# Keep only the columns needed for analysis
required_columns = [
    "trade_date",
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "volume",
    "trading_value"
]

df = df[required_columns].copy()

# Sort by date from oldest to newest
df = df.sort_values("trade_date").reset_index(drop=True)

# Add the stock ticker
df["stock_code"] = stock_code

# Display the final result
print("\nCleaned DataFrame:")
print(df)

print("\nData types:")
print(df.dtypes)

print("\nTransformation completed.")

# Save cleaned data to SQL Server
import pyodbc

server = r"DESKTOP-29RVDTS\SQLEXPRESS"
database = "Finance_dataflow"
driver = "{ODBC Driver 17 for SQL Server}"

connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

try:
    # Convert dates and numeric values to Python types
    rows = []
    for row in df.itertuples(index=False):
        rows.append((
            row.trade_date.date(),
            str(row.stock_code),
            int(row.open_price),
            int(row.high_price),
            int(row.low_price),
            int(row.close_price),
            int(row.volume),
            int(row.trading_value)
        ))

    # Replace existing records for the same stock and date
    for row in rows:
        cursor.execute(
            """
            DELETE FROM dbo.daily_stock_prices
            WHERE stock_code = ? AND trade_date = ?
            """,
            row[1], row[0]
        )

    cursor.executemany(
        """
        INSERT INTO dbo.daily_stock_prices (
            trade_date, stock_code, open_price, high_price,
            low_price, close_price, volume, trading_value
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows
    )

    conn.commit()
    print(f"SQL Server save successful: {len(rows)} rows")

except Exception:
    conn.rollback()
    raise

finally:
    cursor.close()
    conn.close()
