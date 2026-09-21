import pandas as pd

from src.cohort_analysis import weekly_cohorts
from src.data_quality import data_quality_report
from src.session_analysis import add_sessions, session_journeys
from src.time_trends import daily_trends, weekly_trends
from src.visitor_behavior import segment_summary, visitor_segments


def timed_events():
    return pd.DataFrame(
        {
            "visitorid": [1, 1, 1, 2, 2],
            "event": ["view", "addtocart", "transaction", "view", "view"],
            "itemid": [10, 10, 10, 20, 20],
            "event_time": pd.to_datetime(
                [
                    "2026-01-05 10:00",
                    "2026-01-05 10:05",
                    "2026-01-05 10:10",
                    "2026-01-05 09:00",
                    "2026-01-06 09:00",
                ]
            ),
        }
    )


def test_sessionization_and_ordered_journey():
    sessionized = add_sessions(timed_events(), inactivity_minutes=30)
    assert sessionized["session_id"].nunique() == 3
    journeys = session_journeys(sessionized)
    assert journeys["view_cart_transaction"].sum() == 1


def test_repeat_day_segment():
    visitors = visitor_segments(timed_events())
    assert visitors.loc[1, "visitor_type"] == "one_day"
    assert visitors.loc[2, "visitor_type"] == "repeat_day"
    summary = segment_summary(visitors).set_index("visitor_type")
    assert summary.loc["repeat_day", "visitors"] == 1


def test_daily_and_weekly_trends():
    daily = daily_trends(timed_events())
    assert daily["view"].sum() == 3
    weekly = weekly_trends(timed_events())
    assert weekly["transaction"].sum() == 1


def test_weekly_cohort_retention():
    counts, retention = weekly_cohorts(timed_events())
    assert counts.iloc[0, 0] == 2
    assert retention.iloc[0, 0] == 1.0


def test_data_quality_report():
    raw = pd.DataFrame(
        {
            "timestamp": [1, 1],
            "visitorid": [1, 1],
            "event": ["view", "view"],
            "itemid": [10, 10],
            "transactionid": [None, None],
        }
    )
    report = data_quality_report(raw)
    assert report["rows"] == 2
    assert report["exact_duplicates"] == 1
    assert report["unexpected_events"] == []
