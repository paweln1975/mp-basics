import random
min_val = 0
max_val = 1000
mid = -1

count = 0

value = random.randint(min_val, max_val)
print("Value is {}".format(value))

while not mid == value:
    mid = (max_val + min_val) // 2
    if value > mid:
        min_val = mid
    else:
        max_val = mid
    count += 1

print("Value {}  found after {} iterations".format(value, count))


