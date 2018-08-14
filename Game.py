from Board import Board
from BoardView import BoardView
from InnerBoard import InnerBoard
from NoughtCross import NoughtCross


class Game:

    gameIsFinished = False

    def start(self):

        innerBoards = [[InnerBoard(), InnerBoard(), InnerBoard()],
                       [InnerBoard(), InnerBoard(), InnerBoard()],
                       [InnerBoard(), InnerBoard(), InnerBoard()]]

        mainBoard = Board(innerBoards)
        boardView = BoardView()

        playerOneInput = input("Player 1, please input your symbol.\r\n")
        playerOneNoughtCross = NoughtCross(playerOneInput)

        playerTwoInput = input("Player 2, please input your symbol.\r\n")
        playerTwoNoughtCross = NoughtCross(playerTwoInput)

        playerCharacters = [playerOneNoughtCross, playerTwoNoughtCross]

        currentPlayer = 2
        playerSwitchValue = -1

        xBoard, yBoard = 1, 1

        while not self.gameIsFinished:
            currentPlayer += playerSwitchValue
            playerSwitchValue *= -1

            validMove = False

            while not validMove:
                print("Player {}'s go".format(currentPlayer))
                xInput = int(input("xCord\r\n"))
                yInput = int(input("yCord\r\n"))
                moveReturnValue = mainBoard.TakeTurn(xBoard, yBoard, xInput, yInput, playerCharacters[currentPlayer - 1])
                validMove = (moveReturnValue == InnerBoard.ERROR_NO_ERROR)

            boardView.UpdateBoard(xBoard,yBoard, xInput, yInput, playerCharacters[currentPlayer - 1].type)
            print(boardView.GetFormattedBoard())
            xBoard = xInput
            yBoard = yInput

