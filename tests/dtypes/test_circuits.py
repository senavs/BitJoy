import unittest

from bitjoy.dtypes import Bit, LogicalOperator


class TestOperators(unittest.TestCase):

    def setUp(self) -> None:
        self.zero = Bit(0)
        self.one = Bit(1)
        self.op = LogicalOperator

    def test_not(self):
        self.assertEqual(self.op.not_(self.zero), self.one)
        self.assertEqual(self.op.not_(self.one), self.zero)

    def test_or(self):
        self.assertEqual(self.op.or_(self.zero, self.zero), self.zero)
        self.assertEqual(self.op.or_(self.zero, self.one), self.one)
        self.assertEqual(self.op.or_(self.one, self.zero), self.one)
        self.assertEqual(self.op.or_(self.one, self.one), self.one)

    def test_and(self):
        self.assertEqual(self.op.and_(self.zero, self.zero), self.zero)
        self.assertEqual(self.op.and_(self.zero, self.one), self.zero)
        self.assertEqual(self.op.and_(self.one, self.zero), self.zero)
        self.assertEqual(self.op.and_(self.one, self.one), self.one)

    def test_nor(self):
        self.assertEqual(self.op.nor_(self.zero, self.zero), self.one)
        self.assertEqual(self.op.nor_(self.zero, self.one), self.zero)
        self.assertEqual(self.op.nor_(self.one, self.zero), self.zero)
        self.assertEqual(self.op.nor_(self.one, self.one), self.zero)

    def test_nand(self):
        self.assertEqual(self.op.nand_(self.zero, self.zero), self.one)
        self.assertEqual(self.op.nand_(self.zero, self.one), self.one)
        self.assertEqual(self.op.nand_(self.one, self.zero), self.one)
        self.assertEqual(self.op.nand_(self.one, self.one), self.zero)

    def test_xor(self):
        self.assertEqual(self.op.xor_(self.zero, self.zero), self.zero)
        self.assertEqual(self.op.xor_(self.zero, self.one), self.one)
        self.assertEqual(self.op.xor_(self.one, self.zero), self.one)
        self.assertEqual(self.op.xor_(self.one, self.one), self.zero)

    def test_xnor(self):
        self.assertEqual(self.op.xnor_(self.zero, self.zero), self.one)
        self.assertEqual(self.op.xnor_(self.zero, self.one), self.zero)
        self.assertEqual(self.op.xnor_(self.one, self.zero), self.zero)
        self.assertEqual(self.op.xnor_(self.one, self.one), self.one)


if __name__ == '__main__':
    unittest.main()
