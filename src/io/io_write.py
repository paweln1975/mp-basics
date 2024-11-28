cities = ["Krakow", "Warsaw", "Katowice"]

with open("/home/centos/IdeaProjects/mp-basics.py/cities.txt", "w") as city_file:
    for city in cities:
        print(city, file=city_file, flush=True)   # flush - data are written immediately

new_cities = []
with open("/home/centos/IdeaProjects/mp-basics.py/cities.txt", "r") as city_file:
    for city in cities:
        new_cities.append(city.strip())

print(new_cities)

# write a tuple to a file and use eval to evaluate the expression

artist_data = "Dire Straits", "Mark Knopfler", "Brothers in Arms", ((1, "Track 1"), (2, "Track 2"))
with open("/home/centos/IdeaProjects/mp-basics.py/artist.txt", "w") as artist_file:
    print(artist_data, file=artist_file)


with open("/home/centos/IdeaProjects/mp-basics.py/artist.txt", "r") as artist_file:
    new_data = artist_file.readline()

band_name, artist, title, tracks = eval(new_data)
track1, track2 = eval(str(tracks))
print(band_name, artist, title, track1[1], track2[1])

