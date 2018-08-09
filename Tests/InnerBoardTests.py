from unittest import TestCase
from InnerBoard import InnerBoard
from NoughtCross import NoughtCross

emptyBoard = [['e', 'e', 'e'],
              ['e', 'e', 'e'],
              ['e', 'e', 'e']]


class InnerBoardTests(TestCase):

    def setUp(self):
        self.innerBoard = InnerBoard()

    def test_numberOfSpaces_should_show_all_positions_available(self):

        self.assertEqual(9, self.innerBoard.NumberOfSpaces())

    def test_take_turn_should_occupy_position_after_a_go(self):

        self.innerBoard.TakeTurn(0, 0, NoughtCross('X'))

        self.assertEqual(8, self.innerBoard.NumberOfSpaces())

    def test_get_board_should_return_empty_2D_array_representing_the_board(self):

        self.assertEqual(emptyBoard, self.innerBoard.GetBoard())

    def test_take_turn_should_occupy_place_on_the_board(self):

        cross = NoughtCross('X')
        self.innerBoard.TakeTurn(0, 0, cross)

        self.assertEqual(cross, self.innerBoard.board[0][0])

    def test_take_turn_should_another_occupy_place_on_the_board(self):

        nought = NoughtCross('O')
        self.innerBoard.TakeTurn(2, 2, nought)

        self.assertEqual(nought, self.innerBoard.board[2][2])


'''
TestList
-Z
-O
-M
-B
should_show_available_position_when_one_space_left
-I
should_return_no_error_by_default_after_a_go
-E
should_throw_error_when_attempting_to_occupy_unavailable_space
'''
