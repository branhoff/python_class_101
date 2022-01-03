# Author: Brandon Hoffman
# Date: 11/25/2020
# Description:     A class called BuildersGame that represents the board for a two-player game (Player X and Player O) that is played on a 5x5 grid. 
#                  During the game, each players' builders will move around the board and add levels to towers. The winner is the 
#                  first one to move a builder on top of a 3-story tower.


class BuildersGame:
    """
    BuildersGame represents the board for a two-player game (Player X and Player O) that is played on a 5x5 grid. 
    During the game, each players' builders will move around the board and add levels to towers. The winner is the 
    first one to move a builder on top of a 3-story tower.
    """

    def __init__(self):
        """
        intializes 12 private variables to be used throughout the Class
        _current_state represents the state game as "UNFINISHED", "X_WON, "O_WON"
        _board is a list of lists storing the tower height of the game
        _x1_position is a tuple showing the row and column numbers on the board. first piece for player X
        _x2_position is a tuple showing the row and column numbers on the board. second piece for player X
        _o1_position is a tuple showing the row and column numbers on the board. first piece for player O
        _o2_position is a tuple showing the row and column numbers on the board. second piece for player O

        _x1_height, _x2_height, _o1_height, _o2_height return the current, respective position on the board's height
        _player_turn holds a string representing whether it is player X's or player O's turn. Used for conditionals to confirm proper turns are taken
        _turn_count tracks the number of turns completed without error. This will help us know if the program should expect the players to intiate their
        pieces or just do their regular turns
        """

        self._current_state = "UNFINISHED"
        self._board = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]

        self._x1_position = (0, 0)
        self._x2_position = (0, 0)
        self._o1_position = (0, 0)
        self._o2_position = (0, 0)

        self._x1_height = self._board[self._x1_position[0]][self._x1_position[1]]
        self._x2_height = self._board[self._x2_position[0]][self._x2_position[1]]
        self._o1_height = self._board[self._o1_position[0]][self._o1_position[1]]
        self._o2_height = self._board[self._o2_position[0]][self._o2_position[1]]

        self._player_turn = "x"
        self._turn_count = 1

    def print_board(self):
        """
        displays board for testing purposes
        """
        row = 0
        print("  ", 0, "", 1, "", 2, "", 3, "", 4,)
        for line in self._board:
            print(row, line)
            row += 1
        
        self._set_player_height()

        print()
        print("x1 piece:", self._x1_position, "height:", self._x1_height)
        print("x2 piece:", self._x2_position, "height:", self._x2_height)
        print("o1 piece:", self._o1_position, "height:", self._o1_height)
        print("o2 piece:", self._o2_position, "height:", self._o2_height)


    def _set_player_turn(self):
        """
        private method to change the _player_turn variable to the next player
        """
        if self._player_turn == "x":
            self._player_turn = "o"
        
        else:
            self._player_turn = "x"

    def _set_player_height(self):
        """
        private method that updates the private player height variables
        """
        self._x1_height = self._board[self._x1_position[0]][self._x1_position[1]]
        self._x2_height = self._board[self._x2_position[0]][self._x2_position[1]]
        self._o1_height = self._board[self._o1_position[0]][self._o1_position[1]]
        self._o2_height = self._board[self._o2_position[0]][self._o2_position[1]]


    def _check_player_turn(self, from_row, from_col):
        """
        returns a boolean of False if it's not the appropriate players turn
        """
        player_referenced = None
        if (from_row, from_col) in [self._x1_position, self._x2_position]:
            player_referenced = 'x'

        elif (from_row, from_col) in [self._o1_position, self._o2_position]:
            player_referenced = 'o'

        if player_referenced != self._player_turn:
            return False

    def get_current_state(self):
        """
        returns private _current_state variable
        """
        return self._current_state

    def _check_legal_range(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        returns False if row or column variable is less than 0 or greater than 4
        """
        if 4 < to_row or to_row < 0:
            return False

        elif 4 < to_col or to_col < 0:
            return False

        elif 4 < from_row or from_row < 0:
            return False

        elif 4 < from_col or from_col < 0:
            return False

        elif 4 < build_row or build_row < 0:
            return False

        elif 4 < build_col or build_col < 0:
            return False

    def _check_legal_move(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        returns False if a move taken is greater than 1 in the respective column or row variable
        """
        if abs(from_row - to_row) > 1:
            return False

        elif abs(from_col - to_col) > 1:
            return False

        elif abs(to_row - build_row) > 1:
            return False

        elif abs(to_col - build_col) > 1:
            return False

    def _check_player_occupied(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        returns True if a space being moved to is occupied by a different piece
        """
        player_positions = [self._x1_position, self._x2_position, self._o1_position, self._o2_position]
        if (to_row, to_col) in player_positions:
            return True

        player_positions = [self._x1_position, self._x2_position, self._o1_position, self._o2_position]

        # If space is not occupied by other player, we need to temporarily imagine moving our piece, so that our original location is available to build on
        # So we'll mutate the player_positions list with an updated position variable without actually changing a position variable
        i = 0 
        for position in player_positions:
            if position == (from_row, from_col):
                player_positions[i] = (to_row, to_col)
                break
            
            i += 1

        if (build_row, build_col) in player_positions:
            return True

    def _check_tower_level(self, from_row, from_col, to_row, to_col):
        """
        returns True if the height you're moving to less than your the tower height you're moving from is less than 2.
        returns False if diff is 2 or greater
        """
        from_sq_height = self._board[from_row][from_col]
        to_sq_height = self._board[to_row][to_col]

        if to_sq_height - from_sq_height < 2:
            return True

        else:
            return False

    def _can_build_tower(self, build_row, build_col):
        """
        Returns True if square player wants to build on is less than True
        False otherwise
        """
        build_sq_height = self._board[build_row][build_col]

        if build_sq_height < 4:
            return True

        else:
            return False

    def _set_current_state(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        sets the current state to X_WON or O_WON if the respective player piece lands on a tower level 3
        """
        if (from_row, from_col) == self._x1_position:
            self._x1_position = (to_row, to_col)

        elif (from_row, from_col) == self._x2_position:
            self._x2_position = (to_row, to_col)

        elif (from_row, from_col) == self._o1_position:
            self._o1_position = (to_row, to_col)

        elif (from_row, from_col) == self._o2_position:
            self._o2_position = (to_row, to_col)


        if self._board[to_row][to_col] >= 3:
            if self._player_turn == 'x':
                self._current_state = "X_WON"

            else:
                self._current_state = "O_WON"

        self._board[build_row][build_col] += 1

    def _check_legal_inputs(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        Compiles conditional methods above. Returns False if inputs are illegal
        """
        if self._current_state != "UNFINISHED":
            return False

        elif self._turn_count < 3:
            return False

        elif self._check_legal_range(from_row, from_col, to_row, to_col, build_row, build_col) == False:
            return False

        elif self._check_player_turn(from_row, from_col) == False:
            return False
        
        elif self._check_legal_move(from_row, from_col, to_row, to_col, build_row, build_col) == False:
            return False

        elif self._check_player_occupied(from_row, from_col, to_row, to_col, build_row, build_col) == True:
            return False

        elif self._check_tower_level(from_row, from_col, to_row, to_col) == False:
            return False

        elif self._can_build_tower(build_row, build_col) == False:
            return False


    def initial_placement(self, t1_row, t1_col, t2_row, t2_col, player):
        """
        Takes in a row and col input for both pieces a player intially places as well as a player value of x or o
        If conditions for intial placement are not met returns False
        Otherwise updates player pieces, increases turn_count, switches player_turn variables and returns True
        """
        if self._current_state != "UNFINISHED":
            return False

        if player not in ['x', 'o']:
            return False

        if player != self._player_turn:
            return False

        if self._turn_count > 2:
            return False

        if player == 'o':
            if (t1_row, t1_col) in (self._x1_position, self._x2_position):
                return False

            if (t2_row, t2_col) in (self._x1_position, self._x2_position):
                return False

        if (t1_row, t1_col) == (t2_row, t2_col):
            return False

        if 4 < t1_row or t1_row < 0:
            return False
        
        if 4 < t1_col or t1_col < 0:
            return False

        if 4 < t2_row or t2_row < 0:
            return False

        if 4 < t1_col or t1_col < 0:
            return False


        else:

            if player == "x": 
                self._x1_position = (t1_row, t1_col)
                self._x2_position = (t2_row, t2_col)

            elif player == "o":
                self._o1_position = (t1_row, t1_col)
                self._o2_position = (t2_row, t2_col)

            self._set_player_turn()
            self._turn_count += 1
            return True

    def make_move(self, from_row, from_col, to_row, to_col, build_row, build_col):
        """
        first calls _check_legal_inputs variable. If inputs are legal, calls the set_current state method, set_player_turn method and increase _turn_count variable
        """
        if self._check_legal_inputs(from_row, from_col, to_row, to_col, build_row, build_col) == False:
            return False

        else:
            
            self._set_current_state(from_row, from_col, to_row, to_col, build_row, build_col)
            self._set_player_turn()
            self._turn_count += 1

            return True

        


