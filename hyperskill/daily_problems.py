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


def authenticate():
    pass


def print_book_info(title, author=None, year=None):
    disp_auth = "" if author is None else " by " + author
    disp_year = "" if year is None else " in " + str(year)
    disp_was_written = "" if author is None and year is None else " was written"
    value = "\"{title_}\"{was_written_}{by_}{in_}".format(title_=title, was_written_=disp_was_written,
                                                          by_=disp_auth, in_=disp_year)
    print(value)
    return value


def arithmetic_mean():
    numbers = [5, -7, 6, 2, 5, 5, -7, -10]
    sum_n = 0
    for x in numbers:
        sum_n += x
    return sum_n / len(numbers)


def while_loop_55() -> (int, int, int):
    numbers = [5, -7, 6, 2, 5, 5, -7, -10, 55, 1]
    numbers.reverse()
    x = numbers.pop()
    n = 0
    sum_n = 0
    while x != 55:
        sum_n = sum_n + x
        n += 1
        x = numbers.pop()
    return n, sum_n, round(sum_n / n)


def print_colors():
    colors = ["red", "yellow"]
    for color in colors:
        if color == "black":
            break
        elif color == "white":
            continue
        else:
            print(color)
    else:    # this else executed only when no break was executed
        print("Look at all those colors!")


def print_cons_vowel(input_text: str):
    vowels = 'aeiou'
    for c in input_text:
        if c in vowels:
            print("vowel")
        elif not c.isalpha():
            break
        else:
            print("consonant")


def print_location_cartesian(x: int, y: int):
    if x > 0 and y > 0:
        print("I")
    elif x < 0 < y:
        print("II")
    elif x < 0 and y < 0:
        print("III")
    elif x > 0 > y:
        print("IV")
    elif x == 0 and y == 0:
        print("It's the origin!")
    else:
        print("One of the coordinates is equal to zero!")


def print_if_box_can_be_carried(A, B, C, X, Y):
    str_ok = "The box can be carried"
    str_not_ok = "The box cannot be carried"
    result = False
    if X >= A and Y >= B:
        result = True
    elif X >= A and Y >= C:
        result = True
    elif X >= B and Y >= C:
        result = True
    else:
        result = False

    if result:
        print(str_ok)
    else:
        print(str_not_ok)


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

    # print arithmetic mean
    print(arithmetic_mean())
    x, y, z = while_loop_55()
    print(x)
    print(y)
    print(z)

    # print colors
    print_colors()

    # print vowels
    print_cons_vowel("abc def")

    # print cartesian location
    print_location_cartesian(1, 1)
    print_location_cartesian(-1, 1)
    print_location_cartesian(-1, -1)
    print_location_cartesian(1, -1)
    print_location_cartesian(0, 1)
    print_location_cartesian(1, 0)
    print_location_cartesian(0, 0)

    # print box
    print_if_box_can_be_carried(24, 21, 11, 36, 80)
    print_if_box_can_be_carried(80, 50, 80, 33, 78)
