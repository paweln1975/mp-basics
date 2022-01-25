# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fact_gen():
    r, v = 1, 1
    while True:
        yield r
        r = r * v
        v += 1


def fact_using_gen(n):
    ran = fact_gen()
    x = 0
    for x in ran:
        n = n - 1
        if n == -1:
            break
    return x


num = 10
calc = 50000
t = timeit.Timer(lambda: fact(num))
result1 = t.timeit(calc)
print(f"Fact(100): {result1}")

t = timeit.Timer(lambda: factorial(num))
result2 = t.timeit(calc)
print(f"Factorial(100): {result2}")

t = timeit.Timer(lambda: fact_using_gen(num))
result3 = t.timeit(calc)
print(f"Fact_using_gen(100): {result3}")
