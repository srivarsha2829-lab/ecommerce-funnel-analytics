# E-Commerce Funnel Analytics

An exploratory product analytics project focused on understanding how customers move through an e-commerce purchase funnel, where they drop off, and how conversion behavior varies across the journey.

## Questions I want to explore

- How many users progress from product view to cart to purchase?
- Where is the largest funnel drop-off?
- How does conversion change across products and time periods?
- Are there meaningful differences between new and returning users?
- Which behavioral patterns could point to opportunities for improving conversion?

## Planned workflow

1. Explore and clean the event data.
2. Define the product funnel and core metrics.
3. Reproduce key analyses in SQL.
4. Investigate conversion and drop-off patterns in Python.
5. Add cohort and behavioral views where the data supports them.
6. Build a small interactive dashboard for the most useful findings.
7. Document observations, assumptions, and limitations.

## Tools

Python, Pandas, SQL, DuckDB, Jupyter, Matplotlib, and Streamlit.

## Repository structure

- `data/` — dataset notes and local-data instructions
- `notebooks/` — exploratory analysis
- `sql/` — funnel and product analytics queries
- `src/` — reusable analysis code
- `dashboard/` — Streamlit dashboard
- `tests/` — lightweight checks for reusable logic

## Data

The project will use a public e-commerce behavioral dataset. Raw data will not be committed when it is unnecessarily large; the source, download steps, and relevant fields will be documented in `data/README.md`.

## Status

Initial setup. Analysis will be added incrementally as the dataset is explored.
