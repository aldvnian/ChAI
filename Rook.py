from Board import *
from Piece import *
class Rook(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
    
    def display(self):
        return "R"

    def left(self):
        x, y = self.getX(), self.getY()
        for a in range(x - 1, -1, -1):
            currentSquare = Board.checkPiece(a, y)
            if currentSquare != 0:  #square is not empty
                    if not self.checkSameTeam(currentSquare):
                        return a
                    else:
                        return a + 1
        return 0

    def right(self):
        x, y = self.getX(), self.getY()
        for b in range(x + 1, 8):
            currentSquare = Board.checkPiece(b, y)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return b
                else:
                    return b - 1
        return 7

    def down(self):
        x, y = self.getX(), self.getY()
        for c in range(y - 1, -1, -1):
            currentSquare = Board.checkPiece(x, c)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    return c
                else:
                    return c + 1
        return 0

    def up(self):
        x, y = self.getX(), self.getY()
        for y in range(y + 1, 8):
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

        for e in range(y, up + 1):
            

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
