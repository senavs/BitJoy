from typing import Sequence

from .bits import Bit
from .circuits import Adder


class Bytes:

    def __init__(self, bits: Sequence[Bit]):
        # TODO: add architecture
        self._bits = list(bits)

        assert len(self._bits) == 8, 'Bytes has only 8 bits'

    @property
    def bits(self):
        return self._bits

    def __iter__(self):
        return iter(self._bits)

    def __add__(self, other):
        # TODO: optimization without reversed method
        cls = type(self)
        if isinstance(other, cls):
            self_bits = reversed(self.bits)
            other_bits = reversed(other.bits)
            result = []
            carry = Bit(0)
            for i, (self_bit, other_bit) in enumerate(zip(self_bits, other_bits)):
                sum_, carry = Adder.full(self_bit, other_bit, carry)
                result.append(sum_)
            return cls(reversed(result))
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __int__(self):
        bits = ''.join(str(bit.value) for bit in self._bits)
        bits = '0b' + bits
        return int(bits, 2)

    def __index__(self):
        return self.__int__()

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}{tuple(bit.value for bit in self._bits)}'
