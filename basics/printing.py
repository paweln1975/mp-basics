import datetime

print('Hello world!')
print(1+2)
print(6*7)
print()
print('end', 'really end?', 3)

print('Test 1\nTest 2\nTest 3')
print("Test \"Escape character\"")
print('Test 1\tTest 2\tTest 3\tTest 4')

print("Text \
split \
over \
3 \
lines")

print("c:\\Users\\pawel")

print("* "*4)
for x in range(1, 3):
    print("*     *")
print("* "*4)

# function that print names of a day


d = datetime.date(2023, 9, 24)
for i in range(1, 8):
    print(d.strftime("%A"))
    d = d + datetime.timedelta(days=1)
