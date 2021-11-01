d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# create a new dict from iterable
new_dict = dict.fromkeys(pantry_items, "Default Value")
print(new_dict)


# Returns a view of keys
keys = d.keys()
print(keys)

for item, value in d.items():
    print(f"Key={item},Value={value}")

