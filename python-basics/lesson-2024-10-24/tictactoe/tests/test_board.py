import unittest
from unittest.mock import patch

# from src.board import display_board, welcome_message
from src import board, custom_ex


class TicTacToeBoardTest(unittest.TestCase):
    def test_welcome_message(self):
        # Arrange
        expected_message = "WELCOME TO TIC TAC TOA GAME"

        # Act
        result = board.welcome_message()

        # Assert
        self.assertEqual(expected_message, result)

    def test_display_board(self):
        # Arrange
        board_game = [None] * 9

        expected_display = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------"""

        result = board.display_board(board_game)

        self.assertEqual(expected_display, result)

    @patch("src.board.input")
    def test_player_asked_name(self, input_mock):
        # TODO: test a function that will ask a player his name
        # Arrange
        player_number = 1
        # Act
        name = board.ask_player_name(player_number)
        # Player 1, enter your name:
        # Player 2, enter your name:

        # Test that the input was called once with the right message
        input_mock.assert_called_once_with(f"Player {player_number}, enter your name: ")

    def test_update_board_success(self):
        # Arrange
        initial_board: list[None | str] = [
            None,
            "X",
            "O",
            None,
            None,
            None,
            "X",
            None,
            None,
        ]
        cell_selected: int = 4
        player_number: int = 2
        expected_board = [None, "X", "O", "O", None, None, "X", None, None]

        # Act
        result = board.update_board(initial_board, cell_selected, player_number)

        self.assertEqual(result, expected_board)

    def test_update_board_out_of_range(self):
        # Arrange
        initial_board: list[None | str] = [
            None,
            "X",
            "O",
            None,
            None,
            None,
            "X",
            None,
            None,
        ]
        cell_selected: int = 10  # out of range
        player_number: int = 2

        with self.assertRaises(custom_ex.CellOutOfBoundError):
            board.update_board(initial_board, cell_selected, player_number)

    def test_display_updated_board(self):
        initial_board = ["X", "O", "O", "X", None, None, "O", None, None]
        expected_display = """
-------------
| X | O | O |
-------------
| X | 5 | 6 |
-------------
| O | 8 | 9 |
-------------"""
        result = board.display_board(initial_board)

        self.assertEqual(result, expected_display)

    def test_is_winner_true(self):
        initial_board = ["X", "X", "X", None, "O", "O", None, None, None]
        player_number = 1

        result = board.is_winner(player_number, initial_board)

        self.assertTrue(result)
