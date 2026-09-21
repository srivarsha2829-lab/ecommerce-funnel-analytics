-- Daily event volume for trend and anomaly exploration.

SELECT
    CAST(to_timestamp(timestamp / 1000) AS DATE) AS event_date,
    COUNT(*) FILTER (WHERE event = 'view') AS views,
    COUNT(*) FILTER (WHERE event = 'addtocart') AS cart_adds,
    COUNT(*) FILTER (WHERE event = 'transaction') AS purchases,
    COUNT(DISTINCT visitorid) AS active_visitors
FROM events
GROUP BY event_date
ORDER BY event_date;
