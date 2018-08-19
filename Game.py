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

        overallBoard = InnerBoard()

        mainBoard = Board(innerBoards)
        boardView = BoardView()

        playerOneNoughtCross = NoughtCross(input("Player 1, please input your symbol.\r\n"))
        playerTwoNoughtCross = NoughtCross(input("Player 2, please input your symbol.\r\n"))

        playerCharacters = [playerOneNoughtCross, playerTwoNoughtCross]

        currentPlayer = 2
        playerSwitchValue = -1

        xBoard, yBoard = 1, 1

        print("Enter \"tl\" for the top left position.")

        while not self.gameIsFinished:

            print(boardView.GetFormattedBoard())

            currentPlayer += playerSwitchValue
            playerSwitchValue *= -1

            validMove = False


            while not validMove:
                print("Player {}'s go.".format(currentPlayer))

                userInput = input("Where do you want to go?\r\n").lower()

                if userInput.startswith('t'):
                    yInput = 0
                if userInput.startswith('m'):
                    yInput = 1
                if userInput.startswith('b'):
                    yInput = 2


                if userInput.endswith('l'):
                    xInput = 0
                if userInput.endswith('m'):
                    xInput = 1
                if userInput.endswith('r'):
                    xInput = 2

                moveReturnValue = mainBoard.TakeTurn(xBoard, yBoard, int(xInput), int(yInput), playerCharacters[currentPlayer - 1])
                validMove = (moveReturnValue == InnerBoard.ERROR_NO_ERROR)

                if not validMove:
                    print("INVALID MOVE!\r\n")

            boardView.UpdateBoard(xBoard, yBoard, xInput, yInput, playerCharacters[currentPlayer - 1].type)

            self.CheckForWin(currentPlayer, mainBoard, overallBoard, playerCharacters, xBoard, yBoard)

            if(self.gameIsFinished):
                print(boardView.GetFormattedBoard())
                print("Player {} wins!.".format(currentPlayer))


            xBoard = xInput
            yBoard = yInput

    def CheckForWin(self, currentPlayer, mainBoard, overallBoard, playerCharacters, xBoard, yBoard):
        if mainBoard.innerBoards[xBoard][yBoard].HasBeenWon():
            print("this board has been won'd")
            overallBoard.TakeTurn(xBoard, yBoard, playerCharacters[currentPlayer - 1])
            self.gameIsFinished = overallBoard.HasBeenWon()

