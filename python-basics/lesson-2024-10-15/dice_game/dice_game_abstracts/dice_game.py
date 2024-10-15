from abc import ABC, abstractmethod
from typing import Type

from .die import Die


class DiceGameBase(ABC):
    def __init__(self):
        self._dice_board: "DiceBoard"
        self._player_name: str
        self._roll_trials: int

    @abstractmethod
    def check_winner(self): ...

    @abstractmethod
    def roll(self): ...

    @abstractmethod
    def add_dice(self, die_class: Type[Die]): ...

    @property
    @abstractmethod
    def total_points(self): ...
