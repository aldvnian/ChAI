from Board import *
from Piece import *
def Bishop(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "B"

    def leftDown(self):
        x, y = self.getX(), self.getY()
        y = y - 1
        while (x > 0 and x < 7) and (y > 0 and y < 7):
            for b in range(x - 1, -1, -1):
                currentSquare = Board.checkPiece(b, y)
                if currentSquare != 0:
                    if not self.checkSameTeam(currentSquare):
                        return b, y
                    else:
                        return b - 1, y
                y = y - 1
            return 7

    def rightDown(self):
        x, y = self.getX(), self.getY()
        y = y - 1
        while (x > 0 and x < 7) and (y > 0 and y < 7):
            for b in range(x + 1, 8):
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
        while (x > 0 and x < 7) and (y > 0 and y < 7):
            for a in range(x - 1, -1, -1):
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
        while (x > 0 and x < 7) and (y > 0 and y < 7):
            for a in range(x + 1, 8):
                currentSquare = Board.checkPiece(a, y)
                if currentSquare != 0:
                    if not self.checkSameTeam(currentSquare):
                        return a
                    else:
                        return a + 1
                y = y + 1
            return 0

    def getValidMoves(self):
        x, y = self.getX(), self.getY()
        validMoves = []

        # up#

        for a in range(y+1, 7):
            leftUp = Board.checkPiece(x, a)
            rightUp = Board.checkPiece()
            if up == 0:
                validMoves.append((x, a))
            elif isinstance(up, Piece):
                if not self.checkSameTeam(up):
                    validMoves.append((x, y))

        # down#

        for b in range(y, self.min_Y(), -1):
            down = Board.checkPiece(x, b)
            if down == 0:
                validMoves.append((x, b))
            elif isinstance(down, Piece):
                if not self.checkSameTeam(down):
                    validMoves.append((x, b))

        # left#

        for c in range(x, self.min_X(), -1):
            left = Board.checkPiece(c, y)
            if left == 0:
                validMoves.append((c, y))
            elif isinstance(left, Piece):
                if not self.checkSameTeam(left):
                    validMoves.append((c, y))

        # right#

        for d in range(x, self.max_X()):
            right = Board.checkPiece(d, y)
            if right == 0:
                validMoves.append((d, y))
            elif isinstance(right, Piece):
                if not self.checkSameTeam(right):
                    validMoves.append((d, y))
        return validMoves
