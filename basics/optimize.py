"""
optimization
>>> import sys; sys.tracebacklimit = 0
>>> import time
>>> input = "50 45 100 12 26"
>>> output = get_min_max(input)
>>> print(output[0], output[1])
12 100
"""

def get_min_max(s: str):
    list_of_ints = [int(value) for value in s.split()]
    return min(list_of_ints), max(list_of_ints)
