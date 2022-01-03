import unittest
from AddThreeGame import AddThreeGame

class TestAddThreeGame(unittest.TestCase):

    def test_no_errors_first_wins(self):
        # No Errors, First Wins
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 6), True)
        self.assertEqual(game.get_current_state(), "FIRST_WON")

    def test_no_errors_second_wins(self):
        # No Errors, Second Wins
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")
        
        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 9), True)
        self.assertEqual(game.get_current_state(), "SECOND_WON")

    def test_no_errors_draw(self):
        # No Errors, Draw
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")
        
        self.assertEqual(game.make_move("second", 8), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 6), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 4), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 9), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "DRAW")

    def test_out_of_order(self):
        # Out of Order
        game = AddThreeGame()
        self.assertEqual(game.make_move("second", 2), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 5), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 6), True)
        self.assertEqual(game.get_current_state(), "FIRST_WON")


    def test_repeat_values(self):
        # Repeat Values
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 2), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")
        
        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 5), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 9), True)
        self.assertEqual(game.get_current_state(), "SECOND_WON")

    def test_values_out_of_range(self):
        # Values out of range
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")
        
        self.assertEqual(game.make_move("second", 0), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", -1), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 4), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 100), False)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

    def test_play_after_game_finishes(self):
        # Plays after game is finished
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 6), True)
        self.assertEqual(game.get_current_state(), "FIRST_WON")

        self.assertEqual(game.make_move("second", 9), False)
        self.assertEqual(game.get_current_state(), "FIRST_WON")

    def test_player_1_wins_4_choices(self):
        # Player 1 wins after 4 choices
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 4), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 6), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 9), True)
        self.assertEqual(game.get_current_state(), "FIRST_WON")

    def test_player_2_wins_4_choices(self):
        # Player 2 wins after 4 choices
        game = AddThreeGame()
        self.assertEqual(game.make_move("first", 1), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 2), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 3), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 4), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 5), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 7), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("first", 8), True)
        self.assertEqual(game.get_current_state(), "UNFINISHED")

        self.assertEqual(game.make_move("second", 6), True)
        self.assertEqual(game.get_current_state(), "SECOND_WON")


if __name__ == '__main__':
    unittest.main()