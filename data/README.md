# Data

This project uses the public, anonymized **Retailrocket E-Commerce Dataset**.

Dataset page: https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset

## Files used

The completed analysis uses all four source files:

- `events.csv` — visitor views, cart additions, and transactions
- `item_properties_part1.csv`
- `item_properties_part2.csv` — time-varying item metadata, including category assignments
- `category_tree.csv` — anonymized category hierarchy

## Local setup

Create `data/raw/` and place the four extracted CSV files there:

```text
data/raw/events.csv
data/raw/item_properties_part1.csv
data/raw/item_properties_part2.csv
data/raw/category_tree.csv
```

Raw data is intentionally ignored by Git because of its size.

## Event fields

| Field | Meaning |
| --- | --- |
| `timestamp` | Unix timestamp in milliseconds |
| `visitorid` | anonymized visitor identifier |
| `event` | `view`, `addtocart`, or `transaction` |
| `itemid` | anonymized product identifier |
| `transactionid` | populated for transaction events |

## How metadata is used

Item properties change over time. For the category-level screening in this project, the latest observed `categoryid` assignment for each item is used. The category tree is then used to trace category IDs to their top-level anonymized branch.

Because product and category labels are anonymized, the analysis does not infer real merchandise names or customer demographics.

## Scope and interpretation

The dataset contains roughly 2.76 million behavioral events from about 1.4 million visitors over approximately 4.5 months. Sessions are not supplied by the source and are inferred in this project using a 30-minute inactivity threshold. Event-count ratios and recurrence measures are descriptive analytical signals rather than causal effects.
