# Tic Tac Toe Game

## Requirement
- The game will start with 3 by 3 square grid with 9 cells
- They will be two players who will take turns marking `X`, and `O` in the cells
- A player wins by placing their mark in any three squares in a straight, horizontal, vertical or diagonal line.
- The game ends if
    - A player wins
    - All the 9 cells have be filled up with marks


## TDD
### Start of the game
- I want to see a welcome message
- I want to see an empty board labelled from 1 to 9
- Players are asked to give their names

### Playing the game
- This will be in a loop
    - Each player is asked to select a cell
    - The board is updated after the player selects a valid cell
    - Check if player won
        - If player won, print congratulations message and quit the game
    - if all cells are filled up
        - print 'No winner!', and quit the game