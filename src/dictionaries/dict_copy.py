import copy

animals = {
    "lion": "big",
    "cat": "small"
}

# just reference copy
copy_animals = animals
animals.update({"mouse": "tiny"})
print(copy_animals)

# deep copy
copy_animals = animals.copy()
animals.update({"dog": "calm"})
print(copy_animals)
print(animals)

# shallow copy - references to mutable objects are copied
animals = {
    "lion": ["big", "king"],
    "cat": ["small", "nice"]
}

copy_animals = animals.copy()
animals["cat"].append("silent")
print(copy_animals)

# deep copy - special function in a module copy
copy_animals = copy.deepcopy(animals)
animals["cat"].append("greedy")
print(id(copy_animals["cat"]), copy_animals)
print(id(animals["cat"]), animals)