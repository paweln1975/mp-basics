import unittest
import ex_dict_copy


class TestDeepCopy(unittest.TestCase):
    def setUp(self):
        self.testCopy = ex_dict_copy.DictUtils()

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


if __name__ == '__main__':
    unittest.main()
