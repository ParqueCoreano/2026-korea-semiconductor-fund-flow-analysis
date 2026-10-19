
WITH DailyPrices AS (
    SELECT
        trade_date,
        stock_code,
        close_price,
        LAG(close_price) OVER (
            PARTITION BY stock_code
            ORDER BY trade_date
        ) AS previous_close
    FROM dbo.daily_stock_prices
    WHERE stock_code IN ('005930', '000660')
)
SELECT
    trade_date,
    stock_code,
    close_price,
    previous_close,
    CAST(
        (close_price - previous_close) * 100.0
        / NULLIF(previous_close, 0)
        AS DECIMAL(10, 2)
    ) AS daily_return_pct
FROM DailyPrices
ORDER BY trade_date, stock_code;
