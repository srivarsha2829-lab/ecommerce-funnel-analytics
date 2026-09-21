# Product Findings and Recommended Follow-Ups

This document turns the verified analysis into product questions and next actions. The recommendations are investigation priorities, not causal claims.

## 1. Investigate high-traffic products with no transactions

Among the 996 products in the high-traffic screen, 279 recorded no transaction events while receiving 107,352 views. Products such as 187946 (3,410 views) and 5411 (2,325 views) deserve closer inspection.

**Follow-up:** check availability, product-detail quality, pricing, merchandising, cart errors, and tracking for these items. Compare them with similarly trafficked products that do record transactions.

## 2. Examine category branches with traffic but no downstream activity

Twelve categories with at least 1,000 views recorded no transaction events. Category 1007 received 4,545 views with no cart or transaction events, while category 697 received 3,291 views with the same pattern.

**Follow-up:** determine whether the issue is broad across each category or concentrated in a small number of items. Zero cart activity is especially useful for separating pre-cart friction from later checkout behavior.

## 3. Study repeat-day visitors

Repeat-day visitors represent 10.21% of observed visitors but have a 3.50% transaction-visitor rate, compared with 0.53% for one-day visitors.

**Follow-up:** compare the products, categories, and sequences associated with repeat-day visitors. This may identify consideration-heavy journeys worth supporting with better discovery, saved-state, or reminder experiences.

## 4. Focus on the cart-to-transaction stage

The ordered session analysis identifies 35,832 sessions reaching view → cart, but only 10,411 completing view → cart → transaction. The observed progression from ordered cart stage to transaction is 29.06%.

**Follow-up:** if checkout instrumentation becomes available, break this stage into smaller steps such as cart, checkout start, payment, and completion. The current event file cannot identify the reason for abandonment.

## 5. Compare strong and weak categories

Several categories with meaningful traffic show stronger downstream event signals, including 57, 1037, 417, and 686. These should be compared with high-traffic weak categories rather than treated as proof of superior category performance.

**Follow-up:** compare item mix, repeat-visitor share, traffic patterns, and temporal stability across the two groups.

## 6. Treat cohort recurrence as a baseline

Weighted first-seen cohort retention falls from 3.26% in week 1 to 0.95% by week 4.

**Follow-up:** segment cohorts by first-viewed category and first-session depth. This can show whether some entry experiences are associated with greater recurrence.

## Measurement guardrails

- A transaction event is used as the dataset's downstream purchase signal.
- The 30-minute session boundary is an analytical assumption.
- Event-count ratios are not session-matched causal conversion rates.
- Calendar-day and weekly recurrence are descriptive retention measures.
- Category labels are anonymized, so category IDs cannot be assigned real merchandise names.
- Recommendations identify what to investigate next; they do not establish why a pattern occurred.
