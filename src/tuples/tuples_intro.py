"""
training tuples
>>> import sys; sys.tracebacklimit = 0
>>> brave_heart = "Braveheart", "Mel Gibson", 2001
>>> unpack_first_element_from_tuples(brave_heart)
'Braveheart'

>>> unpack_last_element_from_tuples(brave_heart)
2001

>>> first, second, *others, last = create_num_tuple(10)
>>> last
10

>>> others
[2, 3, 4, 5, 6, 7, 8, 9]
"""

def unpack_first_element_from_tuples(t):
    first, *others = t
    return first

def unpack_last_element_from_tuples(t):
    *others, last = t
    return last


def create_num_tuple(num) -> tuple:
    return tuple(n for n in range(0, num+1))


# Simple tuple, tuples are immutable (Benefit 1: data protection)
t = "a", "b", "c"
print(t)

print(10, 20, "Name", 2020)

# Brackets needed if we want a tuple
print((10, 20, "Name", 2020))

brave_heart = "Braveheart", "Mel Gibson", 2001
psy = "Psy", "Cezary Pazura", 1997
psy2 = "Psy 2", "Bogusław Linda", 2002

print(brave_heart, psy, psy2)
print(brave_heart[0])

brave_heart_list = list(brave_heart)
print(brave_heart_list)

brave_heart_list[0] = "Die Hard"
print(brave_heart_list)

# Unpacking the tuple (Benefit 2: Always know how many to unpack)
data = 1, 2, 3
x, y, z = data
print(x)
x = 3
print(x, y, z)

# Unpacking the list
data_list = [10, 20, 30]
x, y, z = data_list
print(x)
x = 30
print(x, y, z)

tuple_var = tuple(data_list)
print(tuple_var)

# print last element of a tuple
numbers = create_num_tuple(10)
print(numbers[len(numbers)-1])
print(numbers[-1])