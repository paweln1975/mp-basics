import unittest
import stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = stack.Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertListEqual([1, 2, 3], self.stack.get_stack())

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        value = self.stack.pop()

        self.assertListEqual([1], self.stack.get_stack())
        self.assertEqual(2, value)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.peek()
        value = self.stack.peek()

        self.assertListEqual([1, 2, 3], self.stack.get_stack())
        self.assertEqual(3, value)

    def test_empty(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertFalse(self.stack.is_empty())

        self.stack.pop()
        self.stack.pop()
        self.stack.pop()

        self.assertTrue(self.stack.is_empty())

    def test_seq(self):
        self.stack.is_empty()
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.pop()
        self.stack.pop()
        self.stack.peek()
        self.stack.pop()

        self.assertFalse(self.stack.is_empty())
