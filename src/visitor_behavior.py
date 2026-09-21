"""Compare one-day and repeat-day visitor behavior."""

import pandas as pd


def visitor_segments(events: pd.DataFrame) -> pd.DataFrame:
    frame = events.copy()
    frame["date"] = frame["event_time"].dt.floor("D")

    base = frame.groupby("visitorid").agg(
        events=("event", "size"),
        active_days=("date", "nunique"),
    )
    event_counts = (
        frame.groupby(["visitorid", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
    )
    visitors = base.join(event_counts)
    visitors["visitor_type"] = visitors["active_days"].gt(1).map(
        {False: "one_day", True: "repeat_day"}
    )
    return visitors


def segment_summary(visitors: pd.DataFrame) -> pd.DataFrame:
    result = visitors.groupby("visitor_type").agg(
        visitors=("events", "size"),
        avg_events=("events", "mean"),
        cart_visitors=("addtocart", lambda s: s.gt(0).sum()),
        purchase_visitors=("transaction", lambda s: s.gt(0).sum()),
    )
    result["cart_visitor_rate"] = result["cart_visitors"] / result["visitors"]
    result["purchase_visitor_rate"] = result["purchase_visitors"] / result["visitors"]
    return result.reset_index()
