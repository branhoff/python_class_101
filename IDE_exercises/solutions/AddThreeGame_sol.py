# Author: Brandon Hoffman
# Date: 11/15/2020
# Description: The class AddThreeGame that allows two players to play a game 
#              in which they alternately choose numbers from 1-9. They may not choose a number 
#              that has already been selected by either player. If at any point exactly three 
#              of the player's numbers sum to 15, then that player has won. 
#              If all numbers from 1-9 are chosen, but neither player has won, 
#              then the game ends in a draw.


class AddThreeGame:
    """
    The class AddThreeGame that allows two players to play a game 
    in which they alternately choose numbers from 1-9. They may not choose a number 
    that has already been selected by either player. If at any point exactly three 
    of the player's numbers sum to 15, then that player has won. 
    If all numbers from 1-9 are chosen, but neither player has won, 
    then the game ends in a draw.
    """

    def __init__(self):
        """
        intializes 4 private variables to be used throughout the Class
        """
        self._nums_chosen = []
        self._current_state = "UNFINISHED"
        self._player_turn = "first"
        self._player_score = 0


    def get_current_state(self):
        """
        get method to allow user to see the state of the game.
        Input: VOID
        Output: Should return string either: "UNFINISHED", "FIRST_WON", "SECOND_WON", or "DRAW"
        """
        return self._current_state

    def get_player_turn(self):
        """
        returns player turn private variable
        """
        return self._player_turn
        
    def get_player_choices(self):
        """
        returns array of player choices for first or second player, depending on instance of player turn
        """
        if self._player_turn == "first":
            n = 0
        elif self._player_turn == "second":
            n = 1

        return self._nums_chosen[n::2]

    def _set_current_state(self):
        """
        private method that will update the current state depending on the state of the
        most current score and which player's turn it is
        """
        if self._check_score(self.get_player_choices()):
            self._current_state = self.get_player_turn().upper() + '_' + 'WON'
        
        elif len(self._nums_chosen) == 9:
            self._current_state = 'DRAW'

    def _set_player_turn(self):
        """
        private method to change the _player_turn variable to the next player
        """
        if self._player_turn == "first":
            self._player_turn = "second"
        
        else:
            self._player_turn = "first"

    def _check_score(self, arr):
        if len(arr) < 3:
            return False
        
        choices = set(arr)
        for i in range(len(arr) -1):
            for j in range(i + 1, len(arr)):
                solution = 15 - (arr[i] + arr[j])
            
            if solution in choices and solution not in [arr[i], arr[j]]:
                return True
            else:
                return False

    def make_move(self, player, num_choice):
        """
        public method that allows players to interact with the game
        Input: takes a player variable either "first" or "second" and an integer from 1-9
        Output: Returns True if rules of game are met.
        """
        if self._current_state != "UNFINISHED":
            return False
        
        if player != self._player_turn:
            return False
            
        if 9 < num_choice or num_choice < 1:
            return False

        if num_choice in self._nums_chosen:
            return False

        else:
            self._nums_chosen.append(num_choice)
            self._set_current_state()
            self._set_player_turn()
            
            return True