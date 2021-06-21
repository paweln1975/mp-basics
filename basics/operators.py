string1 = "hello "
string2 = "world"

print(string1+string2)
print("hello " "world")

print(string1*5)
print(string1*5 + "4")

today = "monday"
print("day" in today)       # True
print("parrot" in today)    # False
print("Day" in today)       # False

age = 46
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print()

print(f"My age is {age}")
print("Type of age: {}".format(type(age)))

current_year = 2021
print("My age is {0} years and I was born in {1}.".format(age, current_year - age))

print("""
Jan: {0}
Feb: {1}
Mar: {0}
""".format(31, 28))

