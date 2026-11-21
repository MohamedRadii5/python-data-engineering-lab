import sys
from importlib.metadata import version 

print("python", sys.version.split()[0])
for pkg in ["pandas", "polars", "pyarrow", "requests", "pytest", "pyspark"]:
    print(f"{pkg:10} {version(pkg)}")
    