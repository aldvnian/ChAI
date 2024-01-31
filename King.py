from Piece import *
from Board import *

class King(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
        self.team.king = self

    def display(self):
        return "I"

    def getValidMoves(self):
        validMoves = []
        x, y = self.getX(), self.getY()

        topRight = Board.checkPiece(x + 1, y + 1)
        if topRight == 0:   # if square is empty
            validMoves.append((x + 1, y + 1))
        elif isinstance(topRight, Piece):   # if square has a piece instance i.e is not out of bounds
            if not self.checkSameTeam(topRight):    # if piece instance is different team
                validMoves.append((x + 1, y + 1))

        topLeft = Board.checkPiece(x - 1, y + 1)
        if topLeft == 0:
            validMoves.append((x - 1, y + 1))
        elif isinstance(topLeft, Piece):
            if not self.checkSameTeam(topLeft):
                validMoves.append((x - 1, y + 1))

        up = Board.checkPiece(x, y + 1)
        if up == 0:
            validMoves.append((x, y + 1))
        elif isinstance(up, Piece):
            if not self.checkSameTeam(up):
                validMoves.append((x, y + 1))

        down = Board.checkPiece(x, y - 1)
        if down == 0:
            validMoves.append((x, y - 1))
        elif isinstance(down, Piece):
            if not self.checkSameTeam(down):
                validMoves.append((x, y - 1))

        left = Board.checkPiece(x - 1, y)
        if left == 0:
            validMoves.append((x - 1, y))
        elif isinstance(left, Piece):
            if not self.checkSameTeam(left):
                validMoves.append((x - 1, y))

        right = Board.checkPiece(x + 1, y)
        if right == 0:
            validMoves.append((x + 1, y))
        elif isinstance(right, Piece):
            if not self.checkSameTeam(right):
                validMoves.append((x + 1, y))
        return validMoves

    '''
    def castling(self, way, player):
        kingCoordinates = player.getKingCoordinates()
        kingX = kingCoordinates[0]
        if way == "left":
            for x in range(kingX, 0, -1):
                if isinstance(Board.board[x][0], Piece):
                    return
                else:
    '''