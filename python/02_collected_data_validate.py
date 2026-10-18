
import pandas as pd
import pyodbc

# 1. SQL Server 연결 설정
server = r"DESKTOP-29RVDTS\SQLEXPRESS"
database = "Finance_dataflow"
driver = "{ODBC Driver 17 for SQL Server}"

connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

# 2. SQL Server에서 저장된 데이터 읽기
conn = pyodbc.connect(connection_string, timeout=5)

try:
    query = """
        SELECT
            trade_date,
            stock_code,
            open_price,
            high_price,
            low_price,
            close_price,
            volume,
            trading_value
        FROM dbo.daily_stock_prices
        WHERE stock_code = ?
        ORDER BY trade_date ASC
    """

    df = pd.read_sql_query(query, conn, params=["005930"])

finally:
    conn.close()

print("Data loaded from SQL Server.")
print("Number of records:", len(df))

# 3. 결측값 확인
missing_count = df.isnull().sum().sum()
print("\nMissing values:", missing_count)

# 4. 중복 거래일 확인
duplicate_count = df["trade_date"].duplicated().sum()
print("Duplicate trading dates:", duplicate_count)

# 5. 비정상 종가 확인
invalid_close = (df["close_price"] <= 0).sum()
print("Invalid closing prices:", invalid_close)

# 6. 음수 거래량 확인
invalid_volume = (df["volume"] < 0).sum()
print("Invalid trading volumes:", invalid_volume)

# 7. 고가가 저가보다 낮은 행 확인
invalid_high_low = (
    df["high_price"] < df["low_price"]
).sum()
print("Invalid high-low relationships:", invalid_high_low)
