def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be negative")
    retvalue = 1
    if n > 1:
        for k in range(2, n+1):
            retvalue *= k
    return retvalue


def recursive_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be negative")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(0, 10):
    print(f"{i}: {factorial(i)}")

for i in range(0, 10):
    print(f"{i}: {recursive_factorial(i)}")