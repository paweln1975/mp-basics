import unittest
import sys
from sort.bubble import bubble_sort
from sort.selection import selection_sort
from sort.quick_sort import quick_sort


class AbstractSortingTestCase:

    def test_general_case(self):
        input_list = [6, 9, 1, 2, -1]
        result = self.function(input_list)
        expected_output = [-1, 1, 2, 6, 9]
        self.assertListEqual(result, expected_output)

    def test_do_not_change_input(self):
        input_list = [6, 9, 1, 2, -1]
        input_list_c = input_list.copy()
        self.function(input_list)

        self.assertListEqual(input_list, input_list_c)

    def test_empty_input(self):
        input_list = []
        input_list_c = input_list.copy()
        self.function(input_list)

        self.assertListEqual(input_list, input_list_c)

    def test_10k_table(self):
        sys.setrecursionlimit(10000)

        input_list = [x for x in range(5000, 0, -1)]
        expected_output = input_list.copy()
        expected_output.sort()
        result = self.function(input_list)
        self.assertListEqual(result, expected_output)


class TestBubbleSort(AbstractSortingTestCase, unittest.TestCase):

    def function(self, input_list: list) -> list:
        return bubble_sort(input_list)


class TestSelectionSort(AbstractSortingTestCase, unittest.TestCase):

    def function(self, input_list: list) -> list:
        return selection_sort(input_list)


class TestQuickSort(AbstractSortingTestCase, unittest.TestCase):

    def function(self, input_list: list) -> list:
        return quick_sort(input_list)
