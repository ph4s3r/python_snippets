"""

blockdata will store transactions at first, but basically anything that can be stringified

t1 = 'Peet sends 6 DC Anita'
t2 = 'Zoli sends 1 DC Anne'
t3 = 'Kari sends 3 DC Zoe'
t4 = 'Sanyi sends 8 DC George'
t5 = 'Doge sends 12 DC Anita'
t6 = 'Anita sends 17 DC Carl'

"""

import hashlib


# usage: hashlib.sha256(message.encode()).hexdigest()


class DogeBlock:
    """
    One block will be storing 2 transactions

    """

    def __init__(self, blockdata, prevhash):
        self.blockdata = blockdata
        self.prevhash = prevhash

        self.block_hash = hashlib.sha256(self.blockdata.encode()).hexdigest()


if __name__ == '__main__':
    t1 = 'Peet sends 6 DC Anita'
    t2 = 'Zoli sends 1 DC Anne'
    t3 = 'Kari sends 3 DC Zoe'
    t4 = 'Sanyi sends 8 DC George'
    t5 = 'Doge sends 12 DC Anita'
    t6 = 'Anita sends 17 DC Carl'

    genesisblock = DogeBlock(t1 + " & " + t2, "N/A")

    # creation of the second block:
    secondblock = DogeBlock(t3 + " & " + t4, genesisblock.block_hash)

    print(genesisblock.blockdata)
    print(genesisblock.block_hash)
    print(secondblock.blockdata)
    print(secondblock.block_hash)
