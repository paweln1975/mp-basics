class Player(object):

    def __init__(self, name: str, level: int = 1):
        self.name = name
        self._lives = 3
        if level <= 0:
            raise ValueError("Level must be positive!")
        self._level = level
        self._score = 1000 * level

    def __str__(self):
        return "Name: {0.name} Lives: {0.lives} Level: {0.level} Score: {0.score}".format(self)

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            raise ValueError("Lives cannot be negative or zero!")

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 0:
            self._score += (level-self._level) * 1000
            self._level = level
        else:
            raise ValueError("Level cannot be negative or zero!")

    def increase_level(self):
        self.level += 1

    def decrease_level(self):
        self.level -= 1

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    lives = property(_get_lives, _set_lives, doc="Number of lives")
    level = property(_get_level, _set_level, doc="Level value")
    # data attribute cannot have the same name as property


p = Player("Tim")
p.lives = 10
print(p)
p.increase_level()
print(p)
p.level = 5
print(p)
p.level = 3
print(p)
p.decrease_level()

