import unittest
import indexed

class IndexedKeysViewTest(unittest.TestCase):
    def testGetItem(self):
        d = indexed.IndexedOrderedDict()
        d["key-zero"] = "zero"
        d["key-one"] = "one"
        d["key-two"] = "two"
        d["key-three"] = "three"
        d["key-four"] = "four"
        d["key-five"] = "five"

        keys = d.keys()
        self.assertEqual(len(keys), 6)

if __name__ == "__main__":
    unittest.main()
