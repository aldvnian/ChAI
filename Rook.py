from Board import *
from Piece import *
class Rook(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
    
    def display(self):
        return "R"

    def minX(self):
        x, y = self.getX(), self.getY()
        for a in range(x, -1, -1):
            if a - 1 < 0:
                return a
            currentSquare = Board.checkPiece(a - 1, y)
            if currentSquare != 0:  #square is not empty
                if not self.checkSameTeam(currentSquare):
                    return a - 1
                else:
                    return a
        return 0

    def maxX(self):
        x, y = self.getX(), self.getY()
        for b in range(x, 8):
            if b + 1 > 7:
                return b
            currentSquare = Board.checkPiece(b + 1, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return b + 1
                else:
                    return b
        return 7

    def minY(self):
        x, y = self.getX(), self.getY()
        for c in range(y, -1, -1):
            if c - 1 < 0:
                return c
            currentSquare = Board.checkPiece(x, c - 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return c - 1
                else:
                    return c
        return 0

    def maxY(self):
        x, y = self.getX(), self.getY()
        for d in range(y, 8):
            currentSquare = Board.checkPiece(x, d + 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return d + 1
                else:
                    return d
        return 7

    def getValidMoves(self):
        validMoves = []
        x, y = self.x, self.y
        maxX = self.maxX()
        maxY = self.maxY()
        minX = self.minX()
        minY = self.minY()

        for a in range(0, maxX):
            validMoves.append((a + 1, y))

        for b in range(0, maxY):
            validMoves.append((x, b + 1))

        for c in range(0, minX, -1):
            validMoves.append((c - 1, y))

        for d in range(0, minY, -1):
            validMoves.append((x, d - 1))

        return validMoves
