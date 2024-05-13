import unittest
from advanced.gen_fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):

    def setUp(self) -> None:
        self.fib = Fibonacci()

    def test_zero(self):
        param = 0

        with self.assertRaises(ValueError):
            self.fib.get(param)

    def test_one(self):
        param = 1
        exp_value = 0

        value = self.fib.get(param)

        self.assertEqual(value, exp_value, f"Fib({param}) should be {exp_value} but got {value}")

    def test_five(self):
        param = 5
        exp_value = 3

        value = self.fib.get(param)

        self.assertEqual(value, exp_value, f"Fib({param}) should be {exp_value} but got {value}")

    def test_twenty(self):
        param = 20
        exp_value = 4181

        value = self.fib.get(param)

        self.assertEqual(value, exp_value, f"Fib({param}) should be {exp_value} but got {value}")
