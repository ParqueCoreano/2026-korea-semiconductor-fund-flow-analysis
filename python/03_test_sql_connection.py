import pyodbc ## Python이 SQL Server와 대화할 수 있도록 연결해 주는 도구

server = r"DESKTOP-29RVDTS\SQLEXPRESS"
database = "Finance_dataflow"
driver = "{ODBC Driver 17 for SQL Server}"

connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

try:
    conn = pyodbc.connect(connection_string, timeout=5)
    print("SQL Server connection successful!")

    cursor = conn.cursor()
    cursor.execute("SELECT DB_NAME()")
    print("Connected database:", cursor.fetchone()[0])

    conn.close()

except pyodbc.Error as e:
    print("Connection failed:")
    print(e)
