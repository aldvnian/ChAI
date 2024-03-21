import copy
from Game import *
from King import *
from Queen import *
from Rook import *
from Knight import *
from Bishop import *
from Pawn import *
from Board import *
from Piece import *

blackPawn = [[50, 50, 50, 50, 50, 50, 50, 50],
             [55, 60, 60, 30, 30, 60, 60, 55],
             [55, 45, 40, 50, 50, 40, 45, 55],
             [50, 50, 50, 70, 70, 50, 50, 50],
             [55, 55, 60, 25, 25, 60, 55, 55],
             [60, 60, 70, 80, 80, 70, 60, 60],
             [85, 85, 85, 85, 85, 85, 85, 85],
             [100, 100, 100, 100, 100, 100, 100, 100]]

blackKnight = [[0, 10, 20, 20, 20, 20, 10, 0],
               [10, 30, 50, 55, 55, 50, 30, 10],
               [20, 55, 65, 65, 65, 65, 55, 20],
               [20, 50, 65, 70, 70, 65, 50, 20],
               [20, 55, 65, 70, 70, 65, 55, 20],
               [20, 50, 60, 65, 65, 60, 50, 20],
               [10, 30, 50, 50, 50, 50, 30, 10],
               [0, 10, 20, 20, 20, 20, 10, 0]]

blackBishop = [[30, 40, 40, 40, 40, 40, 40, 30],
               [40, 55, 50, 50, 50, 50, 55, 40],
               [40, 60, 60, 60, 60, 60, 60, 40],
               [40, 50, 60, 60, 60, 60, 50, 40],
               [40, 55, 55, 60, 60, 55, 55, 40],
               [40, 50, 55, 60, 60, 55, 50, 40],
               [40, 50, 50, 50, 50, 50, 50, 40],
               [30, 40, 40, 40, 40, 40, 40, 30]]

blackRook = [[50, 50, 50, 55, 55, 50, 50, 50],
             [45, 50, 50, 50, 50, 50, 50, 45],
             [45, 50, 50, 50, 50, 50, 50, 45],
             [45, 50, 50, 50, 50, 50, 50, 45],
             [45, 50, 50, 50, 50, 50, 50, 45],
             [45, 50, 50, 50, 50, 50, 50, 45],
             [55, 60, 60, 60, 60, 60, 60, 55],
             [50, 50, 50, 50, 50, 50, 50, 50]]

blackQueen = [[30, 40, 40, 45, 45, 40, 40, 30],
              [40, 50, 55, 50, 50, 50, 50, 40],
              [40, 55, 55, 55, 55, 55, 50, 40],
              [50, 50, 55, 55, 55, 55, 50, 45],
              [45, 50, 55, 55, 55, 55, 50, 45],
              [40, 50, 55, 55, 55, 55, 50, 40],
              [40, 50, 50, 50, 50, 50, 50, 40],
              [30, 40, 40, 45, 45, 40, 40, 30]]

blackKing = [[70, 80, 60, 50, 50, 60, 80, 70],
             [70, 70, 50, 50, 50, 50, 70, 70],
             [40, 30, 30, 30, 30, 30, 30, 40],
             [30, 20, 20, 10, 10, 20, 20, 30],
             [20, 10, 10, 0, 0, 10, 10, 20],
             [20, 10, 10, 0, 0, 10, 10, 20],
             [20, 10, 10, 0, 0, 10, 10, 20],
             [20, 10, 10, 0, 0, 10, 10, 20]]

pieceSquareTable = [blackPawn, blackKnight, blackBishop, blackRook, blackQueen, blackKing]
pieceSquareTableLink = ['P', 'K', 'B', 'R', 'Q', 'I']


