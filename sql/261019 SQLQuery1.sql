
SELECT
    stock_code,
    COUNT(*) AS row_count,
    MIN(trade_date) AS first_date,
    MAX(trade_date) AS last_date
FROM dbo.daily_stock_prices
WHERE stock_code IN ('005930', '000660')
GROUP BY stock_code
ORDER BY stock_code;
