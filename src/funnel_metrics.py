"""Core funnel metrics for the Retailrocket event log."""

import pandas as pd


FUNNEL_ORDER = ["view", "addtocart", "transaction"]


def event_summary(events: pd.DataFrame) -> pd.DataFrame:
    """Return event counts and share of all behavioral events."""
    summary = (
        events["event"]
        .value_counts()
        .reindex(FUNNEL_ORDER, fill_value=0)
        .rename_axis("event")
        .reset_index(name="events")
    )
    total = summary["events"].sum()
    summary["event_share"] = summary["events"] / total if total else 0.0
    return summary


def visitor_funnel(events: pd.DataFrame) -> pd.DataFrame:
    """Return unique visitors reaching each observed funnel stage."""
    counts = (
        events.groupby("event")["visitorid"]
        .nunique()
        .reindex(FUNNEL_ORDER, fill_value=0)
    )

    rows = []
    previous = None
    first = counts.iloc[0] if len(counts) else 0

    for stage, visitors in counts.items():
        rows.append(
            {
                "stage": stage,
                "visitors": int(visitors),
                "conversion_from_view": visitors / first if first else 0.0,
                "conversion_from_previous": (
                    visitors / previous if previous else 1.0
                ),
            }
        )
        previous = visitors

    return pd.DataFrame(rows)


def product_performance(events: pd.DataFrame) -> pd.DataFrame:
    """Aggregate views, cart adds, purchases and simple product conversion rates."""
    pivot = (
        events.groupby(["itemid", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=FUNNEL_ORDER, fill_value=0)
        .rename(
            columns={
                "view": "views",
                "addtocart": "cart_adds",
                "transaction": "purchases",
            }
        )
        .reset_index()
    )

    pivot["view_to_cart_rate"] = (
        pivot["cart_adds"].div(pivot["views"].where(pivot["views"].ne(0)))
    )
    pivot["view_to_purchase_rate"] = (
        pivot["purchases"].div(pivot["views"].where(pivot["views"].ne(0)))
    )

    return pivot
