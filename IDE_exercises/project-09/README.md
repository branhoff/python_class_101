# project-9

Write a class called AddThreeGame that allows two players to play a game in which they alternately choose numbers from 1-9.  They may not choose a number that has already been selected by either player.  If at any point exactly three of the player's numbers sum to 15, then that player has won.  If all numbers from 1-9 are chosen, but neither player has won, then the game ends in a draw.

The class will need **private** data members for:
1. keeping track of which numbers have been chosen, and by whom
2. the current state, which holds one of the four following values: "FIRST_WON", "SECOND_WON", "DRAW", or "UNFINISHED"
3. keeping track of whose turn it is

Your AddThreeGame class must include the following methods:
* An init method that takes no parameters and initializes all data members.
* A get method named get_current_state, which returns the current state.
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
