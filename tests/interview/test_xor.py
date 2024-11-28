import unittest
from xor_impl import xor, fixed_point


class XORTest(unittest.TestCase):
    def test_both_true(self):
        self.assertFalse(xor(True, True))

    def test_both_false(self):
        self.assertFalse((xor(False, False)))

    def test_first_true_second_false(self):
        self.assertTrue(xor(True, False))

    def test_second_true_first_false(self):
        self.assertTrue(xor(False, True))

    def test_fixed_point(self):
        self.assertTrue(fixed_point(True))
        self.assertTrue(fixed_point(False))
        self.assertTrue(fixed_point(1))
        self.assertTrue(fixed_point(0))
