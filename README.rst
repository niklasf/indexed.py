indexed.IndexedOrderedDict: a dictionary that is indexed by insertion order
===========================================================================

.. image:: https://travis-ci.org/niklasf/indexed.py.png?branch=master
    :target: https://travis-ci.org/niklasf/indexed.py
    :alt: build

.. image:: https://badge.fury.io/py/indexed.svg
    :target: https://pypi.python.org/pypi/indexed
    :alt: pypi package

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

Features
--------

* Access keys, values and items by index, e.g. ``d.keys()[5]``.

* Find the index of a key, e.g. ``d.keys().index("key")``.

Excluding those additions the API is the same as the API of
``collections.OrderedDict()``. Including:

* Initializing, setting, getting and deleting items

* Iterating forwards and in reverse

* ``d.clear()``

* ``d.popitem(last=True)``

* ``d.move_to_end(key, last=True)``

* ``d.keys()``, ``d.values()``, ``d.items()``

* ``d.pop(key[, default])``

* ``d.setdefault(key, default=None)``

* String representation

* Pickling

* Copying

* Creating from keys

* Comparing order sensitively with other ordered dictionaries or order
  insensitively with other mappings

Installing
----------

::

    pip install indexed


Performance
-----------

Performance is practically on the same order of magnitude as the built in
``collections.OrderedDict``, with exceptions in bold:

================= ========== ================== ======== ======================
d                 ``collections.OrderedDict``   ``indexed.IndexedOrderedDict``
----------------- ----------------------------- -------------------------------
Operation         Avergage   Worst case         Average  Worst case
================= ========== ================== ======== ======================
d.copy()          O(n)       O(n)               O(n)     O(n)  
----------------- ---------- ------------------ -------- ----------------------
d[key]            O(1)       O(n)               O(1)     O(n)
----------------- ---------- ------------------ -------- ----------------------
d[key] = value    O(1)       O(n) [#a]_         O(1)     O(n) [#a]_
----------------- ---------- ------------------ -------- ----------------------
del d[key]        **O(1)**   O(n)               O(n)     O(n)
----------------- ---------- ------------------ -------- ----------------------
d.keys()[i]       O(n) [#k]_ O(n) [#k]_         **O(1)** **O(1)**
----------------- ---------- ------------------ -------- ----------------------
d.values()[i]     O(n) [#v]_ O(n) [#v]_         **O(1)** O(n)
----------------- ---------- ------------------ -------- ----------------------
d.items()[i]      O(n) [#v]_ O(n) [#v]_         **O(1)** O(n)
----------------- ---------- ------------------ -------- ----------------------
d.keys().index(x) O(n) [#v]_ O(n) [#v]_         O(n)     O(n)
================= ========== ================== ======== ======================

.. [#a] These are amortized_ worst case runtimes.
.. [#k] This does not work in Python 3 because ``colections.KeysView`` is not
        indexable. One of the theoretically best work arounds is
        ``next(itertools.islice(d.keys(), i, i + 1))``.
.. [#v] Assuming the theoretically best possible workaround.

License
-------

This library is derived from CPython's ``collections.OrderedDict``
and licensed under the PSFL.
See the LICENSE file for the full license text.

.. _amortized: http://en.wikipedia.org/wiki/Amortized_analysis
