even = [i for i in range(2, 20, 2)]
odd = [i for i in range(1, 20, 2)]
print(even)
odd.extend(even)
print(odd)

# sorting the list
odd.sort()
print(odd)

odd.sort(reverse=True)
print(odd)

# creating new sorted list
sentence = "The strange guy looked at me"
letters = sorted(sentence, key=str.casefold)
print(letters)

digits = sorted("9384934530945039485")
print(digits)
