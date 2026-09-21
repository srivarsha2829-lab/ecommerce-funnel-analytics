"""Enrich Retailrocket events with product category metadata."""

from pathlib import Path
import pandas as pd


def load_latest_item_categories(part1: str | Path, part2: str | Path) -> pd.DataFrame:
    """Read categoryid property rows and keep the latest category assignment per item."""
    pieces = []
    for path in [part1, part2]:
        for chunk in pd.read_csv(path, chunksize=1_000_000):
            category_rows = chunk[chunk["property"].eq("categoryid")].copy()
            pieces.append(category_rows)

    categories = pd.concat(pieces, ignore_index=True)
    categories["categoryid"] = pd.to_numeric(categories["value"], errors="coerce")
    categories = categories.dropna(subset=["categoryid"])
    categories["categoryid"] = categories["categoryid"].astype("int64")
    return (
        categories.sort_values("timestamp")
        .drop_duplicates("itemid", keep="last")
        [["itemid", "categoryid"]]
    )


def category_performance(events: pd.DataFrame, item_categories: pd.DataFrame) -> pd.DataFrame:
    """Aggregate behavioral event counts by latest observed product category."""
    enriched = events.merge(item_categories, on="itemid", how="left")
    known = enriched.dropna(subset=["categoryid"]).copy()

    result = known.groupby("categoryid").agg(
        views=("event", lambda s: s.eq("view").sum()),
        cart_adds=("event", lambda s: s.eq("addtocart").sum()),
        transactions=("event", lambda s: s.eq("transaction").sum()),
        visitors=("visitorid", "nunique"),
        items=("itemid", "nunique"),
    )
    result["cart_events_per_view"] = result["cart_adds"] / result["views"].replace(0, pd.NA)
    result["transaction_events_per_view"] = result["transactions"] / result["views"].replace(0, pd.NA)
    return result.reset_index()
