"""
class vs instance attributes training
>>> import sys; sys.tracebacklimit = 0
>>> modify()
0

>>> s = Sphere(10)
>>> s.volume
4188.666666666666

>>> greg = Fish("Greg", "guppy")
>>> greg.n_fish
1

>>> clownfish = Fish("Nemo", "clownfish")
>>> clownfish.n_fish
2
"""
class MusicalInstrument:
    n_instruments = 0  # number of instruments

    def __init__(self, name, group):
        self.name = name
        self.group = group


def modify():
    drums = MusicalInstrument("drums", "percussion")
    triangle = MusicalInstrument("triangle", "percussion")
    violin = MusicalInstrument("violin", "string instr.")
    flute = MusicalInstrument("flute", "woodwind instr.")

    drums.n_instruments += 1
    triangle.n_instruments += 1
    violin.n_instruments += 1
    flute.n_instruments += 1

    return MusicalInstrument.n_instruments


class Sphere:
    PI = 3.1415
    def __init__(self, radius):
        self.radius = radius
        self.volume = 4/3 * Sphere.PI * radius**3


class Fish:
    place = "aquarium"
    n_fish = 0  # number of fish in the aquarium

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        Fish.n_fish += 1


