import unittest
import indexed

class IndexedKeysViewTest(unittest.TestCase):
    def test(self):
        d = indexed.IndexedOrderedDict()
        d["key-zero"] = "zero"
        d["key-one"] = "one"
        d["key-two"] = "two"
        d["key-three"] = "three"
        d["key-four"] = "four"
        d["key-five"] = "five"

        keys = d.keys()
        self.assertEqual(len(keys), 6)
        self.assertEqual(keys[0], "key-zero")
        self.assertEqual(keys[4], "key-four")

if __name__ == "__main__":
    unittest.main()
