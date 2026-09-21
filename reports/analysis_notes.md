# Analysis Notes

This file is intentionally separated into **questions, observations, and interpretation**.

No numerical findings are written here until they have been produced from the downloaded source data. This avoids presenting assumed results as if they came from the dataset.

## Questions

### Funnel
- How many unique visitors generate a view, cart-add, and transaction event?
- At which observed event stage does the largest drop occur?
- How should event-level ratios differ from visitor-level ratios?

### Product performance
- Which items attract high view volume but relatively few cart or transaction events?
- Which items have strong downstream activity but limited traffic?
- Do high-volume products dominate transactions?

### Time
- How do views, cart additions, transactions, and active visitors change by day?
- Are there unusual spikes or drops that warrant investigation?
- Does the mix of behavioral events change over the observation period?

### User behavior
- How concentrated is activity among repeat visitors?
- How many visitors appear at more than one event type?
- What does the anonymized event log allow us to say—and what can it not establish?

## Interpretation guardrails

A `view`, `addtocart`, and `transaction` event in the raw log does not by itself prove a strict session-level sequence. The initial funnel therefore describes **observed behavioral stages**. A later analysis can add sessionization and ordered journey logic before making stronger claims about step-to-step user journeys.

Likewise, transaction counts are behavioral events, not revenue, because this dataset does not expose ordinary product names or monetary transaction values in the main event log.
