from King import *
import Queen
import Rook
import Knight
from Bishop import *
from Pawn import *
from Board import *
import copy

class AI:
    def __init__(self, player, enemyPlayer):
        self.player = player
        self.enemyPlayer = enemyPlayer
        self.board = Board.board

    def findBestMove(self):
        aiPieces = self.player.getPieces()
        bestMove = []
        bestScore = -9999999

        for piece in aiPieces:
            pieceX, pieceY = piece.getX(), piece.getY()
            for moveX, moveY in piece.getValidMoves():
                newBoard = copy.deepcopy(self.board)
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
            

                if type(piece) is not int:
                    match piece.team_flag:
                        case "player2_flag":
                            aiPieces.append(piece)
                        case "player1_flag": 
                            enemyPieces.append(piece)
                        case _:
                            print("This piece was skipped: ", piece)

        print(aiPieces)
        print(enemyPieces)

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
        score += (aiPawns - enemyPawns) - 0.5 * (
                aiIsolatedPawns + aiBlockedPawns + aiDoubledPawns - enemyIsolatedPawns - enemyBlockedPawns - enemyDoubledPawns)
        score += 0.1 * (aiMobility - enemyMobility)

        return score

    @staticmethod
    def countOccurrencesOfPiece(pieceType, pieceList):
        count = 0
        for piece in pieceList:
            if piece == pieceType:
                count += 1
        return count

    # TODO: search by column not row as if a pawn is isolated, dont need to check adjacent columns
    #       similarly, if pawn isn't isolated, no need to check adjacent columns
    def isolatedPawns(self, player):
        isolatedPawns = 0
        for row in self.board:
            for piece in row:
                if isinstance(piece, Piece):
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
                                newPiece = self.board[i][columnLeft]
                                if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                    breakEarly = True
                                    break
                            if breakEarly:
                                continue

                        if columnRight < 8:
                            for i in range(0, 7):
                                newPiece = self.board[i][columnRight]
                                if isinstance(newPiece, Pawn) and player.isPlayerPiece(newPiece):
                                    isolated = False
                                    break
                        if isolated:
                            isolatedPawns += 1
            return isolatedPawns

    # TODO: FINISH FUNCTION (URGENT)
    def doubledPawns(self, player):
        doubledPawns = 0
        for row in self.board:
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
                            newPiece = self.board[x][i]
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
        for row in self.board:
            for piece in row:
                if isinstance(piece, Piece):
                    x, y = piece.getX(), piece.getY()
                    if isinstance(piece, Pawn) and player.isPlayerPiece(piece):
                        if y + 1 < 8:
                            if self.board[y + 1][x] != -1:
                                blockedPawns += 1
        return blockedPawns


'''
if len(piece.getValidMoves()) != 0:
    validMoves = piece.getValidMoves()
    for z in validMoves:
        moveX = z[0]
        moveY = z[1]
'''