"""
Assertion training
>>> import sys; sys.tracebacklimit = 0
>>> sum_values(5)
15

>>> sum_values(-10)
Traceback (most recent call last):
AssertionError: Parameter n must be > 0
"""

def sum_values(n: int) -> int:
    s = 0
    assert n >=0, "Parameter n must be > 0"
    s = sum(range(n + 1))
    return s
