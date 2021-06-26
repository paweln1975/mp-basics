computer_parts = [
    "monitor",
    "cpu",
    "keyboard",
    "mouse"
]

for part in computer_parts:
    print(part)

print(computer_parts[0:3])

computer_parts += ["RAM"]
print(computer_parts[:])

list1 = list2 = list3 = computer_parts
list2.append("printer")
print(list1)
print("Max:" + max(list3))
print("Min:" + min(list3))
print("Len:" + str(len(list3)))
print("Count:" + str(list1.count("RAM")))

for number, part in enumerate(list1):
    print("{}: {}".format(number, part))

for number, part in enumerate("ABC"):
    print("{}: {}".format(number, part))

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
