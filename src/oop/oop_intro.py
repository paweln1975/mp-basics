class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    @classmethod
    def from_string(cls, data: str):
        name, price = data.split(" ")
        return cls(name, float(price))

    def get_info(self) -> str:
        return self.make + f' (price: {self.price})'

    @property
    def full_name(self):
        return self.get_info()


kenwood = Kettle("Kenwood", 8.99)

hamilton = Kettle("Hamilton", 14.55)
hamilton.price = 17
hamilton.switch_on()
Kettle.switch_on(kenwood)

kenwood.power = 1.5  # bound to an instance of the class
print(kenwood.power)

print("Models: {} = {}, {} = {}".format(hamilton.make, hamilton.price, kenwood.make, kenwood.price))
print("Models: {0.make} = {0.price} ({0.on}), {1.make} = {1.price}  ({1.on})".format(hamilton, kenwood))

print(hamilton.__dict__)
hamilton.power_source = "atomic"
print(hamilton.__dict__)

Kettle.power_source = "coal"
print(Kettle.power_source, hamilton.power_source, kenwood.power_source)

kettle_1 = Kettle.from_string("Lidl 100.99")
print(kettle_1.get_info())
print(kettle_1.full_name)


class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    # use appropriate decorator
    @classmethod
    def from_string(cls, data):
        hour, minute = data.split(":")
        return cls(hour, minute)


class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    # use appropriate decorat
    @classmethod
    def from_string(cls, data):
        name, email = data.split("-")
        return cls(name, email)


class Area:

    def __init__(self, figure_name):
        self.figure_name = figure_name

    @staticmethod
    def rhombus_area(a, b):
        return float(a) * float(b) * 0.5
