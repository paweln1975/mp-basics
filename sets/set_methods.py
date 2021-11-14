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

# removing non existing element from the set with exception handling
values = {"Paul", "Sean", "Kelly"}

try:
    values.remove("Anna")
    values.remove("Paul")
except KeyError:
    print(f"Exception")

print(values)

# Unpacking * operator, each item is passed separately to the print function
print(*sorted(values), sep='\n')

# pop removes the item from set(), while with set example
while values:
    print(values.pop())





