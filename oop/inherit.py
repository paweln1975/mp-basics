class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    def __init__(self, name, lenght):
        super().__init__(name, lenght)

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    pass


class Drinks:
    pass


class Pastry:
    pass


class Sweets:
    pass


class Chocolate(Sweets):
    pass


def find_the_parent(child):
    if issubclass(child, (Drinks, Pastry, Sweets)):
        print(child.__bases__[0].__name__)


# create an instance of Tesla
tesla_car = Tesla("C60", "red")
seine = River("Seine", 777)

find_the_parent(Chocolate)

print(issubclass(River, (River, Tesla)))
