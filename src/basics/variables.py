greeting = "Hello world!"
print(greeting)
print(type(greeting))

age = 24
print(age)
print(type(age))

ageStr = "24 years"
print(ageStr)
print(type(ageStr))

print("I'm " + str(age) + " years old")

a = 12
b = 3
print(a / b)
print(a // b)

parrot = "Norwegian Blue"

for i in range(0, len(parrot)):
    print(parrot[i], end=' ')

print()

# with negative index we go back
for i in range(0, len(parrot)):
    print(parrot[-i-1], end=' ')

print()

# Slicing
print("Slice 1: " + parrot[0:9])
print("Slice 2: " + parrot[:9])
print("Slice 3: " + parrot[10:])
print("Slice 4: " + parrot[:])
print("Slice 5: " + parrot[::2])    # with step

numbers = "1,2,3;4,5,6 7,8,9"
print(numbers[0::2])

separators = numbers[1::2]
print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values])

# negative step
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

# slicing idiom (1st Python idiom)
print(letters[::-1])

# produces qpo
print(letters[-10:-13:-1])
print(letters[16:13:-1])

# produces edcba
print(letters[-22::-1])
print(letters[4::-1])

# produces 8 last characters in reverse order
print(letters[:-9:-1])

# last 4 letters
print(letters[-4:])

# first char
print(letters[:1])

# last char
print(letters[-1:])
