import unittest
import indexed

class IndexedTestCase(unittest.TestCase):
    def setUp(self):
        self.d = indexed.IndexedOrderedDict()
        self.d["key-zero"] = "zero"
        self.d["key-one"] = "one"
        self.d["key-two"] = "two"
        self.d["key-three"] = "three"
        self.d["key-four"] = "four"
        self.d["key-five"] = "five"

    def testKeysView(self):
        keys = self.d.keys()
        self.assertEqual(len(keys), 6)
        self.assertEqual(keys[0], "key-zero")
        self.assertEqual(keys[4], "key-four")

    def testValuesView(self):
        values = self.d.values()
        self.assertEqual(len(values), 6)
        self.assertEqual(values[1], "one")
        self.assertEqual(values[3], "three")

if __name__ == "__main__":
    unittest.main()
