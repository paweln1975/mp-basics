text = "A big horse came out and set up the door"
capitals = [c.upper() for c in text]
print(capitals)

# use map
map_capitals = list(map(str.upper, text))
print(map_capitals)

words = [word.upper() for word in text.split(" ")]
print(words)

# use map
map_words = list(map(str.upper, text.split(" ")))
print(map_words)


# use filter
def not_space(p):
    return " " not in p


map_capitals_filtered = list(map(str.upper, filter(not_space, text)))
print(map_capitals_filtered)
