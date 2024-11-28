import shelve

print(dir())

for name in dir(__builtins__):
    print(name)

print("=" * 20)

for name in dir(shelve.Shelf):
    if not name.startswith("_"):
        print(name)

print("=" * 20)

help(shelve.Shelf)
