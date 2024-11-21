from .dice import D4, D6, D8, D10
from .dice_board import DiceBoard
from .dummy_dice_game import DummyDiceGame


def main():
    start_player_dice = ["D4", "D6", "D8"]
    player_dice_count = len(start_player_dice)
    player_max_dice_count = 4

    player_name = input("Player, please, state your name: ")
    print("*" * 10)
    print(f"Game will start with {player_dice_count} dice: {start_player_dice}")
    print("Winning rule: Faces of all dice are the same!!!")

    if input("Do you want to add D10? Replay with yes/no: ") == "yes":
        dice_board = DiceBoard(D4, D6, D8, D10)
        player_dice_count += 1
    else:
        dice_board = DiceBoard(D4, D6, D8)

    game = DummyDiceGame(dice_board, player_name)

    print("Dice combination: ", game.dice)

    if game.check_winner():
        print(f"Winner! Congratulations {player_name}")
        print(f"Total points:  {game.total_points}")
        return
    else:
        print("Sorry ! Try again")

    while game.roll_trials:
        # run while the condition in the while loop is True
        print(f"{game.roll_trials} trials left")
        roll_pos = []
        added_dice = False
        if player_dice_count < player_max_dice_count:
            print(
                f"Game will continue with {player_dice_count} of dice: {start_player_dice}"
            )
            print("You will have more points if you add D10")

            if input("Do you want to add D10? yes/no: ") == "yes":
                game.add_dice(D10)
                player_dice_count += 1
                start_player_dice += ["D10"]
                added_dice = True

        if not added_dice:
            if input("Do you want to roll specific dice? yes/no") == "yes":
                roll_pos = input(
                    f"Select which die or dice to roll from {game.dice} (separate each index by space)"
                )
                roll_pos = [int(pos) for pos in roll_pos.split()]  # '0 2' -> ['0', '2']

            game.roll(roll_pos)

        print("Dice combination: ", game.dice)

        if game.check_winner():
            print(f"Winner! Congratulations {player_name}")
            print("Total Points: ", {game.total_points})
            break
        else:
            print("Sorry! Try again")
    else:
        print("You have exhausted all your trials")


if __name__ == "__main__":
    main()
