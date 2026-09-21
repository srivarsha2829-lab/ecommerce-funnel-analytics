# Visitor Behavior and Time Trends

This analysis uses the cleaned Retailrocket event file. Visitor groups are descriptive behavioral segments, not demographic customer types.

## One-day vs repeat-day visitors

A **repeat-day visitor** appears on more than one distinct calendar date in the observation window.

| Segment | Visitors | Share | Visitors with cart activity | Cart visitor rate | Visitors with transaction activity | Transaction visitor rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| One-day | 1,263,811 | 89.79% | 25,502 | 2.02% | 6,689 | 0.53% |
| Repeat-day | 143,769 | 10.21% | 12,220 | 8.50% | 5,030 | 3.50% |

Repeat-day visitors represent only **10.21%** of visitors but show substantially more downstream activity. Their observed transaction-visitor rate is about **6.6×** the one-day visitor rate.

This is an association, not evidence that returning on another day causes a purchase. Higher-intent shoppers may simply be more likely both to return and to transact.

## Event depth

- **1,001,591 visitors (71.16%)** generated only one event in the full observation window.
- **405,989 visitors (28.84%)** generated more than one event.
- Only 70 one-event visitors have a transaction event, whereas 11,649 multi-event visitors have at least one transaction event.

Because a single transaction can be the only recorded event for a visitor, event depth should not be interpreted as a formal funnel sequence.

## Daily transaction activity

The highest raw transaction-event days include:

| Date | Views | Cart adds | Transactions |
| --- | ---: | ---: | ---: |
| 2015-06-16 | 23,589 | 799 | 276 |
| 2015-07-28 | 20,986 | 716 | 273 |
| 2015-06-17 | 22,948 | 674 | 269 |
| 2015-07-22 | 21,288 | 770 | 267 |
| 2015-07-27 | 27,622 | 666 | 267 |

These dates are candidates for deeper investigation; high transaction counts alone do not establish an anomaly or its cause.

## Weekly transaction activity

The highest raw transaction-event weeks begin:

| Week starting | Views | Cart adds | Transactions |
| --- | ---: | ---: | ---: |
| 2015-07-20 | 169,782 | 4,253 | 1,357 |
| 2015-07-27 | 139,108 | 3,852 | 1,344 |
| 2015-06-15 | 140,620 | 4,021 | 1,316 |
| 2015-07-06 | 156,587 | 3,936 | 1,302 |
| 2015-07-13 | 147,278 | 3,677 | 1,259 |

Raw weekly volume should be interpreted alongside traffic. The analysis code therefore also calculates cart-events-per-view and transaction-events-per-view for each period.

## Product implications

The repeat-day pattern suggests a useful product question: **what products or categories are disproportionately associated with visitors who return on later days?** Combining this visitor segmentation with category metadata can distinguish broad browsing behavior from stronger repeat consideration.

## Limitations

Calendar-day recurrence is deliberately simple and reproducible. It is not a formal retention cohort definition. The dataset also does not provide acquisition channel, marketing exposure, ordinary product names, or customer demographics, so those factors cannot be inferred from this analysis.
