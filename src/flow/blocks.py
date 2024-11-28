for i in range(1, 13):
    print("i={0}".format(i))
print("*" * 80)

age = 18

if age < 18 and age < 100:
    print("You are too young. Please come back in {} years".format(18 - age))
elif age == 100:
    print("Amazing achievement!")
elif age > 100:
    print("Too old :-(")
else:
    print("You are an adult!")
    print("Congratulation!")

if 18 <= age <= 40:
    print("Good")


test = 10


def fun():
    print("Did I work?")
    return True


if age >= 18 or fun():   # second condition is not evaluated (the same with and condition)
    print("Correct values")
