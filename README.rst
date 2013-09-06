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
indexed.py is licensed under the GPL3. See the LICENSE file for full copyright
and license information.

.. _amortized: http://en.wikipedia.org/wiki/Amortized_analysis
