"""
In fact, since a text file is a line-based file,
you can simply use open function to loop through the data, one line at a time.
open function already returns a generator and does not load the entire file into memory.


"""


filename = 'C:\dism.log'

for line in open(filename):
    print(line)