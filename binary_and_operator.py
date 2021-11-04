
"""
    Based on https://realpython.com/python-bitwise-operators/#binary-number-representations
"""


def binary_and(a: int, b: int) -> str:

    # Taking two integers, converting them to binary, then return the resulting binary string

    # basically reimplementing bin(a&b)

    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]  # remove the leading "0b"

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == '__main__':

    c = f"{0b101010:08b}"
    d = f"{42:08b}"

    # converting bin to int
    int("101010", 2)

    # converting integer to bin/hex/oct

    # print(bin(42))
    # print(hex(42))
    # print(oct(42))
    # 42 == 0b101010 == 0x2a == 0o52

    print(binary_and(42, 36))
