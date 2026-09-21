# Product-Level Opportunity Analysis

This analysis uses the cleaned Retailrocket behavioral event file and screens products using aggregate view, add-to-cart, and transaction-event counts.

## Method

To avoid drawing conclusions from extremely low-volume items, the initial screen requires **at least 100 view events**. This leaves **3,984 products**.

Within that group, the top traffic quartile begins at approximately **216 views** and contains **996 products**. These high-traffic products are useful candidates for investigating missed downstream activity.

Event-count ratios are used as diagnostic signals. They are **not session-matched causal conversion rates**.

## High-traffic products with little downstream activity

Several items attracted substantial attention but recorded no transaction events:

| Item ID | Views | Cart adds | Transactions |
| --- | ---: | ---: | ---: |
| 187946 | 3,410 | 2 | 0 |
| 5411 | 2,325 | 9 | 0 |
| 370653 | 1,854 | 0 | 0 |
| 298009 | 1,642 | 0 | 0 |
| 96924 | 1,633 | 0 | 0 |
| 335975 | 1,428 | 0 | 0 |
| 151444 | 1,230 | 0 | 0 |
| 142466 | 1,135 | 1 | 0 |
| 434782 | 1,069 | 0 | 0 |
| 91755 | 1,024 | 0 | 0 |

Across the **996 high-traffic products**, **279 recorded zero transaction events**. Those 279 products generated **107,352 view events**, making them a useful investigation pool rather than dismissing them as low-exposure products.

This pattern does not establish *why* downstream activity is weak. Potential explanations such as price, availability, merchandising, product quality, traffic intent, or tracking differences require additional evidence.

## Transaction-volume leaders

| Item ID | Views | Cart adds | Transactions | Transactions / views |
| --- | ---: | ---: | ---: | ---: |
| 461686 | 2,538 | 304 | 133 | 5.24% |
| 119736 | 752 | 44 | 97 | 12.90% |
| 213834 | 293 | 17 | 92 | 31.40% |
| 7943 | 1,346 | 97 | 46 | 3.42% |
| 312728 | 947 | 161 | 46 | 4.86% |
| 445351 | 939 | 89 | 45 | 4.79% |
| 48030 | 986 | 95 | 41 | 4.16% |
| 420960 | 795 | 60 | 38 | 4.78% |
| 248455 | 575 | 52 | 38 | 6.61% |
| 17478 | 631 | 72 | 37 | 5.86% |

Item **461686** generated the largest transaction-event count among products with at least 100 views, while item **213834** stands out for unusually high transaction activity relative to its view count.

These patterns are candidates for deeper journey/category analysis; they should not be interpreted as proof that one product page or merchandising treatment caused better conversion.

## Transaction concentration

The top 10 products by transaction-event count account for **2.73%** of all transaction events. The top 50 account for **6.44%**, and the top 100 account for **9.12%**.

This indicates that transaction activity is not concentrated only in a tiny handful of products.

## Product opportunities

The most useful next investigations are:

- **High traffic, weak downstream activity:** examine the 279 high-traffic products with no transactions.
- **Strong downstream behavior:** study items such as 461686, 119736, and 213834 for category, repeat-user, and journey differences.
- **Cart friction:** distinguish products receiving cart activity but relatively little transaction activity from products that rarely reach cart at all.
- **Category context:** join item properties and the category tree before making merchandising recommendations.
- **Time stability:** check whether apparent product strength/weakness persists across weeks or is driven by a short burst of activity.

## Limitation

The current `events.csv` does not expose ordinary product names, prices, or revenue values. Recommendations about pricing, content, inventory, or merchandising would therefore be hypotheses for investigation, not conclusions supported by this file alone.
