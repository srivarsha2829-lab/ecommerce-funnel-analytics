# Cohort and Data-Quality Analysis

## Data quality

The uploaded Retailrocket `events.csv` contains **2,756,101 rows**.

- Exact duplicate rows: **460**
- Rows after exact deduplication: **2,755,641**
- Missing timestamp: **0**
- Missing visitor ID: **0**
- Missing event type: **0**
- Missing item ID: **0**
- Missing transaction ID: **2,733,644**

The transaction-ID null count is expected from the event structure: all **22,457 transaction events** have a transaction ID, while non-transaction events do not.

Only the expected event types—`view`, `addtocart`, and `transaction`—appear in the file.

Observed timestamp coverage is **2015-05-03 03:00:04.384 through 2015-09-18 02:59:47.788**.

## Weekly first-seen cohorts

Visitors are assigned to the Monday-starting calendar week in which they first appear. Retention means that a visitor is observed again in a later calendar week.

Across cohorts that have enough observation time, weighted retention is:

| Later week | Eligible cohort visitors | Returning visitors | Retention |
| --- | ---: | ---: | ---: |
| Week 1 | 1,374,639 | 44,760 | 3.26% |
| Week 2 | 1,303,434 | 20,790 | 1.60% |
| Week 3 | 1,241,105 | 14,422 | 1.16% |
| Week 4 | 1,175,772 | 11,153 | 0.95% |
| Week 5 | 1,110,508 | 9,079 | 0.82% |
| Week 6 | 1,046,217 | 7,663 | 0.73% |
| Week 7 | 979,136 | 6,511 | 0.66% |
| Week 8 | 905,946 | 5,644 | 0.62% |

The denominator changes at each horizon so that recent cohorts are not penalized for weeks that had not yet occurred before the dataset ended.

## Interpretation

The event log shows low cross-week recurrence for first-seen visitors. This is a descriptive retention measure, not proof of customer churn: the dataset covers a limited observation window, visitors are anonymized, and there is no information about acquisition source, customer lifecycle, or whether a visitor had activity outside the captured site/event stream.

This cohort view complements the one-day vs repeat-day analysis by showing how recurrence decays over progressively longer time horizons.
