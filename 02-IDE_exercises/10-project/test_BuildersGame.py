import unittest
from BuildersGame import BuildersGame

class TestBuildersGame(unittest.TestCase):

    def test_no_illegal_moves_x_wins(self):

        # No Errors, X Wins
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game.make_move(4,2,3,1,2,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,2,1,1,2,0),True)
        self.assertEqual(game.make_move(1,0,0,0,1,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,1,0,2,0),True)
        self.assertEqual(game.make_move(3,1,4,1,4,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,0,2,0,2,1),True)
        self.assertEqual(game.get_current_state(),"X_WON")

        # O plays after X Wins
        self.assertEqual(game.make_move(4,1,4,2,4,3),False)
        self.assertEqual(game.get_current_state(),"X_WON")

        # X plays after X Wins
        self.assertEqual(game.make_move(2,0,1,0,1,1),False)
        self.assertEqual(game.get_current_state(),"X_WON")

    def test_no_illegal_moves_o_wins(self):
        # No errors, O wins
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.make_move(1,1,2,1,1,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,0,0,0,0,1),True)
        self.assertEqual(game.make_move(2,1,1,0,0,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,2,1,3,1,4),True)
        self.assertEqual(game.make_move(1,0,1,1,1,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,3,1,4,1,3),True)
        self.assertEqual(game.make_move(1,1,2,0,1,1),True)
        self.assertEqual(game.get_current_state(),"O_WON")

        # X plays after O Wins
        self.assertEqual(game.make_move(1,3,2,4,1,3),False)
        self.assertEqual(game.get_current_state(),"O_WON")

        # O plays after X Wins
        self.assertEqual(game.make_move(1,0,2,0,1,0),False)
        self.assertEqual(game.get_current_state(),"O_WON")

    def test_x_intiates_twice(self):
        # Intiate X twice
        game_3 = BuildersGame()
        self.assertEqual(game_3.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_3.initial_placement(0,1,4,2,'x'),False)
    
    def test_o_intiates_twice(self):
        # Intiate O twice
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'o'),False)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),False)
    
    def test_initate_out_of_order(self):
        # Intiate out of Order
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'o'),False)
        self.assertEqual(game.initial_placement(0,1,4,2,'x'),True)

    def test_initate_twice(self):
        # Intiate each twice
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),False)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),False)

    def test_initate_out_of_order(self):
        # Make move before placement
        game = BuildersGame()
        self.assertEqual(game.make_move(2,2,1,1,1,0),False)
        self.assertEqual(game.make_move(0,1,1,0,2,0),False)

    def test_land_on_occupied_space(self):
        # Land on occupied space
        game = BuildersGame()
        self.assertEqual(game.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(4,4,4,3,4,4),True)
        self.assertEqual(game.make_move(0,1,0,0,1,0),False)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_initate_out_of_order(self):
        # Land on intiated space
        game = BuildersGame()
        self.assertEqual(game.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,0,0,1,0,2),False)

    def test_initate_on_same_space(self):
        # Intiate on same space
        game = BuildersGame()
        self.assertEqual(game.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game.initial_placement(4,4,0,1,'o'),False)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_initate_x_on_x(self):
        # x2 piece intiates on x1 piece
        game = BuildersGame()    
        self.assertEqual(game.initial_placement(4,4,4,4,'x'),False)
    
    def test_initate_o_on_o(self):
        # o2 piece intiates on o1 piece
        game = BuildersGame()
        self.assertEqual(game.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game.initial_placement(1,1,1,1,'o'),False)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_initate_out_possible_range(self):
        # Intiate out of possible range
        game = BuildersGame()
        self.assertEqual(game.initial_placement(4,5,0,0,'x'),False)
        self.assertEqual(game.initial_placement(4,4,-1,0,'x'),False)
        self.assertEqual(game.initial_placement(3,1,4,3,'x'),True)
        self.assertEqual(game.initial_placement(-2,5,4,2,'o'),False)
        self.assertEqual(game.initial_placement(2,5,5,2,'o'),False)
        self.assertEqual(game.initial_placement(2,4,4,2,'o'),True)

    def test_build_past_4_levels(self):
        # Try to build past 4 towers
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.make_move(1,1,2,1,1,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,0,0,0,0,1),True)
        self.assertEqual(game.make_move(2,1,1,0,0,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,2,1,3,1,4),True)
        self.assertEqual(game.make_move(1,0,1,1,1,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,3,1,4,1,3),True)
        self.assertEqual(game.make_move(1,1,2,0,1,1),True)
        self.assertEqual(game.get_current_state(),"O_WON")

    def test_initate_out_of_order(self):
        # Build tower further than one square
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(2,2,1,1,3,3),False)
        self.assertEqual(game.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game.make_move(0,1,1,0,2,2),False)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_build_outside_of_board(self):
        # Build outside of board
        game = BuildersGame()
        self.assertEqual(game.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,0,0,1,-1,0),False)
        self.assertEqual(game.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_move_greater_than_one_square(self):
        # Move out more than 1 square.
        game = BuildersGame()
        self.assertEqual(game.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,0,2,1,1,1),False)
        self.assertEqual(game.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game.make_move(0,2,0,4,0,2),False)
        self.assertEqual(game.make_move(0,2,0,3,0,2),True)

    def test_move_out_of_possible_range(self):
        # Move out of possible range
        game = BuildersGame()
        self.assertEqual(game.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game.make_move(0,2,0,3,0,2),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,1,-1,1,0,1),False)
        self.assertEqual(game.make_move(0,1,0,0,0,1),True)
        self.assertEqual(game.make_move(0,3,-1,3,0,3),False)
        self.assertEqual(game.make_move(0,3,0,4,0,3),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

    def test_move_nonexistent_piece(self):
        # Move non-existent piece
        game = BuildersGame()
        self.assertEqual(game.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(0,1,0,0,0,1),False)
        self.assertEqual(game.make_move(4,4,4,3,4,4),True)
        self.assertEqual(game.make_move(0,3,0,2,0,3),False)
        self.assertEqual(game.make_move(0,2,0,3,0,2),True)

    def test_move_to_too_tall_a_tower(self):
        # Try to move to too tall a height
        game = BuildersGame()
        self.assertEqual(game.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game.make_move(4,2,3,1,2,1),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,2,1,1,2,0),True)
        self.assertEqual(game.make_move(1,0,0,0,1,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,1,0,2,0),True)
        self.assertEqual(game.make_move(3,1,4,1,4,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game.make_move(4,1,3,1,4,0),True)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

        self.assertEqual(game.make_move(1,1,2,0,1,1),False)
        self.assertEqual(game.get_current_state(),"UNFINISHED")

if __name__ == '__main__':
    unittest.main() 
