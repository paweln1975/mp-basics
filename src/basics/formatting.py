for i in range(1, 13):
    print("value: {0:2}, squared: {1:3}, cubed: {2:4}".format(i, i ** 2, i ** 3))   # aligned left


print()

for i in range(1, 13):
    print("value: {0:<2}, squared: {1:<3}, cubed: {2:^4}".format(i, i ** 2, i ** 3))  # aligned right and centered

print()

print("Pi value: {0:12}".format(22 / 7))
print("Pi value: {0:12.50f}".format(22 / 7))    # precision of 50 after decimal point is more important then size 12

print("Pi value: {0:<72.51f}".format(22 / 7))
print("Pi value: {0:<72.54f}".format(22 / 7))     # max floating precision is 51

print(f"Pi value with f-string: {22 / 7:<72.54f}")    # f-string since Python 3.6

pi = 22 / 7
print(f"Pi value with f-string: {pi:<72.54f}")

print()

for i in range(1, 13):
    print("value: {:<2}, squared: {:<3}, cubed: {:<4}".format(i, i ** 2, i ** 3))   # default order

print()

age = 24
print("My age is %d" % age)      # interpolation, way of formatting deprecated and will be removed in the future
print("PI is: %f" % pi)
print("Age=%d PI=%f" % (age, pi))
