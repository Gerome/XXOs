from unittest import TestCase

from BoardView import BoardView

EMPTY_INNER_BOARD ='┌───┬───┬───┐' '\n' \
                   '│ 1 │ 2 │ 3 │' '\n' \
                   '├───┼───┼───┤' '\n' \
                   '│ 4 │ 5 │ 6 │' '\n' \
                   '├───┼───┼───┤' '\n' \
                   '│ 7 │ 8 │ 9 │' '\n' \
                   '└───┴───┴───┘' '\n'

EMPTY_BOARD_TO_PRINT =   '┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n' \
                         '┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n' \
                         '┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                         '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                         '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n'

BOARD_WITH_ONE_CHAR ='┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n' \
                     '┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                     '│   │   │   ││ X │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n' \
                     '┌───┬───┬───┐┌───┬───┬───┐┌───┬───┬───┐' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '├───┼───┼───┤├───┼───┼───┤├───┼───┼───┤' '\n' \
                     '│   │   │   ││   │   │   ││   │   │   │' '\n' \
                     '└───┴───┴───┘└───┴───┴───┘└───┴───┴───┘' '\n' \

class BoardViewTests(TestCase):
    EMPTY_BOARD = [
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD],
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD],
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD]
    ]

    def setUp(self):
        self.boardView = BoardView()
        self.testBoard = self.EMPTY_BOARD

    def test_init_should_add_empty_board_to_board_view(self):
        self.assertEqual(BoardView.EMPTY_BOARD, self.boardView.boardViewString)

    def test_UpdateBoard_should_add_a_character_to_boardViewString(self):
        self.testBoard[1][1] = self.testBoard[1][1].replace('1', 'X')

        self.boardView.UpdateBoard(1, 1, 0, 0, 'X')

        self.assertEqual(self.testBoard, self.boardView.boardViewString)

    def test_PrintBoard_should_print_an_empty_board(self):
        self.assertEqual(EMPTY_BOARD_TO_PRINT, self.boardView.GetFormattedBoard())

    def test_PrintBoard_should_print_the_board_with_one_character(self):
        self.boardView.UpdateBoard(1, 1, 0, 0, 'X')

        self.assertEqual(BOARD_WITH_ONE_CHAR, self.boardView.GetFormattedBoard())


'''
Testlist
Z
O
M
B
I
E
'''
