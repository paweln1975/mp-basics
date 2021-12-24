import random

class Enemy(object):

    def __init__(self, name: str, level: int = 1, damage: int = 23):
        self.name = name
        self._lives = 3
        if level <= 0:
            raise ValueError("Level must be positive!")
        self._level = level
        self._damage = damage
        self.alive = True
        print(f"Enemy init: {self}")

    def __str__(self):
        return "Name: {0.name} Lives: {0.lives} Level: {0.level} Damage: {0.damage}".format(self)

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
            self._level = level
        else:
            raise ValueError("Level cannot be negative or zero!")

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    lives = property(_get_lives, _set_lives, doc="Number of lives")
    level = property(_get_level, _set_level, doc="Level value")
    # data attribute cannot have the same name as property

    def take_damage(self, damage: int):
        if self._damage > damage:
            self._damage -= damage
        else:
            self.lives -= 1
            if self.lives == 0:
                self.alive = False
                print("{0.name} is dead".format(self))


class Troll(Enemy):

    def __init__(self, name: str):
        super().__init__(name)
        print(f"Troll init {self}")


class Vampire(Enemy):

    def __init__(self, name: str):
        super().__init__(name, level=1, damage=13)
        print(f"Vampire init {self}")

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"{self} successfully dodges")
            return True
        return False

    def take_damage(self, damage: int):
        if not self.dodges():
            super().take_damage(damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super(VampireKing, self).__init__(name)
        self._damage = 140

    def take_damage(self, damage: int):
        super().take_damage(damage // 4)


t = Troll("Troll")
print(t)
e = Enemy("Boris")
print(e)
v = Vampire("Dracula")
print(v)
v.take_damage(50)
v.take_damage(45)
while v.alive:
    v.take_damage(1)
    print(v)
vk = VampireKing("King")
vk.take_damage(100)
print(vk)