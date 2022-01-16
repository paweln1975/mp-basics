def test_star(*args: int) -> None:  # packs as a tuple
    print(args, sep=":")
    for x in args:
        print(x)


def func(p1, p2, *args, k, **kwargs) -> None:
    print("positional-or-keyword: {}, {}".format(p1, p2))
    print("var-positional: {}".format(args))
    print("keyword: {}".format(k))
    print("var-keyword: {}".format(kwargs))


def sum_numbers(*args) -> float:
    """
    Sum argument values
    :param args: Numbers to sum
    :return: A value of arguments sum
    """
    result = 0
    for arg in args:
        result += arg
    print("Sum of values: {}".format(result))
    return result


def print_backward(*args, end=' ', **kwargs):
    # *args unpacks arguments into a tuple, **kwargs unpacks var keyword arguments
    # into a dictionary
    kwargs.pop("end", None)
    print(f"Kwargs={kwargs}")
    for word in args[::-1]:
        print(word, end=' ', **kwargs)


numbers = (1, 2, 3, 4, 5, 6)

print(numbers, sep=";")
print(*numbers, sep=";")
test_star(1, 2, 3)
test_star()

func(1, 2, 3, 4, 9, k=6, key1=7, key2=8)
sum_numbers(1, 2, 3)
sum_numbers(8, 20, 2)
sum_numbers(12.5, 3.147, 98.1)
sum_numbers()
sum_numbers(0)

print_backward("hello", "world", "sun", "planet", end="", sep=":")
