import unittest

from bitjoy.dtypes import Bit, ZeroBit, OneBit


class TestBit(unittest.TestCase):

    def setUp(self) -> None:
        self.zero = Bit(0)
        self.one = Bit(1)

    def test_initialization(self):
        self.assertIsInstance(self.zero, Bit)
        self.assertIsInstance(self.zero, ZeroBit)
        self.assertIsInstance(self.one, Bit)
        self.assertIsInstance(self.one, OneBit)

    def test_comparision(self):
        self.assertEqual(self.zero, 0)
        self.assertEqual(self.zero, self.zero)
        self.assertNotEqual(self.zero, 1)
        self.assertNotEqual(self.zero, self.one)

        self.assertEqual(self.one, 1)
        self.assertEqual(self.one, self.one)
        self.assertNotEqual(self.one, 0)
        self.assertNotEqual(self.one, self.zero)

    def test_add(self):
        self.assertEqual(self.zero + self.zero, self.zero)
        self.assertEqual(self.zero + self.one, self.one)
        self.assertEqual(self.one + self.zero, self.one)
        self.assertEqual(self.one + self.one, self.one)

    def test_value(self):
        self.assertEqual(self.zero.value, 0)
        self.assertEqual(self.one.value, 1)


if __name__ == '__main__':
    unittest.main()
