"""Sessionize Retailrocket events and calculate ordered shopping journeys."""

import pandas as pd


def add_sessions(events: pd.DataFrame, inactivity_minutes: int = 30) -> pd.DataFrame:
    """Assign sessions using a configurable inactivity threshold."""
    events = events.sort_values(["visitorid", "event_time"]).copy()
    gap = events.groupby("visitorid")["event_time"].diff()
    new_session = gap.isna() | gap.gt(pd.Timedelta(minutes=inactivity_minutes))
    events["session_number"] = (
        new_session.groupby(events["visitorid"]).cumsum().astype("int32")
    )
    return events


def session_journeys(events: pd.DataFrame) -> pd.DataFrame:
    """Create one row per session and record the first timestamp of each event type."""
    grouped = events.groupby(["visitorid", "session_number"])

    base = grouped.agg(
        session_start=("event_time", "min"),
        session_end=("event_time", "max"),
        event_count=("event", "size"),
    )

    first_stage = (
        events.pivot_table(
            index=["visitorid", "session_number"],
            columns="event",
            values="event_time",
            aggfunc="min",
        )
        .rename(
            columns={
                "view": "view_time",
                "addtocart": "cart_time",
                "transaction": "transaction_time",
            }
        )
    )

    sessions = base.join(first_stage).reset_index()
    for column in ["view_time", "cart_time", "transaction_time"]:
        if column not in sessions:
            sessions[column] = pd.NaT

    sessions["view_then_cart"] = (
        sessions["view_time"].notna()
        & sessions["cart_time"].notna()
        & sessions["cart_time"].ge(sessions["view_time"])
    )
    sessions["view_cart_transaction"] = (
        sessions["view_then_cart"]
        & sessions["transaction_time"].notna()
        & sessions["transaction_time"].ge(sessions["cart_time"])
    )
    return sessions
