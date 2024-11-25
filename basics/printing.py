"""
printing internal library plus pprint training
>>> import sys; sys.tracebacklimit = 0
>>> import datetime
>>> import pprint

>>> print_days()
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday

>>> print_table()
* * * *
*     *
*     *
* * * *
>>> d = [
...         {"abcdef": 1, "babcdef": 2, "cabcdef": 3},
...         {"abcdef": 4, "babcdef": 5, "cabcdef": 6}
...     ]
>>> print_dict(d)
[{'abcdef': 1, 'babcdef': 2, 'cabcdef': 3},
 {'abcdef': 4, 'babcdef': 5, 'cabcdef': 6}]
"""
import datetime
import pprint

print('Hello world!')
print(1+2)
print(6*7)
print()
print('end', 'really end?', 3)

print('Test 1\nTest 2\nTest 3')
print("Test \"Escape character\"")
print('Test 1\tTest 2\tTest 3\tTest 4')

print("Text \
split \
over \
3 \
lines")

print("c:\\Users\\pawel")

def print_table():
    s = "* "*4
    s = s.rstrip()
    print(s)
    for x in range(1, 3):
        print("*     *")
    print(s)

# function that print names of a day

def print_days():
    d = datetime.date(2023, 9, 24)
    for i in range(1, 8):
        print(d.strftime("%A"))
        d = d + datetime.timedelta(days=1)

def print_dict(d: list):
    pprint.pprint(d)