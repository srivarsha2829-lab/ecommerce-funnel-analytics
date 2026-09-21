# Category-Level Analysis

This step combines the uploaded Retailrocket `item_properties_part1.csv`, `item_properties_part2.csv`, and `category_tree.csv` with the cleaned event log.

## Metadata coverage

The two item-property files contain **788,214 category-property records** covering **417,053 unique items**. Keeping the latest observed `categoryid` assignment per item produces metadata for 417,053 items across 1,180 category IDs.

After joining those assignments to the behavioral event log, **90.73% of cleaned events** have a category assignment, covering **1,086 categories** represented in the event data.

Because the dataset anonymizes category labels, findings refer to category IDs rather than human-readable merchandise names.

## Highest-traffic categories

| Category | Views | Cart adds | Transactions | Transaction events / views |
| --- | ---: | ---: | ---: | ---: |
| 1051 | 73,014 | 1,709 | 485 | 0.66% |
| 1483 | 62,785 | 1,520 | 469 | 0.75% |
| 491 | 59,298 | 1,548 | 263 | 0.44% |
| 959 | 50,112 | 1,633 | 532 | 1.06% |
| 342 | 45,288 | 1,278 | 281 | 0.62% |
| 683 | 37,765 | 907 | 211 | 0.56% |
| 1279 | 33,531 | 720 | 123 | 0.37% |
| 5 | 28,952 | 576 | 186 | 0.64% |
| 646 | 27,669 | 484 | 87 | 0.31% |
| 48 | 26,701 | 600 | 146 | 0.55% |

Category **959** combines high traffic with the largest transaction-event count among these ten high-traffic categories.

## High-traffic categories with no transaction events

Using **1,000 views** as an initial stability screen leaves 410 categories. Twelve of them record no transaction events.

Examples include:

| Category | Views | Cart adds | Transactions |
| --- | ---: | ---: | ---: |
| 1007 | 4,545 | 0 | 0 |
| 697 | 3,291 | 0 | 0 |
| 741 | 2,196 | 0 | 0 |
| 561 | 2,179 | 0 | 0 |
| 474 | 1,513 | 0 | 0 |
| 1142 | 1,338 | 0 | 0 |
| 1069 | 1,269 | 0 | 0 |
| 1262 | 1,213 | 0 | 0 |

These categories are useful investigation targets because they receive meaningful traffic without corresponding transaction events. The data does not establish whether this is caused by assortment, availability, user intent, merchandising, tracking, or another factor.

## Strong downstream signals

Among categories with at least 1,000 views and at least 10 transaction events, several show relatively high transaction-event-to-view ratios:

| Category | Views | Cart adds | Transactions | Transaction events / views |
| --- | ---: | ---: | ---: | ---: |
| 57 | 2,229 | 128 | 150 | 6.73% |
| 1037 | 5,189 | 652 | 226 | 4.36% |
| 417 | 1,914 | 205 | 82 | 4.28% |
| 686 | 6,052 | 422 | 236 | 3.90% |
| 972 | 1,975 | 164 | 74 | 3.75% |

These ratios are screening signals based on aggregate event counts. They are not session-matched conversion rates and should not be interpreted causally.

## Category tree

The supplied category tree contains **1,669 category nodes**. Mapping leaf categories upward produces 23 represented top-level category groups in the joined behavioral data.

The largest top-level group by view volume is root category **140**, with 696,264 views, 20,928 cart events, and 7,563 transaction events. Root category **1224** shows 80,679 views and 1,537 transaction events, giving it a comparatively high aggregate transaction-events-per-view signal of about 1.91%.

## Product questions created by this analysis

- Why do categories such as 1007 and 697 receive thousands of views but no recorded cart or transaction activity?
- What behavioral or assortment characteristics distinguish categories 57, 1037, 417, and 686?
- Are weak category results broad across many products or driven by a few high-traffic items?
- Do repeat-day visitors concentrate in particular category branches?
- Are category patterns stable over time?

The next step should combine these category findings with product and visitor behavior before writing final business recommendations.
