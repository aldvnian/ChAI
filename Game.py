import pygame

import Board
from Rook import *
from Player import *
from Pawn import *
from Board import *
from King import *
from Bishop import *
from Queen import *
from Knight import *


class Game:
    player1 = None
    player2 = None
    currentPlayer = None

    pieceX = None
    pieceY = None
    moveX = None
    moveY = None

    isCheck = False
    isCheckmate = False

    @staticmethod
    def __init__(player1, player2):
        Board.__init__(player1, player2)

        playerOneKing = King(player1, 4, 0)
        playerTwoKing = King(player2, 4, 7)

        Board.addPiece(4, 0, playerOneKing)
        Board.addPiece(4, 7, playerTwoKing)

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

        playerOneQueen = Queen(player1, 3, 0)
        playerTwoQueen = Queen(player2, 3, 7)

        Board.addPiece(3, 0, playerOneQueen)
        Board.addPiece(3, 7, playerTwoQueen)

        playerOneKnight = Knight(player1, 1, 0)
        Board.addPiece(1, 0, playerOneKnight)
        playerOneKnight = Knight(player1, 6, 0)
        Board.addPiece(6, 0, playerOneKnight)
        playerTwoKnight = Knight(player2, 1, 7)
        Board.addPiece(1, 7, playerTwoKnight)
        playerTwoKnight = Knight(player2, 6, 7)
        Board.addPiece(6, 7, playerTwoKnight)

        Game.player1 = player1
        Game.player2 = player2
        Game.currentPlayer = player1

    @staticmethod
    def swap():
        if Game.currentPlayer == Game.player1:
            Game.currentPlayer = Game.player2
            print("Player 2s turn now")
        else:
            print("Player 1s turn now")
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
        if isinstance(theSquare, Piece):
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
    def undoMove(piece):
        Board.movePiece(Game.moveX, Game.moveY, Game.pieceX, Game.pieceY) #move piece back to original position
        Board.addPiece(Game.moveX, Game.moveY, piece)

        if piece != 0:
            if Game.currentPlayer == Game.player1:
                Game.player2.addPiece(piece)
            else:
                Game.player1.addPiece(piece)

    @staticmethod
    def squares(screen, squareY):
        squareWidth = 700 / 8
        squareHeight = 700 / 8
        blackSquareX = squareWidth
        whiteSquareX = 2 * squareWidth
        Pieces, Coordinates = Board.isPiece(int(squareY / (700 / 8)))

        for blackRow in range(0, 4):
            blackSurface = pygame.Surface((squareWidth, squareHeight))
            blackSurfaceRect = blackSurface.get_rect(bottomright=(blackSquareX, squareY))
            blackSurface.fill('black')
            screen.blit(blackSurface, blackSurfaceRect)
            blackRowButtons = pieceButton((blackSquareX, squareY), squareWidth, squareHeight)
            blackRowButtons.apply(screen)
            blackSquareX += 2 * squareWidth

        for whiteRow in range(0, 4):
            whiteSurface = pygame.Surface((squareWidth, squareHeight))
            whiteSurfaceRect = whiteSurface.get_rect(bottomright=(whiteSquareX, squareY))
            whiteSurface.fill('gray')
            screen.blit(whiteSurface, whiteSurfaceRect)
            whiteRowButtons = pieceButton((blackSquareX, squareY), squareWidth, squareHeight)
            whiteRowButtons.apply(screen)
            whiteSquareX += 2 * squareWidth

        for x in range(0, len(Pieces)):
            index = piecesLink.index(Pieces[x])
            individualCoordinates = Coordinates[x]
            if Board.board[individualCoordinates[0]][individualCoordinates[1]] in Board.player1.pieces:
                whitePiece = whitePieces[index]
                whitePieceRect = whitePiece.get_rect(
                    bottomright=(squareWidth * (Coordinates[x][1] + 1), squareHeight * (Coordinates[x][0] + 1)))
                screen.blit(whitePiece, whitePieceRect)
            if Board.board[individualCoordinates[0]][individualCoordinates[1]] in Board.player2.pieces:
                blackPiece = blackPieces[index]
                blackPieceRect = blackPiece.get_rect(
                    bottomright=(squareWidth * (Coordinates[x][1] + 1), squareHeight * (Coordinates[x][0] + 1)))
                screen.blit(blackPiece, blackPieceRect)

    @staticmethod
    def squaresReverse(screen, squareY):
        squareWidth = 700 / 8
        squareHeight = 700 / 8
        blackSquareX = 2 * squareWidth
        whiteSquareX = squareWidth
        Pieces, Coordinates = Board.isPiece(int(squareY / (700 / 8)))

        for x in range(0, 4):
            whiteSurface = pygame.Surface((squareWidth, squareHeight))
            whiteSurface.fill('gray')
            whiteSurfaceRect = whiteSurface.get_rect(bottomright=(whiteSquareX, squareY))
            screen.blit(whiteSurface, whiteSurfaceRect)
            whiteRowButtons = pieceButton((blackSquareX, squareY), squareWidth, squareHeight)
            whiteRowButtons.apply(screen)
            whiteSquareX += 2 * squareWidth

        for y in range(0, 4):
            blackSurface = pygame.Surface((squareWidth, squareHeight))
            blackSurfaceRect = blackSurface.get_rect(bottomright=(blackSquareX, squareY))
            blackSurface.fill('black')
            screen.blit(blackSurface, blackSurfaceRect)
            blackRowButtons = pieceButton((blackSquareX, squareY), squareWidth, squareHeight)
            blackRowButtons.apply(screen)
            blackSquareX += 2 * squareWidth

        for x in range(0, len(Pieces)):
            index = piecesLink.index(Pieces[x])
            individualCoordinates = Coordinates[x]
            if Board.board[individualCoordinates[0]][individualCoordinates[1]] in Board.player1.pieces:
                whitePiece = whitePieces[index]
                whitePieceRect = whitePiece.get_rect(
                    bottomright=(squareWidth * (Coordinates[x][1] + 1), squareHeight * (Coordinates[x][0] + 1)))
                screen.blit(whitePiece, whitePieceRect)
            if Board.board[individualCoordinates[0]][individualCoordinates[1]] in Board.player2.pieces:
                blackPiece = blackPieces[index]
                blackPieceRect = blackPiece.get_rect(
                    bottomright=(squareWidth * (Coordinates[x][1] + 1), squareHeight * (Coordinates[x][0] + 1)))
                screen.blit(blackPiece, blackPieceRect)

    @staticmethod
    def displayBoard():
        screen = pygame.display.set_mode([700, 700])
        timer = pygame.time.Clock()
        fps = 60
        run = True
        screen.fill('gray')
        squaresY = 700 / 8
        squaresReverseY = (700 / 8) * 2
        pieceSelected = False

        for x in range(0, 4):
            Game.squares(screen, squaresY)
            Game.squaresReverse(screen, squaresReverseY)
            squaresY += 2 * (700 / 8)
            squaresReverseY += 2 * (700 / 8)

        while run:
            timer.tick(fps)

            if Game.isInCheck():
                print("In check!")
                Game.isCheck = True
                Game.isCheckmate = Game.checkmate()
            if Game.isCheckmate:
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pieceSelected:
                        piece = Board.checkPiece(Game.pieceX, Game.pieceY)
                        newX, newY = int(event.pos[0] // (700 / 8)), int(event.pos[1] // (700 / 8))
                        if (newX, newY) in piece.getValidMoves():
                            Game.moveX, Game.moveY = newX, newY
                            Game.move()
                            if Game.isInCheck():
                                Game.undoMove(piece)
                            else:
                                Game.swap()
                                pieceSelected = False
                                squaresY = 700 / 8
                                squaresReverseY = (700 / 8) * 2

                                for x in range(0, 4):
                                    Game.squares(screen, squaresY)
                                    Game.squaresReverse(screen, squaresReverseY)
                                    squaresY += 2 * (700 / 8)
                                    squaresReverseY += 2 * (700 / 8)

                    if not pieceSelected:
                        xCoordinate, yCoordinate = int(event.pos[0] // (700 / 8)), int(event.pos[1] // (700 / 8))
                        pieceAtPos = Board.checkPiece(xCoordinate, yCoordinate)
                        if isinstance(pieceAtPos, Piece):
                            if Game.currentPlayer.isPlayerPiece(pieceAtPos):
                                Game.pieceX, Game.pieceY = xCoordinate, yCoordinate
                                pieceSelected = True

            pygame.display.flip()
        pygame.quit()

    @staticmethod
    def doTurn():
        if Game.isInCheck():
            print("In check!")
            Game.isCheck = True
            Game.isCheckmate = Game.checkmate()
        if Game.isCheckmate:
            return
        #
        # selection = 0
        #
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         xCoordinate, yCoordinate = int(event.pos[0] // (700/8)), int(event.pos[1] // (700/8))
        #         print(xCoordinate, yCoordinate)
        #         position = (xCoordinate, yCoordinate)
        #         pieceAtPos = Board.checkPiece(xCoordinate, yCoordinate)
        #         print(pieceAtPos)
        #         if isinstance(pieceAtPos, Piece):
        #             if Game.currentPlayer.isPlayerPiece(pieceAtPos):
        #                 selection = Board.board.index(position)
        #                 Game.pieceX, Game.pieceY = xCoordinate, yCoordinate
        #                 print(selection)
        #         if (xCoordinate, yCoordinate) in pieceAtPos.getValidMoves and selection != 0:
        #             Game.moveX, Game.moveY = xCoordinate, yCoordinate
        #             print(Game.moveX, Game.moveY)
        #             Game.move()

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
        defendingPieces = Game.currentPlayer.getPieces()
        for defendingPiece in defendingPieces:
            if Game.doesBlock(checkingPiece, defendingPiece):
                return True
        return False

    # returns true if defending piece has a move which blocks the checking piece
    #       returns false otherwise
    @staticmethod
    def doesBlock(checkingPiece, defendingPiece):
        # DEFENDING PIECE TUPLE ERROR
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