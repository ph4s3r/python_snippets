"""

Reading csv file with builtin methods from the machine and process it

I`d rather opt for pandas when processing data

"""

import os
import csv
from pathlib import Path

path = Path('C:\dev\stocks.csv')

if os.path.exists(path):
    with open(path) as f:
        d_csv = csv.DictReader(f)  # Will have the headers as keys in all row-dicts
        for row in d_csv:
            print(row)

else:
    print(f"File {path} does not exists")
