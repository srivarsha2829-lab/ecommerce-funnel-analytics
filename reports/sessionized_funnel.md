# Sessionized Funnel Analysis

This analysis uses the uploaded Retailrocket `events.csv` and a **30-minute inactivity threshold** to separate each visitor's activity into sessions. Exact duplicate source rows were removed before analysis.

## Results

| Metric | Sessions | Rate |
| --- | ---: | ---: |
| Total sessions | 1,761,675 | — |
| Sessions containing a view | 1,755,781 | — |
| View → add-to-cart in chronological order | 35,832 | 2.04% of view sessions |
| View → add-to-cart → transaction in chronological order | 10,411 | 0.59% of view sessions |
| Ordered cart → transaction progression | — | 29.06% |

There were **14,297 sessions containing a transaction event**. Of those, **10,411** contained the complete ordered view → cart → transaction pattern under this session definition.

## Journey timing

For the 10,411 sessions with the complete ordered journey:

- Median first view → first cart: **2.99 minutes**
- Median first cart → first transaction: **4.34 minutes**
- Median first view → first transaction: **10.48 minutes**

## Engagement pattern

**1,378,963 sessions (78.28%) contained only one event.** This helps explain why the top of the funnel is much larger than downstream behavioral stages and suggests that a large share of observed visits are shallow interactions.

## Interpretation

The 30-minute threshold is an analytical assumption, not a session identifier supplied by Retailrocket. Results can change if a different inactivity window is used.

The ordered funnel is stricter than the earlier visitor-stage view because it requires the relevant event types to occur within the same derived session and in chronological order. It is still not a causal measure: the dataset does not expose every contextual factor that may influence purchase behavior.

## Product questions to investigate next

1. Which high-traffic items have unusually weak cart and transaction activity?
2. Which products convert efficiently despite lower traffic?
3. Are funnel rates stable over time or concentrated in particular dates?
4. How much downstream activity comes from repeat visitors?
5. Do category-level patterns explain part of the product-level variation?
