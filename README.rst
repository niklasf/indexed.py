indexed.py: a dictionary that is indexed by insertion order
===========================================================

Introduction
------------

``indexed.IndexedOrderedDict`` is fully compatible with
``collections.OrderedDict`` and can be used as a drop in replacement.
The main difference is that key, value and item views support accessing
elements by their index.

::

    d = indexed.IndexedOrderedDict()
    d["first-key"] = "first-value"
    d["second-key"] = "second-value"
    d["third-key"] = "third-value"

    values = d.values()
    assert values[2] == "third-value"

    assert d.keys().index("second-key") == 1

Performance
-----------

Performance is practically on the same order of magnitude as the built in
``collections.OrderedDict``.

============= =========================== ==============================
              ``collections.OrderedDict`` ``indexed.IndexedOrderedDict``
============= =========================== ==============================
a             b                           c
------------- --------------------------- ------------------------------
d             e                           f
============= =========================== ==============================
