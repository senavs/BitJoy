from typing import Tuple

from dtypes import Bit


class ArithmeticOperator:

    @staticmethod
    def add_(bit1: Bit, bit2: Bit) -> Tuple[Bit, Bit]:
        """Addition arithmetic operator

        :param bit1: first Bit
            :type: Bit
        :param bit2: second Bit
            :type: Bit

        :return: sum bit and carry bit
            :type: tuple
            :example: (Bit(0), Bit(1))
        """

        sum_ = bit1.VALUE + bit2.VALUE
        if sum_ == 2:
            return Bit(0), Bit(1)
        elif sum_ == 1:
            return Bit(1), Bit(0)
        else:
            return Bit(0), Bit(0)

    @staticmethod
    def sub_(bit1: Bit, bit2: Bit) -> Tuple[Bit, Bit]:
        """Subtraction arithmetic operator

        :param bit1: first Bit
            :type: Bit
        :param bit2: second Bit
            :type: Bit

        :return: difference bit and borrow bit
            :type: tuple
            :example: (Bit(0), Bit(1))
        """

        if bit1 == 0 and bit2 == 1:
            return Bit(1), Bit(1)
        elif bit1 == 1 and bit2 == 0:
            return Bit(1), Bit(0)
        else:
            return Bit(0), Bit(0)

    @staticmethod
    def mul_(bit1: Bit, bit2: Bit) -> Bit:
        """Subtraction arithmetic operator

        :param bit1: first Bit
            :type: Bit
        :param bit2: second Bit
            :type: Bit

        :return: result bit
            :type: Bit
            :example: Bit(1)
        """

        sum_ = bit1.VALUE + bit2.VALUE
        if sum_ == 0:
            return Bit(0)
        else:
            return Bit(1)
