"""
Test data classes
>>> import sys; sys.tracebacklimit = 0
>>> p1 = Person('Pawel', 49)
>>> p1
Person(name='Pawel', age=49)

>>> p2 = Person('Pawel', 49)
>>> p1 == p2
True

>>> p1 > p2
False

>>> p3 = Person(name='Monika', age=49)
>>> p3.age = 50
>>> p3
Person(name='Monika', age=50)
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age
