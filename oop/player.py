class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3

    def __str__(self):
        return "Name: {0.name} Lives: {0.lives}".format(self)

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            raise ValueError("Lives cannot be negative!")

    lives = property(_get_lives, _set_lives, doc="Number of lives")
    # data attribute cannot have the same name as property


p = Player("Tim")
p.lives = 10
print(p)

