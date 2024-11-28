"""
Testing match statement
>>> import sys; sys.tracebacklimit = 0

>>> cat = Cat(name='Kitty', age=5, tail_length=20.0, breed='Persian')
>>> match_animal(cat)
Any cat with the tail length of 20.0 matches this case! Name is Kitty, age is 5, breed is Persian

>>> cat = Cat(name='Kitty', age=5, tail_length=20.1, breed='Persian')
>>> match_animal(cat)
Any cat named Kitty of age 5 matches this case! Breed is Persian, tail length is 20.1

>>> dog = Dog(name='Fluffy', age=5, breed='Labrador', barking_volume=20.0, is_hunting_breed=True)
>>> match_animal(dog)
Any dog named Fluffy matches this case! No need for statistics :)

>>> dog = Dog(name='Reksio', age=5, breed='Labrador', barking_volume=20.0, is_hunting_breed=True)
>>> match_animal(dog)
Any dog matches this case!

>>> cat = Cat(name='Fraya', age=10, tail_length=20.1, breed='Persian')
>>> match_animal(cat)
Every left animal matches this case! Name is Fraya, age is 10, breed is Persian


>>> analyze_dict(input)
Programming definition!
>>> analyze_dict(input2)
corresponding definition
>>> analyze_dict(input3)
The dictionary does not contain the word code
"""
from dataclasses import dataclass

@dataclass
class Cat:
    name: str
    age: int
    breed: str
    tail_length: float

@dataclass
class Dog:
    name: str
    age: int
    breed: str
    barking_volume: float
    is_hunting_breed: bool

def match_animal(animal):
    match animal:
        case Cat(tail_length=20.0):
            print('Any cat with the tail length of 20.0 matches this case! '
                  f'Name is {animal.name}, age is {animal.age}, breed is {animal.breed}')
        case Cat(name='Kitty', age=5):
            print('Any cat named Kitty of age 5 matches this case! '
                 f'Breed is {animal.breed}, tail length is {animal.tail_length}')
        case Dog(name='Fluffy'):
            print('Any dog named Fluffy matches this case! No need for statistics :)')
        case Dog():
            print('Any dog matches this case!')
        case _:
            print('Every left animal matches this case! ' 
                  f'Name is {animal.name}, age is {animal.age}, breed is {animal.breed}')

input = {
    "code": "program instructions",
    "drive ": "an innate, biologically determined urge to attain a goal or satisfy a need",
    "to": "preposition",
    "develop": "grow or cause to grow and become more mature, advanced, or elaborate"
}

input2 = {
    "code": "corresponding definition",
    "drive ": "an innate, biologically determined urge to attain a goal or satisfy a need",
    "to": "preposition",
    "develop": "grow or cause to grow and become more mature, advanced, or elaborate"
}

input3 = {
    "no_code": "corresponding definition",
    "drive ": "an innate, biologically determined urge to attain a goal or satisfy a need",
    "to": "preposition",
    "develop": "grow or cause to grow and become more mature, advanced, or elaborate"
}

def analyze_dict(data_dict):
    match data_dict:
        case {'code': 'program instructions'}:
            print('Programming definition!')
        case {'code': definition}:
            print(definition)
        case _:
            print('The dictionary does not contain the word code')
