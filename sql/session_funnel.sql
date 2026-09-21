-- Sessionized ordered funnel using a 30-minute inactivity threshold.
-- DuckDB syntax. The timestamp column is Unix milliseconds.

WITH ordered_events AS (
    SELECT
        *,
        to_timestamp(timestamp / 1000.0) AS event_time,
        LAG(to_timestamp(timestamp / 1000.0)) OVER (
            PARTITION BY visitorid ORDER BY timestamp
        ) AS previous_event_time
    FROM events
),
session_flags AS (
    SELECT
        *,
        CASE
            WHEN previous_event_time IS NULL
              OR event_time - previous_event_time > INTERVAL '30 minutes'
            THEN 1 ELSE 0
        END AS new_session
    FROM ordered_events
),
sessionized AS (
    SELECT
        *,
        SUM(new_session) OVER (
            PARTITION BY visitorid ORDER BY timestamp
            ROWS UNBOUNDED PRECEDING
        ) AS session_number
    FROM session_flags
),
journeys AS (
    SELECT
        visitorid,
        session_number,
        MIN(event_time) FILTER (WHERE event = 'view') AS view_time,
        MIN(event_time) FILTER (WHERE event = 'addtocart') AS cart_time,
        MIN(event_time) FILTER (WHERE event = 'transaction') AS transaction_time
    FROM sessionized
    GROUP BY visitorid, session_number
)
SELECT
    COUNT(*) AS sessions,
    COUNT(*) FILTER (WHERE view_time IS NOT NULL) AS sessions_with_view,
    COUNT(*) FILTER (
        WHERE view_time IS NOT NULL
          AND cart_time >= view_time
    ) AS view_then_cart_sessions,
    COUNT(*) FILTER (
        WHERE view_time IS NOT NULL
          AND cart_time >= view_time
          AND transaction_time >= cart_time
    ) AS ordered_purchase_sessions
FROM journeys;
