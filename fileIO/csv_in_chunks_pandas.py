import pandas as pd

filename = '/home/ubuntu/data.csv'
chunksize = 10000

for chunk in pd.read_csv(filename, chunksize=chunksize):
    # process chunk
    print(chunk)
