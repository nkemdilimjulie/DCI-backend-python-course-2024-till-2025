from src import board


def main():
    # define an empty board
    game_board: list[None | str] = [None] * 9

    print(board.welcome_message())
    print(board.display_board(game_board))
    print("*" * 20)

    player_one: str = board.ask_player_name(1)
    player_two: str = board.ask_player_name(2)

    player_number_bool: bool = True  # player 1

    while True:
        player_name: str = player_one if player_number_bool else player_two
        player_count: int = int(not player_number_bool) + 1

        player_cell: int = int(input(f"Player {player_name} choose a cell: "))
        # I need a function to update the board.
        game_board = board.update_board(game_board, player_cell, player_count)

        # Display the updated board
        print(board.display_board(game_board))

        if board.is_winner(player_count, game_board):
            print(f"Game over, Player {player_name} winner!!!!")
            break

        # TODO: Check if the board is full, then stop the game

        player_number_bool = not player_number_bool


if __name__ == "__main__":
    main()
