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

for i in range(0, len(parrot)):
    print(parrot[-i-1], end=' ')

print()

# Slicing
print("Slice 1: " + parrot[0:9])
print("Slice 2: " + parrot[:9])
print("Slice 3: " + parrot[10:])
print("Slice 4: " + parrot[:])
print("Slice 5: " + parrot[::2]) # with step
