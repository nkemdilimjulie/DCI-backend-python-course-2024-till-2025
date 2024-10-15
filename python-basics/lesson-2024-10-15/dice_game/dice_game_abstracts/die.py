## Get object representation

from abc import ABC, abstractmethod


class Die(ABC):
    def __init__(self) -> None:
        self.face: int  # Here we are just declaring that the face will be an integer
        self.roll()

    @abstractmethod
    def roll(self) -> None: ...

    def __str__(self) -> str:
        # String representation # Works with print()
        return f"{self.face}"

    def __repr__(self) -> str:
        #  Get object representation # Works without print()
        return f"{self.face}"
