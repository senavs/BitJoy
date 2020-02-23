import unittest

from bitjoy.dtypes import Bit, Adder


class TestCircuits(unittest.TestCase):

    def setUp(self) -> None:
        self.zero = Bit(0)
        self.one = Bit(1)
        self.adder = Adder

    def test_half(self):
        self.assertEqual(self.adder.half(self.zero, self.zero), (self.zero, self.zero))
        self.assertEqual(self.adder.half(self.zero, self.one), (self.one, self.zero))
        self.assertEqual(self.adder.half(self.one, self.zero), (self.one, self.zero))
        self.assertEqual(self.adder.half(self.one, self.one), (self.zero, self.one))

    def test_full(self):
        self.assertEqual(self.adder.full(self.zero, self.zero, self.zero), (self.zero, self.zero))
        self.assertEqual(self.adder.full(self.zero, self.zero, self.one), (self.one, self.zero))
        self.assertEqual(self.adder.full(self.zero, self.one, self.zero), (self.one, self.zero))
        self.assertEqual(self.adder.full(self.zero, self.one, self.one), (self.zero, self.one))

        self.assertEqual(self.adder.full(self.one, self.zero, self.zero), (self.one, self.zero))
        self.assertEqual(self.adder.full(self.one, self.zero, self.one), (self.zero, self.one))
        self.assertEqual(self.adder.full(self.one, self.one, self.zero), (self.zero, self.one))
        self.assertEqual(self.adder.full(self.one, self.one, self.one), (self.one, self.one))


if __name__ == '__main__':
    unittest.main()
