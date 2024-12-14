"""
Enum library training
>>> import sys; sys.tracebacklimit = 0
>>> from enum import auto, Enum
>>> Color.RED.value
1
>>> Color.GREEN.value
2
>>> print(Color(1))
Color.RED
>>> print(Color['RED'])
Color.RED

>>> print_colors()
1 RED
2 GREEN
3 BLUE

>>> print(Direction.get_opposite_direction(Direction.NORTH))
Direction.SOUTH

>>> print(Direction.get_direction_name('N'))
NORTH

>>> get_temperature(15)
MODERATE
>>> get_temperature(20)
MODERATE
>>> get_temperature(30)
WARM
>>> get_temperature(35)
WARM
>>> get_temperature(-10)
FREEZING

>>> print(sorted(Fruit, key=lambda fruit: fruit.value))
[<Fruit.PINEAPPLE: 1>, <Fruit.BANANA: 2>, <Fruit.MANGO: 3>, <Fruit.ORANGE: 4>, <Fruit.APPLE: 5>]

>>> is_weekend(DaysOfWeek.SATURDAY)
True
>>> is_weekend(DaysOfWeek.SUNDAY)
True
>>> is_weekend(DaysOfWeek.MONDAY)
False
"""
from enum import auto, Enum
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    @staticmethod
    def get_opposite_direction(direction):
        match direction:
            case Direction.NORTH:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.NORTH
            case Direction.EAST:
                return Direction.WEST
            case Direction.WEST:
                return Direction.EAST
            case _:
                raise Exception("Unknown direction")

    @staticmethod
    def get_direction_name(direction):
        return Direction(direction).name

class Temperature(Enum):
    FREEZING = -5
    COLD = 10
    MODERATE = 25
    WARM = 35
    HOT = 40


def get_temperature(t: int)->Temperature:
    retValue = None
    match t:
        case t if t <= Temperature.FREEZING.value:
            retValue = Temperature.FREEZING
        case t if Temperature.FREEZING.value < t <= Temperature.COLD.value:
            retValue = Temperature.COLD
        case t if t > Temperature.COLD.value < t <= Temperature.MODERATE.value:
            retValue = Temperature.MODERATE
        case t if t > Temperature.MODERATE.value < t <= Temperature.WARM.value:
            retValue = Temperature.WARM
        case _:
            retValue = Temperature.HOT
    print(retValue.name)


def print_colors():
    for color in Color:
        print(color.value, color.name)

class Fruit(Enum):
    APPLE = 5
    MANGO = 3
    BANANA = 2
    ORANGE = 4
    PINEAPPLE = 1

class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def is_weekend(day):
    return day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY]