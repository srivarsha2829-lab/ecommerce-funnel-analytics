"""Load and prepare Retailrocket behavioral event data."""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "timestamp",
    "visitorid",
    "event",
    "itemid",
    "transactionid",
}

VALID_EVENTS = {"view", "addtocart", "transaction"}


def load_events(path: str | Path) -> pd.DataFrame:
    """Load events.csv and add useful time fields."""
    path = Path(path)
    events = pd.read_csv(path)

    missing = REQUIRED_COLUMNS.difference(events.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    events = events.copy()
    events["event_time"] = pd.to_datetime(
        events["timestamp"], unit="ms", errors="coerce"
    )

    events = events[events["event"].isin(VALID_EVENTS)]
    events = events.dropna(subset=["event_time", "visitorid", "itemid"])
    events = events.drop_duplicates()

    events["date"] = events["event_time"].dt.date
    events["hour"] = events["event_time"].dt.hour
    events["day_of_week"] = events["event_time"].dt.day_name()

    return events.sort_values(["visitorid", "event_time"]).reset_index(drop=True)
