import pickle

print(f"Default protocol is {pickle.DEFAULT_PROTOCOL}, highest protocol version is {pickle.HIGHEST_PROTOCOL}")

artist_data = "Dire Straits", "Mark Knopfler", "Brothers in Arms", ((1, "Track 1"), (2, "Track 2"))
even = list(range(0, 100, 2))
odd = list(range(1, 101, 2))

with open("/home/centos/IdeaProjects/mp-basics.py/artist.pickle", "wb") as pickle_file:
    pickle.dump(artist_data, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)

with open("/home/centos/IdeaProjects/mp-basics.py/artist.pickle", "rb") as pickle_file:
    artist_data2 = pickle.load(pickle_file)
    even_list = pickle.load(pickle_file)
    odd_list = pickle.load(pickle_file)

print(artist_data2)
band_name, artist, title, tracks = artist_data2
print(band_name)
print(even_list)
print(odd_list)

