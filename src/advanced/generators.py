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
        a, b = b, a + b


my_r = my_range(5)
for val in my_r:
    print(val, end=' ')

print()

fib_r = fib()


def fibonacci(n):
    v = 0
    if n == 0:
        return v
    gen = fib()

    for _ in range(n):
        v = next(gen)

    return v


for i in range(10):
    print(f"fib({i})={fibonacci(i)}", end=' ')

print()

# Leibniz formula for PI
print(f"PI={math.pi}")


def leibniz():
    start, result = -1, 1
    while 1:
        start += 2
        yield result
        if start > 1:
            if not (start / 2 - 0.5) % 2:
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


def letters(word):
    for c in word:
        yield c


gen = letters('python')
for _ in range(len('python')):
    print(next(gen))


def number_gen(str_number):
    for c in str_number:
        yield int(c)


def calc_numbers_sum(value):
    value_str = str(value)
    gen = number_gen(value_str)

    values_sum = 0
    for c in gen:
        values_sum += c

    return values_sum


print(calc_numbers_sum('5358052'))
print(calc_numbers_sum('4066376'))

print(sum((int(i) for i in '5358052')))
print(sum((int(i) for i in '4066376')))


def square():
    value = 1
    while True:
        yield value ** 2
        value += 1


gen = square()

for _ in range(5):
    print(next(gen))


def gen_even(n):
    yield from range(0, 2 * n, 2)


n = 10
gen = gen_even(n)

for _ in range(n):
    print(next(gen), end=' ')
