computer_parts = [
    "monitor",
    "cpu",
    "keyboard",
    "mouse"
]

for part in computer_parts:
    print(part)

print(computer_parts[0:3])

# extend the list
computer_parts += ["RAM"]
print(computer_parts[:])

list1 = list2 = list3 = computer_parts
list2.append("printer")
print(list1)
print("Max:" + max(list3))
print("Min:" + min(list3))
print("Len:" + str(len(list3)))
print("Count:" + str(list1.count("RAM")))

# enumerate function - index + item
for number, part in enumerate(list1):
    print("{}: {}".format(number, part))

for number, part in enumerate("ABC"):
    print("{}: {}".format(number, part))

# creating list
valid_choices = [str(i) for i in range(0, len(computer_parts))]
print(valid_choices)

# immutable objects
result = True
result_copy = result
print(id(result))
print(id(result_copy))

result = False
print(id(result))
print(id(result_copy))

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for d in data:
    if "Flower" in d:
        flowers.append(d)
    if "Shrub" in d:
        shrubs.append(d)
print("Flowers:{}".format(flowers))
print("Shrubs:{}".format(shrubs))

# save removal
shrubs_idx = [item for item in shrubs]
for item in shrubs_idx:
    if item in shrubs:
        shrubs.remove(item)

print("Shrubs:{}:{}".format(len(shrubs), shrubs))

# copying list
digits = list("09340958309458039485039485")
print(digits)

digits1 = list("123")
digits2 = list(digits1)

print("The same list: {}".format(digits1 is digits2))
print("The same content: {}".format(digits1 == digits2))

digits3 = digits2.copy()
print("The same list: {}".format(digits3 is digits2))
print("The same content: {}".format(digits3 == digits2))

