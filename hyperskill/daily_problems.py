import time
import math
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
    else:  # this else executed only when no break was executed
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


def print_formatter_float(input_float, precision):
    str_to_format = "{:." + str(precision) + "f}"

    print(str_to_format.format(input_float))


def find_number(input_list_str: str, searched_num: int) -> str:
    input_list = input_list_str.split(sep=' ')
    output_list = [str(index) for index, item in enumerate(input_list) if item == str(searched_num)]
    return ' '.join(output_list) if output_list else 'not found'


def dict_check(input_list_str: str) -> str:
    dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
                  'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
                  'sign', 'the', 'to', 'uncertain']
    input_list = input_list_str.split(sep=' ')
    list_missing = [item for item in input_list if item not in dictionary]
    return '\n'.join(list_missing) if list_missing else 'OK'


def closest_higher_mod_5(x):
    for i in range(0, 5):
        remainder = (x + i) % 5
        if remainder == 0:
            return x + i
    return "I don't know :("


def create_url(host='localhost', port=443):
    return "https://{}:{}".format(host, str(port))


def heading(text, level=1):
    if level < 1:
        level = 1
    elif level > 6:
        level = 6

    return "#" * level + " " + text


def code(language='Python'):
    print("We code in {language}".format(language=language))


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        return ((3 * math.sqrt(3) * self.side_length * self.side_length / 2) * 1000) / 1000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return math.sqrt(math.pow(self.x - p2.x, 2) + math.pow(self.y - p2.y, 2))


class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, dest):
        return "The {name} has sailed for {dest}!".format(name=self.name, dest=dest)


class House1:
    def __init__(self, floors):
        self.floors = floors
        self.color = None

    # create the method here
    def paint(self, color):
        self.color = color


class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return "Object of the class Patient. name: {name}, last_name: {last_name}, age: {age}"\
            .format(name=self.name, last_name=self.last_name, age=self.age)

    def __str__(self):
        return "{name} {last_name}. {age}" \
            .format(name=self.name, last_name=self.last_name, age=self.age)

    def __new__(cls, name, last_name, age):
        return object.__new__(cls)


class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)


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

    print_formatter_float(1 / 2, 3)

    # join/split
    print(find_number('5 8 2 7 8 8 2 4', 8))

    print(dict_check('srutinize is to examene closely and minutely'))
    print(dict_check('all correct'))

    # closest to x divided by 5
    print(closest_higher_mod_5(40))
    print(closest_higher_mod_5(43))

    print(heading("A"))

    # Hexagon
    print(Hexagon(1).get_area())

    # print distance
    p1 = Point(1.5, 1)
    p2 = Point(1.5, 2)

    print(p1.dist(p2))

    n = 10
    p = Person(n)
    print(p.greet())

    black_pearl = Ship("Black Pearl", 800)
    print(black_pearl.sail("No way"))


