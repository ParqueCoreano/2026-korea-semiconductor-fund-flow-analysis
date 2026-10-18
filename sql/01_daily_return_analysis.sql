
SELECT
    trade_date,
    stock_code,
    close_price,

    LAG(close_price) OVER (
        PARTITION BY stock_code
        ORDER BY trade_date
    ) AS previous_close,

    close_price - LAG(close_price) OVER (
        PARTITION BY stock_code
        ORDER BY trade_date
    ) AS price_change,

    ROUND(
        (close_price - LAG(close_price) OVER (
            PARTITION BY stock_code
            ORDER BY trade_date
        )) * 100.0
        / NULLIF(
            LAG(close_price) OVER (
                PARTITION BY stock_code
                ORDER BY trade_date
            ),
            0
        ),
        2
    ) AS daily_return_pct

FROM dbo.daily_stock_prices
WHERE stock_code = '005930'
ORDER BY trade_date ASC;
