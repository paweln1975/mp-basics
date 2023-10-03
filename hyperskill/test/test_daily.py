import unittest
from hyperskill.daily_problems import time_diff
from hyperskill.daily_problems import mystery_function
from hyperskill.daily_problems import print_book_info

class TestDates(unittest.TestCase):

    def test_the_same_time(self):
        h1 = 1
        m1 = 1
        s1 = 1

        h2 = 1
        m2 = 1
        s2 = 1

        diff = time_diff(h2, m2, s2, h1, m1, s1)
        self.assertEqual(diff, 0, msg="Diff for the same time should be 0")

    def test_diff_1_sec(self):
        h1 = 1
        m1 = 1
        s1 = 1

        h2 = 1
        m2 = 1
        s2 = 2

        diff = time_diff(h2, m2, s2, h1, m1, s1)
        self.assertEqual(diff, 1, msg="Diff for case (1 sec) should be 1")

    def test_diff_50_sec(self):
        h1 = 1
        m1 = 2
        s1 = 30

        h2 = 1
        m2 = 3
        s2 = 20

        diff = time_diff(h2, m2, s2, h1, m1, s1)
        self.assertEqual(diff, 50, msg="Diff for case (50 sec) should be 50")

    def test_diff_3661_sec(self):
        h1 = 1
        m1 = 1
        s1 = 1

        h2 = 2
        m2 = 2
        s2 = 2

        diff = time_diff(h2, m2, s2, h1, m1, s1)
        self.assertEqual(diff, 3661, msg="Diff for case (3661 sec) should be 50")


def repeat(times):
    def repeat_helper(f):
        def call_helper(*args):
            for i in range(0, times):
                f(*args)
        return call_helper
    return repeat_helper


class TestMystery(unittest.TestCase):
    @repeat(10)
    def test_mystery_fun(self):
        x = 5

        output = mystery_function(x)
        exp_output = [1, 3]

        self.assertListEqual(output, exp_output, "Lists should have the same values.")


class TestPrintBook(unittest.TestCase):
    auth = "Leo Tolstoy"
    year = 1869

    def test_all(self):
        output = print_book_info("War and Peace", self.auth, self.year)
        exp_output = "\"War and Peace\" was written by Leo Tolstoy in 1869"
        self.assertEqual(output, exp_output, "All data given")

    def test_author(self):
        output = print_book_info("War and Peace", self.auth)
        exp_output = "\"War and Peace\" was written by Leo Tolstoy"
        self.assertEqual(output, exp_output, "Author given")

    def test_year(self):
        output = print_book_info("War and Peace", None, self.year)
        exp_output = "\"War and Peace\" was written in 1869"
        self.assertEqual(output, exp_output, "Year given")

    def test_none(self):
        output = print_book_info("War and Peace")
        exp_output = "\"War and Peace\""
        self.assertEqual(output, exp_output, "Only title given")