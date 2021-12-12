import song

a_list = song.load_data()
print(len(a_list))


s = song.Song("Walking death", 5)
s.duration -= 1
s.duration -= 1
print(s)
