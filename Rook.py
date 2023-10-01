from Board import *
from Piece import *
class Rook(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
    
    def display(self):
        return "R"

    def min_X(self):
        y = self.getY()
        for x in range(self.x - 1, -1, -1):
            currentSquare = Board.checkPiece(x, y)
            if currentSquare != 0:  #square is not empty
                    if not self.checkSameTeam(currentSquare):
                        return x
                    else:
                        return x + 1
        return 0

    def max_X(self):
        y = self.getY()
        for x in range(self.x + 1, 8):
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

    def max_y(self):
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
        x, y = self.x , self.y


        for a in range(y, 6):
            if y + 1 > 7:

            up = Board.checkPiece(x, a + 1)
            if up == 0:
                validMoves.append((x, a + 1))
            elif isinstance(up, Piece):
                validMoves.append((x, a + 1))

        for b in range(0, y):
            down = Board.checkPiece(x, b )
