set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e", "f"}

print(set1)
print(set2)

# union
set3 = set1.union(set2)
print(f"Union:{sorted(set3)}")

# intersection
set3 = set1.intersection(set2)
print(f"Intersection:{sorted(set3)}")

# difference
set3 = set1 - set2
print(f"Difference:{sorted(set3)}")

# symmetric difference - opposite to intersection
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

# remove duplicates
color_list = ["red", "yellow", "blue", "red"]
colors = set(color_list)
print(sorted(colors))

# remove duplicates but preserve the order
colors = list(dict.fromkeys(color_list))
print(colors)

int_set = set(range(0, 30, 2))
print(int_set)
int_set.remove(20)  # error if 20 does not exist
int_set.discard(20)   # no error if there is no 20 in the set
print(int_set)
int_set.clear()
print(int_set)


