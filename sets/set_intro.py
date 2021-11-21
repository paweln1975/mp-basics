set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e", "f"}

print(set1)
print(set2)

# union | operator
set3 = set1.union(set2)
print(f"Union:{sorted(set3)}")

# intersection & operator
set3 = set1.intersection(set2)
print(f"Intersection:{sorted(set3)}")

# difference - returns a new set
set3 = set1 - set2
print(f"Difference:{sorted(set3)}")

set3.difference_update(["a"])
print(f"Difference update :{sorted(set3)}")

# symmetric difference - opposite to intersection   ^ operator
set3 = set1.symmetric_difference(set2)
print(f"Symmetric difference:{sorted(set3)}")


# comparing sets
set4 = {"c", "d", "e", "f"}
print(f"Equal sets: {set2} and {set4}:{set2 == set4}")
print(f"Different sets: {set1} and {set4}:{set1 == set4}")

# create set
print(set("12345"))
print(set(range(0, 20, 2)))

# empty set
numbers = set()
print(f"Empty set {numbers} with type {type(numbers)}")

# add values
numbers.add(1)
for i in list("1234"):
    numbers.add(int(i))
print(numbers)

# create immutable set
list1 = range(1, 20)
im_set = frozenset(list1)
print(im_set)

# updates a set, useful in a loop
list2 = []
for i in range(1, 10):
    list2.append(set(range(1, i)))

print(f"List 2: {list2}")

set5 = set()
for item in list2:
    set5.update(item)   # the same as operator |=

print(f"Set 5: {set5}")
