# E-Commerce Funnel Analytics

An exploratory product analytics project focused on understanding how customers move through an e-commerce purchase funnel, where they drop off, and how conversion behavior varies across the journey.

## Project at a glance

![E-Commerce Funnel Analytics – End-to-End Flow](E-commerce.png)

The project takes raw Retailrocket behavioral events through data cleaning, sessionization, funnel analysis, product-level opportunity analysis, SQL/Python workflows, and an interactive Streamlit dashboard.

## Questions I want to explore

- How many users progress from product view to cart to purchase?
- Where is the largest funnel drop-off?
- How does conversion change across products and time periods?
- Are there meaningful differences between new and returning users?
- Which behavioral patterns could point to opportunities for improving conversion?

## Current findings

Using the Retailrocket event data:

- **2,755,641** clean behavioral events after exact deduplication.
- **1,407,580** unique visitors and **235,061** unique products.
- With a 30-minute inactivity threshold, the analysis identifies **1,761,675** sessions.
- **35,832** sessions contain an ordered view → add-to-cart journey.
- **10,411** sessions contain the complete ordered view → add-to-cart → transaction journey.
- Among 996 high-traffic products in the initial opportunity screen, **279** recorded zero transaction events despite generating **107,352** views.

These figures are analytical signals rather than causal conclusions. Session boundaries are derived rather than supplied by the source data, and product event-count ratios should not be interpreted as causal conversion rates.

## Workflow

1. Load and clean the event data.
2. Parse timestamps and remove exact duplicates.
3. Sessionize visitor activity using a 30-minute inactivity threshold.
4. Analyze observed and ordered funnel behavior.
5. Screen product-level engagement and transaction patterns.
6. Reproduce key analyses in SQL.
7. Explore daily behavioral trends.
8. Surface findings through reports and an interactive dashboard.

## Tools

Python, Pandas, NumPy, SQL, DuckDB, Matplotlib, Streamlit, and Pytest.

## Repository structure

- `data/` — dataset documentation and local-data instructions
- `notebooks/` — exploratory analysis workspace
- `sql/` — funnel, session, trend, and product-opportunity queries
- `src/` — reusable Python analysis code
- `dashboard/` — Streamlit dashboard
- `reports/` — verified findings and analytical notes
- `tests/` — lightweight checks for reusable logic

## Data

The project uses the public **Retailrocket E-Commerce Dataset**, with behavioral events for product views, cart additions, and transactions. Raw source data is kept out of Git because of its size. See `data/README.md` for the source and setup instructions.

## Run locally

```bash
pip install -r requirements.txt
```

Place `events.csv` in `data/raw/events.csv`, then run:

```bash
python -m src.analysis
streamlit run dashboard/app.py
```

## Analysis reports

- `reports/initial_findings.md` — dataset profile and observed-stage funnel
- `reports/sessionized_funnel.md` — ordered session journey analysis
- `reports/product_opportunities.md` — product-level opportunity screening
- `reports/analysis_notes.md` — questions, assumptions, and interpretation guardrails

## Status

Core data preparation, funnel analysis, sessionization, product-opportunity analysis, SQL queries, tests, and the first dashboard implementation are in place. Additional category enrichment and deeper repeat-user analysis can be added as the project develops.
