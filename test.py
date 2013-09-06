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

    def testReversed(self):
        d = indexed.IndexedOrderedDict()

        d["a"] = "b"
        d["b"] = "a"

        it = d.__reversed__()
        self.assertEqual(next(it), "b")
        self.assertEqual(next(it), "a")

    def testCompability(self):
        d = indexed.IndexedOrderedDict()
        self.assertEqual(len(d.keysview()), 0)
        self.assertEqual(len(d.valuesview()), 0)
        self.assertEqual(len(d.itemsview()), 0)

    def testClear(self):
        d = indexed.IndexedOrderedDict()

        d["foo"] = "bar"
        self.assertEqual(len(d), 1)
        self.assertEqual(len(d.values()), 1)

        d.clear()
        self.assertEqual(len(d), 0)
        self.assertEqual(len(d.values()), 0)

    def testPopitem(self):
        d = indexed.IndexedOrderedDict()
        d["first-key"] = "first"
        d["middle-key"] = "middle"
        d["last-key"] = "last"

        self.assertEqual(d.popitem(), ("last-key", "last"))
        self.assertEqual(d.popitem(False), ("first-key", "first"))

        self.assertEqual(len(d), 1)
        self.assertEqual(d["middle-key"], "middle")

    def testMoveToEnd(self):
        d = indexed.IndexedOrderedDict()
        d["first-key"] = "first"
        d["middle-key"] = "middle"
        d["last-key"] = "last"

        d.move_to_end("middle-key")
        self.assertEqual(d.keys()[2], "middle-key")
        self.assertEqual(d.values()[2], "middle")
        self.assertEqual(d.keys()[1], "last-key")

        d.move_to_end("last-key", False)
        self.assertEqual(d.keys()[0], "last-key")
        self.assertEqual(d.values()[0], "last")

        self.assertEqual(len(d), 3)

    def testPop(self):
        d = indexed.IndexedOrderedDict()
        d["foo"] = "bar"

        self.assertTrue("foo" in d)
        self.assertEqual(d.pop("foo"), "bar")
        self.assertFalse("foo" in d)

        self.assertEqual(d.pop("hello", "default"), "default")

    def testSetDefault(self):
        d = indexed.IndexedOrderedDict()
        d["a"] = "set"

        self.assertEqual(d.setdefault("a", "not-set"), "set")
        self.assertEqual(d.setdefault("b", "not-set"), "not-set")

        self.assertEqual(d.setdefault("b", "still-not-set"), "not-set")

    def testRepr(self):
        d = indexed.IndexedOrderedDict()
        d["key"] = "value"
        d["recursive"] = d
        self.assertEqual(d.__repr__(), "IndexedOrderedDict([('key', 'value'), ('recursive', ...)])")

    def testEquality(self):
        a = indexed.IndexedOrderedDict()
        a["foo"] = "bar"
        a["baz"] = "zab"

        b = a.copy()

        self.assertTrue(a == b)
        self.assertFalse(a != b)

        b["zip"] = "zap"

        self.assertFalse(a == b)
        self.assertTrue(a != b)

        std_dict = { "foo": "bar", "baz": "zab" }
        self.assertEqual(std_dict, a)


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
