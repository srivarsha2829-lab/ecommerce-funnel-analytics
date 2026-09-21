"""Run the first reproducible exploratory analysis on Retailrocket events.csv.

Usage:
    python -m src.analysis
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.data_loader import load_events
from src.funnel_metrics import event_summary, product_performance, visitor_funnel


RAW_PATH = Path("data/raw/events.csv")
OUTPUT_DIR = Path("data/processed")
FIGURE_DIR = Path("reports/figures")


def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            "events.csv was not found. Download the Retailrocket dataset and place "
            "events.csv in data/raw/events.csv."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    events = load_events(RAW_PATH)

    summary = event_summary(events)
    funnel = visitor_funnel(events)
    products = product_performance(events)

    daily = (
        events.assign(date=pd.to_datetime(events["event_time"]).dt.date)
        .groupby(["date", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
        .reset_index()
    )

    summary.to_csv(OUTPUT_DIR / "event_summary.csv", index=False)
    funnel.to_csv(OUTPUT_DIR / "visitor_funnel.csv", index=False)
    products.to_csv(OUTPUT_DIR / "product_performance.csv", index=False)
    daily.to_csv(OUTPUT_DIR / "daily_events.csv", index=False)

    print("\nDataset overview")
    print("----------------")
    print(f"Rows after cleaning: {len(events):,}")
    print(f"Unique visitors: {events['visitorid'].nunique():,}")
    print(f"Unique items: {events['itemid'].nunique():,}")
    print(f"Start: {events['event_time'].min()}")
    print(f"End:   {events['event_time'].max()}")

    print("\nEvent summary")
    print(summary.to_string(index=False))

    print("\nVisitor funnel")
    print(funnel.to_string(index=False))

    ax = funnel.plot.bar(
        x="stage",
        y="visitors",
        legend=False,
        title="Unique visitors by observed event stage",
    )
    ax.set_xlabel("")
    ax.set_ylabel("Unique visitors")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "visitor_funnel.png", dpi=150)
    plt.close()

    daily_plot = daily.set_index("date")
    ax = daily_plot.plot(title="Daily e-commerce events")
    ax.set_xlabel("Date")
    ax.set_ylabel("Events")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "daily_events.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
