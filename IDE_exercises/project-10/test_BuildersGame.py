import unittest
from BuildersGame import BuildersGame

class TestBuildersGame(unittest.TestCase):

    def test_builders_game(self):

        # No Errors, X Wins
        game_1 = BuildersGame()
        self.assertEqual(game_1.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_1.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_1.get_current_state(),"UNFINISHED")

        self.assertEqual(game_1.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game_1.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_1.get_current_state(),"UNFINISHED")

        self.assertEqual(game_1.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game_1.make_move(4,2,3,1,2,1),True)
        self.assertEqual(game_1.get_current_state(),"UNFINISHED")

        self.assertEqual(game_1.make_move(1,2,1,1,2,0),True)
        self.assertEqual(game_1.make_move(1,0,0,0,1,0),True)
        self.assertEqual(game_1.get_current_state(),"UNFINISHED")

        self.assertEqual(game_1.make_move(1,1,1,0,2,0),True)
        self.assertEqual(game_1.make_move(3,1,4,1,4,0),True)
        self.assertEqual(game_1.get_current_state(),"UNFINISHED")

        self.assertEqual(game_1.make_move(1,0,2,0,2,1),True)
        self.assertEqual(game_1.get_current_state(),"X_WON")

        # O plays after X Wins
        self.assertEqual(game_1.make_move(4,1,4,2,4,3),False)
        self.assertEqual(game_1.get_current_state(),"X_WON")

        # X plays after X Wins
        self.assertEqual(game_1.make_move(2,0,1,0,1,1),False)
        self.assertEqual(game_1.get_current_state(),"X_WON")

        # No errors, O wins
        game_2 = BuildersGame()
        self.assertEqual(game_2.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_2.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game_2.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game_2.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_2.make_move(1,1,2,1,1,1),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(1,0,0,0,0,1),True)
        self.assertEqual(game_2.make_move(2,1,1,0,0,1),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(1,2,1,3,1,4),True)
        self.assertEqual(game_2.make_move(1,0,1,1,1,0),True)
        self.assertEqual(game_2.get_current_state(),"UNFINISHED")

        self.assertEqual(game_2.make_move(1,3,1,4,1,3),True)
        self.assertEqual(game_2.make_move(1,1,2,0,1,1),True)
        self.assertEqual(game_2.get_current_state(),"O_WON")

        # X plays after O Wins
        self.assertEqual(game_2.make_move(1,3,2,4,1,3),False)
        self.assertEqual(game_2.get_current_state(),"O_WON")

        # O plays after X Wins
        self.assertEqual(game_2.make_move(1,0,2,0,1,0),False)
        self.assertEqual(game_2.get_current_state(),"O_WON")


        # Intiate X twice
        game_3 = BuildersGame()
        self.assertEqual(game_3.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_3.initial_placement(0,1,4,2,'x'),False)

        # Intiate O twice
        game_4 = BuildersGame()
        self.assertEqual(game_4.initial_placement(2,2,1,2,'o'),False)
        self.assertEqual(game_4.initial_placement(0,1,4,2,'o'),False)

        # Intiate out of Order
        game_5 = BuildersGame()
        self.assertEqual(game_5.initial_placement(2,2,1,2,'o'),False)
        self.assertEqual(game_5.initial_placement(0,1,4,2,'x'),True)

        # Intiate each twice
        game_6 = BuildersGame()
        self.assertEqual(game_6.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_6.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_6.initial_placement(2,2,1,2,'x'),False)
        self.assertEqual(game_6.initial_placement(0,1,4,2,'o'),False)

        # Make move before placement
        game_7 = BuildersGame()
        self.assertEqual(game_7.make_move(2,2,1,1,1,0),False)
        self.assertEqual(game_7.make_move(0,1,1,0,2,0),False)

        # Land on occupied space
        game_8 = BuildersGame()
        self.assertEqual(game_8.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game_8.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_8.get_current_state(),"UNFINISHED")

        self.assertEqual(game_8.make_move(4,4,4,3,4,4),True)
        self.assertEqual(game_8.make_move(0,1,0,0,1,0),False)
        self.assertEqual(game_8.get_current_state(),"UNFINISHED")

        # Land on intiated space
        game_9 = BuildersGame()
        self.assertEqual(game_9.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game_9.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_9.get_current_state(),"UNFINISHED")

        self.assertEqual(game_9.make_move(0,0,0,1,0,2),False)

        # Intiate on same space
        game_10 = BuildersGame()
        self.assertEqual(game_10.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game_10.initial_placement(4,4,0,1,'o'),False)
        self.assertEqual(game_10.get_current_state(),"UNFINISHED")

        # x2 piece intiates on x1 piece
        game_11 = BuildersGame()
        self.assertEqual(game_11.initial_placement(4,4,4,4,'x'),False)

        # o2 piece intiates on o1 piece
        game_12 = BuildersGame()
        self.assertEqual(game_12.initial_placement(4,4,0,0,'x'),True)
        self.assertEqual(game_12.initial_placement(1,1,1,1,'o'),False)
        self.assertEqual(game_12.get_current_state(),"UNFINISHED")

        # Intiate out of possible range
        game_13 = BuildersGame()
        self.assertEqual(game_13.initial_placement(4,5,0,0,'x'),False)
        self.assertEqual(game_13.initial_placement(4,4,-1,0,'x'),False)
        self.assertEqual(game_13.initial_placement(3,1,4,3,'x'),True)
        self.assertEqual(game_13.initial_placement(-2,5,4,2,'o'),False)
        self.assertEqual(game_13.initial_placement(2,5,5,2,'o'),False)
        self.assertEqual(game_13.initial_placement(2,4,4,2,'o'),True)

        # Try to build past 4 towers
        game_14 = BuildersGame()
        self.assertEqual(game_14.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_14.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game_14.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game_14.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_14.make_move(1,1,2,1,1,1),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(1,0,0,0,0,1),True)
        self.assertEqual(game_14.make_move(2,1,1,0,0,1),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(1,2,1,3,1,4),True)
        self.assertEqual(game_14.make_move(1,0,1,1,1,0),True)
        self.assertEqual(game_14.get_current_state(),"UNFINISHED")

        self.assertEqual(game_14.make_move(1,3,1,4,1,3),True)
        self.assertEqual(game_14.make_move(1,1,2,0,1,1),True)
        self.assertEqual(game_14.get_current_state(),"O_WON")

        # Build tower further than one square
        game_15 = BuildersGame()
        self.assertEqual(game_15.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_15.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_15.get_current_state(),"UNFINISHED")

        self.assertEqual(game_15.make_move(2,2,1,1,3,3),False)
        self.assertEqual(game_15.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game_15.make_move(0,1,1,0,2,2),False)
        self.assertEqual(game_15.get_current_state(),"UNFINISHED")

        # Build outside of board
        game_16 = BuildersGame()
        self.assertEqual(game_16.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game_16.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game_16.get_current_state(),"UNFINISHED")

        self.assertEqual(game_16.make_move(0,0,0,1,-1,0),False)
        self.assertEqual(game_16.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game_16.get_current_state(),"UNFINISHED")

        # Move out more than 1 square.
        game_17 = BuildersGame()
        self.assertEqual(game_17.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game_17.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game_17.get_current_state(),"UNFINISHED")

        self.assertEqual(game_17.make_move(0,0,2,1,1,1),False)
        self.assertEqual(game_17.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game_17.make_move(0,2,0,4,0,2),False)
        self.assertEqual(game_17.make_move(0,2,0,3,0,2),True)

        # Move out of possible range
        game_18 = BuildersGame()
        self.assertEqual(game_18.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game_18.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game_18.get_current_state(),"UNFINISHED")

        self.assertEqual(game_18.make_move(0,0,0,1,0,0),True)
        self.assertEqual(game_18.make_move(0,2,0,3,0,2),True)
        self.assertEqual(game_18.get_current_state(),"UNFINISHED")

        self.assertEqual(game_18.make_move(0,1,-1,1,0,1),False)
        self.assertEqual(game_18.make_move(0,1,0,0,0,1),True)
        self.assertEqual(game_18.make_move(0,3,-1,3,0,3),False)
        self.assertEqual(game_18.make_move(0,3,0,4,0,3),True)
        self.assertEqual(game_18.get_current_state(),"UNFINISHED")

        # Move non-existent piece\
        game_19 = BuildersGame()
        self.assertEqual(game_19.initial_placement(0,0,4,4,'x'),True)
        self.assertEqual(game_19.initial_placement(0,2,4,2,'o'),True)
        self.assertEqual(game_19.get_current_state(),"UNFINISHED")

        self.assertEqual(game_19.make_move(0,1,0,0,0,1),False)
        self.assertEqual(game_19.make_move(4,4,4,3,4,4),True)
        self.assertEqual(game_19.make_move(0,3,0,2,0,3),False)
        self.assertEqual(game_19.make_move(0,2,0,3,0,2),True)

        # Try to move to too tall a height
        game_20 = BuildersGame()
        self.assertEqual(game_20.initial_placement(2,2,1,2,'x'),True)
        self.assertEqual(game_20.initial_placement(0,1,4,2,'o'),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(2,2,1,1,1,0),True)
        self.assertEqual(game_20.make_move(0,1,1,0,2,0),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(1,1,0,1,1,1),True)
        self.assertEqual(game_20.make_move(4,2,3,1,2,1),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(1,2,1,1,2,0),True)
        self.assertEqual(game_20.make_move(1,0,0,0,1,0),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(1,1,1,0,2,0),True)
        self.assertEqual(game_20.make_move(3,1,4,1,4,0),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(1,0,1,1,2,0),True)
        self.assertEqual(game_20.make_move(4,1,3,1,4,0),True)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        self.assertEqual(game_20.make_move(1,1,2,0,1,1),False)
        self.assertEqual(game_20.get_current_state(),"UNFINISHED")

        # Move out of order
