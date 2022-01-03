# project-09

Write a Python class named AddThreeGame that has two players to play a game in which they alternately choose numbers from 1-9. The number cannot be selected if one of the player already selected it and if at any point exactly three of the player's numbers sum to 15, then that player has won.  
If all numbers from 1-9 are chosen, but neither player has won, then the game ends in a draw.

The class will need **private** variables for:
1. keeping track of chosen number, and by whom
2. the current state, which holds one of the four following values: "FIRST_WON", "SECOND_WON", "DRAW", or "UNFINISHED"
3. keeping track of whose turn it is

Your AddThreeGame class must include the following methods:
* An init method to initialize the players without any parameters.
* A get method named get_current_state to return the current state of the game.
* A method named make_move that takes two parameters - a string designating the player making the move, either "first" or "second", and an integer giving their number choice (in that order).  If it is not that player's turn, or if the integer is not in the correct range, or if that integer has already been chosen, or if the game has already been won or drawn, make_move should return False.  Otherwise, it should record the move, update the current state if the move caused a win or draw, update which player's turn it is, and return True.

For example, your class could be used as follows:
```
game = AddThreeGame()
game.make_move("first", 2)
game.make_move("second", 5)
result = game.make_move("first", 7)
state = game.get_current_state()
```
Your file should be named: AddThreeGame.py
