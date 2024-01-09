from Rook import *
from Bishop import *
from Piece import *

class Queen():
    def __init__(self, team, x, y):
        super.__init__(team, x, y)

    def display(self):
        return "Q"

    def getValidMoves(self):
        validMoves = []
        validMoves.append(self.Bishop.getValidMoves())
        validMoves.append(self.Rook.getValidMoves())

        return validMoves
