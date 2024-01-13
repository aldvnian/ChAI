import Board
from Rook import *
from Player import *
from Pawn import *
from Board import *
from King import *
from Bishop import *
from Queen import *


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

        playerOneKing = King(player1, 4, 0)
        playerTwoKing = King(player2, 4, 7)

        Board.addPiece(4, 0, playerOneKing)
        Board.addPiece(4, 7, playerTwoKing)

        playerOneBishop = Bishop(player1, 2, 0)
        playerOneBishop = Bishop(player1, 5, 0)
        playerTwoBishop = Bishop(player2, 2, 7)
        playerTwoBishop = Bishop(player2, 5, 7)

        Board.addPiece(2, 0, playerOneBishop)
        Board.addPiece(5, 0, playerOneBishop)
        Board.addPiece(2, 7, playerTwoBishop)
        Board.addPiece(5, 7, playerTwoBishop)

        playerOneRook = Rook(player1, 0, 0)
        playerOneRook = Rook(player1, 7, 0)
        playerTwoRook = Rook(player2, 0, 7)
        playerTwoRook = Rook(player2, 7, 7)

        Board.addPiece(0, 0, playerOneRook)
        Board.addPiece(7, 0, playerOneRook)
        Board.addPiece(0, 7, playerTwoRook)
        Board.addPiece(7, 7, playerTwoRook)

        playerOneQueen = Queen(player1, 3, 0)
        playerTwoQueen = Queen(player2, 3, 7)

        Board.addPiece(3, 0, playerOneQueen)
        Board.addPiece(3, 7, playerTwoQueen)

        Game.currentPlayer = player1
        Game.player1 = player1
        Game.player2 = player2

    @staticmethod
    def swap():
        if Game.currentPlayer == Game.player1:
            Game.currentPlayer = Game.player2
            print("Player2 now")
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
        piece = Board.checkPiece(Game.moveX, Game.moveY)
        if piece != 0:
            if Game.currentPlayer == Game.player1:
                Game.player2.removePiece(piece)
            else:
                Game.player1.removePiece(piece)
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

    def isInCheck(self):
        kingCoordinates = Game.currentPlayer.getKingCoordinates()
        possibleMoves = []
        if Game.currentPlayer == Game.player1:
            possibleMoves = Game.player2.findPossibleMoves()
        else:
            possibleMoves = Game.player1.findPossibleMoves()

        return kingCoordinates in possibleMoves

    def canKingMoveOutOfChecks(self):
        kingMoves = Game.currentPlayer.king.getValidMoves()
        possibleMoves = []
        if Game.currentPlayer == Game.player1:
            possibleMoves = Game.player2.findPossibleMoves()
        else:
            possibleMoves = Game.player1.findPossibleMoves()

        for x in kingMoves:
            if x not in possibleMoves:
                return True
        return False

    def allCheckingPieces(self):
        kingCoordinates = Game.currentPlayer.getKingCoordinates()
        if Game.currentPlayer == Game.player1:
            allPlayerPieces = Game.player2.pieces
        else:
            allPlayerPieces = Game.player1.pieces

        checkingPieces = []
        for piece in allPlayerPieces:
            validMoves = piece.getValidMoves()
            if kingCoordinates in validMoves:
                checkingPieces.append(piece)

        return checkingPieces

    def canBeBlocked(self, checkingPieces):
        possibleblocks = Game.currentPlayer.findPossibleMoves()
        for x in checkingPieces:
            for y in possibleblocks:
                if y in x.getValidMoves():
                    return True
        return False

    def checkmate(self):
        checkmate = False
        canBeBlocked = Game.currentPlayer.canBeBlocked()
        canKingMoveOutOfChecks = Game.currentPlayer.canKingMoveOutOfChecks()
        if canBeBlocked == False:
            if canKingMoveOutOfChecks == False:
                checkmate = True
        return checkmate

    # TODO: write a function which given a list of checking pieces returns true if all pieces can be blocked
    #       or false otherwise
    # I think only one piece can check you at once and when there is a double check, you must move your king.
    # The check can't be blocked, therefore I'm not sure if the allCheckingPieces() function is relevant
    # and the parameter for the canBeBlocked() function should just be a single checking piece
