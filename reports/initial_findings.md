# Initial Findings

These results were calculated from the Retailrocket `events.csv` source file after removing 460 exact duplicate rows.

## Dataset profile

- Rows in source file: **2,756,101**
- Rows after exact deduplication: **2,755,641**
- Unique visitors: **1,407,580**
- Unique items: **235,061**
- Observation period: **May 3, 2015 to September 18, 2015**

## Behavioral event volume

| Event | Events | Unique visitors |
| --- | ---: | ---: |
| View | 2,664,218 | 1,404,179 |
| Add to cart | 68,966 | 37,722 |
| Transaction | 22,457 | 11,719 |

## Observed visitor-stage funnel

Using unique visitors who generated each event type:

| Stage | Unique visitors | % of view visitors | % of previous observed stage |
| --- | ---: | ---: | ---: |
| View | 1,404,179 | 100.00% | — |
| Add to cart | 37,722 | 2.69% | 2.69% |
| Transaction | 11,719 | 0.83% | 31.07% |

The largest observed reduction is between visitors who generated a view event and visitors who generated an add-to-cart event.

### Important interpretation

This is an **observed-stage funnel**, not yet a strict sequential session funnel. A visitor counted in a downstream event is known to have generated that event somewhere in the dataset, but this table alone does not establish that the same visitor followed a specific view → cart → transaction sequence within one shopping session.

The next journey-analysis phase should sessionize events and enforce event ordering before interpreting these percentages as true step-to-step conversion.

## Product signals

Among items with at least 20 view events, the items with the highest transaction-event counts include:

| Item ID | Views | Cart adds | Transactions | Transactions / views |
| --- | ---: | ---: | ---: | ---: |
| 461686 | 2,538 | 304 | 133 | 5.24% |
| 119736 | 752 | 44 | 97 | 12.90% |
| 213834 | 293 | 17 | 92 | 31.40% |
| 7943 | 1,346 | 97 | 46 | 3.42% |
| 312728 | 947 | 161 | 46 | 4.86% |

These ratios are useful screening metrics, but they should not yet be described as causal product conversion rates because the event counts are not session-matched.

## Next questions

The next analysis will focus on sessionized journeys, time trends, repeat visitors, high-traffic/low-downstream-activity products, and product/category enrichment.
