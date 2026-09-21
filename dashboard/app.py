"""Interactive product funnel explorer."""

from pathlib import Path

import pandas as pd
import streamlit as st

from src.data_loader import load_events
from src.funnel_metrics import event_summary, product_performance, visitor_funnel


DATA_PATH = Path("data/raw/events.csv")

st.set_page_config(page_title="E-Commerce Funnel Analytics", layout="wide")
st.title("E-Commerce Funnel Analytics")
st.caption("Retailrocket behavioral events: views, cart additions, and transactions")

if not DATA_PATH.exists():
    st.info(
        "Place Retailrocket events.csv in data/raw/events.csv to run the dashboard locally."
    )
    st.stop()

@st.cache_data
def get_events() -> pd.DataFrame:
    return load_events(DATA_PATH)

events = get_events()
min_date = events["event_time"].min().date()
max_date = events["event_time"].max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = events[
        (events["event_time"].dt.date >= start_date)
        & (events["event_time"].dt.date <= end_date)
    ]
else:
    filtered = events

summary = event_summary(filtered)
funnel = visitor_funnel(filtered)
products = product_performance(filtered)

c1, c2, c3 = st.columns(3)
c1.metric("Visitors", f"{filtered['visitorid'].nunique():,}")
c2.metric("Items", f"{filtered['itemid'].nunique():,}")
c3.metric("Events", f"{len(filtered):,}")

st.subheader("Visitor funnel")
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

st.subheader("Event mix")
st.dataframe(
    summary.style.format({"event_share": "{:.2%}"}),
    use_container_width=True,
)

st.subheader("Daily behavior")
daily = (
    filtered.set_index("event_time")
    .groupby([pd.Grouper(freq="D"), "event"])
    .size()
    .unstack(fill_value=0)
    .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
)
st.line_chart(daily)

st.subheader("Product performance")
min_views = st.number_input("Minimum product views", min_value=1, value=20, step=10)
product_view = products[products["views"] >= min_views].sort_values(
    ["purchases", "views"], ascending=False
)
st.dataframe(
    product_view.head(100).style.format(
        {
            "view_to_cart_rate": "{:.2%}",
            "view_to_purchase_rate": "{:.2%}",
        }
    ),
    use_container_width=True,
)
