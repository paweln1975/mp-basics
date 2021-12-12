class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


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