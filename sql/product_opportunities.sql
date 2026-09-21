-- Product opportunity screening.
-- Rates below compare aggregate event counts and are not session-matched causal conversion rates.

WITH product_metrics AS (
    SELECT
        itemid,
        COUNT(*) FILTER (WHERE event = 'view') AS views,
        COUNT(*) FILTER (WHERE event = 'addtocart') AS cart_adds,
        COUNT(*) FILTER (WHERE event = 'transaction') AS purchases
    FROM events
    GROUP BY itemid
),
eligible AS (
    SELECT
        *,
        cart_adds * 1.0 / NULLIF(views, 0) AS view_to_cart_rate,
        purchases * 1.0 / NULLIF(views, 0) AS view_to_purchase_rate
    FROM product_metrics
    WHERE views >= 100
),
threshold AS (
    SELECT quantile_cont(views, 0.75) AS high_traffic_cutoff
    FROM eligible
)
SELECT e.*
FROM eligible e
CROSS JOIN threshold t
WHERE e.views >= t.high_traffic_cutoff
ORDER BY e.view_to_purchase_rate ASC, e.views DESC;
