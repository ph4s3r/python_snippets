filename = '/home/ubuntu/data.csv'

def read_chunk():
    return filename.read(1024)

for piece in iter(read_chunk, ''):
    print(piece)

### Using yield

filename = '/home/ubuntu/data.csv'


def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open(filename) as f:
    for piece in read_in_chunks(f):
        #process data
        print(piece)