from dtypes import Bit, Bytes


def int_to_bytes(int_: int) -> Bytes:
    bin_ = f'{bin(int_)[2:]:0>8}'
    bytes_ = [Bit(int(bit)) for bit in bin_]
    return Bytes(bytes_)
