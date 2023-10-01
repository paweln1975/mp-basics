import unittest
from hyperskill.daily_problems import time_diff


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
