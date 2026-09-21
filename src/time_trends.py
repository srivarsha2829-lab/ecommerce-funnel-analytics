"""Daily and weekly behavioral trend tables."""

import pandas as pd


def daily_trends(events: pd.DataFrame) -> pd.DataFrame:
    frame = events.copy()
    frame["date"] = frame["event_time"].dt.floor("D")
    trend = (
        frame.groupby(["date", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
    )
    trend["active_visitors"] = frame.groupby("date")["visitorid"].nunique()
    trend["cart_events_per_view"] = trend["addtocart"] / trend["view"]
    trend["transaction_events_per_view"] = trend["transaction"] / trend["view"]
    return trend.reset_index()


def weekly_trends(events: pd.DataFrame) -> pd.DataFrame:
    frame = events.copy()
    frame["week"] = (
        frame["event_time"].dt.floor("D")
        - frame["event_time"].dt.weekday * pd.Timedelta(days=1)
    )
    trend = (
        frame.groupby(["week", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
    )
    trend["cart_events_per_view"] = trend["addtocart"] / trend["view"]
    trend["transaction_events_per_view"] = trend["transaction"] / trend["view"]
    return trend.reset_index()
