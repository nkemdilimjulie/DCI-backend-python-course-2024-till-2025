from copy import deepcopy
from typing import Type

from .dice_game_abstracts.die import Die


class DiceBoard:
    # Type[Die] means it will be a class that has as parent Die
    def __init__(self, *die_classes: Type[Die]):
        self.__dice: list[Die] = [die() for die in die_classes]
        self.rolled_pos: set(int) = set()

    def to_be_rolled(self, pos):
        # Check to make sure all the positions given falls in the range
        if all(0 <= p < len(self.__dice) for p in pos):
            self.rolled_pos = set(pos)
        else:
            raise ValueError("Invalid Dice Positions")

        return self  # To enable chain call.

    def roll_all_dice(self):
        # This method will roll all the dice

        if self.rolled_pos:
            # If possition was set, then roll only dice at that position
            for pos in self.rolled_pos:
                self.__dice[pos].roll()

            self.rolled_pos = set()
        else:
            # Else, roll all dice
            for die in self.dice:
                die.roll()

    def is_winner(self) -> bool:
        return len(set(die.face for die in self.__dice)) == 1

    def __add__(self, die: Type[Die]):
        # Check if 'die' is a class and it is a child of 'Die'
        if isinstance(die, type) and issubclass(die, Die):
            new_self = deepcopy(self)

            new_self.__dice += [die()]
            return new_self
        else:
            raise NotImplementedError

    @property  # GETTER
    def dice(self):
        return self.__dice

    @dice.setter
    def dice(self, value):
        raise NotImplementedError

    # TODO: Create a property called `total` that will return the total sum of all dice faces
    @property
    def total(self):
        return sum(die.face for die in self.dice)
