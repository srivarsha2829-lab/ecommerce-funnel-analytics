"""Weekly first-seen cohort retention analysis."""

import pandas as pd


def weekly_cohorts(events: pd.DataFrame):
    frame = events.copy()
    frame["week"] = (
        frame["event_time"].dt.floor("D")
        - pd.to_timedelta(frame["event_time"].dt.weekday, unit="D")
    )

    first_week = frame.groupby("visitorid")["week"].min().rename("cohort_week")
    visitor_weeks = (
        frame[["visitorid", "week"]]
        .drop_duplicates()
        .join(first_week, on="visitorid")
    )
    visitor_weeks["week_index"] = (
        (visitor_weeks["week"] - visitor_weeks["cohort_week"]).dt.days // 7
    ).astype(int)

    counts = (
        visitor_weeks.groupby(["cohort_week", "week_index"])["visitorid"]
        .nunique()
        .unstack(fill_value=0)
    )
    retention = counts.div(counts[0], axis=0)
    return counts, retention
