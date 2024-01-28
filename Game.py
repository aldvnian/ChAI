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

    isCheckmate = False

    @staticmethod
    def __init__(player1, player2):
        Board.__init__(player1, player2)

        for x in range(0, 8):
            playerOnePawn = Pawn(player1, x, 1)
            playerTwoPawn = Pawn(player2, x, 6)

            Board.addPiece(x, 1, playerOnePawn)
            Board.addPiece(x, 6, playerTwoPawn)

        playerOneKing = King(player1, 4, 0)
        playerTwoKing = King(player2, 3, 7)

        Board.addPiece(4, 0, playerOneKing)
        Board.addPiece(3, 7, playerTwoKing)

        playerOneBishop = Bishop(player1, 2, 0)
        Board.addPiece(2, 0, playerOneBishop)
        playerOneBishop = Bishop(player1, 5, 0)
        Board.addPiece(5, 0, playerOneBishop)
        playerTwoBishop = Bishop(player2, 2, 7)
        Board.addPiece(2, 7, playerTwoBishop)
        playerTwoBishop = Bishop(player2, 5, 7)
        Board.addPiece(5, 7, playerTwoBishop)

        playerOneRook = Rook(player1, 0, 0)
        Board.addPiece(0, 0, playerOneRook)
        playerOneRook = Rook(player1, 7, 0)
        Board.addPiece(7, 0, playerOneRook)
        playerTwoRook = Rook(player2, 0, 7)
        Board.addPiece(0, 7, playerTwoRook)
        playerTwoRook = Rook(player2, 7, 7)
        Board.addPiece(7, 7, playerTwoRook)

        #playerOneQueen = Queen(player1, 3, 0)
        #playerTwoQueen = Queen(player2, 3, 7)

        #Board.addPiece(3, 0, playerOneQueen)
        #Board.addPiece(3, 7, playerTwoQueen)

        Game.player1 = player1
        Game.player2 = player2
        Game.currentPlayer = player1

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
        if Game.isInCheck():
            print("In check!")
            Game.isCheckmate = Game.checkmate()
        Board.displayBoard()
        if Game.isCheckmate:
            return
        Game.getInput()
        while not Game.validMove():
            Board.displayBoard()
            Game.getInput()
        Game.move()
        Game.swap()

    @staticmethod
    def isInCheck():
        kingCoordinates = Game.currentPlayer.getKingCoordinates()
        possibleMoves = []
        if Game.currentPlayer == Game.player1:
            possibleMoves = Board.findPossibleMoves(Game.player2.getPieces())
        else:
            possibleMoves = Board.findPossibleMoves(Game.player1.getPieces())

        return kingCoordinates in possibleMoves

    # return: True/False
    # purpose: To check if the king has any possible moves that can move it out of all the current check
    @staticmethod
    def canKingMoveOutOfChecks():
        kingMoves = Game.currentPlayer.king.getValidMoves()
        checkingPieces = Game.allCheckingPieces()
        for move in kingMoves:
            for checkingPiece in checkingPieces:
                if move in checkingPiece.getValidMoves():
                    break
                return True
        return False

    @staticmethod
    def allCheckingPieces():
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

    # return: True/False
    # purpose: To check if any piece can block the check on the king
    @staticmethod
    def canBeBlocked(checkingPiece):
        defendingPieces = Board.findPossibleMoves(Game.currentPlayer.getPieces())
        for defendingPiece in defendingPieces:
            if Game.doesBlock(checkingPiece, defendingPiece):
                return True
        return False

    # returns true if defending piece has a move which blocks the checking piece
    #       returns false otherwise
    @staticmethod
    def doesBlock(checkingPiece, defendingPiece):
        checkingX, checkingY = checkingPiece.getX(), checkingPiece.getY()
        kingX, kingY = Game.currentPlayer.getKingCoordinates()
        possibleMoves = defendingPiece.getValidMoves()

        xDifference = kingX - checkingX
        if xDifference == 0:
            for y in range(checkingY, kingY):
                if (y, y) in possibleMoves:
                    return True
        else:
            yDifference = kingY - checkingY
            if yDifference == 0:
                for x in range(checkingX, kingX):
                    if (x, kingY) in possibleMoves:
                        return True
            else:
                for x in range(checkingX, kingX):
                    if (x, x) in possibleMoves:
                        return True

        return False

    @staticmethod
    def checkmate():
        checkingPieces = Game.allCheckingPieces()

        if len(checkingPieces) == 1:
            canBeBlocked = Game.canBeBlocked(checkingPieces[0])
            if canBeBlocked:
                print("Check blocked!")
                return False

        canKingMoveOutOfChecks = Game.canKingMoveOutOfChecks()

        if not canKingMoveOutOfChecks:
            print("Checkmate!")
            return True
        print("King can move out of check!")
        return False
