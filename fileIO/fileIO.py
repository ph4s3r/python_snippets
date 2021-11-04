# File operations:

# opening a text file to read: ('rb' for binary,'w' obviously for writing)

with open('file.txt', 'rt', encoding='ascii', errors='replace') as f:
    pass
    # doSomething()

# 1) doSomething : Read entire file to a variable:

data = f.read()

2) Iterate
over
lines:

for line in f:
# testing if a file exists in a location:

    import os

path = '/Users/beazley/Data/data.csv'

if os.path.exists('somefile'):
    with
open('somefile', 'wt') as f:
f.write('Hello\n')
else:
print('File already exists!')

# Get size of file

os.path.getsize(path)

# List directory

os.listdir(path)

import os

path = '/Users/beazley/Data/data.csv'
# Get the last component of the path
os.path.basename(path)
'data.csv'
# Get the directory name
os.path.dirname(path)
# /Users/beazley/Data#
# Join path components together
os.path.join('tmp', 'data', os.path.basename(path))
'tmp/data/data.csv'
# Split the file extension
os.path.splitext(path)
('~/Data/data', '.csv')

