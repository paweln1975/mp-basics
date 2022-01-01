import sys
print(f"Recursion limit {sys.getrecursionlimit()}")


def recursion_test(n: int = 100):
    if n < 0:
        raise ValueError("Value is not allowed to be negative")
    if n == 0:
        return True
    else:
        recursion_test(n-1)


# noinspection PyBroadException
try:
    recursion_test(-1)
except Exception as error:
    print("Error:{}".format(error))

try:
    x = 10 / 1
    recursion_test(1000)
except (ZeroDivisionError, RecursionError) as error:
    print(f"Error: {error}")


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError as error:
            print("Invalid number")
        except EOFError:
            print("OK. Exiting")
            sys.exit(0)


first = getint("Enter a=")
second = getint("Enter b=")
try:
    print(f"{first}/{second}={first/second}")
except ZeroDivisionError:
    print("Division by 0")
else:   # only when there was no exception
    print("Else executed")
finally:
    print("Finished")
