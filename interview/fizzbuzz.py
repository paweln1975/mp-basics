"""
Calculates typical interview question about fizz buzz
>>> import sys; sys.tracebacklimit = 0
>>> fizzbuzz(2, 1)
Traceback (most recent call last):
ValueError: start cannot be greater then end

>>> fizzbuzz(1, 1)
Traceback (most recent call last):
ValueError: start cannot be equal to end

>>> fizzbuzz('1', 0)
Traceback (most recent call last):
TypeError: start must be int

>>> fizzbuzz(-5, '0')
Traceback (most recent call last):
TypeError: end must be int

>>> fizzbuzz(1, 31)
[1, 2, 'fiz', 4, 'buz', 'fiz', 7, 8, 'fiz', 'buz', 11, 'fiz', 13, 14, 'fizzbuzz', 16, 17, 'fiz', 19, 'buz', 'fiz', 22, \
23, 'fiz', 'buz', 26, 'fiz', 28, 29, 'fizzbuzz']

>>> fizzbuzz(3, 4)
['fiz']

>>> fizzbuzz(15, 16)
['fizzbuzz']

>>> fizzbuzz(5, 6)
['buz']

>>> fizzbuzz(-100, 100)
['buz', 'fiz', -98, -97, 'fiz', 'buz', -94, 'fiz', -92, -91, 'fizzbuzz', -89, -88, 'fiz', -86, 'buz', 'fiz', -83, \
-82, 'fiz', 'buz', -79, 'fiz', -77, -76, 'fizzbuzz', -74, -73, 'fiz', -71, 'buz', 'fiz', -68, -67, 'fiz', 'buz', -64, \
'fiz', -62, -61, 'fizzbuzz', -59, -58, 'fiz', -56, 'buz', 'fiz', -53, -52, 'fiz', 'buz', -49, 'fiz', -47, -46, \
'fizzbuzz', -44, -43, 'fiz', -41, 'buz', 'fiz', -38, -37, 'fiz', 'buz', -34, 'fiz', -32, -31, 'fizzbuzz', -29, -28, \
'fiz', -26, 'buz', 'fiz', -23, -22, 'fiz', 'buz', -19, 'fiz', -17, -16, 'fizzbuzz', -14, -13, 'fiz', -11, 'buz', \
'fiz', -8, -7, 'fiz', 'buz', -4, 'fiz', -2, -1, 'fizzbuzz', 1, 2, 'fiz', 4, 'buz', 'fiz', 7, 8, 'fiz', 'buz', 11, \
'fiz', 13, 14, 'fizzbuzz', 16, 17, 'fiz', 19, 'buz', 'fiz', 22, 23, 'fiz', 'buz', 26, 'fiz', 28, 29, 'fizzbuzz', \
31, 32, 'fiz', 34, 'buz', 'fiz', 37, 38, 'fiz', 'buz', 41, 'fiz', 43, 44, 'fizzbuzz', 46, 47, 'fiz', 49, 'buz', \
'fiz', 52, 53, 'fiz', 'buz', 56, 'fiz', 58, 59, 'fizzbuzz', 61, 62, 'fiz', 64, 'buz', 'fiz', 67, 68, 'fiz', 'buz', \
71, 'fiz', 73, 74, 'fizzbuzz', 76, 77, 'fiz', 79, 'buz', 'fiz', 82, 83, 'fiz', 'buz', 86, 'fiz', 88, 89, 'fizzbuzz', \
91, 92, 'fiz', 94, 'buz', 'fiz', 97, 98, 'fiz']
"""


def fizzbuzz(start, end):
    if not type(start) is int:
        raise TypeError('start must be int')

    if not type(end) is int:
        raise TypeError('end must be int')

    if start > end:
        raise ValueError('start cannot be greater then end')

    if start == end:
        raise ValueError('start cannot be equal to end')

    result = ["fizzbuzz"
              if val % 15 == 0
              else "fiz" if val % 3 == 0
              else "buz" if val % 5 == 0
              else val
              for val in range(start, end)]
    return result
