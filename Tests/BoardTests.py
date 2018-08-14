from unittest import TestCase

from Board import Board
from InnerBoard import InnerBoard
from NoughtCross import NoughtCross

testInnerBoards = [[InnerBoard(), InnerBoard(), InnerBoard()],
                   [InnerBoard(), InnerBoard(), InnerBoard()],
                   [InnerBoard(), InnerBoard(), InnerBoard()]]


class BoardTests(TestCase):

    def setUp(self):
        self.board = Board(testInnerBoards)
        self.nought = NoughtCross('X')

    def test_should_fill_2d_array_with_InnersBoards(self):
        innerBoardClass = InnerBoard().__class__

        self.assertEqual(innerBoardClass, self.board.innerBoards[0][0].__class__)
        self.assertEqual(innerBoardClass, self.board.innerBoards[2][2].__class__)

    def test_takeTurn_should_call_take_turn_on_innerBoard(self):
        self.board.TakeTurn(0, 0, 0, 0, self.nought)

        self.assertEqual(testInnerBoards[0][0].board[0][0], self.nought.type)

    def test_takeTurn_should_return_error_when_passed_invalid_inner_board_positions(self):
        returnedError = self.board.TakeTurn(0, 0, 0, 3, self.nought)

        self.assertEqual(InnerBoard.ERROR_INVALID_POSITION, returnedError)

    def test_takeTurn_should_return_error_when_passed_invalid_board_positions(self):
        returnedError = self.board.TakeTurn(0, 3, 0, 0, self.nought)

        self.assertEqual(self.board.ERROR_INVALID_BOARD, returnedError)


'''
TestList
-Z
-O
-M
-B
-I
-E
'''