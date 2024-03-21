from King import *
from AI import *


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

    #Initialising all the pieces
        playerTwoKing = King(player2, 4, 0)
        playerOneKing = King(player1, 4, 7)
        
        Board.addPiece(4, 0, playerTwoKing)
        Board.addPiece(4, 7, playerOneKing)
        
        for x in range(0, 8):
            playerTwoPawn = Pawn(player2, x, 1)
            playerOnePawn = Pawn(player1, x, 6)
        
            Board.addPiece(x, 1, playerTwoPawn)
            Board.addPiece(x, 6, playerOnePawn)
        
        playerTwoBishop = Bishop(player2, 2, 0)
        Board.addPiece(2, 0, playerTwoBishop)
        playerTwoBishop = Bishop(player2, 5, 0)
        Board.addPiece(5, 0, playerTwoBishop)
        playerOneBishop = Bishop(player1, 2, 7)
        Board.addPiece(2, 7, playerOneBishop)
        playerOneBishop = Bishop(player1, 5, 7)
        Board.addPiece(5, 7, playerOneBishop)
        
        playerTwoRook = Rook(player2, 0, 0)
        Board.addPiece(0, 0, playerTwoRook)
        playerTwoRook = Rook(player2, 7, 0)
        Board.addPiece(7, 0, playerTwoRook)
        playerOneRook = Rook(player1, 0, 7)
        Board.addPiece(0, 7, playerOneRook)
        playerOneRook = Rook(player1, 7, 7)
        Board.addPiece(7, 7, playerOneRook)
        
        playerTwoQueen = Queen(player2, 3, 0)
        playerOneQueen = Queen(player1, 3, 7)
        
        Board.addPiece(3, 0, playerTwoQueen)
        Board.addPiece(3, 7, playerOneQueen)
        
        playerTwoKnight = Knight(player2, 1, 0)
        Board.addPiece(1, 0, playerTwoKnight)
        playerTwoKnight = Knight(player2, 6, 0)
        Board.addPiece(6, 0, playerTwoKnight)
        playerOneKnight = Knight(player1, 1, 7)
        Board.addPiece(1, 7, playerOneKnight)
        playerOneKnight = Knight(player1, 6, 7)
        Board.addPiece(6, 7, playerOneKnight)

    #Method that swaps the turn of the player
    @staticmethod
    def swap():
        if Game.currentPlayer == Game.player1:
            Game.currentPlayer = Game.player2
        else:
            Game.currentPlayer = Game.player1

    #Method that gets an input
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

    #Method that makes a move given the pieceX, pieceY, moveX and moveY
    @staticmethod
    def move():
        #print(f"game.pieceX: {Game.pieceX}, game.pieceY: {Game.pieceY}")
        #print(f"game.moveX: {Game.moveX}, game.moveY: {Game.moveY}")
        piece = Board.checkPiece(Game.moveX, Game.moveY)
        try:
            if piece != 0:
                if Game.currentPlayer == Game.player1:
                    Game.player2.removePiece(piece)
                else:
                    Game.player1.removePiece(piece)
        except Exception as e:
            print(len(Game.player1.pieces))
            print(len(Game.player2.pieces))
            Board.testing()
            print("ERROR")
            print(f"Current turn is {Game.currentPlayer.name}")
            print(f"The piece at {Game.pieceX}, {Game.pieceY} \ntried deleting piece at {Game.moveX}, {Game.moveY}")
            print(f"Piece belonged to {piece.team.name}")
            exit(1)
        Board.movePiece(Game.pieceX, Game.pieceY, Game.moveX, Game.moveY)

    #Method for undoing a move
    @staticmethod
    def undoMove(piece):
        Board.movePiece(Game.moveX, Game.moveY, Game.pieceX, Game.pieceY)  # move piece back to original position
        Board.addPiece(Game.moveX, Game.moveY, piece)

        if piece != 0:
            piece.team.addPiece(piece)


    #Method for creating one line of the chess board
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

    #Method for reversing the line
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

    #Method for creating the display and handling the running of the game
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
                Game.isCheck = True
                Game.isCheckmate = Game.checkmate()
            if Game.isCheckmate:
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    movePlaced = False
                    if pieceSelected:
                        newX, newY = int(event.pos[0] // (700 / 8)), int(event.pos[1] // (700 / 8))
                        newSquare = Board.checkPiece(newX, newY)
                        if (newX, newY) in pieceAtPos.getValidMoves():
                            Game.moveX, Game.moveY = newX, newY
                            if isinstance(pieceAtPos, Pawn):
                                pawnX, pawnY = pieceAtPos.getX(), pieceAtPos.getY()
                                if Game.moveY == pawnY + 2:
                                    pieceAtPos.canEnpassant()

                            Game.move()

                            if isinstance(pieceAtPos, King):
                                kingY = Game.currentPlayer.king.getY()
                                hasMoved = Game.currentPlayer.king.hasMoved

                                if newX == 2 and not hasMoved:
                                    if not pieceAtPos.hasCastled:
                                        Game.pieceX, Game.pieceY = 0, kingY
                                        Game.moveX, Game.moveY = 3, kingY
                                        Game.move()
                                        pieceAtPos.castled()
                                elif newX == 6 and not hasMoved:
                                    if not pieceAtPos.hasCastled:
                                        Game.pieceX, Game.pieceY = 7, kingY
                                        Game.moveX, Game.moveY = 5, kingY
                                        Game.move()
                                        pieceAtPos.castled()
                                else:
                                    Game.currentPlayer.king.kingMoved()

                            if Game.isInCheck():
                                if isinstance(newSquare, Piece):
                                    if Game.player1.isPlayerPiece(newSquare):
                                        Game.player1.addPiece(newSquare)
                                    else:
                                        Game.player2.addPiece(newSquare)
                                Board.movePiece(Game.moveX, Game.moveY, Game.pieceX, Game.pieceY)

                            squaresY = 700 / 8
                            squaresReverseY = (700 / 8) * 2

                            for x in range(0, 4):
                                Game.squares(screen, squaresY)
                                Game.squaresReverse(screen, squaresReverseY)
                                squaresY += 2 * (700 / 8)
                                squaresReverseY += 2 * (700 / 8)

                            else:
                                Game.swap()
                                Game.chessEngine = AI(Game.player2, Game.player1, Board, Game)
                                # score, engineBestPiece, engineBestMove = Game.chessEngine.minimax(3, True)
                                engineBestPiece = Game.chessEngine.findBestMove()
                                engineBestMove = Game.chessEngine.findBestMove()
                                Game.pieceX, Game.pieceY = engineBestPiece[0][0], engineBestPiece[0][1]
                                AIPiece = Board.checkPiece(Game.pieceX, Game.pieceY)
                                Game.moveX, Game.moveY = engineBestMove[1][0], engineBestMove[1][1]
                                if isinstance(AIPiece, Pawn):
                                    if Game.moveY == Game.pieceY - 2:
                                        AIPiece.canEnpassant()
                                Game.move()
                                if isinstance(AIPiece, King):
                                    AIKingY = Game.player2.king.getY()
                                    if Game.moveX == 2 and not Game.player2.king.hasMoved:
                                        if not AIPiece.hasCastled:
                                            Game.pieceX, Game.pieceY = 0, AIKingY
                                            Game.moveX, Game.moveY = 3, AIKingY
                                            Game.move()
                                            AIPiece.castled()
                                    elif Game.moveX == 6 and not Game.player2.king.hasMoved:
                                        if not AIPiece.hasCastled:
                                            Game.pieceX, Game.pieceY = 7, AIKingY
                                            Game.moveX, Game.moveY = 5, AIKingY
                                            Game.move()
                                            AIPiece.castled()
                                    else:
                                        Game.player2.king.kingMoved()

                                Game.swap()

                                squaresY = 700 / 8
                                squaresReverseY = (700 / 8) * 2

                                for x in range(0, 4):
                                    Game.squares(screen, squaresY)
                                    Game.squaresReverse(screen, squaresReverseY)
                                    squaresY += 2 * (700 / 8)
                                    squaresReverseY += 2 * (700 / 8)
                        pieceSelected = False
                        movePlaced = True

                    if not movePlaced:
                        if not pieceSelected:
                            xCoordinate, yCoordinate = int(event.pos[0] // (700 / 8)), int(event.pos[1] // (700 / 8))
                            pieceAtPos = Board.checkPiece(xCoordinate, yCoordinate)
                            if isinstance(pieceAtPos, Piece):
                                if Game.currentPlayer.isPlayerPiece(pieceAtPos):
                                    Game.pieceX, Game.pieceY = xCoordinate, yCoordinate
                                    pieceSelected = True

            pygame.display.flip()
        pygame.quit()

    #Method for checking if a player is in check
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

    #Method for checking if checkmate is delivered
    @staticmethod
    def checkmate():
        checkingPieces = Game.allCheckingPieces()

        if len(checkingPieces) == 1:
            canBeBlocked = Game.canBeBlocked(checkingPieces[0])
            if canBeBlocked:
                return False

        canKingMoveOutOfChecks = Game.canKingMoveOutOfChecks()

        if not canKingMoveOutOfChecks:
            return True
        return False
