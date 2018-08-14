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


def __BoardPositionOutOfBounds__(xPos, yPos):
    return xPos > 2 or yPos > 2 or xPos < 0 or yPos < 0

class InnerBoard:
    ERROR_INVALID_POSITION = -2
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

        if __BoardPositionOutOfBounds__(xPos, yPos):
            return self.ERROR_INVALID_POSITION

        if self.board[xPos][yPos] != '.':
            return self.ERROR_OCCUPIED

        self.numberOfSpaces -= 1

        self.board[xPos][yPos] = noughtCross.type

        return self.ERROR_NO_ERROR

    def HasBeenWon(self):
        for coordinates in WINNING_COMBINATIONS:
            letters = [self.board[x][y] for x, y in coordinates]

            # If all the letters match
            if "." not in letters:
                if len(set(letters)) <= 1:
                    return True

        return False


