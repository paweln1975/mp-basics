import unittest
from strings.grade_search import calc_proportion


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        input_str = "A B"
        output = calc_proportion(input_str, 'A')
        output_ex = 0.5
        self.assertEqual(output_ex, output, "Test simple failed")

    def test_non_A(self):
        input_str = "B B C"
        output = calc_proportion(input_str, 'A')
        output_ex = 0.0
        self.assertEqual(output_ex, output, "Test non A failed")

    def test_normal(self):
        input_str = "F B A A B C A D"
        output = calc_proportion(input_str, 'A')
        output_ex = 0.38
        self.assertEqual(output_ex, output, "Test normal failed")


if __name__ == '__main__':
    unittest.main()
