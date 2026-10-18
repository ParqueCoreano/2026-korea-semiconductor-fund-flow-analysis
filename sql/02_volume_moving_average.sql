
WITH daily_analysis AS (
    SELECT
        trade_date,
        stock_code,
        close_price,
        volume,

        LAG(volume) OVER (
            PARTITION BY stock_code
            ORDER BY trade_date
        ) AS previous_volume,

        AVG(CAST(close_price AS DECIMAL(18, 2))) OVER (
            PARTITION BY stock_code
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS moving_avg_5d

    FROM dbo.daily_stock_prices
    WHERE stock_code = '005930'
)
SELECT
    trade_date,
    close_price,
    volume,
    previous_volume,

    volume - previous_volume AS volume_change,

    ROUND(
        (volume - previous_volume) * 100.0
        / NULLIF(previous_volume, 0),
        2
    ) AS volume_change_pct,

    ROUND(moving_avg_5d, 2) AS moving_avg_5d

FROM daily_analysis
ORDER BY trade_date ASC;
