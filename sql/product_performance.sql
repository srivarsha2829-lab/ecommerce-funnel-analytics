-- Product-level behavioral performance.
-- Requires an events table created from data/raw/events.csv.

SELECT
    itemid,
    COUNT(*) FILTER (WHERE event = 'view') AS views,
    COUNT(*) FILTER (WHERE event = 'addtocart') AS cart_adds,
    COUNT(*) FILTER (WHERE event = 'transaction') AS purchases,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE event = 'addtocart')
        / NULLIF(COUNT(*) FILTER (WHERE event = 'view'), 0),
        2
    ) AS view_to_cart_pct,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE event = 'transaction')
        / NULLIF(COUNT(*) FILTER (WHERE event = 'view'), 0),
        2
    ) AS view_to_purchase_pct
FROM events
GROUP BY itemid
HAVING COUNT(*) FILTER (WHERE event = 'view') >= 20
ORDER BY purchases DESC, views DESC;
