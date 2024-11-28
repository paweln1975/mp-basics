"""
training OrderedDict
>>> import sys; sys.tracebacklimit = 0
>>> from collections import OrderedDict
>>> od1 = create_ordered_dict()
>>> od1
OrderedDict({'Ann': 9.5, 'Em': 8.5, 'Paul': 7.5})

>>> od2 = add_new_item(od1, "Max", 100)
>>> od2
OrderedDict({'Max': 100, 'Ann': 9.5, 'Em': 8.5, 'Paul': 7.5})

>>> od3 = remove_2_items(od2)
>>> od3
OrderedDict({'Max': 100, 'Ann': 9.5})
"""
from collections import OrderedDict

def create_ordered_dict():
    marks = OrderedDict()
    marks['Ann'] = 9.5
    marks['Em'] = 8.5
    marks['Paul'] = 7.5
    return marks

def add_new_item(marks, key, value):
    marks.update({key: value})
    marks = OrderedDict(marks)
    marks.move_to_end(key, last=False)
    return marks


def remove_2_items(marks):
    marks.popitem(last=True)
    marks.popitem(last=True)
    return marks