class AI:
    def __init__(self, player, enemyPlayer, board, game):
        self.player = player
        self.enemyPlayer = enemyPlayer
        self.board = board
        self.game = game


    def findBestMove(self):
        aiPieces = self.player.getPieces()
        bestMove = []
        bestScore = -9999999

        for piece in aiPieces:
            pieceX, pieceY = piece.getX(), piece.getY()
            for moveX, moveY in piece.getValidMoves():
                temp = self.board.checkPiece(moveX, moveY)
                self.board.movePiece(pieceX, pieceY, moveX, moveY)
                if self.game.isInCheck():
                    self.board.movePiece(moveX, moveY, pieceX, pieceY)
                    self.board.board[moveY][moveX] = temp
                    continue

                score = self.evaluation(self.board, None, None)
                if score > bestScore:
                    bestScore = score
                    bestMove = [(pieceX, pieceY), (moveX, moveY)]
                self.board.movePiece(moveX, moveY, pieceX, pieceY)
                self.board.board[moveY][moveX] = temp
        return bestMove

    def evaluation(self, board, pieceMoves, pieceCoords):
        aiPieces = []
        enemyPieces = []
        if pieceMoves is not None:
            piece = Board.checkPiece(pieceMoves[0], pieceMoves[1])
            # print('Here are the coordinates of the move:', (pieceMoves[0], pieceMoves[1]))
            displayOfPiece = piece.display()
            indexOfPiece = pieceSquareTableLink.index(displayOfPiece)
            positionTable = pieceSquareTable[indexOfPiece]
            positionValue = positionTable[pieceMoves[1]][pieceMoves[0]]
            positionValueBefore = positionTable[pieceCoords[1]][pieceCoords[0]]
            # print(f'For piece: {displayOfPiece},\nMoves: ({pieceMoves[0]}, {pieceMoves[1]})')
            # print(f'Position Value: {positionValue}')
        for row in board.board:
            for piece in row:
                if isinstance(piece, Piece):
                    if piece.team_flag == 'player2_flag':
                        aiPieces.append(piece)
                    elif piece.team_flag == "player1_flag":
                        enemyPieces.append(piece)

        aiKings, enemyKings = self.countOccurrencesOfPiece(King, aiPieces), self.countOccurrencesOfPiece(King,
                                                                                                         enemyPieces)
        aiQueens, enemyQueens = self.countOccurrencesOfPiece(Queen, aiPieces), self.countOccurrencesOfPiece(Queen,
                                                                                                            enemyPieces)
        aiRooks, enemyRooks = self.countOccurrencesOfPiece(Rook, aiPieces), self.countOccurrencesOfPiece(Rook,
                                                                                                         enemyPieces)
        aiKnights, enemyKnights = self.countOccurrencesOfPiece(Knight, aiPieces), self.countOccurrencesOfPiece(Knight,
                                                                                                               enemyPieces)
        aiBishops, enemyBishops = self.countOccurrencesOfPiece(Bishop, aiPieces), self.countOccurrencesOfPiece(Bishop,
                                                                                                               enemyPieces)
        aiPawns, enemyPawns = self.countOccurrencesOfPiece(Pawn, aiPieces), self.countOccurrencesOfPiece(Pawn,
                                                                                                         enemyPieces)

        aiMobility = len([piece.getValidMoves() for piece in self.player.getPieces()])
        enemyMobility = len([piece.getValidMoves() for piece in self.enemyPlayer.getPieces()])

        aiIsolatedPawns = self.isolatedPawns(self.player)
        enemyIsolatedPawns = self.isolatedPawns(self.enemyPlayer)

        aiDoubledPawns = self.doubledPawns(self.player)
        enemyDoubledPawns = self.doubledPawns(self.player)

        aiBlockedPawns = self.blockedPawns(self.player)
        enemyBlockedPawns = self.blockedPawns(self.enemyPlayer)

        score = 200 * (aiKings - enemyKings) + 9 * (
                aiQueens - enemyQueens) + 5 * (
                        aiRooks - enemyRooks) + 3 * (
                        aiBishops + aiKnights - enemyBishops - enemyKnights)
        score += (aiPawns - enemyPawns) - 0.2 * (
                aiIsolatedPawns + aiBlockedPawns + aiDoubledPawns - enemyIsolatedPawns - enemyBlockedPawns - enemyDoubledPawns)
        score += 0 * (aiMobility - enemyMobility)
        if pieceCoords is not None:
            # print(f'For piece: {displayOfPiece} \n Move before: {pieceCoords[0], pieceCoords[1]} \n Score+:'
            #       f' {positionValue - positionValueBefore}')
            score += 0.02 * (positionValue - positionValueBefore)

        return score

    @staticmethod
    def countOccurrencesOfPiece(pieceType, pieceList):
        count = 0
        for piece in pieceList:
            if isinstance(piece, pieceType):
                count += 1
        return count

    # TODO: search by column not row as if a pawn is isolated, dont need to check adjacent columns
    #       similarly, if pawn isn't isolated, no need to check adjacent columns
    def isolatedPawns(self, player):
        isolatedPawns = 0
        for row in self.board.board:
            for piece in row:
                if isinstance(piece, Piece):
                    x, y = piece.getX(), piece.getY()
                    if piece == 0:
                        continue
                    if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                        columnLeft = x - 1
                        columnRight = x + 1
                        breakEarly = False
                        isolated = True

                        if columnLeft > -1:
                            for i in range(0, 7):
                                newPiece = self.board.board[i][columnLeft]
                                if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                    breakEarly = True
                                    break
                            if breakEarly:
                                continue

                        if columnRight < 8:
                            for i in range(0, 7):
                                newPiece = self.board.board[i][columnRight]
                                if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                    isolated = False
                                    break
                        if isolated:
                            isolatedPawns += 1
            return isolatedPawns

    def doubledPawns(self, player):
        doubledPawns = 0
        for row in self.board.board:
            for piece in row:
                if piece == 0:
                    continue
                if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                    x, y = piece.getX(), piece.getY()
                    up = y + 1
                    breakEarly = False
                    doubledPawn = False

                    if up < 8:
                        for i in range(0, 7):
                            newPiece = self.board.board[x][i]
                            if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                doubledPawn = True
                                breakEarly = True
                                break
                        if breakEarly:
                            continue
                    if doubledPawn:
                        doubledPawns += 1

        return doubledPawns

    def blockedPawns(self, player):
        blockedPawns = 0
        for row in self.board.board:
            for piece in row:
                if isinstance(piece, Piece):
                    x, y = piece.getX(), piece.getY()
                    if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                        if y + 1 < 8:
                            if self.board.board[y + 1][x] != 0:
                                blockedPawns += 1
        return blockedPawns

    def findAllMoves(self, selectedPlayer):
        pieces = selectedPlayer.getPieces()
        allMoves = []

        for piece in pieces:
            validMove = piece.getValidMoves()
            pieceX, pieceY = piece.getX(), piece.getY()

            for moves in validMove:
                allMoves.append([(pieceX, pieceY), moves])

            print(f"All moves for {type(piece)} at ({pieceX}, {pieceY}):")
            print()
        return allMoves

    def minimax(self, depth, maxPlayer):
        checkmate = False
        bestMove = None
        bestPiece = None
        if self.game.isInCheck():
            checkmate = self.game.checkmate()

        if checkmate or depth == 0:
            evaluation = self.evaluation(self.board, (self.game.moveX, self.game.moveY),
                                         (self.game.pieceX, self.game.pieceY))
            return evaluation, None, None

        if maxPlayer:
            maxEval = -99999999

            pieces = self.player.getPieces()
            for piece in pieces:
                pieceX, pieceY = piece.getX(), piece.getY()

                firstMove = None
                if type(piece) == Pawn:
                    firstMove = piece.hasMoved

                possibleMoves = piece.getValidMoves()
                for move in possibleMoves:
                    self.game.pieceX, self.game.pieceY = pieceX, pieceY
                    self.game.moveX, self.game.moveY = move
                    undoPiece = Board.checkPiece(move[0], move[1])

                    self.game.move()
                    self.game.swap()

                    evaluation, aPiece, aMove = self.minimax(depth - 1, not maxPlayer)
                    self.game.pieceX, self.game.pieceY = pieceX, pieceY
                    self.game.moveX, self.game.moveY = move

                    if type(piece) == Pawn:
                        piece.hasMoved = firstMove

                    self.game.undoMove(undoPiece)
                    self.game.swap()

                    if evaluation > maxEval:
                        bestMove = move
                        bestPiece = piece
                        maxEval = evaluation

            return maxEval, (bestPiece.getX(), bestPiece.getY()), bestMove

        else:
            minEval = 99999999

            pieces = self.enemyPlayer.getPieces()
            for piece in pieces:
                pieceX, pieceY = piece.getX(), piece.getY()

                firstMove = None
                if type(piece) == Pawn:
                    firstMove = piece.hasMoved

                possibleMoves = piece.getValidMoves()
                for move in possibleMoves:
                    self.game.pieceX, self.game.pieceY = pieceX, pieceY
                    self.game.moveX, self.game.moveY = move
                    undoPiece = Board.checkPiece(move[0], move[1])

                    self.game.move()
                    self.game.swap()

                    evaluation, aPiece, aMove = self.minimax(depth - 1, not maxPlayer)
                    self.game.pieceX, self.game.pieceY = pieceX, pieceY
                    self.game.moveX, self.game.moveY = move

                    if type(piece) == Pawn:
                        piece.hasMoved = firstMove

                    self.game.undoMove(undoPiece)
                    self.game.swap()

                    if evaluation < minEval:
                        bestMove = move
                        bestPiece = piece
                        minEval = evaluation

            return minEval, (bestPiece.getX(), bestPiece.getY()), bestMove
