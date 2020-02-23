import unittest

from bitjoy.dtypes import Bit, Bytes
from bitjoy.utils import int_to_bytes


class TestOperators(unittest.TestCase):

    def setUp(self) -> None:
        self.zero = Bit(0)
        self.one = Bit(1)

        self.b0 = int_to_bytes(0)
        self.b1 = int_to_bytes(1)
        self.b255 = int_to_bytes(255)
        self.b256 = int_to_bytes(256)

    def test_initialization(self):
        self.assertEqual(self.b0.architecture, 8)
        self.assertEqual(self.b1.architecture, 8)
        self.assertEqual(self.b255.architecture, 8)
        self.assertEqual(self.b256.architecture, 9)

    def test_add(self):
        self.assertEqual(self.b0 + self.b1, int_to_bytes(1))
        self.assertEqual(self.b1 + self.b0, int_to_bytes(1))

        self.assertEqual(self.b0 + self.b255, int_to_bytes(255))
        self.assertEqual(self.b1 + self.b255, int_to_bytes(0))
        self.assertEqual(self.b255 + self.b255, int_to_bytes(254))

    def test_int(self):
        self.assertEqual(int(self.b0), 0)
        self.assertEqual(int(self.b1), 1)
        self.assertEqual(int(self.b255), 255)
        self.assertEqual(int(self.b256), 256)


if __name__ == '__main__':
    unittest.main()
