WINNING_COMBINATIONS = [
            # horizontal
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # vertical
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # crossed
            [(0,0), (1,1), (2,2)],
            [(2,0), (1,1), (0,2)]
            ]


class InnerBoard:

    ERROR_OCCUPIED = -1
    ERROR_NO_ERROR = 0

    numberOfSpaces = 9

    def __init__(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

    def NumberOfSpaces(self):
        return self.numberOfSpaces

    def TakeTurn(self, xPos, yPos, noughtCross):
        self.numberOfSpaces -= 1

        if self.board[xPos][yPos] != '.':
            return self.ERROR_OCCUPIED

        self.board[xPos][yPos] = noughtCross.type

        return self.ERROR_NO_ERROR

    def GetBoard(self):
        return self.board

    def HasBeenWon(self):
        for coordinates in WINNING_COMBINATIONS:
            letters = [self.board[x][y] for x, y in coordinates]

            # If all the letters match
            if "." not in letters:
                if len(set(letters)) <= 1:
                    return True

        return False
