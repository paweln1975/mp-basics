# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

for c in text:
    if c.isalpha():
        cl = c.lower()
        word_count[cl] = word_count.setdefault(cl, 0) + 1
#        print(f"{cl} {word_count[cl]}")

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
