"""Interactive dashboard for Retailrocket product analytics."""

from pathlib import Path
import sys

import pandas as pd
import streamlit as st

# Ensure repository root is importable when Streamlit runs dashboard/app.py directly.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data_loader import load_events
from src.funnel_metrics import event_summary, product_performance, visitor_funnel
from src.visitor_behavior import visitor_segments, segment_summary
from src.time_trends import daily_trends

DATA_PATH = Path("data/raw/events.csv")

st.set_page_config(
    page_title="E-Commerce Funnel Analytics",
    page_icon="📊",
    layout="wide",
)
st.title("E-Commerce Funnel Analytics")
st.caption(
    "Retailrocket behavioral events • funnel health • visitor behavior • product opportunities"
)

if not DATA_PATH.exists():
    st.info("Place Retailrocket events.csv in data/raw/events.csv to run the dashboard.")
    st.stop()


@st.cache_data
def get_events() -> pd.DataFrame:
    return load_events(DATA_PATH)


events = get_events()
min_date = events["event_time"].min().date()
max_date = events["event_time"].max().date()

st.sidebar.header("Filters")
date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)
min_views = st.sidebar.number_input(
    "Minimum product views", min_value=1, value=100, step=25
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = events[
        (events["event_time"].dt.date >= start_date)
        & (events["event_time"].dt.date <= end_date)
    ].copy()
else:
    filtered = events.copy()

if filtered.empty:
    st.warning("No events are available for the selected date range.")
    st.stop()

summary = event_summary(filtered)
funnel = visitor_funnel(filtered)
products = product_performance(filtered)
daily = daily_trends(filtered)

views = int((filtered["event"] == "view").sum())
carts = int((filtered["event"] == "addtocart").sum())
transactions = int((filtered["event"] == "transaction").sum())

k1, k2, k3, k4 = st.columns(4)
k1.metric("Visitors", f"{filtered['visitorid'].nunique():,}")
k2.metric("Products", f"{filtered['itemid'].nunique():,}")
k3.metric("Events", f"{len(filtered):,}")
k4.metric("Transactions", f"{transactions:,}")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Funnel", "Trends", "Visitor behavior", "Product opportunities"]
)

with tab1:
    st.subheader("Observed visitor-stage funnel")
    st.bar_chart(funnel.set_index("stage")["visitors"])
    st.dataframe(
        funnel.style.format(
            {
                "conversion_from_view": "{:.2%}",
                "conversion_from_previous": "{:.2%}",
            }
        ),
        use_container_width=True,
    )
    st.caption(
        "Stages are based on visitors observed generating each event type; "
        "they are not a causal session-level conversion measure."
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("View events", f"{views:,}")
    e2.metric("Cart events", f"{carts:,}")
    e3.metric("Transaction events", f"{transactions:,}")

    st.subheader("Event mix")
    st.dataframe(
        summary.style.format({"event_share": "{:.2%}"}),
        use_container_width=True,
    )

with tab2:
    st.subheader("Daily event volume")
    chart = daily.set_index("date")[["view", "addtocart", "transaction"]]
    st.line_chart(chart)

    st.subheader("Daily downstream activity relative to views")
    rate_chart = daily.set_index("date")[
        ["cart_events_per_view", "transaction_events_per_view"]
    ]
    st.line_chart(rate_chart)

with tab3:
    st.subheader("One-day vs repeat-day visitors")
    segments = segment_summary(visitor_segments(filtered))
    st.dataframe(
        segments.style.format(
            {
                "avg_events": "{:.2f}",
                "cart_visitor_rate": "{:.2%}",
                "purchase_visitor_rate": "{:.2%}",
            }
        ),
        use_container_width=True,
    )
    st.caption(
        "Repeat-day means a visitor appears on more than one calendar date "
        "within the currently selected dashboard period."
    )

with tab4:
    st.subheader("Product performance")
    eligible = products[products["views"] >= min_views].copy()

    if eligible.empty:
        st.info("No products meet the selected minimum-view threshold.")
    else:
        high_traffic_cutoff = eligible["views"].quantile(0.75)
        opportunity = eligible[
            (eligible["views"] >= high_traffic_cutoff)
            & (eligible["purchases"] == 0)
        ].sort_values("views", ascending=False)

        p1, p2 = st.columns(2)
        p1.metric("Products meeting view threshold", f"{len(eligible):,}")
        p2.metric(
            "High-traffic products with no transactions",
            f"{len(opportunity):,}",
        )

        st.markdown("#### High-traffic products with no transaction events")
        st.dataframe(
            opportunity.head(50).style.format(
                {
                    "view_to_cart_rate": "{:.2%}",
                    "view_to_purchase_rate": "{:.2%}",
                }
            ),
            use_container_width=True,
        )

        st.markdown("#### Transaction-volume leaders")
        leaders = eligible.sort_values(
            ["purchases", "views"], ascending=False
        ).head(50)
        st.dataframe(
            leaders.style.format(
                {
                    "view_to_cart_rate": "{:.2%}",
                    "view_to_purchase_rate": "{:.2%}",
                }
            ),
            use_container_width=True,
        )

        st.caption(
            "Product ratios compare aggregate event counts and should be used "
            "as screening signals rather than causal conversion estimates."
        )
