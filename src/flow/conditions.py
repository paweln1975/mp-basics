day = "Saturday"
temperature = 21
raining = True

if (day == "Saturday" and temperature > 25) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

name = ""
value = 0
table = []

if name or value or table:
    print("1. True")
else:
    print("1. False")

day = "day"

if day in "Monday":
    print("2. True")

if day not in "Python":
    print("3. True")

print("Good buy".casefold())

if "Monday".find(day) > -1:
    print("4. True")
else:
    print("4. False")

if "Python".find(day) > -1:
    print("5. True")
else:
    print("5. False")
