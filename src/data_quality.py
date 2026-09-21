"""Dataset quality checks for the Retailrocket event log."""

import pandas as pd


def data_quality_report(raw: pd.DataFrame) -> dict:
    required = ["timestamp", "visitorid", "event", "itemid", "transactionid"]
    missing_columns = sorted(set(required).difference(raw.columns))
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    return {
        "rows": len(raw),
        "exact_duplicates": int(raw.duplicated().sum()),
        "missing_timestamp": int(raw["timestamp"].isna().sum()),
        "missing_visitorid": int(raw["visitorid"].isna().sum()),
        "missing_event": int(raw["event"].isna().sum()),
        "missing_itemid": int(raw["itemid"].isna().sum()),
        "missing_transactionid": int(raw["transactionid"].isna().sum()),
        "unexpected_events": sorted(
            set(raw["event"].dropna().unique())
            - {"view", "addtocart", "transaction"}
        ),
    }
