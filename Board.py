

class Board:
    ERROR_INVALID_BOARD = -1

    def __init__(self, innerBoards):
        self.innerBoards = innerBoards

    def TakeTurn(self, boardX, boardY, xPos, yPos, noughtCross):

        if boardX > 2 or boardY > 2 or boardX < 0 or boardY < 0:
            return self.ERROR_INVALID_BOARD

        return self.innerBoards[boardX][boardY].TakeTurn(xPos, yPos, noughtCross)
