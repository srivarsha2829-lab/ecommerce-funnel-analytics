-- Core funnel analysis for Retailrocket events.csv loaded as a table named events.
-- DuckDB can create the table directly from the local CSV:
-- CREATE OR REPLACE TABLE events AS
-- SELECT * FROM read_csv_auto('data/raw/events.csv');

WITH visitor_stage AS (
    SELECT
        event,
        COUNT(DISTINCT visitorid) AS visitors
    FROM events
    WHERE event IN ('view', 'addtocart', 'transaction')
    GROUP BY event
),
ordered AS (
    SELECT
        CASE event
            WHEN 'view' THEN 1
            WHEN 'addtocart' THEN 2
            WHEN 'transaction' THEN 3
        END AS stage_order,
        event AS stage,
        visitors
    FROM visitor_stage
)
SELECT
    stage,
    visitors,
    ROUND(
        100.0 * visitors /
        NULLIF(MAX(CASE WHEN stage = 'view' THEN visitors END) OVER (), 0),
        2
    ) AS pct_of_view_visitors,
    ROUND(
        100.0 * visitors /
        NULLIF(LAG(visitors) OVER (ORDER BY stage_order), 0),
        2
    ) AS pct_of_previous_stage
FROM ordered
ORDER BY stage_order;
