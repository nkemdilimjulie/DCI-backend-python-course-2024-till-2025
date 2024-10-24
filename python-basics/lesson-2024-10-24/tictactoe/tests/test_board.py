import unittest

from src.board import display_board, welcome_message


class TicTacToeBoardTest(unittest.TestCase):
    def test_welcome_message(self):
        # Arrange
        expected_message = "WELCOME TO TIC TAC TOA GAME"

        # Act
        result = welcome_message()

        # Assert
        self.assertEqual(expected_message, result)

    def test_display_board(self):
        # Arrange
        board = [None] * 9

        expected_display = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------"""

        result = display_board(board)

        self.assertEqual(expected_display, result)

    def test_player_asked_name(self):
        # TODO: test a function that will ask a player his name
