def factorial(n: int) -> int:
    """
    Calculate factorial (n!) value. 0! = 1 5! = 1*2*3*4*5

    :param n: `int` value greater or equal to 0.
    :return: Factorial value for n.
    :raises ValueError: If n is lower then 0
    """
    value = 1
    if n < 0:
        raise ValueError("Parameter must be greater or equal to 0")
    elif n == 0:
        return value
    else:
        for i in range(1, n+1):
            value *= i
        return value


def factorial_rec(n: int) -> int:
    """
    Return n! (0! is 1).

    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1

    return n * factorial_rec(n - 1)


for i in range(36):
    print("{0} {1}".format(i, factorial(i)))

print("Recursive test")
k = 998
print("{0} {1}".format(k, factorial_rec(k)))
