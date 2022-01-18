numbers = [1, 2, 3, 4, 5]

squares = []
for n in numbers:
    squares.append(n ** 2)

print(squares)

print("".join(["1", "=" * 40]))

squares = [n ** 2 for n in numbers]
print(squares)

print("".join(["2", "=" * 40]))
squares_set = {n ** 2 for n in numbers}
print(squares_set)


print("".join(["3", "=" * 40]))
squares_dict = {n: n ** 2 for n in numbers}
print(squares_dict)

print("".join(["4", "=" * 40]))
text = "text done"
capitals = [char.upper() for char in text]
print(capitals)
words = [word.upper() for word in text.split(" ")]
print(words)
lc_words = text.split(" ")
print(lc_words)

print("".join(["5", "=" * 40]))


def center_text(*args):
    text1 = "-".join([str(arg) for arg in args])
    left_margin = (80 - len(text1)) // 2
    print(" " * left_margin, text1)


center_text("spam and eggs")
center_text("spam", "spam")
center_text(12, 4)
center_text("first", "second", 3, 4, "spam")
