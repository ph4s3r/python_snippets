import pandas as pd
from pathlib import Path

p = Path("C:/dev/au20.csv")
chunksize = 10
print(p)

with pd.read_csv(p, chunksize=chunksize) as reader:
    for chunk in reader:
        print(chunk)
        break
