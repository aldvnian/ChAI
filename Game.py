import Board
from Pawn import *
from Board import *
from King import *
class Game:
    player1 = None
    player2 = None
    currentPlayer = None

    pieceX = None
    pieceY = None
    moveX = None
    moveY = None

    runGame = True

    @staticmethod
    def __init__(player1, player2):
        Board.__init__(player1, player2)
        for x in range(0, 8):
            playerOnePawn = Pawn(player1, x, 1)
            playerTwoPawn = Pawn(player2, x, 6)

            Board.addPiece(x, 1, playerOnePawn)
            Board.addPiece(x, 6, playerTwoPawn)

        Board.addPiece(4, 0, King(player1, 4, 0))
        Board.addPiece(5, 7, King(player2, 3, 7))


        Game.currentPlayer = player1
        Game.player1 = player1
        Game.player2 = player2

    @staticmethod
    def swap():
        if Game.currentPlayer == Game.player1:
            Game.currentPlayer = Game.player2
        else:
            Game.currentPlayer = Game.player1

    @staticmethod
    def getInput():
        Game.pieceX = int(input("Enter your pieces x co-ordinate"))
        Game.pieceY = int(input("Enter your pieces y co-ordinate"))
        Game.moveX = int(input("Enter the x co-ordinate you wish to move to"))
        Game.moveY = int(input("Enter the y co-ordinate you wish to move to"))

    @staticmethod
    def validMove():
        theSquare = Board.checkPiece(Game.pieceX, Game.pieceY)
        if theSquare != 0:
            if not Game.currentPlayer.isPlayerPiece(theSquare):
                print("It is not your piece")
                return False
            if (Game.moveX, Game.moveY) in theSquare.getValidMoves():
                return True
            else:
                print("Invalid move for that piece!")
                return False
        else:
            print("No piece at that location!")
            return False

    @staticmethod
    def move():
        Board.movePiece(Game.pieceX, Game.pieceY, Game.moveX, Game.moveY)

    @staticmethod
    def doTurn():
        Board.displayBoard()
        Game.getInput()
        while not Game.validMove():
            Board.displayBoard()
            Game.getInput()
        Game.move()
        Game.swap()

