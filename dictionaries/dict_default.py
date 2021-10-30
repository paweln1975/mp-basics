def add_value_to_dict(data: dict, key: str, value: int):
    """setdefault method gets the value from dictionary, if the value for the key does not exist it sets the
    default value."""
    data[key] = data.setdefault(key, 0) + value
    return data[key]


k = 10
d1 = {}

add_value_to_dict(d1, "k", k)
print(d1)

add_value_to_dict(d1, "k", k)
print(d1)

k1 = d1.get("k1", 0)
print(f"k={k1}")

for key, value in sorted(d1.items()):
    print(f"{key}={value}")
