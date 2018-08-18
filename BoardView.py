


# source -> https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
def __nth_repl__(s, sub, repl, nth):
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
    # if i is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s


def __CalculatePosition__(xPos, yPos):
    numToReplace = str(((yPos * 3) + (xPos + 1)))
    return numToReplace


EMPTY_INNER_BOARD ='┌───┬───┬───┐' '\n' \
                   '│ 1 │ 2 │ 3 │' '\n' \
                   '├───┼───┼───┤' '\n' \
                   '│ 4 │ 5 │ 6 │' '\n' \
                   '├───┼───┼───┤' '\n' \
                   '│ 7 │ 8 │ 9 │' '\n' \
                   '└───┴───┴───┘' '\n'


def RemoveNumbersFromString(formattedBoard):
    for i in range(1, 10):
        formattedBoard = formattedBoard.replace(str(i), " ")

    return formattedBoard


class BoardView:

    EMPTY_BOARD = [
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD],
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD],
        [EMPTY_INNER_BOARD, EMPTY_INNER_BOARD, EMPTY_INNER_BOARD]
    ]

    boardViewString = ""

    def __init__(self):
        self.boardViewString = self.EMPTY_BOARD

    def UpdateBoard(self, xBoard, yBoard, xPos, yPos, playerChar):
        numToReplace = __CalculatePosition__(xPos, yPos)
        self.boardViewString[xBoard][yBoard] = self.boardViewString[xBoard][yBoard].replace(numToReplace, playerChar)

    def GetFormattedBoard(self):
        formattedBoard = ""

        for i in range(len(self.boardViewString)):
            for k in range(len(self.boardViewString[0][0].splitlines())):
                for j in range(len(self.boardViewString[i])):
                    formattedBoard += self.boardViewString[j][i].splitlines()[k]
                formattedBoard += "\n"

        return RemoveNumbersFromString(formattedBoard)


