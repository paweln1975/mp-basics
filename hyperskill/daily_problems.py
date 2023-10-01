import time
from datetime import datetime


# definition of the class
class House:
    construction = "building"
    elevator = True


def time_diff(h2, m2, s2, h1, m1, s1):
    start = str(h1) + ":" + str(m1) + ":" + str(s1)
    end = str(h2) + ":" + str(m2) + ":" + str(s2)

    time1 = datetime.strptime(start, "%H:%M:%S")
    time2 = datetime.strptime(end, "%H:%M:%S")

    return (time2 - time1).total_seconds()


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
