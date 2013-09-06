import unittest
import indexed

class IndexedOrderedDictTestCase(unittest.TestCase):
    def testDelItem(self):
        d = indexed.IndexedOrderedDict()
        keys = d.keys()

        d["key-a"] = "a"
        d["key-b"] = "b"
        d["key-c"] = "c"

        del d["key-a"]
        self.assertFalse("key-a" in d)
        self.assertEqual(keys.index("key-b"), 0)
        self.assertEqual(keys.index("key-c"), 1)

    def testIter(self):
        d = indexed.IndexedOrderedDict()

        d[8] = "8"
        d[5] = "5"
        d[9] = "9"

        it = d.__iter__()
        self.assertEqual(next(it), 8)
        self.assertEqual(next(it), 5)
        self.assertEqual(next(it), 9)


class IndexedViewTestCase(unittest.TestCase):
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

        self.assertEqual(keys.index("key-two"), 2)

    def testValuesView(self):
        values = self.d.values()
        self.assertEqual(len(values), 6)
        self.assertEqual(values[1], "one")
        self.assertEqual(values[3], "three")

    def testItemsView(self):
        items = self.d.items()
        self.assertEqual(len(items), 6)
        self.assertEqual(items[4], ("key-four", "four"))
        self.assertEqual(items[5], ("key-five", "five"))


if __name__ == "__main__":
    unittest.main()
