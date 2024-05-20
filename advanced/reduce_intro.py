import functools
import collections


def fun_add(x, y):
    return x + y


list1 = [4, 5, 6, 34, 1, 0]
value = functools.reduce(fun_add, list1, 0)
print(value)
print(sum(list1))

# any, all functions
print(f"any: {any(list1)}")
print(f"all: {all(list1)}")

list2 = ["", False, '', 0, 0.0, [], (), None, {}]
print(f"any: {any(list2)}")
print(f"all: {all(list2)}")

Person = collections.namedtuple("Person", ["name", "e_mail"])
people = [
    Person("Pawel", "pn1@poczta.onet.pl"),
    Person("Monika", "")
]

# check if all have e-mail address, be careful any with empty list returns True
print(bool(people) and all([person.e_mail for person in people]))

print(any(["poczta" in person.e_mail for person in people]))
