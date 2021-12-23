class Enemy(object):

    def __init__(self, name: str, level: int = 1):
        self.name = name
        self._lives = 3
        if level <= 0:
            raise ValueError("Level must be positive!")
        self._level = level
        self._damage = 100 * level

    def __str__(self):
        return "Name: {0.name} Lives: {0.lives} Level: {0.level} Score: {0.damage}".format(self)

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
            self._damage += (level-self._level) * 500
            self._level = level
        else:
            raise ValueError("Level cannot be negative or zero!")

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, score):
        self._damage = score

    lives = property(_get_lives, _set_lives, doc="Number of lives")
    level = property(_get_level, _set_level, doc="Level value")
    # data attribute cannot have the same name as property


class Troll(Enemy):
    pass


t = Troll("Troll")
print(t)
e = Enemy("Boris")
print(e)
