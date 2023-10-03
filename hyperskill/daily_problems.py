import time
from datetime import datetime


# definition of the class
class House:
    construction = "building"
    elevator = True


# diff between two hours
def time_diff(h2, m2, s2, h1, m1, s1):
    start = str(h1) + ":" + str(m1) + ":" + str(s1)
    end = str(h2) + ":" + str(m2) + ":" + str(s2)

    time1 = datetime.strptime(start, "%H:%M:%S")
    time2 = datetime.strptime(end, "%H:%M:%S")

    return (time2 - time1).total_seconds()


def mystery_function(x):
    result = []
    for i in range(x):
        result.append(i)
        if i % 2 == 0:
            result.pop()
    return result


def identity_function(value):
    x = value
    y = value
    print("Identity for {}".format(value))
    print(id(x))
    print(id(y))


def print_book_info(title, author=None, year=None):
    disp_auth = "" if author is None else " by " + author
    disp_year = "" if year is None else " in " + str(year)
    disp_was_written = "" if author is None and year is None else " was written"
    value = "\"{title_}\"{was_written_}{by_}{in_}".format(title_=title, was_written_=disp_was_written,
                                                          by_=disp_auth, in_=disp_year)
    print(value)
    return value


if __name__ == '__main__':
    # object of the class House
    new_house = House()
    print(time.ctime())

    # the following line reads the string to work with from the input, do not modify it, please
    # input_str = input()
    input_str = 'python str'

    # convert to list
    print(list(input_str))

    # last element from the list
    print(input_str[-1])

    # verify mystery function
    output = mystery_function(5)
    print(output)

    # identity
    identity_function(5)
    identity_function(-5)
    identity_function(-6)
    identity_function(1000)

    # print book
    print_book_info("War and Peace", "Leo Tolstoy", 1869)
    print_book_info("War and Peace", "Leo Tolstoy")
    print_book_info("War and Peace", None, 1869)
    print_book_info("War and Peace")
