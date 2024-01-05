from Piece import *
from Board import *


class Bishop(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "B"

    def leftDown(self):
        x, y = self.getX(), self.getY()
        y = y - 1
        #while (0 <= x <= 8) and (0 <= y <= 8):
        for b in range(x - 1, -1, -1):
            if (b - 1 < 0) or (y - 1 < 0):
                return b
            currentSquare = Board.checkPiece(b, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return b
                else:
                    return b + 1
            y = y - 1
        return 0

    def rightDown(self):
        x, y = self.getX(), self.getY()
        y = y - 1
        #while (0 <= x <= 8) and (0 <= y <= 8):
        for b in range(x + 1, 8):
            if (b + 1 > 7) or (y - 1 < 0):
                return b
            currentSquare = Board.checkPiece(b, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return b
                else:
                    return b - 1
            y = y - 1
        return 7

    def leftUp(self):
        x, y = self.getX(), self.getY()
        y = y + 1
        #while (0 <= x <= 8) and (0 <= y <= 8):
        for a in range(x - 1, -1, -1):
            if (a - 1 < 0) or (y + 1 > 7):
                return a
            currentSquare = Board.checkPiece(a, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return a
                else:
                    return a + 1
            y = y + 1
        return 0

    def rightUp(self):
        x, y = self.getX(), self.getY()
        y = y + 1
        #while (0 <= x <= 8) and (0 <= y <= 8):
        for a in range(x + 1, 8):
            if (a + 1 > 7) or (y + 1 > 7):
            currentSquare = Board.checkPiece(a, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return a
                else:
                    return a - 1
            y = y + 1
        return 7

    def getValidMoves(self):
        x, y = self.getX(), self.getY()
        leftDown = self.leftDown()
        rightDown = self.rightDown()
        leftUp = self.leftUp()
        rightUp = self.rightUp()
        validMoves = []

        #leftUp#

        for a in range(x, -1, leftUp):
            validMoves.append((a - 1, y + 1))
            y += 1
        
        #rightUp#
        
        for b in range(x, rightUp):
            validMoves.append((b + 1, y + 1))
            y += 1

        #leftDown#

        for c in range(x, -1, leftDown):
            validMoves.append((c - 1, y - 1))
            y -= 1

        #rightDown#

        for d in range(x, leftUp):
            validMoves.append((d + 1, y - 1))
            y -= 1
        
        return validMoves
