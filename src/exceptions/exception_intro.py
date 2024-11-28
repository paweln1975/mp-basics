"""
Exceptions training
>>> import sys; sys.tracebacklimit = 0
>>> recursion_test(-1)
Traceback (most recent call last):
ValueError: Value is not allowed to be negative

>>> divide(10, 5)
2.0

>>> divide(10, 0)
Traceback (most recent call last):
ZeroDivisionError: division by zero

>>> get_names('Anthony Stark')
'Welcome to our party, Anthony Stark'

>>> get_names('Steven Rogers Captain America')
'You need to enter exactly 2 words. Try again!'

>>> check_integer(8)
Traceback (most recent call last):
exception_intro.NotInBoundsError: There is an error! Value 8 is not allowed to be outside 45 and 67!

>>> error_handling(8)
There is an error! Value 8 is not allowed to be outside 45 and 67!

>>> error_handling(50)
50

"""
import sys

print(f"Recursion limit {sys.getrecursionlimit()}")


def recursion_test(n: int = 100):
    if n < 0:
        raise ValueError("Value is not allowed to be negative")
    if n == 0:
        return True
    else:
        recursion_test(n - 1)


def divide(a, b):
    while True:
        try:
            number = a / b
            return number
        except ValueError as error:
            print("Invalid number")
        except EOFError:
            print("OK. Exiting")
            sys.exit(0)


def get_names(space_separated: str) -> str:
    try:
        name, surname = space_separated.split(" ")
    except ValueError:
        return "You need to enter exactly 2 words. Try again!"
    return f"Welcome to our party, {name} {surname}"


class NotInBoundsError(Exception):
    def __init__(self, lower_bound, upper_bound, current):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current = current
        super().__init__(f"There is an error! Value {current} is not allowed "
                         f"to be outside {lower_bound} and {upper_bound}!")

def check_integer(num):
    if 45 < num < 67:
        return num
    else:
        raise NotInBoundsError(45, 67, num)

def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as e:
        print(str(e))
        return
    return num