"""
Lambda function training
>>> import sys; sys.tracebacklimit = 0
>>> power2(10)
100

>>> list1 = [1, 2, 3, 4, 5]
>>> list(map(lambda v: v ** 2, list1))
[1, 4, 9, 16, 25]

>>> list(map(power2, list1))
[1, 4, 9, 16, 25]

>>> power3 = create_power_n(3)
>>> list(map(power3, list1))
[1, 8, 27, 64, 125]

>>> filter1 = create_filter_mod(2)
>>> list(filter(filter1, map(power3, list1)))
[8, 64]

>>> list2 = reversed(list1)
>>> list(map(lambda x, y: x + y, list1, list2))
[6, 6, 6, 6, 6]

>>> list3 = [-2, -1, 0, 1, 2, 3]
>>> find_positive(list3)
[1, 2, 3]
"""
power2 = lambda x: x ** 2

def create_power_n(n):
    return lambda x: x ** n

def create_filter_mod(n):
    return lambda x: x % n == 0

def find_positive(my_list):
    # complete the next line
    return list(filter(lambda x: x > 0, my_list))
