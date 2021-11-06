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
