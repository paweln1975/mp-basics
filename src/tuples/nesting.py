albums = [
    ("Album 1", "Author 1", 2001,
     [
         (1, "Song 1"),
         (2, "Song 2"),
         (3, "Song 3"),
         (4, "Song 4"),
     ]
     ),
    ("Album 2", "Author 2", 2002,
     [
         (1, "Song 5"),
         (2, "Song 6"),
         (3, "Song 7"),
         (4, "Song 8"),
     ]
     )
]

print(albums)

for name, author, year, songs in albums:
    print("Album: {} Author: {}, Year: {} Songs: {}".format(name, author, year, songs))

song8 = albums[1][3][3][1]
print(song8)
