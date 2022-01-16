import sys
import math

big_r = range(10000)
print(f"Size of big_r is {sys.getsizeof(big_r)}")
big_l = []
for val in big_r:
    big_l.append(val)

print(f"Size of big_l is {sys.getsizeof(big_l)}")


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b


my_r = my_range(5)
for val in my_r:
    print(val, end=' ')

print()

fib_r = fib()
for i in range(10):
    print(f"fib({i})={next(fib_r)}", end=' ')

print()

# Leibniz formula for PI
print(f"PI={math.pi}")


def leibniz():
    start, result = -1, 1
    while 1:
        start += 2
        yield result
        if start > 1:
            if not (start/2-0.5) % 2:
                result = result + 1 / start
            else:
                result = result - 1 / start


pi = 0
lei = leibniz()
for i in range(1000000):
    pi = 4 * next(lei)
print(f"PI={pi}")


def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = odd_numbers()
    approx_pi = 0
    while True:
        approx_pi += (4 / next(odds))
        yield approx_pi
        approx_pi -= (4 / next(odds))
        yield approx_pi


pi_range = pi_series()
for i in range(1000000):
    pi = next(pi_range)
print(f"PI={pi}")
