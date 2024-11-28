for index, value in enumerate("abcdefgh"):
    print(index, value)

for t in enumerate("abcdefgh"):
    idx, value = t
    print(t, t[0], t[1], idx, value)

# Nested
albums = [("Braveheart", "Mel Gibson", 2001),
          ("Psy", "Cezary Pazura", 1997),
          ("Psy 2", "Bogusław Linda", 2002),
          ]

print(albums)
print("Len: {}".format(len(albums)))

for album in albums:
    name, actor, year = album
    print("Album {} {} {}".format(name, actor, year))

for name, actor, year in albums:
    print("Album {} {} {}".format(name, actor, year))
