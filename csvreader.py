"""

This snippet is to read a csv file from the machine and process it

"""

import os
import csv

path = 'C:\dev\stocks.csv'

if os.path.exists(path):
    with open(path) as f:
        d_csv = csv.DictReader(f)  # Will have the headers as keys in all row-dicts
        for row in d_csv:
            print(row)

else:
    print(f"File {path} does not exists")
