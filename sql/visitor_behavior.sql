-- One-day vs repeat-day visitor behavior.

WITH visitor_days AS (
    SELECT
        visitorid,
        COUNT(DISTINCT CAST(to_timestamp(timestamp / 1000.0) AS DATE)) AS active_days,
        MAX(CASE WHEN event = 'addtocart' THEN 1 ELSE 0 END) AS has_cart,
        MAX(CASE WHEN event = 'transaction' THEN 1 ELSE 0 END) AS has_transaction
    FROM events
    GROUP BY visitorid
)
SELECT
    CASE WHEN active_days > 1 THEN 'repeat_day' ELSE 'one_day' END AS visitor_type,
    COUNT(*) AS visitors,
    SUM(has_cart) AS cart_visitors,
    ROUND(100.0 * SUM(has_cart) / COUNT(*), 2) AS cart_visitor_pct,
    SUM(has_transaction) AS transaction_visitors,
    ROUND(100.0 * SUM(has_transaction) / COUNT(*), 2) AS transaction_visitor_pct
FROM visitor_days
GROUP BY visitor_type
ORDER BY visitor_type;
