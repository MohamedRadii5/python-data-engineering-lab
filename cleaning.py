import pandas as pd

REQUIRED = ["order_id", "order_date", "city","product_id", "quantity", "unit_price"]
CITIES = ["Lahora", "Austin","Berlin","Nairobi","Lima"]


def check_columns(df):
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
 
def check_orders(df):
    check_columns(df)
    df = df.copy()
    df["city"] = df["city"].str.strip().str.title()
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["reason"] = ""
    df.loc[df["quantity"].isna(), "reason"] = "missing quantity"
    df.loc[df["quantity"] <= 0, "reason"] = "quantity not positive"
    df.loc[~df["city"].isin(CITIES), "reason"] = "Unknown city"
    df.loc[df.duplicated("order_id"), "reason"] = "duplicate order_id"
    bad = df[df["reason"] != ""]
    good = df[df["reason"] == ""].drop(columns=["reason"])
    good = good.astype({"quantity": "Int64"})
    return good, bad


if __name__ == "__main__":
    raw = pd.read_csv("data/raw/orders.csv")
    good, bad = check_orders(raw)
    print(f"raw {len(raw)}, good {len(good)}, bad {len(bad)}")
    print(bad["reason"].value_counts())
    good.to_parquet("data/orders_clean.parquet", index=False)
    bad.to_csv("data/orders_rejected.csv", index=False)
    assert (good["order_id"].is_unique), "Order_id must be unique"
    assert (good["quantity"] > 0).all(), "quantity must be positive"
    print("All checks passed")