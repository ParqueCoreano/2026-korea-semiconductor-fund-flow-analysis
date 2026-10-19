
SELECT
    stock_code,
    trade_date,
    COUNT(*) AS duplicate_count
FROM dbo.daily_stock_prices
GROUP BY stock_code, trade_date
HAVING COUNT(*) > 1;
