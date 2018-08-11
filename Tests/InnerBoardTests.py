from unittest import TestCase
from InnerBoard import InnerBoard
from NoughtCross import NoughtCross

# the 'e' stands for empty
emptyBoard = [['.', '.', '.'],
              ['.', '.', '.'],
              ['.', '.', '.']]


class InnerBoardTests(TestCase):

    def setUp(self):
        self.innerBoard = InnerBoard()

    def test_numberOfSpaces_should_show_all_positions_available(self):
        self.assertEqual(9, self.innerBoard.NumberOfSpaces())

    def test_take_turn_should_a_occupy_position_after_a_go(self):
        self.innerBoard.TakeTurn(0, 0, NoughtCross('X'))

        self.assertEqual(8, self.innerBoard.NumberOfSpaces())

    def test_get_board_should_return_empty_2D_array_representing_the_board(self):
        self.assertEqual(emptyBoard, self.innerBoard.GetBoard())

    def test_take_turn_should_occupy_place_on_the_board(self):
        cross = NoughtCross('X')
        self.innerBoard.TakeTurn(0, 0, cross)

        self.assertEqual(cross.type, self.innerBoard.board[0][0])

    def test_take_turn_should_another_occupy_place_on_the_board(self):
        nought = NoughtCross('O')
        self.innerBoard.TakeTurn(2, 2, nought)

        self.assertEqual(nought.type, self.innerBoard.board[2][2])

    def test_HasBeenWon_should_return_false_by_default(self):
        self.assertEqual(False, self.innerBoard.HasBeenWon())

    def test_HasBeenWon_should_return_true_if_a_player_has_3_in_a_row(self):
        nought = NoughtCross('X')
        self.innerBoard.board[0][0] = nought.type
        self.innerBoard.board[1][0] = nought.type
        self.innerBoard.board[2][0] = nought.type

        self.assertEqual(True, self.innerBoard.HasBeenWon())

    def test_should_return_no_error_by_default(self):
        cross = NoughtCross('X')
        returnedError = self.innerBoard.TakeTurn(0, 0, cross)

        self.assertEqual(InnerBoard.ERROR_NO_ERROR, returnedError)

    def test_should_throw_error_when_attempting_to_occupy_unavailable_space(self):
        nought = NoughtCross('O')
        self.innerBoard.TakeTurn(2, 2, nought)
        returnedError = self.innerBoard.TakeTurn(2, 2, nought)

        self.assertEqual(InnerBoard.ERROR_OCCUPIED, returnedError)


'''
TestList
-Z
-O
-M
-B
-I
-E
'''
