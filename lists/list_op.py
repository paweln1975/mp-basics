computer_parts = [
    "monitor",
    "cpu",
    "keyboard",
    "mouse",
    "mouse mat"
]

# replacing a slice
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts[3:])

# removing items from list
del computer_parts[0:2]
print(computer_parts)

# problem with removing the items using for loop
list1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list2 = list1.copy()

min_value = 5
max_value = 10
for index, value in enumerate(list1):
    if (value < min_value) or (value > max_value):
        del list1[index]

# the value 10 still remains in the list
print(list1)

stop = 0
for index, value in enumerate(list2):
    if value > min_value:
        stop = index
        break

del list2[:stop]

stop = 0
for index, value in enumerate(list2[::-1]):
    if value < max_value:
        stop = len(list2) - index
        break

del list2[stop:]
print(list2)

# safe removing items from list using backward traversing
data = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
min_valid = 5
max_valid = 10

for index in range(len(data)-1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        del data[index]
print("Data after removing values lower then {} and greater then {}: {}".format(min_valid, max_value, data))

# use of reversed() function
top_index = len(data) - 1
min_valid = 6
max_valid = 9
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index-index]
print("Data after removing values lower then {} and greater then {}: {}".format(min_valid, max_value, data))


# Nested list
even = [2, 4, 6, 8]
odd = [1, 3, 5]

con_list = [even, odd]
print("List: {}".format(con_list))

# Number of element occurrences
print(computer_parts)
print("Count: {}".format(computer_parts.count("trackball")))

challange1 = [
    ["test", "a", "b", "c"],
    ["e", "f", "g"],
    ["h", "Test", "test", "j"],
]

for list3 in challange1:
    top_idx = len(list3) - 1
    for index, item in enumerate(reversed(list3)):
        if item.casefold() == "test":
            del list3[top_idx - index]
    print(list3, end=' ')

print()

for list4 in challange1:
    items = ", ".join(item for item in list4 if item.casefold() != "test")
    print(items)



