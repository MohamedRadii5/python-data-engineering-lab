import csv 
import json
from pathlib import Path

import pyarrow.csv as pacsv
import pyarrow.parquet as pq

src = Path("data/raw/orders.csv")
out = Path("data/format")
out.mkdir(parents=True, exist_ok=True)

with open(src, newline="") as f:
    rows = list(csv.DictReader(f))
    
print("CSV rows:", len(rows), "first row:", rows[0])  

with open(out / "orders.json", "w") as f:
    json.dump(rows, f)
    
with open(out / "orders.jsonl", "w") as f:    
    for row in rows:
        f.write(json.dumps(row) + "\n")
        
table = pacsv.read_csv(src)
print(table.schema)
pq.write_table(table, out / "orders.parquet")

for p in [src, *sorted(out.iterdir())]:
    print(f"{p.name:16} {p.stat().st_size:>9,} bytes")
    

cols = pq.read_table(out / "orders.parquet", columns=["order_id", "quantity"])
print("Parquet read only",cols.num_columns, "columns, ", cols.num_rows, "rows")