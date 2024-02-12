import King
import Queen
import Rook
import Knight
import Bishop
import Pawn


class AI:
    def __init__(self, player, enemyPlayer):
        self.player = player
        self.enemyPlayer = enemyPlayer

    def findBestMove(self, board):
        aiPieces = self.player.getPieces()
        bestMove = []
        bestScore = -9999999

        for piece in aiPieces:
            pieceX, pieceY = piece.getX(), piece.getY()
            for moveX, moveY in piece.getValidMoves():
                newBoard = board.copy()
                newBoard[pieceY][pieceX] = -1
                newBoard[moveX][moveY] = piece

                score = self.evaluation(newBoard)
                if score > bestScore:
                    bestScore = score
                    bestMove = [(pieceX, pieceY), (moveX, moveY)]
        return bestMove

    def evaluation(self, board):
        aiPieces = []
        enemyPieces = []
        for row in board:
            for piece in row:
                if piece == -1:
                    continue
                if self.player.isPlayerPiece(piece):
                    aiPieces.append(piece)
                else:
                    enemyPieces.append(piece)

        aiKings, enemyKings = self.countOccurencesOfPiece(King, aiPieces), self.countOccurencesOfPiece(King, enemyPieces)
        aiQueens, enemyQueens = self.countOccurencesOfPiece(Queen, aiPieces), self.countOccurencesOfPiece(Queen, enemyPieces)
        aiRooks, enemyRooks = self.countOccurencesOfPiece(Rook, aiPieces), self.countOccurencesOfPiece(Rook, enemyPieces)
        aiKnights, enemyKnights = self.countOccurencesOfPiece(Knight, aiPieces), self.countOccurencesOfPiece(Knight, enemyPieces)
        aiBishops, enemyBishops = self.countOccurencesOfPiece(Bishop, aiPieces), self.countOccurencesOfPiece(Bishop, enemyPieces)
        aiPawns, enemyPawns = self.countOccurencesOfPiece(Pawn, aiPieces), self.countOccurencesOfPiece(Pawn, enemyPieces)

        aiMobility = len([piece.getValidMoves() for piece in self.player.getPieces()])
        enemyMobility = len([piece.getValidMoves() for piece in self.enemyPlayer.getPieces()])

        aiIsolatedPawns = self.isolatedPawns(board, self.player)
        enemyIsolatedPawns = self.isolatedPawns(board, self.enemyPlayer)

        aiDoubledPawns = self.doubledPawns(board, self.player)
        enemyDoubledPawns = self.doubledPawns(board, self.player)

        aiBlockedPawns = self.blockedPawns(board, self.player)
        enemyBlockedPawns = self.blockedPawns(board, self.enemyPlayer)

        score = 200 * (aiKings - enemyKings) + 9 * (
                aiQueens - enemyQueens) + 5 * (
                aiRooks - enemyRooks) + 3 * (
                aiBishops + aiKnights - enemyBishops - enemyKnights)
        score += (aiPawns - enemyPawns) - 0.5 * (
                aiIsolatedPawns + aiBlockedPawns + aiDoubledPawns - enemyIsolatedPawns - enemyBlockedPawns - enemyDoubledPawns)
        score += 0.1 * (aiMobility - enemyMobility)

        return score


    def countOccurencesOfPiece(self, pieceType, pieceList):
        count = 0
        for piece in pieceList:
            if isinstance(piece, pieceType):
                count += 1
        return count

    # TODO: search by column not row as if a pawn is isolated, dont need to check adjacent columns
    #       similarly, if pawn isn't isolated, no need to check adjacent columns
    def isolatedPawns(self, board, player):
        isolatedPawns = 0
        for row in board:
            for piece in row:
                x, y = piece.getX(), piece.getY()
                if piece == -1:
                    continue
                if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                    columnLeft = x - 1
                    columnRight = x + 1
                    breakEarly = False
                    isolated = True

                    if columnLeft > -1:
                        for i in range(0, 7):
                            newPiece = board[i][columnLeft]
                            if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                breakEarly = True
                                break
                        if breakEarly: continue

                    if columnRight < 8:
                        for i in range(0, 7):
                            newPiece = board[i][columnRight]
                            if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                isolated = False
                                break
                    if isolated: isolatedPawns += 1
            return isolatedPawns

    # TODO: FINISH FUNCTION (URGENT)
    def doubledPawns(self, board, player):
        doubledPawns = 0
        for row in board:
            for piece in row:
                if piece == -1:
                    continue
                if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                    x, y = piece.getX(), piece.getY()
                    up = y + 1
                    breakEarly = False
                    doubledPawn = False

                if up < 8:
                    for i in range(0, 7):
                        newPiece = board[x][i]
                        if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                            doubledPawn = True
                            breakEarly = True
                            break
                    if breakEarly: continue
                if doubledPawn: doubledPawns += 1

        return doubledPawns




    def blockedPawns(self, board, player):
        blockedPawns = 0
        for row in board:
            for piece in row:
                x, y = piece.getX(), piece.getY()
                if isinstance(piece, Pawn) and self.player.isPlayerPiece(piece):
                    if board[y + 1][x] != -1:
                        blockedPawns += 1
        return blockedPawns


        if Game.currentPlayer == Game.player1:
            Game.getInput()
        else:
            engineBestMove = AI.findBestMove(Board.board)
            Game.pieceX, Game.pieceY, Game.moveX, Game.moveY = engineBestMove
            Game.move()