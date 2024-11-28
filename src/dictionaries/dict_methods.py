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
    "xi": "eleven"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']


def print_dict(dp):
    for item, value in dp.items():
        print(f"Key={item},Value={value}")


# create a new dict from iterable
new_dict = dict.fromkeys(pantry_items, "Default Value")
print(new_dict)


# Returns a view of keys
keys = d.keys()
print(keys)

# Updates the dict, overwrites existing keys
d2 = {
    7: "lucky seven",
    10: "ten",
    3: "new three"
}

d.update(d2)

d.update(enumerate(pantry_items, 1))
print_dict(d)

# Returns a view of values
v = d.values()
d[11] = "eleven"

# If added to the dict, view will be automatically updated
print(v)

# check existence
print("eleven" in v)

# convert to lists
lkeys = list(keys)
lvalues = list(v)

# find the index of a given value, finds first
if "eleven" in lvalues:
    index = lvalues.index("eleven")
    key = lkeys[index]
    print(f"{d[key]} found with the key {key}")

# alternative via loop without memory allocation for views, finds all
for key, value in d.items():
    if value == "eleven":
        print(f"{value} found with the key {key}")
