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
stock_codes = ["005930", "000660"]

start_date = "20260701"
end_date = datetime.now().strftime("%Y%m%d")

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


all_stock_dfs = []

# 컬럼명 변경 규칙
column_mapping = {
    "stck_bsop_date": "trade_date",
    "stck_oprc": "open_price",
    "stck_hgpr": "high_price",
    "stck_lwpr": "low_price",
    "stck_clpr": "close_price",
    "acml_vol": "volume",
    "acml_tr_pbmn": "trading_value"
}

numeric_columns = [
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "volume",
    "trading_value"
]

required_columns = ["trade_date", *numeric_columns]

for stock_code in stock_codes:

    # 1. 현재 종목의 API 요청 조건 설정
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": stock_code,
        "FID_INPUT_DATE_1": start_date,
        "FID_INPUT_DATE_2": end_date,
        "FID_PERIOD_DIV_CODE": "D",
        "FID_ORG_ADJ_PRC": "1"
    }

    # 2. API 요청
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )
    response.raise_for_status()
    data = response.json()

    # 3. API 응답 확인
    if data.get("rt_cd") != "0":
        raise RuntimeError(
            f"KIS API error: {data.get('msg1', 'Unknown error')}"
        )

    # 4. DataFrame 생성
    daily_data = data.get("output2", [])
    df = pd.DataFrame(daily_data)

    if df.empty:
        print(f"No data returned for {stock_code}")
        continue

    # 5. 컬럼명 변경
    df = df.rename(columns=column_mapping)

    # 6. 날짜 및 숫자 자료형 변환
    df["trade_date"] = pd.to_datetime(
        df["trade_date"],
        format="%Y%m%d",
        errors="coerce"
    )

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # 7. 분석에 필요한 컬럼만 유지
    df = df[required_columns].copy()

    # 8. 종목 코드 추가
    df["stock_code"] = stock_code

    # 9. 정리된 데이터 보관
    all_stock_dfs.append(df)

    print(f"{stock_code}: {len(df)} rows collected.")


# 모든 종목 데이터 통합
if not all_stock_dfs:
    raise ValueError("수집된 데이터가 없습니다.")

df = pd.concat(all_stock_dfs, ignore_index=True)

df = df.sort_values(
    ["stock_code", "trade_date"]
).reset_index(drop=True)

# 데이터 검증
if df.duplicated(
    subset=["stock_code", "trade_date"]
).any():
    raise ValueError("종목별 거래일 중복이 발견되었습니다.")

if df["trade_date"].isna().any():
    raise ValueError("거래일 변환에 실패한 데이터가 있습니다.")

if df[numeric_columns].isna().any().any():
    raise ValueError("숫자 컬럼에 변환 실패 데이터가 있습니다.")

# 수집 결과 출력
print("\nRows by stock:")
print(df.groupby("stock_code").size())

print("\nTotal rows:", len(df))

print("\nCleaned DataFrame:")
print(df.head())

print("\nData types:")
print(df.dtypes)


# Save cleaned data to SQL Server (이 아래부터 기존 SQL Server 연결 및 저장 코드)
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
