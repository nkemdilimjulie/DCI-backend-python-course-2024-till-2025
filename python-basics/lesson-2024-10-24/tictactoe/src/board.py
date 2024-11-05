from src import custom_ex


def welcome_message():
    return "WELCOME TO TIC TAC TOA GAME"


def display_board(board: list[None | str]):
    # TODO: Improve on this
    cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9 = board

    return f"""
-------------
| {cell1 if cell1 else '1'} | {cell2 if cell2 else '2'} | {cell3 if cell3 else '3'} |
-------------
| {cell4 if cell4 else '4'} | {cell5 if cell5 else '5'} | {cell6 if cell6 else '6'} |
-------------
| {cell7 if cell7 else '7'} | {cell8 if cell8 else '8'} | {cell9 if cell9 else '9'} |
-------------"""


def ask_player_name(player_number):
    return input(f"Player {player_number}, enter your name: ")


def update_board(board, cell_selected, player_number):
    # TODO: What happens if a player selects a cell that is already taken.
    # If that happens, let's raise a nice custom exception

    cell_position = cell_selected - 1

    mark: str = "X" if player_number == 1 else "O"

    try:
        board[cell_position] = mark
        return board
    except IndexError:
        raise custom_ex.CellOutOfBoundError


def is_winner(player_number, board):
    # TODO: Improve on this
    # ("PPP.....") # [0, 1, 2]
    # ("...PPP...") # [3, 4, 5]
    # ("......PPP") # [6, 7, 8]
    # ("P..P..P..") # [0, 3, 6]
    # (".P..P..P.") # [1, 4, 7]
    # ("..P..P..P") # [2, 5, 8]
    # ("P...P...P") # [0, 4, 8]
    # (..P.P.P..) # [2, 4, 6]

    win_boards = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    player_mark = "X" if player_number == 1 else "O"

    for i, j, k in win_boards:
        if board[i] == board[j] == board[k] == player_mark:
            return True
    else:
        return False
