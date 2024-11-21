from random import randint

from .dice_game_abstracts.die import Die


class D4(Die):
    def roll(self):
        self.face = randint(1, 4)


class D6(Die):
    def roll(self):
        self.face = randint(1, 6)


class D8(Die):
    def roll(self):
        self.face = randint(1, 8)


class D10(Die):
    def roll(self):
        self.face = randint(1, 10)
