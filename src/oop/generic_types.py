"""
typing library and generic classes
>>> import sys; sys.tracebacklimit = 0
>>> a: MyGenericClass(str) = MyGenericClass('abc')
>>> a.output()
The stored value is abc. The type variable equals to <class 'str'>.
>>> b: MyGenericClass(int) = MyGenericClass(123)
>>> b.output()
The stored value is 123. The type variable equals to <class 'int'>.
>>>
"""
from typing import TypeVar, List, Union, Generic
T = TypeVar('T')


class MyGenericClass (Generic[T]) :
    def __init__(self, value: T) -> None:
        self.value = value
    def output(self) -> None:
        print(f'The stored value is {self.value}. The type variable equals to {type(self.value)}.')
