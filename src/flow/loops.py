import random

string = "Python"
for character in string:
    print(character)

numbers = "34,4343.455;3242 233:4"
separators = ""
for char in numbers:
    if not char.isnumeric():
        separators += char

print(separators)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

capitals = ""
for char in quote:
    if char.isupper():
        capitals += char

print(capitals)

values = ""
for i in range(1, 20):
    if i == 10:
        continue
    values += str(i)
    if i < 15:
        values += " "
    else:
        break

print(values)

shopping_list = ["bread", "eggs", "milk"]
value = "eggs"
index = None

for val in range(0, len(shopping_list)):
    if value == shopping_list[val]:
        index = val
        break

if value in shopping_list:
    index = shopping_list.index(value)


if index is not None:
    print("Value {} found at index {}".format(value, index))
else:
    print("Not found")

letter = "a"
alphabet = ""
while not ord(letter) == 123:
    alphabet += letter
    letter = chr(ord(letter)+1)

print(alphabet)
values = []

for i in range(0, 100, 5):
    values.append(random.randint(0, i))
    if i == 95:
        break
else:
    print("Else in the loop")    # executed only when loop was not broken

print(values)
