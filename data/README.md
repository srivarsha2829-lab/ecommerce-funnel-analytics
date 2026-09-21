# Data

This project uses the **Retailrocket recommender system dataset**, a public, anonymized behavioral dataset collected from a real e-commerce website.

Dataset page: https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset

## Why this dataset

The event log maps naturally to a product funnel:

- `view` — a visitor views an item
- `addtocart` — a visitor adds an item to the cart
- `transaction` — a visitor completes a purchase

That makes it useful for studying customer journeys, funnel conversion, drop-off, product engagement, repeat behavior, and time-based trends.

## Dataset scale

The published dataset contains roughly 2.76 million behavioral events from about 1.4 million visitors over approximately 4.5 months.

The main files are:

- `events.csv` — visitor behavioral events
- `item_properties_part1.csv` and `item_properties_part2.csv` — item properties over time
- `category_tree.csv` — category hierarchy

For the first phase of this project, the analysis uses **events.csv**. Product/category enrichment can be added later.

## events.csv fields

| Field | Meaning |
| --- | --- |
| `timestamp` | Unix timestamp in milliseconds |
| `visitorid` | anonymized visitor identifier |
| `event` | `view`, `addtocart`, or `transaction` |
| `itemid` | anonymized product identifier |
| `transactionid` | transaction identifier; populated for purchase events |

## Download

1. Open the dataset page linked above.
2. Download and extract the dataset.
3. Place `events.csv` at:

```
data/raw/events.csv
```

Raw data is ignored by Git and should remain local.

## Notes

The source values are anonymized/hashed. This project therefore focuses on behavioral patterns rather than customer demographics or identifiable product names.

The source dataset was originally published for recommender-system research; here it is being explored from a product-analytics perspective.
