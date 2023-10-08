from Board import *
from Piece import *
class Rook(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
    
    def display(self):
        return "R"

    def min_X(self):
        y = self.getY()
        for x in range(self.get - 1, -1, -1):
            currentSquare = Board.checkPiece(x, y)
            if currentSquare != 0:  #square is not empty
                    if not self.checkSameTeam(currentSquare):
                        return x
                    else:
                        return x + 1
        return 0

    def max_X(self):
        y = self.getY()
        for x in range(self.getX() + 1, 8):
            currentSquare = Board.checkPiece(x, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return x
                else:
                    return x - 1
        return 7

    def min_Y(self):
        x = self.getX()
        for y in range(self.getY() - 1, -1, -1):
            currentSquare = Board.checkPiece(x, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return y
                else:
                    return y + 1
        return 0

    def max_Y(self):
        x = self.getX()
        for y in range(self.getY() + 1, 8):
            currentSquare = Board.checkPiece(x, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return y
                else:
                    return y - 1
        return 7

    def getValidMoves(self):
        validMoves = []
        x, y = self.x, self.y

    #up#

        for a in range(y, self.max_Y()):
            up = Board.checkPiece(x, a)
            if up == 0:
                validMoves.append((x, a))
            elif isinstance(up, Piece):
                if not self.checkSameTeam(up):
                    validMoves.append((x, y))

    #down#

        for b in range(y, self.min_Y(), -1):
            down = Board.checkPiece(x, b)
            if down == 0:
                validMoves.append((x, b))
            elif isinstance(down, Piece):
                if not self.checkSameTeam(down):
                    validMoves.append((x, b))

    #left#

        for c in range(x, self.min_X(), -1):
            left = Board.checkPiece(c, y)
            if left == 0:
                validMoves.append((c, y))
            elif isinstance(left, Piece):
                if not self.checkSameTeam(left):
                    validMoves.append((c, y))

    #right#

        for d in range(x, self.max_X()):
            right = Board.checkPiece(d, y)
            if right == 0:
                validMoves.append((d, y))
            elif isinstance(right, Piece):
                if not self.checkSameTeam(right):
                    validMoves.append((d, y))