"""
training Hashable interface
>>> import sys; sys.tracebacklimit = 0
>>> from collections.abc import Hashable
>>> x = 1
>>> print(check_hashable(x))
Hashable

>>> x = [0, 1, 2]
>>> print(check_hashable(x))
Not hashable
"""
from collections.abc import Hashable


def check_hashable(some_object) -> str:
    if isinstance(some_object, Hashable):
        return "Hashable"
    return "Not hashable"