
WITH RankedPrices AS (
    SELECT
        stock_code,
        trade_date,
        close_price,
        ROW_NUMBER() OVER (
            PARTITION BY stock_code
            ORDER BY trade_date ASC
        ) AS first_rank,
        ROW_NUMBER() OVER (
            PARTITION BY stock_code
            ORDER BY trade_date DESC
        ) AS last_rank
    FROM dbo.daily_stock_prices
    WHERE stock_code IN ('005930', '000660')
      AND trade_date >= '2026-07-01'
),
PeriodPrices AS (
    SELECT
        stock_code,
        MAX(CASE WHEN first_rank = 1
                 THEN trade_date END) AS first_date,
        MAX(CASE WHEN first_rank = 1
                 THEN close_price END) AS first_close,
        MAX(CASE WHEN last_rank = 1
                 THEN trade_date END) AS last_date,
        MAX(CASE WHEN last_rank = 1
                 THEN close_price END) AS last_close
    FROM RankedPrices
    GROUP BY stock_code
)
SELECT
    stock_code,
    first_date,
    first_close,
    last_date,
    last_close,
    CAST(
        (last_close - first_close) * 100.0
        / NULLIF(first_close, 0)
        AS DECIMAL(10, 2)
    ) AS period_return_pct
FROM PeriodPrices
ORDER BY stock_code;
