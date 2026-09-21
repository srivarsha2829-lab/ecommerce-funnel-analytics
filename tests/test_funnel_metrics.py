import pandas as pd

from src.funnel_metrics import event_summary, product_performance, visitor_funnel


def sample_events():
    return pd.DataFrame(
        {
            "visitorid": [1, 1, 1, 2, 2, 3],
            "event": [
                "view",
                "addtocart",
                "transaction",
                "view",
                "addtocart",
                "view",
            ],
            "itemid": [10, 10, 10, 20, 20, 30],
        }
    )


def test_event_summary_counts():
    summary = event_summary(sample_events()).set_index("event")
    assert summary.loc["view", "events"] == 3
    assert summary.loc["addtocart", "events"] == 2
    assert summary.loc["transaction", "events"] == 1


def test_visitor_funnel():
    funnel = visitor_funnel(sample_events()).set_index("stage")
    assert funnel.loc["view", "visitors"] == 3
    assert funnel.loc["addtocart", "visitors"] == 2
    assert funnel.loc["transaction", "visitors"] == 1


def test_product_performance():
    products = product_performance(sample_events()).set_index("itemid")
    assert products.loc[10, "purchases"] == 1
    assert products.loc[20, "cart_adds"] == 1
