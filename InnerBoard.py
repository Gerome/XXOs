class InnerBoard:
    INNER_BOARD_HEIGHT = 3
    INNER_BOARD_WIDTH = 3

    numberOfSpaces = 9

    board = [['e', 'e', 'e'],
                  ['e', 'e', 'e'],
                  ['e', 'e', 'e']]

    def NumberOfSpaces(self):
        return self.numberOfSpaces

    def TakeTurn(self, xPos, yPos, noughtCross):
        self.numberOfSpaces -= 1
        self.board[xPos][yPos] = noughtCross

    def GetBoard(self):
        return self.board

