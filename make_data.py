import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

CITIES = ["Lahora", "Austin", "Berlin", "Nairobi", "lima"]
PRODUCTS = ["P01", "P02", "P03","P04"]
PRICES = {"P01":49.0, "P02":19.5, "P03":189.0, "P04":59.9}

def make_rows(n, seed=42):
    rng = random.Random(seed)
    start = date(2026, 1, 1)
    for i in range(1, n + 1):
        pid = rng.choice(PRODUCTS)
        yield {
            "order_id": 1000 + i,
            "order_date": str(start + timedelta(days=rng.randrange(90))),
            "city": rng.choice(CITIES),
            "product_id": pid,
            "quantity": rng.randint(1, 5),
            "unit_price": PRICES[pid],
        }

def add_mess(rows, seed=7):
    rng = random.Random(seed)
    for row in rows:
        roll = rng.random()
        if roll < 0.02:
            row["quantity"] = ""
        elif roll < 0.04:
            row["city"] = " " + row["city"].lower() + " "
        elif roll < 0.05:
            row["quantity"] = -1
        yield row
        if rng.random() < 0.02:
            yield dict(row)



if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "data/raw/orders.csv")
    fields = ["order_id", "order_date", "city", "product_id", "quantity", "unit_price"]
    count = 0
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in add_mess(make_rows(n)):
            writer.writerow(row)
            count += 1 
    print(f"wrote {count:,} rows to {out}")  
          