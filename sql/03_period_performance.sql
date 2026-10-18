
WITH price_summary AS (
    SELECT
        trade_date,
        close_price,

        FIRST_VALUE(close_price) OVER (
            ORDER BY trade_date ASC
        ) AS first_close,

        ROW_NUMBER() OVER (
            ORDER BY trade_date DESC
        ) AS latest_rank

    FROM dbo.daily_stock_prices
    WHERE stock_code = '005930'
)
SELECT
    MIN(trade_date) AS first_trade_date,
    MAX(trade_date) AS latest_trade_date,

    MAX(
        CASE
            WHEN latest_rank = 1 THEN close_price
        END
    ) AS latest_close,

    MAX(first_close) AS first_close,

    ROUND(
        (
            MAX(
                CASE
                    WHEN latest_rank = 1 THEN close_price
                END
            ) - MAX(first_close)
        ) * 100.0
        / NULLIF(MAX(first_close), 0),
        2
    ) AS period_return_pct

FROM price_summary;
