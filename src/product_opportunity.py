"""Identify product-level opportunities from Retailrocket behavioral events."""

import numpy as np
import pandas as pd


def product_opportunities(events: pd.DataFrame, min_views: int = 100):
    """Build stable product-level screening tables.

    Rates are event-count ratios, not session-matched causal conversion rates.
    """
    product = (
        events.groupby(["itemid", "event"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["view", "addtocart", "transaction"], fill_value=0)
        .rename(columns={"view": "views", "addtocart": "cart_adds", "transaction": "purchases"})
    )

    product["view_to_cart_rate"] = product["cart_adds"] / product["views"].replace(0, np.nan)
    product["view_to_purchase_rate"] = product["purchases"] / product["views"].replace(0, np.nan)

    eligible = product[product["views"] >= min_views].copy()
    high_traffic_cutoff = eligible["views"].quantile(0.75)
    high_traffic = eligible[eligible["views"] >= high_traffic_cutoff].copy()

    weak_high_traffic = high_traffic.sort_values(
        ["view_to_purchase_rate", "views"], ascending=[True, False]
    )
    purchase_leaders = eligible.sort_values(
        ["purchases", "views"], ascending=[False, False]
    )
    efficient = eligible[eligible["purchases"] >= 5].sort_values(
        ["view_to_purchase_rate", "purchases"], ascending=[False, False]
    )

    return product, weak_high_traffic, purchase_leaders, efficient
