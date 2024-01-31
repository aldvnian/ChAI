from Piece import *
from Board import *


class Bishop(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "B"

    def leftDown(self):
        x, y = self.getX(), self.getY()
        # while (0 <= x <= 8) and (0 <= y <= 8):
        for b in range(x, -1, -1):
            if (b - 1 < 0) or (y - 1 < 0):
                return b
            currentSquare = Board.checkPiece(b - 1, y - 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return b - 1
                else:
                    return b
            y = y - 1
        return 0

    def rightDown(self):
        x, y = self.getX(), self.getY()
        # while (0 <= x <= 8) and (0 <= y <= 8):
        for b in range(x, 8):
            if (b + 1 > 7) or (y - 1 < 0):
                return b
            currentSquare = Board.checkPiece(b + 1, y - 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return b + 1
                else:
                    return b
            y = y - 1
        return 7

    def leftUp(self):
        x, y = self.getX(), self.getY()
        # while (0 <= x <= 8) and (0 <= y <= 8):
        for a in range(x, -1, -1):
            if (a - 1 < 0) or (y + 1 > 7):
                return a
            currentSquare = Board.checkPiece(a - 1, y + 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return a - 1
                else:
                    return a
            y = y + 1
        return 0

    def rightUp(self):
        x, y = self.getX(), self.getY()
        # while (0 <= x <= 8) and (0 <= y <= 8):
        for a in range(x, 8):
            if (a + 1 > 7) or (y + 1 > 7):
                return a
            currentSquare = Board.checkPiece(a + 1, y + 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return a + 1
                else:
                    return a
            y = y + 1
        return 7

    def getValidMoves(self):
        x, y = self.getX(), self.getY()
        leftDown = self.leftDown()
        rightDown = self.rightDown()
        leftUp = self.leftUp()
        rightUp = self.rightUp()
        validMoves = []

        # leftUp#

        for a in range(x, leftUp, -1):
            validMoves.append((a - 1, y + 1))
            y += 1

        x, y = self.getX(), self.getY()
        # rightUp#

        for b in range(x, rightUp):
            validMoves.append((b + 1, y + 1))
            y += 1

        x, y = self.getX(), self.getY()
        # leftDown#

        for c in range(x, leftDown, -1):
            validMoves.append((c - 1, y - 1))
            y -= 1

        x, y = self.getX(), self.getY()
        # rightDown#

        for d in range(x, rightDown):
            validMoves.append((d + 1, y - 1))
            y -= 1

        return validMoves
