import unittest
from interview.add_one_task import AddOne


class TestAddOne(unittest.TestCase):

    def setUp(self) -> None:
        self.interview = AddOne()

    def test_empty_list(self):
        input_list = []
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, [1], msg="Empty list should return [1]")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            input_list = [-1]
            self.interview.add_one(input_list)

    def test_simple(self):
        input_list = [1, 3, 7]
        exp_list = [1, 3, 8]
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, exp_list, msg="Expected result not matched.")

    def test_with_nine_at_the_end(self):
        input_list = [1, 3, 9]
        exp_list = [1, 4, 0]
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, exp_list, msg="Expected result not matched.")

    def test_with_all_nine(self):
        input_list = [9, 9, 9]
        exp_list = [1, 0, 0, 0]
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, exp_list, msg="Expected result not matched.")

    def test_with_two_nine(self):
        input_list = [4, 9, 9]
        exp_list = [5, 0, 0]
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, exp_list, msg="Expected result not matched.")

    def test_long(self):
        count = 1000000
        input_list = [9 for i in range(1, count)]
        exp_list = [0 for i in range(1, count)]
        exp_list.append(1)
        exp_list.reverse()
        out = self.interview.add_one(input_list)
        self.assertListEqual(out, exp_list, msg="Expected result not matched.")

    def test_list_two_elements_and_leading_zero(self):
        with self.assertRaises(ValueError):
            input_list = [0, 1]
            self.interview.add_one(input_list)
