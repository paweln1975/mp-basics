import unittest
from ex_dict_copy import DictUtils


class TestDeepCopy(unittest.TestCase):
    def setUp(self):
        self.testCopy = DictUtils()

    def tearDown(self) -> None:
        self.testCopy = None

    def testSimpleCopyList(self):
        d = {"a": [1, 2],
             "b": [3, 4]}
        dc = self.testCopy.my_dict_copy(d)

        dc["a"][0] = 10
        self.assertNotEqual(d["a"][0], dc["a"][0])

    def testSimpleCopyDict(self):
        d = {"a": {"a": 1, "b": 2},
             "b": {"c": 3, "d": 4}}
        dc = self.testCopy.my_dict_copy(d)

        dc["a"]["b"] = 10
        self.assertNotEqual(d["a"]["b"], dc["a"]["b"])

    def testAttributeError(self):
        d = {"a": 1}

        with self.assertRaises(AttributeError):
            self.testCopy.my_dict_copy(d)

        no_d = 1
        with self.assertRaises(AttributeError):
            self.testCopy.my_dict_copy(no_d)


if __name__ == '__main__':
    unittest.main()
