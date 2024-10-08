numbers = [1, 2, 3, 4, 5]

squares = []
for n in numbers:
    squares.append(n ** 2)

print(squares)

print("".join(["1", "=" * 40]))

squares = [n ** 2 for n in numbers if n % 2 == 0]
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


print("".join(["6", "=" * 40]))
r = range(1, 51)
even = [val for val in r if val % 2 == 1]
print(even)

print("".join(["7", "=" * 40]))
r = range(1, 26)
even_with_0 = [val if val % 2 == 1 else 0 for val in r]
print(even_with_0)

print("".join(["8", "=" * 40]))

fizzbuzz = ["fizzbuzz" if val % 15 == 0 else "fiz" if val % 3 == 0 else "buz" if val % 5 == 0 else val for val in range(1, 31)]
print(fizzbuzz)

print("".join(["9", "=" * 40]))
burgers = ["beef", "pork", "chicken"]
toppings = ["cheese", "egg", "salad"]
meals = [[(burger, topping) for burger in burgers] for topping in toppings]
print(meals)

# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
print([item for item in my_numbers if item % 2 == 0])
