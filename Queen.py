from Player import *
from Rook import *
from Board import *

class Queen(Piece):
    def __init__(self, team, x, y):
        super.__init__(team, x, y)

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
    
    def getValidMoves(self):
        ValidMoves = []
        

    def display(self):
        return 'Q'
