from typing import Type

from .dice_board import DiceBoard
from .dice_game_abstracts.dice_game import DiceGameBase
from .dice_game_abstracts.die import Die


class DummyDiceGame(DiceGameBase):
    def __init__(self, dice_board: DiceBoard, player_name: str):
        self._dice_board = dice_board
        self._player_name = player_name
        self.roll_trials = 5

    def check_winner(self):
        return self._dice_board.is_winner()

    def roll(self, pos: list[int]):
        if self.roll_trials <= 0:
            raise OperationalError("You have exhausted your roll trials")

        if pos:
            self._dice_board.to_be_rolled(pos).roll_all_dice()
        else:
            self._dice_board.roll_all_dice()

        # reduce roll trials
        self.roll_trials -= 1

    def add_dice(self, dice_class: Type[Die]):
        self._dice_board = self._dice_board + dice_class

    @property
    def total_points(self):
        return self._dice_board.total

    @property
    def dice(self):
        return self._dice_board.dice
